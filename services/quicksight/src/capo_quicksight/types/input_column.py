"""Generated from Smithy shape ``com.amazonaws.quicksight#InputColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_data_sub_type
    import capo_quicksight.types.column_id
    import capo_quicksight.types.column_name
    import capo_quicksight.types.input_column_data_type


class InputColumn(TypedDict, closed=True):
    name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name of this column in the underlying data source.</p>"""
    id: NotRequired["capo_quicksight.types.column_id.ColumnId"]
    """<p>A unique identifier for the input column.</p>"""
    type: "capo_quicksight.types.input_column_data_type.InputColumnDataType"
    """<p>The data type of the column.</p> <p> <b>Note:</b> <code>SEMISTRUCT</code> represents Athena's map, row, and struct data types. It is supported when using the new data preparation experience.</p>"""
    sub_type: NotRequired[
        "capo_quicksight.types.column_data_sub_type.ColumnDataSubType"
    ]
    """<p>The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputColumn) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    import capo_quicksight.types.input_column_data_type

    out["Type"] = capo_quicksight.types.input_column_data_type.serialize_json(
        value["type"]
    )
    if "sub_type" in value:
        import capo_quicksight.types.column_data_sub_type

        out["SubType"] = capo_quicksight.types.column_data_sub_type.serialize_json(
            value["sub_type"]
        )
    return out


def deserialize_json(data: dict) -> InputColumn:
    out: InputColumn = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_quicksight.types.input_column_data_type

        out["type"] = capo_quicksight.types.input_column_data_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.input_column_data_type.InputColumnDataType", ""
        )
    if data.get("SubType") is not None:
        import capo_quicksight.types.column_data_sub_type

        out["sub_type"] = capo_quicksight.types.column_data_sub_type.deserialize_json(
            data["SubType"]
        )
    return out
