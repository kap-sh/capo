"""Generated from Smithy shape ``com.amazonaws.abusesignal#CreateAbuseReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_abuse_signal.types.correlation_id
    import capo_abuse_signal.types.report_id


class CreateAbuseReportResponse(TypedDict, closed=True):
    report_id: "capo_abuse_signal.types.report_id.ReportId"
    """<p>The unique identifier assigned to the submitted abuse report. Use this ID with <a>GetAbuseReportStatus</a> to track processing.</p>"""
    correlation_id: NotRequired["capo_abuse_signal.types.correlation_id.CorrelationId"]
    """<p>The correlation ID that you provided in the request, if any. The service echoes this value back in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAbuseReportResponse) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    if "correlation_id" in value:
        out["correlationId"] = value["correlation_id"]
    return out


def deserialize_json(data: dict) -> CreateAbuseReportResponse:
    out: CreateAbuseReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    if data.get("correlationId") is not None:
        out["correlation_id"] = data["correlationId"]
    return out
