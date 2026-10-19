"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobAnalysisOverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_resource_permissions
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobAnalysisOverridePermissions(TypedDict, closed=True):
    analysis_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of analysis IDs that you want to apply overrides to. You can use <code>*</code> to override all analyses in this asset bundle.</p>"""
    permissions: "capo_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    """<p>A list of permissions for the analyses that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobAnalysisOverridePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["AnalysisIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["analysis_ids"]
        )
    )
    import capo_quicksight.types.asset_bundle_resource_permissions

    out["Permissions"] = (
        capo_quicksight.types.asset_bundle_resource_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobAnalysisOverridePermissions:
    out: AssetBundleImportJobAnalysisOverridePermissions = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["analysis_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["AnalysisIds"]
            )
        )
    else:
        out["analysis_ids"] = []
    if data.get("Permissions") is not None:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobAnalysisOverridePermissions.permissions required"
        )
    return out
