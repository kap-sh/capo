"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTaskRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.page_size
    import capo_glue.types.pagination_token
    import capo_glue.types.task_run_filter_criteria
    import capo_glue.types.task_run_sort_criteria


class GetMLTaskRunsRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A token for pagination of the results. The default is empty.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of results to return. </p>"""
    filter: NotRequired[
        "capo_glue.types.task_run_filter_criteria.TaskRunFilterCriteria"
    ]
    """<p>The filter criteria, in the <code>TaskRunFilterCriteria</code> structure, for the task run.</p>"""
    sort: NotRequired["capo_glue.types.task_run_sort_criteria.TaskRunSortCriteria"]
    """<p>The sorting criteria, in the <code>TaskRunSortCriteria</code> structure, for the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTaskRunsRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import capo_glue.types.task_run_filter_criteria

        out["Filter"] = capo_glue.types.task_run_filter_criteria.serialize_aws_json_1_1(
            value["filter"]
        )
    if "sort" in value:
        import capo_glue.types.task_run_sort_criteria

        out["Sort"] = capo_glue.types.task_run_sort_criteria.serialize_aws_json_1_1(
            value["sort"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTaskRunsRequest:
    out: GetMLTaskRunsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransformId") is not None:
        out["transform_id"] = data["TransformId"]
    else:
        out["transform_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filter") is not None:
        import capo_glue.types.task_run_filter_criteria

        out["filter"] = (
            capo_glue.types.task_run_filter_criteria.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("Sort") is not None:
        import capo_glue.types.task_run_sort_criteria

        out["sort"] = capo_glue.types.task_run_sort_criteria.deserialize_aws_json_1_1(
            data["Sort"]
        )
    return out
