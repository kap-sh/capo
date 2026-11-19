"""Generated from Smithy shape ``com.amazonaws.kinesis#CreateQueueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_attributes
    import capo_kinesis.types.queue_name
    import capo_kinesis.types.queue_stream_configuration_list
    import capo_kinesis.types.tag_map


class CreateQueueInput(TypedDict, closed=True):
    queue_name: "capo_kinesis.types.queue_name.QueueName"
    """<p>A name for the queue. The name is scoped to the Amazon Web Services account and Region used by the request, so two queues in different accounts, or in the same account and different Regions, can have the same name.</p>"""
    stream_configuration_list: "capo_kinesis.types.queue_stream_configuration_list.QueueStreamConfigurationList"
    """<p>The data stream the queue delivers records from, and the position in that stream where delivery begins. The list must contain exactly one entry, because a queue delivers records from a single data stream.</p>"""
    queue_attributes: NotRequired["capo_kinesis.types.queue_attributes.QueueAttributes"]
    """<p>The configuration attributes for the queue, including its visibility timeout and its dead-letter handling configuration.</p>"""
    tags: NotRequired["capo_kinesis.types.tag_map.TagMap"]
    """<p>A set of up to 50 key-value pairs to apply to the queue. You can also add, change, and remove tags after the queue is created with <a>TagResource</a> and <a>UntagResource</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateQueueInput) -> dict:
    out: dict = {}
    out["QueueName"] = value["queue_name"]
    import capo_kinesis.types.queue_stream_configuration_list

    out["StreamConfigurationList"] = (
        capo_kinesis.types.queue_stream_configuration_list.serialize_aws_json_1_1(
            value["stream_configuration_list"]
        )
    )
    if "queue_attributes" in value:
        import capo_kinesis.types.queue_attributes

        out["QueueAttributes"] = (
            capo_kinesis.types.queue_attributes.serialize_aws_json_1_1(
                value["queue_attributes"]
            )
        )
    if "tags" in value:
        import capo_kinesis.types.tag_map

        out["Tags"] = capo_kinesis.types.tag_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateQueueInput:
    out: CreateQueueInput = {}  # type: ignore[typeddict-item]
    if data.get("QueueName") is not None:
        out["queue_name"] = data["QueueName"]
    else:
        out["queue_name"] = ""
    if data.get("StreamConfigurationList") is not None:
        import capo_kinesis.types.queue_stream_configuration_list

        out["stream_configuration_list"] = (
            capo_kinesis.types.queue_stream_configuration_list.deserialize_aws_json_1_1(
                data["StreamConfigurationList"]
            )
        )
    else:
        out["stream_configuration_list"] = []
    if data.get("QueueAttributes") is not None:
        import capo_kinesis.types.queue_attributes

        out["queue_attributes"] = (
            capo_kinesis.types.queue_attributes.deserialize_aws_json_1_1(
                data["QueueAttributes"]
            )
        )
    if data.get("Tags") is not None:
        import capo_kinesis.types.tag_map

        out["tags"] = capo_kinesis.types.tag_map.deserialize_aws_json_1_1(data["Tags"])
    return out
