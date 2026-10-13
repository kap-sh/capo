"""Generated from Smithy shape ``com.amazonaws.bedrock#ByteContentDoc``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.byte_content_blob
    import capo_bedrock.types.content_type
    import capo_bedrock.types.identifier


class ByteContentDoc(TypedDict, closed=True):
    identifier: "capo_bedrock.types.identifier.Identifier"
    """<p>The file name of the document contained in the wrapper object.</p>"""
    content_type: "capo_bedrock.types.content_type.ContentType"
    """<p>The MIME type of the document contained in the wrapper object.</p>"""
    data: "capo_bedrock.types.byte_content_blob.ByteContentBlob"
    """<p>The byte value of the file to upload, encoded as a Base-64 string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ByteContentDoc) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["contentType"] = value["content_type"]
    import capo_bedrock.types.byte_content_blob

    out["data"] = capo_bedrock.types.byte_content_blob.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> ByteContentDoc:
    out: ByteContentDoc = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("ByteContentDoc.identifier required")
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("ByteContentDoc.content_type required")
    if data.get("data") is not None:
        import capo_bedrock.types.byte_content_blob

        out["data"] = capo_bedrock.types.byte_content_blob.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("ByteContentDoc.data required")
    return out


def redact_sensitive(value: ByteContentDoc) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identifier" in value:
        out["identifier"] = "*** Sensitive Data Redacted ***"
    if "data" in value:
        out["data"] = "*** Sensitive Data Redacted ***"
    return out
