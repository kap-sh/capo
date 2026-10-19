"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.function_association_list
    import capo_cloudfront.types.integer


class FunctionAssociations(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of CloudFront functions in the list.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.function_association_list.FunctionAssociationList"
    ]
    """<p>The CloudFront functions that are associated with a cache behavior in a CloudFront distribution. Your functions must be published to the <code>LIVE</code> stage to associate them with a cache behavior.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FunctionAssociations, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.function_association_list

        capo_cloudfront.types.function_association_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> FunctionAssociations:
    out: FunctionAssociations = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.function_association_list

        out["items"] = capo_cloudfront.types.function_association_list.deserialize_xml(
            child_items
        )
    return out
