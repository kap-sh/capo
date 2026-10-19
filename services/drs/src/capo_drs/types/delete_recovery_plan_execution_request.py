"""Generated from Smithy shape ``com.amazonaws.drs#DeleteRecoveryPlanExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class DeleteRecoveryPlanExecutionRequest(TypedDict, closed=True):
    recovery_plan_execution_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan execution to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryPlanExecutionRequest) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionArn"] = value["recovery_plan_execution_arn"]
    return out


def deserialize_json(data: dict) -> DeleteRecoveryPlanExecutionRequest:
    out: DeleteRecoveryPlanExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionArn") is not None:
        out["recovery_plan_execution_arn"] = data["recoveryPlanExecutionArn"]
    else:
        out["recovery_plan_execution_arn"] = ""
    return out
