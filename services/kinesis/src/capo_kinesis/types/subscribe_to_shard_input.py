"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.consumer_arn
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.starting_position
    import capo_kinesis.types.stream_id


class SubscribeToShardInput(TypedDict, closed=True):
    consumer_arn: "capo_kinesis.types.consumer_arn.ConsumerARN"
    """<p>For this parameter, use the value you obtained when you called <a>RegisterStreamConsumer</a>.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    shard_id: "capo_kinesis.types.shard_id.ShardId"
    """<p>The ID of the shard you want to subscribe to. To see a list of all the shards for a given stream, use <a>ListShards</a>.</p>"""
    starting_position: "capo_kinesis.types.starting_position.StartingPosition"
    """<p>The starting position in the data stream from which to start streaming.</p>"""
    dry_run: NotRequired["capo_kinesis.types.boolean_object.BooleanObject"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribeToShardInput) -> dict:
    out: dict = {}
    out["ConsumerARN"] = value["consumer_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    out["ShardId"] = value["shard_id"]
    import capo_kinesis.types.starting_position

    out["StartingPosition"] = (
        capo_kinesis.types.starting_position.serialize_aws_json_1_1(
            value["starting_position"]
        )
    )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribeToShardInput:
    out: SubscribeToShardInput = {}  # type: ignore[typeddict-item]
    if data.get("ConsumerARN") is not None:
        out["consumer_arn"] = data["ConsumerARN"]
    else:
        out["consumer_arn"] = ""
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    else:
        out["shard_id"] = ""
    if data.get("StartingPosition") is not None:
        import capo_kinesis.types.starting_position

        out["starting_position"] = (
            capo_kinesis.types.starting_position.deserialize_aws_json_1_1(
                data["StartingPosition"]
            )
        )
    else:
        raise DeserializationError("SubscribeToShardInput.starting_position required")
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
