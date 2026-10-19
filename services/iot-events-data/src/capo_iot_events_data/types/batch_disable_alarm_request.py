"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDisableAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.disable_alarm_action_requests


class BatchDisableAlarmRequest(TypedDict, closed=True):
    disable_action_requests: "capo_iot_events_data.types.disable_alarm_action_requests.DisableAlarmActionRequests"
    """<p>The list of disable action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisableAlarmRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.disable_alarm_action_requests

    out["disableActionRequests"] = (
        capo_iot_events_data.types.disable_alarm_action_requests.serialize_json(
            value["disable_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDisableAlarmRequest:
    out: BatchDisableAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("disableActionRequests") is not None:
        import capo_iot_events_data.types.disable_alarm_action_requests

        out["disable_action_requests"] = (
            capo_iot_events_data.types.disable_alarm_action_requests.deserialize_json(
                data["disableActionRequests"]
            )
        )
    else:
        out["disable_action_requests"] = []
    return out
