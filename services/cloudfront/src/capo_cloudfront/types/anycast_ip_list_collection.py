"""Generated from Smithy shape ``com.amazonaws.cloudfront#AnycastIpListCollection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.anycast_ip_list_summaries
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class AnycastIpListCollection(TypedDict, closed=True):
    items: NotRequired[
        "capo_cloudfront.types.anycast_ip_list_summaries.AnycastIpListSummaries"
    ]
    """<p>Items in the Anycast static IP list collection. Each item is of the <a>AnycastIpListSummary</a> structure type.</p>"""
    marker: "capo_cloudfront.types.string.string"
    """<p>Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Indicates the next page of the Anycast static IP list collection. To get the next page of the list, use this value in the <code>Marker</code> field of your request.</p>"""
    max_items: "capo_cloudfront.types.integer.integer"
    """<p>The maximum number of Anycast static IP list collections that you want returned in the response.</p>"""
    is_truncated: "capo_cloudfront.types.boolean.boolean"
    """<p>If there are more items in the list collection than are in this response, this value is <code>true</code>.</p>"""
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The quantity of Anycast static IP lists in the collection.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnycastIpListCollection, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "items" in value:
        import capo_cloudfront.types.anycast_ip_list_summaries

        capo_cloudfront.types.anycast_ip_list_summaries.serialize_xml(
            value["items"], el, "Items"
        )
    SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "IsTruncated").text = "true" if value["is_truncated"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])


def deserialize_xml(el: Element) -> AnycastIpListCollection:
    out: AnycastIpListCollection = {}  # type: ignore[typeddict-item]
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.anycast_ip_list_summaries

        out["items"] = capo_cloudfront.types.anycast_ip_list_summaries.deserialize_xml(
            child_items
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    else:
        out["marker"] = ""
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_quantity = el.find("Quantity")
    if child_quantity is not None:
        out["quantity"] = int(child_quantity.text or "")
    else:
        out["quantity"] = 0
    return out
