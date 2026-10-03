"""Generated from Smithy shape ``com.amazonaws.support#CaseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.case_id
    import capo_support.types.category_code
    import capo_support.types.cc_email_address_list
    import capo_support.types.display_id
    import capo_support.types.language
    import capo_support.types.recent_case_communications
    import capo_support.types.service_code
    import capo_support.types.severity_code
    import capo_support.types.status
    import capo_support.types.subject
    import capo_support.types.submitted_by
    import capo_support.types.time_created


class CaseDetails(TypedDict, closed=True):
    case_id: NotRequired["capo_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>"""
    display_id: NotRequired["capo_support.types.display_id.DisplayId"]
    """<p>The ID displayed for the case in the Amazon Web Services Support Center. This is a numeric string.</p>"""
    subject: NotRequired["capo_support.types.subject.Subject"]
    """<p>The subject line for the case in the Amazon Web Services Support Center.</p>"""
    status: NotRequired["capo_support.types.status.Status"]
    """<p>The status of the case.</p> <p>Valid values:</p> <ul> <li> <p> <code>all-open</code> </p> </li> <li> <p> <code>customer-action-completed</code> </p> </li> <li> <p> <code>opened</code> </p> </li> <li> <p> <code>pending-customer-action</code> </p> </li> <li> <p> <code>reopened</code> </p> </li> <li> <p> <code>resolved</code> </p> </li> <li> <p> <code>unassigned</code> </p> </li> <li> <p> <code>work-in-progress</code> </p> </li> </ul>"""
    service_code: NotRequired["capo_support.types.service_code.ServiceCode"]
    """<p>The code for the Amazon Web Services service. You can get a list of codes and the corresponding service names by calling <a>DescribeServices</a>.</p>"""
    category_code: NotRequired["capo_support.types.category_code.CategoryCode"]
    """<p>The category of problem for the support case.</p>"""
    severity_code: NotRequired["capo_support.types.severity_code.SeverityCode"]
    """<p>The code for the severity level returned by the call to <a>DescribeSeverityLevels</a>.</p>"""
    submitted_by: NotRequired["capo_support.types.submitted_by.SubmittedBy"]
    """<p>The email address of the account that submitted the case.</p>"""
    time_created: NotRequired["capo_support.types.time_created.TimeCreated"]
    """<p>The time that the case was created in the Amazon Web Services Support Center.</p>"""
    recent_communications: NotRequired[
        "capo_support.types.recent_case_communications.RecentCaseCommunications"
    ]
    """<p>The five most recent communications between you and Amazon Web Services Support Center, including the IDs of any attachments to the communications. Also includes a <code>nextToken</code> that you can use to retrieve earlier communications.</p>"""
    cc_email_addresses: NotRequired[
        "capo_support.types.cc_email_address_list.CcEmailAddressList"
    ]
    """<p>The email addresses that receive copies of communication about the case.</p>"""
    language: NotRequired["capo_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English ("en"), Japanese ("ja") , Chinese ("zh"), Spanish ("es"), Portuguese ("pt"), French ("fr"), Korean (“ko”), and Turkish ("tr"). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseDetails) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    if "display_id" in value:
        out["displayId"] = value["display_id"]
    if "subject" in value:
        out["subject"] = value["subject"]
    if "status" in value:
        out["status"] = value["status"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "category_code" in value:
        out["categoryCode"] = value["category_code"]
    if "severity_code" in value:
        out["severityCode"] = value["severity_code"]
    if "submitted_by" in value:
        out["submittedBy"] = value["submitted_by"]
    if "time_created" in value:
        out["timeCreated"] = value["time_created"]
    if "recent_communications" in value:
        import capo_support.types.recent_case_communications

        out["recentCommunications"] = (
            capo_support.types.recent_case_communications.serialize_aws_json_1_1(
                value["recent_communications"]
            )
        )
    if "cc_email_addresses" in value:
        import capo_support.types.cc_email_address_list

        out["ccEmailAddresses"] = (
            capo_support.types.cc_email_address_list.serialize_aws_json_1_1(
                value["cc_email_addresses"]
            )
        )
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CaseDetails:
    out: CaseDetails = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    if data.get("displayId") is not None:
        out["display_id"] = data["displayId"]
    if data.get("subject") is not None:
        out["subject"] = data["subject"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("categoryCode") is not None:
        out["category_code"] = data["categoryCode"]
    if data.get("severityCode") is not None:
        out["severity_code"] = data["severityCode"]
    if data.get("submittedBy") is not None:
        out["submitted_by"] = data["submittedBy"]
    if data.get("timeCreated") is not None:
        out["time_created"] = data["timeCreated"]
    if data.get("recentCommunications") is not None:
        import capo_support.types.recent_case_communications

        out["recent_communications"] = (
            capo_support.types.recent_case_communications.deserialize_aws_json_1_1(
                data["recentCommunications"]
            )
        )
    if data.get("ccEmailAddresses") is not None:
        import capo_support.types.cc_email_address_list

        out["cc_email_addresses"] = (
            capo_support.types.cc_email_address_list.deserialize_aws_json_1_1(
                data["ccEmailAddresses"]
            )
        )
    if data.get("language") is not None:
        out["language"] = data["language"]
    return out
