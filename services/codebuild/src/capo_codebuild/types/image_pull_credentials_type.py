"""Generated from Smithy shape ``com.amazonaws.codebuild#ImagePullCredentialsType``."""

from typing import Literal, TypeAlias, cast

ImagePullCredentialsType: TypeAlias = Literal[
    "CODEBUILD",
    "SERVICE_ROLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImagePullCredentialsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImagePullCredentialsType:
    return cast(ImagePullCredentialsType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImagePullCredentialsType) -> str:
    return value


def deserialize_cbor(data: str) -> ImagePullCredentialsType:
    return cast(ImagePullCredentialsType, data)
