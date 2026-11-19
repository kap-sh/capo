"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListAnalysisReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_reports
    import capo_network_firewall.types.pagination_token


class ListAnalysisReportsResponse(TypedDict, closed=True):
    analysis_reports: NotRequired[
        "capo_network_firewall.types.analysis_reports.AnalysisReports"
    ]
    """<p>The <code>id</code> and <code>ReportTime</code> associated with a requested analysis report. Does not provide the status of the analysis report. </p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAnalysisReportsResponse) -> dict:
    out: dict = {}
    if "analysis_reports" in value:
        import capo_network_firewall.types.analysis_reports

        out["AnalysisReports"] = (
            capo_network_firewall.types.analysis_reports.serialize_aws_json_1_0(
                value["analysis_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAnalysisReportsResponse:
    out: ListAnalysisReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReports") is not None:
        import capo_network_firewall.types.analysis_reports

        out["analysis_reports"] = (
            capo_network_firewall.types.analysis_reports.deserialize_aws_json_1_0(
                data["AnalysisReports"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAnalysisReportsResponse) -> dict:
    out: dict = {}
    if "analysis_reports" in value:
        import capo_network_firewall.types.analysis_reports

        out["AnalysisReports"] = (
            capo_network_firewall.types.analysis_reports.serialize_cbor(
                value["analysis_reports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAnalysisReportsResponse:
    out: ListAnalysisReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisReports") is not None:
        import capo_network_firewall.types.analysis_reports

        out["analysis_reports"] = (
            capo_network_firewall.types.analysis_reports.deserialize_cbor(
                data["AnalysisReports"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
