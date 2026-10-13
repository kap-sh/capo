"""Generated from Smithy shape ``com.amazonaws.quicksight#TableRowConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_color


class TableRowConditionalFormatting(TypedDict, closed=True):
    background_color: NotRequired[
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting color (solid, gradient) of the background for a table row.</p>"""
    text_color: NotRequired[
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting color (solid, gradient) of the text for a table row.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableRowConditionalFormatting) -> dict:
    out: dict = {}
    if "background_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["BackgroundColor"] = (
            capo_quicksight.types.conditional_formatting_color.serialize_json(
                value["background_color"]
            )
        )
    if "text_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["TextColor"] = (
            capo_quicksight.types.conditional_formatting_color.serialize_json(
                value["text_color"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableRowConditionalFormatting:
    out: TableRowConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("BackgroundColor") is not None:
        import capo_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["BackgroundColor"]
            )
        )
    if data.get("TextColor") is not None:
        import capo_quicksight.types.conditional_formatting_color

        out["text_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["TextColor"]
            )
        )
    return out


def redact_sensitive(value: TableRowConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "background_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            capo_quicksight.types.conditional_formatting_color.redact_sensitive(
                value["background_color"]
            )
        )
    if "text_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["text_color"] = (
            capo_quicksight.types.conditional_formatting_color.redact_sensitive(
                value["text_color"]
            )
        )
    return out
