"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#MessageContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.message_text


class MessageContent(TypedDict, closed=True):
    text: "capo_opensearchmemory.types.message_text.MessageText"
    """<p>The text of the turn.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageContent) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageContent:
    out: MessageContent = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out


def redact_sensitive(value: MessageContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
