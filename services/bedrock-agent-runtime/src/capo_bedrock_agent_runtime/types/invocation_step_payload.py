"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStepPayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_session_content_blocks


class _InvocationStepPayload_contentBlocks(TypedDict, closed=True):
    contentBlocks: "capo_bedrock_agent_runtime.types.bedrock_session_content_blocks.BedrockSessionContentBlocks"


InvocationStepPayload: TypeAlias = _InvocationStepPayload_contentBlocks


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStepPayload) -> dict:
    if "contentBlocks" in value:
        import capo_bedrock_agent_runtime.types.bedrock_session_content_blocks

        return {
            "contentBlocks": capo_bedrock_agent_runtime.types.bedrock_session_content_blocks.serialize_json(
                value["contentBlocks"]
            )
        }
    else:
        raise SerializationError("InvocationStepPayload: no variant present")


def deserialize_json(data: dict) -> InvocationStepPayload:
    if data.get("contentBlocks") is not None:
        import capo_bedrock_agent_runtime.types.bedrock_session_content_blocks

        return {
            "contentBlocks": capo_bedrock_agent_runtime.types.bedrock_session_content_blocks.deserialize_json(
                data["contentBlocks"]
            )
        }
    else:
        raise DeserializationError("InvocationStepPayload: no recognized variant key")


def redact_sensitive(value: InvocationStepPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contentBlocks" in value:
        import capo_bedrock_agent_runtime.types.bedrock_session_content_blocks

        out["contentBlocks"] = (
            capo_bedrock_agent_runtime.types.bedrock_session_content_blocks.redact_sensitive(
                value["contentBlocks"]
            )
        )
    return out
