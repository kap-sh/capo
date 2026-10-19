"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.tag_arn
    import capo_mediapackagev2.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediapackagev2.types.tag_arn.TagArn"
    """<p>The ARN of the MediaPackage resource that you're adding tags to.</p>"""
    tags: "capo_mediapackagev2.types.tag_map.TagMap"
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.tag_map

    out["tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
