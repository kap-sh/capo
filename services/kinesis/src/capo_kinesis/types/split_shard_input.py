"""Generated from Smithy shape ``com.amazonaws.kinesis#SplitShardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.hash_key
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class SplitShardInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream for the shard split.</p>"""
    shard_to_split: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the shard to split.</p>"""
    new_starting_hash_key: "capo_kinesis.types.hash_key.HashKey"
    """<p>A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for <code>NewStartingHashKey</code> must be in the range of hash keys being mapped into the shard. The <code>NewStartingHashKey</code> hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitShardInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["ShardToSplit"] = value["shard_to_split"]
    out["NewStartingHashKey"] = value["new_starting_hash_key"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SplitShardInput:
    out: SplitShardInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("ShardToSplit") is not None:
        out["shard_to_split"] = data["ShardToSplit"]
    else:
        out["shard_to_split"] = ""
    if data.get("NewStartingHashKey") is not None:
        out["new_starting_hash_key"] = data["NewStartingHashKey"]
    else:
        out["new_starting_hash_key"] = ""
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
