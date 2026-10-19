"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ApprovePlanExecutionStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.approval
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.step_name


class ApprovePlanExecutionStepRequest(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    step_name: "capo_arc_region_switch.types.step_name.StepName"
    """<p>The name of a step in a plan execution.</p>"""
    approval: "capo_arc_region_switch.types.approval.Approval"
    """<p>The status of approval for a plan execution step. </p>"""
    comment: NotRequired[
        "capo_arc_region_switch.types.execution_comment.ExecutionComment"
    ]
    """<p>A comment that you can enter about a plan execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApprovePlanExecutionStepRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    out["stepName"] = value["step_name"]
    import capo_arc_region_switch.types.approval

    out["approval"] = capo_arc_region_switch.types.approval.serialize_aws_json_1_0(
        value["approval"]
    )
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ApprovePlanExecutionStepRequest:
    out: ApprovePlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        out["plan_arn"] = ""
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    else:
        out["step_name"] = ""
    if data.get("approval") is not None:
        import capo_arc_region_switch.types.approval

        out["approval"] = (
            capo_arc_region_switch.types.approval.deserialize_aws_json_1_0(
                data["approval"]
            )
        )
    else:
        import typing

        out["approval"] = typing.cast(
            "capo_arc_region_switch.types.approval.Approval", ""
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    return out
