"""Generated from Smithy shape ``com.amazonaws.detective#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn
    import capo_detective.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to assign the tags to.</p>"""
    tags: "capo_detective.types.tag_map.TagMap"
    """<p>The tags to assign to the behavior graph. You can add up to 50 tags. For each tag, you provide the tag key and the tag value. Each tag key can contain up to 128 characters. Each tag value can contain up to 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_detective.types.tag_map

    out["Tags"] = capo_detective.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_detective.types.tag_map

        out["tags"] = capo_detective.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
