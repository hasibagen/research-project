# 与 Superpowers 等流程包协作

## 职责和落点

research-project 规定研究记录的归属、状态来源与结果引用；Superpowers 提供需求澄清、设计、实施拆解、测试和审查方法。两者的 plan 不直接等同：研究 PLAN 是研究目标和方案，实施计划是实现某项改动的详细步骤。

```text
docs/plans/<plan_id>/
├── PLAN.md                    # 研究目标、方案、整体验收
├── TASK.md                    # 任务身份、唯一当前状态、验收证据
├── LOG.md                     # 执行与审查事件
├── DESIGN.md                  # brainstorming 形成的设计；按需
├── IMPLEMENTATION.md          # writing-plans 形成的实施步骤；按需
├── references/                # 参考材料；按需
├── decisions/                 # 重要决定；按需
└── backup/                    # 被替代的同一份文档版本；按需
```

先定位现有 plan，不能每次调用流程包就新建研究计划。多个独立实施事项可用 DESIGN-<topic>.md／IMPLEMENTATION-<topic>.md，彼此独立的事项不是历史版本，不放 backup。无需书面设计的简单变更不强制生成附加文件。

## 单一状态源与交接

- PLAN 引用设计和实施文件，不把 Superpowers 输出直接覆盖到研究 PLAN。
- IMPLEMENTATION 保留准确文件、步骤、测试和审查要求；每个执行任务关联 TASK 的稳定 task_id。研究任务和实施步骤可一对多，不必把每个测试步骤都变成独立研究任务。
- TASK 保存当前状态与验收证据。实施文件中的复选框若需保留，作为可重建的派生视图，注明状态来源和核对时间；不能两边独立维护。同一次操作先更新 TASK，再刷新视图；发生分歧查实际证据。
- 执行器、审查者和子 agent 接收明确的绝对 design_path、implementation_path、task_path、plan_id 及关联 task_id，不靠扫描默认目录猜入口。给定路径使用当前工作区实际位置，不带入其他 worktree 的旧绝对路径。
- 实施或设计通过审查不等于研究计划完成。科学有效性、终评准入、产物检查和正式采用仍按科研规范核对。
- 自动化任务面板只作执行视图，关键接续和证据回写 TASK／LOG；不成为第三份长期状态源。

## 默认路径适配

在项目 AGENTS 中声明本项目使用上述落点，不新增 docs/superpowers/specs、docs/superpowers/plans 或零散日期计划文件。已存在旧目录只读登记，未经迁移授权不搬动。其他流程包同样先映射产物职责，不一律增加独立目录。

截至 2026-10-20 核对的上游 main：
- [brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) 默认设计路径为 docs/superpowers/specs，并允许用户位置偏好覆盖。
- [writing-plans](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md) 默认实施路径为 docs/superpowers/plans，并明确用户偏好覆盖默认位置。

AGENTS 是给执行 agent 的项目约定，不是拦截器。安装版本可能不同，使用时读实际 skill；路径硬编码的脚本必须核对接口，不能声称 AGENTS 会自动改写脚本。保留流程中适用的设计确认、验证和审查要求；路径适配不扩大运行、外发、删除或仓库操作授权。

jj／Git 与工作区操作遵守项目规则；不把插件示例的 git commit、worktree 或清理命令原样套到 jj 仓库。需要隔离工作区时先核对工具能力、授权与路径，不在共享工作区自动切分支或清理文件。修改本 skill 的模板不自动修改 Superpowers 安装或任何实例项目。
