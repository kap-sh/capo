"""Generated from Smithy shape ``com.amazonaws.quicksight#TableCellConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.text_conditional_format


class TableCellConditionalFormatting(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the cell for conditional formatting.</p>"""
    text_format: NotRequired[
        "capo_quicksight.types.text_conditional_format.TextConditionalFormat"
    ]
    """<p>The text format of the cell for conditional formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableCellConditionalFormatting) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "text_format" in value:
        import capo_quicksight.types.text_conditional_format

        out["TextFormat"] = (
            capo_quicksight.types.text_conditional_format.serialize_json(
                value["text_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableCellConditionalFormatting:
    out: TableCellConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("TableCellConditionalFormatting.field_id required")
    if data.get("TextFormat") is not None:
        import capo_quicksight.types.text_conditional_format

        out["text_format"] = (
            capo_quicksight.types.text_conditional_format.deserialize_json(
                data["TextFormat"]
            )
        )
    return out


def redact_sensitive(value: TableCellConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_format" in value:
        import capo_quicksight.types.text_conditional_format

        out["text_format"] = (
            capo_quicksight.types.text_conditional_format.redact_sensitive(
                value["text_format"]
            )
        )
    return out
