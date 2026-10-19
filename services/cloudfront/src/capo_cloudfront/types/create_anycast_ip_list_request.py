"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateAnycastIpListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.anycast_ip_list_name
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.ip_address_type
    import capo_cloudfront.types.ipam_cidr_config_list
    import capo_cloudfront.types.tags


class CreateAnycastIpListRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.anycast_ip_list_name.AnycastIpListName"
    """<p>Name of the Anycast static IP list.</p>"""
    ip_count: "capo_cloudfront.types.integer.integer"
    """<p>The number of static IP addresses that are allocated to the Anycast static IP list. Valid values: 21 or 3.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]
    ip_address_type: NotRequired["capo_cloudfront.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the Anycast static IP list. You can specify one of the following options:</p> <ul> <li> <p> <code>ipv4</code> only</p> </li> <li> <p> <code>ipv6</code> only </p> </li> <li> <p> <code>dualstack</code> - Allocate a list of both IPv4 and IPv6 addresses</p> </li> </ul>"""
    ipam_cidr_configs: NotRequired[
        "capo_cloudfront.types.ipam_cidr_config_list.IpamCidrConfigList"
    ]
    """<p> A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for creating the Anycast static IP list. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateAnycastIpListRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "IpCount").text = str(value["ip_count"])
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")
    if "ip_address_type" in value:
        import capo_cloudfront.types.ip_address_type

        capo_cloudfront.types.ip_address_type.serialize_xml(
            value["ip_address_type"], el, "IpAddressType"
        )
    if "ipam_cidr_configs" in value:
        import capo_cloudfront.types.ipam_cidr_config_list

        capo_cloudfront.types.ipam_cidr_config_list.serialize_xml(
            value["ipam_cidr_configs"], el, "IpamCidrConfigs"
        )


def deserialize_xml(el: Element) -> CreateAnycastIpListRequest:
    out: CreateAnycastIpListRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_ip_count = el.find("IpCount")
    if child_ip_count is not None:
        out["ip_count"] = int(child_ip_count.text or "")
    else:
        out["ip_count"] = 0
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_cloudfront.types.ip_address_type

        out["ip_address_type"] = capo_cloudfront.types.ip_address_type.deserialize_xml(
            child_ip_address_type
        )
    child_ipam_cidr_configs = el.find("IpamCidrConfigs")
    if child_ipam_cidr_configs is not None:
        import capo_cloudfront.types.ipam_cidr_config_list

        out["ipam_cidr_configs"] = (
            capo_cloudfront.types.ipam_cidr_config_list.deserialize_xml(
                child_ipam_cidr_configs
            )
        )
    return out
