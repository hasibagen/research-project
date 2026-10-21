# 合成演示

使用已安装依赖的 conda Python 执行本目录 run_demo.py，并传入一个尚不存在的绝对输出目录：

```text
<conda-python-absolute-path> <skill-absolute-path>/assets/demo/run_demo.py --output <new-absolute-directory>
```

演示会执行 Snakemake、生成来源记录、去重导入、由模板生成问题页、导出 RO-Crate、用 rocrate-validator 校验基础 RO-Crate 1.3 必需项，最后回填问题页。每一步的日志留在输出目录；失败不宣称完成，重新执行完整演示需新目录。

如需检查计算恢复，直接对未完成的 run_root 重跑本目录 Snakefile；先核对失败日志与已有材料。完成后的 demo.py 拒绝覆盖；正式项目须在执行器入口实现同样保护。演示不是生产级作业管理器，没有实现远端提交对账。

数据为合成数据：固定前 40 行作为训练集、后 20 行作为测试集，比较多数类基线与固定阈值。仅验证管理流程，不宣称这是嵌套交叉验证或临床模型。聚类模板字段已提供，但本演示没有执行聚类算法。

分发时保留整个 research-project 大 skill，内部 modules、docs、assets、scripts 一并携带；其他宿主的安装映射尚未验证。当前只验证 Linux、Python、本地执行和基础研究包，不宣称已支持 R/MATLAB、真实超算或 Workflow Run profile。

## 故障演练

用 conda Python 运行本目录 fault_demo.py --output <新的绝对目录>：在导入成功、回填前终止真实子进程，再恢复；重复导入不增加事实，同 run_id 异内容拒绝且保留来件与原记录，findings 保留待解释状态。报告为 fault-report.json。这验证的是本地检查点中断，不涵盖磁盘故障、断电或远端作业对账。正常演示已改为生成 v2，并记录机器和合成随机性。
