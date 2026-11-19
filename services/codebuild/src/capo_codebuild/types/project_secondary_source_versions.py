"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSecondarySourceVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.project_source_version

ProjectSecondarySourceVersions: TypeAlias = list[
    "capo_codebuild.types.project_source_version.ProjectSourceVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSecondarySourceVersions) -> list:
    import capo_codebuild.types.project_source_version

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.project_source_version.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectSecondarySourceVersions:
    import capo_codebuild.types.project_source_version

    out: ProjectSecondarySourceVersions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.project_source_version.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectSecondarySourceVersions) -> list:
    import capo_codebuild.types.project_source_version

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.project_source_version.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProjectSecondarySourceVersions:
    import capo_codebuild.types.project_source_version

    out: ProjectSecondarySourceVersions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.project_source_version.deserialize_cbor(item))
    return out
