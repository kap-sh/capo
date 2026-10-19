"""Generated from Smithy shape ``com.amazonaws.kinesis#GetShardIteratorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.shard_iterator_type
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.timestamp


class GetShardIteratorInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the Amazon Kinesis data stream.</p>"""
    shard_id: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the Kinesis Data Streams shard to get the iterator for.</p>"""
    shard_iterator_type: "capo_kinesis.types.shard_iterator_type.ShardIteratorType"
    """<p>Determines how the shard iterator is used to start reading data records from the shard.</p> <p>The following are the valid Amazon Kinesis shard iterator types:</p> <ul> <li> <p>AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value <code>StartingSequenceNumber</code>.</p> </li> <li> <p>AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value <code>StartingSequenceNumber</code>.</p> </li> <li> <p>AT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value <code>Timestamp</code>.</p> </li> <li> <p>TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.</p> </li> <li> <p>LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.</p> </li> </ul>"""
    starting_sequence_number: NotRequired[
        "capo_kinesis.types.sequence_number.SequenceNumber"
    ]
    """<p>The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.</p>"""
    timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The time stamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, <code>2016-04-04T19:58:46.480-00:00</code> or <code>1459799926.480</code>. If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    dry_run: NotRequired["capo_kinesis.types.boolean_object.BooleanObject"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetShardIteratorInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["ShardId"] = value["shard_id"]
    import capo_kinesis.types.shard_iterator_type

    out["ShardIteratorType"] = (
        capo_kinesis.types.shard_iterator_type.serialize_aws_json_1_1(
            value["shard_iterator_type"]
        )
    )
    if "starting_sequence_number" in value:
        out["StartingSequenceNumber"] = value["starting_sequence_number"]
    if "timestamp" in value:
        import capo_kinesis.types.timestamp

        out["Timestamp"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetShardIteratorInput:
    out: GetShardIteratorInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    else:
        out["shard_id"] = ""
    if data.get("ShardIteratorType") is not None:
        import capo_kinesis.types.shard_iterator_type

        out["shard_iterator_type"] = (
            capo_kinesis.types.shard_iterator_type.deserialize_aws_json_1_1(
                data["ShardIteratorType"]
            )
        )
    else:
        import typing

        out["shard_iterator_type"] = typing.cast(
            "capo_kinesis.types.shard_iterator_type.ShardIteratorType", ""
        )
    if data.get("StartingSequenceNumber") is not None:
        out["starting_sequence_number"] = data["StartingSequenceNumber"]
    if data.get("Timestamp") is not None:
        import capo_kinesis.types.timestamp

        out["timestamp"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
