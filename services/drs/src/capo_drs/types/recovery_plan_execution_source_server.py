"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanExecutionSourceServer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_snapshot_id
    import capo_drs.types.source_server_id


class RecoveryPlanExecutionSourceServer(TypedDict, closed=True):
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the source server.</p>"""
    recovery_snapshot_id: "capo_drs.types.recovery_snapshot_id.RecoverySnapshotID"
    """<p>The ID of the recovery snapshot to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanExecutionSourceServer) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    out["recoverySnapshotID"] = value["recovery_snapshot_id"]
    return out


def deserialize_json(data: dict) -> RecoveryPlanExecutionSourceServer:
    out: RecoveryPlanExecutionSourceServer = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("recoverySnapshotID") is not None:
        out["recovery_snapshot_id"] = data["recoverySnapshotID"]
    else:
        out["recovery_snapshot_id"] = ""
    return out
