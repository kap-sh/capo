"""Generated from Smithy shape ``com.amazonaws.connect#TaskActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_references
    import capo_connect.types.task_description_expression
    import capo_connect.types.task_name_expression


class TaskActionDefinition(TypedDict, closed=True):
    name: "capo_connect.types.task_name_expression.TaskNameExpression"
    """<p>The name. Supports variable injection. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    description: NotRequired[
        "capo_connect.types.task_description_expression.TaskDescriptionExpression"
    ]
    """<p>The description. Supports variable injection. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html">JSONPath reference</a> in the <i>Connect Customer Administrators Guide</i>.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""
    references: NotRequired["capo_connect.types.contact_references.ContactReferences"]
    """<p>Information about the reference when the <code>referenceType</code> is <code>URL</code>. Otherwise, null. (Supports variable injection in the <code>Value</code> field.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskActionDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["ContactFlowId"] = value["contact_flow_id"]
    if "references" in value:
        import capo_connect.types.contact_references

        out["References"] = capo_connect.types.contact_references.serialize_json(
            value["references"]
        )
    return out


def deserialize_json(data: dict) -> TaskActionDefinition:
    out: TaskActionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TaskActionDefinition.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("TaskActionDefinition.contact_flow_id required")
    if data.get("References") is not None:
        import capo_connect.types.contact_references

        out["references"] = capo_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    return out
