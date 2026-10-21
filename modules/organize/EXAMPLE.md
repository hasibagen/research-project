# 创建与整理样例

合成案例，未执行真实迁移。结构依据：[整体项目](../../structures/project/GUIDE.md)。

## 新建单模态项目

请求：建立 demo-rest 项目，先准备研究文档，后续加入 EEG 代码和数据。
输入：/srv/research/demo-rest/codebase 是拟建代码根；/srv/research/demo-rest/storage 是拟用数据盘，须现场核对。新项目 VCS 选择遵守用户约定，不自动初始化。

动作：确定单模态 data/raw 与 data/interim → 生成已有工具支持的文档骨架 → 填 AGENTS 和 docs README 的实际树 → 在 PROJECT 标明数据和代码尚未创建 → 后续创建对应职责区时同时补其 README 和样例。

输出：根入口、docs/README、PROJECT、rest-qc 的 PLAN/TASK/LOG。数据盘、run、科学算法没有随文档生成而存在。
验收：生成文件与声明一致，链接可解析，计划校验通过；科学方案未审阅单独标明。

## 整理已有结果

请求：结果散落，允许整理说明，尚未授权搬迁。
动作：核对已有 results 和 outputs 的真实职责 → 登记两处结果范围及台账 → 补结果 README 的输入数据布局和查找样例 → 列待迁移清单及消费者。
输出：唯一权威入口与真实映射；原文件保持原位。不能按 run 名相同就合并记录，不能把未授权搬迁写成完成。

若后来授权迁移，先排除活跃作业，按清单复制与校验、更新消费者，再切换路径；删除源文件需在明确授权内。
