"""Exercise default layout and task identities across new and legacy records."""
import importlib.util,tempfile,unittest
from pathlib import Path
import yaml
BASE=Path(__file__).resolve().parents[1]
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
sc=load('layout_scaffold',BASE/'scripts/create_project_template.py')
check=load('layout_check',BASE/'modules/plan/scripts/check_plans.py')
class Layout(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=sc.create(Path(self.temp.name)/'new','p','study','first');self.plan=self.root/'docs/plans/study'
 def tearDown(self):self.temp.cleanup()
 def audit(self):return check.audit(self.root,self.root/'docs/plans')
 def read(self,name):return yaml.safe_load((self.plan/name).read_text().split('---',2)[1])
 def write(self,name,data):
  p=self.plan/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('---\n'+yaml.safe_dump(data,allow_unicode=True)+'---\n')
 def test_minimal_and_no_empty_directories(self):
  self.assertEqual({str(p.relative_to(self.root)) for p in self.root.rglob('*') if p.is_file()},{'README.md','AGENTS.md','.gitignore','docs/README.md','docs/PROJECT.md','docs/plans/study/PLAN.md','docs/plans/study/TASK.md','docs/plans/study/LOG.md'})
  self.assertTrue(self.audit()['passed']);self.assertIn('## first',(self.plan/'TASK.md').read_text())
 def test_multiple_tasks_cycle_and_completion(self):
  d=self.read('TASK.md');second=dict(d['tasks'][0],task_id='second');d['tasks'].append(second)
  self.write('TASK.md',d);self.assertTrue(self.audit()['passed'])
  d['tasks'][0]['depends_on']=['study#second'];second['depends_on']=['study#first'];self.write('TASK.md',d)
  self.assertTrue(any('依赖环' in e for e in self.audit()['errors']))
  d['tasks'][0]['depends_on']=[];second['depends_on']=[];second['status']='完成';self.write('TASK.md',d)
  self.assertTrue(any('完成缺少证据' in e for e in self.audit()['errors']))
 def test_legacy_split_and_duplicate_state(self):
  d=self.read('TASK.md');task={'plan_id':'study','owner':d['owner'],'updated':d['updated'],**d['tasks'][0]}
  self.write('tasks/first/TASK.md',task);plan=self.read('PLAN.md');plan['task_files']=['tasks/first/TASK.md'];self.write('PLAN.md',plan)
  self.assertTrue(any('根 TASK.md' in e for e in self.audit()['errors']))
  (self.plan/'TASK.md').write_text('# 任务入口\n见 tasks/first/TASK.md\n');self.assertTrue(self.audit()['passed'])
 def test_new_split_and_escape(self):
  d=self.read('TASK.md');task={'plan_id':'study','owner':d['owner'],'updated':d['updated'],**d['tasks'][0]};self.write('tasks/T01-first.md',task)
  plan=self.read('PLAN.md');plan['task_files']=['tasks/T01-first.md'];self.write('PLAN.md',plan);(self.plan/'TASK.md').write_text('# 入口\n');self.assertTrue(self.audit()['passed'])
  plan['task_files']=['../outside.md'];self.write('PLAN.md',plan);self.assertTrue(any('任务文件必须' in e for e in self.audit()['errors']))
 def test_backup_not_a_live_plan(self):
  import shutil
  backup=self.plan/'backup'/'old';backup.mkdir(parents=True)
  shutil.copy2(self.plan/'PLAN.md',backup/'PLAN.md')
  self.assertTrue(self.audit()['passed'],self.audit())
 def test_backup_cannot_supply_live_task_state(self):
  d=self.read('TASK.md');task={'plan_id':'study','owner':d['owner'],'updated':d['updated'],**d['tasks'][0]}
  self.write('tasks/backup/T01.md',task)
  self.assertTrue(self.audit()['passed'],self.audit())
  plan=self.read('PLAN.md');plan['task_files']=['tasks/backup/T01.md'];self.write('PLAN.md',plan)
  self.assertTrue(any('历史备份' in e for e in self.audit()['errors']))
 def test_legacy_inline_and_duplicate_id(self):
  plan=self.read('PLAN.md');plan.pop('task_files');plan['tasks']=self.read('TASK.md')['tasks'];self.write('PLAN.md',plan);self.assertTrue(self.audit()['passed'])
  plan['tasks'].append(dict(plan['tasks'][0]));self.write('PLAN.md',plan);self.assertTrue(any('重复任务键' in e for e in self.audit()['errors']))
if __name__=='__main__':unittest.main()
