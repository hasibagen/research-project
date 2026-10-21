# 代码修改样例

合成请求：为 demo-rest 的通道 QC 增加可配置阈值。

输入：/srv/research/demo-rest/codebase/code/README.md、实际配置加载器、清洗接口和 PLAN 的阈值定义。
动作：核对配置优先级与拟合范围 → 在已有计算模块增加参数 → 修改科学配置 → 立即核对解析及覆盖后的有效值 → 用合成异常通道验证行为 → 同步 code README 的接口和样例。

输出：源码、配置、实际检查记录；参数变化影响结果，后续运行使用新 run。旧结果保持来源，登记受影响消费者。

验收：阈值实际进入计算，输出目录由 path_manager 解析，未向 raw 写入；仅 YAML 解析通过不算完成。具体模块契约见 [代码样例](../../structures/code/EXAMPLE.md)。
