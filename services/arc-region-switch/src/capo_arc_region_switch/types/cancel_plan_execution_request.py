"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#CancelPlanExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.plan_arn


class CancelPlanExecutionRequest(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    comment: NotRequired[
        "capo_arc_region_switch.types.execution_comment.ExecutionComment"
    ]
    """<p>A comment that you can enter about canceling a plan execution step.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelPlanExecutionRequest) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelPlanExecutionRequest:
    out: CancelPlanExecutionRequest = {}  # type: ignore[typeddict-item]
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
    return out
