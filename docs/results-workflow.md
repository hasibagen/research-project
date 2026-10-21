# 结果模板、产物与研究发现

## 1. 三层事实分开保存

实际产物进入运行目录；findings 按研究问题组织观察、比较及证据；decisions 记录根据证据选择什么。release 再明确采用了哪些产物。findings 不以“最好分数”代替完整尝试记录，decisions 不覆盖原始指标。

目录结构和运行位置以 [结果目录架构](../structures/results/GUIDE.md) 为准。默认 `<结果根>/runs/<run_id>/`；已有执行范围保留映射。公共 schema 通过 artifacts 列出来源材料路径和哈希，不自动检查全部来源信息是否齐全。

## 2. Findings 模板怎样实例化

新问题先用 [通用模板](../assets/templates/analysis.md) 创建计划内 FINDINGS.md（多个独立问题再拆为 findings/{question_id}.md），再按分析类型补 [分类／回归／聚类字段](../assets/templates/analysis-types.md)。登记 project／plan／task、question_id、模板版本、方案 revision 和探索／确认阶段。

执行前填写问题、依据、输入人群、主次指标、基线、固定条件、允许变化、划分、预处理拟合范围、预算和判断标准。执行后补实际样本、运行引用、全部组合结果、失败与检查、区间或稳定性、适用范围及决定链接。设计与实际不一致时记录偏离，不能悄悄把设计改成结果。

| 内容 | 权威位置 | 更新者／动作 |
|---|---|---|
| 方案与比较约束 | PLAN 与 findings 设计区的明确引用 | plan／interpret 模块 |
| 实际配置、样本、划分及执行事实 | run 来源材料与记录 | run 模块 |
| 组合指标及产物索引 | 运行产物，findings 引用或派生展示 | run 模块 |
| 可比性、解释与限制 | findings 说明区，正式判断引用 decision | interpret 模块 |
| 下一步任务 | TASK／PLAN | plan 协议 |
| 最终采用 | release 映射 | release 模块 |

不得同时手工维护两份指标。跨计划使用同一 run 时链接原证据；当前 run schema 只有一个 question 字段，跨问题关联通过 findings 显式引用，不伪造多个同身份 run 记录。

## 3. 比较与类型要求

比较前核对输入版本、人群与纳排、目标、划分、预处理拟合范围、调参预算、指标与汇总、代码和方案修订。不同条件分组展示并解释，不能直接排总榜。分类需保留阳性类、逐样本概率／标签和混淆矩阵；回归需保留单位、原尺度误差和偏差；聚类需保留表示、距离、噪声及稳定性。字段细节见类型模板。

报告全变量与全条件；剔除前后、协变量调整前后按研究设计双报，不适用写理由。失败没有指标则保持缺失，绝不填零。技术失败不能直接判断假设错误。独立复算保存计算与差异处理，不能仅请模型复述结论。

## 4. 导入与回填

先运行 scripts/research_records.py --help，使用 conda Python 和绝对参数路径。实际 CLI 接口：

```text
<python> <skill>/scripts/research_records.py append --record <absolute-record.json> --root <absolute-run-root> --registry <absolute-registry.json>
<python> <skill>/scripts/research_records.py render --registry <absolute-registry.json> --page <absolute-findings.md> --question <question-id>
<python> <skill>/scripts/research_records.py export --record <absolute-record.json> --root <absolute-run-root> --dest <new-absolute-package-dir> --license <verified-license-uri>
```

尖括号需替换，不可原样执行。append 校验 schema、材料路径和内容哈希，相同 run 同内容不重复登记，同身份异内容拒绝。修改检查结论或补充材料也不能覆盖已导入记录；保留新证据与冲突说明，先安排版本化记录迁移，现有程序没有 update 命令。

render 按 question 筛选，只替换 research-results:start/end 之间的基础表，保留区外人工内容；标记名称是程序接口，不因目录改成 findings 而改名。程序不自动填完整科学字段、不自动判可比性，也不自动形成 decision。执行后人工核对必填区和引用。

## 5. 交付与可追溯性

使用 [交付模板](../assets/templates/release.md)，从论文／报告中的每项采用内容反查 decision → findings → run → 配置／输入／代码／环境。检查实际选定材料，不把整个探索目录自动当交付包。代码可追溯、验证完整且无影响结论的未解决疑点后再标正式采用；包校验和备份恢复另记状态。

RO-Crate 是描述与打包机制，不证明科学正确，也不自动授予材料发布许可。现有 export 导出 artifacts 清单与运行记录；校验器检查基础 RO-Crate 1.3，尚无 Workflow Run profile 映射。对外发送遵守实际授权，生成包不等于已发布。

## 最小科学健全性检查

1. 按数据字典检查值域、单位、缺失编码及约束：例如明确的量表原始分上限、合法 AUC 的 0—1 范围；仅对互斥且完备分组检查组数之和等于总数。异常先查变换、复合分和人群定义，不套用未经核实的量表阈值。
2. 对随机程序，固定输入、环境和种子复跑代表性样例；记录无法保证确定性的操作、硬件和差异。固定种子用于重现，不代替多重复稳定性检查。
3. 浮点比较预先定义绝对／相对容差、NaN 与缺失处理，保存检查报告。失败保持 checks=failed 或 pending，不以退出码为零覆盖。实际分析入口须显式抛错，不能只用可能被优化禁用的 Python assert。

这些领域检查由项目代码实现，本公共 schema 不识别所有指标的科学含义。
