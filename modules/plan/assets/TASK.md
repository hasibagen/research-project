---
plan_id: example-plan
owner: 待指定
updated: "2026-10-20"
tasks:
  - task_id: baseline
    status: 未开始
    done_when: 基线产物与验证证据可定位且满足本任务标准
    depends_on: []
    evidence: []
    reason: ""
    resume_when: ""
---

# 任务清单与接续

任务状态只更新上面的列表；各任务可覆盖 owner、updated。证据相对项目根；步骤和解释按 task_id 写在下方。关键事件追加计划 LOG.md，不在每任务重复维护日志。

## baseline

### 目标与输入
交付范围、所属里程碑、输入版本与前置条件；科学参数引用配置。
数据、代码、结果和参考资料统一查所属 PLAN 的“本计划资源与目录”；本任务仅补充特定输入或产物身份，不复制资源总表。

### 执行与验收说明
步骤、检查办法、资源限制；验收证据写头部 evidence，详细报告只引用。

## 当前接续
研究问题、阶段、已有认识、在跑、卡点、待解释、下一步与核对边界。运行机器、作业号和核对时间引用权威运行记录。

## 扩展规则
确需并行独立维护时拆为 tasks/T01-name.md 等，每份使用单任务头部（plan_id、task_id、owner、updated、status、done_when、depends_on、evidence）。PLAN.task_files 改为实际文件列表，本页仅留入口；不得同时保留两份任务状态。
