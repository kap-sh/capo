"""Generated from Smithy shape ``com.amazonaws.memorydb#ShardDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.shard_configuration
    import capo_memorydb.types.string
    import capo_memorydb.types.t_stamp


class ShardDetail(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the shard</p>"""
    configuration: NotRequired[
        "capo_memorydb.types.shard_configuration.ShardConfiguration"
    ]
    """<p>The configuration details of the shard</p>"""
    size: NotRequired["capo_memorydb.types.string.String"]
    """<p>The size of the shard's snapshot</p>"""
    snapshot_creation_time: NotRequired["capo_memorydb.types.t_stamp.TStamp"]
    """<p>The date and time that the shard's snapshot was created</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShardDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import capo_memorydb.types.shard_configuration

        out["Configuration"] = (
            capo_memorydb.types.shard_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "size" in value:
        out["Size"] = value["size"]
    if "snapshot_creation_time" in value:
        import capo_memorydb.types.t_stamp

        out["SnapshotCreationTime"] = (
            capo_memorydb.types.t_stamp.serialize_aws_json_1_1(
                value["snapshot_creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShardDetail:
    out: ShardDetail = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Configuration") is not None:
        import capo_memorydb.types.shard_configuration

        out["configuration"] = (
            capo_memorydb.types.shard_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    if data.get("SnapshotCreationTime") is not None:
        import capo_memorydb.types.t_stamp

        out["snapshot_creation_time"] = (
            capo_memorydb.types.t_stamp.deserialize_aws_json_1_1(
                data["SnapshotCreationTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShardDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import capo_memorydb.types.shard_configuration

        out["Configuration"] = capo_memorydb.types.shard_configuration.serialize_cbor(
            value["configuration"]
        )
    if "size" in value:
        out["Size"] = value["size"]
    if "snapshot_creation_time" in value:
        import capo_memorydb.types.t_stamp

        out["SnapshotCreationTime"] = capo_memorydb.types.t_stamp.serialize_cbor(
            value["snapshot_creation_time"]
        )
    return out


def deserialize_cbor(data: dict) -> ShardDetail:
    out: ShardDetail = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Configuration") is not None:
        import capo_memorydb.types.shard_configuration

        out["configuration"] = capo_memorydb.types.shard_configuration.deserialize_cbor(
            data["Configuration"]
        )
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    if data.get("SnapshotCreationTime") is not None:
        import capo_memorydb.types.t_stamp

        out["snapshot_creation_time"] = capo_memorydb.types.t_stamp.deserialize_cbor(
            data["SnapshotCreationTime"]
        )
    return out
