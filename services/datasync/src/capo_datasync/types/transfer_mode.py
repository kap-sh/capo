"""Generated from Smithy shape ``com.amazonaws.datasync#TransferMode``."""

from typing import Literal, TypeAlias, cast

TransferMode: TypeAlias = Literal[
    "CHANGED",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransferMode:
    return cast(TransferMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TransferMode) -> str:
    return value


def deserialize_cbor(data: str) -> TransferMode:
    return cast(TransferMode, data)
