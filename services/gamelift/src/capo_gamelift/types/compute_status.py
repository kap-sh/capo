"""Generated from Smithy shape ``com.amazonaws.gamelift#ComputeStatus``."""

from typing import Literal, TypeAlias, cast

ComputeStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "TERMINATING",
    "IMPAIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeStatus:
    return cast(ComputeStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComputeStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ComputeStatus:
    return cast(ComputeStatus, data)
