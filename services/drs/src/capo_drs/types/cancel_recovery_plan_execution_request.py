"""Generated from Smithy shape ``com.amazonaws.drs#CancelRecoveryPlanExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class CancelRecoveryPlanExecutionRequest(TypedDict, closed=True):
    recovery_plan_execution_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan execution to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelRecoveryPlanExecutionRequest) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionArn"] = value["recovery_plan_execution_arn"]
    return out


def deserialize_json(data: dict) -> CancelRecoveryPlanExecutionRequest:
    out: CancelRecoveryPlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionArn") is not None:
        out["recovery_plan_execution_arn"] = data["recoveryPlanExecutionArn"]
    else:
        out["recovery_plan_execution_arn"] = ""
    return out
