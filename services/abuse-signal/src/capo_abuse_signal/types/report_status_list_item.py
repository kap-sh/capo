"""Generated from Smithy shape ``com.amazonaws.abusesignal#ReportStatusListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_abuse_signal.types.correlation_id
    import capo_abuse_signal.types.reason_code
    import capo_abuse_signal.types.report_id
    import capo_abuse_signal.types.report_submission_status


class ReportStatusListItem(TypedDict, closed=True):
    report_id: "capo_abuse_signal.types.report_id.ReportId"
    """<p>The unique identifier of the abuse report.</p>"""
    correlation_id: NotRequired["capo_abuse_signal.types.correlation_id.CorrelationId"]
    """<p>The reporter-provided correlation ID for cross-referencing.</p>"""
    status: "capo_abuse_signal.types.report_submission_status.ReportSubmissionStatus"
    """<p>The current processing status of the abuse report. Valid values are <code>QUEUED</code> (the report has been received and queued for processing), <code>PROCESSING</code> (the report has been received and is being processed), and <code>COMPLETED</code> (downstream resolution is finished).</p>"""
    description: "str"
    """<p>A human-readable description of the status.</p>"""
    reason_code: NotRequired["capo_abuse_signal.types.reason_code.ReasonCode"]
    """<p>A code that explains the resolution outcome. This value is present only after the report reaches the terminal <code>COMPLETED</code> status; it is absent while the report is <code>QUEUED</code> or <code>PROCESSING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportStatusListItem) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    if "correlation_id" in value:
        out["correlationId"] = value["correlation_id"]
    import capo_abuse_signal.types.report_submission_status

    out["status"] = capo_abuse_signal.types.report_submission_status.serialize_json(
        value["status"]
    )
    out["description"] = value["description"]
    if "reason_code" in value:
        import capo_abuse_signal.types.reason_code

        out["reasonCode"] = capo_abuse_signal.types.reason_code.serialize_json(
            value["reason_code"]
        )
    return out


def deserialize_json(data: dict) -> ReportStatusListItem:
    out: ReportStatusListItem = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    if data.get("correlationId") is not None:
        out["correlation_id"] = data["correlationId"]
    if data.get("status") is not None:
        import capo_abuse_signal.types.report_submission_status

        out["status"] = (
            capo_abuse_signal.types.report_submission_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_abuse_signal.types.report_submission_status.ReportSubmissionStatus",
            "",
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("reasonCode") is not None:
        import capo_abuse_signal.types.reason_code

        out["reason_code"] = capo_abuse_signal.types.reason_code.deserialize_json(
            data["reasonCode"]
        )
    return out
