"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCommitmentPurchaseAnalysesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.analyses_page_size
    import capo_cost_explorer.types.analysis_ids
    import capo_cost_explorer.types.analysis_status
    import capo_cost_explorer.types.next_page_token


class ListCommitmentPurchaseAnalysesRequest(TypedDict, closed=True):
    analysis_status: NotRequired[
        "capo_cost_explorer.types.analysis_status.AnalysisStatus"
    ]
    """<p>The status of the analysis.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""
    page_size: NotRequired[
        "capo_cost_explorer.types.analyses_page_size.AnalysesPageSize"
    ]
    """<p>The number of analyses that you want returned in a single response object.</p>"""
    analysis_ids: NotRequired["capo_cost_explorer.types.analysis_ids.AnalysisIds"]
    """<p>The analysis IDs associated with the commitment purchase analyses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommitmentPurchaseAnalysesRequest) -> dict:
    out: dict = {}
    if "analysis_status" in value:
        import capo_cost_explorer.types.analysis_status

        out["AnalysisStatus"] = (
            capo_cost_explorer.types.analysis_status.serialize_aws_json_1_1(
                value["analysis_status"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "analysis_ids" in value:
        import capo_cost_explorer.types.analysis_ids

        out["AnalysisIds"] = (
            capo_cost_explorer.types.analysis_ids.serialize_aws_json_1_1(
                value["analysis_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCommitmentPurchaseAnalysesRequest:
    out: ListCommitmentPurchaseAnalysesRequest = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisStatus") is not None:
        import capo_cost_explorer.types.analysis_status

        out["analysis_status"] = (
            capo_cost_explorer.types.analysis_status.deserialize_aws_json_1_1(
                data["AnalysisStatus"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("AnalysisIds") is not None:
        import capo_cost_explorer.types.analysis_ids

        out["analysis_ids"] = (
            capo_cost_explorer.types.analysis_ids.deserialize_aws_json_1_1(
                data["AnalysisIds"]
            )
        )
    return out
