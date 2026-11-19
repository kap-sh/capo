"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetStatusCode``."""

from typing import Literal, TypeAlias, cast

FleetStatusCode: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ROTATING",
    "PENDING_DELETION",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_ROLLBACK_FAILED",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetStatusCode:
    return cast(FleetStatusCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetStatusCode) -> str:
    return value


def deserialize_cbor(data: str) -> FleetStatusCode:
    return cast(FleetStatusCode, data)
