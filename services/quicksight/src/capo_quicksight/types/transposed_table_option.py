"""Generated from Smithy shape ``com.amazonaws.quicksight#TransposedTableOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.transposed_column_index
    import capo_quicksight.types.transposed_column_type


class TransposedTableOption(TypedDict, closed=True):
    column_index: NotRequired[
        "capo_quicksight.types.transposed_column_index.TransposedColumnIndex"
    ]
    """<p>The index of a columns in a transposed table. The index range is 0-9999.</p>"""
    column_width: NotRequired["capo_quicksight.types.pixel_length.PixelLength"]
    """<p>The width of a column in a transposed table.</p>"""
    column_type: "capo_quicksight.types.transposed_column_type.TransposedColumnType"
    """<p>The column type of the column in a transposed table. Choose one of the following options:</p> <ul> <li> <p> <code>ROW_HEADER_COLUMN</code>: Refers to the leftmost column of the row header in the transposed table.</p> </li> <li> <p> <code>VALUE_COLUMN</code>: Refers to all value columns in the transposed table.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransposedTableOption) -> dict:
    out: dict = {}
    if "column_index" in value:
        out["ColumnIndex"] = value["column_index"]
    if "column_width" in value:
        out["ColumnWidth"] = value["column_width"]
    import capo_quicksight.types.transposed_column_type

    out["ColumnType"] = capo_quicksight.types.transposed_column_type.serialize_json(
        value["column_type"]
    )
    return out


def deserialize_json(data: dict) -> TransposedTableOption:
    out: TransposedTableOption = {}  # type: ignore[typeddict-item]
    if data.get("ColumnIndex") is not None:
        out["column_index"] = data["ColumnIndex"]
    if data.get("ColumnWidth") is not None:
        out["column_width"] = data["ColumnWidth"]
    if data.get("ColumnType") is not None:
        import capo_quicksight.types.transposed_column_type

        out["column_type"] = (
            capo_quicksight.types.transposed_column_type.deserialize_json(
                data["ColumnType"]
            )
        )
    else:
        import typing

        out["column_type"] = typing.cast(
            "capo_quicksight.types.transposed_column_type.TransposedColumnType", ""
        )
    return out
