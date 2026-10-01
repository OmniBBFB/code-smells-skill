# 四类耦合问题审查报告

范围：独立检查 cases/case-01 至 case-12 的 sample.py 全部内容；使用 code-smells/SKILL.md 与 references/coupling.md 四张规则卡。所有案例分别判断，未假定案例间共享定义，未修改案例。四类均在每个案例内检查。

结果：4 项证据充分的发现（case-01、04、07、10），4 项上下文不足（case-03、06、09、12），4 个案例没有证据充分的发现（case-02、05、08、11）。发现的影响以当前代码为依据；潜在变化明确作为推断。

## 发现

case-04 已观察到不变量绕过，维护影响最直接；其他发现体现规则或结构耦合，未来修改风险为推断。

### case-04：S20 不恰当的亲密

位置：cases/case-04/sample.py:14-15
证据：Wallet 第2行要求通过 debit 同时更新余额与流水；debit 第8-11行校验金额并追加流水；Payment 直接修改 _balance。
影响：当前 pay 路径漏记流水且绕过金额校验，破坏 Wallet 的余额与流水一致性约束。
建议：Payment.pay 调用 wallet.debit(amount)，由 Wallet 维护完整扣款约束。
确定性：代码定义与可见调用支持该判断；不依赖隐藏架构或历史。

### case-01：S19 依恋情结

位置：cases/case-01/sample.py:9-13
证据：Subscription 的第2行契约声明其拥有包括宽限期计费资格在内的权益规则；InvoiceRenderer 用 active、overdue_days、grace_days 重建资格判断。
影响：计费资格规则调整时，展示器需要理解并同步修改 Subscription 的领域规则，规则与显示职责分离失败。
建议：在 Subscription 提供计费资格查询，渲染器只将结果转换为文字。
确定性：代码定义与可见调用支持该判断；不依赖隐藏架构或历史。

### case-07：S21 消息链

位置：cases/case-07/sample.py:21-22
证据：已定义 Employee→Department→Manager→Contact 四个业务对象；仅负责发送提醒的 ApprovalReminder 沿 department.manager.contact.email 导航获得邮箱。
影响：提醒客户端依赖部门、经理和联系方式的完整中间拓扑；若路径调整，发送提醒代码也要修改（潜在维护风险）。
建议：提供员工审批联系人查询或独立的审批收件人解析入口，使提醒器只依赖收件能力；避免为每个字段机械添加转发。
确定性：代码定义与可见调用支持该判断；不依赖隐藏架构或历史。

### case-10：S22 中间人

位置：cases/case-10/sample.py:12-22
证据：函数局部 Bridge 的 get/put 逐项转发 RowStore 的同名接口；lookup 已直接接受具体 RowStore，仅创建 Bridge(store) 后调用 get。
影响：在已读函数范围内增加两套 get/put 接口与一次实例化、转发路径，未提供转换、校验或替换边界；底层接口调整可能需要同步维护转发。
建议：将 lookup 的返回改为 store.get(key)，去掉局部 Bridge；此处调用者已经依赖 RowStore，不增加底层依赖扩散。
确定性：代码定义与可见调用支持该判断；不依赖隐藏架构或历史。

## 上下文不足

- case-03 / S19：缺少 product 定义、定价规则归属及 display_price 的调用边界；base_price 与 discount_rate 运算可能是产品领域规则或独立展示/定价策略，无法确认归属。 下一步应读取所缺定义及契约。
- case-06 / S20：缺少 wallet 定义、余额不变量和恢复/序列化访问契约；下划线写入值得核查，但可能属于受控恢复路径，不能仅凭字段名称判定越界。 下一步应读取所缺定义及契约。
- case-09 / S21：缺少 client、get_user、profile、address、city 的定义和返回类型及公开契约；无法确认各跳是否不同对象，可能为流式 API。 下一步应读取所缺定义及契约。
- case-12 / S22：Gateway 两个方法机械转发，但缺少调用者、backend 定义、接口契约及适配目的，不能确认该层是否提供稳定端口、隔离或替换价值。 下一步应读取所缺定义及契约。

## 已排除的候选

- case-02 / S19：Account 明确是公开只读报表投影；导出仅映射三个字段为 CSV，未重建领域规则。
- case-05 / S20：Payment 调用 Wallet.debit，校验、余额修改及流水追加均封装在 Wallet 内。
- case-08 / S21：filter、order_by、limit 均明确返回 self；该链是同一个 Query 的流式构建步骤，不是跨业务对象导航。
- case-11 / S22：RepositoryPort 明确提供稳定应用边界，load 依赖该端口；SqlRepository 适配 fetch_row，MemoryRepository 提供可替换实现，薄实现有实际边界价值。

## 局限

仅访问本目录的 skill、规则卡及 12 个 sample.py；未读取外部定义、调用者、测试、历史或隐藏评估答案。未运行样本，无需动态执行即可核实列出的结构证据。其他未列类别在可见代码中未发现足够候选，不代表对隐藏上下文的全面排除。本次系统覆盖限于 S19–S22，不宣称覆盖其余代码坏味道。无充分证据的案例不补造发现。
