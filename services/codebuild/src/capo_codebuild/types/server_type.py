"""Generated from Smithy shape ``com.amazonaws.codebuild#ServerType``."""

from typing import Literal, TypeAlias, cast

ServerType: TypeAlias = Literal[
    "GITHUB",
    "BITBUCKET",
    "GITHUB_ENTERPRISE",
    "GITLAB",
    "GITLAB_SELF_MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServerType:
    return cast(ServerType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServerType) -> str:
    return value


def deserialize_cbor(data: str) -> ServerType:
    return cast(ServerType, data)
