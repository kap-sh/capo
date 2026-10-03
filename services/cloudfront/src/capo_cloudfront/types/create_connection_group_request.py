"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateConnectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.string
    import capo_cloudfront.types.tags


class CreateConnectionGroupRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>The name of the connection group. Enter a friendly identifier that is unique within your Amazon Web Services account. This name can't be updated after you create the connection group.</p>"""
    ipv6_enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Enable IPv6 for the connection group. The default is <code>true</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6">Enable IPv6</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]
    anycast_ip_list_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The ID of the Anycast static IP list.</p>"""
    enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Enable the connection group.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateConnectionGroupRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    if "ipv6_enabled" in value:
        SubElement(el, "Ipv6Enabled").text = (
            "true" if value["ipv6_enabled"] else "false"
        )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")
    if "anycast_ip_list_id" in value:
        SubElement(el, "AnycastIpListId").text = str(value["anycast_ip_list_id"])
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"


def deserialize_xml(el: Element) -> CreateConnectionGroupRequest:
    out: CreateConnectionGroupRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateConnectionGroupRequest.name required")
    child_ipv6_enabled = el.find("Ipv6Enabled")
    if child_ipv6_enabled is not None:
        out["ipv6_enabled"] = (child_ipv6_enabled.text or "").lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    child_anycast_ip_list_id = el.find("AnycastIpListId")
    if child_anycast_ip_list_id is not None:
        out["anycast_ip_list_id"] = str(child_anycast_ip_list_id.text or "")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
