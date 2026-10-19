"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ResumeBatchLoadTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.batch_load_task_id


class ResumeBatchLoadTaskRequest(TypedDict, closed=True):
    task_id: "capo_timestream_write.types.batch_load_task_id.BatchLoadTaskId"
    """<p>The ID of the batch load task to resume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResumeBatchLoadTaskRequest) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResumeBatchLoadTaskRequest:
    out: ResumeBatchLoadTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    return out
