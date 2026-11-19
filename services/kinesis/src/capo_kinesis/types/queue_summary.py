"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_arn
    import capo_kinesis.types.queue_name
    import capo_kinesis.types.queue_status
    import capo_kinesis.types.queue_stream_identifier_list
    import capo_kinesis.types.timestamp


class QueueSummary(TypedDict, closed=True):
    queue_name: "capo_kinesis.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    queue_arn: "capo_kinesis.types.queue_arn.QueueARN"
    """<p>The ARN of the queue.</p>"""
    queue_status: "capo_kinesis.types.queue_status.QueueStatus"
    """<p>The current status of the queue.</p>"""
    queue_creation_timestamp: "capo_kinesis.types.timestamp.Timestamp"
    """<p>The time the queue was created.</p>"""
    streams: "capo_kinesis.types.queue_stream_identifier_list.QueueStreamIdentifierList"
    """<p>The data stream the queue delivers records from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueSummary) -> dict:
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
    import capo_kinesis.types.queue_stream_identifier_list

    out["Streams"] = (
        capo_kinesis.types.queue_stream_identifier_list.serialize_aws_json_1_1(
            value["streams"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueueSummary:
    out: QueueSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("Streams") is not None:
        import capo_kinesis.types.queue_stream_identifier_list

        out["streams"] = (
            capo_kinesis.types.queue_stream_identifier_list.deserialize_aws_json_1_1(
                data["Streams"]
            )
        )
    else:
        out["streams"] = []
    return out
