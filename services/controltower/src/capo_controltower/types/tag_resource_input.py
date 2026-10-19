"""Generated from Smithy shape ``com.amazonaws.controltower#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the resource to be tagged.</p>"""
    tags: "capo_controltower.types.tag_map.TagMap"
    """<p>Tags to be applied to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_controltower.types.tag_map

    out["tags"] = capo_controltower.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
