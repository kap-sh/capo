"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobTopicV2OverridePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_resource_permissions
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list


class AssetBundleImportJobTopicV2OverridePermissions(TypedDict, closed=True):
    topic_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of topic IDs that you want to apply overrides to. You can use <code>*</code> to override all topics in this asset bundle.</p>"""
    permissions: "capo_quicksight.types.asset_bundle_resource_permissions.AssetBundleResourcePermissions"
    """<p>A list of permissions for the topics that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobTopicV2OverridePermissions) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["TopicIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["topic_ids"]
        )
    )
    import capo_quicksight.types.asset_bundle_resource_permissions

    out["Permissions"] = (
        capo_quicksight.types.asset_bundle_resource_permissions.serialize_json(
            value["permissions"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobTopicV2OverridePermissions:
    out: AssetBundleImportJobTopicV2OverridePermissions = {}  # type: ignore[typeddict-item]
    if data.get("TopicIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["topic_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["TopicIds"]
            )
        )
    else:
        out["topic_ids"] = []
    if data.get("Permissions") is not None:
        import capo_quicksight.types.asset_bundle_resource_permissions

        out["permissions"] = (
            capo_quicksight.types.asset_bundle_resource_permissions.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError(
            "AssetBundleImportJobTopicV2OverridePermissions.permissions required"
        )
    return out
