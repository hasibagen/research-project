import unittest,tempfile,importlib.util
from pathlib import Path
import yaml
spec=importlib.util.spec_from_file_location('check',Path(__file__).resolve().parents[1]/'scripts/check_plans.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Audit(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);(self.root/'evidence.md').write_text('verified')
 def tearDown(self):self.tmp.cleanup()
 def write(self,name,**kwargs):
  d=dict(plan_id=name,directions=['prediction'],owner='researcher',updated='2026-10-19',status='未开始',depends_on=[],tasks=[],evidence=[]);d.update(kwargs)
  p=self.root/name;p.mkdir(exist_ok=True);(p/'PLAN.md').write_text('---\n'+yaml.safe_dump(d,allow_unicode=True)+'---\n# Plan')
 def check(self):return m.audit(self.root,self.root)
 def test_parallel_and_shared_dependency(self):
  self.write('a',status='完成',checks_passed=True,evidence=['evidence.md']);self.write('b',depends_on=['a']);self.write('c',depends_on=['a']);self.assertTrue(self.check()['passed'])
 def test_cycle(self):
  self.write('a',depends_on=['b']);self.write('b',depends_on=['a']);self.assertFalse(self.check()['passed'])
 def test_self_parent_deadlock(self):
  self.write('a',tasks=[dict(task_id='x',status='未开始',done_when='check',depends_on=['a'])]);self.assertFalse(self.check()['passed'])
 def test_missing_and_unready(self):
  self.write('a');self.write('b',status='进行中',depends_on=['a','missing']);self.assertGreaterEqual(len(self.check()['errors']),2)
 def test_completion_evidence(self):
  self.write('a',status='完成',checks_passed=True,evidence=['absent']);self.assertFalse(self.check()['passed'])
 def test_pause_resume(self):
  self.write('a',status='暂缓',reason='budget');self.assertFalse(self.check()['passed'])
 def test_duplicate(self):
  self.write('a');self.write('b',plan_id='a');self.assertFalse(self.check()['passed'])
 def external(self,plan='a',**kwargs):
  self.write(plan,project_id='project',task_files=['tasks/x/TASK.md'])
  pf=self.root/plan/'PLAN.md';raw=pf.read_text();d=yaml.safe_load(raw.split('---',2)[1]);d.pop('tasks');pf.write_text('---\n'+yaml.safe_dump(d,allow_unicode=True)+'---\n# Plan')
  f=self.root/plan/'tasks/x/TASK.md';f.parent.mkdir(parents=True)
  task=dict(plan_id=plan,task_id='x',owner='r',updated='2026-10-19',status='未开始',done_when='verified',depends_on=[],evidence=[]);task.update(kwargs)
  f.write_text('---\n'+yaml.safe_dump(task,allow_unicode=True)+'---\n# Task');return f
 def test_external_tasks(self):
  self.external();self.assertTrue(self.check()['passed'])
 def test_external_ownership(self):
  self.external(plan_id='wrong');self.assertFalse(self.check()['passed'])
 def test_external_completion(self):
  self.external(status='完成');self.assertFalse(self.check()['passed'])
 def test_external_cycle(self):
  self.external(depends_on=['a#x']);self.assertFalse(self.check()['passed'])
 def test_orphan_task(self):
  f=self.external();q=f.parent.parent/'y/TASK.md';q.parent.mkdir();q.write_text(f.read_text());self.assertFalse(self.check()['passed'])
 def test_missing_external_file(self):
  self.write('a',project_id='p',task_files=['tasks/missing/TASK.md']);self.assertFalse(self.check()['passed'])
 def test_mixed_storage_rejected(self):
  self.external();f=self.root/'a/PLAN.md';f.write_text(f.read_text().replace('task_files:', 'tasks: []\ntask_files:'));self.assertFalse(self.check()['passed'])
 def test_task_path_escape(self):
  self.external();f=self.root/'a/PLAN.md';f.write_text(f.read_text().replace('tasks/x/TASK.md','../evidence.md'));self.assertFalse(self.check()['passed'])
if __name__=='__main__':unittest.main()
