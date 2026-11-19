"""Generated from Smithy shape ``com.amazonaws.codebuild#ArtifactPackaging``."""

from typing import Literal, TypeAlias, cast

ArtifactPackaging: TypeAlias = Literal[
    "NONE",
    "ZIP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactPackaging) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactPackaging:
    return cast(ArtifactPackaging, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactPackaging) -> str:
    return value


def deserialize_cbor(data: str) -> ArtifactPackaging:
    return cast(ArtifactPackaging, data)
