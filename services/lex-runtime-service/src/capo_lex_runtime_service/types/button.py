"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#Button``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_runtime_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.button_text_string_with_length
    import capo_lex_runtime_service.types.button_value_string_with_length


class Button(TypedDict, closed=True):
    text: "capo_lex_runtime_service.types.button_text_string_with_length.ButtonTextStringWithLength"
    """<p>Text that is visible to the user on the button.</p>"""
    value: "capo_lex_runtime_service.types.button_value_string_with_length.ButtonValueStringWithLength"
    """<p>The value sent to Amazon Lex when a user chooses the button. For example, consider button text "NYC." When the user chooses the button, the value sent can be "New York City."</p>"""


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
        raise DeserializationError("Button.text required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Button.value required")
    return out
