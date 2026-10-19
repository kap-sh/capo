"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Trigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.trigger_condition_list
    import capo_arc_region_switch.types.workflow_target_action


class Trigger(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>The description for a trigger.</p>"""
    target_region: "capo_arc_region_switch.types.region.Region"
    """<p>The Amazon Web Services Region for a trigger.</p>"""
    action: "capo_arc_region_switch.types.workflow_target_action.WorkflowTargetAction"
    """<p>The action to perform when the trigger fires. Valid values include <code>activate</code> and <code>deactivate</code>.</p>"""
    conditions: (
        "capo_arc_region_switch.types.trigger_condition_list.TriggerConditionList"
    )
    """<p>The conditions that must be met for the trigger to fire.</p>"""
    min_delay_minutes_between_executions: "int"
    """<p>The minimum time, in minutes, that must elapse between automatic executions of the plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Trigger) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["targetRegion"] = value["target_region"]
    import capo_arc_region_switch.types.workflow_target_action

    out["action"] = (
        capo_arc_region_switch.types.workflow_target_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    import capo_arc_region_switch.types.trigger_condition_list

    out["conditions"] = (
        capo_arc_region_switch.types.trigger_condition_list.serialize_aws_json_1_0(
            value["conditions"]
        )
    )
    out["minDelayMinutesBetweenExecutions"] = value[
        "min_delay_minutes_between_executions"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> Trigger:
    out: Trigger = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("targetRegion") is not None:
        out["target_region"] = data["targetRegion"]
    else:
        out["target_region"] = ""
    if data.get("action") is not None:
        import capo_arc_region_switch.types.workflow_target_action

        out["action"] = (
            capo_arc_region_switch.types.workflow_target_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_arc_region_switch.types.workflow_target_action.WorkflowTargetAction",
            "",
        )
    if data.get("conditions") is not None:
        import capo_arc_region_switch.types.trigger_condition_list

        out["conditions"] = (
            capo_arc_region_switch.types.trigger_condition_list.deserialize_aws_json_1_0(
                data["conditions"]
            )
        )
    else:
        out["conditions"] = []
    if data.get("minDelayMinutesBetweenExecutions") is not None:
        out["min_delay_minutes_between_executions"] = data[
            "minDelayMinutesBetweenExecutions"
        ]
    else:
        out["min_delay_minutes_between_executions"] = 0
    return out
