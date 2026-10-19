"""Generated from Smithy shape ``com.amazonaws.drs#RetryRecoveryPlanExecutionStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class RetryRecoveryPlanExecutionStepRequest(TypedDict, closed=True):
    recovery_plan_execution_step_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the execution step to retry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryRecoveryPlanExecutionStepRequest) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionStepArn"] = value["recovery_plan_execution_step_arn"]
    return out


def deserialize_json(data: dict) -> RetryRecoveryPlanExecutionStepRequest:
    out: RetryRecoveryPlanExecutionStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionStepArn") is not None:
        out["recovery_plan_execution_step_arn"] = data["recoveryPlanExecutionStepArn"]
    else:
        out["recovery_plan_execution_step_arn"] = ""
    return out
