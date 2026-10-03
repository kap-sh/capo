"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.artifact_id
    import capo_connect.types.artifact_status
    import capo_connect.types.attachment_name
    import capo_connect.types.content_type


class RealTimeContactAnalysisAttachment(TypedDict, closed=True):
    attachment_name: "capo_connect.types.attachment_name.AttachmentName"
    """<p>A case-sensitive name of the attachment being uploaded. Can be redacted.</p>"""
    content_type: NotRequired["capo_connect.types.content_type.ContentType"]
    """<p>Describes the MIME file type of the attachment. For a list of supported file types, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html">Feature specifications</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    attachment_id: "capo_connect.types.artifact_id.ArtifactId"
    """<p>A unique identifier for the attachment.</p>"""
    status: NotRequired["capo_connect.types.artifact_status.ArtifactStatus"]
    """<p>Status of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisAttachment) -> dict:
    out: dict = {}
    out["AttachmentName"] = value["attachment_name"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    out["AttachmentId"] = value["attachment_id"]
    if "status" in value:
        import capo_connect.types.artifact_status

        out["Status"] = capo_connect.types.artifact_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisAttachment:
    out: RealTimeContactAnalysisAttachment = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentName") is not None:
        out["attachment_name"] = data["AttachmentName"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisAttachment.attachment_name required"
        )
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisAttachment.attachment_id required"
        )
    if data.get("Status") is not None:
        import capo_connect.types.artifact_status

        out["status"] = capo_connect.types.artifact_status.deserialize_json(
            data["Status"]
        )
    return out
