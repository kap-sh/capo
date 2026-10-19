"""Generated from Smithy shape ``com.amazonaws.cloudfront#CustomHeaders``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.origin_custom_headers_list


class CustomHeaders(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of custom headers, if any, for this distribution.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.origin_custom_headers_list.OriginCustomHeadersList"
    ]
    """<p> <b>Optional</b>: A list that contains one <code>OriginCustomHeader</code> element for each custom header that you want CloudFront to forward to the origin. If Quantity is <code>0</code>, omit <code>Items</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CustomHeaders, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.origin_custom_headers_list

        capo_cloudfront.types.origin_custom_headers_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> CustomHeaders:
    out: CustomHeaders = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.origin_custom_headers_list

        out["items"] = capo_cloudfront.types.origin_custom_headers_list.deserialize_xml(
            child_items
        )
    return out


def redact_sensitive(value: CustomHeaders) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_cloudfront.types.origin_custom_headers_list

        out["items"] = (
            capo_cloudfront.types.origin_custom_headers_list.redact_sensitive(
                value["items"]
            )
        )
    return out
