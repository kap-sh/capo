"""Generated from Smithy shape ``com.amazonaws.gamelift#FleetStatus``."""

from typing import Literal, TypeAlias, cast

FleetStatus: TypeAlias = Literal[
    "NEW",
    "DOWNLOADING",
    "VALIDATING",
    "BUILDING",
    "ACTIVATING",
    "ACTIVE",
    "DELETING",
    "ERROR",
    "TERMINATED",
    "NOT_FOUND",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetStatus:
    return cast(FleetStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetStatus) -> str:
    return value


def deserialize_cbor(data: str) -> FleetStatus:
    return cast(FleetStatus, data)
