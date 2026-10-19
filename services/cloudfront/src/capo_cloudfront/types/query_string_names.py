"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryStringNames``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.query_string_names_list


class QueryStringNames(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of query string names in the <code>Items</code> list.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.query_string_names_list.QueryStringNamesList"
    ]
    """<p>A list of query string names.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryStringNames, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.query_string_names_list

        capo_cloudfront.types.query_string_names_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> QueryStringNames:
    out: QueryStringNames = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.query_string_names_list

        out["items"] = capo_cloudfront.types.query_string_names_list.deserialize_xml(
            child_items
        )
    return out
