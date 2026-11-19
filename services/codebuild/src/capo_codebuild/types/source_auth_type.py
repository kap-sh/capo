"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceAuthType``."""

from typing import Literal, TypeAlias, cast

SourceAuthType: TypeAlias = Literal[
    "OAUTH",
    "CODECONNECTIONS",
    "SECRETS_MANAGER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAuthType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceAuthType:
    return cast(SourceAuthType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceAuthType) -> str:
    return value


def deserialize_cbor(data: str) -> SourceAuthType:
    return cast(SourceAuthType, data)
