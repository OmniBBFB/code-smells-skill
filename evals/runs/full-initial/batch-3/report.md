# 匿名案例独立代码审查

范围：只读取本目录 code-smells/ 规则及 cases/case-01 至 case-23 的 sample.py。23个案例彼此独立，以全部23类逐案筛选。未读取其他目录、答案或历史，未修改案例。供应材料不包含 .codegraph 索引；直接读取已知文件。

六组规则均完整读取：膨胀、面向对象、阻碍修改、可清理、耦合、类库边界。所有候选按证据、例外、缺失上下文判断；没有候选的类别不机械列举。8个案例有8个确定发现；同根因标签合并，次要标签写在正文。确定性指所给材料，影响描述未来变化时是推断，并非历史事实。

读取规则：code-smells/SKILL.md；references/smell-index.md、bloaters.md、object-orientation.md、change-preventers.md、dispensables.md、coupling.md、library-boundaries.md（均位于 code-smells/）。

读取材料：cases/case-01/sample.py、cases/case-02/sample.py、cases/case-03/sample.py、cases/case-04/sample.py、cases/case-05/sample.py、cases/case-06/sample.py、cases/case-07/sample.py、cases/case-08/sample.py、cases/case-09/sample.py、cases/case-10/sample.py、cases/case-11/sample.py、cases/case-12/sample.py、cases/case-13/sample.py、cases/case-14/sample.py、cases/case-15/sample.py、cases/case-16/sample.py、cases/case-17/sample.py、cases/case-18/sample.py、cases/case-19/sample.py、cases/case-20/sample.py、cases/case-21/sample.py、cases/case-22/sample.py、cases/case-23/sample.py。

局限：没有运行配置、额外定义、外部调用者或提交历史；不以缺调用、类小、行数、参数数或点号数直接定罪。results.json 提供全部案例的结构化结果。

## case-01

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S05：Endpoint 已将 host/port/tls 表达为不可变整体，connect/fetch 直接接收对象。
- 已排除 S16：只见明确端点配置值记录及整体传递，没有外部重建领域规则的路径。
- 已排除 S15：命名端点值对象具有实际分组语义，不能因缺行为判为懒惰类。

## case-02

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S02：record/balance/last_entry 共享同一 append-only entries，契约及实现显示内聚账本职责。
- 已排除 S10：所见操作均围绕同一历史记录，没有独立变化轴证据。

## case-03

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S02：bill/print/schedule 只有省略实现；缺成员状态、职责实现和调用者，无法确认是否为已委托的内聚门面。
- 上下文不足 S10：缺各方法规则实现及变化归属，名称不能证明独立变化轴集中。

## case-04

- **S09 / cases/case-04/sample.py:3-14**：LocalBackupSms 第7行明确与 LocalSms 同投递/失败契约且均为本地类；send(phone, body) 与 transmit(body, phone) 强迫 notify 以 isinstance 分流。
  维护影响：新增可互换实现时，客户端必须了解类型及参数顺序；接口差异传播至通知调用。
  最小建议：统一本地类的 send(phone, body) 接口并让 notify 直接调用。


## case-05

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S17：plugin_hook 无可见调用，但明确缺插件注册、导出及外部入口配置，不能判定未使用。

## case-06

- **S04 / cases/case-06/sample.py:1-12**：十个位置参数同时混合发件人、收件人和服务配置；sample 连续传递姓名、电话、地址及两个布尔值，契约明确收件人详情共同演化。
  维护影响：调用者需记住同类型字段及布尔值顺序；收件人字段增加会同步改签名和调用。
  最小建议：优先引入 Recipient 参数对象；按实际用途将发件人及服务选项分组，保留清晰关键词参数。


## case-07

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S01：weekday_labels 是一个内聚声明式表，无交织阶段或难辨控制流。

## case-08

- **S05 / cases/case-08/sample.py:1-13**：connect、check、fetch、refresh 四个签名重复 host/port/tls，文档明确同属一个服务端点，调用均整体转传。
  维护影响：端点增加配置时必须调整四处签名及转传，容易漏传或组合错配。
  最小建议：用 Endpoint 命名记录集中端点数据，调用内部直接传对象。


## case-09

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S06：first/second 都判 item.kind==1，但缺 kind 语义和解码/领域边界，无法区分分散领域分派与合法协议映射。
- 上下文不足 S03：数字 kind 候选缺允许值和领域约束；不能凭裸数字认定基本类型不足。

## case-10

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S22：fetch/save 机械转发已可见，但无调用者及网关端口、替换、兼容或鉴权契约，尚不能否认边界价值。

## case-11

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S19：价格计算可见，但缺 product 定义、折扣规则归属及 display_price 边界；可能为展示或独立计价策略。

## case-12

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S21：缺每跳返回类型及公开导航契约；无法确认是不同业务对象、不必要拓扑还是稳定公开结构/流式API。

## case-13

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S11：cart/checkout 都复用唯一 shipping 规则，门槛变更集中。
- 已排除 S14：两个调用入口不独立复制运费计算；重复调用不等于重复知识。

## case-14

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S20：Payment 只调 Wallet.debit，由钱包统一校验余额并更新账本，未越界维护内部协议。

## case-15

- **S23 / cases/case-15/sample.py:1-12**：VendorDay 明确为不可编辑且仅有 y/m/d 的第三方 API；receipt_day 第7行和 export_day 第10行独立拼装同一 ISO 日期表示，契约明确需求与缺失能力。
  维护影响：两个调用者都依赖库字段及格式细节，格式或兼容需求调整时容易分叉；同根因亦属 S14。
  最小建议：提炼本地 iso_day(day) 辅助函数，两个入口共用，避免修改第三方或全局 monkey patch。


## case-16

- **S13 / cases/case-16/sample.py:1-11**：第2-4行注释必须把 x/y/z 解释为分、优惠金额及运费，并解释 10000、0.9；实现仍以 f、x、y、z 及裸数字表达。
  维护影响：读者需对照注释重建计价意图；优惠或运费计算变化时两份解释可能不一致。
  最小建议：改为表达含义和单位的函数及变量名，提取折扣率和门槛常量，保留解释政策原因的注释。


## case-17

- **S01 / cases/case-17/sample.py:1-35**：close_day 直接展开校验分流(3-11)、客户汇总(12-15)、税额构造(16-19)、事务写库(20-27)、HTML存储(28-32)、邮件(33-34)，且文档明确副作用失败政策独立。
  维护影响：修改邮件或存储失败处理需在同一函数理解数据库已提交的时点；展示和计税实现也增加整体流程理解负担。
  最小建议：提炼验证、发票计算、事务保存、报告生成和通知阶段，保留协调入口并明确每阶段输入及失败顺序。


## case-18

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S03：Money 明确 cents 单位、币种允许值及验证，并作为整体传入 reserve。
- 已排除 S16：领域规则已经集中于不可变 Money.__post_init__，没有外部重建状态约束。

## case-19

- **S10 / cases/case-19/sample.py:1-22**：BusinessDesk 内直接实现税率0.17(8-9)、SQL表结构与发票映射(11-13)、员工徽章文案(15-16)、排班cron调用(18-19)、员工名册(21-22)。
  维护影响：可推断税法、数据库表结构、徽章展示及排班接口这几种独立变化都会进入同一类，扩大审阅和回归范围；职责簇同时支持 S02。
  最小建议：先分离计税策略与发票持久化，再按需要提炼员工展示和排班职责，保留轻量协调入口。


## case-20

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S01：只有阶段注释，函数体明确省略；缺具体认知负担、控制流及阶段状态。
- 上下文不足 S13：缺注释对应实现，无法确认它补偿晦涩结构或只是有益说明。

## case-21

在本次已检查范围内，未发现证据充分的代码坏味道。

- 已排除 S12：第13行明确文档变体和输出介质独立且允许全组合，未见强制一一配套构造/注册。

## case-22

在本次已检查范围内，未发现证据充分的代码坏味道。

- 上下文不足 S10：tax/html/save 仅接口片段，明确缺规则归属及实现；可能是协调入口，不能证明不同变化原因集中实现。
- 上下文不足 S02：缺成员实现、状态簇和使用路径，三种方法名不证明大类。

## case-23

- **S07 / cases/case-23/sample.py:2-16**：_running_sum/_running_tax 初始化 None，仅 prepare 写入，finish 假定已准备；quote 每次创建对象并依次 prepare/finish，数据只是本次报价中间结果。
  维护影响：finish 的正确性依赖未在类型中表达的调用顺序；额外调用可能读未准备或旧结果。
  最小建议：把单次报价的 sum/tax 保持为局部变量并直接返回；若两阶段确有契约需求，使用明确的已准备结果对象。

