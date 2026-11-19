"""Generated from Smithy shape ``com.amazonaws.snowball#ShippingLabelStatus``."""

from typing import Literal, TypeAlias, cast

ShippingLabelStatus: TypeAlias = Literal[
    "InProgress",
    "TimedOut",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShippingLabelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShippingLabelStatus:
    return cast(ShippingLabelStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShippingLabelStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ShippingLabelStatus:
    return cast(ShippingLabelStatus, data)
