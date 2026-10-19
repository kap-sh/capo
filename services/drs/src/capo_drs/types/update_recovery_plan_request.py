"""Generated from Smithy shape ``com.amazonaws.drs#UpdateRecoveryPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_plan_description
    import capo_drs.types.recovery_plan_name
    import capo_drs.types.strict_drsarn


class UpdateRecoveryPlanRequest(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan to update.</p>"""
    name: NotRequired["capo_drs.types.recovery_plan_name.RecoveryPlanName"]
    description: NotRequired[
        "capo_drs.types.recovery_plan_description.RecoveryPlanDescription"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPlanRequest) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPlanRequest:
    out: UpdateRecoveryPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
