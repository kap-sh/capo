"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIProgressBarConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_color


class KPIProgressBarConditionalFormatting(TypedDict, closed=True):
    foreground_color: NotRequired[
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting of the progress bar's foreground color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIProgressBarConditionalFormatting) -> dict:
    out: dict = {}
    if "foreground_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["ForegroundColor"] = (
            capo_quicksight.types.conditional_formatting_color.serialize_json(
                value["foreground_color"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIProgressBarConditionalFormatting:
    out: KPIProgressBarConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("ForegroundColor") is not None:
        import capo_quicksight.types.conditional_formatting_color

        out["foreground_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["ForegroundColor"]
            )
        )
    return out


def redact_sensitive(value: KPIProgressBarConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "foreground_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["foreground_color"] = (
            capo_quicksight.types.conditional_formatting_color.redact_sensitive(
                value["foreground_color"]
            )
        )
    return out
