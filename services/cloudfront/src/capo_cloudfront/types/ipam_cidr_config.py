"""Generated from Smithy shape ``com.amazonaws.cloudfront#IpamCidrConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.ipam_cidr_status
    import capo_cloudfront.types.string


class IpamCidrConfig(TypedDict, closed=True):
    cidr: "capo_cloudfront.types.string.string"
    """<p>The CIDR that specifies the IP address range for this IPAM configuration.</p>"""
    ipam_pool_arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the IPAM pool that the CIDR block is assigned to.</p>"""
    anycast_ip: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The specified Anycast IP address allocated from the IPAM pool for this CIDR configuration.</p>"""
    status: NotRequired["capo_cloudfront.types.ipam_cidr_status.IpamCidrStatus"]
    """<p>The current status of the IPAM CIDR configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: IpamCidrConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Cidr").text = str(value["cidr"])
    SubElement(el, "IpamPoolArn").text = str(value["ipam_pool_arn"])
    if "anycast_ip" in value:
        SubElement(el, "AnycastIp").text = str(value["anycast_ip"])
    if "status" in value:
        import capo_cloudfront.types.ipam_cidr_status

        capo_cloudfront.types.ipam_cidr_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> IpamCidrConfig:
    out: IpamCidrConfig = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    else:
        out["cidr"] = ""
    child_ipam_pool_arn = el.find("IpamPoolArn")
    if child_ipam_pool_arn is not None:
        out["ipam_pool_arn"] = str(child_ipam_pool_arn.text or "")
    else:
        out["ipam_pool_arn"] = ""
    child_anycast_ip = el.find("AnycastIp")
    if child_anycast_ip is not None:
        out["anycast_ip"] = str(child_anycast_ip.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudfront.types.ipam_cidr_status

        out["status"] = capo_cloudfront.types.ipam_cidr_status.deserialize_xml(
            child_status
        )
    return out
