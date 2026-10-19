"""Generated from Smithy shape ``com.amazonaws.connect#EmailAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.file_name
    import capo_connect.types.pre_signed_attachment_url


class EmailAttachment(TypedDict, closed=True):
    file_name: "capo_connect.types.file_name.FileName"
    """<p>A case-sensitive name of the attached file being uploaded.</p>"""
    s3_url: "capo_connect.types.pre_signed_attachment_url.PreSignedAttachmentUrl"
    """<p>The pre-signed URLs for the S3 bucket where the email attachment is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAttachment) -> dict:
    out: dict = {}
    out["FileName"] = value["file_name"]
    out["S3Url"] = value["s3_url"]
    return out


def deserialize_json(data: dict) -> EmailAttachment:
    out: EmailAttachment = {}  # type: ignore[typeddict-item]
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    else:
        out["file_name"] = ""
    if data.get("S3Url") is not None:
        out["s3_url"] = data["S3Url"]
    else:
        out["s3_url"] = ""
    return out
