"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluatorModelConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.bedrock_evaluator_models


class EvaluatorModelConfigBedrockEvaluatorModelsMember(TypedDict, closed=True):
    bedrockEvaluatorModels: (
        "capo_bedrock.types.bedrock_evaluator_models.BedrockEvaluatorModels"
    )


EvaluatorModelConfig: TypeAlias = (
    EvaluatorModelConfigBedrockEvaluatorModelsMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorModelConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluatorModelConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "bedrockEvaluatorModels" in value:
        import capo_bedrock.types.bedrock_evaluator_models

        return {
            "bedrockEvaluatorModels": capo_bedrock.types.bedrock_evaluator_models.serialize_json(
                value["bedrockEvaluatorModels"]
            )
        }
    else:
        raise SerializationError("EvaluatorModelConfig: no variant present")


def deserialize_json(data: dict) -> EvaluatorModelConfig:
    if data.get("bedrockEvaluatorModels") is not None:
        import capo_bedrock.types.bedrock_evaluator_models

        return {
            "bedrockEvaluatorModels": capo_bedrock.types.bedrock_evaluator_models.deserialize_json(
                data["bedrockEvaluatorModels"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EvaluatorModelConfig: no recognized variant key")
