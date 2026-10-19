"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorModelConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config
    import capo_bedrock_agentcore_control.types.open_responses_evaluator_model_config


class _EvaluatorModelConfig_bedrockEvaluatorModelConfig(TypedDict, closed=True):
    bedrockEvaluatorModelConfig: "capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config.BedrockEvaluatorModelConfig"


class _EvaluatorModelConfig_responsesEvaluatorModelConfig(TypedDict, closed=True):
    responsesEvaluatorModelConfig: "capo_bedrock_agentcore_control.types.open_responses_evaluator_model_config.OpenResponsesEvaluatorModelConfig"


EvaluatorModelConfig: TypeAlias = (
    _EvaluatorModelConfig_bedrockEvaluatorModelConfig
    | _EvaluatorModelConfig_responsesEvaluatorModelConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorModelConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluatorModelConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "bedrockEvaluatorModelConfig" in value:
        import capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config

        return {
            "bedrockEvaluatorModelConfig": capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config.serialize_json(
                value["bedrockEvaluatorModelConfig"]
            )
        }
    elif "responsesEvaluatorModelConfig" in value:
        import capo_bedrock_agentcore_control.types.open_responses_evaluator_model_config

        return {
            "responsesEvaluatorModelConfig": capo_bedrock_agentcore_control.types.open_responses_evaluator_model_config.serialize_json(
                value["responsesEvaluatorModelConfig"]
            )
        }
    else:
        raise SerializationError("EvaluatorModelConfig: no variant present")


def deserialize_json(data: dict) -> EvaluatorModelConfig:
    if data.get("bedrockEvaluatorModelConfig") is not None:
        import capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config

        return {
            "bedrockEvaluatorModelConfig": capo_bedrock_agentcore_control.types.bedrock_evaluator_model_config.deserialize_json(
                data["bedrockEvaluatorModelConfig"]
            )
        }
    elif data.get("responsesEvaluatorModelConfig") is not None:
        import capo_bedrock_agentcore_control.types.open_responses_evaluator_model_config

        return {
            "responsesEvaluatorModelConfig": capo_bedrock_agentcore_control.types.open_responses_evaluator_model_config.deserialize_json(
                data["responsesEvaluatorModelConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EvaluatorModelConfig: no recognized variant key")
