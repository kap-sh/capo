"""Generated from Smithy shape ``com.amazonaws.snowball#ShipmentState``."""

from typing import Literal, TypeAlias, cast

ShipmentState: TypeAlias = Literal[
    "RECEIVED",
    "RETURNED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShipmentState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShipmentState:
    return cast(ShipmentState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShipmentState) -> str:
    return value


def deserialize_cbor(data: str) -> ShipmentState:
    return cast(ShipmentState, data)
