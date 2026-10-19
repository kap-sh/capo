"""Generated from Smithy shape ``com.amazonaws.bedrock#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.taggable_resources_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_bedrock.types.taggable_resources_arn.TaggableResourcesArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_bedrock.types.tag_list.TagList"
    """<p>Tags to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    import capo_bedrock.types.tag_list

    out["tags"] = capo_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceARN") is not None:
        out["resource_arn"] = data["resourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_bedrock.types.tag_list

        out["tags"] = capo_bedrock.types.tag_list.deserialize_json(data["tags"])
    else:
        out["tags"] = []
    return out
