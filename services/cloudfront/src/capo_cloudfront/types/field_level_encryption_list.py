"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldLevelEncryptionList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.field_level_encryption_summary_list
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class FieldLevelEncryptionList(TypedDict, closed=True):
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>If there are more elements to be listed, this element is present and contains the value that you can use for the <code>Marker</code> request parameter to continue listing your configurations where you left off.</p>"""
    max_items: "capo_cloudfront.types.integer.integer"
    """<p>The maximum number of elements you want in the response body.</p>"""
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of field-level encryption items.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.field_level_encryption_summary_list.FieldLevelEncryptionSummaryList"
    ]
    """<p>An array of field-level encryption items.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FieldLevelEncryptionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.field_level_encryption_summary_list

        capo_cloudfront.types.field_level_encryption_summary_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> FieldLevelEncryptionList:
    out: FieldLevelEncryptionList = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.field_level_encryption_summary_list

        out["items"] = (
            capo_cloudfront.types.field_level_encryption_summary_list.deserialize_xml(
                child_items
            )
        )
    return out
