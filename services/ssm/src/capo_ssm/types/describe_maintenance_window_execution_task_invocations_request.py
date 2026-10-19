"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowExecutionTaskInvocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_task_id
    import capo_ssm.types.maintenance_window_filter_list
    import capo_ssm.types.maintenance_window_max_results
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowExecutionTaskInvocationsRequest(TypedDict, closed=True):
    window_execution_id: (
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution the task is part of.</p>"""
    task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    """<p>The ID of the specific task in the maintenance window task that should be retrieved.</p>"""
    filters: NotRequired[
        "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
    ]
    """<p>Optional filters used to scope down the returned task invocations. The supported filter key is <code>STATUS</code> with the corresponding values <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, <code>CANCELLING</code>, and <code>CANCELLED</code>.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeMaintenanceWindowExecutionTaskInvocationsRequest,
) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    out["TaskId"] = value["task_id"]
    if "filters" in value:
        import capo_ssm.types.maintenance_window_filter_list

        out["Filters"] = (
            capo_ssm.types.maintenance_window_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeMaintenanceWindowExecutionTaskInvocationsRequest:
    out: DescribeMaintenanceWindowExecutionTaskInvocationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        out["window_execution_id"] = ""
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("Filters") is not None:
        import capo_ssm.types.maintenance_window_filter_list

        out["filters"] = (
            capo_ssm.types.maintenance_window_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
