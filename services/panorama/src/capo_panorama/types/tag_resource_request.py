"""Generated from Smithy shape ``com.amazonaws.panorama#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.resource_arn
    import capo_panorama.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_panorama.types.resource_arn.ResourceArn"
    """<p>The resource's ARN.</p>"""
    tags: "capo_panorama.types.tag_map.TagMap"
    """<p>Tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_panorama.types.tag_map

    out["Tags"] = capo_panorama.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_panorama.types.tag_map

        out["tags"] = capo_panorama.types.tag_map.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
