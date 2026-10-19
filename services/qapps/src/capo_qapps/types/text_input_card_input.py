"""Generated from Smithy shape ``com.amazonaws.qapps#TextInputCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.card_type
    import capo_qapps.types.default
    import capo_qapps.types.placeholder
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class TextInputCardInput(TypedDict, closed=True):
    title: "capo_qapps.types.title.Title"
    """<p>The title or label of the text input card.</p>"""
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the text input card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    placeholder: NotRequired["capo_qapps.types.placeholder.Placeholder"]
    """<p>The placeholder text to display in the text input field.</p>"""
    default_value: NotRequired["capo_qapps.types.default.Default"]
    """<p>The default value to pre-populate in the text input field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextInputCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(
        value.get("type", "text-input")
    )
    if "placeholder" in value:
        out["placeholder"] = value["placeholder"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> TextInputCardInput:
    out: TextInputCardInput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "text-input"
    if data.get("placeholder") is not None:
        out["placeholder"] = data["placeholder"]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    return out
