"""Generated from Smithy shape ``com.amazonaws.drs#DeleteRecoveryPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn


class DeleteRecoveryPlanResponse(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the deleted Recovery Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecoveryPlanResponse) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    return out


def deserialize_json(data: dict) -> DeleteRecoveryPlanResponse:
    out: DeleteRecoveryPlanResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    return out
