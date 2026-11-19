"""Generated from Smithy shape ``com.amazonaws.codedeploy#AlarmConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.alarm_list
    import capo_codedeploy.types.boolean


class AlarmConfiguration(TypedDict, closed=True):
    enabled: "capo_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether the alarm configuration is enabled.</p>"""
    ignore_poll_alarm_failure: "capo_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch. The default value is false.</p> <ul> <li> <p> <code>true</code>: The deployment proceeds even if alarm status information can't be retrieved from Amazon CloudWatch.</p> </li> <li> <p> <code>false</code>: The deployment stops if alarm status information can't be retrieved from Amazon CloudWatch.</p> </li> </ul>"""
    alarms: NotRequired["capo_codedeploy.types.alarm_list.AlarmList"]
    """<p>A list of alarms configured for the deployment or deployment group. A maximum of 10 alarms can be added.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    out["ignorePollAlarmFailure"] = value.get("ignore_poll_alarm_failure", False)
    if "alarms" in value:
        import capo_codedeploy.types.alarm_list

        out["alarms"] = capo_codedeploy.types.alarm_list.serialize_aws_json_1_1(
            value["alarms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlarmConfiguration:
    out: AlarmConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("ignorePollAlarmFailure") is not None:
        out["ignore_poll_alarm_failure"] = data["ignorePollAlarmFailure"]
    else:
        out["ignore_poll_alarm_failure"] = False
    if data.get("alarms") is not None:
        import capo_codedeploy.types.alarm_list

        out["alarms"] = capo_codedeploy.types.alarm_list.deserialize_aws_json_1_1(
            data["alarms"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlarmConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    out["ignorePollAlarmFailure"] = value.get("ignore_poll_alarm_failure", False)
    if "alarms" in value:
        import capo_codedeploy.types.alarm_list

        out["alarms"] = capo_codedeploy.types.alarm_list.serialize_cbor(value["alarms"])
    return out


def deserialize_cbor(data: dict) -> AlarmConfiguration:
    out: AlarmConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("ignorePollAlarmFailure") is not None:
        out["ignore_poll_alarm_failure"] = data["ignorePollAlarmFailure"]
    else:
        out["ignore_poll_alarm_failure"] = False
    if data.get("alarms") is not None:
        import capo_codedeploy.types.alarm_list

        out["alarms"] = capo_codedeploy.types.alarm_list.deserialize_cbor(
            data["alarms"]
        )
    return out
