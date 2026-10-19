"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchSnoozeAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.snooze_alarm_action_requests


class BatchSnoozeAlarmRequest(TypedDict, closed=True):
    snooze_action_requests: "capo_iot_events_data.types.snooze_alarm_action_requests.SnoozeAlarmActionRequests"
    """<p>The list of snooze action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSnoozeAlarmRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.snooze_alarm_action_requests

    out["snoozeActionRequests"] = (
        capo_iot_events_data.types.snooze_alarm_action_requests.serialize_json(
            value["snooze_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchSnoozeAlarmRequest:
    out: BatchSnoozeAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("snoozeActionRequests") is not None:
        import capo_iot_events_data.types.snooze_alarm_action_requests

        out["snooze_action_requests"] = (
            capo_iot_events_data.types.snooze_alarm_action_requests.deserialize_json(
                data["snoozeActionRequests"]
            )
        )
    else:
        out["snooze_action_requests"] = []
    return out
