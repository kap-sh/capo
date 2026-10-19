"""Generated from Smithy shape ``com.amazonaws.support#AddAttachmentsToSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.attachment_set_id
    import capo_support.types.attachments
    import capo_support.types.nullable_boolean_type


class AddAttachmentsToSetRequest(TypedDict, closed=True):
    attachment_set_id: NotRequired[
        "capo_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of the attachment set. If an <code>attachmentSetId</code> is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an <code>attachmentSetId</code> is specified, the attachments are added to the specified set, if it exists.</p>"""
    attachments: "capo_support.types.attachments.Attachments"
    """<p>One or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.</p> <p>In the <code>Attachment</code> object, use the <code>data</code> parameter to specify the contents of the attachment file. In the previous request syntax, the value for <code>data</code> appear as <code>blob</code>, which is represented as a base64-encoded string. The value for <code>fileName</code> is the name of the attachment, such as <code>troubleshoot-screenshot.png</code>.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually adding the attachments. When set to <code>true</code>, the request is validated but no attachments are stored, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddAttachmentsToSetRequest) -> dict:
    out: dict = {}
    if "attachment_set_id" in value:
        out["attachmentSetId"] = value["attachment_set_id"]
    import capo_support.types.attachments

    out["attachments"] = capo_support.types.attachments.serialize_aws_json_1_1(
        value["attachments"]
    )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddAttachmentsToSetRequest:
    out: AddAttachmentsToSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("attachmentSetId") is not None:
        out["attachment_set_id"] = data["attachmentSetId"]
    if data.get("attachments") is not None:
        import capo_support.types.attachments

        out["attachments"] = capo_support.types.attachments.deserialize_aws_json_1_1(
            data["attachments"]
        )
    else:
        out["attachments"] = []
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
