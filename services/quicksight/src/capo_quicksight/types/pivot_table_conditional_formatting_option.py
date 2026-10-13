"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_cell_conditional_formatting


class PivotTableConditionalFormattingOption(TypedDict, closed=True):
    cell: NotRequired[
        "capo_quicksight.types.pivot_table_cell_conditional_formatting.PivotTableCellConditionalFormatting"
    ]
    """<p>The cell conditional formatting option for a pivot table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingOption) -> dict:
    out: dict = {}
    if "cell" in value:
        import capo_quicksight.types.pivot_table_cell_conditional_formatting

        out["Cell"] = (
            capo_quicksight.types.pivot_table_cell_conditional_formatting.serialize_json(
                value["cell"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConditionalFormattingOption:
    out: PivotTableConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if data.get("Cell") is not None:
        import capo_quicksight.types.pivot_table_cell_conditional_formatting

        out["cell"] = (
            capo_quicksight.types.pivot_table_cell_conditional_formatting.deserialize_json(
                data["Cell"]
            )
        )
    return out


def redact_sensitive(value: PivotTableConditionalFormattingOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cell" in value:
        import capo_quicksight.types.pivot_table_cell_conditional_formatting

        out["cell"] = (
            capo_quicksight.types.pivot_table_cell_conditional_formatting.redact_sensitive(
                value["cell"]
            )
        )
    return out
