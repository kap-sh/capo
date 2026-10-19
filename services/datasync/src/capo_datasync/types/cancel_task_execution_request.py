"""Generated from Smithy shape ``com.amazonaws.datasync#CancelTaskExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.task_execution_arn


class CancelTaskExecutionRequest(TypedDict, closed=True):
    task_execution_arn: "capo_datasync.types.task_execution_arn.TaskExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the task execution to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelTaskExecutionRequest) -> dict:
    out: dict = {}
    out["TaskExecutionArn"] = value["task_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelTaskExecutionRequest:
    out: CancelTaskExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutionArn") is not None:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    else:
        out["task_execution_arn"] = ""
    return out
