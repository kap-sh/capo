"""Generated from Smithy shape ``com.amazonaws.rekognition#GetPersonTrackingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.job_id
    import capo_rekognition.types.max_results
    import capo_rekognition.types.pagination_token
    import capo_rekognition.types.person_tracking_sort_by


class GetPersonTrackingRequest(TypedDict, closed=True):
    job_id: "capo_rekognition.types.job_id.JobId"
    """<p>The identifier for a job that tracks persons in a video. You get the <code>JobId</code> from a call to <code>StartPersonTracking</code>. </p>"""
    max_results: NotRequired["capo_rekognition.types.max_results.MaxResults"]
    """<p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the previous response was incomplete (because there are more persons to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of persons. </p>"""
    sort_by: NotRequired[
        "capo_rekognition.types.person_tracking_sort_by.PersonTrackingSortBy"
    ]
    """<p>Sort to use for elements in the <code>Persons</code> array. Use <code>TIMESTAMP</code> to sort array elements by the time persons are detected. Use <code>INDEX</code> to sort by the tracked persons. If you sort by <code>INDEX</code>, the array elements for each person are sorted by detection confidence. The default sort is by <code>TIMESTAMP</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPersonTrackingRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_rekognition.types.person_tracking_sort_by

        out["SortBy"] = (
            capo_rekognition.types.person_tracking_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPersonTrackingRequest:
    out: GetPersonTrackingRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SortBy") is not None:
        import capo_rekognition.types.person_tracking_sort_by

        out["sort_by"] = (
            capo_rekognition.types.person_tracking_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    return out
