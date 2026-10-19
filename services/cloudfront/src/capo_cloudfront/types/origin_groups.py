"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.origin_group_list


class OriginGroups(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of origin groups.</p>"""
    items: NotRequired["capo_cloudfront.types.origin_group_list.OriginGroupList"]
    """<p>The items (origin groups) in a distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginGroups, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.origin_group_list

        capo_cloudfront.types.origin_group_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> OriginGroups:
    out: OriginGroups = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.origin_group_list

        out["items"] = capo_cloudfront.types.origin_group_list.deserialize_xml(
            child_items
        )
    return out
