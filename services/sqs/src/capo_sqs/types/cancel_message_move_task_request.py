"""Generated from Smithy shape ``com.amazonaws.sqs#CancelMessageMoveTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.string


class CancelMessageMoveTaskRequest(TypedDict, closed=True):
    task_handle: "capo_sqs.types.string.String"
    """<p>An identifier associated with a message movement task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelMessageMoveTaskRequest) -> dict:
    out: dict = {}
    out["TaskHandle"] = value["task_handle"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelMessageMoveTaskRequest:
    out: CancelMessageMoveTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("TaskHandle") is not None:
        out["task_handle"] = data["TaskHandle"]
    else:
        out["task_handle"] = ""
    return out
