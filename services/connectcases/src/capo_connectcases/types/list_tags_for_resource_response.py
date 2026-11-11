"""Generated from Smithy shape ``com.amazonaws.connectcases#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    return out
