"""Generated from Smithy shape ``com.amazonaws.rekognition#GetContentModerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.content_moderation_aggregate_by
    import capo_rekognition.types.content_moderation_sort_by
    import capo_rekognition.types.job_id
    import capo_rekognition.types.max_results
    import capo_rekognition.types.pagination_token


class GetContentModerationRequest(TypedDict, closed=True):
    job_id: "capo_rekognition.types.job_id.JobId"
    """<p>The identifier for the inappropriate, unwanted, or offensive content moderation job. Use <code>JobId</code> to identify the job in a subsequent call to <code>GetContentModeration</code>.</p>"""
    max_results: NotRequired["capo_rekognition.types.max_results.MaxResults"]
    """<p>Maximum number of results to return per paginated call. The largest value you can specify is 1000. If you specify a value greater than 1000, a maximum of 1000 results is returned. The default value is 1000.</p>"""
    next_token: NotRequired["capo_rekognition.types.pagination_token.PaginationToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of content moderation labels.</p>"""
    sort_by: NotRequired[
        "capo_rekognition.types.content_moderation_sort_by.ContentModerationSortBy"
    ]
    """<p>Sort to use for elements in the <code>ModerationLabelDetections</code> array. Use <code>TIMESTAMP</code> to sort array elements by the time labels are detected. Use <code>NAME</code> to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by <code>TIMESTAMP</code>.</p>"""
    aggregate_by: NotRequired[
        "capo_rekognition.types.content_moderation_aggregate_by.ContentModerationAggregateBy"
    ]
    """<p>Defines how to aggregate results of the StartContentModeration request. Default aggregation option is TIMESTAMPS. SEGMENTS mode aggregates moderation labels over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContentModerationRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_rekognition.types.content_moderation_sort_by

        out["SortBy"] = (
            capo_rekognition.types.content_moderation_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "aggregate_by" in value:
        import capo_rekognition.types.content_moderation_aggregate_by

        out["AggregateBy"] = (
            capo_rekognition.types.content_moderation_aggregate_by.serialize_aws_json_1_1(
                value["aggregate_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContentModerationRequest:
    out: GetContentModerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SortBy") is not None:
        import capo_rekognition.types.content_moderation_sort_by

        out["sort_by"] = (
            capo_rekognition.types.content_moderation_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("AggregateBy") is not None:
        import capo_rekognition.types.content_moderation_aggregate_by

        out["aggregate_by"] = (
            capo_rekognition.types.content_moderation_aggregate_by.deserialize_aws_json_1_1(
                data["AggregateBy"]
            )
        )
    return out
