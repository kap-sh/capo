"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.cleanrooms_arn
    import capo_cleanrooms.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_cleanrooms.types.cleanrooms_arn.CleanroomsArn"
    """<p>The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>"""
    tags: "capo_cleanrooms.types.tag_map.TagMap"
    """<p>A map of objects specifying each key name and value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.tag_map

    out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
