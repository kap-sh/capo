"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_rolesanywhere.types.tag_list.TagList"]
    """<p>A list of tags attached to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: ListTagsForResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.redact_sensitive(value["tags"])
    return out
