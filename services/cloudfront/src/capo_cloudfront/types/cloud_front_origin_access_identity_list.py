"""Generated from Smithy shape ``com.amazonaws.cloudfront#CloudFrontOriginAccessIdentityList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.cloud_front_origin_access_identity_summary_list
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string


class CloudFrontOriginAccessIdentityList(TypedDict, closed=True):
    marker: "capo_cloudfront.types.string.string"
    """<p>Use this when paginating results to indicate where to begin in your list of origin access identities. The results include identities in the list that occur after the marker. To get the next page of results, set the <code>Marker</code> to the value of the <code>NextMarker</code> from the current page's response (which is also the ID of the last identity on that page).</p>"""
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>If <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value you can use for the <code>Marker</code> request parameter to continue listing your origin access identities where they left off.</p>"""
    max_items: "capo_cloudfront.types.integer.integer"
    """<p>The maximum number of origin access identities you want in the response body.</p>"""
    is_truncated: "capo_cloudfront.types.boolean.boolean"
    """<p>A flag that indicates whether more origin access identities remain to be listed. If your results were truncated, you can make a follow-up pagination request using the <code>Marker</code> request parameter to retrieve more items in the list.</p>"""
    quantity: "capo_cloudfront.types.integer.integer"
    """<p>The number of CloudFront origin access identities that were created by the current Amazon Web Services account.</p>"""
    items: NotRequired[
        "capo_cloudfront.types.cloud_front_origin_access_identity_summary_list.CloudFrontOriginAccessIdentitySummaryList"
    ]
    """<p>A complex type that contains one <code>CloudFrontOriginAccessIdentitySummary</code> element for each origin access identity that was created by the current Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CloudFrontOriginAccessIdentityList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Marker").text = str(value["marker"])
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    SubElement(el, "MaxItems").text = str(value["max_items"])
    SubElement(el, "IsTruncated").text = "true" if value["is_truncated"] else "false"
    SubElement(el, "Quantity").text = str(value["quantity"])
    if "items" in value:
        import capo_cloudfront.types.cloud_front_origin_access_identity_summary_list

        capo_cloudfront.types.cloud_front_origin_access_identity_summary_list.serialize_xml(
            value["items"], el, "Items"
        )


def deserialize_xml(el: Element) -> CloudFrontOriginAccessIdentityList:
    out: CloudFrontOriginAccessIdentityList = {}  # type: ignore[typeddict-item]
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
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.cloud_front_origin_access_identity_summary_list

        out["items"] = (
            capo_cloudfront.types.cloud_front_origin_access_identity_summary_list.deserialize_xml(
                child_items
            )
        )
    return out
