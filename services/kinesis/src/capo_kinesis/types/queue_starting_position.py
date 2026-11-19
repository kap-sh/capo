"""Generated from Smithy shape ``com.amazonaws.kinesis#QueueStartingPosition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_starting_position_type
    import capo_kinesis.types.timestamp


class QueueStartingPosition(TypedDict, closed=True):
    type: "capo_kinesis.types.queue_starting_position_type.QueueStartingPositionType"
    """<p>You can set the starting position to one of the following values:</p> <p> <code>LATEST</code>: Delivers records that arrive after you create the queue. This is the default.</p> <p> <code>TRIM_HORIZON</code>: Start delivering at the last untrimmed record in the stream, which is the oldest record the stream still retains.</p> <p> <code>AT_TIMESTAMP</code>: Delivers records that arrive at or after a time stamp that you provide.</p>"""
    timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The approximate time from which the queue begins delivering records. Records that arrive at approximately this time or later are delivered.</p> <p>In a request, specify this value only when <code>Type</code> is <code>AT_TIMESTAMP</code>. It is required in that case, and specifying it for any other type returns a <code>ValidationException</code>.</p> <p>In a response, this value is approximate and reflects the queue's effective starting position. While the queue is <code>CREATING</code>, the response echoes what you configured: for <code>AT_TIMESTAMP</code>, the timestamp you provided, and for <code>TRIM_HORIZON</code> and <code>LATEST</code>, this member is absent because the effective position is not yet determined. Once the queue is <code>ACTIVE</code>, the response always includes this member. For <code>AT_TIMESTAMP</code>, it is the timestamp you provided or the earliest time the stream can be read from, whichever is later.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueueStartingPosition) -> dict:
    out: dict = {}
    import capo_kinesis.types.queue_starting_position_type

    out["Type"] = (
        capo_kinesis.types.queue_starting_position_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    if "timestamp" in value:
        import capo_kinesis.types.timestamp

        out["Timestamp"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueueStartingPosition:
    out: QueueStartingPosition = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_kinesis.types.queue_starting_position_type

        out["type"] = (
            capo_kinesis.types.queue_starting_position_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_kinesis.types.queue_starting_position_type.QueueStartingPositionType",
            "",
        )
    if data.get("Timestamp") is not None:
        import capo_kinesis.types.timestamp

        out["timestamp"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    return out
