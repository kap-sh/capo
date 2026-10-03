"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectparticipant.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectparticipant.types.attachment_size_in_bytes
    import capo_connectparticipant.types.iso8601_datetime
    import capo_connectparticipant.types.pre_signed_attachment_url


class GetAttachmentResponse(TypedDict, closed=True):
    url: NotRequired[
        "capo_connectparticipant.types.pre_signed_attachment_url.PreSignedAttachmentUrl"
    ]
    """<p>This is the pre-signed URL that can be used for uploading the file to Amazon S3 when used in response to <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_StartAttachmentUpload.html">StartAttachmentUpload</a>.</p>"""
    url_expiry: NotRequired[
        "capo_connectparticipant.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""
    attachment_size_in_bytes: (
        "capo_connectparticipant.types.attachment_size_in_bytes.AttachmentSizeInBytes"
    )
    """<p>The size of the attachment in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttachmentResponse) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "url_expiry" in value:
        out["UrlExpiry"] = value["url_expiry"]
    out["AttachmentSizeInBytes"] = value["attachment_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> GetAttachmentResponse:
    out: GetAttachmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("UrlExpiry") is not None:
        out["url_expiry"] = data["UrlExpiry"]
    if data.get("AttachmentSizeInBytes") is not None:
        out["attachment_size_in_bytes"] = data["AttachmentSizeInBytes"]
    else:
        raise DeserializationError(
            "GetAttachmentResponse.attachment_size_in_bytes required"
        )
    return out
