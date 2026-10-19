"""Generated from Smithy shape ``com.amazonaws.drs#ReorderRecoveryPlanStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_step_arn_list
    import capo_drs.types.strict_drsarn


class ReorderRecoveryPlanStepsRequest(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan.</p>"""
    ordered_step_arns: (
        "capo_drs.types.recovery_plan_step_arn_list.RecoveryPlanStepArnList"
    )
    """<p>Ordered list of all step ARNs representing the desired sequence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReorderRecoveryPlanStepsRequest) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    import capo_drs.types.recovery_plan_step_arn_list

    out["orderedStepArns"] = capo_drs.types.recovery_plan_step_arn_list.serialize_json(
        value["ordered_step_arns"]
    )
    return out


def deserialize_json(data: dict) -> ReorderRecoveryPlanStepsRequest:
    out: ReorderRecoveryPlanStepsRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    if data.get("orderedStepArns") is not None:
        import capo_drs.types.recovery_plan_step_arn_list

        out["ordered_step_arns"] = (
            capo_drs.types.recovery_plan_step_arn_list.deserialize_json(
                data["orderedStepArns"]
            )
        )
    else:
        out["ordered_step_arns"] = []
    return out
