"""Generated from Smithy shape ``com.amazonaws.snowball#AddressType``."""

from typing import Literal, TypeAlias, cast

AddressType: TypeAlias = Literal[
    "CUST_PICKUP",
    "AWS_SHIP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddressType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AddressType:
    return cast(AddressType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AddressType) -> str:
    return value


def deserialize_cbor(data: str) -> AddressType:
    return cast(AddressType, data)
