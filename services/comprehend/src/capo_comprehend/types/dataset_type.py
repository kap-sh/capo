"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetType``."""

from typing import Literal, TypeAlias, cast

DatasetType: TypeAlias = Literal[
    "TRAIN",
    "TEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetType:
    return cast(DatasetType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DatasetType) -> str:
    return value


def deserialize_cbor(data: str) -> DatasetType:
    return cast(DatasetType, data)
