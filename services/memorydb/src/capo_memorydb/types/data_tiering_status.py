"""Generated from Smithy shape ``com.amazonaws.memorydb#DataTieringStatus``."""

from typing import Literal, TypeAlias, cast

DataTieringStatus: TypeAlias = Literal[
    "true",
    "false",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataTieringStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataTieringStatus:
    return cast(DataTieringStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataTieringStatus) -> str:
    return value


def deserialize_cbor(data: str) -> DataTieringStatus:
    return cast(DataTieringStatus, data)
