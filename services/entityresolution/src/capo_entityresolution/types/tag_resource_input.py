"""Generated from Smithy shape ``com.amazonaws.entityresolution#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.tag_map
    import capo_entityresolution.types.venice_global_arn


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn"
    """<p>The ARN of the resource for which you want to view tags.</p>"""
    tags: "capo_entityresolution.types.tag_map.TagMap"
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.tag_map

    out["tags"] = capo_entityresolution.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
