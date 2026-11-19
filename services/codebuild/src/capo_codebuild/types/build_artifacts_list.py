"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildArtifactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build_artifacts

BuildArtifactsList: TypeAlias = list[
    "capo_codebuild.types.build_artifacts.BuildArtifacts"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildArtifactsList) -> list:
    import capo_codebuild.types.build_artifacts

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_artifacts.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildArtifactsList:
    import capo_codebuild.types.build_artifacts

    out: BuildArtifactsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_artifacts.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildArtifactsList) -> list:
    import capo_codebuild.types.build_artifacts

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_artifacts.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BuildArtifactsList:
    import capo_codebuild.types.build_artifacts

    out: BuildArtifactsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_artifacts.deserialize_cbor(item))
    return out
