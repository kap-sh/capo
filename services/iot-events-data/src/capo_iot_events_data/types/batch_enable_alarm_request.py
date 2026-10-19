"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchEnableAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.enable_alarm_action_requests


class BatchEnableAlarmRequest(TypedDict, closed=True):
    enable_action_requests: "capo_iot_events_data.types.enable_alarm_action_requests.EnableAlarmActionRequests"
    """<p>The list of enable action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnableAlarmRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.enable_alarm_action_requests

    out["enableActionRequests"] = (
        capo_iot_events_data.types.enable_alarm_action_requests.serialize_json(
            value["enable_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchEnableAlarmRequest:
    out: BatchEnableAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("enableActionRequests") is not None:
        import capo_iot_events_data.types.enable_alarm_action_requests

        out["enable_action_requests"] = (
            capo_iot_events_data.types.enable_alarm_action_requests.deserialize_json(
                data["enableActionRequests"]
            )
        )
    else:
        out["enable_action_requests"] = []
    return out
