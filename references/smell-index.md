# 23 项代码坏味道索引

本索引用于全范围筛选与按需加载；23 项均有完整规则卡。索引提示只产生候选，确定判断须读取对应规则并核实证据和例外。分组沿用网站侧栏；S23 在总目录正文归于耦合组。[原目录](https://refactoringguru.cn/refactoring/catalog)

| 编号 | 分类 | 中文与英文 | 概念提示 | 规则文件 |
|---|---|---|---|---|
| S01 | 膨胀 | 长方法 Long Method | 多个阶段难以理解 | [规则](bloaters.md) |
| S02 | 膨胀 | 大类 Large Class | 无关职责集中 | [规则](bloaters.md) |
| S03 | 膨胀 | 基本类型偏执 Primitive Obsession | 基本类型承担领域概念 | [规则](bloaters.md) |
| S04 | 膨胀 | 长参数列表 Long Parameter List | 输入难以理解和组织 | [规则](bloaters.md) |
| S05 | 膨胀 | 数据泥团 Data Clumps | 同组数据反复结伴 | [规则](bloaters.md) |
| S06 | 面向对象 | switch 判断 Switch Statements | 重复类型分支 | [规则](object-orientation.md) |
| S07 | 面向对象 | 临时字段 Temporary Field | 状态仅部分阶段有效 | [规则](object-orientation.md) |
| S08 | 面向对象 | 被拒绝的遗赠 Refused Bequest | 子类不适用父类契约 | [规则](object-orientation.md) |
| S09 | 面向对象 | 接口不同的替代类 Alternative Classes with Different Interfaces | 相似能力接口不一致 | [规则](object-orientation.md) |
| S10 | 阻碍修改 | 发散式变化 Divergent Change | 一类承受多种变化原因 | [规则](change-preventers.md) |
| S11 | 阻碍修改 | 霰弹式修改 Shotgun Surgery | 一项规则分散多处 | [规则](change-preventers.md) |
| S12 | 阻碍修改 | 平行继承体系 Parallel Inheritance Hierarchies | 两套体系配套变化 | [规则](change-preventers.md) |
| S13 | 可清理 | 注释 Comments | 注释掩盖晦涩实现 | [规则](dispensables.md) |
| S14 | 可清理 | 重复代码 Duplicate Code | 同一知识重复表达 | [规则](dispensables.md) |
| S15 | 可清理 | 懒惰类 Lazy Class | 独立职责收益过低 | [规则](dispensables.md) |
| S16 | 可清理 | 数据类 Data Class | 领域规则散落外部 | [规则](dispensables.md) |
| S17 | 可清理 | 死代码 Dead Code | 无有效使用路径 | [规则](dispensables.md) |
| S18 | 可清理 | 推测性泛化 Speculative Generality | 未证实需要的抽象 | [规则](dispensables.md) |
| S19 | 耦合 | 依恋情结 Feature Envy | 行为归属不合理 | [规则](coupling.md) |
| S20 | 耦合 | 不恰当的亲密 Inappropriate Intimacy | 内部边界被侵入 | [规则](coupling.md) |
| S21 | 耦合 | 消息链 Message Chains | 暴露不必要的对象拓扑 | [规则](coupling.md) |
| S22 | 耦合 | 中间人 Middle Man | 无收益的机械转发 | [规则](coupling.md) |
| S23 | 其他 | 不完整的类库类 Incomplete Library Class | 不可修改的外部类缺能力 | [规则](library-boundaries.md) |
