"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Alarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.alarm_model_name
    import capo_iot_events_data.types.alarm_model_version
    import capo_iot_events_data.types.alarm_state
    import capo_iot_events_data.types.key_value
    import capo_iot_events_data.types.severity
    import capo_iot_events_data.types.timestamp


class Alarm(TypedDict, closed=True):
    alarm_model_name: NotRequired[
        "capo_iot_events_data.types.alarm_model_name.AlarmModelName"
    ]
    """<p>The name of the alarm model.</p>"""
    alarm_model_version: NotRequired[
        "capo_iot_events_data.types.alarm_model_version.AlarmModelVersion"
    ]
    """<p>The version of the alarm model.</p>"""
    key_value: NotRequired["capo_iot_events_data.types.key_value.KeyValue"]
    """<p>The value of the key used as a filter to select only the alarms associated with the <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key">key</a>.</p>"""
    alarm_state: NotRequired["capo_iot_events_data.types.alarm_state.AlarmState"]
    """<p>Contains information about the current state of the alarm.</p>"""
    severity: NotRequired["capo_iot_events_data.types.severity.Severity"]
    """<p>A non-negative integer that reflects the severity level of the alarm.</p>"""
    creation_time: NotRequired["capo_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the alarm was created, in the Unix epoch format.</p>"""
    last_update_time: NotRequired["capo_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the alarm was last updated, in the Unix epoch format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alarm) -> dict:
    out: dict = {}
    if "alarm_model_name" in value:
        out["alarmModelName"] = value["alarm_model_name"]
    if "alarm_model_version" in value:
        out["alarmModelVersion"] = value["alarm_model_version"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "alarm_state" in value:
        import capo_iot_events_data.types.alarm_state

        out["alarmState"] = capo_iot_events_data.types.alarm_state.serialize_json(
            value["alarm_state"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "creation_time" in value:
        import capo_iot_events_data.types.timestamp

        out["creationTime"] = capo_iot_events_data.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import capo_iot_events_data.types.timestamp

        out["lastUpdateTime"] = capo_iot_events_data.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    return out


def deserialize_json(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if data.get("alarmModelName") is not None:
        out["alarm_model_name"] = data["alarmModelName"]
    if data.get("alarmModelVersion") is not None:
        out["alarm_model_version"] = data["alarmModelVersion"]
    if data.get("keyValue") is not None:
        out["key_value"] = data["keyValue"]
    if data.get("alarmState") is not None:
        import capo_iot_events_data.types.alarm_state

        out["alarm_state"] = capo_iot_events_data.types.alarm_state.deserialize_json(
            data["alarmState"]
        )
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("creationTime") is not None:
        import capo_iot_events_data.types.timestamp

        out["creation_time"] = capo_iot_events_data.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdateTime") is not None:
        import capo_iot_events_data.types.timestamp

        out["last_update_time"] = capo_iot_events_data.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    return out
