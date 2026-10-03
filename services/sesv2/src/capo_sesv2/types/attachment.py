"""Generated from Smithy shape ``com.amazonaws.sesv2#Attachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.attachment_content_description
    import capo_sesv2.types.attachment_content_disposition
    import capo_sesv2.types.attachment_content_id
    import capo_sesv2.types.attachment_content_transfer_encoding
    import capo_sesv2.types.attachment_content_type
    import capo_sesv2.types.attachment_file_name
    import capo_sesv2.types.raw_attachment_data


class Attachment(TypedDict, closed=True):
    raw_content: "capo_sesv2.types.raw_attachment_data.RawAttachmentData"
    """<p> The raw data of the attachment. It needs to be base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.</p>"""
    content_disposition: NotRequired[
        "capo_sesv2.types.attachment_content_disposition.AttachmentContentDisposition"
    ]
    """<p> A standard descriptor indicating how the attachment should be rendered in the email. Supported values: <code>ATTACHMENT</code> or <code>INLINE</code>.</p>"""
    file_name: "capo_sesv2.types.attachment_file_name.AttachmentFileName"
    """<p>The file name for the attachment as it will appear in the email. Amazon SES restricts certain file extensions. To ensure attachments are accepted, check the <a href="https://docs.aws.amazon.com/ses/latest/dg/mime-types.html">Unsupported attachment types</a> in the Amazon SES Developer Guide.</p>"""
    content_description: NotRequired[
        "capo_sesv2.types.attachment_content_description.AttachmentContentDescription"
    ]
    """<p> A brief description of the attachment content.</p>"""
    content_id: NotRequired[
        "capo_sesv2.types.attachment_content_id.AttachmentContentId"
    ]
    """<p> Unique identifier for the attachment, used for referencing attachments with INLINE disposition in HTML content.</p>"""
    content_transfer_encoding: NotRequired[
        "capo_sesv2.types.attachment_content_transfer_encoding.AttachmentContentTransferEncoding"
    ]
    """<p> Specifies how the attachment is encoded. Supported values: <code>BASE64</code>, <code>QUOTED_PRINTABLE</code>, <code>SEVEN_BIT</code>.</p>"""
    content_type: NotRequired[
        "capo_sesv2.types.attachment_content_type.AttachmentContentType"
    ]
    """<p> The MIME type of the attachment.</p> <note> <p>Example: <code>application/pdf</code>, <code>image/jpeg</code> </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attachment) -> dict:
    out: dict = {}
    import capo_sesv2.types.raw_attachment_data

    out["RawContent"] = capo_sesv2.types.raw_attachment_data.serialize_json(
        value["raw_content"]
    )
    if "content_disposition" in value:
        import capo_sesv2.types.attachment_content_disposition

        out["ContentDisposition"] = (
            capo_sesv2.types.attachment_content_disposition.serialize_json(
                value["content_disposition"]
            )
        )
    out["FileName"] = value["file_name"]
    if "content_description" in value:
        out["ContentDescription"] = value["content_description"]
    if "content_id" in value:
        out["ContentId"] = value["content_id"]
    if "content_transfer_encoding" in value:
        import capo_sesv2.types.attachment_content_transfer_encoding

        out["ContentTransferEncoding"] = (
            capo_sesv2.types.attachment_content_transfer_encoding.serialize_json(
                value["content_transfer_encoding"]
            )
        )
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if data.get("RawContent") is not None:
        import capo_sesv2.types.raw_attachment_data

        out["raw_content"] = capo_sesv2.types.raw_attachment_data.deserialize_json(
            data["RawContent"]
        )
    else:
        raise DeserializationError("Attachment.raw_content required")
    if data.get("ContentDisposition") is not None:
        import capo_sesv2.types.attachment_content_disposition

        out["content_disposition"] = (
            capo_sesv2.types.attachment_content_disposition.deserialize_json(
                data["ContentDisposition"]
            )
        )
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    else:
        raise DeserializationError("Attachment.file_name required")
    if data.get("ContentDescription") is not None:
        out["content_description"] = data["ContentDescription"]
    if data.get("ContentId") is not None:
        out["content_id"] = data["ContentId"]
    if data.get("ContentTransferEncoding") is not None:
        import capo_sesv2.types.attachment_content_transfer_encoding

        out["content_transfer_encoding"] = (
            capo_sesv2.types.attachment_content_transfer_encoding.deserialize_json(
                data["ContentTransferEncoding"]
            )
        )
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    return out
