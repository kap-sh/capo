"""Generated from Smithy shape ``com.amazonaws.firehose#ListTagsForDeliveryStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.list_tags_for_delivery_stream_output_tag_list


class ListTagsForDeliveryStreamOutput(TypedDict, closed=True):
    tags: "capo_firehose.types.list_tags_for_delivery_stream_output_tag_list.ListTagsForDeliveryStreamOutputTagList"
    """<p>A list of tags associated with <code>DeliveryStreamName</code>, starting with the first tag after <code>ExclusiveStartTagKey</code> and up to the specified <code>Limit</code>.</p>"""
    has_more_tags: "capo_firehose.types.boolean_object.BooleanObject"
    """<p>If this is <code>true</code> in the response, more tags are available. To list the remaining tags, set <code>ExclusiveStartTagKey</code> to the key of the last tag returned and call <code>ListTagsForDeliveryStream</code> again.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForDeliveryStreamOutput) -> dict:
    out: dict = {}
    import capo_firehose.types.list_tags_for_delivery_stream_output_tag_list

    out["Tags"] = (
        capo_firehose.types.list_tags_for_delivery_stream_output_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    out["HasMoreTags"] = value["has_more_tags"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForDeliveryStreamOutput:
    out: ListTagsForDeliveryStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_firehose.types.list_tags_for_delivery_stream_output_tag_list

        out["tags"] = (
            capo_firehose.types.list_tags_for_delivery_stream_output_tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    if data.get("HasMoreTags") is not None:
        out["has_more_tags"] = data["HasMoreTags"]
    else:
        out["has_more_tags"] = False
    return out
