"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.message_data
    import capo_qconnect.types.participant
    import capo_qconnect.types.uuid


class MessageOutput(TypedDict, closed=True):
    value: "capo_qconnect.types.message_data.MessageData"
    """<p>The value of a message data.</p>"""
    message_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of a message.</p>"""
    participant: "capo_qconnect.types.participant.Participant"
    """<p>The participant of a message.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of a message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageOutput) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_data

    out["value"] = capo_qconnect.types.message_data.serialize_json(value["value"])
    out["messageId"] = value["message_id"]
    out["participant"] = value["participant"]
    import capo_qconnect.types._prelude.timestamp

    out["timestamp"] = capo_qconnect.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    return out


def deserialize_json(data: dict) -> MessageOutput:
    out: MessageOutput = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_qconnect.types.message_data

        out["value"] = capo_qconnect.types.message_data.deserialize_json(data["value"])
    else:
        import capo_qconnect.types._unknown

        out["value"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    else:
        out["message_id"] = ""
    if data.get("participant") is not None:
        out["participant"] = data["participant"]
    else:
        out["participant"] = ""
    if data.get("timestamp") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["timestamp"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: MessageOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_qconnect.types.message_data

        out["value"] = capo_qconnect.types.message_data.redact_sensitive(value["value"])
    return out
