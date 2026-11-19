"""Generated from Smithy shape ``com.amazonaws.codebuild#ArtifactNamespace``."""

from typing import Literal, TypeAlias, cast

ArtifactNamespace: TypeAlias = Literal[
    "NONE",
    "BUILD_ID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactNamespace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactNamespace:
    return cast(ArtifactNamespace, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactNamespace) -> str:
    return value


def deserialize_cbor(data: str) -> ArtifactNamespace:
    return cast(ArtifactNamespace, data)
