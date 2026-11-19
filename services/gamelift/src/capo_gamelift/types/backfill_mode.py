"""Generated from Smithy shape ``com.amazonaws.gamelift#BackfillMode``."""

from typing import Literal, TypeAlias, cast

BackfillMode: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackfillMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackfillMode:
    return cast(BackfillMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BackfillMode) -> str:
    return value


def deserialize_cbor(data: str) -> BackfillMode:
    return cast(BackfillMode, data)
