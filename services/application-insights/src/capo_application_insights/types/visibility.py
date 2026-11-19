"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Visibility``."""

from typing import Literal, TypeAlias, cast

Visibility: TypeAlias = Literal[
    "IGNORED",
    "VISIBLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Visibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Visibility:
    return cast(Visibility, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Visibility) -> str:
    return value


def deserialize_cbor(data: str) -> Visibility:
    return cast(Visibility, data)
