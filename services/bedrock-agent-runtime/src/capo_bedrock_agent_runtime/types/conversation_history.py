"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConversationHistory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.messages


class ConversationHistory(TypedDict, closed=True):
    messages: NotRequired["capo_bedrock_agent_runtime.types.messages.Messages"]
    """<p>The conversation's messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationHistory) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_bedrock_agent_runtime.types.messages

        out["messages"] = capo_bedrock_agent_runtime.types.messages.serialize_json(
            value["messages"]
        )
    return out


def deserialize_json(data: dict) -> ConversationHistory:
    out: ConversationHistory = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_agent_runtime.types.messages

        out["messages"] = capo_bedrock_agent_runtime.types.messages.deserialize_json(
            data["messages"]
        )
    return out


def redact_sensitive(value: ConversationHistory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_bedrock_agent_runtime.types.messages

        out["messages"] = capo_bedrock_agent_runtime.types.messages.redact_sensitive(
            value["messages"]
        )
    return out
