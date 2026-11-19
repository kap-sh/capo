"""Generated from Smithy shape ``com.amazonaws.appstream#FleetState``."""

from typing import Literal, TypeAlias, cast

FleetState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetState:
    return cast(FleetState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetState) -> str:
    return value


def deserialize_cbor(data: str) -> FleetState:
    return cast(FleetState, data)
