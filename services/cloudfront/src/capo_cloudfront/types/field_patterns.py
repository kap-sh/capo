"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldPatterns``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.field_pattern_list
    import capo_cloudfront.types.integer


class FieldPatterns(TypedDict, closed=True):
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of field-level encryption field patterns.</p>"""
    items: NotRequired["capo_cloudfront.types.field_pattern_list.FieldPatternList"]
    """<p>An array of the field-level encryption field patterns.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FieldPatterns, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.field_pattern_list

        capo_cloudfront.types.field_pattern_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> FieldPatterns:
    out: FieldPatterns = {}  # type: ignore[typeddict-item]
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.field_pattern_list

        out["items"] = capo_cloudfront.types.field_pattern_list.deserialize_xml(
            child_items
        )
    return out
