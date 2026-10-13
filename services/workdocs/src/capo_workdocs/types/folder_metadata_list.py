"""Generated from Smithy shape ``com.amazonaws.workdocs#FolderMetadataList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.folder_metadata

FolderMetadataList: TypeAlias = list[
    "capo_workdocs.types.folder_metadata.FolderMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderMetadataList) -> list:
    import capo_workdocs.types.folder_metadata

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.folder_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderMetadataList:
    import capo_workdocs.types.folder_metadata

    out: FolderMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.folder_metadata.deserialize_json(item))
    return out


def redact_sensitive(value: FolderMetadataList) -> list[Any]:
    import capo_workdocs.types.folder_metadata

    return [
        capo_workdocs.types.folder_metadata.redact_sensitive(item) for item in value
    ]
