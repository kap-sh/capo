"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetQuotaUtilizationReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.max_results_utilization
    import capo_service_quotas.types.next_token
    import capo_service_quotas.types.report_id


class GetQuotaUtilizationReportRequest(TypedDict, closed=True):
    report_id: "capo_service_quotas.types.report_id.ReportId"
    """<p>The unique identifier for the quota utilization report. This identifier is returned by the <code>StartQuotaUtilizationReport</code> operation.</p>"""
    next_token: NotRequired["capo_service_quotas.types.next_token.NextToken"]
    """<p>A token that indicates the next page of results to retrieve. This token is returned in the response when there are more results available. Omit this parameter for the first request.</p>"""
    max_results: NotRequired[
        "capo_service_quotas.types.max_results_utilization.MaxResultsUtilization"
    ]
    """<p>The maximum number of results to return per page. The default value is 1,000 and the maximum allowed value is 1,000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQuotaUtilizationReportRequest) -> dict:
    out: dict = {}
    out["ReportId"] = value["report_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQuotaUtilizationReportRequest:
    out: GetQuotaUtilizationReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReportId") is not None:
        out["report_id"] = data["ReportId"]
    else:
        out["report_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
