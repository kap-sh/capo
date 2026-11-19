"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagFilterType``."""

from typing import Literal, TypeAlias, cast

TagFilterType: TypeAlias = Literal[
    "KEY_ONLY",
    "VALUE_ONLY",
    "KEY_AND_VALUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagFilterType:
    return cast(TagFilterType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagFilterType) -> str:
    return value


def deserialize_cbor(data: str) -> TagFilterType:
    return cast(TagFilterType, data)
