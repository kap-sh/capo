"""Generated from Smithy shape ``com.amazonaws.imagebuilder#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "capo_imagebuilder.types.tag_map.TagMap"
    """<p>The tags to apply to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.tag_map

    out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
