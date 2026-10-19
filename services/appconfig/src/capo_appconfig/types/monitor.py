"""Generated from Smithy shape ``com.amazonaws.appconfig#Monitor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.role_arn
    import capo_appconfig.types.string_with_length_between1_and2048


class Monitor(TypedDict, closed=True):
    alarm_arn: "capo_appconfig.types.string_with_length_between1_and2048.StringWithLengthBetween1And2048"
    """<p>Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.</p>"""
    alarm_role_arn: NotRequired["capo_appconfig.types.role_arn.RoleArn"]
    """<p>ARN of an Identity and Access Management (IAM) role for AppConfig to monitor <code>AlarmArn</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Monitor) -> dict:
    out: dict = {}
    out["AlarmArn"] = value["alarm_arn"]
    if "alarm_role_arn" in value:
        out["AlarmRoleArn"] = value["alarm_role_arn"]
    return out


def deserialize_json(data: dict) -> Monitor:
    out: Monitor = {}  # type: ignore[typeddict-item]
    if data.get("AlarmArn") is not None:
        out["alarm_arn"] = data["AlarmArn"]
    else:
        out["alarm_arn"] = ""
    if data.get("AlarmRoleArn") is not None:
        out["alarm_role_arn"] = data["AlarmRoleArn"]
    return out
