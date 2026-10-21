"""Run the complete synthetic workflow in a NEW absolute output directory."""
import argparse,json,shutil,subprocess,sys
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args()
out=Path(a.output)
if not out.is_absolute():p.error('--output 必须为绝对路径')
out=out.resolve();out.mkdir(parents=True,exist_ok=False)
here=Path(__file__).resolve().parent;skill=here.parents[1]
sys.path.insert(0,str(skill/'scripts'));import research_records as records
run=out/'run1'
def execute(args,log):
 with (out/log).open('w') as f:subprocess.run(args,stdout=f,stderr=subprocess.STDOUT,check=True)
execute([str(Path(sys.executable).with_name('snakemake')),'--snakefile',str(here/'Snakefile'),'--directory',str(out),'--cores','1','--config',f'run_root={run}'],'snakemake.log')
registry=out/'registry.json';record=run/'record.json';page=out/'question.md'
records.append(record,run,registry);assert not records.append(record,run,registry)
shutil.copy2(skill/'assets/templates/analysis.md',page)
records.export(record,run,out/'crate','https://creativecommons.org/publicdomain/zero/1.0/')
execute([str(Path(sys.executable).with_name('rocrate-validator')),'validate',str(out/'crate'),'-p','ro-crate-1.3','--no-auto-profile','-l','required','-f','json','-o',str(out/'validation.json'),'--no-paging'],'validator.log')
records.render(registry,page,'synthetic-demo')
print(out)
