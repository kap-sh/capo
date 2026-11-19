"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetOverflowBehavior``."""

from typing import Literal, TypeAlias, cast

FleetOverflowBehavior: TypeAlias = Literal[
    "QUEUE",
    "ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetOverflowBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetOverflowBehavior:
    return cast(FleetOverflowBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetOverflowBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> FleetOverflowBehavior:
    return cast(FleetOverflowBehavior, data)
