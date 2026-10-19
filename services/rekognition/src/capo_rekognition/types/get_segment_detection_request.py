"""Generated from Smithy shape ``com.amazonaws.rekognition#GetSegmentDetectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.job_id
    import capo_rekognition.types.max_results
    import capo_rekognition.types.pagination_token


class GetSegmentDetectionRequest(TypedDict, closed=True):
    job_id: "capo_rekognition.types.job_id.JobId"
    """<p>Job identifier for the text detection operation for which you want results returned. You get the job identifer from an initial call to <code>StartSegmentDetection</code>.</p>"""
    max_results: NotRequired["capo_rekognition.types.max_results.MaxResults"]
    """<p>Maximum number of results to return per paginated call. The largest value you can specify is 1000.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSegmentDetectionRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSegmentDetectionRequest:
    out: GetSegmentDetectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
