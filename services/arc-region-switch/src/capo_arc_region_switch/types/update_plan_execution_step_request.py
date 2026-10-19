"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.update_plan_execution_step_action


class UpdatePlanExecutionStepRequest(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan containing the execution step to update.</p>"""
    execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The unique identifier of the plan execution containing the step to update.</p>"""
    comment: "capo_arc_region_switch.types.execution_comment.ExecutionComment"
    """<p>An optional comment about the plan execution.</p>"""
    step_name: "str"
    """<p>The name of the execution step to update.</p>"""
    action_to_take: "capo_arc_region_switch.types.update_plan_execution_step_action.UpdatePlanExecutionStepAction"
    """<p>The updated action to take for the step. This can be used to skip or retry a step.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionStepRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    out["comment"] = value["comment"]
    out["stepName"] = value["step_name"]
    import capo_arc_region_switch.types.update_plan_execution_step_action

    out["actionToTake"] = (
        capo_arc_region_switch.types.update_plan_execution_step_action.serialize_aws_json_1_0(
            value["action_to_take"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanExecutionStepRequest:
    out: UpdatePlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        out["plan_arn"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    else:
        out["comment"] = ""
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    else:
        out["step_name"] = ""
    if data.get("actionToTake") is not None:
        import capo_arc_region_switch.types.update_plan_execution_step_action

        out["action_to_take"] = (
            capo_arc_region_switch.types.update_plan_execution_step_action.deserialize_aws_json_1_0(
                data["actionToTake"]
            )
        )
    else:
        import typing

        out["action_to_take"] = typing.cast(
            "capo_arc_region_switch.types.update_plan_execution_step_action.UpdatePlanExecutionStepAction",
            "",
        )
    return out
