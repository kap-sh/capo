"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Button``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.button_text
    import capo_lex_models_v2.types.button_value


class Button(TypedDict, closed=True):
    text: "capo_lex_models_v2.types.button_text.ButtonText"
    """<p>The text that appears on the button. Use this to tell the user what value is returned when they choose this button.</p>"""
    value: "capo_lex_models_v2.types.button_value.ButtonValue"
    """<p>The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Button) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Button:
    out: Button = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
