"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list
    import capo_quicksight.types.tag_list


class AssetBundleImportJobDataSetOverrideTags(TypedDict, closed=True):
    data_set_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of dataset IDs that you want to apply overrides to. You can use <code>*</code> to override all datasets in this asset bundle.</p>"""
    tags: "capo_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the datasets that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverrideTags) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["DataSetIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["data_set_ids"]
        )
    )
    import capo_quicksight.types.tag_list

    out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSetOverrideTags:
    out: AssetBundleImportJobDataSetOverrideTags = {}  # type: ignore[typeddict-item]
    if data.get("DataSetIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["data_set_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["DataSetIds"]
            )
        )
    else:
        out["data_set_ids"] = []
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
