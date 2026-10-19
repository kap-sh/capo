"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CreateBatchLoadTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.batch_load_task_id


class CreateBatchLoadTaskResponse(TypedDict, closed=True):
    task_id: "capo_timestream_write.types.batch_load_task_id.BatchLoadTaskId"
    """<p>The ID of the batch load task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBatchLoadTaskResponse) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBatchLoadTaskResponse:
    out: CreateBatchLoadTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    return out
