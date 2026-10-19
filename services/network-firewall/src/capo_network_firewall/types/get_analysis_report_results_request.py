"""Generated from Smithy shape ``com.amazonaws.networkfirewall#GetAnalysisReportResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_report_id
    import capo_network_firewall.types.analysis_report_next_token
    import capo_network_firewall.types.pagination_max_results
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class GetAnalysisReportResultsRequest(TypedDict, closed=True):
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    analysis_report_id: (
        "capo_network_firewall.types.analysis_report_id.AnalysisReportId"
    )
    """<p>The unique ID of the query that ran when you requested an analysis report. </p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.analysis_report_next_token.AnalysisReportNextToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    max_results: NotRequired[
        "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAnalysisReportResultsRequest) -> dict:
    out: dict = {}
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    out["AnalysisReportId"] = value["analysis_report_id"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAnalysisReportResultsRequest:
    out: GetAnalysisReportResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("AnalysisReportId") is not None:
        out["analysis_report_id"] = data["AnalysisReportId"]
    else:
        out["analysis_report_id"] = ""
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
