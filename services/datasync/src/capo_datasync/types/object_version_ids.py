"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectVersionIds``."""

from typing import Literal, TypeAlias, cast

ObjectVersionIds: TypeAlias = Literal[
    "INCLUDE",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectVersionIds) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectVersionIds:
    return cast(ObjectVersionIds, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ObjectVersionIds) -> str:
    return value


def deserialize_cbor(data: str) -> ObjectVersionIds:
    return cast(ObjectVersionIds, data)
