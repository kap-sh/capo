"""Generated from Smithy shape ``com.amazonaws.connect#Prompt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.common_name_length127
    import capo_connect.types.prompt_description
    import capo_connect.types.prompt_id
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class Prompt(TypedDict, closed=True):
    prompt_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the prompt.</p>"""
    prompt_id: NotRequired["capo_connect.types.prompt_id.PromptId"]
    """<p>A unique identifier for the prompt.</p>"""
    name: NotRequired["capo_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the prompt.</p>"""
    description: NotRequired["capo_connect.types.prompt_description.PromptDescription"]
    """<p>The description of the prompt.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Prompt) -> dict:
    out: dict = {}
    if "prompt_arn" in value:
        out["PromptARN"] = value["prompt_arn"]
    if "prompt_id" in value:
        out["PromptId"] = value["prompt_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> Prompt:
    out: Prompt = {}  # type: ignore[typeddict-item]
    if data.get("PromptARN") is not None:
        out["prompt_arn"] = data["PromptARN"]
    if data.get("PromptId") is not None:
        out["prompt_id"] = data["PromptId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
