# 整体项目结构

本模块管理职责区之间的关系、导航和结构变更；区内细节由相应结构模块维护。创建或整理使用 [organize 动作](../../modules/organize/GUIDE.md)，日常接续使用 [project 动作](../../modules/project/GUIDE.md)。

## 责任边界与依赖

文档提出问题、解释证据；代码与配置执行方法；数据提供固定输入；结果保留实际执行事实；交付固定采用版本。计划、计算执行和存储边界不要求一一对应。项目群与多仓例外见 [范围与共享关系](scope.md)。

```text
<代码仓绝对路径>/
├── AGENTS.md                  # 当前整体架构、操作约束、各区入口
├── README.md                  # 目的、整体树、最小使用样例和导航
├── .gitignore
├── docs/                      # 文档结构模块
│   ├── README.md              # 文档树与读写样例
│   ├── PROJECT.md             # 权威资源映射、计划入口
│   └── plans/<plan_id>/       # PLAN、TASK、LOG；其他按需
├── code/                      # 或已有语言包；代码结构模块
│   ├── README.md              # 依赖方向、执行与检查样例
│   ├── tests/                 # 有测试时创建；小型合成样例
│   ├── notebooks/             # 探索时按需，不作为唯一执行入口
│   └── ...
└── configs/                   # 科学配置、机器配置分开；说明可并入 code README

<数据盘项目绝对路径>/
├── README.md                  # 数据架构、来源、结果入口和读取样例
├── naming/                    # 有身份映射时受控保存
├── data/                      # 单模态 raw/interim，多模态再加模态层
└── results/                   # 结果结构模块；也可在另一磁盘
    ├── README.md              # 结果与输入数据架构、定位样例
    ├── registry.json          # 完成记录的显式登记；沿用现有格式
    └── runs/<run_id>/
```

目录按实际工作创建；小项目可以同盘，各根仍登记绝对路径。上树是职责关系，不要求所有目录存在，不强制代码目录叫 code。交付说明默认归计划 DELIVERY，稿件可留已有 paper；独立包仅在交付需要时生成，见 [交付结构](../delivery/GUIDE.md)。

## 各区入口必须说明什么

采用 [职责区 README 模板](../../assets/templates/area-readme.md)，在实际存在的职责区维护以下信息：

1. 本区职责、与其他区的关系及权威来源。
2. 以实际路径为根的内部目录树；存在、拟建、未核对分清。
3. 主要输入输出、依赖、版本身份和消费者入口。
4. 最容易出错的本地约束、创建位置与修改后需同步的入口。
5. 一个填好身份与路径的使用样例；可执行命令先核实，未执行标明。
6. 检查入口、检查范围及最近实际核对情况。

这里的“模块”是项目中有独立职责的部分。code 下 preprocessing、statistics 等模块复杂到需要独立维护时，在各自 README 说明内部架构和样例；小模块合写在 code README 的对应章节即可。docs 下计划由 PLAN/TASK/LOG 承担说明；数据集由自己的 README 承担字典、版本与来源；run 由 record/config/provenance/CHECKS 承担证据，不强制再复制一份 README。

## 事实归属与同步

| 内容 | 权威位置 | 其他入口怎样使用 |
|---|---|---|
| 目标、资源身份与权威路径映射 | PROJECT | AGENTS 和区 README 提供导航摘要与链接 |
| 当前实际整体树、操作规则 | AGENTS | 根 README 提供人类总览，引用 AGENTS |
| 区内结构、接口与使用样例 | 对应区 README 或已有等价入口 | 总入口链接，不复制整篇 |
| 任务状态 | TASK | PLAN、PROJECT 只引用 |
| 输入版本、运行事实 | 数据产品记录及 run 记录 | README 只说明如何查找 |

新增或改变职责区、路径、公共入口、依赖接口时，同步受影响说明并核对链接。只修改一个计算函数且接口不变，无须重写全项目架构。结构漂移应在创建文件时避免，不等积累后再批量整理。

## 创建、整理与验证

创建按需要实例化；旧项目先登记真实布局。整理按 [落点规则](placement-rules.md) 和 [整理模板](../../assets/templates/structure-adoption-plan.md) 列源、目标、消费者、校验与恢复，禁止在仓根或数据盘根增建混装临时／归档桶。入口与版本控制见 [entrypoints](entrypoints.md)。

检查一次完整链路：根入口→职责区→具体对象→上游来源；再从一项结果回查数据、代码、配置和计划解释。目录存在只证明结构，不证明科学有效。现有计划／运行校验器检查各自的字段与文件，不提供自动全盘架构保证。

## 样例与模板

[完整项目与逐区样例](EXAMPLE.md) 展示单模态项目和多模态扩展。[根模板](../../assets/templates/project-scaffold/README.md)、[AGENTS 模板](../../assets/templates/project-scaffold/AGENTS.md) 与 [区 README 模板](../../assets/templates/area-readme.md) 用于实例化；模板中的待填写内容不作为检查证据。
