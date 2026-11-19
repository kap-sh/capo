"""Generated from Smithy shape ``com.amazonaws.appstream#VisibilityType``."""

from typing import Literal, TypeAlias, cast

VisibilityType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
    "SHARED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VisibilityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VisibilityType:
    return cast(VisibilityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VisibilityType) -> str:
    return value


def deserialize_cbor(data: str) -> VisibilityType:
    return cast(VisibilityType, data)
