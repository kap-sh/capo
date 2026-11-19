"""Generated from Smithy shape ``com.amazonaws.codebuild#ArtifactsType``."""

from typing import Literal, TypeAlias, cast

ArtifactsType: TypeAlias = Literal[
    "CODEPIPELINE",
    "S3",
    "NO_ARTIFACTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactsType:
    return cast(ArtifactsType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactsType) -> str:
    return value


def deserialize_cbor(data: str) -> ArtifactsType:
    return cast(ArtifactsType, data)
