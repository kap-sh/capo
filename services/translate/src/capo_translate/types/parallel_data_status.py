"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataStatus``."""

from typing import Literal, TypeAlias, cast

ParallelDataStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParallelDataStatus:
    return cast(ParallelDataStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ParallelDataStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ParallelDataStatus:
    return cast(ParallelDataStatus, data)
