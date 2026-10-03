"""Generated from Smithy shape ``com.amazonaws.connect#UpdateTaskTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.instance_id
    import capo_connect.types.task_template_arn
    import capo_connect.types.task_template_constraints
    import capo_connect.types.task_template_defaults
    import capo_connect.types.task_template_description
    import capo_connect.types.task_template_fields
    import capo_connect.types.task_template_id
    import capo_connect.types.task_template_name
    import capo_connect.types.task_template_status
    import capo_connect.types.timestamp


class UpdateTaskTemplateResponse(TypedDict, closed=True):
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    id: NotRequired["capo_connect.types.task_template_id.TaskTemplateId"]
    """<p>The identifier of the task template resource.</p>"""
    arn: NotRequired["capo_connect.types.task_template_arn.TaskTemplateArn"]
    """<p>The Amazon Resource Name (ARN) for the task template resource.</p>"""
    name: NotRequired["capo_connect.types.task_template_name.TaskTemplateName"]
    """<p>The name of the task template.</p>"""
    description: NotRequired[
        "capo_connect.types.task_template_description.TaskTemplateDescription"
    ]
    """<p>The description of the task template.</p>"""
    contact_flow_id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow that runs by default when a task is created by referencing this template.</p>"""
    self_assign_flow_id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.</p>"""
    constraints: NotRequired[
        "capo_connect.types.task_template_constraints.TaskTemplateConstraints"
    ]
    """<p>Constraints that are applicable to the fields listed. Although this parameter is marked as optional in the API model, the service requires it when calling <code>CreateTaskTemplate</code> or <code>UpdateTaskTemplate</code>. The <code>RequiredFields</code> array must contain at least one element, and the field of type <code>NAME</code> must be included in <code>RequiredFields</code>.</p>"""
    defaults: NotRequired[
        "capo_connect.types.task_template_defaults.TaskTemplateDefaults"
    ]
    """<p>The default values for fields when a task is created by referencing this template.</p>"""
    fields: NotRequired["capo_connect.types.task_template_fields.TaskTemplateFields"]
    """<p>Fields that are part of the template.</p>"""
    status: NotRequired["capo_connect.types.task_template_status.TaskTemplateStatus"]
    """<p>Marks a template as <code>ACTIVE</code> or <code>INACTIVE</code> for a task to refer to it. Tasks can only be created from <code>ACTIVE</code> templates. If a template is marked as <code>INACTIVE</code>, then a task that refers to this template cannot be created.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the task template was last modified.</p>"""
    created_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the task template was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTaskTemplateResponse) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "self_assign_flow_id" in value:
        out["SelfAssignFlowId"] = value["self_assign_flow_id"]
    if "constraints" in value:
        import capo_connect.types.task_template_constraints

        out["Constraints"] = (
            capo_connect.types.task_template_constraints.serialize_json(
                value["constraints"]
            )
        )
    if "defaults" in value:
        import capo_connect.types.task_template_defaults

        out["Defaults"] = capo_connect.types.task_template_defaults.serialize_json(
            value["defaults"]
        )
    if "fields" in value:
        import capo_connect.types.task_template_fields

        out["Fields"] = capo_connect.types.task_template_fields.serialize_json(
            value["fields"]
        )
    if "status" in value:
        import capo_connect.types.task_template_status

        out["Status"] = capo_connect.types.task_template_status.serialize_json(
            value["status"]
        )
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "created_time" in value:
        import capo_connect.types.timestamp

        out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTaskTemplateResponse:
    out: UpdateTaskTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    if data.get("SelfAssignFlowId") is not None:
        out["self_assign_flow_id"] = data["SelfAssignFlowId"]
    if data.get("Constraints") is not None:
        import capo_connect.types.task_template_constraints

        out["constraints"] = (
            capo_connect.types.task_template_constraints.deserialize_json(
                data["Constraints"]
            )
        )
    if data.get("Defaults") is not None:
        import capo_connect.types.task_template_defaults

        out["defaults"] = capo_connect.types.task_template_defaults.deserialize_json(
            data["Defaults"]
        )
    if data.get("Fields") is not None:
        import capo_connect.types.task_template_fields

        out["fields"] = capo_connect.types.task_template_fields.deserialize_json(
            data["Fields"]
        )
    if data.get("Status") is not None:
        import capo_connect.types.task_template_status

        out["status"] = capo_connect.types.task_template_status.deserialize_json(
            data["Status"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    return out
