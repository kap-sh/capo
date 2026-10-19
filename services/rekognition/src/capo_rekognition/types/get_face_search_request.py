"""Generated from Smithy shape ``com.amazonaws.rekognition#GetFaceSearchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.face_search_sort_by
    import capo_rekognition.types.job_id
    import capo_rekognition.types.max_results
    import capo_rekognition.types.pagination_token


class GetFaceSearchRequest(TypedDict, closed=True):
    job_id: "capo_rekognition.types.job_id.JobId"
    """<p>The job identifer for the search request. You get the job identifier from an initial call to <code>StartFaceSearch</code>.</p>"""
    max_results: NotRequired["capo_rekognition.types.max_results.MaxResults"]
    """<p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the previous response was incomplete (because there is more search results to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of search results. </p>"""
    sort_by: NotRequired["capo_rekognition.types.face_search_sort_by.FaceSearchSortBy"]
    """<p>Sort to use for grouping faces in the response. Use <code>TIMESTAMP</code> to group faces by the time that they are recognized. Use <code>INDEX</code> to sort by recognized faces. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFaceSearchRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_rekognition.types.face_search_sort_by

        out["SortBy"] = (
            capo_rekognition.types.face_search_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFaceSearchRequest:
    out: GetFaceSearchRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SortBy") is not None:
        import capo_rekognition.types.face_search_sort_by

        out["sort_by"] = (
            capo_rekognition.types.face_search_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    return out
