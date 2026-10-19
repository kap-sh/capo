"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateDeliverabilityTestReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.deliverability_test_status
    import capo_pinpoint_email.types.report_id


class CreateDeliverabilityTestReportResponse(TypedDict, closed=True):
    report_id: "capo_pinpoint_email.types.report_id.ReportId"
    """<p>A unique string that identifies the predictive inbox placement test.</p>"""
    deliverability_test_status: (
        "capo_pinpoint_email.types.deliverability_test_status.DeliverabilityTestStatus"
    )
    """<p>The status of the predictive inbox placement test. If the status is <code>IN_PROGRESS</code>, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is <code>COMPLETE</code>, then the test is finished, and you can use the <code>GetDeliverabilityTestReport</code> to view the results of the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeliverabilityTestReportResponse) -> dict:
    out: dict = {}
    out["ReportId"] = value["report_id"]
    import capo_pinpoint_email.types.deliverability_test_status

    out["DeliverabilityTestStatus"] = (
        capo_pinpoint_email.types.deliverability_test_status.serialize_json(
            value["deliverability_test_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateDeliverabilityTestReportResponse:
    out: CreateDeliverabilityTestReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("ReportId") is not None:
        out["report_id"] = data["ReportId"]
    else:
        out["report_id"] = ""
    if data.get("DeliverabilityTestStatus") is not None:
        import capo_pinpoint_email.types.deliverability_test_status

        out["deliverability_test_status"] = (
            capo_pinpoint_email.types.deliverability_test_status.deserialize_json(
                data["DeliverabilityTestStatus"]
            )
        )
    else:
        import typing

        out["deliverability_test_status"] = typing.cast(
            "capo_pinpoint_email.types.deliverability_test_status.DeliverabilityTestStatus",
            "",
        )
    return out
