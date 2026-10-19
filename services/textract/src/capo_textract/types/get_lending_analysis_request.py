"""Generated from Smithy shape ``com.amazonaws.textract#GetLendingAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.job_id
    import capo_textract.types.max_results
    import capo_textract.types.pagination_token


class GetLendingAnalysisRequest(TypedDict, closed=True):
    job_id: "capo_textract.types.job_id.JobId"
    """<p>A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from <code>StartLendingAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>"""
    max_results: NotRequired["capo_textract.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per paginated call. The largest value that you can specify is 30. If you specify a value greater than 30, a maximum of 30 results is returned. The default value is 30.</p>"""
    next_token: NotRequired["capo_textract.types.pagination_token.PaginationToken"]
    """<p>If the previous response was incomplete, Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of lending results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLendingAnalysisRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLendingAnalysisRequest:
    out: GetLendingAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
