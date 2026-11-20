"""Generated from Smithy shape ``com.amazonaws.abusesignal#GetAbuseReportStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_abuse_signal.types.report_id


class GetAbuseReportStatusRequest(TypedDict, closed=True):
    report_id: "capo_abuse_signal.types.report_id.ReportId"
    """<p>The unique identifier of the abuse report to retrieve status for. This is the <code>reportId</code> that is returned by <a>CreateAbuseReport</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAbuseReportStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAbuseReportStatusRequest:
    out: GetAbuseReportStatusRequest = {}  # type: ignore[typeddict-item]
    return out
