"""Generated from Smithy shape ``com.amazonaws.kinesis#MergeShardsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class MergeShardsInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream for the merge.</p>"""
    shard_to_merge: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the shard to combine with the adjacent shard for the merge.</p>"""
    adjacent_shard_to_merge: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the adjacent shard for the merge.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeShardsInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["ShardToMerge"] = value["shard_to_merge"]
    out["AdjacentShardToMerge"] = value["adjacent_shard_to_merge"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeShardsInput:
    out: MergeShardsInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("ShardToMerge") is not None:
        out["shard_to_merge"] = data["ShardToMerge"]
    else:
        out["shard_to_merge"] = ""
    if data.get("AdjacentShardToMerge") is not None:
        out["adjacent_shard_to_merge"] = data["AdjacentShardToMerge"]
    else:
        out["adjacent_shard_to_merge"] = ""
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
