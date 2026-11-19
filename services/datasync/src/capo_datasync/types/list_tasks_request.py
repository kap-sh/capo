"""Generated from Smithy shape ``com.amazonaws.datasync#ListTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.max_results
    import capo_datasync.types.next_token
    import capo_datasync.types.task_filters


class ListTasksRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_datasync.types.max_results.MaxResults"]
    """<p>The maximum number of tasks to return.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>An opaque string that indicates the position at which to begin the next list of tasks.</p>"""
    filters: NotRequired["capo_datasync.types.task_filters.TaskFilters"]
    """<p>You can use API filters to narrow down the list of resources returned by <code>ListTasks</code>. For example, to retrieve all tasks on a specific source location, you can use <code>ListTasks</code> with filter name <code>LocationId</code> and <code>Operator Equals</code> with the ARN for the location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTasksRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_datasync.types.task_filters

        out["Filters"] = capo_datasync.types.task_filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTasksRequest:
    out: ListTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_datasync.types.task_filters

        out["filters"] = capo_datasync.types.task_filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTasksRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_datasync.types.task_filters

        out["Filters"] = capo_datasync.types.task_filters.serialize_cbor(
            value["filters"]
        )
    return out


def deserialize_cbor(data: dict) -> ListTasksRequest:
    out: ListTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_datasync.types.task_filters

        out["filters"] = capo_datasync.types.task_filters.deserialize_cbor(
            data["Filters"]
        )
    return out
