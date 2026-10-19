"""Generated from Smithy shape ``com.amazonaws.firehose#TagDeliveryStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.delivery_stream_name
    import capo_firehose.types.tag_delivery_stream_input_tag_list


class TagDeliveryStreamInput(TypedDict, closed=True):
    delivery_stream_name: "capo_firehose.types.delivery_stream_name.DeliveryStreamName"
    """<p>The name of the Firehose stream to which you want to add the tags.</p>"""
    tags: "capo_firehose.types.tag_delivery_stream_input_tag_list.TagDeliveryStreamInputTagList"
    """<p>A set of key-value pairs to use to create the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagDeliveryStreamInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import capo_firehose.types.tag_delivery_stream_input_tag_list

    out["Tags"] = (
        capo_firehose.types.tag_delivery_stream_input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagDeliveryStreamInput:
    out: TagDeliveryStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamName") is not None:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        out["delivery_stream_name"] = ""
    if data.get("Tags") is not None:
        import capo_firehose.types.tag_delivery_stream_input_tag_list

        out["tags"] = (
            capo_firehose.types.tag_delivery_stream_input_tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    return out
