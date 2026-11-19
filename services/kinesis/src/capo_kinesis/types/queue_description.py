"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_arn
    import capo_kinesis.types.queue_attributes
    import capo_kinesis.types.queue_name
    import capo_kinesis.types.queue_status
    import capo_kinesis.types.queue_stream_configuration_list
    import capo_kinesis.types.timestamp


class QueueDescription(TypedDict, closed=True):
    queue_name: "capo_kinesis.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    queue_arn: "capo_kinesis.types.queue_arn.QueueARN"
    """<p>The ARN of the queue. The resource identifier in the ARN is generated when the queue is created and is not derived from <code>QueueName</code>. Use the returned <code>QueueARN</code> to identify the queue in subsequent requests.</p>"""
    queue_status: "capo_kinesis.types.queue_status.QueueStatus"
    """<p>The current status of the queue.</p>"""
    queue_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The time the queue was created.</p>"""
    stream_configuration_list: "capo_kinesis.types.queue_stream_configuration_list.QueueStreamConfigurationList"
    """<p>The data stream the queue delivers records from, and the position in that stream where delivery begins. The list contains exactly one entry, because a queue delivers records from a single data stream.</p>"""
    queue_attributes: NotRequired["capo_kinesis.types.queue_attributes.QueueAttributes"]
    """<p>The configuration attributes of the queue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueDescription) -> dict:
    out: dict = {}
    out["QueueName"] = value["queue_name"]
    out["QueueARN"] = value["queue_arn"]
    import capo_kinesis.types.queue_status

    out["QueueStatus"] = capo_kinesis.types.queue_status.serialize_aws_json_1_1(
        value["queue_status"]
    )
    import capo_kinesis.types.timestamp

    out["QueueCreationTimestamp"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
        value["queue_creation_timestamp"]
    )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> QueueDescription:
    out: QueueDescription = {}  # type: ignore[typeddict-item]
    if data.get("QueueName") is not None:
        out["queue_name"] = data["QueueName"]
    else:
        out["queue_name"] = ""
    if data.get("QueueARN") is not None:
        out["queue_arn"] = data["QueueARN"]
    else:
        out["queue_arn"] = ""
    if data.get("QueueStatus") is not None:
        import capo_kinesis.types.queue_status

        out["queue_status"] = capo_kinesis.types.queue_status.deserialize_aws_json_1_1(
            data["QueueStatus"]
        )
    else:
        import typing

        out["queue_status"] = typing.cast(
            "capo_kinesis.types.queue_status.QueueStatus", ""
        )
    if data.get("QueueCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["queue_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["QueueCreationTimestamp"]
            )
        )
    else:
        import datetime

        out["queue_creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
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
    return out
