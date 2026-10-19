"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.mime_type


class RetrievalContent(TypedDict, closed=True):
    byte_content: NotRequired["bytes"]
    """<p>The binary content of the retrieved item.</p>"""
    text: NotRequired["str"]
    """<p>The text content of the retrieved item.</p>"""
    mime_type: "capo_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p>The MIME type of the retrieved content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalContent) -> dict:
    out: dict = {}
    if "byte_content" in value:
        import capo_bedrock_agent_runtime.types._prelude.blob

        out["byteContent"] = (
            capo_bedrock_agent_runtime.types._prelude.blob.serialize_json(
                value["byte_content"]
            )
        )
    if "text" in value:
        out["text"] = value["text"]
    out["mimeType"] = value["mime_type"]
    return out


def deserialize_json(data: dict) -> RetrievalContent:
    out: RetrievalContent = {}  # type: ignore[typeddict-item]
    if data.get("byteContent") is not None:
        import capo_bedrock_agent_runtime.types._prelude.blob

        out["byte_content"] = (
            capo_bedrock_agent_runtime.types._prelude.blob.deserialize_json(
                data["byteContent"]
            )
        )
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("mimeType") is not None:
        out["mime_type"] = data["mimeType"]
    else:
        out["mime_type"] = ""
    return out
