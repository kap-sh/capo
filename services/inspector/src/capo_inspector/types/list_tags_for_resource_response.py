"""Generated from Smithy shape ``com.amazonaws.inspector#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_inspector.types.tag_list.TagList"
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.tag_list

    out["tags"] = capo_inspector.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_inspector.types.tag_list

        out["tags"] = capo_inspector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
