"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Message``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.content_blocks
    import capo_bedrock_agent_runtime.types.conversation_role


class Message(TypedDict, closed=True):
    role: "capo_bedrock_agent_runtime.types.conversation_role.ConversationRole"
    """<p>The message's role.</p>"""
    content: "capo_bedrock_agent_runtime.types.content_blocks.ContentBlocks"
    """<p>The message's content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.conversation_role

    out["role"] = capo_bedrock_agent_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    import capo_bedrock_agent_runtime.types.content_blocks

    out["content"] = capo_bedrock_agent_runtime.types.content_blocks.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_bedrock_agent_runtime.types.conversation_role

        out["role"] = (
            capo_bedrock_agent_runtime.types.conversation_role.deserialize_json(
                data["role"]
            )
        )
    else:
        import typing

        out["role"] = typing.cast(
            "capo_bedrock_agent_runtime.types.conversation_role.ConversationRole", ""
        )
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.content_blocks

        out["content"] = (
            capo_bedrock_agent_runtime.types.content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = []
    return out


def redact_sensitive(value: Message) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agent_runtime.types.content_blocks

        out["content"] = (
            capo_bedrock_agent_runtime.types.content_blocks.redact_sensitive(
                value["content"]
            )
        )
    return out
