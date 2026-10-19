"""Generated from Smithy shape ``com.amazonaws.ecs#AttachmentStateChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class AttachmentStateChange(TypedDict, closed=True):
    attachment_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the attachment.</p>"""
    status: "capo_ecs.types.string.String"
    """<p>The status of the attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentStateChange) -> dict:
    out: dict = {}
    out["attachmentArn"] = value["attachment_arn"]
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentStateChange:
    out: AttachmentStateChange = {}  # type: ignore[typeddict-item]
    if data.get("attachmentArn") is not None:
        out["attachment_arn"] = data["attachmentArn"]
    else:
        out["attachment_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
