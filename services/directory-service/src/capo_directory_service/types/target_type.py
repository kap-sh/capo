"""Generated from Smithy shape ``com.amazonaws.directoryservice#TargetType``."""

from typing import Literal, TypeAlias, cast

TargetType: TypeAlias = Literal["ACCOUNT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetType:
    return cast(TargetType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetType) -> str:
    return value


def deserialize_cbor(data: str) -> TargetType:
    return cast(TargetType, data)
