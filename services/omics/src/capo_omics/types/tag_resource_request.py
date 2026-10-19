"""Generated from Smithy shape ``com.amazonaws.omics#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.tag_arn
    import capo_omics.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_omics.types.tag_arn.TagArn"
    """<p>The resource's ARN.</p>"""
    tags: "capo_omics.types.tag_map.TagMap"
    """<p>Tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_omics.types.tag_map

    out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
