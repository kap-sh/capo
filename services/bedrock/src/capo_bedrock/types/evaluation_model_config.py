"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationModelConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_bedrock_model
    import capo_bedrock.types.evaluation_precomputed_inference_source


class EvaluationModelConfigBedrockModelMember(TypedDict, closed=True):
    bedrockModel: "capo_bedrock.types.evaluation_bedrock_model.EvaluationBedrockModel"


class EvaluationModelConfigPrecomputedInferenceSourceMember(TypedDict, closed=True):
    precomputedInferenceSource: "capo_bedrock.types.evaluation_precomputed_inference_source.EvaluationPrecomputedInferenceSource"


EvaluationModelConfig: TypeAlias = (
    EvaluationModelConfigBedrockModelMember
    | EvaluationModelConfigPrecomputedInferenceSourceMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationModelConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluationModelConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("EvaluationModelConfig: no recognized variant key")


def redact_sensitive(value: EvaluationModelConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bedrockModel" in value:
        import capo_bedrock.types.evaluation_bedrock_model

        out["bedrockModel"] = (
            capo_bedrock.types.evaluation_bedrock_model.redact_sensitive(
                value["bedrockModel"]
            )
        )
    return out
