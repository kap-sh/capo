"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectableValuesSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.control_sort_direction


class SelectableValuesSort(TypedDict, closed=True):
    direction: "capo_quicksight.types.control_sort_direction.ControlSortDirection"
    """<p>The sort direction for the selectable values. Choose one of the following options:</p> <ul> <li> <p> <code>ASC</code>: Sort in ascending order.</p> </li> <li> <p> <code>DESC</code>: Sort in descending order.</p> </li> <li> <p> <code>USER_DEFINED_ORDER</code>: Preserve the order in which the values were entered.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectableValuesSort) -> dict:
    out: dict = {}
    import capo_quicksight.types.control_sort_direction

    out["Direction"] = capo_quicksight.types.control_sort_direction.serialize_json(
        value["direction"]
    )
    return out


def deserialize_json(data: dict) -> SelectableValuesSort:
    out: SelectableValuesSort = {}  # type: ignore[typeddict-item]
    if data.get("Direction") is not None:
        import capo_quicksight.types.control_sort_direction

        out["direction"] = (
            capo_quicksight.types.control_sort_direction.deserialize_json(
                data["Direction"]
            )
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_quicksight.types.control_sort_direction.ControlSortDirection", ""
        )
    return out
