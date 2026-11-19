"""Generated from Smithy shape ``com.amazonaws.datasync#VerifyMode``."""

from typing import Literal, TypeAlias, cast

VerifyMode: TypeAlias = Literal[
    "POINT_IN_TIME_CONSISTENT",
    "ONLY_FILES_TRANSFERRED",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VerifyMode:
    return cast(VerifyMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VerifyMode) -> str:
    return value


def deserialize_cbor(data: str) -> VerifyMode:
    return cast(VerifyMode, data)
