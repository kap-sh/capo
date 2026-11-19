"""Generated from Smithy shape ``com.amazonaws.mgn#DataReplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.data_replication_error
    import capo_mgn.types.data_replication_info_replicated_disks
    import capo_mgn.types.data_replication_initiation
    import capo_mgn.types.data_replication_state
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.iso8601_duration_string
    import capo_mgn.types.outpost_arn
    import capo_mgn.types.replicator_id


class DataReplicationInfo(TypedDict, closed=True):
    lag_duration: NotRequired[
        "capo_mgn.types.iso8601_duration_string.ISO8601DurationString"
    ]
    """<p>Request to query data replication lag duration.</p>"""
    eta_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to query the time when data replication will be complete.</p>"""
    replicated_disks: NotRequired[
        "capo_mgn.types.data_replication_info_replicated_disks.DataReplicationInfoReplicatedDisks"
    ]
    """<p>Request to query disks replicated.</p>"""
    data_replication_state: NotRequired[
        "capo_mgn.types.data_replication_state.DataReplicationState"
    ]
    """<p>Request to query the data replication state.</p>"""
    data_replication_initiation: NotRequired[
        "capo_mgn.types.data_replication_initiation.DataReplicationInitiation"
    ]
    """<p>Request to query whether data replication has been initiated.</p>"""
    data_replication_error: NotRequired[
        "capo_mgn.types.data_replication_error.DataReplicationError"
    ]
    """<p>Error in obtaining data replication info.</p>"""
    last_snapshot_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to query data replication last snapshot time.</p>"""
    replicator_id: NotRequired["capo_mgn.types.replicator_id.ReplicatorID"]
    """<p>Replication server instance ID.</p>"""
    staging_outpost_arn: NotRequired["capo_mgn.types.outpost_arn.OutpostARN"]
    """<p>The ARN of the AWS Outpost that hosts the staging area, when the staging area subnet is on an Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInfo) -> dict:
    out: dict = {}
    if "lag_duration" in value:
        out["lagDuration"] = value["lag_duration"]
    if "eta_date_time" in value:
        out["etaDateTime"] = value["eta_date_time"]
    if "replicated_disks" in value:
        import capo_mgn.types.data_replication_info_replicated_disks

        out["replicatedDisks"] = (
            capo_mgn.types.data_replication_info_replicated_disks.serialize_json(
                value["replicated_disks"]
            )
        )
    if "data_replication_state" in value:
        out["dataReplicationState"] = value["data_replication_state"]
    if "data_replication_initiation" in value:
        import capo_mgn.types.data_replication_initiation

        out["dataReplicationInitiation"] = (
            capo_mgn.types.data_replication_initiation.serialize_json(
                value["data_replication_initiation"]
            )
        )
    if "data_replication_error" in value:
        import capo_mgn.types.data_replication_error

        out["dataReplicationError"] = (
            capo_mgn.types.data_replication_error.serialize_json(
                value["data_replication_error"]
            )
        )
    if "last_snapshot_date_time" in value:
        out["lastSnapshotDateTime"] = value["last_snapshot_date_time"]
    if "replicator_id" in value:
        out["replicatorId"] = value["replicator_id"]
    if "staging_outpost_arn" in value:
        out["stagingOutpostArn"] = value["staging_outpost_arn"]
    return out


def deserialize_json(data: dict) -> DataReplicationInfo:
    out: DataReplicationInfo = {}  # type: ignore[typeddict-item]
    if data.get("lagDuration") is not None:
        out["lag_duration"] = data["lagDuration"]
    if data.get("etaDateTime") is not None:
        out["eta_date_time"] = data["etaDateTime"]
    if data.get("replicatedDisks") is not None:
        import capo_mgn.types.data_replication_info_replicated_disks

        out["replicated_disks"] = (
            capo_mgn.types.data_replication_info_replicated_disks.deserialize_json(
                data["replicatedDisks"]
            )
        )
    if data.get("dataReplicationState") is not None:
        out["data_replication_state"] = data["dataReplicationState"]
    if data.get("dataReplicationInitiation") is not None:
        import capo_mgn.types.data_replication_initiation

        out["data_replication_initiation"] = (
            capo_mgn.types.data_replication_initiation.deserialize_json(
                data["dataReplicationInitiation"]
            )
        )
    if data.get("dataReplicationError") is not None:
        import capo_mgn.types.data_replication_error

        out["data_replication_error"] = (
            capo_mgn.types.data_replication_error.deserialize_json(
                data["dataReplicationError"]
            )
        )
    if data.get("lastSnapshotDateTime") is not None:
        out["last_snapshot_date_time"] = data["lastSnapshotDateTime"]
    if data.get("replicatorId") is not None:
        out["replicator_id"] = data["replicatorId"]
    if data.get("stagingOutpostArn") is not None:
        out["staging_outpost_arn"] = data["stagingOutpostArn"]
    return out
