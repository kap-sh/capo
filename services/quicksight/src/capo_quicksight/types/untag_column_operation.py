"""Generated from Smithy shape ``com.amazonaws.quicksight#UntagColumnOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.column_tag_names


class UntagColumnOperation(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The column that this operation acts on.</p>"""
    tag_names: "capo_quicksight.types.column_tag_names.ColumnTagNames"
    """<p>The column tags to remove from this column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagColumnOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    import capo_quicksight.types.column_tag_names

    out["TagNames"] = capo_quicksight.types.column_tag_names.serialize_json(
        value["tag_names"]
    )
    return out


def deserialize_json(data: dict) -> UntagColumnOperation:
    out: UntagColumnOperation = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("TagNames") is not None:
        import capo_quicksight.types.column_tag_names

        out["tag_names"] = capo_quicksight.types.column_tag_names.deserialize_json(
            data["TagNames"]
        )
    else:
        out["tag_names"] = []
    return out
