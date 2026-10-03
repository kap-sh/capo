"""Generated from Smithy shape ``com.amazonaws.connect#GetTaskTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.snapshot_version
    import capo_connect.types.task_template_id


class GetTaskTemplateRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    task_template_id: "capo_connect.types.task_template_id.TaskTemplateId"
    """<p>A unique identifier for the task template.</p>"""
    snapshot_version: NotRequired["capo_connect.types.snapshot_version.SnapshotVersion"]
    """<p>The system generated version of a task template that is associated with a task, when the task is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaskTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTaskTemplateRequest:
    out: GetTaskTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
