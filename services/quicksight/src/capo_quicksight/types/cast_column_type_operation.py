"""Generated from Smithy shape ``com.amazonaws.quicksight#CastColumnTypeOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_data_sub_type
    import capo_quicksight.types.column_data_type
    import capo_quicksight.types.column_name
    import capo_quicksight.types.type_cast_format


class CastColumnTypeOperation(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>Column name.</p>"""
    new_column_type: "capo_quicksight.types.column_data_type.ColumnDataType"
    """<p>New column data type.</p>"""
    sub_type: NotRequired[
        "capo_quicksight.types.column_data_sub_type.ColumnDataSubType"
    ]
    """<p>The sub data type of the new column. Sub types are only available for decimal columns that are part of a SPICE dataset.</p>"""
    format: NotRequired["capo_quicksight.types.type_cast_format.TypeCastFormat"]
    """<p>When casting a column from string to datetime type, you can supply a string in a format supported by Quick Sight to denote the source data format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CastColumnTypeOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    import capo_quicksight.types.column_data_type

    out["NewColumnType"] = capo_quicksight.types.column_data_type.serialize_json(
        value["new_column_type"]
    )
    if "sub_type" in value:
        import capo_quicksight.types.column_data_sub_type

        out["SubType"] = capo_quicksight.types.column_data_sub_type.serialize_json(
            value["sub_type"]
        )
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_json(data: dict) -> CastColumnTypeOperation:
    out: CastColumnTypeOperation = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("NewColumnType") is not None:
        import capo_quicksight.types.column_data_type

        out["new_column_type"] = (
            capo_quicksight.types.column_data_type.deserialize_json(
                data["NewColumnType"]
            )
        )
    else:
        import typing

        out["new_column_type"] = typing.cast(
            "capo_quicksight.types.column_data_type.ColumnDataType", ""
        )
    if data.get("SubType") is not None:
        import capo_quicksight.types.column_data_sub_type

        out["sub_type"] = capo_quicksight.types.column_data_sub_type.deserialize_json(
            data["SubType"]
        )
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    return out
