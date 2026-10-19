"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InputContentBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.body
    import capo_bedrock_agentcore.types.max_len_string


class InputContentBlock(TypedDict, closed=True):
    path: "capo_bedrock_agentcore.types.max_len_string.MaxLenString"
    """<p>The path to the input content.</p>"""
    text: NotRequired["capo_bedrock_agentcore.types.max_len_string.MaxLenString"]
    """<p>The text input content.</p>"""
    blob: NotRequired["capo_bedrock_agentcore.types.body.Body"]
    """<p>The binary input content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputContentBlock) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "text" in value:
        out["text"] = value["text"]
    if "blob" in value:
        import capo_bedrock_agentcore.types.body

        out["blob"] = capo_bedrock_agentcore.types.body.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> InputContentBlock:
    out: InputContentBlock = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("blob") is not None:
        import capo_bedrock_agentcore.types.body

        out["blob"] = capo_bedrock_agentcore.types.body.deserialize_json(data["blob"])
    return out


def redact_sensitive(value: InputContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blob" in value:
        out["blob"] = "*** Sensitive Data Redacted ***"
    return out
