"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceType``."""

from typing import Literal, TypeAlias, cast

SourceType: TypeAlias = Literal[
    "CODECOMMIT",
    "CODEPIPELINE",
    "GITHUB",
    "GITLAB",
    "GITLAB_SELF_MANAGED",
    "S3",
    "BITBUCKET",
    "GITHUB_ENTERPRISE",
    "NO_SOURCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    return cast(SourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceType) -> str:
    return value


def deserialize_cbor(data: str) -> SourceType:
    return cast(SourceType, data)
