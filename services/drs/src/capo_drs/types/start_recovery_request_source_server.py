"""Generated from Smithy shape ``com.amazonaws.drs#StartRecoveryRequestSourceServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_snapshot_id
    import capo_drs.types.source_server_id


class StartRecoveryRequestSourceServer(TypedDict, closed=True):
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server you want to recover.</p>"""
    recovery_snapshot_id: NotRequired[
        "capo_drs.types.recovery_snapshot_id.RecoverySnapshotID"
    ]
    """<p>The ID of a Recovery Snapshot we want to recover from. Omit this field to launch from the latest data by taking an on-demand snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecoveryRequestSourceServer) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "recovery_snapshot_id" in value:
        out["recoverySnapshotID"] = value["recovery_snapshot_id"]
    return out


def deserialize_json(data: dict) -> StartRecoveryRequestSourceServer:
    out: StartRecoveryRequestSourceServer = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("recoverySnapshotID") is not None:
        out["recovery_snapshot_id"] = data["recoverySnapshotID"]
    return out
