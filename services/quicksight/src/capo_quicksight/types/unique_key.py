"""Generated from Smithy shape ``com.amazonaws.quicksight#UniqueKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.unique_key_column_name_list


class UniqueKey(TypedDict, closed=True):
    column_names: (
        "capo_quicksight.types.unique_key_column_name_list.UniqueKeyColumnNameList"
    )
    """<p>The name of the column that is referenced in the <code>UniqueKey</code> configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UniqueKey) -> dict:
    out: dict = {}
    import capo_quicksight.types.unique_key_column_name_list

    out["ColumnNames"] = (
        capo_quicksight.types.unique_key_column_name_list.serialize_json(
            value["column_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> UniqueKey:
    out: UniqueKey = {}  # type: ignore[typeddict-item]
    if data.get("ColumnNames") is not None:
        import capo_quicksight.types.unique_key_column_name_list

        out["column_names"] = (
            capo_quicksight.types.unique_key_column_name_list.deserialize_json(
                data["ColumnNames"]
            )
        )
    else:
        out["column_names"] = []
    return out
