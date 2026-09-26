"""Generated from Smithy shape ``com.amazonaws.supportauthz#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.tags


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_supportauthz.types.tags.Tags"]
    """<p>The tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_supportauthz.types.tags

        out["tags"] = capo_supportauthz.types.tags.deserialize_json(data["tags"])
    return out
