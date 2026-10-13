"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationResultMember``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.api_result
    import capo_bedrock_agent_runtime.types.function_result


class _InvocationResultMember_apiResult(TypedDict, closed=True):
    apiResult: "capo_bedrock_agent_runtime.types.api_result.ApiResult"


class _InvocationResultMember_functionResult(TypedDict, closed=True):
    functionResult: "capo_bedrock_agent_runtime.types.function_result.FunctionResult"


InvocationResultMember: TypeAlias = (
    _InvocationResultMember_apiResult | _InvocationResultMember_functionResult
)


# --- restJson1 ser/de ---
def serialize_json(value: InvocationResultMember) -> dict:
    if "apiResult" in value:
        import capo_bedrock_agent_runtime.types.api_result

        return {
            "apiResult": capo_bedrock_agent_runtime.types.api_result.serialize_json(
                value["apiResult"]
            )
        }
    elif "functionResult" in value:
        import capo_bedrock_agent_runtime.types.function_result

        return {
            "functionResult": capo_bedrock_agent_runtime.types.function_result.serialize_json(
                value["functionResult"]
            )
        }
    else:
        raise SerializationError("InvocationResultMember: no variant present")


def deserialize_json(data: dict) -> InvocationResultMember:
    if data.get("apiResult") is not None:
        import capo_bedrock_agent_runtime.types.api_result

        return {
            "apiResult": capo_bedrock_agent_runtime.types.api_result.deserialize_json(
                data["apiResult"]
            )
        }
    elif data.get("functionResult") is not None:
        import capo_bedrock_agent_runtime.types.function_result

        return {
            "functionResult": capo_bedrock_agent_runtime.types.function_result.deserialize_json(
                data["functionResult"]
            )
        }
    else:
        raise DeserializationError("InvocationResultMember: no recognized variant key")


def redact_sensitive(value: InvocationResultMember) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "apiResult" in value:
        import capo_bedrock_agent_runtime.types.api_result

        out["apiResult"] = capo_bedrock_agent_runtime.types.api_result.redact_sensitive(
            value["apiResult"]
        )
    return out
