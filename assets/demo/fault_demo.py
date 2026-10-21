"""Exercise interrupted import, replay, and conflict preservation on synthetic evidence."""
import json,subprocess,sys,time
from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'scripts'));import research_records as r
def exercise(root):
 root.mkdir(parents=True,exist_ok=False);(root/'evidence.txt').write_text('synthetic evidence')
 record={'schema_version':2,'run_id':'fault-demo','question':'fault-q','revision':1,'status':'success','checks':'pending','artifacts':[{'path':'evidence.txt','sha256':r.sha(root/'evidence.txt')}],'results':[{'combo':'baseline','metrics':{'auc':0.5}}]}
 f=root/'record.json';f.write_text(json.dumps(record));reg=root/'registry.json';page=root/'findings.md';page.write_text('人工说明\n'+r.START+'\n尚未同步\n'+r.END+'\n判断：待解释')
 # Kill a real worker after durable import but before findings refresh.
 code="import sys,time;from pathlib import Path;sys.path.insert(0,sys.argv[1]);import research_records as r;p=Path(sys.argv[2]);r.append(p/'record.json',p,p/'registry.json');(p/'ready').write_text('imported');time.sleep(30)"
 worker=subprocess.Popen([sys.executable,'-c',code,str(BASE/'scripts'),str(root)])
 try:
  deadline=time.monotonic()+10
  while not (root/'ready').exists():
   if worker.poll() is not None or time.monotonic()>deadline:raise RuntimeError('worker did not reach checkpoint')
   time.sleep(.02)
  worker.kill();worker.wait(timeout=5)
 finally:
  if worker.poll() is None:worker.kill();worker.wait()
 if r.append(f,root,reg):raise AssertionError('duplicate imported')
 r.render(reg,page,'fault-q')
 conflict=root/'conflict.json';changed=dict(record,revision=2);conflict.write_text(json.dumps(changed))
 try:r.append(conflict,root,reg)
 except ValueError:pass
 else:raise AssertionError('conflict accepted')
 assert len(json.loads(reg.read_text()))==1 and json.loads(reg.read_text())[0]['revision']==1
 assert conflict.exists() and f.exists() and '待解释' in page.read_text() and 'pending' in page.read_text()
 report={'interrupted_after_import':True,'replay_added':False,'conflict_preserved':True,'pending_visible':True}
 (root/'fault-report.json').write_text(json.dumps(report,indent=2));return report
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 if not a.output.is_absolute():ap.error('必须为绝对路径')
 print(exercise(a.output))
