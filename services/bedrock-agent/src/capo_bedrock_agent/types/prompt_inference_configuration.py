"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptInferenceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_model_inference_configuration


class PromptInferenceConfigurationTextMember(TypedDict, closed=True):
    text: "capo_bedrock_agent.types.prompt_model_inference_configuration.PromptModelInferenceConfiguration"


PromptInferenceConfiguration: TypeAlias = (
    PromptInferenceConfigurationTextMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PromptInferenceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PromptInferenceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        import capo_bedrock_agent.types.prompt_model_inference_configuration

        return {
            "text": capo_bedrock_agent.types.prompt_model_inference_configuration.serialize_json(
                value["text"]
            )
        }
    else:
        raise SerializationError("PromptInferenceConfiguration: no variant present")


def deserialize_json(data: dict) -> PromptInferenceConfiguration:
    if data.get("text") is not None:
        import capo_bedrock_agent.types.prompt_model_inference_configuration

        return {
            "text": capo_bedrock_agent.types.prompt_model_inference_configuration.deserialize_json(
                data["text"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PromptInferenceConfiguration: no recognized variant key"
        )
