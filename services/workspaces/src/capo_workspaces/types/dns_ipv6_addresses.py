"""Generated from Smithy shape ``com.amazonaws.workspaces#DnsIpv6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.ipv6_address

DnsIpv6Addresses: TypeAlias = list["capo_workspaces.types.ipv6_address.Ipv6Address"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpv6Addresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpv6Addresses:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnsIpv6Addresses) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DnsIpv6Addresses:
    return [item for item in data if item is not None]
