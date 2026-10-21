"""Create a NEW self-contained project documentation and run-template scaffold."""
import argparse,json,re,shutil,sys
from datetime import date
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
def key(value):
 reserved={'con','prn','aux','nul',*(f'com{i}' for i in range(1,10)),*(f'lpt{i}' for i in range(1,10))}
 if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',value) or value in reserved:raise ValueError('身份须小写字母／数字与连字符，且非 Windows 保留名')
 return value
def create(dest,project,plan,task,with_run_template=False):
 if not dest.is_absolute():raise ValueError('输出必须为绝对路径')
 for value in [project,plan,task]:key(value)
 dest.mkdir(parents=True,exist_ok=False)
 project_dir=dest/'docs';plan_dir=project_dir/'plans'/plan
 sources={'PROJECT.md':'project-contract.md'}
 def copy(src,target):
  target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target)
  # Retain working references to installed guidance; generated research records stay local.
  if target.suffix=='.md':
   def link(m):
    v=m.group(1)
    if '://' in v or v.startswith('#') or Path(v).is_absolute():return m.group(0)
    return ']('+str((src.parent/v).resolve())+')'
   target.write_text(re.sub(r'\]\(([^)]+)\)',link,target.read_text()))
 for target,src in sources.items():copy(BASE/'assets/templates'/src,project_dir/target)
 for filename in ['PLAN.md','TASK.md']:
  target=plan_dir/filename
  copy(BASE/'modules/plan/assets'/filename,target)
  text=target.read_text().replace('example-project',project).replace('example-plan',plan).replace('task_id: baseline',f'task_id: {task}').replace('## baseline',f'## {task}')
  target.write_text(text)
 copy(BASE/'assets/templates/work-log.md',plan_dir/'LOG.md')
 # Run template lives apart from documentation; this is not an executed run.
 if with_run_template:
  run=dest/'results-templates/run-template';run.mkdir(parents=True)
  for folder in ['provenance','logs','tables','figures','predictions','labels','model_dump']:(run/folder).mkdir()
  record={'schema_version':2,'run_id':'replace-before-execution','question':'question-01','revision':1,'status':'success','checks':'pending','machine':{'machine':'unknown','gpu':[],'env_ref':'provenance/environment.txt'},'randomness':{'mode':'unknown','note':'填写实际设计后执行'},'artifacts':[{'path':'provenance/environment.txt','sha256':'REPLACE_WITH_ACTUAL_SHA256'}],'results':[]}
  (run/'record.template.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
  (run/'provenance/environment.txt').write_text('模板：填写实际环境恢复命令、版本与硬件；未执行。\n')
  (run/'CHECKS.md').write_text('# 运行检查模板\n值域／单位／样本计数：未检查\n固定输入与种子复跑：未检查\n浮点容差：待确定\n多重复稳定性：未检查\n产物与哈希：未检查\n')
 f=project_dir/'PROJECT.md';f.write_text(f.read_text().replace('project_id：待填写（文档工作区内唯一）',f'project_id：{project}')+f'\n- [{plan}](plans/{plan}/PLAN.md)；任务状态见该计划 TASK.md。模板待填写。\n')
 text=(BASE/'assets/templates/project-scaffold/README.md').read_text()
 for token,value in {'PROJECT_ROOT':str(dest.resolve())}.items():
  text=text.replace('{{'+token+'}}',value)
 (dest/'README.md').write_text(text)
 shutil.copy2(BASE/'assets/templates/project-scaffold/gitignore',dest/'.gitignore')
 text=(BASE/'assets/templates/project-scaffold/AGENTS.md').read_text()
 for token,value in {'PROJECT_ID':project,'PLAN_ID':plan,'PROJECT_ROOT':str(dest.resolve()),'SKILL_ROOT':str(BASE),'WRITING_ROOT':str(Path.home()/'.agents/skills'),'DATE':date.today().isoformat()}.items():
  text=text.replace('{{'+token+'}}',value)
 if with_run_template:
  text+='\n已生成可选 results-templates/run-template 教学样板；不是实际运行或检查证据。\n'
 (dest/'AGENTS.md').write_text(text)
 text=(BASE/'assets/templates/project-scaffold/docs-readme.md').read_text()
 for token,value in {'PROJECT_ID':project,'PLAN_ID':plan,'PROJECT_ROOT':str(dest.resolve()),'SKILL_ROOT':str(BASE)}.items():
  text=text.replace('{{'+token+'}}',value)
 (project_dir/'README.md').write_text(text)
 return dest
if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--project',required=True);ap.add_argument('--plan',required=True);ap.add_argument('--task',required=True);ap.add_argument('--with-run-template',action='store_true',help='另生成未执行的运行教学样板');a=ap.parse_args()
 try:print(create(a.output,a.project,a.plan,a.task,a.with_run_template))
 except (ValueError,FileExistsError) as exc:ap.error(str(exc))
