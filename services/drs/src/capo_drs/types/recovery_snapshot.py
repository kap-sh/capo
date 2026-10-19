"""Generated from Smithy shape ``com.amazonaws.drs#RecoverySnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.ebs_snapshots_list
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_snapshot_id
    import capo_drs.types.source_server_id


class RecoverySnapshot(TypedDict, closed=True):
    snapshot_id: "capo_drs.types.recovery_snapshot_id.RecoverySnapshotID"
    """<p>The ID of the Recovery Snapshot.</p>"""
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server that the snapshot was taken for.</p>"""
    expected_timestamp: "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    """<p>The timestamp of when we expect the snapshot to be taken.</p>"""
    timestamp: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The actual timestamp that the snapshot was taken.</p>"""
    ebs_snapshots: NotRequired["capo_drs.types.ebs_snapshots_list.EbsSnapshotsList"]
    """<p>A list of EBS snapshots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoverySnapshot) -> dict:
    out: dict = {}
    out["snapshotID"] = value["snapshot_id"]
    out["sourceServerID"] = value["source_server_id"]
    out["expectedTimestamp"] = value["expected_timestamp"]
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "ebs_snapshots" in value:
        import capo_drs.types.ebs_snapshots_list

        out["ebsSnapshots"] = capo_drs.types.ebs_snapshots_list.serialize_json(
            value["ebs_snapshots"]
        )
    return out


def deserialize_json(data: dict) -> RecoverySnapshot:
    out: RecoverySnapshot = {}  # type: ignore[typeddict-item]
    if data.get("snapshotID") is not None:
        out["snapshot_id"] = data["snapshotID"]
    else:
        out["snapshot_id"] = ""
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("expectedTimestamp") is not None:
        out["expected_timestamp"] = data["expectedTimestamp"]
    else:
        out["expected_timestamp"] = ""
    if data.get("timestamp") is not None:
        out["timestamp"] = data["timestamp"]
    if data.get("ebsSnapshots") is not None:
        import capo_drs.types.ebs_snapshots_list

        out["ebs_snapshots"] = capo_drs.types.ebs_snapshots_list.deserialize_json(
            data["ebsSnapshots"]
        )
    return out
