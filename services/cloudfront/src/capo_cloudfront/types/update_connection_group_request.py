"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateConnectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string


class UpdateConnectionGroupRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID of the connection group.</p>"""
    ipv6_enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Enable IPv6 for the connection group. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6">Enable IPv6</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The value of the <code>ETag</code> header that you received when retrieving the connection group that you're updating.</p>"""
    anycast_ip_list_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the Anycast static IP list.</p>"""
    enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Whether the connection group is enabled.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateConnectionGroupRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "ipv6_enabled" in value:
        SubElement(el, "Ipv6Enabled").text = (
            "true" if value["ipv6_enabled"] else "false"
        )
    if "anycast_ip_list_id" in value:
        SubElement(el, "AnycastIpListId").text = str(value["anycast_ip_list_id"])
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> UpdateConnectionGroupRequest:
    out: UpdateConnectionGroupRequest = {}  # type: ignore[typeddict-item]
    child_ipv6_enabled = el.find("Ipv6Enabled")
    if child_ipv6_enabled is not None:
        out["ipv6_enabled"] = (child_ipv6_enabled.text or "").lower() == "true"
    child_anycast_ip_list_id = el.find("AnycastIpListId")
    if child_anycast_ip_list_id is not None:
        out["anycast_ip_list_id"] = str(child_anycast_ip_list_id.text or "")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
