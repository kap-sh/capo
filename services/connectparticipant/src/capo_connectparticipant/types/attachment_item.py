"""Generated from Smithy shape ``com.amazonaws.connectparticipant#AttachmentItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.artifact_id
    import capo_connectparticipant.types.artifact_status
    import capo_connectparticipant.types.attachment_name
    import capo_connectparticipant.types.content_type


class AttachmentItem(TypedDict, closed=True):
    content_type: NotRequired["capo_connectparticipant.types.content_type.ContentType"]
    """<p>Describes the MIME file type of the attachment. For a list of supported file types, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html">Feature specifications</a> in the <i>Amazon Connect Administrator Guide</i>.</p>"""
    attachment_id: NotRequired["capo_connectparticipant.types.artifact_id.ArtifactId"]
    """<p>A unique identifier for the attachment.</p>"""
    attachment_name: NotRequired[
        "capo_connectparticipant.types.attachment_name.AttachmentName"
    ]
    """<p>A case-sensitive name of the attachment being uploaded.</p>"""
    status: NotRequired["capo_connectparticipant.types.artifact_status.ArtifactStatus"]
    """<p>Status of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentItem) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "attachment_name" in value:
        out["AttachmentName"] = value["attachment_name"]
    if "status" in value:
        import capo_connectparticipant.types.artifact_status

        out["Status"] = capo_connectparticipant.types.artifact_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AttachmentItem:
    out: AttachmentItem = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("AttachmentName") is not None:
        out["attachment_name"] = data["AttachmentName"]
    if data.get("Status") is not None:
        import capo_connectparticipant.types.artifact_status

        out["status"] = capo_connectparticipant.types.artifact_status.deserialize_json(
            data["Status"]
        )
    return out
