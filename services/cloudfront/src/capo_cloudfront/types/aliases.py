"""Generated from Smithy shape ``com.amazonaws.cloudfront#Aliases``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.alias_list
    import capo_cloudfront.types.integer


class Aliases(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of CNAME aliases, if any, that you want to associate with this distribution.</p>"""
    items: NotRequired["capo_cloudfront.types.alias_list.AliasList"]
    """<p>A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Aliases, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.alias_list

        capo_cloudfront.types.alias_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Aliases:
    out: Aliases = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.alias_list

        out["items"] = capo_cloudfront.types.alias_list.deserialize_xml(child_items)
    return out
