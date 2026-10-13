"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowTasksResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowTasksResult(TypedDict, closed=True):
    tasks: NotRequired[
        "capo_ssm.types.maintenance_window_task_list.MaintenanceWindowTaskList"
    ]
    """<p>Information about the tasks in the maintenance window.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowTasksResult) -> dict:
    out: dict = {}
    if "tasks" in value:
        import capo_ssm.types.maintenance_window_task_list

        out["Tasks"] = (
            capo_ssm.types.maintenance_window_task_list.serialize_aws_json_1_1(
                value["tasks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowTasksResult:
    out: DescribeMaintenanceWindowTasksResult = {}  # type: ignore[typeddict-item]
    if data.get("Tasks") is not None:
        import capo_ssm.types.maintenance_window_task_list

        out["tasks"] = (
            capo_ssm.types.maintenance_window_task_list.deserialize_aws_json_1_1(
                data["Tasks"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeMaintenanceWindowTasksResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tasks" in value:
        import capo_ssm.types.maintenance_window_task_list

        out["tasks"] = capo_ssm.types.maintenance_window_task_list.redact_sensitive(
            value["tasks"]
        )
    return out
