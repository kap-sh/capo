"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AlarmSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.alarm_model_name
    import capo_iot_events_data.types.alarm_model_version
    import capo_iot_events_data.types.alarm_state_name
    import capo_iot_events_data.types.key_value
    import capo_iot_events_data.types.timestamp


class AlarmSummary(TypedDict, closed=True):
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
    state_name: NotRequired[
        "capo_iot_events_data.types.alarm_state_name.AlarmStateName"
    ]
    """<p>The name of the alarm state. The state name can be one of the following values:</p> <ul> <li> <p> <code>DISABLED</code> - When the alarm is in the <code>DISABLED</code> state, it isn't ready to evaluate data. To enable the alarm, you must change the alarm to the <code>NORMAL</code> state.</p> </li> <li> <p> <code>NORMAL</code> - When the alarm is in the <code>NORMAL</code> state, it's ready to evaluate data.</p> </li> <li> <p> <code>ACTIVE</code> - If the alarm is in the <code>ACTIVE</code> state, the alarm is invoked.</p> </li> <li> <p> <code>ACKNOWLEDGED</code> - When the alarm is in the <code>ACKNOWLEDGED</code> state, the alarm was invoked and you acknowledged the alarm.</p> </li> <li> <p> <code>SNOOZE_DISABLED</code> - When the alarm is in the <code>SNOOZE_DISABLED</code> state, the alarm is disabled for a specified period of time. After the snooze time, the alarm automatically changes to the <code>NORMAL</code> state. </p> </li> <li> <p> <code>LATCHED</code> - When the alarm is in the <code>LATCHED</code> state, the alarm was invoked. However, the data that the alarm is currently evaluating is within the specified range. To change the alarm to the <code>NORMAL</code> state, you must acknowledge the alarm.</p> </li> </ul>"""
    creation_time: NotRequired["capo_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the alarm was created, in the Unix epoch format.</p>"""
    last_update_time: NotRequired["capo_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the alarm was last updated, in the Unix epoch format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmSummary) -> dict:
    out: dict = {}
    if "alarm_model_name" in value:
        out["alarmModelName"] = value["alarm_model_name"]
    if "alarm_model_version" in value:
        out["alarmModelVersion"] = value["alarm_model_version"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "state_name" in value:
        import capo_iot_events_data.types.alarm_state_name

        out["stateName"] = capo_iot_events_data.types.alarm_state_name.serialize_json(
            value["state_name"]
        )
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


def deserialize_json(data: dict) -> AlarmSummary:
    out: AlarmSummary = {}  # type: ignore[typeddict-item]
    if data.get("alarmModelName") is not None:
        out["alarm_model_name"] = data["alarmModelName"]
    if data.get("alarmModelVersion") is not None:
        out["alarm_model_version"] = data["alarmModelVersion"]
    if data.get("keyValue") is not None:
        out["key_value"] = data["keyValue"]
    if data.get("stateName") is not None:
        import capo_iot_events_data.types.alarm_state_name

        out["state_name"] = (
            capo_iot_events_data.types.alarm_state_name.deserialize_json(
                data["stateName"]
            )
        )
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
