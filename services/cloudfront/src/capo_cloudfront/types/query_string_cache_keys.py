"""Generated from Smithy shape ``com.amazonaws.cloudfront#QueryStringCacheKeys``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.query_string_cache_keys_list


class QueryStringCacheKeys(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of <code>whitelisted</code> query string parameters for a cache behavior.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.query_string_cache_keys_list.QueryStringCacheKeysList"
    ]
    """<p>A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If <code>Quantity</code> is 0, you can omit <code>Items</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: QueryStringCacheKeys, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.query_string_cache_keys_list

        capo_cloudfront.types.query_string_cache_keys_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> QueryStringCacheKeys:
    out: QueryStringCacheKeys = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.query_string_cache_keys_list

        out["items"] = (
            capo_cloudfront.types.query_string_cache_keys_list.deserialize_xml(
                child_items
            )
        )
    return out
