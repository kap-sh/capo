"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateWorkflowStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.migration_workflow_id
    import capo_migrationhuborchestrator.types.step_action_type
    import capo_migrationhuborchestrator.types.step_description
    import capo_migrationhuborchestrator.types.step_group_id
    import capo_migrationhuborchestrator.types.step_id
    import capo_migrationhuborchestrator.types.step_name
    import capo_migrationhuborchestrator.types.step_status
    import capo_migrationhuborchestrator.types.string_list
    import capo_migrationhuborchestrator.types.workflow_step_automation_configuration
    import capo_migrationhuborchestrator.types.workflow_step_output_list


class UpdateWorkflowStepRequest(TypedDict, closed=True):
    id: "capo_migrationhuborchestrator.types.step_id.StepId"
    """<p>The ID of the step.</p>"""
    step_group_id: "capo_migrationhuborchestrator.types.step_group_id.StepGroupId"
    """<p>The ID of the step group.</p>"""
    workflow_id: (
        "capo_migrationhuborchestrator.types.migration_workflow_id.MigrationWorkflowId"
    )
    """<p>The ID of the migration workflow.</p>"""
    name: NotRequired["capo_migrationhuborchestrator.types.step_name.StepName"]
    """<p>The name of the step.</p>"""
    description: NotRequired[
        "capo_migrationhuborchestrator.types.step_description.StepDescription"
    ]
    """<p>The description of the step.</p>"""
    step_action_type: NotRequired[
        "capo_migrationhuborchestrator.types.step_action_type.StepActionType"
    ]
    """<p>The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.</p>"""
    workflow_step_automation_configuration: NotRequired[
        "capo_migrationhuborchestrator.types.workflow_step_automation_configuration.WorkflowStepAutomationConfiguration"
    ]
    """<p>The custom script to run tests on the source and target environments.</p>"""
    step_target: NotRequired[
        "capo_migrationhuborchestrator.types.string_list.StringList"
    ]
    """<p>The servers on which a step will be run.</p>"""
    outputs: NotRequired[
        "capo_migrationhuborchestrator.types.workflow_step_output_list.WorkflowStepOutputList"
    ]
    """<p>The outputs of a step.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step.</p>"""
    status: NotRequired["capo_migrationhuborchestrator.types.step_status.StepStatus"]
    """<p>The status of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkflowStepRequest) -> dict:
    out: dict = {}
    out["stepGroupId"] = value["step_group_id"]
    out["workflowId"] = value["workflow_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "step_action_type" in value:
        out["stepActionType"] = value["step_action_type"]
    if "workflow_step_automation_configuration" in value:
        import capo_migrationhuborchestrator.types.workflow_step_automation_configuration

        out["workflowStepAutomationConfiguration"] = (
            capo_migrationhuborchestrator.types.workflow_step_automation_configuration.serialize_json(
                value["workflow_step_automation_configuration"]
            )
        )
    if "step_target" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["stepTarget"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["step_target"]
            )
        )
    if "outputs" in value:
        import capo_migrationhuborchestrator.types.workflow_step_output_list

        out["outputs"] = (
            capo_migrationhuborchestrator.types.workflow_step_output_list.serialize_json(
                value["outputs"]
            )
        )
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> UpdateWorkflowStepRequest:
    out: UpdateWorkflowStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("stepGroupId") is not None:
        out["step_group_id"] = data["stepGroupId"]
    else:
        out["step_group_id"] = ""
    if data.get("workflowId") is not None:
        out["workflow_id"] = data["workflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("stepActionType") is not None:
        out["step_action_type"] = data["stepActionType"]
    if data.get("workflowStepAutomationConfiguration") is not None:
        import capo_migrationhuborchestrator.types.workflow_step_automation_configuration

        out["workflow_step_automation_configuration"] = (
            capo_migrationhuborchestrator.types.workflow_step_automation_configuration.deserialize_json(
                data["workflowStepAutomationConfiguration"]
            )
        )
    if data.get("stepTarget") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["step_target"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["stepTarget"]
            )
        )
    if data.get("outputs") is not None:
        import capo_migrationhuborchestrator.types.workflow_step_output_list

        out["outputs"] = (
            capo_migrationhuborchestrator.types.workflow_step_output_list.deserialize_json(
                data["outputs"]
            )
        )
    if data.get("previous") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if data.get("next") is not None:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
