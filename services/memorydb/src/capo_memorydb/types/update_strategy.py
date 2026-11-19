"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateStrategy``."""

from typing import Literal, TypeAlias, cast

UpdateStrategy: TypeAlias = Literal[
    "coordinated",
    "uncoordinated",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateStrategy:
    return cast(UpdateStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> UpdateStrategy:
    return cast(UpdateStrategy, data)
