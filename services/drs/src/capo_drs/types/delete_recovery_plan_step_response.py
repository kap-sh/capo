"""Generated from Smithy shape ``com.amazonaws.drs#DeleteRecoveryPlanStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class DeleteRecoveryPlanStepResponse(TypedDict, closed=True):
    recovery_plan_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the deleted Recovery Plan step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryPlanStepResponse) -> dict:
    out: dict = {}
    out["recoveryPlanStepArn"] = value["recovery_plan_step_arn"]
    return out


def deserialize_json(data: dict) -> DeleteRecoveryPlanStepResponse:
    out: DeleteRecoveryPlanStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanStepArn") is not None:
        out["recovery_plan_step_arn"] = data["recoveryPlanStepArn"]
    else:
        out["recovery_plan_step_arn"] = ""
    return out
