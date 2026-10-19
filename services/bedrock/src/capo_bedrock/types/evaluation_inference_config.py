"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationInferenceConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_model_configs
    import capo_bedrock.types.rag_configs


class _EvaluationInferenceConfig_models(TypedDict, closed=True):
    models: "capo_bedrock.types.evaluation_model_configs.EvaluationModelConfigs"


class _EvaluationInferenceConfig_ragConfigs(TypedDict, closed=True):
    ragConfigs: "capo_bedrock.types.rag_configs.RagConfigs"


EvaluationInferenceConfig: TypeAlias = (
    _EvaluationInferenceConfig_models
    | _EvaluationInferenceConfig_ragConfigs
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationInferenceConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationInferenceConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "models" in value:
        import capo_bedrock.types.evaluation_model_configs

        return {
            "models": capo_bedrock.types.evaluation_model_configs.serialize_json(
                value["models"]
            )
        }
    elif "ragConfigs" in value:
        import capo_bedrock.types.rag_configs

        return {
            "ragConfigs": capo_bedrock.types.rag_configs.serialize_json(
                value["ragConfigs"]
            )
        }
    else:
        raise SerializationError("EvaluationInferenceConfig: no variant present")


def deserialize_json(data: dict) -> EvaluationInferenceConfig:
    if data.get("models") is not None:
        import capo_bedrock.types.evaluation_model_configs

        return {
            "models": capo_bedrock.types.evaluation_model_configs.deserialize_json(
                data["models"]
            )
        }
    elif data.get("ragConfigs") is not None:
        import capo_bedrock.types.rag_configs

        return {
            "ragConfigs": capo_bedrock.types.rag_configs.deserialize_json(
                data["ragConfigs"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "EvaluationInferenceConfig: no recognized variant key"
        )


def redact_sensitive(
    value: EvaluationInferenceConfig,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "models" in value:
        import capo_bedrock.types.evaluation_model_configs

        out["models"] = capo_bedrock.types.evaluation_model_configs.redact_sensitive(
            value["models"]
        )
    if "ragConfigs" in value:
        import capo_bedrock.types.rag_configs

        out["ragConfigs"] = capo_bedrock.types.rag_configs.redact_sensitive(
            value["ragConfigs"]
        )
    return out
