"""Generated from Smithy shape ``com.amazonaws.kinesis#StartingPosition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.shard_iterator_type
    import capo_kinesis.types.timestamp


class StartingPosition(TypedDict, closed=True):
    type: "capo_kinesis.types.shard_iterator_type.ShardIteratorType"
    """<p>You can set the starting position to one of the following values:</p> <p> <code>AT_SEQUENCE_NUMBER</code>: Start streaming from the position denoted by the sequence number specified in the <code>SequenceNumber</code> field.</p> <p> <code>AFTER_SEQUENCE_NUMBER</code>: Start streaming right after the position denoted by the sequence number specified in the <code>SequenceNumber</code> field.</p> <p> <code>AT_TIMESTAMP</code>: Start streaming from the position denoted by the time stamp specified in the <code>Timestamp</code> field.</p> <p> <code>TRIM_HORIZON</code>: Start streaming at the last untrimmed record in the shard, which is the oldest data record in the shard.</p> <p> <code>LATEST</code>: Start streaming just after the most recent record in the shard, so that you always read the most recent data in the shard.</p>"""
    sequence_number: NotRequired["capo_kinesis.types.sequence_number.SequenceNumber"]
    """<p>The sequence number of the data record in the shard from which to start streaming. To specify a sequence number, set <code>StartingPosition</code> to <code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>.</p>"""
    timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The time stamp of the data record from which to start reading. To specify a time stamp, set <code>StartingPosition</code> to <code>Type AT_TIMESTAMP</code>. A time stamp is the Unix epoch date with precision in milliseconds. For example, <code>2016-04-04T19:58:46.480-00:00</code> or <code>1459799926.480</code>. If a record with this exact time stamp does not exist, records will be streamed from the next (later) record. If the time stamp is older than the current trim horizon, records will be streamed from the oldest untrimmed data record (<code>TRIM_HORIZON</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartingPosition) -> dict:
    out: dict = {}
    import capo_kinesis.types.shard_iterator_type

    out["Type"] = capo_kinesis.types.shard_iterator_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    if "timestamp" in value:
        import capo_kinesis.types.timestamp

        out["Timestamp"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartingPosition:
    out: StartingPosition = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_kinesis.types.shard_iterator_type

        out["type"] = capo_kinesis.types.shard_iterator_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_kinesis.types.shard_iterator_type.ShardIteratorType", ""
        )
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    if data.get("Timestamp") is not None:
        import capo_kinesis.types.timestamp

        out["timestamp"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    return out
