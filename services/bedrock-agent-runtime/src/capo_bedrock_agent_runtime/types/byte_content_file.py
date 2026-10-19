"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ByteContentFile``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.byte_content_blob
    import capo_bedrock_agent_runtime.types.mime_type


class ByteContentFile(TypedDict, closed=True):
    media_type: "capo_bedrock_agent_runtime.types.mime_type.MimeType"
    """<p>The MIME type of data contained in the file used for chat.</p>"""
    data: "capo_bedrock_agent_runtime.types.byte_content_blob.ByteContentBlob"
    """<p>The raw bytes of the file to attach. The maximum size of all files that is attached is 10MB. You can attach a maximum of 5 files. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ByteContentFile) -> dict:
    out: dict = {}
    out["mediaType"] = value["media_type"]
    import capo_bedrock_agent_runtime.types.byte_content_blob

    out["data"] = capo_bedrock_agent_runtime.types.byte_content_blob.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> ByteContentFile:
    out: ByteContentFile = {}  # type: ignore[typeddict-item]
    if data.get("mediaType") is not None:
        out["media_type"] = data["mediaType"]
    else:
        out["media_type"] = ""
    if data.get("data") is not None:
        import capo_bedrock_agent_runtime.types.byte_content_blob

        out["data"] = (
            capo_bedrock_agent_runtime.types.byte_content_blob.deserialize_json(
                data["data"]
            )
        )
    else:
        out["data"] = b""
    return out


def redact_sensitive(value: ByteContentFile) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        out["data"] = "*** Sensitive Data Redacted ***"
    return out
