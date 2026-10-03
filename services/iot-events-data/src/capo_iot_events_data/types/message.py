"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events_data.types.ephemeral_input_name
    import capo_iot_events_data.types.message_id
    import capo_iot_events_data.types.payload
    import capo_iot_events_data.types.timestamp_value


class Message(TypedDict, closed=True):
    message_id: "capo_iot_events_data.types.message_id.MessageId"
    """<p>The ID to assign to the message. Within each batch sent, each <code>"messageId"</code> must be unique.</p>"""
    input_name: "capo_iot_events_data.types.ephemeral_input_name.EphemeralInputName"
    """<p>The name of the input into which the message payload is transformed.</p>"""
    payload: "capo_iot_events_data.types.payload.Payload"
    """<p>The payload of the message. This can be a JSON string or a Base-64-encoded string representing binary data (in which case you must decode it).</p>"""
    timestamp: NotRequired["capo_iot_events_data.types.timestamp_value.TimestampValue"]
    """<p>The timestamp associated with the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    out["messageId"] = value["message_id"]
    out["inputName"] = value["input_name"]
    import capo_iot_events_data.types.payload

    out["payload"] = capo_iot_events_data.types.payload.serialize_json(value["payload"])
    if "timestamp" in value:
        import capo_iot_events_data.types.timestamp_value

        out["timestamp"] = capo_iot_events_data.types.timestamp_value.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    else:
        raise DeserializationError("Message.message_id required")
    if data.get("inputName") is not None:
        out["input_name"] = data["inputName"]
    else:
        raise DeserializationError("Message.input_name required")
    if data.get("payload") is not None:
        import capo_iot_events_data.types.payload

        out["payload"] = capo_iot_events_data.types.payload.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("Message.payload required")
    if data.get("timestamp") is not None:
        import capo_iot_events_data.types.timestamp_value

        out["timestamp"] = capo_iot_events_data.types.timestamp_value.deserialize_json(
            data["timestamp"]
        )
    return out
