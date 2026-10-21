# 文档架构与使用

项目：{{PROJECT_ID}}。文档根：{{PROJECT_ROOT}}/docs。
整体入口：[AGENTS]({{PROJECT_ROOT}}/AGENTS.md)；资源与目标：[PROJECT]({{PROJECT_ROOT}}/docs/PROJECT.md)。

## 当前架构

```text
{{PROJECT_ROOT}}/docs/
├── README.md
├── PROJECT.md
└── plans/{{PLAN_ID}}/
    ├── PLAN.md
    ├── TASK.md
    └── LOG.md
```

PROJECT 维护目标、权威资源与计划入口；PLAN 维护研究方案和整体验收；TASK 维护任务状态、证据与接续；LOG 追加关键事件。FINDINGS、references、decisions 和 DELIVERY 有内容时再创建。

每份 PLAN 的“本计划资源与目录”集中列明本计划使用的数据、代码、结果和参考资料及完整路径、用途、读写边界和核对状态。查本计划的具体材料先看该节；PROJECT 保存全项目共享根，TASK 不再复制目录表。

## 本计划的使用样例

开始本计划时，先读 [方案](plans/{{PLAN_ID}}/PLAN.md)，再读 [任务](plans/{{PLAN_ID}}/TASK.md) 当前状态和 [日志](plans/{{PLAN_ID}}/LOG.md) 最近事件。按任务完成标准保存实际证据，更新 TASK，最后在 LOG 记关键变化。

例如增加一个分析方法设计，应写在该计划 DESIGN.md；生成的表图放到已登记结果根的独立 run，在 FINDINGS 引用。外部参考笔记放 references，自己计算得到的解释不放 references。上述可选文件尚未创建，示例不代表分析已执行。

## 修改与检查

新增／拆分文档时同步本树和受影响入口；任务状态不复制到 README。数据与结果位置查 PROJECT，具体输入版本查 run 来源记录。

校验入口：[模板与检查说明]({{SKILL_ROOT}}/docs/template-guide.md)。实际科学方案、数据访问和环境尚待填写；模板生成不能证明科学验收通过。
