"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class ShardConfiguration(TypedDict, closed=True):
    slots: NotRequired["capo_memorydb.types.string.String"]
    """<p>A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format startkey-endkey.</p>"""
    replica_count: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of read replica nodes in this shard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardConfiguration) -> dict:
    out: dict = {}
    if "slots" in value:
        out["Slots"] = value["slots"]
    if "replica_count" in value:
        out["ReplicaCount"] = value["replica_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ShardConfiguration:
    out: ShardConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Slots") is not None:
        out["slots"] = data["Slots"]
    if data.get("ReplicaCount") is not None:
        out["replica_count"] = data["ReplicaCount"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShardConfiguration) -> dict:
    out: dict = {}
    if "slots" in value:
        out["Slots"] = value["slots"]
    if "replica_count" in value:
        out["ReplicaCount"] = value["replica_count"]
    return out


def deserialize_cbor(data: dict) -> ShardConfiguration:
    out: ShardConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Slots") is not None:
        out["slots"] = data["Slots"]
    if data.get("ReplicaCount") is not None:
        out["replica_count"] = data["ReplicaCount"]
    return out
