"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationModelConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_bedrock_model
    import capo_bedrock.types.evaluation_precomputed_inference_source


class _EvaluationModelConfig_bedrockModel(TypedDict, closed=True):
    bedrockModel: "capo_bedrock.types.evaluation_bedrock_model.EvaluationBedrockModel"


class _EvaluationModelConfig_precomputedInferenceSource(TypedDict, closed=True):
    precomputedInferenceSource: "capo_bedrock.types.evaluation_precomputed_inference_source.EvaluationPrecomputedInferenceSource"


EvaluationModelConfig: TypeAlias = (
    _EvaluationModelConfig_bedrockModel
    | _EvaluationModelConfig_precomputedInferenceSource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationModelConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationModelConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "bedrockModel" in value:
        import capo_bedrock.types.evaluation_bedrock_model

        return {
            "bedrockModel": capo_bedrock.types.evaluation_bedrock_model.serialize_json(
                value["bedrockModel"]
            )
        }
    elif "precomputedInferenceSource" in value:
        import capo_bedrock.types.evaluation_precomputed_inference_source

        return {
            "precomputedInferenceSource": capo_bedrock.types.evaluation_precomputed_inference_source.serialize_json(
                value["precomputedInferenceSource"]
            )
        }
    else:
        raise SerializationError("EvaluationModelConfig: no variant present")


def deserialize_json(data: dict) -> EvaluationModelConfig:
    if data.get("bedrockModel") is not None:
        import capo_bedrock.types.evaluation_bedrock_model

        return {
            "bedrockModel": capo_bedrock.types.evaluation_bedrock_model.deserialize_json(
                data["bedrockModel"]
            )
        }
    elif data.get("precomputedInferenceSource") is not None:
        import capo_bedrock.types.evaluation_precomputed_inference_source

        return {
            "precomputedInferenceSource": capo_bedrock.types.evaluation_precomputed_inference_source.deserialize_json(
                data["precomputedInferenceSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EvaluationModelConfig: no recognized variant key")


def redact_sensitive(
    value: EvaluationModelConfig,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "bedrockModel" in value:
        import capo_bedrock.types.evaluation_bedrock_model

        out["bedrockModel"] = (
            capo_bedrock.types.evaluation_bedrock_model.redact_sensitive(
                value["bedrockModel"]
            )
        )
    return out
