"""Generated from Smithy shape ``com.amazonaws.bedrockagent#TextContentDoc``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.data


class TextContentDoc(TypedDict, closed=True):
    data: "capo_bedrock_agent.types.data.Data"
    """<p>The text of the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextContentDoc) -> dict:
    out: dict = {}
    out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> TextContentDoc:
    out: TextContentDoc = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        out["data"] = data["data"]
    else:
        raise DeserializationError("TextContentDoc.data required")
    return out


def redact_sensitive(value: TextContentDoc) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        out["data"] = "*** Sensitive Data Redacted ***"
    return out
