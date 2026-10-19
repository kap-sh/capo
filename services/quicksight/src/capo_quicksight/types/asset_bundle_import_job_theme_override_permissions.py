"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobThemeOverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_resource_permissions
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobThemeOverridePermissions(TypedDict, closed=True):
    theme_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of theme IDs that you want to apply overrides to. You can use <code>*</code> to override all themes in this asset bundle.</p>"""
    permissions: "capo_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    """<p>A list of permissions for the themes that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobThemeOverridePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["ThemeIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["theme_ids"]
        )
    )
    import capo_quicksight.types.asset_bundle_resource_permissions

    out["Permissions"] = (
        capo_quicksight.types.asset_bundle_resource_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobThemeOverridePermissions:
    out: AssetBundleImportJobThemeOverridePermissions = {}  # type: ignore[typeddict-item]
    if data.get("ThemeIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["theme_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["ThemeIds"]
            )
        )
    else:
        out["theme_ids"] = []
    if data.get("Permissions") is not None:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobThemeOverridePermissions.permissions required"
        )
    return out
