"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_data


class MessageInput(TypedDict, closed=True):
    value: "capo_qconnect.types.message_data.MessageData"
    """<p>The message input value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageInput) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_data

    out["value"] = capo_qconnect.types.message_data.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> MessageInput:
    out: MessageInput = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_qconnect.types.message_data

        out["value"] = capo_qconnect.types.message_data.deserialize_json(data["value"])
    else:
        import capo_qconnect.types._unknown

        out["value"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    return out


def redact_sensitive(value: MessageInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        import capo_qconnect.types.message_data

        out["value"] = capo_qconnect.types.message_data.redact_sensitive(value["value"])
    return out
