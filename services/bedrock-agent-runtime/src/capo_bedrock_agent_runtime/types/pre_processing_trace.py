"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PreProcessingTrace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.model_invocation_input
    import capo_bedrock_agent_runtime.types.pre_processing_model_invocation_output


class PreProcessingTraceModelInvocationInputMember(TypedDict, closed=True):
    modelInvocationInput: (
        "capo_bedrock_agent_runtime.types.model_invocation_input.ModelInvocationInput"
    )


class PreProcessingTraceModelInvocationOutputMember(TypedDict, closed=True):
    modelInvocationOutput: "capo_bedrock_agent_runtime.types.pre_processing_model_invocation_output.PreProcessingModelInvocationOutput"


PreProcessingTrace: TypeAlias = (
    PreProcessingTraceModelInvocationInputMember
    | PreProcessingTraceModelInvocationOutputMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PreProcessingTrace) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PreProcessingTrace: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "modelInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": capo_bedrock_agent_runtime.types.model_invocation_input.serialize_json(
                value["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in value:
        import capo_bedrock_agent_runtime.types.pre_processing_model_invocation_output

        return {
            "modelInvocationOutput": capo_bedrock_agent_runtime.types.pre_processing_model_invocation_output.serialize_json(
                value["modelInvocationOutput"]
            )
        }
    else:
        raise SerializationError("PreProcessingTrace: no variant present")


def deserialize_json(data: dict) -> PreProcessingTrace:
    if data.get("modelInvocationInput") is not None:
        import capo_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": capo_bedrock_agent_runtime.types.model_invocation_input.deserialize_json(
                data["modelInvocationInput"]
            )
        }
    elif data.get("modelInvocationOutput") is not None:
        import capo_bedrock_agent_runtime.types.pre_processing_model_invocation_output

        return {
            "modelInvocationOutput": capo_bedrock_agent_runtime.types.pre_processing_model_invocation_output.deserialize_json(
                data["modelInvocationOutput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PreProcessingTrace: no recognized variant key")
