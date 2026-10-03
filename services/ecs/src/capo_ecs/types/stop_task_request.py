"""Generated from Smithy shape ``com.amazonaws.ecs#StopTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.string


class StopTaskRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.</p>"""
    task: "capo_ecs.types.string.String"
    """<p>Thefull Amazon Resource Name (ARN) of the task.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>An optional message specified when a task is stopped. For example, if you're using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html">DescribeTasks</a>&gt; API operations on this task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTaskRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["task"] = value["task"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTaskRequest:
    out: StopTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("task") is not None:
        out["task"] = data["task"]
    else:
        raise DeserializationError("StopTaskRequest.task required")
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
