"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeRootFoldersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.folder_metadata_list
    import capo_workdocs.types.page_marker_type


class DescribeRootFoldersResponse(TypedDict, closed=True):
    folders: NotRequired["capo_workdocs.types.folder_metadata_list.FolderMetadataList"]
    """<p>The user's special folders.</p>"""
    marker: NotRequired["capo_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRootFoldersResponse) -> dict:
    out: dict = {}
    if "folders" in value:
        import capo_workdocs.types.folder_metadata_list

        out["Folders"] = capo_workdocs.types.folder_metadata_list.serialize_json(
            value["folders"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeRootFoldersResponse:
    out: DescribeRootFoldersResponse = {}  # type: ignore[typeddict-item]
    if data.get("Folders") is not None:
        import capo_workdocs.types.folder_metadata_list

        out["folders"] = capo_workdocs.types.folder_metadata_list.deserialize_json(
            data["Folders"]
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out


def redact_sensitive(value: DescribeRootFoldersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "folders" in value:
        import capo_workdocs.types.folder_metadata_list

        out["folders"] = capo_workdocs.types.folder_metadata_list.redact_sensitive(
            value["folders"]
        )
    return out
