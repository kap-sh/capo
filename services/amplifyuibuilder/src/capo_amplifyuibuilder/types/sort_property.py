"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#SortProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.sort_direction


class SortProperty(TypedDict, closed=True):
    field: "str"
    """<p>The field to perform the sort on.</p>"""
    direction: "capo_amplifyuibuilder.types.sort_direction.SortDirection"
    """<p>The direction of the sort, either ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortProperty) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    import capo_amplifyuibuilder.types.sort_direction

    out["direction"] = capo_amplifyuibuilder.types.sort_direction.serialize_json(
        value["direction"]
    )
    return out


def deserialize_json(data: dict) -> SortProperty:
    out: SortProperty = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("direction") is not None:
        import capo_amplifyuibuilder.types.sort_direction

        out["direction"] = capo_amplifyuibuilder.types.sort_direction.deserialize_json(
            data["direction"]
        )
    else:
        import typing

        out["direction"] = typing.cast(
            "capo_amplifyuibuilder.types.sort_direction.SortDirection", ""
        )
    return out
