"""Generated from Smithy shape ``com.amazonaws.amplify#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.resource_arn
    import capo_amplify.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_amplify.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) to use to tag a resource. </p>"""
    tags: "capo_amplify.types.tag_map.TagMap"
    """<p>The tags used to tag the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_amplify.types.tag_map

    out["tags"] = capo_amplify.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
