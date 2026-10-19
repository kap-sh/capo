"""Generated from Smithy shape ``com.amazonaws.cloudfront#StatusCodes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.status_code_list


class StatusCodes(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of status codes.</p>"""
    items: "capo_cloudfront.types.status_code_list.StatusCodeList"
    """<p>The items (status codes) for an origin group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StatusCodes, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import capo_cloudfront.types.status_code_list

    capo_cloudfront.types.status_code_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> StatusCodes:
    out: StatusCodes = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.status_code_list

        out["items"] = capo_cloudfront.types.status_code_list.deserialize_xml(
            child_items
        )
    else:
        out["items"] = []
    return out
