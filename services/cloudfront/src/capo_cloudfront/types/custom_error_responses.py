"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomErrorResponses``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.custom_error_response_list
    import capo_cloudfront.types.integer


class CustomErrorResponses(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.custom_error_response_list.CustomErrorResponseList"
    ]
    """<p>A complex type that contains a <code>CustomErrorResponse</code> element for each HTTP status code for which you want to specify a custom error page and/or a caching duration. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: CustomErrorResponses, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.custom_error_response_list

        capo_cloudfront.types.custom_error_response_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> CustomErrorResponses:
    out: CustomErrorResponses = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.custom_error_response_list

        out["items"] = capo_cloudfront.types.custom_error_response_list.deserialize_xml(
            child_items
        )
    return out
