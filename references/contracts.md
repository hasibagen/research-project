# 共同记录与执行契约

问题页维护理由、设计和判断；方案修订固定一次设计；run 固定一次执行。方法、参数、实现版本、输入和执行次数分别记录。一个 run 可以包含多条组合结果。

公共程序入口为本 skill 的 scripts/research_records.py，先执行 --help。它提供 append（校验与去重导入）、render（只更新标记区）、export（通过 ro-crate-py 打包）。这些操作不执行科学分析，不替代领域验收。输入路径全部为绝对路径；材料文件引用限制在给定材料根内，拒绝路径逃逸和符号链接逃逸。

记录采用 assets/templates/run.schema.json。status 为 failed 时保留失败信息与证据，不能出现科学指标；成功也必须由检查状态区分是否已验收。代码、输入、配置、环境需指向已保存材料。包元数据和每个文件内容哈希分开核验。

自动区使用 <!-- research-results:start --> 与 <!-- research-results:end -->。人工说明在区外。问题页更新是单接收端操作；导入记录通过文件锁序列化，重复内容不重复登记，同身份异内容拒绝并保留来件。不要用此本地锁承诺跨网络文件系统协调。

模板结构升级不重写旧 run；科学方案变化产生新 revision，新执行产生新 run_id。结果表可重建，原始记录不可覆盖。字段未知时不编造，用明确待核对项阻止正式验收。

## 工具边界与首版演示

assets/demo/Snakefile 使用 Python 标准库生成合成数据、执行两种简单分类规则并输出记录。此演示验证执行、来源、模板回填和导出，不是临床 ML 方法或模型优劣证据。执行说明见 assets/demo/README.md。本机用已装依赖的 python3 运行；其他安装按实际 conda 解释器解析。已测直接依赖见 tested-requirements.txt，它不是整个 base 的环境锁。

Snakemake 与 RO-Crate 随首个 demo 接入。真实项目已有分析入口优先包装；资源配置独立；已验收输出不作为重算覆盖目标。新运行独立目录，恢复需先核对状态。接真实超算、R/MATLAB 和更多宿主均需额外实测。

RO-Crate 导出是基础包；用 rocrate-validator 检查选定标准，保存报告。尚未实现 Workflow Run profile 映射，不宣称 profile 合规。阶段交付再固定采用范围。不开启 Aim，不自建第二套调度器。

## 依据

- https://book.the-turing-way.org/reproducible-research/compendia/ ：材料、代码与说明相连。
- https://doi.org/10.1371/journal.pcbi.1008770 ：探索、改进、整理的迭代。
- https://www.researchobject.org/ro-crate/ ：研究材料描述标准。
- https://www.researchobject.org/workflow-run-crate/ ：执行来源 profiles。
- https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html ：依赖规则。

模板字段为本套设计，不冒充上述标准要求。领域论文记录 DOI、采用步骤、适用条件和本项目偏离；本地 wiki 模板仅作为字段设计参考，不复制其整套审批规则。

## 日常入口优先

执行与交付前阅读 [日常操作规范](../docs/daily-operations.md)。工具缺失时可手工维护同一问题页与判断条。现有 schema／脚本未实现终评授权、脱敏检测、备份验收或科学就绪的自动闸门，不能把基础校验通过解释为这些检查通过。来源沿革见 [机制溯源](../docs/mechanism-provenance.md)。

跨 skill 的责任与恢复协议见 [协作架构契约](../docs/architecture-contract.md)；本页继续只维护运行记录与工具接口。

## 当前记录版本

新记录为 v2，旧 v1 读取兼容；machine／randomness 字段及材料引用验证见 [兼容说明](../docs/record-v2.md)。新例程生成 v2；人工构造记录不能跳过实际哈希和环境来源。
