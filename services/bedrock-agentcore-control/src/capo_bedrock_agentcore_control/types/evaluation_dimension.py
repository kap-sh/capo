"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluationDimension``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dimension_rating_scale
    import capo_bedrock_agentcore_control.types.evaluation_dimension_instruction
    import capo_bedrock_agentcore_control.types.evaluation_dimension_name


class EvaluationDimension(TypedDict, closed=True):
    dimension_name: "capo_bedrock_agentcore_control.types.evaluation_dimension_name.EvaluationDimensionName"
    """<p> The name of the dimension. This name is unique within the evaluator and identifies the dimension's results. </p>"""
    dimension_instruction: "capo_bedrock_agentcore_control.types.evaluation_dimension_instruction.EvaluationDimensionInstruction"
    """<p> The instruction to the evaluator model for this dimension, describing what the model should judge when scoring the dimension. </p>"""
    dimension_rating_scale: "capo_bedrock_agentcore_control.types.dimension_rating_scale.DimensionRatingScale"
    """<p> The rating scale for this dimension, which can be numerical or categorical. A dimension's rating scale cannot itself be multi-dimensional. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDimension) -> dict:
    out: dict = {}
    out["dimensionName"] = value["dimension_name"]
    out["dimensionInstruction"] = value["dimension_instruction"]
    import capo_bedrock_agentcore_control.types.dimension_rating_scale

    out["dimensionRatingScale"] = (
        capo_bedrock_agentcore_control.types.dimension_rating_scale.serialize_json(
            value["dimension_rating_scale"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationDimension:
    out: EvaluationDimension = {}  # type: ignore[typeddict-item]
    if data.get("dimensionName") is not None:
        out["dimension_name"] = data["dimensionName"]
    else:
        out["dimension_name"] = ""
    if data.get("dimensionInstruction") is not None:
        out["dimension_instruction"] = data["dimensionInstruction"]
    else:
        out["dimension_instruction"] = ""
    if data.get("dimensionRatingScale") is not None:
        import capo_bedrock_agentcore_control.types.dimension_rating_scale

        out["dimension_rating_scale"] = (
            capo_bedrock_agentcore_control.types.dimension_rating_scale.deserialize_json(
                data["dimensionRatingScale"]
            )
        )
    else:
        out["dimension_rating_scale"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: EvaluationDimension) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dimension_instruction" in value:
        out["dimension_instruction"] = "*** Sensitive Data Redacted ***"
    if "dimension_rating_scale" in value:
        out["dimension_rating_scale"] = "*** Sensitive Data Redacted ***"
    return out
