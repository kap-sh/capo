"""Generated from Smithy shape ``com.amazonaws.cloudfront#Headers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.header_list
    import capo_cloudfront.types.integer


class Headers(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of header names in the <code>Items</code> list.</p>"""
    items: NotRequired["capo_cloudfront.types.header_list.HeaderList"]
    """<p>A list of HTTP header names.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Headers, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.header_list

        capo_cloudfront.types.header_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Headers:
    out: Headers = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.header_list

        out["items"] = capo_cloudfront.types.header_list.deserialize_xml(child_items)
    return out
