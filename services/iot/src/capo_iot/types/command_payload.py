"""Generated from Smithy shape ``com.amazonaws.iot#CommandPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_payload_blob
    import capo_iot.types.mime_type


class CommandPayload(TypedDict, closed=True):
    content: NotRequired["capo_iot.types.command_payload_blob.CommandPayloadBlob"]
    """<p>The static payload file for the command.</p>"""
    content_type: NotRequired["capo_iot.types.mime_type.MimeType"]
    """<p>The content type that specifies the format type of the payload file. This field must use a type/subtype format, such as <code>application/json</code>. For information about various content types, see <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types">Common MIME types</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandPayload) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_iot.types.command_payload_blob

        out["content"] = capo_iot.types.command_payload_blob.serialize_json(
            value["content"]
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> CommandPayload:
    out: CommandPayload = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_iot.types.command_payload_blob

        out["content"] = capo_iot.types.command_payload_blob.deserialize_json(
            data["content"]
        )
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    return out
