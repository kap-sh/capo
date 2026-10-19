"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobFolderOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name


class AssetBundleImportJobFolderOverrideParameters(TypedDict, closed=True):
    folder_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the folder that you want to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the folder.</p>"""
    parent_folder_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>A new parent folder arn. This change can only be applied if the import creates a brand new folder. Existing folders cannot be moved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobFolderOverrideParameters) -> dict:
    out: dict = {}
    out["FolderId"] = value["folder_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "parent_folder_arn" in value:
        out["ParentFolderArn"] = value["parent_folder_arn"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobFolderOverrideParameters:
    out: AssetBundleImportJobFolderOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("FolderId") is not None:
        out["folder_id"] = data["FolderId"]
    else:
        out["folder_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ParentFolderArn") is not None:
        out["parent_folder_arn"] = data["ParentFolderArn"]
    return out
