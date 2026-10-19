"""Generated from Smithy shape ``com.amazonaws.controltower#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "capo_controltower.types.tag_map.TagMap"
    """<p>A list of tags, as <code>key:value</code> strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.tag_map

    out["tags"] = capo_controltower.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
