"""Generated from Smithy shape ``com.amazonaws.fms#ResourceSetStatus``."""

from typing import Literal, TypeAlias, cast

ResourceSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "OUT_OF_ADMIN_SCOPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceSetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceSetStatus:
    return cast(ResourceSetStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceSetStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceSetStatus:
    return cast(ResourceSetStatus, data)
