import importlib.util,subprocess,tempfile,unittest
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('files',BASE/'scripts/check_repo_files.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class RepoFiles(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.git('init','-q')
 def tearDown(self):self.tmp.cleanup()
 def git(self,*args):subprocess.run(['git','-C',str(self.root),*args],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 def file(self,name,size):
  with (self.root/name).open('wb') as f:f.truncate(size)
 def test_threshold(self):
  self.file('small',m.LIMIT);self.assertTrue(m.audit(self.root)['passed'])
  self.file('large',m.LIMIT+1);self.assertFalse(m.audit(self.root)['passed'])
 def test_ignore_and_already_tracked(self):
  self.file('large',m.LIMIT+1);self.git('add','large');(self.root/'.gitignore').write_text('large\n')
  self.assertFalse(m.audit(self.root)['passed'])
  self.file('ignored',m.LIMIT+1);(self.root/'.gitignore').write_text('large\nignored\n')
  self.assertFalse(any(x['path']=='ignored' for x in m.audit(self.root)['oversized']))
 def test_staged_blob_larger_than_worktree(self):
  self.file('data',m.LIMIT+1);self.git('add','data');self.file('data',1)
  result=m.audit(self.root);self.assertFalse(result['passed']);self.assertTrue(any(x['source']=='git-index' for x in result['oversized']))
 def test_ignored_untracked_and_symlink(self):
  self.file('data',m.LIMIT+1);(self.root/'.gitignore').write_text('data\n');(self.root/'link').symlink_to('data');self.assertTrue(m.audit(self.root)['passed'])
 def test_no_repository(self):
  folder=self.root/'empty';folder.mkdir();self.assertFalse(m.audit(folder)['passed'])
if __name__=='__main__':unittest.main()
