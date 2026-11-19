"""Generated from Smithy shape ``com.amazonaws.memorydb#NetworkType``."""

from typing import Literal, TypeAlias, cast

NetworkType: TypeAlias = Literal[
    "ipv4",
    "ipv6",
    "dual_stack",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkType:
    return cast(NetworkType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkType) -> str:
    return value


def deserialize_cbor(data: str) -> NetworkType:
    return cast(NetworkType, data)
