"""Generated from Smithy shape ``com.amazonaws.workdocs#GetFolderResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.custom_metadata_map
    import capo_workdocs.types.folder_metadata


class GetFolderResponse(TypedDict, closed=True):
    metadata: NotRequired["capo_workdocs.types.folder_metadata.FolderMetadata"]
    """<p>The metadata of the folder.</p>"""
    custom_metadata: NotRequired[
        "capo_workdocs.types.custom_metadata_map.CustomMetadataMap"
    ]
    """<p>The custom metadata on the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFolderResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_workdocs.types.folder_metadata

        out["Metadata"] = capo_workdocs.types.folder_metadata.serialize_json(
            value["metadata"]
        )
    if "custom_metadata" in value:
        import capo_workdocs.types.custom_metadata_map

        out["CustomMetadata"] = capo_workdocs.types.custom_metadata_map.serialize_json(
            value["custom_metadata"]
        )
    return out


def deserialize_json(data: dict) -> GetFolderResponse:
    out: GetFolderResponse = {}  # type: ignore[typeddict-item]
    if data.get("Metadata") is not None:
        import capo_workdocs.types.folder_metadata

        out["metadata"] = capo_workdocs.types.folder_metadata.deserialize_json(
            data["Metadata"]
        )
    if data.get("CustomMetadata") is not None:
        import capo_workdocs.types.custom_metadata_map

        out["custom_metadata"] = (
            capo_workdocs.types.custom_metadata_map.deserialize_json(
                data["CustomMetadata"]
            )
        )
    return out


def redact_sensitive(value: GetFolderResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata" in value:
        import capo_workdocs.types.folder_metadata

        out["metadata"] = capo_workdocs.types.folder_metadata.redact_sensitive(
            value["metadata"]
        )
    return out
