"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactTaskTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.task_template_id


class UpdateContactTaskTemplateRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    task_template_id: "capo_connect.types.task_template_id.TaskTemplateId"
    """<p>A unique identifier for the task template. For more information about task templates, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/task-templates.html">Task templates</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactTaskTemplateRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["TaskTemplateId"] = value["task_template_id"]
    out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> UpdateContactTaskTemplateRequest:
    out: UpdateContactTaskTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateContactTaskTemplateRequest.instance_id required"
        )
    if data.get("TaskTemplateId") is not None:
        out["task_template_id"] = data["TaskTemplateId"]
    else:
        raise DeserializationError(
            "UpdateContactTaskTemplateRequest.task_template_id required"
        )
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError(
            "UpdateContactTaskTemplateRequest.contact_id required"
        )
    return out
