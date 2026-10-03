"""Generated from Smithy shape ``com.amazonaws.datasync#TaskListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.tag_value
    import capo_datasync.types.task_arn
    import capo_datasync.types.task_mode
    import capo_datasync.types.task_status


class TaskListEntry(TypedDict, closed=True):
    task_arn: NotRequired["capo_datasync.types.task_arn.TaskArn"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
    status: NotRequired["capo_datasync.types.task_status.TaskStatus"]
    """<p>The status of the task.</p>"""
    name: NotRequired["capo_datasync.types.tag_value.TagValue"]
    """<p>The name of the task.</p>"""
    task_mode: NotRequired["capo_datasync.types.task_mode.TaskMode"]
    """<p>The task mode that you're using. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Choosing a task mode for your data transfer</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskListEntry) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "status" in value:
        import capo_datasync.types.task_status

        out["Status"] = capo_datasync.types.task_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "task_mode" in value:
        import capo_datasync.types.task_mode

        out["TaskMode"] = capo_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskListEntry:
    out: TaskListEntry = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("Status") is not None:
        import capo_datasync.types.task_status

        out["status"] = capo_datasync.types.task_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TaskMode") is not None:
        import capo_datasync.types.task_mode

        out["task_mode"] = capo_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    return out
