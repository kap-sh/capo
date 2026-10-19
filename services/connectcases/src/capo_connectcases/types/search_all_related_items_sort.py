"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.order
    import capo_connectcases.types.search_all_related_items_sort_property


class SearchAllRelatedItemsSort(TypedDict, closed=True):
    sort_property: "capo_connectcases.types.search_all_related_items_sort_property.SearchAllRelatedItemsSortProperty"
    """<p>Whether related items should be sorted in ascending or descending order. </p>"""
    sort_order: "capo_connectcases.types.order.Order"
    """<p>Whether related items should be sorted by association time or case ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsSort) -> dict:
    out: dict = {}
    out["sortProperty"] = value["sort_property"]
    out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsSort:
    out: SearchAllRelatedItemsSort = {}  # type: ignore[typeddict-item]
    if data.get("sortProperty") is not None:
        out["sort_property"] = data["sortProperty"]
    else:
        out["sort_property"] = ""
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    else:
        out["sort_order"] = ""
    return out
