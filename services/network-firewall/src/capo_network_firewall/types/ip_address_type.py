"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IPAddressType``."""

from typing import Literal, TypeAlias, cast

IPAddressType: TypeAlias = Literal[
    "DUALSTACK",
    "IPV4",
    "IPV6",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IPAddressType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IPAddressType:
    return cast(IPAddressType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IPAddressType) -> str:
    return value


def deserialize_cbor(data: str) -> IPAddressType:
    return cast(IPAddressType, data)
