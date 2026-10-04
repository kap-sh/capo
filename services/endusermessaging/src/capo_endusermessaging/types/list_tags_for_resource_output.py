"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_endusermessaging.types.tag_list.TagList"]
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
