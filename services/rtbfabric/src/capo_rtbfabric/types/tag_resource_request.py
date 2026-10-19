"""Generated from Smithy shape ``com.amazonaws.rtbfabric#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.rtb_taggable_resource_arn
    import capo_rtbfabric.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "capo_rtbfabric.types.tags_map.TagsMap"
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.tags_map

    out["tags"] = capo_rtbfabric.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_rtbfabric.types.tags_map

        out["tags"] = capo_rtbfabric.types.tags_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
