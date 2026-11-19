"""Generated from Smithy shape ``com.amazonaws.directconnect#AddressFamily``."""

from typing import Literal, TypeAlias, cast

AddressFamily: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddressFamily) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AddressFamily:
    return cast(AddressFamily, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AddressFamily) -> str:
    return value


def deserialize_cbor(data: str) -> AddressFamily:
    return cast(AddressFamily, data)
