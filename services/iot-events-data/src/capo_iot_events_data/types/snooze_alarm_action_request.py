"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#SnoozeAlarmActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events_data.types.alarm_model_name
    import capo_iot_events_data.types.key_value
    import capo_iot_events_data.types.note
    import capo_iot_events_data.types.request_id
    import capo_iot_events_data.types.snooze_duration


class SnoozeAlarmActionRequest(TypedDict, closed=True):
    request_id: "capo_iot_events_data.types.request_id.RequestId"
    """<p>The request ID. Each ID must be unique within each batch.</p>"""
    alarm_model_name: "capo_iot_events_data.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    key_value: NotRequired["capo_iot_events_data.types.key_value.KeyValue"]
    """<p>The value of the key used as a filter to select only the alarms associated with the <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key">key</a>.</p>"""
    note: NotRequired["capo_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you snooze the alarm.</p>"""
    snooze_duration: "capo_iot_events_data.types.snooze_duration.SnoozeDuration"
    """<p>The snooze time in seconds. The alarm automatically changes to the <code>NORMAL</code> state after this duration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnoozeAlarmActionRequest) -> dict:
    out: dict = {}
    out["requestId"] = value["request_id"]
    out["alarmModelName"] = value["alarm_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "note" in value:
        out["note"] = value["note"]
    out["snoozeDuration"] = value["snooze_duration"]
    return out


def deserialize_json(data: dict) -> SnoozeAlarmActionRequest:
    out: SnoozeAlarmActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("SnoozeAlarmActionRequest.request_id required")
    if data.get("alarmModelName") is not None:
        out["alarm_model_name"] = data["alarmModelName"]
    else:
        raise DeserializationError("SnoozeAlarmActionRequest.alarm_model_name required")
    if data.get("keyValue") is not None:
        out["key_value"] = data["keyValue"]
    if data.get("note") is not None:
        out["note"] = data["note"]
    if data.get("snoozeDuration") is not None:
        out["snooze_duration"] = data["snoozeDuration"]
    else:
        raise DeserializationError("SnoozeAlarmActionRequest.snooze_duration required")
    return out
