"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_plan_name
    import capo_drs.types.recovery_plan_status
    import capo_drs.types.strict_drsarn


class RecoveryPlanSummary(TypedDict, closed=True):
    recovery_plan_arn: "capo_drs.types.strict_drsarn.StrictDRSARN"
    """<p>The ARN of the Recovery Plan.</p>"""
    name: "capo_drs.types.recovery_plan_name.RecoveryPlanName"
    status: "capo_drs.types.recovery_plan_status.RecoveryPlanStatus"
    """<p>The status of the Recovery Plan.</p>"""
    created_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the Recovery Plan was created.</p>"""
    updated_at: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp when the Recovery Plan was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanSummary) -> dict:
    out: dict = {}
    out["recoveryPlanArn"] = value["recovery_plan_arn"]
    out["name"] = value["name"]
    out["status"] = value["status"]
    out["createdAt"] = value["created_at"]
    out["updatedAt"] = value["updated_at"]
    return out


def deserialize_json(data: dict) -> RecoveryPlanSummary:
    out: RecoveryPlanSummary = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlanArn") is not None:
        out["recovery_plan_arn"] = data["recoveryPlanArn"]
    else:
        out["recovery_plan_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("createdAt") is not None:
        out["created_at"] = data["createdAt"]
    else:
        out["created_at"] = ""
    if data.get("updatedAt") is not None:
        out["updated_at"] = data["updatedAt"]
    else:
        out["updated_at"] = ""
    return out
