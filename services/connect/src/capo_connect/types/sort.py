"""Generated from Smithy shape ``com.amazonaws.connect#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.sort_order
    import capo_connect.types.sortable_field_name


class Sort(TypedDict, closed=True):
    field_name: "capo_connect.types.sortable_field_name.SortableFieldName"
    """<p>The name of the field on which to sort.</p>"""
    order: "capo_connect.types.sort_order.SortOrder"
    """<p>An ascending or descending sort.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    import capo_connect.types.sortable_field_name

    out["FieldName"] = capo_connect.types.sortable_field_name.serialize_json(
        value["field_name"]
    )
    import capo_connect.types.sort_order

    out["Order"] = capo_connect.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if data.get("FieldName") is not None:
        import capo_connect.types.sortable_field_name

        out["field_name"] = capo_connect.types.sortable_field_name.deserialize_json(
            data["FieldName"]
        )
    else:
        import typing

        out["field_name"] = typing.cast(
            "capo_connect.types.sortable_field_name.SortableFieldName", ""
        )
    if data.get("Order") is not None:
        import capo_connect.types.sort_order

        out["order"] = capo_connect.types.sort_order.deserialize_json(data["Order"])
    else:
        import typing

        out["order"] = typing.cast("capo_connect.types.sort_order.SortOrder", "")
    return out
