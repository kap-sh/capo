"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryConnectSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.dns_ip_addrs
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.subnet_ids
    import capo_directory_service.types.user_name
    import capo_directory_service.types.vpc_id


class DirectoryConnectSettings(TypedDict, closed=True):
    vpc_id: "capo_directory_service.types.vpc_id.VpcId"
    """<p>The identifier of the VPC in which the AD Connector is created.</p>"""
    subnet_ids: "capo_directory_service.types.subnet_ids.SubnetIds"
    """<p>A list of subnet identifiers in the VPC in which the AD Connector is created.</p>"""
    customer_dns_ips: "capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"
    """<p>The IP addresses of DNS servers or domain controllers in your self-managed directory.</p>"""
    customer_dns_ips_v6: NotRequired[
        "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>The IPv6 addresses of DNS servers or domain controllers in your self-managed directory.</p>"""
    customer_user_name: "capo_directory_service.types.user_name.UserName"
    """<p>The user name of an account in your self-managed directory that is used to connect to the directory. This account must have the following permissions:</p> <ul> <li> <p>Read users and groups</p> </li> <li> <p>Create computer objects</p> </li> <li> <p>Join computers to the domain</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryConnectSettings) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import capo_directory_service.types.subnet_ids

    out["SubnetIds"] = capo_directory_service.types.subnet_ids.serialize_aws_json_1_1(
        value["subnet_ids"]
    )
    import capo_directory_service.types.dns_ip_addrs

    out["CustomerDnsIps"] = (
        capo_directory_service.types.dns_ip_addrs.serialize_aws_json_1_1(
            value.get("customer_dns_ips", [])
        )
    )
    if "customer_dns_ips_v6" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["CustomerDnsIpsV6"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["customer_dns_ips_v6"]
            )
        )
    out["CustomerUserName"] = value["customer_user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryConnectSettings:
    out: DirectoryConnectSettings = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("SubnetIds") is not None:
        import capo_directory_service.types.subnet_ids

        out["subnet_ids"] = (
            capo_directory_service.types.subnet_ids.deserialize_aws_json_1_1(
                data["SubnetIds"]
            )
        )
    else:
        out["subnet_ids"] = []
    if data.get("CustomerDnsIps") is not None:
        import capo_directory_service.types.dns_ip_addrs

        out["customer_dns_ips"] = (
            capo_directory_service.types.dns_ip_addrs.deserialize_aws_json_1_1(
                data["CustomerDnsIps"]
            )
        )
    else:
        out["customer_dns_ips"] = []
    if data.get("CustomerDnsIpsV6") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["customer_dns_ips_v6"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["CustomerDnsIpsV6"]
            )
        )
    if data.get("CustomerUserName") is not None:
        out["customer_user_name"] = data["CustomerUserName"]
    else:
        out["customer_user_name"] = ""
    return out
