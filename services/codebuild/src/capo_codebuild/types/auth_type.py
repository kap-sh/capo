"""Generated from Smithy shape ``com.amazonaws.codebuild#AuthType``."""

from typing import Literal, TypeAlias, cast

AuthType: TypeAlias = Literal[
    "OAUTH",
    "BASIC_AUTH",
    "PERSONAL_ACCESS_TOKEN",
    "CODECONNECTIONS",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthType:
    return cast(AuthType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuthType) -> str:
    return value


def deserialize_cbor(data: str) -> AuthType:
    return cast(AuthType, data)
