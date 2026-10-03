"""Generated from Smithy shape ``com.amazonaws.support#Communication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.attachment_set
    import capo_support.types.case_id
    import capo_support.types.submitted_by
    import capo_support.types.time_created
    import capo_support.types.validated_communication_body


class Communication(TypedDict, closed=True):
    case_id: NotRequired["capo_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>"""
    body: NotRequired[
        "capo_support.types.validated_communication_body.ValidatedCommunicationBody"
    ]
    """<p>The text of the communication between the customer and Amazon Web Services Support.</p>"""
    submitted_by: NotRequired["capo_support.types.submitted_by.SubmittedBy"]
    """<p>The identity of the account that submitted, or responded to, the support case. Customer entries include the IAM role as well as the email address (for example, "AdminRole (Role) <janedoe@example.com>). Entries from the Amazon Web Services Support team display "Amazon Web Services," and don't show an email address. </p>"""
    time_created: NotRequired["capo_support.types.time_created.TimeCreated"]
    """<p>The time the communication was created.</p>"""
    attachments: NotRequired["capo_support.types.attachment_set.AttachmentSet"]
    """<p>Information about all attachments on the case communication. This includes attachments added through <code>AddAttachmentsToSet</code> and attachments uploaded through <code>GetAttachmentUploadLinks</code>.</p> <p>Use this field to enumerate every attachment on the communication. To download an attachment listed in this field, use <a>GetAttachmentDownloadLink</a>. <code>GetAttachmentDownloadLink</code> returns a presigned URL that works for attachments of any size. </p>"""
    attachment_set: NotRequired["capo_support.types.attachment_set.AttachmentSet"]
    """<p>Information about the attachments to the case communication that are 5 MB or smaller. This field doesn't include attachments larger than 5 MB. To enumerate every attachment on the communication, including attachments larger than 5 MB, use the <code>attachments</code> field instead.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Communication) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "body" in value:
        out["body"] = value["body"]
    if "submitted_by" in value:
        out["submittedBy"] = value["submitted_by"]
    if "time_created" in value:
        out["timeCreated"] = value["time_created"]
    if "attachments" in value:
        import capo_support.types.attachment_set

        out["attachments"] = capo_support.types.attachment_set.serialize_aws_json_1_1(
            value["attachments"]
        )
    if "attachment_set" in value:
        import capo_support.types.attachment_set

        out["attachmentSet"] = capo_support.types.attachment_set.serialize_aws_json_1_1(
            value["attachment_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Communication:
    out: Communication = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    if data.get("body") is not None:
        out["body"] = data["body"]
    if data.get("submittedBy") is not None:
        out["submitted_by"] = data["submittedBy"]
    if data.get("timeCreated") is not None:
        out["time_created"] = data["timeCreated"]
    if data.get("attachments") is not None:
        import capo_support.types.attachment_set

        out["attachments"] = capo_support.types.attachment_set.deserialize_aws_json_1_1(
            data["attachments"]
        )
    if data.get("attachmentSet") is not None:
        import capo_support.types.attachment_set

        out["attachment_set"] = (
            capo_support.types.attachment_set.deserialize_aws_json_1_1(
                data["attachmentSet"]
            )
        )
    return out
