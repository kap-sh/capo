"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LlmAsAJudgeEvaluatorConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_instructions
    import capo_bedrock_agentcore_control.types.evaluator_model_config
    import capo_bedrock_agentcore_control.types.rating_scale


class LlmAsAJudgeEvaluatorConfig(TypedDict, closed=True):
    instructions: "capo_bedrock_agentcore_control.types.evaluator_instructions.EvaluatorInstructions"
    """<p> The evaluation instructions that guide the language model in assessing agent performance, including criteria and evaluation guidelines. </p>"""
    rating_scale: "capo_bedrock_agentcore_control.types.rating_scale.RatingScale"
    """<p> The rating scale that defines how the evaluator should score agent performance, either numerical or categorical. </p>"""
    model_config: "capo_bedrock_agentcore_control.types.evaluator_model_config.EvaluatorModelConfig"
    """<p> The model configuration that specifies which foundation model to use and how to configure it for evaluation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LlmAsAJudgeEvaluatorConfig) -> dict:
    out: dict = {}
    out["instructions"] = value["instructions"]
    import capo_bedrock_agentcore_control.types.rating_scale

    out["ratingScale"] = (
        capo_bedrock_agentcore_control.types.rating_scale.serialize_json(
            value["rating_scale"]
        )
    )
    import capo_bedrock_agentcore_control.types.evaluator_model_config

    out["modelConfig"] = (
        capo_bedrock_agentcore_control.types.evaluator_model_config.serialize_json(
            value["model_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> LlmAsAJudgeEvaluatorConfig:
    out: LlmAsAJudgeEvaluatorConfig = {}  # type: ignore[typeddict-item]
    if data.get("instructions") is not None:
        out["instructions"] = data["instructions"]
    else:
        raise DeserializationError("LlmAsAJudgeEvaluatorConfig.instructions required")
    if data.get("ratingScale") is not None:
        import capo_bedrock_agentcore_control.types.rating_scale

        out["rating_scale"] = (
            capo_bedrock_agentcore_control.types.rating_scale.deserialize_json(
                data["ratingScale"]
            )
        )
    else:
        raise DeserializationError("LlmAsAJudgeEvaluatorConfig.rating_scale required")
    if data.get("modelConfig") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_model_config

        out["model_config"] = (
            capo_bedrock_agentcore_control.types.evaluator_model_config.deserialize_json(
                data["modelConfig"]
            )
        )
    else:
        raise DeserializationError("LlmAsAJudgeEvaluatorConfig.model_config required")
    return out


def redact_sensitive(value: LlmAsAJudgeEvaluatorConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instructions" in value:
        out["instructions"] = "*** Sensitive Data Redacted ***"
    if "rating_scale" in value:
        out["rating_scale"] = "*** Sensitive Data Redacted ***"
    return out
