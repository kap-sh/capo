"""Generated from Smithy shape ``com.amazonaws.mailmanager#Ipv6Cidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.ipv6_cidr

Ipv6Cidrs: TypeAlias = list["capo_mailmanager.types.ipv6_cidr.Ipv6Cidr"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv6Cidrs) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Ipv6Cidrs:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Ipv6Cidrs) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Ipv6Cidrs:
    return [item for item in data if item is not None]
