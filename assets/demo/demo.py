import argparse, csv, hashlib, json, random, shutil, sys, platform, os
from pathlib import Path
from importlib.metadata import version
p=argparse.ArgumentParser();p.add_argument('action',choices=['data','analyze','record']);p.add_argument('--root',required=True);p.add_argument('--combo',choices=['majority','threshold']);a=p.parse_args()
root=Path(a.root).resolve();root.mkdir(parents=True,exist_ok=True)
if (root/'record.json').exists(): raise SystemExit('已完成的演示运行不可覆盖，请使用新的 run_root')
def write(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n')
if a.action=='data':
    rng=random.Random(19)
    rows=[{'x':rng.random(),'y':None} for _ in range(60)]
    for r in rows:r['y']=int(r['x']>0.5)
    write(root/'data.json',rows)
elif a.action=='analyze':
    rows=json.loads((root/'data.json').read_text()); train,test=rows[:40],rows[40:]
    majority=int(sum(r['y'] for r in train)>=len(train)/2)
    predictions=[majority if a.combo=='majority' else int(r['x']>0.5) for r in test]
    write(root/(a.combo+'.json'),{'combo':a.combo,'metrics':{'accuracy':sum(pred==r['y'] for pred,r in zip(predictions,test))/len(test)}})
else:
    shutil.copy2(Path(__file__),root/'code.py')
    shutil.copy2(Path(__file__).with_name('Snakefile'),root/'Snakefile')
    write(root/'effective-config.json',{'template_version':1,'seed':19,'split':'first 40 train, last 20 test','threshold':0.5,'purpose':'orchestration only'})
    write(root/'environment.json',{'python':sys.version,'snakemake':version('snakemake'),'rocrate':version('rocrate')})
    files=['data.json','majority.json','threshold.json','code.py','Snakefile','effective-config.json','environment.json']
    write(root/'record.json',{'schema_version':2,'machine':{'machine':platform.node(),'node':platform.node(),'cpu_cores':os.cpu_count() or 1,'env_ref':'environment.json'},'randomness':{'mode':'stochastic','seeds':[19],'repeats':1,'design_ref':'effective-config.json','note':'合成数据随机生成；分析规则确定；单次仅演示'},'run_id':root.name,'question':'synthetic-demo','revision':1,'status':'success','checks':'passed','artifacts':[{'path':f,'sha256':hashlib.sha256((root/f).read_bytes()).hexdigest()} for f in files],'results':[json.loads((root/(c+'.json')).read_text()) for c in ['majority','threshold']]})
