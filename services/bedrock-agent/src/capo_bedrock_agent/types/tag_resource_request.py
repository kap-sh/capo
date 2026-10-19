"""Generated from Smithy shape ``com.amazonaws.bedrockagent#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.taggable_resources_arn
    import capo_bedrock_agent.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_bedrock_agent.types.tags_map.TagsMap"
    """<p>An object containing key-value pairs that define the tags to attach to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.tags_map

    out["tags"] = capo_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_bedrock_agent.types.tags_map

        out["tags"] = capo_bedrock_agent.types.tags_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
