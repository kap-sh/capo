"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.column_name
    import capo_cleanroomsml.types.column_type_list


class ColumnSchema(TypedDict, closed=True):
    column_name: "capo_cleanroomsml.types.column_name.ColumnName"
    """<p>The name of a column.</p>"""
    column_types: "capo_cleanroomsml.types.column_type_list.ColumnTypeList"
    """<p>The data type of column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSchema) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    import capo_cleanroomsml.types.column_type_list

    out["columnTypes"] = capo_cleanroomsml.types.column_type_list.serialize_json(
        value["column_types"]
    )
    return out


def deserialize_json(data: dict) -> ColumnSchema:
    out: ColumnSchema = {}  # type: ignore[typeddict-item]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    else:
        out["column_name"] = ""
    if data.get("columnTypes") is not None:
        import capo_cleanroomsml.types.column_type_list

        out["column_types"] = capo_cleanroomsml.types.column_type_list.deserialize_json(
            data["columnTypes"]
        )
    else:
        out["column_types"] = []
    return out
