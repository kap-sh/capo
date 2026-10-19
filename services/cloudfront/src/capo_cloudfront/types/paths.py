"""Generated from Smithy shape ``com.amazonaws.cloudfront#Paths``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.path_list


class Paths(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of invalidation paths specified for the objects that you want to invalidate.</p>"""
    items: NotRequired["capo_cloudfront.types.path_list.PathList"]
    """<p>A complex type that contains a list of the paths that you want to invalidate.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Paths, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.path_list

        capo_cloudfront.types.path_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Paths:
    out: Paths = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.path_list

        out["items"] = capo_cloudfront.types.path_list.deserialize_xml(child_items)
    return out
