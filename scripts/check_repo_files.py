"""Read-only 5 MB gate for Git / colocated jj candidates and Git index blobs.
Does not snapshot jj, mutate the index, audit history, or install hooks.
"""
import argparse,json,os,subprocess
from pathlib import Path
LIMIT=5_000_000

def git(root,*args,input=None):
 return subprocess.run(['git','-C',str(root),*args],input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout

def audit(root):
 root=Path(root).resolve()
 # Avoid treating a parent repository as the requested project's repository.
 if not (root/'.git').exists():
  return {'passed':False,'errors':['未完成检查：需要项目根的 Git 或 colocated jj 仓库；未初始化或非 colocated jj 须另行核对。'],'oversized':[],'limit_bytes':LIMIT}
 errors=[];large=[];count=0
 try:
  names=set(git(root,'ls-files','--cached','--others','--exclude-standard','-z').split(b'\0'))-{b''}
  for raw in sorted(names):
   name=os.fsdecode(raw);p=root/name
   if p.is_symlink():continue # Git stores the link text, not the referenced dataset.
   try:
    if p.is_file():
     count+=1;size=p.stat().st_size
     if size>LIMIT:large.append({'path':name,'bytes':size,'source':'working-copy'})
   except OSError as exc:errors.append(f'{name}: {exc}')
  records=[]
  for entry in git(root,'ls-files','--stage','-z').split(b'\0'):
   if not entry:continue
   meta,name=entry.split(b'\t',1);mode,oid,stage=meta.split()
   if mode==b'160000':continue # Submodule commit is not a file blob.
   records.append((oid,os.fsdecode(name),stage.decode()))
  oids=sorted({oid for oid,_,_ in records})
  sizes={}
  if oids:
   for line in git(root,'cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)',input=b'\n'.join(oids)+b'\n').splitlines():
    fields=line.split()
    if len(fields)!=3 or fields[1]!=b'blob':errors.append('索引对象无法核对: '+line.decode(errors='replace'));continue
    sizes[fields[0]]=int(fields[2])
   for oid,name,stage in records:
    if sizes.get(oid,0)>LIMIT:large.append({'path':name,'bytes':sizes[oid],'source':'git-index','stage':stage})
 except (OSError,subprocess.CalledProcessError,ValueError) as exc:
  errors.append(str(exc))
 return {'passed':not errors and not large,'limit_bytes':LIMIT,'working_files_checked':count,'oversized':large,'errors':errors}

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,required=True);args=parser.parse_args()
 if not args.root.is_absolute() or not args.root.is_dir():parser.error('--root 必须是存在的绝对目录')
 result=audit(args.root);print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
