"""Generated from Smithy shape ``com.amazonaws.iot#AlertTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.alert_target_arn
    import capo_iot.types.role_arn


class AlertTarget(TypedDict, closed=True):
    alert_target_arn: "capo_iot.types.alert_target_arn.AlertTargetArn"
    """<p>The Amazon Resource Name (ARN) of the notification target to which alerts are sent.</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>The ARN of the role that grants permission to send alerts to the notification target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlertTarget) -> dict:
    out: dict = {}
    out["alertTargetArn"] = value["alert_target_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AlertTarget:
    out: AlertTarget = {}  # type: ignore[typeddict-item]
    if data.get("alertTargetArn") is not None:
        out["alert_target_arn"] = data["alertTargetArn"]
    else:
        out["alert_target_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
