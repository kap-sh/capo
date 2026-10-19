"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_ivs_realtime.types.tags.Tags"
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.tags

    out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
