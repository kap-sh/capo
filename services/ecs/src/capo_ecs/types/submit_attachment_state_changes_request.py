"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitAttachmentStateChangesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.attachment_state_changes
    import capo_ecs.types.string


class SubmitAttachmentStateChangesRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full ARN of the cluster that hosts the container instance the attachment belongs to.</p>"""
    attachments: "capo_ecs.types.attachment_state_changes.AttachmentStateChanges"
    """<p>Any attachments associated with the state change request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitAttachmentStateChangesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import capo_ecs.types.attachment_state_changes

    out["attachments"] = capo_ecs.types.attachment_state_changes.serialize_aws_json_1_1(
        value["attachments"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitAttachmentStateChangesRequest:
    out: SubmitAttachmentStateChangesRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("attachments") is not None:
        import capo_ecs.types.attachment_state_changes

        out["attachments"] = (
            capo_ecs.types.attachment_state_changes.deserialize_aws_json_1_1(
                data["attachments"]
            )
        )
    else:
        out["attachments"] = []
    return out
