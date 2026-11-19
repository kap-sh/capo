"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectFileSystemLocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.project_file_system_location

ProjectFileSystemLocations: TypeAlias = list[
    "capo_codebuild.types.project_file_system_location.ProjectFileSystemLocation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectFileSystemLocations) -> list:
    import capo_codebuild.types.project_file_system_location

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.project_file_system_location.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectFileSystemLocations:
    import capo_codebuild.types.project_file_system_location

    out: ProjectFileSystemLocations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.project_file_system_location.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectFileSystemLocations) -> list:
    import capo_codebuild.types.project_file_system_location

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.project_file_system_location.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ProjectFileSystemLocations:
    import capo_codebuild.types.project_file_system_location

    out: ProjectFileSystemLocations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.project_file_system_location.deserialize_cbor(item)
        )
    return out
