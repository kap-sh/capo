"""Generated from Smithy shape ``com.amazonaws.pipes#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_pipes.types.tag_map.TagMap"]
    """<p>The list of key-value pairs to associate with the pipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: ListTagsForResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.redact_sensitive(value["tags"])
    return out
