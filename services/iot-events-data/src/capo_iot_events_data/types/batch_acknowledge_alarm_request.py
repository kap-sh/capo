"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchAcknowledgeAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.acknowledge_alarm_action_requests


class BatchAcknowledgeAlarmRequest(TypedDict, closed=True):
    acknowledge_action_requests: "capo_iot_events_data.types.acknowledge_alarm_action_requests.AcknowledgeAlarmActionRequests"
    """<p>The list of acknowledge action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAcknowledgeAlarmRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.acknowledge_alarm_action_requests

    out["acknowledgeActionRequests"] = (
        capo_iot_events_data.types.acknowledge_alarm_action_requests.serialize_json(
            value["acknowledge_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchAcknowledgeAlarmRequest:
    out: BatchAcknowledgeAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("acknowledgeActionRequests") is not None:
        import capo_iot_events_data.types.acknowledge_alarm_action_requests

        out["acknowledge_action_requests"] = (
            capo_iot_events_data.types.acknowledge_alarm_action_requests.deserialize_json(
                data["acknowledgeActionRequests"]
            )
        )
    else:
        out["acknowledge_action_requests"] = []
    return out
