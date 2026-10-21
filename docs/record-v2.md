# 运行记录 v2 与兼容

新记录使用 run.schema.json（schema_version=2）；旧记录继续由 run-v1.schema.json 校验，append／render／export 均保留原版本。新增可选 machine 和 randomness 对象，字段不得随意扩展。machine 含 machine、node、gpu（字符串数组）、cpu_cores、env_ref；randomness 含 mode、seeds、repeats、design_ref、note。硬件未知可省略并在解释中注明，不能伪造设备信息。

env_ref 和 design_ref 必须是 artifacts 中的材料相对路径，内容哈希同其他材料核验。环境之前可作为 artifact 保存，v2 增加显式引用。机器名／节点名公开前核对是否需要脱敏。

不自动重写已导入 v1。需要升级时保存独立 v2 候选记录、核对真实来源，在新的版本化 registry 验证后由 PROJECT 切换权威映射，保留旧 registry 为历史；同 run_id 不得在当前 registry 直接替换。升级格式不能伪装为重新执行。现有 append 不提供更新 API。

领域值域和多 seed 充分性仍须项目检查，schema 只检查结构和引用。sources／旧实施报告中的 v1 描述为历史，当前契约以本页为准。
