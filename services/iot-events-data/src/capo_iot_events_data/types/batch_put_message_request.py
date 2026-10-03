"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchPutMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events_data.types.messages


class BatchPutMessageRequest(TypedDict, closed=True):
    messages: "capo_iot_events_data.types.messages.Messages"
    """<p>The list of messages to send. Each message has the following format: <code>'{ "messageId": "string", "inputName": "string", "payload": "string"}'</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMessageRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.messages

    out["messages"] = capo_iot_events_data.types.messages.serialize_json(
        value["messages"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutMessageRequest:
    out: BatchPutMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_iot_events_data.types.messages

        out["messages"] = capo_iot_events_data.types.messages.deserialize_json(
            data["messages"]
        )
    else:
        raise DeserializationError("BatchPutMessageRequest.messages required")
    return out
