"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartAnalysisReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_report_id


class StartAnalysisReportResponse(TypedDict, closed=True):
    analysis_report_id: (
        "capo_network_firewall.types.analysis_report_id.AnalysisReportId"
    )
    """<p>The unique ID of the query that ran when you requested an analysis report. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAnalysisReportResponse) -> dict:
    out: dict = {}
    out["AnalysisReportId"] = value["analysis_report_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAnalysisReportResponse:
    out: StartAnalysisReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        out["analysis_report_id"] = ""
    return out
