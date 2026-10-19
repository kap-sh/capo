"""Generated from Smithy shape ``com.amazonaws.cloudfront#CacheBehaviors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_behavior_list
    import capo_cloudfront.types.integer


class CacheBehaviors(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of cache behaviors for this distribution.</p>"""
    items: NotRequired["capo_cloudfront.types.cache_behavior_list.CacheBehaviorList"]
    """<p>Optional: A complex type that contains cache behaviors for this distribution. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CacheBehaviors, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.cache_behavior_list

        capo_cloudfront.types.cache_behavior_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> CacheBehaviors:
    out: CacheBehaviors = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.cache_behavior_list

        out["items"] = capo_cloudfront.types.cache_behavior_list.deserialize_xml(
            child_items
        )
    return out
