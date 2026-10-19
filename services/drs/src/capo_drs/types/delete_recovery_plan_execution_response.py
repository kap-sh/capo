"""Generated from Smithy shape ``com.amazonaws.drs#DeleteRecoveryPlanExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class DeleteRecoveryPlanExecutionResponse(TypedDict, closed=True):
    recovery_plan_execution_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the deleted Recovery Plan execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryPlanExecutionResponse) -> dict:
    out: dict = {}
    out["recoveryPlanExecutionArn"] = value["recovery_plan_execution_arn"]
    return out


def deserialize_json(data: dict) -> DeleteRecoveryPlanExecutionResponse:
    out: DeleteRecoveryPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanExecutionArn") is not None:
        out["recovery_plan_execution_arn"] = data["recoveryPlanExecutionArn"]
    else:
        out["recovery_plan_execution_arn"] = ""
    return out
