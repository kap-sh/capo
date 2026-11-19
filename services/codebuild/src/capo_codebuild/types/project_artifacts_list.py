"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectArtifactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.project_artifacts

ProjectArtifactsList: TypeAlias = list[
    "capo_codebuild.types.project_artifacts.ProjectArtifacts"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectArtifactsList) -> list:
    import capo_codebuild.types.project_artifacts

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project_artifacts.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectArtifactsList:
    import capo_codebuild.types.project_artifacts

    out: ProjectArtifactsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.project_artifacts.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectArtifactsList) -> list:
    import capo_codebuild.types.project_artifacts

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project_artifacts.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProjectArtifactsList:
    import capo_codebuild.types.project_artifacts

    out: ProjectArtifactsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.project_artifacts.deserialize_cbor(item))
    return out
