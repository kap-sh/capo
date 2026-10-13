"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableCellConditionalFormatting``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.pivot_table_conditional_formatting_scope
    import capo_quicksight.types.pivot_table_conditional_formatting_scope_list
    import capo_quicksight.types.text_conditional_format


class PivotTableCellConditionalFormatting(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the cell for conditional formatting.</p>"""
    text_format: NotRequired[
        "capo_quicksight.types.text_conditional_format.TextConditionalFormat"
    ]
    """<p>The text format of the cell for conditional formatting.</p>"""
    scope: NotRequired[
        "capo_quicksight.types.pivot_table_conditional_formatting_scope.PivotTableConditionalFormattingScope"
    ]
    """<p>The scope of the cell for conditional formatting.</p>"""
    scopes: NotRequired[
        "capo_quicksight.types.pivot_table_conditional_formatting_scope_list.PivotTableConditionalFormattingScopeList"
    ]
    """<p>A list of cell scopes for conditional formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableCellConditionalFormatting) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "text_format" in value:
        import capo_quicksight.types.text_conditional_format

        out["TextFormat"] = (
            capo_quicksight.types.text_conditional_format.serialize_json(
                value["text_format"]
            )
        )
    if "scope" in value:
        import capo_quicksight.types.pivot_table_conditional_formatting_scope

        out["Scope"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_scope.serialize_json(
                value["scope"]
            )
        )
    if "scopes" in value:
        import capo_quicksight.types.pivot_table_conditional_formatting_scope_list

        out["Scopes"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_scope_list.serialize_json(
                value["scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableCellConditionalFormatting:
    out: PivotTableCellConditionalFormatting = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError(
            "PivotTableCellConditionalFormatting.field_id required"
        )
    if data.get("TextFormat") is not None:
        import capo_quicksight.types.text_conditional_format

        out["text_format"] = (
            capo_quicksight.types.text_conditional_format.deserialize_json(
                data["TextFormat"]
            )
        )
    if data.get("Scope") is not None:
        import capo_quicksight.types.pivot_table_conditional_formatting_scope

        out["scope"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_scope.deserialize_json(
                data["Scope"]
            )
        )
    if data.get("Scopes") is not None:
        import capo_quicksight.types.pivot_table_conditional_formatting_scope_list

        out["scopes"] = (
            capo_quicksight.types.pivot_table_conditional_formatting_scope_list.deserialize_json(
                data["Scopes"]
            )
        )
    return out


def redact_sensitive(value: PivotTableCellConditionalFormatting) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_format" in value:
        import capo_quicksight.types.text_conditional_format

        out["text_format"] = (
            capo_quicksight.types.text_conditional_format.redact_sensitive(
                value["text_format"]
            )
        )
    return out
