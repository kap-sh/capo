"""Generated from Smithy shape ``com.amazonaws.workspaces#DnsIpAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.ip_address

DnsIpAddresses: TypeAlias = list["capo_workspaces.types.ip_address.IpAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsIpAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DnsIpAddresses:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DnsIpAddresses) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DnsIpAddresses:
    return [item for item in data if item is not None]
