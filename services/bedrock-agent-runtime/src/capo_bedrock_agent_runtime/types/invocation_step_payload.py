"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStepPayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_session_content_blocks


class InvocationStepPayloadContentBlocksMember(TypedDict, closed=True):
    contentBlocks: "capo_bedrock_agent_runtime.types.bedrock_session_content_blocks.BedrockSessionContentBlocks"


InvocationStepPayload: TypeAlias = (
    InvocationStepPayloadContentBlocksMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStepPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"InvocationStepPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "contentBlocks" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
