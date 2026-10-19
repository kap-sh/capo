"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Workflow``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.steps
    import capo_arc_region_switch.types.workflow_target_action


class Workflow(TypedDict, closed=True):
    steps: NotRequired["capo_arc_region_switch.types.steps.Steps"]
    """<p>The steps that make up the workflow.</p>"""
    workflow_target_action: (
        "capo_arc_region_switch.types.workflow_target_action.WorkflowTargetAction"
    )
    """<p>The action that the workflow performs. Valid values include <code>activate</code> and <code>deactivate</code>.</p>"""
    workflow_target_region: NotRequired["capo_arc_region_switch.types.region.Region"]
    """<p>The Amazon Web Services Region that the workflow targets.</p>"""
    workflow_description: NotRequired["str"]
    """<p>The description of the workflow.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Workflow) -> dict:
    out: dict = {}
    if "steps" in value:
        import capo_arc_region_switch.types.steps

        out["steps"] = capo_arc_region_switch.types.steps.serialize_aws_json_1_0(
            value["steps"]
        )
    import capo_arc_region_switch.types.workflow_target_action

    out["workflowTargetAction"] = (
        capo_arc_region_switch.types.workflow_target_action.serialize_aws_json_1_0(
            value["workflow_target_action"]
        )
    )
    if "workflow_target_region" in value:
        out["workflowTargetRegion"] = value["workflow_target_region"]
    if "workflow_description" in value:
        out["workflowDescription"] = value["workflow_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Workflow:
    out: Workflow = {}  # type: ignore[typeddict-item]
    if data.get("steps") is not None:
        import capo_arc_region_switch.types.steps

        out["steps"] = capo_arc_region_switch.types.steps.deserialize_aws_json_1_0(
            data["steps"]
        )
    if data.get("workflowTargetAction") is not None:
        import capo_arc_region_switch.types.workflow_target_action

        out["workflow_target_action"] = (
            capo_arc_region_switch.types.workflow_target_action.deserialize_aws_json_1_0(
                data["workflowTargetAction"]
            )
        )
    else:
        import typing

        out["workflow_target_action"] = typing.cast(
            "capo_arc_region_switch.types.workflow_target_action.WorkflowTargetAction",
            "",
        )
    if data.get("workflowTargetRegion") is not None:
        out["workflow_target_region"] = data["workflowTargetRegion"]
    if data.get("workflowDescription") is not None:
        out["workflow_description"] = data["workflowDescription"]
    return out


def redact_sensitive(value: Workflow) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "steps" in value:
        import capo_arc_region_switch.types.steps

        out["steps"] = capo_arc_region_switch.types.steps.redact_sensitive(
            value["steps"]
        )
    return out
