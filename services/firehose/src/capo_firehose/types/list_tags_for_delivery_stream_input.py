"""Generated from Smithy shape ``com.amazonaws.firehose#ListTagsForDeliveryStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.list_tags_for_delivery_stream_input_limit
    import capo_firehose.types.tag_key


class ListTagsForDeliveryStreamInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream whose tags you want to list.</p>"""
    exclusive_start_tag_key: NotRequired["capo_firehose.types.tag_key.TagKey"]
    """<p>The key to use as the starting point for the list of tags. If you set this parameter, <code>ListTagsForDeliveryStream</code> gets all tags that occur after <code>ExclusiveStartTagKey</code>.</p>"""
    limit: NotRequired[
        "capo_firehose.types.list_tags_for_delivery_stream_input_limit.ListTagsForDeliveryStreamInputLimit"
    ]
    """<p>The number of tags to return. If this number is less than the total number of tags associated with the Firehose stream, <code>HasMoreTags</code> is set to <code>true</code> in the response. To list additional tags, set <code>ExclusiveStartTagKey</code> to the last key in the response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    if "exclusive_start_tag_key" in value:
        out["ExclusiveStartTagKey"] = value["exclusive_start_tag_key"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForDeliveryStreamInput:
    out: ListTagsForDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("ExclusiveStartTagKey") is not None:
        out["exclusive_start_tag_key"] = data["ExclusiveStartTagKey"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
