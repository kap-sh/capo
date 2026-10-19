"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PlainTextMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.plain_text_message_value


class PlainTextMessage(TypedDict, closed=True):
    value: "capo_lex_models_v2.types.plain_text_message_value.PlainTextMessageValue"
    """<p>The message to send to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlainTextMessage) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PlainTextMessage:
    out: PlainTextMessage = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
