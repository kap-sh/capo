"""Generated from Smithy shape ``com.amazonaws.translate#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_translate.types.tag_list.TagList"]
    """<p>Tags associated with the Amazon Translate resource being queried. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Translate. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_translate.types.tag_list

        out["Tags"] = capo_translate.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_translate.types.tag_list

        out["tags"] = capo_translate.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
