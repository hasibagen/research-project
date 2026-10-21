"""Small local record adapter. Run with a conda-managed Python."""
import argparse, contextlib, fcntl, hashlib, json, math, os, tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
START, END = '<!-- research-results:start -->', '<!-- research-results:end -->'

def absolute(value):
    p = Path(value)
    if not p.is_absolute(): raise ValueError('需要绝对路径: ' + str(p))
    return p.resolve()

def dump(value): return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def atomic(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=p.parent, prefix='.record-')
    with os.fdopen(fd, 'w') as f:
        f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, p)

@contextlib.contextmanager
def lock(p):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield

def artifact(root, rel):
    p = (root / rel).resolve()
    if Path(rel).is_absolute() or not p.is_relative_to(root): raise ValueError('材料越界')
    if not p.is_file(): raise ValueError('材料不存在: ' + str(p))
    return p

def validate(record, root):
    import jsonschema
    version=record.get('schema_version')
    if type(version) is not int or version not in (1,2): raise ValueError('不支持的 schema_version')
    schema='run-v1.schema.json' if version==1 else 'run.schema.json'
    jsonschema.validate(record, json.loads((BASE/'assets/templates'/schema).read_text()))
    if record['status']=='failed' and record['results']: raise ValueError('失败记录不能包含科学指标')
    if record['status']=='failed' and record['checks']=='passed': raise ValueError('失败执行不能验收通过')
    combos = [r['combo'] for r in record['results']]
    if len(combos)!=len(set(combos)): raise ValueError('组合身份重复')
    for r in record['results']:
        if any(not math.isfinite(v) for v in r['metrics'].values()): raise ValueError('指标必须有限')
    paths = [a['path'] for a in record['artifacts']]
    if any(x in {'ro-crate-metadata.json','ro-crate-preview.html','run-record.json'} for x in paths): raise ValueError('材料使用导出保留名称')
    if len(paths)!=len(set(paths)): raise ValueError('材料重复')
    for ref in [record.get('machine',{}).get('env_ref'),record.get('randomness',{}).get('design_ref')]:
        if ref is not None and ref not in paths: raise ValueError('来源引用必须登记到 artifacts: '+ref)
    for a in record['artifacts']:
        if sha(artifact(root,a['path']))!=a['sha256']: raise ValueError('材料哈希不匹配: '+a['path'])

def append(record_path, root, registry):
    record=json.loads(record_path.read_text()); validate(record,root)
    with lock(registry.with_suffix(registry.suffix+'.lock')):
        records=json.loads(registry.read_text()) if registry.exists() else []
        for old in records:
            if old['run_id']==record['run_id']:
                if old!=record: raise ValueError('同一 run 身份内容冲突；原记录和来件均保留')
                return False
        records.append(record); atomic(registry,dump(records))
    return True

def render(registry, page, question):
    records=json.loads(registry.read_text())
    with lock(page.with_suffix(page.suffix+'.lock')):
        text=page.read_text()
        if text.count(START)!=1 or text.count(END)!=1 or text.index(START)>text.index(END): raise ValueError('自动区标记无效')
        def cell(v): return str(v).replace('|','\\|').replace('\n',' ')
        lines=['| Run | 修订 | 组合 | 指标 | 状态／检查 |','|---|---|---|---|---|']
        for r in records:
            if r['question']!=question: continue
            for result in r['results'] or [{'combo':'—','metrics':{}}]:
                lines.append('| '+' | '.join(map(cell,[r['run_id'],r['revision'],result['combo'],json.dumps(result['metrics'],ensure_ascii=False),r['status']+'/'+r['checks']]))+' |')
        atomic(page,text.split(START)[0]+START+'\n'+'\n'.join(lines)+'\n'+END+text.split(END)[1])

def export(record_path, root, dest, license_uri):
    from rocrate.rocrate import ROCrate
    r=json.loads(record_path.read_text()); validate(r,root)
    dest.mkdir(parents=True,exist_ok=False)
    crate=ROCrate()
    crate.name='Research run '+r['run_id']
    crate.description='Recorded execution materials; scientific interpretation is maintained separately.'
    crate.license=license_uri
    # Real projects must set and check their own license before release.
    for a in r['artifacts']:
        crate.add_file(artifact(root,a['path']),dest_path=a['path'],properties={'sha256':a['sha256']})
    crate.add_file(record_path,dest_path='run-record.json')
    crate.write(dest)
    for a in r['artifacts']:
        if sha(artifact(dest,a['path']))!=a['sha256']: raise ValueError('导出完整性失败')
    return dest

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='command',required=True)
    for name in ['append','export']:
        q=sub.add_parser(name);q.add_argument('--record',type=absolute,required=True);q.add_argument('--root',type=absolute,required=True)
        q.add_argument('--registry' if name=='append' else '--dest',type=absolute,required=True)
        if name=='export': q.add_argument('--license',required=True,help='已核对的材料许可 URI')
    q=sub.add_parser('render');q.add_argument('--registry',type=absolute,required=True);q.add_argument('--page',type=absolute,required=True);q.add_argument('--question',required=True)
    a=p.parse_args()
    if a.command=='append': print('added' if append(a.record,a.root,a.registry) else 'unchanged')
    elif a.command=='render': render(a.registry,a.page,a.question)
    else: print(export(a.record,a.root,a.dest,a.license))
if __name__=='__main__': main()
