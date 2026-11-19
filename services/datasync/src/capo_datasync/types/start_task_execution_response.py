"""Generated from Smithy shape ``com.amazonaws.datasync#StartTaskExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.task_execution_arn


class StartTaskExecutionResponse(TypedDict, closed=True):
    task_execution_arn: NotRequired[
        "capo_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The ARN of the running task execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTaskExecutionResponse) -> dict:
    out: dict = {}
    if "task_execution_arn" in value:
        out["TaskExecutionArn"] = value["task_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTaskExecutionResponse:
    out: StartTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutionArn") is not None:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartTaskExecutionResponse) -> dict:
    out: dict = {}
    if "task_execution_arn" in value:
        out["TaskExecutionArn"] = value["task_execution_arn"]
    return out


def deserialize_cbor(data: dict) -> StartTaskExecutionResponse:
    out: StartTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutionArn") is not None:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    return out
