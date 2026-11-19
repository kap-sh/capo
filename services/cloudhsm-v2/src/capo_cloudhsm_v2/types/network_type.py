"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#NetworkType``."""

from typing import Literal, TypeAlias, cast

NetworkType: TypeAlias = Literal[
    "IPV4",
    "DUALSTACK",
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
