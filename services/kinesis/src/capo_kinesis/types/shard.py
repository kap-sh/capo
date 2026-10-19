"""Generated from Smithy shape ``com.amazonaws.kinesis#Shard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.hash_key_range
    import capo_kinesis.types.sequence_number_range
    import capo_kinesis.types.shard_id


class Shard(TypedDict, closed=True):
    shard_id: "capo_kinesis.types.shard_id.ShardId"
    """<p>The unique identifier of the shard within the stream.</p>"""
    parent_shard_id: NotRequired["capo_kinesis.types.shard_id.ShardId"]
    """<p>The shard ID of the shard's parent.</p>"""
    adjacent_parent_shard_id: NotRequired["capo_kinesis.types.shard_id.ShardId"]
    """<p>The shard ID of the shard adjacent to the shard's parent.</p>"""
    hash_key_range: "capo_kinesis.types.hash_key_range.HashKeyRange"
    """<p>The range of possible hash key values for the shard, which is a set of ordered contiguous positive integers.</p>"""
    sequence_number_range: (
        "capo_kinesis.types.sequence_number_range.SequenceNumberRange"
    )
    """<p>The range of possible sequence numbers for the shard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Shard) -> dict:
    out: dict = {}
    out["ShardId"] = value["shard_id"]
    if "parent_shard_id" in value:
        out["ParentShardId"] = value["parent_shard_id"]
    if "adjacent_parent_shard_id" in value:
        out["AdjacentParentShardId"] = value["adjacent_parent_shard_id"]
    import capo_kinesis.types.hash_key_range

    out["HashKeyRange"] = capo_kinesis.types.hash_key_range.serialize_aws_json_1_1(
        value["hash_key_range"]
    )
    import capo_kinesis.types.sequence_number_range

    out["SequenceNumberRange"] = (
        capo_kinesis.types.sequence_number_range.serialize_aws_json_1_1(
            value["sequence_number_range"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Shard:
    out: Shard = {}  # type: ignore[typeddict-item]
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    else:
        out["shard_id"] = ""
    if data.get("ParentShardId") is not None:
        out["parent_shard_id"] = data["ParentShardId"]
    if data.get("AdjacentParentShardId") is not None:
        out["adjacent_parent_shard_id"] = data["AdjacentParentShardId"]
    if data.get("HashKeyRange") is not None:
        import capo_kinesis.types.hash_key_range

        out["hash_key_range"] = (
            capo_kinesis.types.hash_key_range.deserialize_aws_json_1_1(
                data["HashKeyRange"]
            )
        )
    else:
        raise DeserializationError("Shard.hash_key_range required")
    if data.get("SequenceNumberRange") is not None:
        import capo_kinesis.types.sequence_number_range

        out["sequence_number_range"] = (
            capo_kinesis.types.sequence_number_range.deserialize_aws_json_1_1(
                data["SequenceNumberRange"]
            )
        )
    else:
        raise DeserializationError("Shard.sequence_number_range required")
    return out
