"""Generated from Smithy shape ``com.amazonaws.drs#ReverseReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_id


class ReverseReplicationRequest(TypedDict, closed=True):
    recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID"
    """<p>The ID of the Recovery Instance that we want to reverse the replication for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReverseReplicationRequest) -> dict:
    out: dict = {}
    out["recoveryInstanceID"] = value["recovery_instance_id"]
    return out


def deserialize_json(data: dict) -> ReverseReplicationRequest:
    out: ReverseReplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryInstanceID") is not None:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    else:
        out["recovery_instance_id"] = ""
    return out
