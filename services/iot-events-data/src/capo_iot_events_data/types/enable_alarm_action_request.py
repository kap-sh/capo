"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#EnableAlarmActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events_data.types.alarm_model_name
    import capo_iot_events_data.types.key_value
    import capo_iot_events_data.types.note
    import capo_iot_events_data.types.request_id


class EnableAlarmActionRequest(TypedDict, closed=True):
    request_id: "capo_iot_events_data.types.request_id.RequestId"
    """<p>The request ID. Each ID must be unique within each batch.</p>"""
    alarm_model_name: "capo_iot_events_data.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    key_value: NotRequired["capo_iot_events_data.types.key_value.KeyValue"]
    """<p>The value of the key used as a filter to select only the alarms associated with the <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key">key</a>.</p>"""
    note: NotRequired["capo_iot_events_data.types.note.Note"]
    """<p>The note that you can leave when you enable the alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableAlarmActionRequest) -> dict:
    out: dict = {}
    out["requestId"] = value["request_id"]
    out["alarmModelName"] = value["alarm_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "note" in value:
        out["note"] = value["note"]
    return out


def deserialize_json(data: dict) -> EnableAlarmActionRequest:
    out: EnableAlarmActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("EnableAlarmActionRequest.request_id required")
    if data.get("alarmModelName") is not None:
        out["alarm_model_name"] = data["alarmModelName"]
    else:
        raise DeserializationError("EnableAlarmActionRequest.alarm_model_name required")
    if data.get("keyValue") is not None:
        out["key_value"] = data["keyValue"]
    if data.get("note") is not None:
        out["note"] = data["note"]
    return out
