"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetContextCode``."""

from typing import Literal, TypeAlias, cast

FleetContextCode: TypeAlias = Literal[
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "ACTION_REQUIRED",
    "PENDING_DELETION",
    "INSUFFICIENT_CAPACITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetContextCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetContextCode:
    return cast(FleetContextCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetContextCode) -> str:
    return value


def deserialize_cbor(data: str) -> FleetContextCode:
    return cast(FleetContextCode, data)
