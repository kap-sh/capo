"""Generated from Smithy shape ``com.amazonaws.codepipeline#BlockerType``."""

from typing import Literal, TypeAlias, cast

BlockerType: TypeAlias = Literal["Schedule",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockerType:
    return cast(BlockerType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlockerType) -> str:
    return value


def deserialize_cbor(data: str) -> BlockerType:
    return cast(BlockerType, data)
