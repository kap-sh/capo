"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyPairIds``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.key_pair_id_list


class KeyPairIds(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of key pair identifiers in the list.</p>"""
    items: NotRequired["capo_cloudfront.types.key_pair_id_list.KeyPairIdList"]
    """<p>A list of CloudFront key pair identifiers.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyPairIds, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.key_pair_id_list

        capo_cloudfront.types.key_pair_id_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> KeyPairIds:
    out: KeyPairIds = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.key_pair_id_list

        out["items"] = capo_cloudfront.types.key_pair_id_list.deserialize_xml(
            child_items
        )
    return out
