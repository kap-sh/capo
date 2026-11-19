"""Generated from Smithy shape ``com.amazonaws.datasync#CreateTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.task_arn


class CreateTaskResponse(TypedDict, closed=True):
    task_arn: NotRequired["capo_datasync.types.task_arn.TaskArn"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTaskResponse) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTaskResponse:
    out: CreateTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateTaskResponse) -> dict:
    out: dict = {}
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateTaskResponse:
    out: CreateTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    return out
