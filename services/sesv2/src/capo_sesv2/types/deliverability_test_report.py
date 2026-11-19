"""Generated from Smithy shape ``com.amazonaws.sesv2#DeliverabilityTestReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.deliverability_test_status
    import capo_sesv2.types.deliverability_test_subject
    import capo_sesv2.types.email_address
    import capo_sesv2.types.report_id
    import capo_sesv2.types.report_name
    import capo_sesv2.types.timestamp


class DeliverabilityTestReport(TypedDict, closed=True):
    report_id: NotRequired["capo_sesv2.types.report_id.ReportId"]
    """<p>A unique string that identifies the predictive inbox placement test.</p>"""
    report_name: NotRequired["capo_sesv2.types.report_name.ReportName"]
    """<p>A name that helps you identify a predictive inbox placement test report.</p>"""
    subject: NotRequired[
        "capo_sesv2.types.deliverability_test_subject.DeliverabilityTestSubject"
    ]
    """<p>The subject line for an email that you submitted in a predictive inbox placement test.</p>"""
    from_email_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The sender address that you specified for the predictive inbox placement test.</p>"""
    create_date: NotRequired["capo_sesv2.types.timestamp.Timestamp"]
    """<p>The date and time when the predictive inbox placement test was created.</p>"""
    deliverability_test_status: NotRequired[
        "capo_sesv2.types.deliverability_test_status.DeliverabilityTestStatus"
    ]
    """<p>The status of the predictive inbox placement test. If the status is <code>IN_PROGRESS</code>, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is <code>COMPLETED</code>, then the test is finished, and you can use the <code>GetDeliverabilityTestReport</code> operation to view the results of the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeliverabilityTestReport) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["ReportId"] = value["report_id"]
    if "report_name" in value:
        out["ReportName"] = value["report_name"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "create_date" in value:
        import capo_sesv2.types.timestamp

        out["CreateDate"] = capo_sesv2.types.timestamp.serialize_json(
            value["create_date"]
        )
    if "deliverability_test_status" in value:
        import capo_sesv2.types.deliverability_test_status

        out["DeliverabilityTestStatus"] = (
            capo_sesv2.types.deliverability_test_status.serialize_json(
                value["deliverability_test_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeliverabilityTestReport:
    out: DeliverabilityTestReport = {}  # type: ignore[typeddict-item]
    if data.get("ReportId") is not None:
        out["report_id"] = data["ReportId"]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    if data.get("CreateDate") is not None:
        import capo_sesv2.types.timestamp

        out["create_date"] = capo_sesv2.types.timestamp.deserialize_json(
            data["CreateDate"]
        )
    if data.get("DeliverabilityTestStatus") is not None:
        import capo_sesv2.types.deliverability_test_status

        out["deliverability_test_status"] = (
            capo_sesv2.types.deliverability_test_status.deserialize_json(
                data["DeliverabilityTestStatus"]
            )
        )
    return out
