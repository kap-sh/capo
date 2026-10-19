"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSourceOverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_resource_permissions
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobDataSourceOverridePermissions(TypedDict, closed=True):
    data_source_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of data source IDs that you want to apply overrides to. You can use <code>*</code> to override all data sources in this asset bundle.</p>"""
    permissions: "capo_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    """<p>A list of permissions for the data source that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSourceOverridePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DataSourceIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["data_source_ids"]
        )
    )
    import capo_quicksight.types.asset_bundle_resource_permissions

    out["Permissions"] = (
        capo_quicksight.types.asset_bundle_resource_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSourceOverridePermissions:
    out: AssetBundleImportJobDataSourceOverridePermissions = {}  # type: ignore[typeddict-item]
    if data.get("DataSourceIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["data_source_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DataSourceIds"]
            )
        )
    else:
        out["data_source_ids"] = []
    if data.get("Permissions") is not None:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobDataSourceOverridePermissions.permissions required"
        )
    return out
