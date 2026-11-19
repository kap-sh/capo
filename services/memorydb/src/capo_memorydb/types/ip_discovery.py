"""Generated from Smithy shape ``com.amazonaws.memorydb#IpDiscovery``."""

from typing import Literal, TypeAlias, cast

IpDiscovery: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpDiscovery) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpDiscovery:
    return cast(IpDiscovery, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpDiscovery) -> str:
    return value


def deserialize_cbor(data: str) -> IpDiscovery:
    return cast(IpDiscovery, data)
