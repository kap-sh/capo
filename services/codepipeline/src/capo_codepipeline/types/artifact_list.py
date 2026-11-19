"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact

ArtifactList: TypeAlias = list["capo_codepipeline.types.artifact.Artifact"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactList) -> list:
    import capo_codepipeline.types.artifact

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.artifact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactList:
    import capo_codepipeline.types.artifact

    out: ArtifactList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.artifact.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArtifactList) -> list:
    import capo_codepipeline.types.artifact

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.artifact.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ArtifactList:
    import capo_codepipeline.types.artifact

    out: ArtifactList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.artifact.deserialize_cbor(item))
    return out
