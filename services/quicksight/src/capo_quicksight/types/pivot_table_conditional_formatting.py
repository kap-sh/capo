"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_conditional_formatting_option_list


class PivotTableConditionalFormatting(TypedDict, closed=True):
    conditional_formatting_options: NotRequired[
        "capo_quicksight.types.pivot_table_conditional_formatting_option_list.PivotTableConditionalFormattingOptionList"
    ]
    """<p>Conditional formatting options for a <code>PivotTableVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormatting) -> dict:
    out: dict = {}
    if "conditional_formatting_options" in value:
        import capo_quicksight.types.pivot_table_conditional_formatting_option_list

        out["ConditionalFormattingOptions"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_option_list.serialize_json(
                value["conditional_formatting_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConditionalFormatting:
    out: PivotTableConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("ConditionalFormattingOptions") is not None:
        import capo_quicksight.types.pivot_table_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    return out


def redact_sensitive(value: PivotTableConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conditional_formatting_options" in value:
        import capo_quicksight.types.pivot_table_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_option_list.redact_sensitive(
                value["conditional_formatting_options"]
            )
        )
    return out
