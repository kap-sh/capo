"""Generated from Smithy shape ``com.amazonaws.cloudfront#Origins``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.origin_list


class Origins(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of origins for this distribution.</p>"""
    items: "capo_cloudfront.types.origin_list.OriginList"
    """<p>A list of origins.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Origins, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    import capo_cloudfront.types.origin_list

    capo_cloudfront.types.origin_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Origins:
    out: Origins = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        raise DeserializationError("Origins.quantity required")
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.origin_list

        out["items"] = capo_cloudfront.types.origin_list.deserialize_xml(child_items)
    else:
        raise DeserializationError("Origins.items required")
    return out


def redact_sensitive(value: Origins) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_cloudfront.types.origin_list

        out["items"] = capo_cloudfront.types.origin_list.redact_sensitive(
            value["items"]
        )
    return out
