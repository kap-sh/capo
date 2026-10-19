"""Generated from Smithy shape ``com.amazonaws.iot#CloudwatchAlarmAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.alarm_name
    import capo_iot.types.aws_arn
    import capo_iot.types.state_reason
    import capo_iot.types.state_value


class CloudwatchAlarmAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The IAM role that allows access to the CloudWatch alarm.</p>"""
    alarm_name: "capo_iot.types.alarm_name.AlarmName"
    """<p>The CloudWatch alarm name.</p>"""
    state_reason: "capo_iot.types.state_reason.StateReason"
    """<p>The reason for the alarm change.</p>"""
    state_value: "capo_iot.types.state_value.StateValue"
    """<p>The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudwatchAlarmAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["alarmName"] = value["alarm_name"]
    out["stateReason"] = value["state_reason"]
    out["stateValue"] = value["state_value"]
    return out


def deserialize_json(data: dict) -> CloudwatchAlarmAction:
    out: CloudwatchAlarmAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("alarmName") is not None:
        out["alarm_name"] = data["alarmName"]
    else:
        out["alarm_name"] = ""
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        out["state_reason"] = ""
    if data.get("stateValue") is not None:
        out["state_value"] = data["stateValue"]
    else:
        out["state_value"] = ""
    return out
