"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.cidr_ip
    import capo_directory_service.types.cidr_ipv6
    import capo_directory_service.types.description


class IpRoute(TypedDict, closed=True):
    cidr_ip: NotRequired["capo_directory_service.types.cidr_ip.CidrIp"]
    """<p>IP address block in CIDR format, such as 10.0.0.0/24. This is often the address block of the DNS server used for your self-managed domain. For a single IP address, use a CIDR address block with /32. For example, 10.0.0.0/32.</p>"""
    cidr_ipv6: NotRequired["capo_directory_service.types.cidr_ipv6.CidrIpv6"]
    """<p>IPv6 address block in CIDR format, such as 2001:db8::/32. This is often the address block of the DNS server used for your self-managed domain. For a single IPv6 address, use a CIDR address block with /128. For example, 2001:db8::1/128.</p>"""
    description: NotRequired["capo_directory_service.types.description.Description"]
    """<p>Description of the address block.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRoute) -> dict:
    out: dict = {}
    if "cidr_ip" in value:
        out["CidrIp"] = value["cidr_ip"]
    if "cidr_ipv6" in value:
        out["CidrIpv6"] = value["cidr_ipv6"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpRoute:
    out: IpRoute = {}  # type: ignore[typeddict-item]
    if data.get("CidrIp") is not None:
        out["cidr_ip"] = data["CidrIp"]
    if data.get("CidrIpv6") is not None:
        out["cidr_ipv6"] = data["CidrIpv6"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRoute) -> dict:
    out: dict = {}
    if "cidr_ip" in value:
        out["CidrIp"] = value["cidr_ip"]
    if "cidr_ipv6" in value:
        out["CidrIpv6"] = value["cidr_ipv6"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> IpRoute:
    out: IpRoute = {}  # type: ignore[typeddict-item]
    if data.get("CidrIp") is not None:
        out["cidr_ip"] = data["CidrIp"]
    if data.get("CidrIpv6") is not None:
        out["cidr_ipv6"] = data["CidrIpv6"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
