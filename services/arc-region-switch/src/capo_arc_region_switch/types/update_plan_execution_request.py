"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.update_plan_execution_action


class UpdatePlanExecutionRequest(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan with the execution to update.</p>"""
    execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    action: "capo_arc_region_switch.types.update_plan_execution_action.UpdatePlanExecutionAction"
    """<p>The action specified for a plan execution, for example, Switch to Graceful or Pause.</p>"""
    comment: NotRequired[
        "capo_arc_region_switch.types.execution_comment.ExecutionComment"
    ]
    """<p>An optional comment about the plan execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanExecutionRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    import capo_arc_region_switch.types.update_plan_execution_action

    out["action"] = (
        capo_arc_region_switch.types.update_plan_execution_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanExecutionRequest:
    out: UpdatePlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        out["plan_arn"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("action") is not None:
        import capo_arc_region_switch.types.update_plan_execution_action

        out["action"] = (
            capo_arc_region_switch.types.update_plan_execution_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_arc_region_switch.types.update_plan_execution_action.UpdatePlanExecutionAction",
            "",
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
