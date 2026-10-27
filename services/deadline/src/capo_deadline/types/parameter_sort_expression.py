"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterSortExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.sort_order
    import capo_deadline.types.string


class ParameterSortExpression(TypedDict, closed=True):
    sort_order: "capo_deadline.types.sort_order.SortOrder"
    """The sort order for the parameter."""
    name: "capo_deadline.types.string.String"
    """The parameter name to sort by."""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSortExpression) -> dict:
    out: dict = {}
    import capo_deadline.types.sort_order

    out["sortOrder"] = capo_deadline.types.sort_order.serialize_json(
        value["sort_order"]
    )
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ParameterSortExpression:
    out: ParameterSortExpression = {}  # type: ignore[typeddict-item]
    if data.get("sortOrder") is not None:
        import capo_deadline.types.sort_order

        out["sort_order"] = capo_deadline.types.sort_order.deserialize_json(
            data["sortOrder"]
        )
    else:
        import typing

        out["sort_order"] = typing.cast("capo_deadline.types.sort_order.SortOrder", "")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
