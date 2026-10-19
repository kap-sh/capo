"""Generated from Smithy shape ``com.amazonaws.drs#GetRecoveryPlanStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class GetRecoveryPlanStepRequest(TypedDict, closed=True):
    recovery_plan_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan step to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPlanStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanStepArn"] = value["recovery_plan_step_arn"]
    return out


def deserialize_json(data: dict) -> GetRecoveryPlanStepRequest:
    out: GetRecoveryPlanStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanStepArn") is not None:
        out["recovery_plan_step_arn"] = data["recoveryPlanStepArn"]
    else:
        out["recovery_plan_step_arn"] = ""
    return out
