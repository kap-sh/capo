"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartPrimaryValueConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_color
    import capo_quicksight.types.conditional_formatting_icon


class GaugeChartPrimaryValueConditionalFormatting(TypedDict, closed=True):
    text_color: NotRequired[
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting of the primary value text color.</p>"""
    icon: NotRequired[
        "capo_quicksight.types.conditional_formatting_icon.ConditionalFormattingIcon"
    ]
    """<p>The conditional formatting of the primary value icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartPrimaryValueConditionalFormatting) -> dict:
    out: dict = {}
    if "text_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["TextColor"] = (
            capo_quicksight.types.conditional_formatting_color.serialize_json(
                value["text_color"]
            )
        )
    if "icon" in value:
        import capo_quicksight.types.conditional_formatting_icon

        out["Icon"] = capo_quicksight.types.conditional_formatting_icon.serialize_json(
            value["icon"]
        )
    return out


def deserialize_json(data: dict) -> GaugeChartPrimaryValueConditionalFormatting:
    out: GaugeChartPrimaryValueConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("TextColor") is not None:
        import capo_quicksight.types.conditional_formatting_color

        out["text_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["TextColor"]
            )
        )
    if data.get("Icon") is not None:
        import capo_quicksight.types.conditional_formatting_icon

        out["icon"] = (
            capo_quicksight.types.conditional_formatting_icon.deserialize_json(
                data["Icon"]
            )
        )
    return out


def redact_sensitive(
    value: GaugeChartPrimaryValueConditionalFormatting,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["text_color"] = (
            capo_quicksight.types.conditional_formatting_color.redact_sensitive(
                value["text_color"]
            )
        )
    if "icon" in value:
        import capo_quicksight.types.conditional_formatting_icon

        out["icon"] = (
            capo_quicksight.types.conditional_formatting_icon.redact_sensitive(
                value["icon"]
            )
        )
    return out
