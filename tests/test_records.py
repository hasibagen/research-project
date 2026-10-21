import copy, hashlib, importlib.util, json, tempfile, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('records',Path(__file__).resolve().parents[1]/'scripts/research_records.py'); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
try:
    HAS_ROCRATE=importlib.util.find_spec('rocrate') is not None
except Exception:
    HAS_ROCRATE=False
class Records(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);(self.root/'x').write_text('evidence')
  self.r={'schema_version':1,'run_id':'r1','question':'q','revision':1,'status':'success','checks':'passed','artifacts':[{'path':'x','sha256':m.sha(self.root/'x')}],'results':[{'combo':'a','metrics':{'score':0.5}}]}
  self.record=self.root/'record.json';self.registry=self.root/'registry.json';self.save()
 def tearDown(self):self.tmp.cleanup()
 def save(self):self.record.write_text(json.dumps(self.r))
 def test_duplicate_and_conflict(self):
  self.assertTrue(m.append(self.record,self.root,self.registry));self.assertFalse(m.append(self.record,self.root,self.registry))
  self.r['revision']=2;self.save()
  with self.assertRaises(ValueError):m.append(self.record,self.root,self.registry)
  self.assertEqual(json.loads(self.registry.read_text())[0]['revision'],1)
 def test_tamper(self):
  (self.root/'x').write_text('changed')
  with self.assertRaises(ValueError):m.validate(self.r,self.root)
 def test_escape(self):
  self.r['artifacts'][0]['path']='../outside'
  with self.assertRaises(ValueError):m.validate(self.r,self.root)
 def test_failed_metrics(self):
  self.r['status']='failed'
  with self.assertRaises(ValueError):m.validate(self.r,self.root)
 def test_preserve_narrative_and_filter(self):
  m.append(self.record,self.root,self.registry);page=self.root/'plan.md';page.write_text('human\n'+m.START+'\nold\n'+m.END+'\ndecision')
  m.render(self.registry,page,'q');s=page.read_text();self.assertTrue(s.startswith('human'));self.assertTrue(s.endswith('decision'));self.assertIn('0.5',s)
  m.render(self.registry,page,'other');self.assertNotIn('0.5',page.read_text())
 @unittest.skipUnless(HAS_ROCRATE,'optional dependency not installed: rocrate')
 def test_relocation_and_export(self):
  import shutil
  moved=self.root/'moved';moved.mkdir();shutil.copy(self.root/'x',moved/'x');m.validate(self.r,moved)
  out=self.root/'crate';m.export(self.record,moved,out,'https://creativecommons.org/publicdomain/zero/1.0/')
  self.assertEqual(m.sha(out/'x'),self.r['artifacts'][0]['sha256'])
  with self.assertRaises(FileExistsError):m.export(self.record,moved,out,'https://creativecommons.org/publicdomain/zero/1.0/')
if __name__=='__main__':unittest.main()
