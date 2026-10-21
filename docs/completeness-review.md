# 完整性核对：2026-10-19

## 对话要求与落点

| 已确定要求 | 当前维护位置 |
|---|---|
| 一个大 skill，内部模块按需加载 | SKILL.md、modules/*/GUIDE.md |
| docs → project → plan → task，完整层级可见 | SKILL.md 完整树、project-structure.md |
| 多方向多计划，独立任务与接续 | modules/plan 的 protocol、exploration、PLAN／TASK 模板 |
| findings 与实际 results 区分 | results-workflow.md、analysis.md |
| 分类／回归／聚类固定字段 | analysis.md、analysis-types.md |
| 代码、数据、执行、证据、判断、采用之间的关系 | system-architecture.md |
| Snakemake、多组合运行、恢复及来源 | snakemake-workflow.md、assets/demo、references/contracts.md |
| 失败、阴性、不可比、独立复算与待复核 | results-workflow.md、daily-operations.md |
| MADR 的选项、取舍、落实与替代 | architecture-decision.md、scientific-decision.md |
| 交付采用、研究包和备份 | release.md、results-workflow.md、daily-operations.md |
| 开工收尾、周期审计、四口与终评 | daily-operations.md、project-structure.md |

## 本次验证

- skill 入口格式通过；唯一 SKILL.md 保持不变。
- 核对时入口、模块、模板与工作流正文的 124 个本地链接存在；链接集合其后随模板调整变化，以实际扫描结果为准。
- 计划／任务校验器 15 项测试通过；公共运行记录 6 项测试通过。
- 合成演示实际重新执行成功，覆盖 Snakemake、记录去重导入、由模板生成问题页、基础 RO-Crate 导出与 1.3 required 校验；回填问题页是最后一步。
- 演示材料：`<validation-output>/question.md`（本次输出），`<validation-output>/validation.json`（包校验报告）。

## 边界

链接存在不代表科学内容正确。本次未迁移真实科研项目、未执行真实模型或终评；没有新增超算执行器、跨语言适配、后台审计或完整 Workflow Run profile。类型模板和科学检查仍需按项目填充与核对。历史材料与原文快照保留，不能覆盖当前规范。
