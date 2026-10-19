"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#GetShardIteratorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.sequence_number
    import capo_keyspacesstreams.types.shard_id
    import capo_keyspacesstreams.types.shard_iterator_type
    import capo_keyspacesstreams.types.stream_arn


class GetShardIteratorInput(TypedDict, closed=True):
    stream_arn: "capo_keyspacesstreams.types.stream_arn.StreamArn"
    """<p> The Amazon Resource Name (ARN) of the stream for which to get the shard iterator. The ARN uniquely identifies the stream within Amazon Keyspaces. </p>"""
    shard_id: "capo_keyspacesstreams.types.shard_id.ShardId"
    """<p> The identifier of the shard within the stream. The shard ID uniquely identifies a subset of the stream's data records that you want to access. </p>"""
    shard_iterator_type: (
        "capo_keyspacesstreams.types.shard_iterator_type.ShardIteratorType"
    )
    """<p> Determines how the shard iterator is positioned. Must be one of the following: </p> <ul> <li> <p> <code>TRIM_HORIZON</code> - Start reading at the last untrimmed record in the shard, which is the oldest data record in the shard.</p> </li> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Start reading exactly from the specified sequence number.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Start reading right after the specified sequence number. </p> </li> <li> <p> <code>LATEST</code> - Start reading just after the most recent record in the shard, so that you always read the most recent data. </p> </li> </ul>"""
    sequence_number: NotRequired[
        "capo_keyspacesstreams.types.sequence_number.SequenceNumber"
    ]
    """<p> The sequence number of the data record in the shard from which to start reading. Required if <code>ShardIteratorType</code> is <code>AT_SEQUENCE_NUMBER</code> or <code>AFTER_SEQUENCE_NUMBER</code>. This parameter is ignored for other iterator types. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetShardIteratorInput) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    out["shardId"] = value["shard_id"]
    import capo_keyspacesstreams.types.shard_iterator_type

    out["shardIteratorType"] = (
        capo_keyspacesstreams.types.shard_iterator_type.serialize_aws_json_1_0(
            value["shard_iterator_type"]
        )
    )
    if "sequence_number" in value:
        out["sequenceNumber"] = value["sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetShardIteratorInput:
    out: GetShardIteratorInput = {}  # type: ignore[typeddict-item]
    if data.get("streamArn") is not None:
        out["stream_arn"] = data["streamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("shardId") is not None:
        out["shard_id"] = data["shardId"]
    else:
        out["shard_id"] = ""
    if data.get("shardIteratorType") is not None:
        import capo_keyspacesstreams.types.shard_iterator_type

        out["shard_iterator_type"] = (
            capo_keyspacesstreams.types.shard_iterator_type.deserialize_aws_json_1_0(
                data["shardIteratorType"]
            )
        )
    else:
        import typing

        out["shard_iterator_type"] = typing.cast(
            "capo_keyspacesstreams.types.shard_iterator_type.ShardIteratorType", ""
        )
    if data.get("sequenceNumber") is not None:
        out["sequence_number"] = data["sequenceNumber"]
    return out
