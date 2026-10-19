"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobTopicV2OverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.topic_description


class AssetBundleImportJobTopicV2OverrideParameters(TypedDict, closed=True):
    topic_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the topic that you want to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the topic.</p>"""
    description: NotRequired["capo_quicksight.types.topic_description.TopicDescription"]
    """<p>A new description for the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobTopicV2OverrideParameters) -> dict:
    out: dict = {}
    out["TopicId"] = value["topic_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobTopicV2OverrideParameters:
    out: AssetBundleImportJobTopicV2OverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    else:
        out["topic_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
