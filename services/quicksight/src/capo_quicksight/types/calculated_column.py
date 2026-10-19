"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedColumn``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_id
    import capo_quicksight.types.column_name
    import capo_quicksight.types.data_set_calculated_field_expression


class CalculatedColumn(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>Column name.</p>"""
    column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Quick Sight preserves the existing calculated column.</p>"""
    expression: "capo_quicksight.types.data_set_calculated_field_expression.DataSetCalculatedFieldExpression"
    """<p>An expression that defines the calculated column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedColumn) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["ColumnId"] = value["column_id"]
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> CalculatedColumn:
    out: CalculatedColumn = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("ColumnId") is not None:
        out["column_id"] = data["ColumnId"]
    else:
        out["column_id"] = ""
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    return out


def redact_sensitive(value: CalculatedColumn) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
