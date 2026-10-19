"""Generated from Smithy shape ``com.amazonaws.kinesis#ChildShard``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.hash_key_range
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.shard_id_list


class ChildShard(TypedDict, closed=True):
    shard_id: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the existing child shard of the current shard.</p>"""
    parent_shards: "capo_kinesis.types.shard_id_list.ShardIdList"
    """<p>The current shard that is the parent of the existing child shard.</p>"""
    hash_key_range: "capo_kinesis.types.hash_key_range.HashKeyRange"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChildShard) -> dict:
    out: dict = {}
    out["ShardId"] = value["shard_id"]
    import capo_kinesis.types.shard_id_list

    out["ParentShards"] = capo_kinesis.types.shard_id_list.serialize_aws_json_1_1(
        value["parent_shards"]
    )
    import capo_kinesis.types.hash_key_range

    out["HashKeyRange"] = capo_kinesis.types.hash_key_range.serialize_aws_json_1_1(
        value["hash_key_range"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChildShard:
    out: ChildShard = {}  # type: ignore[typeddict-item]
    if data.get("ShardId") is not None:
        out["shard_id"] = data["ShardId"]
    else:
        out["shard_id"] = ""
    if data.get("ParentShards") is not None:
        import capo_kinesis.types.shard_id_list

        out["parent_shards"] = (
            capo_kinesis.types.shard_id_list.deserialize_aws_json_1_1(
                data["ParentShards"]
            )
        )
    else:
        out["parent_shards"] = []
    if data.get("HashKeyRange") is not None:
        import capo_kinesis.types.hash_key_range

        out["hash_key_range"] = (
            capo_kinesis.types.hash_key_range.deserialize_aws_json_1_1(
                data["HashKeyRange"]
            )
        )
    else:
        raise DeserializationError("ChildShard.hash_key_range required")
    return out
