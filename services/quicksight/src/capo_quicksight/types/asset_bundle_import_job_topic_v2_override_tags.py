"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobTopicV2OverrideTags``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list
    import capo_quicksight.types.tag_list


class AssetBundleImportJobTopicV2OverrideTags(TypedDict, closed=True):
    topic_ids: "capo_quicksight.types.asset_bundle_restrictive_resource_id_list.AssetBundleRestrictiveResourceIdList"
    """<p>A list of topic IDs that you want to apply overrides to. You can use <code>*</code> to override all topics in this asset bundle.</p>"""
    tags: "capo_quicksight.types.tag_list.TagList"
    """<p>A list of tags for the topics that you want to apply overrides to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobTopicV2OverrideTags) -> dict:
    out: dict = {}
    import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

    out["TopicIds"] = (
        capo_quicksight.types.asset_bundle_restrictive_resource_id_list.serialize_json(
            value["topic_ids"]
        )
    )
    import capo_quicksight.types.tag_list

    out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobTopicV2OverrideTags:
    out: AssetBundleImportJobTopicV2OverrideTags = {}  # type: ignore[typeddict-item]
    if data.get("TopicIds") is not None:
        import capo_quicksight.types.asset_bundle_restrictive_resource_id_list

        out["topic_ids"] = (
            capo_quicksight.types.asset_bundle_restrictive_resource_id_list.deserialize_json(
                data["TopicIds"]
            )
        )
    else:
        out["topic_ids"] = []
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
