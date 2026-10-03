"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#GetMigrationWorkflowTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_migrationhuborchestrator.types.string_map
    import capo_migrationhuborchestrator.types.template_input_list
    import capo_migrationhuborchestrator.types.template_status
    import capo_migrationhuborchestrator.types.tools_list


class GetMigrationWorkflowTemplateResponse(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    template_arn: NotRequired["str"]
    """<p>&gt;The Amazon Resource Name (ARN) of the migration workflow template. The format for an Migration Hub Orchestrator template ARN is <code>arn:aws:migrationhub-orchestrator:region:account:template/template-abcd1234</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    name: NotRequired["str"]
    """<p>The name of the template.</p>"""
    description: NotRequired["str"]
    """<p>The time at which the template was last created.</p>"""
    inputs: NotRequired[
        "capo_migrationhuborchestrator.types.template_input_list.TemplateInputList"
    ]
    """<p>The inputs provided for the creation of the migration workflow.</p>"""
    tools: NotRequired["capo_migrationhuborchestrator.types.tools_list.ToolsList"]
    """<p>List of AWS services utilized in a migration workflow.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time at which the template was last created.</p>"""
    owner: NotRequired["str"]
    """<p>The owner of the migration workflow template.</p>"""
    status: NotRequired[
        "capo_migrationhuborchestrator.types.template_status.TemplateStatus"
    ]
    """<p>The status of the template.</p>"""
    status_message: NotRequired["str"]
    """<p>The status message of retrieving migration workflow templates.</p>"""
    template_class: NotRequired["str"]
    """<p>The class of the migration workflow template. The available template classes are:</p> <ul> <li> <p>A2C</p> </li> <li> <p>MGN</p> </li> <li> <p>SAP_MULTI</p> </li> <li> <p>SQL_EC2</p> </li> <li> <p>SQL_RDS</p> </li> <li> <p>VMIE</p> </li> </ul>"""
    tags: NotRequired["capo_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags added to the migration workflow template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMigrationWorkflowTemplateResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "inputs" in value:
        import capo_migrationhuborchestrator.types.template_input_list

        out["inputs"] = (
            capo_migrationhuborchestrator.types.template_input_list.serialize_json(
                value["inputs"]
            )
        )
    if "tools" in value:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.serialize_json(
            value["tools"]
        )
    if "creation_time" in value:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creationTime"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "template_class" in value:
        out["templateClass"] = value["template_class"]
    if "tags" in value:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetMigrationWorkflowTemplateResponse:
    out: GetMigrationWorkflowTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inputs") is not None:
        import capo_migrationhuborchestrator.types.template_input_list

        out["inputs"] = (
            capo_migrationhuborchestrator.types.template_input_list.deserialize_json(
                data["inputs"]
            )
        )
    if data.get("tools") is not None:
        import capo_migrationhuborchestrator.types.tools_list

        out["tools"] = capo_migrationhuborchestrator.types.tools_list.deserialize_json(
            data["tools"]
        )
    if data.get("creationTime") is not None:
        import capo_migrationhuborchestrator.types._prelude.timestamp

        out["creation_time"] = (
            capo_migrationhuborchestrator.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("templateClass") is not None:
        out["template_class"] = data["templateClass"]
    if data.get("tags") is not None:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.deserialize_json(
            data["tags"]
        )
    return out
