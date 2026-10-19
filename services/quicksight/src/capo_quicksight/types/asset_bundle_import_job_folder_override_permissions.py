"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobFolderOverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_resource_permissions
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobFolderOverridePermissions(TypedDict, closed=True):
    folder_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of folder IDs that you want to apply overrides to. You can use <code>*</code> to override all folders in this asset bundle.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobFolderOverridePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["FolderIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["folder_ids"]
        )
    )
    if "permissions" in value:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["Permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.serialize_json(
                value["permissions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobFolderOverridePermissions:
    out: AssetBundleImportJobFolderOverridePermissions = {}  # type: ignore[typeddict-item]
    if data.get("FolderIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["folder_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["FolderIds"]
            )
        )
    else:
        out["folder_ids"] = []
    if data.get("Permissions") is not None:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    return out
