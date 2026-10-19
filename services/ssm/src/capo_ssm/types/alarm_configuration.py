"""Generated from Smithy shape ``com.amazonaws.ssm#AlarmConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_list
    import capo_ssm.types.boolean


class AlarmConfiguration(TypedDict, closed=True):
    ignore_poll_alarm_failure: "capo_ssm.types.boolean.Boolean"
    """<p>When this value is <i>true</i>, your automation or command continues to run in cases where we can’t retrieve alarm status information from CloudWatch. In cases where we successfully retrieve an alarm status of OK or INSUFFICIENT_DATA, the automation or command continues to run, regardless of this value. Default is <i>false</i>.</p>"""
    alarms: "capo_ssm.types.alarm_list.AlarmList"
    """<p>The name of the CloudWatch alarm specified in the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmConfiguration) -> dict:
    out: dict = {}
    out["IgnorePollAlarmFailure"] = value.get("ignore_poll_alarm_failure", False)
    import capo_ssm.types.alarm_list

    out["Alarms"] = capo_ssm.types.alarm_list.serialize_aws_json_1_1(value["alarms"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AlarmConfiguration:
    out: AlarmConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IgnorePollAlarmFailure") is not None:
        out["ignore_poll_alarm_failure"] = data["IgnorePollAlarmFailure"]
    else:
        out["ignore_poll_alarm_failure"] = False
    if data.get("Alarms") is not None:
        import capo_ssm.types.alarm_list

        out["alarms"] = capo_ssm.types.alarm_list.deserialize_aws_json_1_1(
            data["Alarms"]
        )
    else:
        out["alarms"] = []
    return out
