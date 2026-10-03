"""Generated from Smithy shape ``com.amazonaws.connectparticipant#StartAttachmentUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectparticipant.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectparticipant.types.attachment_name
    import capo_connectparticipant.types.attachment_size_in_bytes
    import capo_connectparticipant.types.content_type
    import capo_connectparticipant.types.non_empty_client_token
    import capo_connectparticipant.types.participant_token


class StartAttachmentUploadRequest(TypedDict, closed=True):
    content_type: "capo_connectparticipant.types.content_type.ContentType"
    """<p>Describes the MIME file type of the attachment. For a list of supported file types, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html">Feature specifications</a> in the <i>Amazon Connect Administrator Guide</i>.</p>"""
    attachment_size_in_bytes: (
        "capo_connectparticipant.types.attachment_size_in_bytes.AttachmentSizeInBytes"
    )
    """<p>The size of the attachment in bytes.</p>"""
    attachment_name: "capo_connectparticipant.types.attachment_name.AttachmentName"
    """<p>A case-sensitive name of the attachment being uploaded.</p>"""
    client_token: (
        "capo_connectparticipant.types.non_empty_client_token.NonEmptyClientToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken"
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAttachmentUploadRequest) -> dict:
    out: dict = {}
    out["ContentType"] = value["content_type"]
    out["AttachmentSizeInBytes"] = value.get("attachment_size_in_bytes", 0)
    out["AttachmentName"] = value["attachment_name"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartAttachmentUploadRequest:
    out: StartAttachmentUploadRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("StartAttachmentUploadRequest.content_type required")
    if data.get("AttachmentSizeInBytes") is not None:
        out["attachment_size_in_bytes"] = data["AttachmentSizeInBytes"]
    else:
        out["attachment_size_in_bytes"] = 0
    if data.get("AttachmentName") is not None:
        out["attachment_name"] = data["AttachmentName"]
    else:
        raise DeserializationError(
            "StartAttachmentUploadRequest.attachment_name required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("StartAttachmentUploadRequest.client_token required")
    return out
