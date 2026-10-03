"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags associated with this resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
