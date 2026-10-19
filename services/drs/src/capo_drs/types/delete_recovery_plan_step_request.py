"""Generated from Smithy shape ``com.amazonaws.drs#DeleteRecoveryPlanStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class DeleteRecoveryPlanStepRequest(TypedDict, closed=True):
    recovery_plan_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan step to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryPlanStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanStepArn"] = value["recovery_plan_step_arn"]
    return out


def deserialize_json(data: dict) -> DeleteRecoveryPlanStepRequest:
    out: DeleteRecoveryPlanStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanStepArn") is not None:
        out["recovery_plan_step_arn"] = data["recoveryPlanStepArn"]
    else:
        out["recovery_plan_step_arn"] = ""
    return out
