"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlAllowHeaders``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.access_control_allow_headers_list
    import capo_cloudfront.types.integer


class ResponseHeadersPolicyAccessControlAllowHeaders(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of HTTP header names in the list.</p>"""
    items: "capo_cloudfront.types.access_control_allow_headers_list.AccessControlAllowHeadersList"
    """<p>The list of HTTP header names. You can specify <code>*</code> to allow all headers.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyAccessControlAllowHeaders, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import capo_cloudfront.types.access_control_allow_headers_list

    capo_cloudfront.types.access_control_allow_headers_list.serialize_xml(
        value["items"], el, "Items"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyAccessControlAllowHeaders:
    out: ResponseHeadersPolicyAccessControlAllowHeaders = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.access_control_allow_headers_list

        out["items"] = (
            capo_cloudfront.types.access_control_allow_headers_list.deserialize_xml(
                child_items
            )
        )
    else:
        out["items"] = []
    return out
