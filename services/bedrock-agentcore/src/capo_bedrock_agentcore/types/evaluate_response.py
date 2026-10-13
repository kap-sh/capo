"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.evaluation_results


class EvaluateResponse(TypedDict, closed=True):
    evaluation_results: (
        "capo_bedrock_agentcore.types.evaluation_results.EvaluationResults"
    )
    """<p> The detailed evaluation results containing scores, explanations, and metadata. Includes the evaluator information, numerical or categorical ratings based on the evaluator's rating scale, and token usage statistics for the evaluation process. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.evaluation_results

    out["evaluationResults"] = (
        capo_bedrock_agentcore.types.evaluation_results.serialize_json(
            value["evaluation_results"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluateResponse:
    out: EvaluateResponse = {}  # type: ignore[typeddict-item]
    if data.get("evaluationResults") is not None:
        import capo_bedrock_agentcore.types.evaluation_results

        out["evaluation_results"] = (
            capo_bedrock_agentcore.types.evaluation_results.deserialize_json(
                data["evaluationResults"]
            )
        )
    else:
        raise DeserializationError("EvaluateResponse.evaluation_results required")
    return out


def redact_sensitive(value: EvaluateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "evaluation_results" in value:
        import capo_bedrock_agentcore.types.evaluation_results

        out["evaluation_results"] = (
            capo_bedrock_agentcore.types.evaluation_results.redact_sensitive(
                value["evaluation_results"]
            )
        )
    return out
