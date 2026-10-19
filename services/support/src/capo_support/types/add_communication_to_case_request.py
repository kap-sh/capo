"""Generated from Smithy shape ``com.amazonaws.support#AddCommunicationToCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.attachment_set_id
    import capo_support.types.case_id
    import capo_support.types.cc_email_address_list
    import capo_support.types.communication_body
    import capo_support.types.nullable_boolean_type
    import capo_support.types.upload_ids


class AddCommunicationToCaseRequest(TypedDict, closed=True):
    case_id: NotRequired["capo_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>"""
    communication_body: "capo_support.types.communication_body.CommunicationBody"
    """<p>The body of an email communication to add to the support case.</p>"""
    cc_email_addresses: NotRequired[
        "capo_support.types.cc_email_address_list.CcEmailAddressList"
    ]
    """<p>The email addresses in the CC line of an email to be added to the support case.</p>"""
    attachment_set_id: NotRequired[
        "capo_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of a set of one or more attachments for the communication to add to the case. Create the set by calling <a>AddAttachmentsToSet</a>. Each attachment in the set must be 5 MB or smaller. To attach files larger than 5 MB, use <code>uploadIds</code>.</p>"""
    upload_ids: NotRequired["capo_support.types.upload_ids.UploadIds"]
    """<p>A list of upload IDs that identify attachments to add to the case. Each <code>uploadId</code> is returned by the <a>GetAttachmentUploadLinks</a> operation. The upload must reach the <code>attachment-ready</code> state by calling <a>CompleteAttachmentUpload</a> before it can be passed here. Use <code>uploadIds</code> to attach files of any supported size, including files larger than 5 MB.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually adding the communication to the case. When set to <code>true</code>, the request is validated but the communication isn't added, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCommunicationToCaseRequest) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    out["communicationBody"] = value["communication_body"]
    if "cc_email_addresses" in value:
        import capo_support.types.cc_email_address_list

        out["ccEmailAddresses"] = (
            capo_support.types.cc_email_address_list.serialize_aws_json_1_1(
                value["cc_email_addresses"]
            )
        )
    if "attachment_set_id" in value:
        out["attachmentSetId"] = value["attachment_set_id"]
    if "upload_ids" in value:
        import capo_support.types.upload_ids

        out["uploadIds"] = capo_support.types.upload_ids.serialize_aws_json_1_1(
            value["upload_ids"]
        )
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCommunicationToCaseRequest:
    out: AddCommunicationToCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    if data.get("communicationBody") is not None:
        out["communication_body"] = data["communicationBody"]
    else:
        out["communication_body"] = ""
    if data.get("ccEmailAddresses") is not None:
        import capo_support.types.cc_email_address_list

        out["cc_email_addresses"] = (
            capo_support.types.cc_email_address_list.deserialize_aws_json_1_1(
                data["ccEmailAddresses"]
            )
        )
    if data.get("attachmentSetId") is not None:
        out["attachment_set_id"] = data["attachmentSetId"]
    if data.get("uploadIds") is not None:
        import capo_support.types.upload_ids

        out["upload_ids"] = capo_support.types.upload_ids.deserialize_aws_json_1_1(
            data["uploadIds"]
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
