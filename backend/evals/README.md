# Eval Skeleton

这个目录用于后续接入 DeepEval（大模型评测框架）。

第一阶段先不直接调用真实评测模型，只沉淀 Golden Set（黄金测试集）样本，让项目从一开始就有可回归的数据结构。

## 样本字段

```json
{
  "id": "case_001",
  "query": "智能门锁多少钱，有库存吗，保修多久",
  "expected_route": "mixed",
  "expected_tools": ["product_tool", "policy_tool"],
  "expected_evidence_keywords": ["智能门锁", "保修"],
  "expected_behavior": "基于证据回答，不编造额外承诺"
}
```

## 后续指标

1. Router Accuracy（路由准确率）
2. Tool Correctness（工具正确性）
3. Faithfulness（忠实度）
4. Answer Relevancy（答案相关性）
5. Hallucination Rate（幻觉率）
