# 文档结构样例

与 [完整项目](../project/EXAMPLE.md) 共用合成项目 demo-rest；下列内容为填写示例，未执行研究。

## docs README 示例

本区：/srv/research/demo-rest/codebase/docs。维护研究方案、任务、解释与采用；计算文件由结果根保存。

```text
/srv/research/demo-rest/codebase/docs/
├── README.md
├── PROJECT.md
└── plans/rest-qc/
    ├── PLAN.md
    ├── TASK.md
    ├── LOG.md
    └── FINDINGS.md
```

入口顺序：PROJECT → rest-qc/PLAN → TASK 当前接续 → LOG 最近事件。FINDINGS 用于解释已核对的表图。数据与结果路径查 PROJECT，不另设 PROGRESS 或重复待办表。

## 项目、计划、任务各自的架构

PROJECT 示例：project_id 为 demo-rest，目标是验证合成 EEG 质控流程；代码根 /srv/research/demo-rest/codebase，数据根 /srv/research/demo-rest/storage/data，结果根 /srv/research/demo-rest/storage/results。计划入口为 rest-qc，任务状态只引用 TASK。

PLAN 示例：plan_id 为 rest-qc，研究问题为“通道质控输出是否符合预设合成信号特征”；先确定异常定义，再比较预设异常通道与检测结果。整体验收是输出可追溯、合成测试符合预期、限制得到说明；不以显著性为完成条件。

TASK 头部填写例（供理解字段；实际使用配套完整模板）：

```yaml
plan_id: rest-qc
owner: researcher
updated: '2026-10-21'
tasks:
  - task_id: inspect-qc
    status: 未开始
    done_when: 核对通道计数、单位与合成异常位置，保存检查证据
    depends_on: []
    evidence: []
```

任务步骤和接续写正文的 inspect-qc 小节，状态不在正文再维护一份。未开始任务没有验收证据，不能为了展示完整而填“完成”。

LOG 示例事件：2026-10-21，已形成合成质控设计，尚未执行；下一步核对入口和配置。它是样例事件，不声称真实项目发生过。

FINDINGS 示例架构：问题→设计／比较条件引用→运行与产物引用→实际观察→解释与限制→下一步。待结果到来后填真实观察；预期异常位置属于 PLAN／测试输入，不能提前写成结果。

## 常见创建场景

新增方法设计放 /srv/research/demo-rest/codebase/docs/plans/rest-qc/DESIGN.md；实施步骤放同目录 IMPLEMENTATION.md；外部论文笔记放 references；自己算出的质控解释放 FINDINGS。生成表图留结果 run，以绝对路径和运行身份引用。

拆出独立任务文件时 TASK 留索引，状态转由实际 task 文件维护；不能清单和独立文件各改一份。改变主分析方法时保存主责计划 decisions 记录及旧方案历史。

## 本计划资源与目录示例

以下可作为 rest-qc 的 PLAN 前部章节，置于目标与范围之后。所有路径均为合成场景，未访问这些位置；“拟建”和“已有”是示例角色，实际计划必须用现场核对结果替换。

| 类别／角色 | 本计划使用的目录或关键文件（绝对路径） | 用途、范围与读写边界 | 核对状态与日期 |
|---|---|---|---|
| 数据：原始输入 | /srv/research/demo-rest/storage/data/raw/batch-01/ | 本次 EEG 原始批次，只读；batch-02 不纳入 | 合成示例，未核对 |
| 数据：纳入依据 | /srv/research/demo-rest/codebase/configs/rest-qc-inclusion.tsv | 固定本计划样本选择；只存脱敏 ID，变更需修订方案 | 拟建清单，尚未生成 |
| 数据：共享产品 | /srv/research/demo-rest/storage/data/interim/clean-rest/v1/README.md | 后续需要复用时登记；生产来源由产品说明维护 | 拟建产品，尚未生成 |
| 代码：实现与入口 | /srv/research/demo-rest/codebase/code/preprocessing/；/srv/research/demo-rest/codebase/code/run_analysis.py | 前者是本计划实现区，后者装配执行；允许修改范围按任务确定 | 合成示例，未核对 |
| 代码：配置与环境 | /srv/research/demo-rest/codebase/configs/analysis.yaml；/srv/research/demo-rest/codebase/environment.yml | 科学参数及环境恢复入口；实际值随 run 固定 | 合成示例，未核对 |
| 结果：新运行范围与台账 | /srv/research/demo-rest/storage/results/；/srv/research/demo-rest/storage/results/registry.json | 新执行进入本根的 runs；台账显式登记，不覆盖旧 run | 尚未运行、未核对 |
| 结果：旧基准 | /srv/research/demo-rest/storage/legacy-results/qc-baseline/tables/channel-qc.tsv | 旧方案对照，只读；保留原结果范围，不迁入新结果根 | 合成已有基准，未核对 |
| 参考：方法说明 | /srv/research/method-library/eeg-qc/README.md | 阈值定义和单位依据，只读；使用前核对其版本 | 合成外部参考，未核对 |
| 参考：旧方案 | /srv/research/demo-rest/codebase/docs/plans/pilot-qc/PLAN.md | 查旧基准的纳入规则和方法，不能当成当前方案 | 合成历史方案，未核对 |

最终输入范围是 batch-01 中纳入清单指定的记录，不是 data/raw 下所有批次；清单形成前不得宣称样本已固定。共享 clean-rest/v1 是拟建产品，当前不能作为可读输入。

资源关系：batch-01＋纳入清单 → preprocessing 与 run_analysis＋analysis 配置 → 新结果 run 的通道 QC 表 → 与旧基准比较的汇总 run → rest-qc/FINDINGS 解释。外部方法 README 支持阈值定义，旧 PLAN 支持基准口径核对。

TASK 的目标与输入只写“资源入口见 PLAN 的本计划资源与目录；本任务额外使用哪份具体产物”，不重抄上述表。后续增加一个 run 时更新台账和证据引用；只有计划采用的关键资源变了，才更新此表。

## 检查方式

用 check_plans.py 检查身份、依赖和证据路径；再人工核对方案和解释是否把预期写成事实、引用是否可定位。这些示例片段不是完整可校验项目；可生成的初始模板见 [模板指南](../../docs/template-guide.md)。
