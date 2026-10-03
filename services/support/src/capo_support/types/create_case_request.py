"""Generated from Smithy shape ``com.amazonaws.support#CreateCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.attachment_set_id
    import capo_support.types.category_code
    import capo_support.types.cc_email_address_list
    import capo_support.types.communication_body
    import capo_support.types.issue_type
    import capo_support.types.language
    import capo_support.types.nullable_boolean_type
    import capo_support.types.service_code2
    import capo_support.types.severity_code
    import capo_support.types.subject
    import capo_support.types.upload_ids


class CreateCaseRequest(TypedDict, closed=True):
    subject: "capo_support.types.subject.Subject"
    """<p>The title of the support case. The title appears in the <b>Subject</b> field on the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page.</p>"""
    service_code: NotRequired["capo_support.types.service_code2.ServiceCode2"]
    """<p>The code for the Amazon Web Services service. You can use the <a>DescribeServices</a> operation to get the possible <code>serviceCode</code> values.</p>"""
    severity_code: NotRequired["capo_support.types.severity_code.SeverityCode"]
    """<p>A value that indicates the urgency of the case. This value determines the response time according to your service level agreement with Amazon Web Services Support. You can use the <a>DescribeSeverityLevels</a> operation to get the possible values for <code>severityCode</code>. </p> <p>For more information, see <a>SeverityLevel</a> and <a href="https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html#choosing-severity">Choosing a Severity</a> in the <i>Amazon Web Services Support User Guide</i>.</p> <note> <p>The availability of severity levels depends on the support plan for the Amazon Web Services account.</p> </note>"""
    category_code: NotRequired["capo_support.types.category_code.CategoryCode"]
    """<p>The category of problem for the support case. You also use the <a>DescribeServices</a> operation to get the category code for a service. Each Amazon Web Services service defines its own set of category codes.</p>"""
    communication_body: "capo_support.types.communication_body.CommunicationBody"
    """<p>The communication body text that describes the issue. This text appears in the <b>Description</b> field on the Amazon Web Services Support Center <a href="https://console.aws.amazon.com/support/home#/case/create">Create Case</a> page.</p>"""
    cc_email_addresses: NotRequired[
        "capo_support.types.cc_email_address_list.CcEmailAddressList"
    ]
    """<p>A list of email addresses that Amazon Web Services Support copies on case correspondence. Amazon Web Services Support identifies the account that creates the case when you specify your Amazon Web Services credentials in an HTTP POST method or use the <a href="http://aws.amazon.com/tools/">Amazon Web Services SDKs</a>. </p>"""
    language: NotRequired["capo_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""
    issue_type: NotRequired["capo_support.types.issue_type.IssueType"]
    """<p>The type of issue for the case. You can specify <code>customer-service</code> or <code>technical</code>. If you don't specify a value, the default is <code>technical</code>.</p>"""
    attachment_set_id: NotRequired[
        "capo_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of a set of one or more attachments for the case. Create the set by using the <a>AddAttachmentsToSet</a> operation. Each attachment in the set must be 5 MB or smaller. To attach files larger than 5 MB, use <code>uploadIds</code>.</p>"""
    upload_ids: NotRequired["capo_support.types.upload_ids.UploadIds"]
    """<p>A list of upload IDs that identify attachments to add to the case. Each <code>uploadId</code> is returned by the <a>GetAttachmentUploadLinks</a> operation. The upload must reach the <code>attachment-ready</code> state by calling <a>CompleteAttachmentUpload</a> before it can be passed here. Use <code>uploadIds</code> to attach files of any supported size, including files larger than 5 MB.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually creating the case. When set to <code>true</code>, the request is validated but no case is created, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCaseRequest) -> dict:
    out: dict = {}
    out["subject"] = value["subject"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "severity_code" in value:
        out["severityCode"] = value["severity_code"]
    if "category_code" in value:
        out["categoryCode"] = value["category_code"]
    out["communicationBody"] = value["communication_body"]
    if "cc_email_addresses" in value:
        import capo_support.types.cc_email_address_list

        out["ccEmailAddresses"] = (
            capo_support.types.cc_email_address_list.serialize_aws_json_1_1(
                value["cc_email_addresses"]
            )
        )
    if "language" in value:
        out["language"] = value["language"]
    if "issue_type" in value:
        out["issueType"] = value["issue_type"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateCaseRequest:
    out: CreateCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("subject") is not None:
        out["subject"] = data["subject"]
    else:
        raise DeserializationError("CreateCaseRequest.subject required")
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("severityCode") is not None:
        out["severity_code"] = data["severityCode"]
    if data.get("categoryCode") is not None:
        out["category_code"] = data["categoryCode"]
    if data.get("communicationBody") is not None:
        out["communication_body"] = data["communicationBody"]
    else:
        raise DeserializationError("CreateCaseRequest.communication_body required")
    if data.get("ccEmailAddresses") is not None:
        import capo_support.types.cc_email_address_list

        out["cc_email_addresses"] = (
            capo_support.types.cc_email_address_list.deserialize_aws_json_1_1(
                data["ccEmailAddresses"]
            )
        )
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("issueType") is not None:
        out["issue_type"] = data["issueType"]
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
