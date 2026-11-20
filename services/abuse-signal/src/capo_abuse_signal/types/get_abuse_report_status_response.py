"""Generated from Smithy shape ``com.amazonaws.abusesignal#GetAbuseReportStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_abuse_signal.types.correlation_id
    import capo_abuse_signal.types.reason_code
    import capo_abuse_signal.types.report_id
    import capo_abuse_signal.types.report_submission_status


class GetAbuseReportStatusResponse(TypedDict, closed=True):
    report_id: "capo_abuse_signal.types.report_id.ReportId"
    """<p>The unique identifier of the abuse report.</p>"""
    correlation_id: NotRequired["capo_abuse_signal.types.correlation_id.CorrelationId"]
    """<p>The reporter-provided correlation ID for cross-referencing.</p>"""
    status: "capo_abuse_signal.types.report_submission_status.ReportSubmissionStatus"
    """<p>The current processing status of the abuse report. Valid values are <code>QUEUED</code> (the report has been received and queued for processing), <code>PROCESSING</code> (the report has been received and is being processed), and <code>COMPLETED</code> (downstream resolution is finished).</p>"""
    description: "str"
    """<p>A human-readable description of the current status.</p>"""
    reason_code: NotRequired["capo_abuse_signal.types.reason_code.ReasonCode"]
    """<p>A code that explains the resolution outcome. This value is returned only after the report reaches the terminal <code>COMPLETED</code> status; it is absent while the report is <code>QUEUED</code> or <code>PROCESSING</code>. Treat an unrecognized value as opaque, because the set of reason codes is append-only.</p>"""
    submitted_at: "datetime.datetime"
    """<p>The date and time when the abuse report was submitted.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the status was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAbuseReportStatusResponse) -> dict:
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
    import capo_abuse_signal.types._prelude.timestamp

    out["submittedAt"] = capo_abuse_signal.types._prelude.timestamp.serialize_json(
        value["submitted_at"]
    )
    if "last_updated_at" in value:
        import capo_abuse_signal.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            capo_abuse_signal.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAbuseReportStatusResponse:
    out: GetAbuseReportStatusResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("submittedAt") is not None:
        import capo_abuse_signal.types._prelude.timestamp

        out["submitted_at"] = (
            capo_abuse_signal.types._prelude.timestamp.deserialize_json(
                data["submittedAt"]
            )
        )
    else:
        import datetime

        out["submitted_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_abuse_signal.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_abuse_signal.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
