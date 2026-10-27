"""Generated from Smithy shape ``com.amazonaws.deadline#ManifestProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.file_system_location_name
    import capo_deadline.types.output_relative_directories_list
    import capo_deadline.types.path_format
    import capo_deadline.types.string


class ManifestProperties(TypedDict, closed=True):
    file_system_location_name: NotRequired[
        "capo_deadline.types.file_system_location_name.FileSystemLocationName"
    ]
    """The file system location name."""
    root_path: "capo_deadline.types.string.String"
    """The file's root path."""
    root_path_format: "capo_deadline.types.path_format.PathFormat"
    """The format of the root path."""
    output_relative_directories: NotRequired[
        "capo_deadline.types.output_relative_directories_list.OutputRelativeDirectoriesList"
    ]
    """The file path relative to the directory."""
    input_manifest_path: NotRequired["capo_deadline.types.string.String"]
    """The file path."""
    input_manifest_hash: NotRequired["capo_deadline.types.string.String"]
    """The hash value of the file."""


# --- restJson1 ser/de ---
def serialize_json(value: ManifestProperties) -> dict:
    out: dict = {}
    if "file_system_location_name" in value:
        out["fileSystemLocationName"] = value["file_system_location_name"]
    out["rootPath"] = value["root_path"]
    import capo_deadline.types.path_format

    out["rootPathFormat"] = capo_deadline.types.path_format.serialize_json(
        value["root_path_format"]
    )
    if "output_relative_directories" in value:
        import capo_deadline.types.output_relative_directories_list

        out["outputRelativeDirectories"] = (
            capo_deadline.types.output_relative_directories_list.serialize_json(
                value["output_relative_directories"]
            )
        )
    if "input_manifest_path" in value:
        out["inputManifestPath"] = value["input_manifest_path"]
    if "input_manifest_hash" in value:
        out["inputManifestHash"] = value["input_manifest_hash"]
    return out


def deserialize_json(data: dict) -> ManifestProperties:
    out: ManifestProperties = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemLocationName") is not None:
        out["file_system_location_name"] = data["fileSystemLocationName"]
    if data.get("rootPath") is not None:
        out["root_path"] = data["rootPath"]
    else:
        out["root_path"] = ""
    if data.get("rootPathFormat") is not None:
        import capo_deadline.types.path_format

        out["root_path_format"] = capo_deadline.types.path_format.deserialize_json(
            data["rootPathFormat"]
        )
    else:
        import typing

        out["root_path_format"] = typing.cast(
            "capo_deadline.types.path_format.PathFormat", ""
        )
    if data.get("outputRelativeDirectories") is not None:
        import capo_deadline.types.output_relative_directories_list

        out["output_relative_directories"] = (
            capo_deadline.types.output_relative_directories_list.deserialize_json(
                data["outputRelativeDirectories"]
            )
        )
    if data.get("inputManifestPath") is not None:
        out["input_manifest_path"] = data["inputManifestPath"]
    if data.get("inputManifestHash") is not None:
        out["input_manifest_hash"] = data["inputManifestHash"]
    return out
