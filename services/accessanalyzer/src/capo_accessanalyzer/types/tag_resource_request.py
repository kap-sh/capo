"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to add the tag to.</p>"""
    tags: "capo_accessanalyzer.types.tags_map.TagsMap"
    """<p>The tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.tags_map

    out["tags"] = capo_accessanalyzer.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
