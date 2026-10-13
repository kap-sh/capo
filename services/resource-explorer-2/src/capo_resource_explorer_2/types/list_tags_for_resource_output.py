"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.tag_map


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_resource_explorer_2.types.tag_map.TagMap"]
    """<p>The tag key and value pairs that you want to attach to the specified view or index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_resource_explorer_2.types.tag_map

        out["Tags"] = capo_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_resource_explorer_2.types.tag_map

        out["tags"] = capo_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: ListTagsForResourceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
