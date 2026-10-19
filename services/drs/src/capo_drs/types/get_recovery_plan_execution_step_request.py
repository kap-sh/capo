"""Generated from Smithy shape ``com.amazonaws.drs#GetRecoveryPlanExecutionStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class GetRecoveryPlanExecutionStepRequest(TypedDict, closed=True):
    recovery_plan_execution_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the execution step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPlanExecutionStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionStepArn"] = value["recovery_plan_execution_step_arn"]
    return out


def deserialize_json(data: dict) -> GetRecoveryPlanExecutionStepRequest:
    out: GetRecoveryPlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionStepArn") is not None:
        out["recovery_plan_execution_step_arn"] = data["recoveryPlanExecutionStepArn"]
    else:
        out["recovery_plan_execution_step_arn"] = ""
    return out
