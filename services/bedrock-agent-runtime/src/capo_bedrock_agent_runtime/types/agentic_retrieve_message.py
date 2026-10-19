"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content
    import capo_bedrock_agent_runtime.types.conversation_role


class AgenticRetrieveMessage(TypedDict, closed=True):
    content: "capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.AgenticRetrieveMessageContent"
    """<p>The content of the message.</p>"""
    role: "capo_bedrock_agent_runtime.types.conversation_role.ConversationRole"
    """<p>The role of the message sender (e.g., user or assistant).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMessage) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content

    out["content"] = (
        capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.serialize_json(
            value["content"]
        )
    )
    import capo_bedrock_agent_runtime.types.conversation_role

    out["role"] = capo_bedrock_agent_runtime.types.conversation_role.serialize_json(
        value["role"]
    )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMessage:
    out: AgenticRetrieveMessage = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_message_content

        out["content"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_message_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("AgenticRetrieveMessage.content required")
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
    return out


def redact_sensitive(value: AgenticRetrieveMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
