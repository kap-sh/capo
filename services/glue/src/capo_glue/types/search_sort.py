"""Generated from Smithy shape ``com.amazonaws.glue#SearchSort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.search_attribute
    import capo_glue.types.search_sort_order


class SearchSort(TypedDict, closed=True):
    attribute: "capo_glue.types.search_attribute.SearchAttribute"
    """<p>The attribute to sort by.</p>"""
    order: NotRequired["capo_glue.types.search_sort_order.SearchSortOrder"]
    """<p>The sort order. Valid values are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSort) -> dict:
    out: dict = {}
    out["Attribute"] = value["attribute"]
    if "order" in value:
        import capo_glue.types.search_sort_order

        out["Order"] = capo_glue.types.search_sort_order.serialize_aws_json_1_1(
            value["order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchSort:
    out: SearchSort = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        out["attribute"] = data["Attribute"]
    else:
        out["attribute"] = ""
    if data.get("Order") is not None:
        import capo_glue.types.search_sort_order

        out["order"] = capo_glue.types.search_sort_order.deserialize_aws_json_1_1(
            data["Order"]
        )
    return out
