"""Generated from Smithy shape ``com.amazonaws.quicksight#ShapeConditionalFormat``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_color


class ShapeConditionalFormat(TypedDict, closed=True):
    background_color: (
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    )
    """<p>The conditional formatting for the shape background color of a filled map visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShapeConditionalFormat) -> dict:
    out: dict = {}
    import capo_quicksight.types.conditional_formatting_color

    out["BackgroundColor"] = (
        capo_quicksight.types.conditional_formatting_color.serialize_json(
            value["background_color"]
        )
    )
    return out


def deserialize_json(data: dict) -> ShapeConditionalFormat:
    out: ShapeConditionalFormat = {}  # type: ignore[typeddict-item]
    if data.get("BackgroundColor") is not None:
        import capo_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["BackgroundColor"]
            )
        )
    else:
        raise DeserializationError("ShapeConditionalFormat.background_color required")
    return out


def redact_sensitive(value: ShapeConditionalFormat) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "background_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            capo_quicksight.types.conditional_formatting_color.redact_sensitive(
                value["background_color"]
            )
        )
    return out
