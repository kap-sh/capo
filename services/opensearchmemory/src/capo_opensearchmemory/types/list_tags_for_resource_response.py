"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_opensearchmemory.types.tag_list.TagList"]
    """<p>The tags for the space.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_opensearchmemory.types.tag_list

        out["tags"] = capo_opensearchmemory.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_opensearchmemory.types.tag_list

        out["tags"] = capo_opensearchmemory.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
