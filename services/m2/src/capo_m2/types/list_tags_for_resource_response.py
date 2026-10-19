"""Generated from Smithy shape ``com.amazonaws.m2#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_m2.types.tag_map.TagMap"
    """<p>The tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_m2.types.tag_map

    out["tags"] = capo_m2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
