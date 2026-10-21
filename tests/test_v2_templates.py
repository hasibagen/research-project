import importlib.util,json,tempfile,unittest
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r=module('rv2',BASE/'scripts/research_records.py');sc=module('scaffold',BASE/'scripts/create_project_template.py');fault=module('fault',BASE/'assets/demo/fault_demo.py')
try:
    HAS_ROCRATE=importlib.util.find_spec('rocrate') is not None
except Exception:
    HAS_ROCRATE=False
class V2(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);(self.root/'env').write_text('environment')
  self.rec=dict(schema_version=2,run_id='r1',question='q',revision=1,status='success',checks='pending',artifacts=[dict(path='env',sha256=r.sha(self.root/'env'))],results=[],machine=dict(machine='host',gpu=['gpu'],cpu_cores=2,env_ref='env'),randomness=dict(mode='stochastic',seeds=[1,2],repeats=2,design_ref='env'))
 def tearDown(self):self.tmp.cleanup()
 @unittest.skipUnless(HAS_ROCRATE,'optional dependency not installed: rocrate')
 def test_v2_roundtrip(self):
  f=self.root/'record.json';f.write_text(json.dumps(self.rec));reg=self.root/'registry.json';r.append(f,self.root,reg);page=self.root/'page.md';page.write_text(r.START+'\n'+r.END);r.render(reg,page,'q');r.export(f,self.root,self.root/'crate','https://creativecommons.org/publicdomain/zero/1.0/');self.assertEqual(json.loads(reg.read_text())[0]['machine'],self.rec['machine'])
 def test_missing_env(self):
  self.rec['machine']['env_ref']='absent'
  with self.assertRaises(ValueError):r.validate(self.rec,self.root)
 def test_invalid_cpu_and_unknown(self):
  import jsonschema
  self.rec['machine']['cpu_cores']=0
  with self.assertRaises(jsonschema.ValidationError):r.validate(self.rec,self.root)
  self.rec['machine']['cpu_cores']=1;self.rec['machine']['extra']='x'
  with self.assertRaises(jsonschema.ValidationError):r.validate(self.rec,self.root)
 def test_versions(self):
  self.rec['schema_version']=99
  with self.assertRaises(ValueError):r.validate(self.rec,self.root)
 def test_scaffold(self):
  dest=sc.create(self.root/'new','project-a','plan-a','task-a',with_run_template=True)
  check=module('plancheck',BASE/'modules/plan/scripts/check_plans.py');result=check.audit(dest,dest/'docs/plans');self.assertTrue(result['passed'],result)
  with self.assertRaises(FileExistsError):sc.create(dest,'project-a','plan-a','task-a')
  import jsonschema
  template=json.loads((dest/'results-templates/run-template/record.template.json').read_text())
  with self.assertRaises(jsonschema.ValidationError):r.validate(template,dest/'results-templates/run-template')
 def test_bad_ids(self):
  for name in ['Bad','a b','CON','con','../x','a_b']:
   with self.assertRaises(ValueError):sc.key(name)
 def test_scaffold_document_navigation(self):
  import re
  dest=sc.create(self.root/'navigation','project-a','plan-a','task-a')
  guide=dest/'docs/README.md'
  self.assertTrue(guide.is_file())
  text=guide.read_text()
  self.assertNotIn('{{',text)
  for ref in re.findall(r'\]\(([^)]+)\)',text):
   if '://' not in ref and not ref.startswith('#'):
    self.assertTrue((guide.parent/ref).resolve().exists(),ref)
  self.assertFalse((dest/'code').exists())
  self.assertFalse((dest/'data').exists())
  self.assertFalse((dest/'results').exists())
 def test_kill_replay_conflict(self):self.assertTrue(all(v is True for k,v in fault.exercise(self.root/'fault').items() if k!='replay_added'))
if __name__=='__main__':unittest.main()
