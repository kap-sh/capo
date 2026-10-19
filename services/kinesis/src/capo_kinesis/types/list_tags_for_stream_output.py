"""Generated from Smithy shape ``com.amazonaws.kinesis#ListTagsForStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.tag_list


class ListTagsForStreamOutput(TypedDict, closed=True):
    tags: "capo_kinesis.types.tag_list.TagList"
    """<p>A list of tags associated with <code>StreamName</code>, starting with the first tag after <code>ExclusiveStartTagKey</code> and up to the specified <code>Limit</code>. </p>"""
    has_more_tags: "capo_kinesis.types.boolean_object.BooleanObject"
    """<p>If set to <code>true</code>, more tags are available. To request additional tags, set <code>ExclusiveStartTagKey</code> to the key of the last tag returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForStreamOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.tag_list

    out["Tags"] = capo_kinesis.types.tag_list.serialize_aws_json_1_1(value["tags"])
    out["HasMoreTags"] = value["has_more_tags"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForStreamOutput:
    out: ListTagsForStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_kinesis.types.tag_list

        out["tags"] = capo_kinesis.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    if data.get("HasMoreTags") is not None:
        out["has_more_tags"] = data["HasMoreTags"]
    else:
        out["has_more_tags"] = False
    return out
