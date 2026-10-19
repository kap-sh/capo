"""Generated from Smithy shape ``com.amazonaws.qapps#ConversationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.sender


class ConversationMessage(TypedDict, closed=True):
    body: "str"
    """<p>The text content of the conversation message.</p>"""
    type: "capo_qapps.types.sender.Sender"
    """<p>The type of the conversation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationMessage) -> dict:
    out: dict = {}
    out["body"] = value["body"]
    import capo_qapps.types.sender

    out["type"] = capo_qapps.types.sender.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ConversationMessage:
    out: ConversationMessage = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        out["body"] = ""
    if data.get("type") is not None:
        import capo_qapps.types.sender

        out["type"] = capo_qapps.types.sender.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_qapps.types.sender.Sender", "")
    return out
