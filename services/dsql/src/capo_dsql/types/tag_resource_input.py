"""Generated from Smithy shape ``com.amazonaws.dsql#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.arn
    import capo_dsql.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_dsql.types.arn.Arn"
    """<p>The ARN of the resource that you want to tag.</p>"""
    tags: "capo_dsql.types.tag_map.TagMap"
    """<p>A map of key and value pairs to use to tag your resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_dsql.types.tag_map

    out["tags"] = capo_dsql.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
