"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

DatasetStatus: TypeAlias = Literal[
    "CREATING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetStatus:
    return cast(DatasetStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DatasetStatus:
    return cast(DatasetStatus, data)
