"""Generated from Smithy shape ``com.amazonaws.cloudfront#AnycastIpList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.anycast_ip_list_name
    import capo_cloudfront.types.anycast_ips
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.ip_address_type
    import capo_cloudfront.types.ipam_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class AnycastIpList(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID of the Anycast static IP list.</p>"""
    name: "capo_cloudfront.types.anycast_ip_list_name.AnycastIpListName"
    """<p>The name of the Anycast static IP list.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The status of the Anycast static IP list. Valid values: <code>Deployed</code>, <code>Deploying</code>, or <code>Failed</code>.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the Anycast static IP list.</p>"""
    ip_address_type: NotRequired["capo_cloudfront.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the Anycast static IP list.</p>"""
    ipam_config: NotRequired["capo_cloudfront.types.ipam_config.IpamConfig"]
    """<p>The IPAM configuration for the Anycast static IP list, that contains the quantity and list of IPAM CIDR configurations.</p>"""
    anycast_ips: "capo_cloudfront.types.anycast_ips.AnycastIps"
    """<p>The static IP addresses that are allocated to the Anycast static IP list.</p>"""
    ip_count: "capo_cloudfront.types.integer.integer"
    """<p>The number of IP addresses in the Anycast static IP list.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The last time the Anycast static IP list was modified.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnycastIpList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Status").text = str(value["status"])
    SubElement(el, "Arn").text = str(value["arn"])
    if "ip_address_type" in value:
        import capo_cloudfront.types.ip_address_type

        capo_cloudfront.types.ip_address_type.serialize_xml(
            value["ip_address_type"], el, "IpAddressType"
        )
    if "ipam_config" in value:
        import capo_cloudfront.types.ipam_config

        capo_cloudfront.types.ipam_config.serialize_xml(
            value["ipam_config"], el, "IpamConfig"
        )
    import capo_cloudfront.types.anycast_ips

    capo_cloudfront.types.anycast_ips.serialize_xml(
        value["anycast_ips"], el, "AnycastIps"
    )
    SubElement(el, "IpCount").text = str(value["ip_count"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )


def deserialize_xml(el: Element) -> AnycastIpList:
    out: AnycastIpList = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_cloudfront.types.ip_address_type

        out["ip_address_type"] = capo_cloudfront.types.ip_address_type.deserialize_xml(
            child_ip_address_type
        )
    child_ipam_config = el.find("IpamConfig")
    if child_ipam_config is not None:
        import capo_cloudfront.types.ipam_config

        out["ipam_config"] = capo_cloudfront.types.ipam_config.deserialize_xml(
            child_ipam_config
        )
    child_anycast_ips = el.find("AnycastIps")
    if child_anycast_ips is not None:
        import capo_cloudfront.types.anycast_ips

        out["anycast_ips"] = capo_cloudfront.types.anycast_ips.deserialize_xml(
            child_anycast_ips
        )
    else:
        out["anycast_ips"] = []
    child_ip_count = el.find("IpCount")
    if child_ip_count is not None:
        out["ip_count"] = int(child_ip_count.text or "")
    else:
        out["ip_count"] = 0
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
