"""Generated from Smithy shape ``com.amazonaws.cloudfront#ActiveTrustedKeyGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.kg_key_pair_ids_list


class ActiveTrustedKeyGroups(TypedDict, closed=True):
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>This field is <code>true</code> if any of the key groups have public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not, this field is <code>false</code>.</p>"""
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of key groups in the list.</p>"""
    items: NotRequired["capo_cloudfront.types.kg_key_pair_ids_list.KGKeyPairIdsList"]
    """<p>A list of key groups, including the identifiers of the public keys in each key group that CloudFront can use to verify the signatures of signed URLs and signed cookies.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ActiveTrustedKeyGroups, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.kg_key_pair_ids_list

        capo_cloudfront.types.kg_key_pair_ids_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> ActiveTrustedKeyGroups:
    out: ActiveTrustedKeyGroups = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.kg_key_pair_ids_list

        out["items"] = capo_cloudfront.types.kg_key_pair_ids_list.deserialize_xml(
            child_items
        )
    return out
