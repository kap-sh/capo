"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluatorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_statistics


class EvaluatorSummary(TypedDict, closed=True):
    evaluator_id: NotRequired["str"]
    """<p>The unique identifier of the evaluator.</p>"""
    evaluation_dimension_name: NotRequired["str"]
    """<p>The name of the dimension that this summary covers. This field is set only for evaluators that use a multi-dimensional rating scale, where each dimension is summarized separately. For single-scale evaluators, this field is not set.</p>"""
    statistics: NotRequired[
        "capo_bedrock_agentcore.types.evaluator_statistics.EvaluatorStatistics"
    ]
    """<p>The aggregated statistics for this evaluator.</p>"""
    total_evaluated: NotRequired["int"]
    """<p>The total number of sessions evaluated by this evaluator.</p>"""
    total_failed: NotRequired["int"]
    """<p>The total number of sessions that failed evaluation by this evaluator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorSummary) -> dict:
    out: dict = {}
    if "evaluator_id" in value:
        out["evaluatorId"] = value["evaluator_id"]
    if "evaluation_dimension_name" in value:
        out["evaluationDimensionName"] = value["evaluation_dimension_name"]
    if "statistics" in value:
        import capo_bedrock_agentcore.types.evaluator_statistics

        out["statistics"] = (
            capo_bedrock_agentcore.types.evaluator_statistics.serialize_json(
                value["statistics"]
            )
        )
    if "total_evaluated" in value:
        out["totalEvaluated"] = value["total_evaluated"]
    if "total_failed" in value:
        out["totalFailed"] = value["total_failed"]
    return out


def deserialize_json(data: dict) -> EvaluatorSummary:
    out: EvaluatorSummary = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorId") is not None:
        out["evaluator_id"] = data["evaluatorId"]
    if data.get("evaluationDimensionName") is not None:
        out["evaluation_dimension_name"] = data["evaluationDimensionName"]
    if data.get("statistics") is not None:
        import capo_bedrock_agentcore.types.evaluator_statistics

        out["statistics"] = (
            capo_bedrock_agentcore.types.evaluator_statistics.deserialize_json(
                data["statistics"]
            )
        )
    if data.get("totalEvaluated") is not None:
        out["total_evaluated"] = data["totalEvaluated"]
    if data.get("totalFailed") is not None:
        out["total_failed"] = data["totalFailed"]
    return out
