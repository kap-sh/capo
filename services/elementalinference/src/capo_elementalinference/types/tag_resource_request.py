"""Generated from Smithy shape ``com.amazonaws.elementalinference#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.resource_arn
    import capo_elementalinference.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_elementalinference.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource where you want to add tags.</p>"""
    tags: "capo_elementalinference.types.tag_map.TagMap"
    """<p>A list of tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_elementalinference.types.tag_map

    out["tags"] = capo_elementalinference.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
