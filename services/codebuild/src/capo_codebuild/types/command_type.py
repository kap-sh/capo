"""Generated from Smithy shape ``com.amazonaws.codebuild#CommandType``."""

from typing import Literal, TypeAlias, cast

CommandType: TypeAlias = Literal["SHELL",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CommandType:
    return cast(CommandType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CommandType) -> str:
    return value


def deserialize_cbor(data: str) -> CommandType:
    return cast(CommandType, data)
