"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_mailmanager.types.tag_list.TagList"
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_mailmanager.types.tag_list

    out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out
