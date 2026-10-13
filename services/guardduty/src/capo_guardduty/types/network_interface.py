"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkInterface``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.ipv6_addresses
    import capo_guardduty.types.private_ip_addresses
    import capo_guardduty.types.security_groups
    import capo_guardduty.types.sensitive_string
    import capo_guardduty.types.string


class NetworkInterface(TypedDict, closed=True):
    ipv6_addresses: NotRequired["capo_guardduty.types.ipv6_addresses.Ipv6Addresses"]
    """<p>A list of IPv6 addresses for the EC2 instance.</p>"""
    network_interface_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    private_dns_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The private DNS name of the EC2 instance.</p>"""
    private_ip_address: NotRequired[
        "capo_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The private IP address of the EC2 instance.</p>"""
    private_ip_addresses: NotRequired[
        "capo_guardduty.types.private_ip_addresses.PrivateIpAddresses"
    ]
    """<p>Other private IP address information of the EC2 instance.</p>"""
    public_dns_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The public DNS name of the EC2 instance.</p>"""
    public_ip: NotRequired["capo_guardduty.types.string.String"]
    """<p>The public IP address of the EC2 instance.</p>"""
    security_groups: NotRequired["capo_guardduty.types.security_groups.SecurityGroups"]
    """<p>The security groups associated with the EC2 instance.</p>"""
    subnet_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The subnet ID of the EC2 instance.</p>"""
    vpc_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The VPC ID of the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterface) -> dict:
    out: dict = {}
    if "ipv6_addresses" in value:
        import capo_guardduty.types.ipv6_addresses

        out["ipv6Addresses"] = capo_guardduty.types.ipv6_addresses.serialize_json(
            value["ipv6_addresses"]
        )
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    if "private_dns_name" in value:
        out["privateDnsName"] = value["private_dns_name"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "private_ip_addresses" in value:
        import capo_guardduty.types.private_ip_addresses

        out["privateIpAddresses"] = (
            capo_guardduty.types.private_ip_addresses.serialize_json(
                value["private_ip_addresses"]
            )
        )
    if "public_dns_name" in value:
        out["publicDnsName"] = value["public_dns_name"]
    if "public_ip" in value:
        out["publicIp"] = value["public_ip"]
    if "security_groups" in value:
        import capo_guardduty.types.security_groups

        out["securityGroups"] = capo_guardduty.types.security_groups.serialize_json(
            value["security_groups"]
        )
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("ipv6Addresses") is not None:
        import capo_guardduty.types.ipv6_addresses

        out["ipv6_addresses"] = capo_guardduty.types.ipv6_addresses.deserialize_json(
            data["ipv6Addresses"]
        )
    if data.get("networkInterfaceId") is not None:
        out["network_interface_id"] = data["networkInterfaceId"]
    if data.get("privateDnsName") is not None:
        out["private_dns_name"] = data["privateDnsName"]
    if data.get("privateIpAddress") is not None:
        out["private_ip_address"] = data["privateIpAddress"]
    if data.get("privateIpAddresses") is not None:
        import capo_guardduty.types.private_ip_addresses

        out["private_ip_addresses"] = (
            capo_guardduty.types.private_ip_addresses.deserialize_json(
                data["privateIpAddresses"]
            )
        )
    if data.get("publicDnsName") is not None:
        out["public_dns_name"] = data["publicDnsName"]
    if data.get("publicIp") is not None:
        out["public_ip"] = data["publicIp"]
    if data.get("securityGroups") is not None:
        import capo_guardduty.types.security_groups

        out["security_groups"] = capo_guardduty.types.security_groups.deserialize_json(
            data["securityGroups"]
        )
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    return out


def redact_sensitive(value: NetworkInterface) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_ip_address" in value:
        out["private_ip_address"] = "*** Sensitive Data Redacted ***"
    if "private_ip_addresses" in value:
        import capo_guardduty.types.private_ip_addresses

        out["private_ip_addresses"] = (
            capo_guardduty.types.private_ip_addresses.redact_sensitive(
                value["private_ip_addresses"]
            )
        )
    return out
