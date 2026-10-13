"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvokeAssistantResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.conversation_id
    import capo_iotsitewise.types.response_stream


class InvokeAssistantResponse(TypedDict, closed=True):
    body: "capo_iotsitewise.types.response_stream.ResponseStream"
    conversation_id: "capo_iotsitewise.types.conversation_id.ConversationId"
    """<p>The ID of the conversation, in UUID format. This ID uniquely identifies the conversation within IoT SiteWise.</p>"""


def redact_sensitive(value: InvokeAssistantResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out
