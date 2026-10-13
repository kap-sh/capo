"""Generated from Smithy shape ``com.amazonaws.mpa#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_mpa.types.tags.Tags"]
    """<p>Tags attached to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mpa.types.tags

        out["Tags"] = capo_mpa.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_mpa.types.tags

        out["tags"] = capo_mpa.types.tags.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: ListTagsForResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
