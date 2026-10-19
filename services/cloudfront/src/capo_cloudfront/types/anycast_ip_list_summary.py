"""Generated from Smithy shape ``com.amazonaws.cloudfront#AnycastIpListSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.anycast_ip_list_name
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.ip_address_type
    import capo_cloudfront.types.ipam_config
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class AnycastIpListSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The ID of the Anycast static IP list.</p>"""
    name: "capo_cloudfront.types.anycast_ip_list_name.AnycastIpListName"
    """<p>The name of the Anycast static IP list.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The deployment status of the Anycast static IP list. Valid values: Deployed, Deploying, or Failed.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the Anycast static IP list.</p>"""
    ip_count: "capo_cloudfront.types.integer.integer"
    """<p>The number of IP addresses in the Anycast static IP list.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The last time the Anycast static IP list was modified.</p>"""
    ip_address_type: NotRequired["capo_cloudfront.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the Anycast static IP list.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version (ETag value) of the Anycast static IP list.</p>"""
    ipam_config: NotRequired["capo_cloudfront.types.ipam_config.IpamConfig"]
    """<p>The IPAM configuration for the Anycast static IP list, that contains the quantity and list of IPAM CIDR configurations.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnycastIpListSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Status").text = str(value["status"])
    SubElement(el, "Arn").text = str(value["arn"])
    SubElement(el, "IpCount").text = str(value["ip_count"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    if "ip_address_type" in value:
        import capo_cloudfront.types.ip_address_type

        capo_cloudfront.types.ip_address_type.serialize_xml(
            value["ip_address_type"], el, "IpAddressType"
        )
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    if "ipam_config" in value:
        import capo_cloudfront.types.ipam_config

        capo_cloudfront.types.ipam_config.serialize_xml(
            value["ipam_config"], el, "IpamConfig"
        )


def deserialize_xml(el: Element) -> AnycastIpListSummary:
    out: AnycastIpListSummary = {}  # type: ignore[typeddict-item]
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
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_cloudfront.types.ip_address_type

        out["ip_address_type"] = capo_cloudfront.types.ip_address_type.deserialize_xml(
            child_ip_address_type
        )
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    child_ipam_config = el.find("IpamConfig")
    if child_ipam_config is not None:
        import capo_cloudfront.types.ipam_config

        out["ipam_config"] = capo_cloudfront.types.ipam_config.deserialize_xml(
            child_ipam_config
        )
    return out
