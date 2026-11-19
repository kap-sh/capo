"""Generated from Smithy shape ``com.amazonaws.snowball#ShippingOption``."""

from typing import Literal, TypeAlias, cast

ShippingOption: TypeAlias = Literal[
    "SECOND_DAY",
    "NEXT_DAY",
    "EXPRESS",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShippingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShippingOption:
    return cast(ShippingOption, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShippingOption) -> str:
    return value


def deserialize_cbor(data: str) -> ShippingOption:
    return cast(ShippingOption, data)
