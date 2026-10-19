"""Generated from Smithy shape ``com.amazonaws.drs#DeleteRecoveryPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class DeleteRecoveryPlanRequest(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryPlanRequest) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    return out


def deserialize_json(data: dict) -> DeleteRecoveryPlanRequest:
    out: DeleteRecoveryPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    return out
