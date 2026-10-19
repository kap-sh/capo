"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationEvaluatorReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluator_arn


class RecommendationEvaluatorReference(TypedDict, closed=True):
    evaluator_arn: "capo_bedrock_agentcore.types.evaluator_arn.EvaluatorArn"
    """<p>The Amazon Resource Name (ARN) of the evaluator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationEvaluatorReference) -> dict:
    out: dict = {}
    out["evaluatorArn"] = value["evaluator_arn"]
    return out


def deserialize_json(data: dict) -> RecommendationEvaluatorReference:
    out: RecommendationEvaluatorReference = {}  # type: ignore[typeddict-item]
    if data.get("evaluatorArn") is not None:
        out["evaluator_arn"] = data["evaluatorArn"]
    else:
        out["evaluator_arn"] = ""
    return out
