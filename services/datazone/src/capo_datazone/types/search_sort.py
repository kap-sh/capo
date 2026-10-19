"""Generated from Smithy shape ``com.amazonaws.datazone#SearchSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute
    import capo_datazone.types.sort_order


class SearchSort(TypedDict, closed=True):
    attribute: "capo_datazone.types.attribute.Attribute"
    """<p>The attribute detail of the way to sort search results.</p>"""
    order: NotRequired["capo_datazone.types.sort_order.SortOrder"]
    """<p>The order detail of the wya to sort search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSort) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    if "order" in value:
        import capo_datazone.types.sort_order

        out["order"] = capo_datazone.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> SearchSort:
    out: SearchSort = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        out["attribute"] = data["attribute"]
    else:
        out["attribute"] = ""
    if data.get("order") is not None:
        import capo_datazone.types.sort_order

        out["order"] = capo_datazone.types.sort_order.deserialize_json(data["order"])
    return out
