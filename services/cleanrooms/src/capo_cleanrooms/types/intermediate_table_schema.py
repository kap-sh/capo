"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_list


class IntermediateTableSchema(TypedDict, closed=True):
    columns: "capo_cleanrooms.types.column_list.ColumnList"
    """<p>The list of columns in the intermediate table schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableSchema) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.column_list

    out["columns"] = capo_cleanrooms.types.column_list.serialize_json(value["columns"])
    return out


def deserialize_json(data: dict) -> IntermediateTableSchema:
    out: IntermediateTableSchema = {}  # type: ignore[typeddict-item]
    if data.get("columns") is not None:
        import capo_cleanrooms.types.column_list

        out["columns"] = capo_cleanrooms.types.column_list.deserialize_json(
            data["columns"]
        )
    else:
        out["columns"] = []
    return out
