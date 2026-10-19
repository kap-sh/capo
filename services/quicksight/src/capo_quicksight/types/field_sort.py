"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.sort_direction


class FieldSort(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The sort configuration target field.</p>"""
    direction: "capo_quicksight.types.sort_direction.SortDirection"
    """<p>The sort direction. Choose one of the following options:</p> <ul> <li> <p> <code>ASC</code>: Ascending</p> </li> <li> <p> <code>DESC</code>: Descending</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSort) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.sort_direction

    out["Direction"] = capo_quicksight.types.sort_direction.serialize_json(
        value["direction"]
    )
    return out


def deserialize_json(data: dict) -> FieldSort:
    out: FieldSort = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Direction") is not None:
        import capo_quicksight.types.sort_direction

        out["direction"] = capo_quicksight.types.sort_direction.deserialize_json(
            data["Direction"]
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_quicksight.types.sort_direction.SortDirection", ""
        )
    return out
