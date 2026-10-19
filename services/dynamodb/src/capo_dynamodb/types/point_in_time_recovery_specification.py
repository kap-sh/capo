"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoverySpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.boolean_object
    import capo_dynamodb.types.recovery_period_in_days


class PointInTimeRecoverySpecification(TypedDict, closed=True):
    point_in_time_recovery_enabled: "capo_dynamodb.types.boolean_object.BooleanObject"
    """<p>Indicates whether point in time recovery is enabled (true) or disabled (false) on the table.</p>"""
    recovery_period_in_days: NotRequired[
        "capo_dynamodb.types.recovery_period_in_days.RecoveryPeriodInDays"
    ]
    """<p>The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional. If no value is provided, the value will default to 35.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoverySpecification) -> dict:
    out: dict = {}
    out["PointInTimeRecoveryEnabled"] = value["point_in_time_recovery_enabled"]
    if "recovery_period_in_days" in value:
        out["RecoveryPeriodInDays"] = value["recovery_period_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecoverySpecification:
    out: PointInTimeRecoverySpecification = {}  # type: ignore[typeddict-item]
    if data.get("PointInTimeRecoveryEnabled") is not None:
        out["point_in_time_recovery_enabled"] = data["PointInTimeRecoveryEnabled"]
    else:
        out["point_in_time_recovery_enabled"] = False
    if data.get("RecoveryPeriodInDays") is not None:
        out["recovery_period_in_days"] = data["RecoveryPeriodInDays"]
    return out
