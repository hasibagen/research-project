"""Read-only plan identity, dependency and evidence checks. Does not validate science."""
import argparse,json
from pathlib import Path
import yaml
STATES={'未开始','已承诺','进行中','待判断','受阻','待复核','暂缓','完成','取消'}
ACTIVE={'进行中','待判断','完成'}
def audit(root,folder):
 errors=[];warnings=[];plans={};nodes={};locations={}
 def err(where,msg):errors.append(f'{where}: {msg}')
 def refs(where,values):
  if not isinstance(values,list):err(where,'evidence 必须为列表');return
  for value in values:
   if not isinstance(value,str):err(where,'证据引用必须是字符串');continue
   if value.startswith(('https://','http://')):warnings.append(f'{where}: 外部证据未检查 {value}');continue
   path=value.split('#')[0]
   if not path:err(where,'证据路径为空');continue
   p=Path(path);p=p if p.is_absolute() else root/p
   if not p.is_file():err(where,'证据文件缺失 '+value)
 for file in sorted(folder.rglob('PLAN.md')):
  if 'backup' in file.relative_to(folder).parts[:-1]:continue
  text=file.read_text()
  if not text.startswith('---\n'):warnings.append(f'{file}: 未结构化／待接入');continue
  parts=text.split('---',2)
  try:d=yaml.safe_load(parts[1])
  except Exception as e:err(file,'YAML 无效 '+str(e));continue
  if not isinstance(d,dict):err(file,'头部必须是对象');continue
  pid=d.get('plan_id')
  if not isinstance(pid,str) or not pid or '#' in pid:err(file,'plan_id 无效');continue
  if pid in plans:err(file,'重复 plan_id '+pid);continue
  if not isinstance(d.get('directions'),list) or not d['directions'] or not all(isinstance(x,str) and x for x in d['directions']):err(pid,'directions 需要非空字符串列表')
  for field in ['owner','updated']:
   if not d.get(field):err(pid,'缺少 '+field)
  tasks=[]
  if 'task_files' in d:
   if 'tasks' in d:err(pid,'tasks 与 task_files 不得并存')
   task_files=d['task_files'];loaded=set()
   if not isinstance(task_files,list):err(pid,'task_files 必须为列表');task_files=[]
   if not isinstance(d.get('project_id'),str) or not d['project_id']:err(pid,'新格式缺少 project_id')
   task_root=(file.parent/'tasks').resolve();plan_root=file.parent.resolve();task_list=plan_root/'TASK.md'
   for ref in task_files:
    if not isinstance(ref,str) or not ref:err(pid,'task_files 路径无效');continue
    q=Path(ref);q=(q if q.is_absolute() else file.parent/q).resolve()
    if q.is_relative_to(plan_root) and 'backup' in q.relative_to(plan_root).parts[:-1]:err(pid,'历史备份不可作为当前任务状态源');continue
    if q!=task_list and not q.is_relative_to(task_root):err(pid,'任务文件必须为本计划 TASK.md 或 tasks 内文件');continue
    if q in loaded:err(pid,'重复任务文件引用');continue
    loaded.add(q)
    if not q.is_file():err(pid,'任务文件缺失 '+ref);continue
    try:
     raw=q.read_text()
     if not raw.startswith('---\n') or len(raw.split('---',2))!=3:raise ValueError('缺少 YAML 头')
     task=yaml.safe_load(raw.split('---',2)[1])
     if not isinstance(task,dict):raise ValueError('任务头必须为对象')
    except (ValueError,yaml.YAMLError) as e:err(q,str(e));continue
    if task.get('plan_id')!=pid:err(q,'任务归属 plan_id 不匹配')
    for field in ['owner','updated']:
     if not task.get(field):err(q,'缺少 '+field)
    if 'tasks' in task:
     if q!=task_list:err(q,'任务清单只允许放计划根 TASK.md')
     if 'task_id' in task or 'status' in task:err(q,'任务清单不能同时维护单任务身份或状态')
     entries=task['tasks']
     if not isinstance(entries,list):err(q,'tasks 必须为列表');entries=[]
     for entry in entries:
      if not isinstance(entry,dict):err(q,'任务必须是对象');continue
      item={'owner':task.get('owner'),'updated':task.get('updated'),**entry}
      for field in ['owner','updated']:
       if not item.get(field):err(q,'缺少 '+field)
      if item.get('status')=='暂缓' and not item.get('resume_when'):err(q,'缺少恢复条件')
      tasks.append(item)
    else:
     if task.get('status')=='暂缓' and not task.get('resume_when'):err(q,'缺少恢复条件')
     tasks.append(task)
   for q in task_root.rglob('*.md'):
    if 'backup' in q.relative_to(task_root).parts[:-1]:continue
    if q.resolve() not in loaded:
     raw=q.read_text()
     try: header=yaml.safe_load(raw.split('---',2)[1]) if raw.startswith('---\n') else None
     except (yaml.YAMLError,IndexError):header=None
     if q.name=='TASK.md' or (isinstance(header,dict) and 'task_id' in header):err(pid,'未登记任务 '+str(q))
   if task_list.is_file() and task_list not in loaded:
    raw=task_list.read_text()
    try: header=yaml.safe_load(raw.split('---',2)[1]) if raw.startswith('---\n') else None
    except (yaml.YAMLError,IndexError):header=None
    if isinstance(header,dict) and ('tasks' in header or 'task_id' in header):err(pid,'根 TASK.md 仍维护未登记的任务状态')
  else:
   tasks=d.get('tasks')
   if not isinstance(tasks,list):err(pid,'tasks 必须为列表');tasks=[]
  plans[pid]=d;nodes[pid]=d;locations[pid]=file
  for task in tasks:
   if not isinstance(task,dict):err(pid,'任务必须是对象');continue
   tid=task.get('task_id')
   if not isinstance(tid,str) or not tid or '#' in tid:err(pid,'task_id 无效');continue
   key=pid+'#'+tid
   if key in nodes:err(key,'重复任务键');continue
   if not task.get('done_when'):err(key,'缺少验收条件')
   nodes[key]=task;locations[key]=file
 if not plans: warnings.append('没有可校验的结构化计划；不能据此宣称审计通过')
 graph={k:[] for k in nodes}
 for key,d in nodes.items():
  status=d.get('status')
  if status not in STATES:err(key,'状态无效')
  if status in {'暂缓','取消','受阻'} and not d.get('reason'):err(key,'缺少状态原因')
  if '#' not in key and status=='暂缓' and not d.get('resume_when'):err(key,'缺少恢复条件')
  refs(key,d.get('evidence',[]))
  if status=='完成' and not d.get('evidence'):err(key,'完成缺少证据')
  deps=d.get('depends_on',[])
  if '#' in key and isinstance(deps,list):
   inherited=plans[key.split('#')[0]].get('depends_on',[])
   if isinstance(inherited,list):deps=deps+inherited
  if not isinstance(deps,list):err(key,'depends_on 必须为列表');deps=[]
  for dep in deps:
   if not isinstance(dep,str) or dep not in nodes:err(key,'依赖不存在 '+str(dep));continue
   graph[key].append(dep)
   if status in ACTIVE and nodes[dep].get('status')!='完成':err(key,'依赖未完成 '+dep)
  if '#' not in key:
   # A plan is complete only after its own tasks are disposed; include these
   # structural edges in cycle checks to catch task -> own parent deadlocks.
   for taskkey in nodes:
    if taskkey.startswith(key+'#'):graph[key].append(taskkey)
   if status=='完成':
    if d.get('checks_passed') is not True:err(key,'完成缺少检查通过依据标记')
    if any(v.get('status') not in {'完成','取消'} for k,v in nodes.items() if k.startswith(key+'#')):err(key,'完成但有未处置任务')
 seen=set();stack=[];active=set()
 def visit(k):
  if k in active:err(k,'依赖环 '+' -> '.join(stack+[k]));return
  if k in seen:return
  active.add(k);stack.append(k)
  for dep in graph[k]:visit(dep)
  stack.pop();active.remove(k);seen.add(k)
 for k in graph:visit(k)
 return {'plans_checked':len(plans),'errors':errors,'warnings':warnings,'passed':bool(plans) and not errors}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',required=True);p.add_argument('--plans',required=True);a=p.parse_args()
 if not Path(a.root).is_absolute() or not Path(a.plans).is_absolute():p.error('必须使用绝对路径')
 root=Path(a.root).resolve();folder=Path(a.plans).resolve()
 if not root.is_dir() or not folder.is_dir():p.error('目录不存在')
 result=audit(root,folder);print(json.dumps(result,ensure_ascii=False,indent=2));return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
