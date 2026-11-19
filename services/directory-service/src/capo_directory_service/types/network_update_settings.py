"""Generated from Smithy shape ``com.amazonaws.directoryservice#NetworkUpdateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.network_type


class NetworkUpdateSettings(TypedDict, closed=True):
    network_type: NotRequired["capo_directory_service.types.network_type.NetworkType"]
    """<p>The target network type for the directory update.</p>"""
    customer_dns_ips_v6: NotRequired[
        "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
    ]
    """<p>IPv6 addresses of DNS servers or domain controllers in the self-managed directory. Required only when updating an AD Connector directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkUpdateSettings) -> dict:
    out: dict = {}
    if "network_type" in value:
        import capo_directory_service.types.network_type

        out["NetworkType"] = (
            capo_directory_service.types.network_type.serialize_aws_json_1_1(
                value["network_type"]
            )
        )
    if "customer_dns_ips_v6" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["CustomerDnsIpsV6"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_aws_json_1_1(
                value["customer_dns_ips_v6"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkUpdateSettings:
    out: NetworkUpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("NetworkType") is not None:
        import capo_directory_service.types.network_type

        out["network_type"] = (
            capo_directory_service.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    if data.get("CustomerDnsIpsV6") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["customer_dns_ips_v6"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_aws_json_1_1(
                data["CustomerDnsIpsV6"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkUpdateSettings) -> dict:
    out: dict = {}
    if "network_type" in value:
        import capo_directory_service.types.network_type

        out["NetworkType"] = capo_directory_service.types.network_type.serialize_cbor(
            value["network_type"]
        )
    if "customer_dns_ips_v6" in value:
        import capo_directory_service.types.dns_ipv6_addrs

        out["CustomerDnsIpsV6"] = (
            capo_directory_service.types.dns_ipv6_addrs.serialize_cbor(
                value["customer_dns_ips_v6"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> NetworkUpdateSettings:
    out: NetworkUpdateSettings = {}  # type: ignore[typeddict-item]
    if data.get("NetworkType") is not None:
        import capo_directory_service.types.network_type

        out["network_type"] = (
            capo_directory_service.types.network_type.deserialize_cbor(
                data["NetworkType"]
            )
        )
    if data.get("CustomerDnsIpsV6") is not None:
        import capo_directory_service.types.dns_ipv6_addrs

        out["customer_dns_ips_v6"] = (
            capo_directory_service.types.dns_ipv6_addrs.deserialize_cbor(
                data["CustomerDnsIpsV6"]
            )
        )
    return out
