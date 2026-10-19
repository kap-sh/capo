"""Generated from Smithy shape ``com.amazonaws.quicksight#UnpivotOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_id
    import capo_quicksight.types.column_name
    import capo_quicksight.types.column_to_unpivot_list
    import capo_quicksight.types.transform_operation_alias
    import capo_quicksight.types.transform_operation_source


class UnpivotOperation(TypedDict, closed=True):
    alias: "capo_quicksight.types.transform_operation_alias.TransformOperationAlias"
    """<p>Alias for this operation.</p>"""
    source: "capo_quicksight.types.transform_operation_source.TransformOperationSource"
    """<p>The source transform operation that provides input data for unpivoting.</p>"""
    columns_to_unpivot: (
        "capo_quicksight.types.column_to_unpivot_list.ColumnToUnpivotList"
    )
    """<p>The list of columns to unpivot from the source data.</p>"""
    unpivoted_label_column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column that will contain the unpivoted column names.</p>"""
    unpivoted_label_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column that will contain the unpivoted column names.</p>"""
    unpivoted_value_column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column that will contain the unpivoted values.</p>"""
    unpivoted_value_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column that will contain the unpivoted values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnpivotOperation) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.transform_operation_source

    out["Source"] = capo_quicksight.types.transform_operation_source.serialize_json(
        value["source"]
    )
    import capo_quicksight.types.column_to_unpivot_list

    out["ColumnsToUnpivot"] = (
        capo_quicksight.types.column_to_unpivot_list.serialize_json(
            value["columns_to_unpivot"]
        )
    )
    out["UnpivotedLabelColumnName"] = value["unpivoted_label_column_name"]
    out["UnpivotedLabelColumnId"] = value["unpivoted_label_column_id"]
    out["UnpivotedValueColumnName"] = value["unpivoted_value_column_name"]
    out["UnpivotedValueColumnId"] = value["unpivoted_value_column_id"]
    return out


def deserialize_json(data: dict) -> UnpivotOperation:
    out: UnpivotOperation = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.transform_operation_source

        out["source"] = (
            capo_quicksight.types.transform_operation_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("UnpivotOperation.source required")
    if data.get("ColumnsToUnpivot") is not None:
        import capo_quicksight.types.column_to_unpivot_list

        out["columns_to_unpivot"] = (
            capo_quicksight.types.column_to_unpivot_list.deserialize_json(
                data["ColumnsToUnpivot"]
            )
        )
    else:
        out["columns_to_unpivot"] = []
    if data.get("UnpivotedLabelColumnName") is not None:
        out["unpivoted_label_column_name"] = data["UnpivotedLabelColumnName"]
    else:
        out["unpivoted_label_column_name"] = ""
    if data.get("UnpivotedLabelColumnId") is not None:
        out["unpivoted_label_column_id"] = data["UnpivotedLabelColumnId"]
    else:
        out["unpivoted_label_column_id"] = ""
    if data.get("UnpivotedValueColumnName") is not None:
        out["unpivoted_value_column_name"] = data["UnpivotedValueColumnName"]
    else:
        out["unpivoted_value_column_name"] = ""
    if data.get("UnpivotedValueColumnId") is not None:
        out["unpivoted_value_column_id"] = data["UnpivotedValueColumnId"]
    else:
        out["unpivoted_value_column_id"] = ""
    return out
