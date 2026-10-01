# 第一版评估记录

日期：2026-10-01。

## 方法

12 个原创 Python 片段：每类耦合问题各有正例、合理反例和上下文不足例。片段语法已检查；它们作为静态审查材料，没有执行其中的业务操作。

两名独立 agent 分别读取有 skill 和无 skill 的隔离目录。均使用相同任务范围、输出字段和匿名 case 编号；无完整对话历史，没有收到答案或疑似问题提示。有 skill 组额外读取 SKILL.md 与引用；无 skill 组没有这些材料。答案表与匿名映射不在评估者允许访问的目录中。

两组都要求四类审查及结构化输出；因此这是“额外 skill 指令”的比较，不是与完全不提示代码坏味道的审查比较。未进行多次采样，也未测量速度、成本或普遍准确率。

## 结果

| 检查 | 有 skill | 无 skill |
|---|---:|---:|
| 正例目标分类 | 4/4 | 4/4 |
| 反例目标排除 | 4/4 | 4/4 |
| 信息不足时保留判断 | 4/4 | 4/4 |
| 确定发现具备位置／证据／影响／建议 | 全部 | 全部 |
| 被审查案例文件变化 | 无 | 无 |

确定发现均为 case-01/S19、case-04/S20、case-07/S21、case-10/S22；四个信息不足案例均没有被放入确定发现。两组没有额外确定标签。

主 agent 对照原始代码复核了四条确定发现的位置、证据、影响与建议，以及反例的排除理由和缺失上下文说明。结构校验、23 项索引编号、引用存在性和 UI 元数据检查通过；评分器的正确分类及错误分类行为检查通过。

这一轮未发现需要修改规则的失败，因此没有为追求分数追加规则。小型案例集上的分类结果一致，不能据此声称 skill 优于模型原有能力。规则与案例覆盖相近，下一轮应加入未见过的真实代码、跨文件调用、公开接口契约与多种语言，并保存误报／漏报再作针对性修订。

## 保存的材料

- `expectations.json`：案例目标标签与预期结果。
- `cases/`：12 个原创片段，按语义命名供维护。
- `runs/baseline/`、`runs/with-skill/`：匿名映射、原始 JSON、报告和评分结果。
- `score.py`：确定性分类与字段完整性评分。它不判断自然语言证据是否正确，仍需人工复核。

正常 skill 审查不需要读取 `evals/`。开发评估时先从 `cases/` 建立新隔离目录，将语义目录名改为匿名编号，仅复制对应代码；把答案表留在评估者目录外。有 skill 组另复制 SKILL.md 和 references；两组输入相同审查范围与输出协议。

从成品根目录复算本次有 skill 结果：

```bash
python3 evals/score.py --expectations evals/expectations.json --mapping evals/runs/with-skill/mapping.json --results evals/runs/with-skill/results.json --output /tmp/code-smells-with-skill-score.json
```

复算无 skill 结果：

```bash
python3 evals/score.py --expectations evals/expectations.json --mapping evals/runs/baseline/mapping.json --results evals/runs/baseline/results.json --output /tmp/code-smells-baseline-score.json
```

## 触发检查的边界

已人工审查 description 的边界：指定代码的坏味道／耦合审查应适用；概念问答、一般功能实现与格式整理不适用。两组测试为明确指定任务，并非客户端自动选择技能的端到端测试。默认启用隐式调用；实际自动发现需要把本目录作为 skill 加入客户端支持的发现位置，本次只交付用户指定目录，未改变客户端配置。
