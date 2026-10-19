"""Generated from Smithy shape ``com.amazonaws.cloudfront#AllowedMethods``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cached_methods
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.methods_list


class AllowedMethods(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for <code>GET</code> and <code>HEAD</code> requests), 3 (for <code>GET</code>, <code>HEAD</code>, and <code>OPTIONS</code> requests) and 7 (for <code>GET, HEAD, OPTIONS, PUT, PATCH, POST</code>, and <code>DELETE</code> requests).</p>"""
    items: "capo_cloudfront.types.methods_list.MethodsList"
    """<p>A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.</p>"""
    cached_methods: NotRequired["capo_cloudfront.types.cached_methods.CachedMethods"]


# --- restXml ser/de ---
def serialize_xml(value: AllowedMethods, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import capo_cloudfront.types.methods_list

    capo_cloudfront.types.methods_list.serialize_xml(value["items"], el, "Items")
    if "cached_methods" in value:
        import capo_cloudfront.types.cached_methods

        capo_cloudfront.types.cached_methods.serialize_xml(
            value["cached_methods"], el, "CachedMethods"
        )


def deserialize_xml(el: Element) -> AllowedMethods:
    out: AllowedMethods = {}  # type: ignore[typeddict-item]
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
    child_cached_methods = el.find("CachedMethods")
    if child_cached_methods is not None:
        import capo_cloudfront.types.cached_methods

        out["cached_methods"] = capo_cloudfront.types.cached_methods.deserialize_xml(
            child_cached_methods
        )
    return out
