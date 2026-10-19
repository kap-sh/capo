"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateWorkflowStepGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.step_group_description
    import capo_migrationhuborchestrator.types.step_group_name
    import capo_migrationhuborchestrator.types.string_list


class CreateWorkflowStepGroupRequest(TypedDict, closed=True):
    workflow_id: (
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    )
    """<p>The ID of the migration workflow that will contain the step group.</p>"""
    name: "capo_migrationhuborchestrator.types.step_group_name.StepGroupName"
    """<p>The name of the step group.</p>"""
    description: NotRequired[
        "capo_migrationhuborchestrator.types.step_group_description.StepGroupDescription"
    ]
    """<p>The description of the step group.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkflowStepGroupRequest) -> dict:
    out: dict = {}
    out["workflowId"] = value["workflow_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateWorkflowStepGroupRequest:
    out: CreateWorkflowStepGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("next") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    if data.get("previous") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    return out
