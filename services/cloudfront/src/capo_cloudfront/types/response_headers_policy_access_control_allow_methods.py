"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicyAccessControlAllowMethods``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.access_control_allow_methods_list
    import capo_cloudfront.types.integer


class ResponseHeadersPolicyAccessControlAllowMethods(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of HTTP methods in the list.</p>"""
    items: "capo_cloudfront.types.access_control_allow_methods_list.AccessControlAllowMethodsList"
    """<p>The list of HTTP methods. Valid values are:</p> <ul> <li> <p> <code>GET</code> </p> </li> <li> <p> <code>DELETE</code> </p> </li> <li> <p> <code>HEAD</code> </p> </li> <li> <p> <code>OPTIONS</code> </p> </li> <li> <p> <code>PATCH</code> </p> </li> <li> <p> <code>POST</code> </p> </li> <li> <p> <code>PUT</code> </p> </li> <li> <p> <code>ALL</code> </p> </li> </ul> <p> <code>ALL</code> is a special value that includes all of the listed HTTP methods.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ResponseHeadersPolicyAccessControlAllowMethods, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import capo_cloudfront.types.access_control_allow_methods_list

    capo_cloudfront.types.access_control_allow_methods_list.serialize_xml(
        value["items"], el, "Items"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicyAccessControlAllowMethods:
    out: ResponseHeadersPolicyAccessControlAllowMethods = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.access_control_allow_methods_list

        out["items"] = (
            capo_cloudfront.types.access_control_allow_methods_list.deserialize_xml(
                child_items
            )
        )
    else:
        out["items"] = []
    return out
