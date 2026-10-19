"""Generated from Smithy shape ``com.amazonaws.support#GetAttachmentDownloadLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.attachment_id
    import capo_support.types.nullable_boolean_type


class GetAttachmentDownloadLinkRequest(TypedDict, closed=True):
    attachment_id: "capo_support.types.attachment_id.AttachmentId"
    """<p>The unique identifier of the attachment for which to retrieve a download link. Attachment IDs are returned in the <code>AttachmentDetails</code> objects in the <code>attachments</code> field of a <a>Communication</a> returned by <a>DescribeCommunications</a> or <a>DescribeCases</a>.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning a download link. When set to <code>true</code>, the request is validated but no URL is returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAttachmentDownloadLinkRequest) -> dict:
    out: dict = {}
    out["attachmentId"] = value["attachment_id"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAttachmentDownloadLinkRequest:
    out: GetAttachmentDownloadLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    else:
        out["attachment_id"] = ""
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
