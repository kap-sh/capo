"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationInputMember``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.api_invocation_input
    import capo_bedrock_agent_runtime.types.function_invocation_input


class _InvocationInputMember_apiInvocationInput(TypedDict, closed=True):
    apiInvocationInput: (
        "capo_bedrock_agent_runtime.types.api_invocation_input.ApiInvocationInput"
    )


class _InvocationInputMember_functionInvocationInput(TypedDict, closed=True):
    functionInvocationInput: "capo_bedrock_agent_runtime.types.function_invocation_input.FunctionInvocationInput"


InvocationInputMember: TypeAlias = (
    _InvocationInputMember_apiInvocationInput
    | _InvocationInputMember_functionInvocationInput
)


# --- restJson1 ser/de ---
def serialize_json(value: InvocationInputMember) -> dict:
    if "apiInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.api_invocation_input

        return {
            "apiInvocationInput": capo_bedrock_agent_runtime.types.api_invocation_input.serialize_json(
                value["apiInvocationInput"]
            )
        }
    elif "functionInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.function_invocation_input

        return {
            "functionInvocationInput": capo_bedrock_agent_runtime.types.function_invocation_input.serialize_json(
                value["functionInvocationInput"]
            )
        }
    else:
        raise SerializationError("InvocationInputMember: no variant present")


def deserialize_json(data: dict) -> InvocationInputMember:
    if data.get("apiInvocationInput") is not None:
        import capo_bedrock_agent_runtime.types.api_invocation_input

        return {
            "apiInvocationInput": capo_bedrock_agent_runtime.types.api_invocation_input.deserialize_json(
                data["apiInvocationInput"]
            )
        }
    elif data.get("functionInvocationInput") is not None:
        import capo_bedrock_agent_runtime.types.function_invocation_input

        return {
            "functionInvocationInput": capo_bedrock_agent_runtime.types.function_invocation_input.deserialize_json(
                data["functionInvocationInput"]
            )
        }
    else:
        raise DeserializationError("InvocationInputMember: no recognized variant key")


def redact_sensitive(value: InvocationInputMember) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "apiInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.api_invocation_input

        out["apiInvocationInput"] = (
            capo_bedrock_agent_runtime.types.api_invocation_input.redact_sensitive(
                value["apiInvocationInput"]
            )
        )
    if "functionInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.function_invocation_input

        out["functionInvocationInput"] = (
            capo_bedrock_agent_runtime.types.function_invocation_input.redact_sensitive(
                value["functionInvocationInput"]
            )
        )
    return out
