"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ByteContentDoc``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.byte_content_blob


class ByteContentDoc(TypedDict, closed=True):
    mime_type: "str"
    """<p>The MIME type of the content. For a list of MIME types, see <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">Media Types</a>. The following MIME types are supported:</p> <ul> <li> <p>text/plain</p> </li> <li> <p>text/html</p> </li> <li> <p>text/csv</p> </li> <li> <p>text/vtt</p> </li> <li> <p>message/rfc822</p> </li> <li> <p>application/xhtml+xml</p> </li> <li> <p>application/pdf</p> </li> <li> <p>application/msword</p> </li> <li> <p>application/vnd.ms-word.document.macroenabled.12</p> </li> <li> <p>application/vnd.ms-word.template.macroenabled.12</p> </li> <li> <p>application/vnd.ms-excel</p> </li> <li> <p>application/vnd.ms-excel.addin.macroenabled.12</p> </li> <li> <p>application/vnd.ms-excel.sheet.macroenabled.12</p> </li> <li> <p>application/vnd.ms-excel.template.macroenabled.12</p> </li> <li> <p>application/vnd.ms-excel.sheet.binary.macroenabled.12</p> </li> <li> <p>application/vnd.ms-spreadsheetml</p> </li> <li> <p>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</p> </li> <li> <p>application/vnd.openxmlformats-officedocument.spreadsheetml.template</p> </li> <li> <p>application/vnd.openxmlformats-officedocument.wordprocessingml.document</p> </li> <li> <p>application/vnd.openxmlformats-officedocument.wordprocessingml.template</p> </li> </ul>"""
    data: "capo_bedrock_agent.types.byte_content_blob.ByteContentBlob"
    """<p>The base64-encoded string of the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ByteContentDoc) -> dict:
    out: dict = {}
    out["mimeType"] = value["mime_type"]
    import capo_bedrock_agent.types.byte_content_blob

    out["data"] = capo_bedrock_agent.types.byte_content_blob.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> ByteContentDoc:
    out: ByteContentDoc = {}  # type: ignore[typeddict-item]
    if data.get("mimeType") is not None:
        out["mime_type"] = data["mimeType"]
    else:
        raise DeserializationError("ByteContentDoc.mime_type required")
    if data.get("data") is not None:
        import capo_bedrock_agent.types.byte_content_blob

        out["data"] = capo_bedrock_agent.types.byte_content_blob.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("ByteContentDoc.data required")
    return out
