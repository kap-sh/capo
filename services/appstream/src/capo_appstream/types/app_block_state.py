"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockState``."""

from typing import Literal, TypeAlias, cast

AppBlockState: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockState:
    return cast(AppBlockState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockState) -> str:
    return value


def deserialize_cbor(data: str) -> AppBlockState:
    return cast(AppBlockState, data)
