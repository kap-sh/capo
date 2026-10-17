"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#GetShardIteratorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb_streams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.sequence_number
    import capo_dynamodb_streams.types.shard_id
    import capo_dynamodb_streams.types.shard_iterator_type
    import capo_dynamodb_streams.types.stream_arn


class GetShardIteratorInput(TypedDict, closed=True):
    stream_arn: "capo_dynamodb_streams.types.stream_arn.StreamArn"
    """<p>The Amazon Resource Name (ARN) for the stream.</p>"""
    shard_id: "capo_dynamodb_streams.types.shard_id.ShardId"
    """<p>The identifier of the shard. The iterator will be returned for this shard ID.</p>"""
    shard_iterator_type: (
        "capo_dynamodb_streams.types.shard_iterator_type.ShardIteratorType"
    )
    """<p>Determines how the shard iterator is used to start reading stream records from the shard:</p> <ul> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Start reading exactly from the position denoted by a specific sequence number.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Start reading right after the position denoted by a specific sequence number.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream.</p> </li> <li> <p> <code>LATEST</code> - Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard.</p> </li> </ul>"""
    sequence_number: NotRequired[
        "capo_dynamodb_streams.types.sequence_number.SequenceNumber"
    ]
    """<p>The sequence number of a stream record in the shard from which to start reading.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetShardIteratorInput) -> dict:
    out: dict = {}
    out["StreamArn"] = value["stream_arn"]
    out["ShardId"] = value["shard_id"]
    import capo_dynamodb_streams.types.shard_iterator_type

    out["ShardIteratorType"] = (
        capo_dynamodb_streams.types.shard_iterator_type.serialize_aws_json_1_0(
            value["shard_iterator_type"]
        )
    )
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetShardIteratorInput:
    out: GetShardIteratorInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    else:
        raise DeserializationError("GetShardIteratorInput.stream_arn required")
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    else:
        raise DeserializationError("GetShardIteratorInput.shard_id required")
    if data.get("ShardIteratorType") is not None:
        import capo_dynamodb_streams.types.shard_iterator_type

        out["shard_iterator_type"] = (
            capo_dynamodb_streams.types.shard_iterator_type.deserialize_aws_json_1_0(
                data["ShardIteratorType"]
            )
        )
    else:
        raise DeserializationError("GetShardIteratorInput.shard_iterator_type required")
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    return out
