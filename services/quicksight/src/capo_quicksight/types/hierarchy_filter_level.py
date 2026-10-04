"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterLevel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier


class HierarchyFilterLevel(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that this level of the hierarchy drills down by. This column must belong to the same dataset as <code>HierarchyFilter$Column</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterLevel) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    return out


def deserialize_json(data: dict) -> HierarchyFilterLevel:
    out: HierarchyFilterLevel = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("HierarchyFilterLevel.column required")
    return out
