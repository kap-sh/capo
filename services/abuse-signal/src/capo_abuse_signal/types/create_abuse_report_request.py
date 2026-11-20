"""Generated from Smithy shape ``com.amazonaws.abusesignal#CreateAbuseReportRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_abuse_signal.types.client_token
    import capo_abuse_signal.types.correlation_id
    import capo_abuse_signal.types.report_data


class CreateAbuseReportRequest(TypedDict, closed=True):
    report: "capo_abuse_signal.types.report_data.ReportData"
    """<p>The abuse report data in XARF format. Provide the report under the <code>xarf</code> key.</p>"""
    correlation_id: NotRequired["capo_abuse_signal.types.correlation_id.CorrelationId"]
    """<p>An optional correlation ID for tracking the report in the reporter's system. The service echoes this value back in responses, and you can use it to filter reports with <a>ListAbuseReportStatuses</a>.</p>"""
    client_token: NotRequired["capo_abuse_signal.types.client_token.ClientToken"]
    """<p>An optional, client-provided idempotency token that ensures the operation completes no more than once. If the token matches a previous request within 24 hours, the service returns the existing report ID instead of creating a new report. When you omit this token, the service automatically generates one that is scoped to a 5-minute window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAbuseReportRequest) -> dict:
    out: dict = {}
    import capo_abuse_signal.types.report_data

    out["report"] = capo_abuse_signal.types.report_data.serialize_json(value["report"])
    if "correlation_id" in value:
        out["correlationId"] = value["correlation_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAbuseReportRequest:
    out: CreateAbuseReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("report") is not None:
        import capo_abuse_signal.types.report_data

        out["report"] = capo_abuse_signal.types.report_data.deserialize_json(
            data["report"]
        )
    else:
        out["report"] = {"$unknown": {"name": ""}}
    if data.get("correlationId") is not None:
        out["correlation_id"] = data["correlationId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateAbuseReportRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "report" in value:
        out["report"] = "*** Sensitive Data Redacted ***"
    return out
