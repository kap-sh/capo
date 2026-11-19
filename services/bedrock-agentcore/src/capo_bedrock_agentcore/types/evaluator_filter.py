"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_dimension_name
    import capo_bedrock_agentcore.types.evaluator_id
    import capo_bedrock_agentcore.types.generation_filter_operator
    import capo_bedrock_agentcore.types.generation_filter_value
    import capo_bedrock_agentcore.types.result_aggregation


class EvaluatorFilter(TypedDict, closed=True):
    evaluator_id: "capo_bedrock_agentcore.types.evaluator_id.EvaluatorId"
    """<p>The unique identifier of the evaluator whose result to compare.</p>"""
    evaluation_dimension_name: NotRequired[
        "capo_bedrock_agentcore.types.evaluation_dimension_name.EvaluationDimensionName"
    ]
    """<p>The dimension of the evaluator's result to compare. Required for an evaluator that scores more than one dimension. Don't specify it for any other evaluator.</p>"""
    operator: "capo_bedrock_agentcore.types.generation_filter_operator.GenerationFilterOperator"
    """<p>How to compare the evaluation result with <code>value</code>.</p>"""
    value: "capo_bedrock_agentcore.types.generation_filter_value.GenerationFilterValue"
    """<p>The value to compare the evaluation result with. Use <code>doubleValue</code> for a score and <code>stringValue</code> for a label. <code>booleanValue</code> isn't supported.</p>"""
    aggregation: NotRequired[
        "capo_bedrock_agentcore.types.result_aggregation.ResultAggregation"
    ]
    """<p>How to combine the evaluator's per-trace or per-span results into one result for the session. Required for an evaluator that scores traces or spans. Don't specify it for an evaluator that scores sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorFilter) -> dict:
    out: dict = {}
    out["evaluatorId"] = value["evaluator_id"]
    if "evaluation_dimension_name" in value:
        out["evaluationDimensionName"] = value["evaluation_dimension_name"]
    import capo_bedrock_agentcore.types.generation_filter_operator

    out["operator"] = (
        capo_bedrock_agentcore.types.generation_filter_operator.serialize_json(
            value["operator"]
        )
    )
    import capo_bedrock_agentcore.types.generation_filter_value

    out["value"] = capo_bedrock_agentcore.types.generation_filter_value.serialize_json(
        value["value"]
    )
    if "aggregation" in value:
        import capo_bedrock_agentcore.types.result_aggregation

        out["aggregation"] = (
            capo_bedrock_agentcore.types.result_aggregation.serialize_json(
                value["aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluatorFilter:
    out: EvaluatorFilter = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorId") is not None:
        out["evaluator_id"] = data["evaluatorId"]
    else:
        out["evaluator_id"] = ""
    if data.get("evaluationDimensionName") is not None:
        out["evaluation_dimension_name"] = data["evaluationDimensionName"]
    if data.get("operator") is not None:
        import capo_bedrock_agentcore.types.generation_filter_operator

        out["operator"] = (
            capo_bedrock_agentcore.types.generation_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_bedrock_agentcore.types.generation_filter_operator.GenerationFilterOperator",
            "",
        )
    if data.get("value") is not None:
        import capo_bedrock_agentcore.types.generation_filter_value

        out["value"] = (
            capo_bedrock_agentcore.types.generation_filter_value.deserialize_json(
                data["value"]
            )
        )
    else:
        out["value"] = {"$unknown": {"name": ""}}
    if data.get("aggregation") is not None:
        import capo_bedrock_agentcore.types.result_aggregation

        out["aggregation"] = (
            capo_bedrock_agentcore.types.result_aggregation.deserialize_json(
                data["aggregation"]
            )
        )
    return out
