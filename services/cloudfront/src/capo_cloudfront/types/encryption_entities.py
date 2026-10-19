"""Generated from Smithy shape ``com.amazonaws.cloudfront#EncryptionEntities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.encryption_entity_list
    import capo_cloudfront.types.integer


class EncryptionEntities(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>Number of field pattern items in a field-level encryption content type-profile mapping.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.encryption_entity_list.EncryptionEntityList"
    ]
    """<p>An array of field patterns in a field-level encryption content type-profile mapping. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: EncryptionEntities, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.encryption_entity_list

        capo_cloudfront.types.encryption_entity_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> EncryptionEntities:
    out: EncryptionEntities = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.encryption_entity_list

        out["items"] = capo_cloudfront.types.encryption_entity_list.deserialize_xml(
            child_items
        )
    return out
