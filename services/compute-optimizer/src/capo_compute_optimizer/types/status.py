"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "Active",
    "Inactive",
    "Pending",
    "Failed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Status) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Status:
    return cast(Status, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Status) -> str:
    return value


def deserialize_cbor(data: str) -> Status:
    return cast(Status, data)
