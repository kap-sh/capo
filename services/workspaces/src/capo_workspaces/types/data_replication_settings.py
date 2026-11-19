"""Generated from Smithy shape ``com.amazonaws.workspaces#DataReplicationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.data_replication
    import capo_workspaces.types.timestamp


class DataReplicationSettings(TypedDict, closed=True):
    data_replication: NotRequired[
        "capo_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates whether data replication is enabled, and if enabled, the type of data replication.</p>"""
    recovery_snapshot_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataReplicationSettings) -> dict:
    out: dict = {}
    if "data_replication" in value:
        import capo_workspaces.types.data_replication

        out["DataReplication"] = (
            capo_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    if "recovery_snapshot_time" in value:
        import capo_workspaces.types.timestamp

        out["RecoverySnapshotTime"] = (
            capo_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["recovery_snapshot_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataReplicationSettings:
    out: DataReplicationSettings = {}  # type: ignore[typeddict-item]
    if data.get("DataReplication") is not None:
        import capo_workspaces.types.data_replication

        out["data_replication"] = (
            capo_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    if data.get("RecoverySnapshotTime") is not None:
        import capo_workspaces.types.timestamp

        out["recovery_snapshot_time"] = (
            capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["RecoverySnapshotTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataReplicationSettings) -> dict:
    out: dict = {}
    if "data_replication" in value:
        import capo_workspaces.types.data_replication

        out["DataReplication"] = capo_workspaces.types.data_replication.serialize_cbor(
            value["data_replication"]
        )
    if "recovery_snapshot_time" in value:
        import capo_workspaces.types.timestamp

        out["RecoverySnapshotTime"] = capo_workspaces.types.timestamp.serialize_cbor(
            value["recovery_snapshot_time"]
        )
    return out


def deserialize_cbor(data: dict) -> DataReplicationSettings:
    out: DataReplicationSettings = {}  # type: ignore[typeddict-item]
    if data.get("DataReplication") is not None:
        import capo_workspaces.types.data_replication

        out["data_replication"] = (
            capo_workspaces.types.data_replication.deserialize_cbor(
                data["DataReplication"]
            )
        )
    if data.get("RecoverySnapshotTime") is not None:
        import capo_workspaces.types.timestamp

        out["recovery_snapshot_time"] = (
            capo_workspaces.types.timestamp.deserialize_cbor(
                data["RecoverySnapshotTime"]
            )
        )
    return out
