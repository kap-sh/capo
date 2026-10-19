"""Generated from Smithy shape ``com.amazonaws.cloudfront#CachedMethods``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.methods_list


class CachedMethods(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of HTTP methods for which you want CloudFront to cache responses. Valid values are <code>2</code> (for caching responses to <code>GET</code> and <code>HEAD</code> requests) and <code>3</code> (for caching responses to <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code> requests).</p>"""
    items: "capo_cloudfront.types.methods_list.MethodsList"
    """<p>A complex type that contains the HTTP methods that you want CloudFront to cache responses to. Valid values for <code>CachedMethods</code> include <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code>, depending on which caching option you choose. For more information, see the preceding section.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CachedMethods, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import capo_cloudfront.types.methods_list

    capo_cloudfront.types.methods_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> CachedMethods:
    out: CachedMethods = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.methods_list

        out["items"] = capo_cloudfront.types.methods_list.deserialize_xml(child_items)
    else:
        out["items"] = []
    return out
