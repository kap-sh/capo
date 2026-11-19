"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnvironmentVariableType``."""

from typing import Literal, TypeAlias, cast

EnvironmentVariableType: TypeAlias = Literal[
    "PLAINTEXT",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariableType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentVariableType:
    return cast(EnvironmentVariableType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentVariableType) -> str:
    return value


def deserialize_cbor(data: str) -> EnvironmentVariableType:
    return cast(EnvironmentVariableType, data)
