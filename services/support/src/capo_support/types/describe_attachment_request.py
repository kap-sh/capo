"""Generated from Smithy shape ``com.amazonaws.support#DescribeAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.attachment_id
    import capo_support.types.nullable_boolean_type


class DescribeAttachmentRequest(TypedDict, closed=True):
    attachment_id: "capo_support.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment to return. Attachment IDs are returned by the <a>DescribeCommunications</a> operation.</p> <p>If the specified attachment is larger than 5 MB, this operation returns <code>InvalidParameterValueException</code>. To download attachments larger than 5 MB, use <a>GetAttachmentDownloadLink</a>.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually retrieving the attachment. When set to <code>true</code>, the request is validated but no attachment content is returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttachmentRequest) -> dict:
    out: dict = {}
    out["attachmentId"] = value["attachment_id"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttachmentRequest:
    out: DescribeAttachmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    else:
        out["attachment_id"] = ""
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
