"""Generated from Smithy shape ``com.amazonaws.codeconnections#BlockerStatus``."""

from typing import Literal, TypeAlias, cast

BlockerStatus: TypeAlias = Literal[
    "ACTIVE",
    "RESOLVED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BlockerStatus:
    return cast(BlockerStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlockerStatus) -> str:
    return value


def deserialize_cbor(data: str) -> BlockerStatus:
    return cast(BlockerStatus, data)
