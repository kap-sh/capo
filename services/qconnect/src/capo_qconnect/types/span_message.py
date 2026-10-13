"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.participant
    import capo_qconnect.types.span_message_value_list
    import capo_qconnect.types.uuid


class SpanMessage(TypedDict, closed=True):
    message_id: "capo_qconnect.types.uuid.Uuid"
    """<p>Unique message identifier</p>"""
    participant: "capo_qconnect.types.participant.Participant"
    """<p>Message source role</p>"""
    timestamp: "datetime.datetime"
    """<p>Message timestamp</p>"""
    values: "capo_qconnect.types.span_message_value_list.SpanMessageValueList"
    """<p>Message content values (text, tool use, tool result, reasoning)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanMessage) -> dict:
    out: dict = {}
    out["messageId"] = value["message_id"]
    out["participant"] = value["participant"]
    import capo_qconnect.types._prelude.timestamp

    out["timestamp"] = capo_qconnect.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_qconnect.types.span_message_value_list

    out["values"] = capo_qconnect.types.span_message_value_list.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> SpanMessage:
    out: SpanMessage = {}  # type: ignore[typeddict-item]
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    else:
        raise DeserializationError("SpanMessage.message_id required")
    if data.get("participant") is not None:
        out["participant"] = data["participant"]
    else:
        raise DeserializationError("SpanMessage.participant required")
    if data.get("timestamp") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["timestamp"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("SpanMessage.timestamp required")
    if data.get("values") is not None:
        import capo_qconnect.types.span_message_value_list

        out["values"] = capo_qconnect.types.span_message_value_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("SpanMessage.values required")
    return out


def redact_sensitive(value: SpanMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_qconnect.types.span_message_value_list

        out["values"] = capo_qconnect.types.span_message_value_list.redact_sensitive(
            value["values"]
        )
    return out
