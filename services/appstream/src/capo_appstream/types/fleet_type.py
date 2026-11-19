"""Generated from Smithy shape ``com.amazonaws.appstream#FleetType``."""

from typing import Literal, TypeAlias, cast

FleetType: TypeAlias = Literal[
    "ALWAYS_ON",
    "ON_DEMAND",
    "ELASTIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetType:
    return cast(FleetType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetType) -> str:
    return value


def deserialize_cbor(data: str) -> FleetType:
    return cast(FleetType, data)
