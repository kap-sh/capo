"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.project_source

ProjectSources: TypeAlias = list["capo_codebuild.types.project_source.ProjectSource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSources) -> list:
    import capo_codebuild.types.project_source

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project_source.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectSources:
    import capo_codebuild.types.project_source

    out: ProjectSources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.project_source.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectSources) -> list:
    import capo_codebuild.types.project_source

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project_source.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProjectSources:
    import capo_codebuild.types.project_source

    out: ProjectSources = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.project_source.deserialize_cbor(item))
    return out
