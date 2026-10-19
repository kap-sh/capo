"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationEvaluationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.recommendation_evaluator_list


class RecommendationEvaluationConfig(TypedDict, closed=True):
    evaluators: "capo_bedrock_agentcore.types.recommendation_evaluator_list.RecommendationEvaluatorList"
    """<p>The list of evaluators to use for assessing recommendation quality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationEvaluationConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.recommendation_evaluator_list

    out["evaluators"] = (
        capo_bedrock_agentcore.types.recommendation_evaluator_list.serialize_json(
            value["evaluators"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecommendationEvaluationConfig:
    out: RecommendationEvaluationConfig = {}  # type: ignore[typeddict-item]
    if data.get("evaluators") is not None:
        import capo_bedrock_agentcore.types.recommendation_evaluator_list

        out["evaluators"] = (
            capo_bedrock_agentcore.types.recommendation_evaluator_list.deserialize_json(
                data["evaluators"]
            )
        )
    else:
        out["evaluators"] = []
    return out
