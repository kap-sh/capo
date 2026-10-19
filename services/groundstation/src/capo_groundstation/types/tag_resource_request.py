"""Generated from Smithy shape ``com.amazonaws.groundstation#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.any_arn
    import capo_groundstation.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_groundstation.types.any_arn.AnyArn"
    """<p>ARN of a resource tag.</p>"""
    tags: "capo_groundstation.types.tags_map.TagsMap"
    """<p>Tags assigned to a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_groundstation.types.tags_map

    out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
