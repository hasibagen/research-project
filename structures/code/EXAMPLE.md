# 代码结构及子模块样例

合成项目 demo-rest，根为 /srv/research/demo-rest/codebase；这是接口设计示例，未实现或执行以下算法。

## code README 示例

职责：将合成 EEG 通道数据转换为质控表和图。输入批次与数据版本来自配置，输出通过 path_manager 指向独立 run。

```text
/srv/research/demo-rest/codebase/code/
├── README.md
├── run_analysis.py
├── preprocessing/clean.py
├── statistics/summarize.py
├── tests/fixtures/              # 小型合成验证输入
├── notebooks/                  # 探索内容，按需创建
└── utils/
    ├── path_manager.py
    └── config.py
```

依赖：run_analysis → preprocessing/statistics；入口通过 utils 获取有效配置和绝对路径。utils 不依赖某个研究计划；统计模块接收显式输入，不扫描全部 runs 猜“最新”。

## 子模块架构与样例

| 子模块 | 输入→输出契约 | 使用样例与检查 |
|---|---|---|
| run_analysis | 配置身份、输入版本→独立 run 及记录 | 选择 batch-01 和 qc 配置，先验证，再执行；已有 run 不覆盖 |
| preprocessing | 按通道组织的数值序列、采样率、缺失规则→清洗序列及 QC 标记 | 合成恒定通道应被标记，输入数组不得原位改写；单位和形状保持约定 |
| statistics | QC 标记、通道 ID→通道计数和异常比例表 | 合成 4 通道中 1 个异常，异常比例预期 0.25；缺失通道另报，不算成正常 |
| path_manager | 已验证机器根、输入版本和 run_id→绝对输入／输出路径 | raw 路径仅供读取，输出在本次 run；测试路径不得越入 raw |
| config | 文件值、默认值、显式覆盖→有效配置 | 对同一个阈值验证覆盖后的最终值，并将该值写入 config_used |

小项目用上述表配合代码 docstring 即可；preprocessing 日后分多步、有独立调用者时，把其内部树、步骤接口和样例放到自己的 README，再从本页引用。

## 配置架构示例

科学配置说明 batch-01、通道质控方法、阈值及随机性；机器配置说明数据根 /srv/research/demo-rest/storage/data、结果根 /srv/research/demo-rest/storage/results 和已核对环境。参数键与命令行形式由项目实际接口确定，不把本例当已有 API。

新增阈值时先读 config 加载器，检查默认值和覆盖顺序，用代表性输入验证，再保存实际生效配置。不得只确认 YAML 可以解析。

## 最小操作样例

读取 rest-qc 方案 → 查入口实际 --help → 核对路径及配置 → 运行既有合成测试 → 在授权后启动独立 run → 核对表和日志。所有命令参数须依据实现填写；本例未提供虚构可执行命令。

环境在 /srv/research/demo-rest/codebase/environment.yml 声明，解释器使用项目登记的 conda 绝对路径。代码身份和未提交改动在运行来源中保存。
