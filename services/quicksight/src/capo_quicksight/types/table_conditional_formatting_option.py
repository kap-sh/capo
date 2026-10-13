"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConditionalFormattingOption``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_cell_conditional_formatting
    import capo_quicksight.types.table_row_conditional_formatting


class TableConditionalFormattingOption(TypedDict, closed=True):
    cell: NotRequired[
        "capo_quicksight.types.table_cell_conditional_formatting.TableCellConditionalFormatting"
    ]
    """<p>The cell conditional formatting option for a table.</p>"""
    row: NotRequired[
        "capo_quicksight.types.table_row_conditional_formatting.TableRowConditionalFormatting"
    ]
    """<p>The row conditional formatting option for a table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableConditionalFormattingOption) -> dict:
    out: dict = {}
    if "cell" in value:
        import capo_quicksight.types.table_cell_conditional_formatting

        out["Cell"] = (
            capo_quicksight.types.table_cell_conditional_formatting.serialize_json(
                value["cell"]
            )
        )
    if "row" in value:
        import capo_quicksight.types.table_row_conditional_formatting

        out["Row"] = (
            capo_quicksight.types.table_row_conditional_formatting.serialize_json(
                value["row"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableConditionalFormattingOption:
    out: TableConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if data.get("Cell") is not None:
        import capo_quicksight.types.table_cell_conditional_formatting

        out["cell"] = (
            capo_quicksight.types.table_cell_conditional_formatting.deserialize_json(
                data["Cell"]
            )
        )
    if data.get("Row") is not None:
        import capo_quicksight.types.table_row_conditional_formatting

        out["row"] = (
            capo_quicksight.types.table_row_conditional_formatting.deserialize_json(
                data["Row"]
            )
        )
    return out


def redact_sensitive(value: TableConditionalFormattingOption) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cell" in value:
        import capo_quicksight.types.table_cell_conditional_formatting

        out["cell"] = (
            capo_quicksight.types.table_cell_conditional_formatting.redact_sensitive(
                value["cell"]
            )
        )
    if "row" in value:
        import capo_quicksight.types.table_row_conditional_formatting

        out["row"] = (
            capo_quicksight.types.table_row_conditional_formatting.redact_sensitive(
                value["row"]
            )
        )
    return out
