"""Generated from Smithy shape ``com.amazonaws.costexplorer#StartCommitmentPurchaseAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.analysis_id
    import capo_cost_explorer.types.zoned_date_time


class StartCommitmentPurchaseAnalysisResponse(TypedDict, closed=True):
    analysis_id: "capo_cost_explorer.types.analysis_id.AnalysisId"
    """<p>The analysis ID that's associated with the commitment purchase analysis.</p>"""
    analysis_started_time: "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    """<p>The start time of the analysis.</p>"""
    estimated_completion_time: "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    """<p>The estimated time for when the analysis will complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCommitmentPurchaseAnalysisResponse) -> dict:
    out: dict = {}
    out["AnalysisId"] = value["analysis_id"]
    out["AnalysisStartedTime"] = value["analysis_started_time"]
    out["EstimatedCompletionTime"] = value["estimated_completion_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCommitmentPurchaseAnalysisResponse:
    out: StartCommitmentPurchaseAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisId") is not None:
        out["analysis_id"] = data["AnalysisId"]
    else:
        out["analysis_id"] = ""
    if data.get("AnalysisStartedTime") is not None:
        out["analysis_started_time"] = data["AnalysisStartedTime"]
    else:
        out["analysis_started_time"] = ""
    if data.get("EstimatedCompletionTime") is not None:
        out["estimated_completion_time"] = data["EstimatedCompletionTime"]
    else:
        out["estimated_completion_time"] = ""
    return out
