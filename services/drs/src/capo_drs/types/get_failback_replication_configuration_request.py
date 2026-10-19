"""Generated from Smithy shape ``com.amazonaws.drs#GetFailbackReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_id


class GetFailbackReplicationConfigurationRequest(TypedDict, closed=True):
    recovery_instance_id: "capo_drs.types.recovery_instance_id.RecoveryInstanceID"
    """<p>The ID of the Recovery Instance whose failback replication configuration should be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFailbackReplicationConfigurationRequest) -> dict:
    out: dict = {}
    out["recoveryInstanceID"] = value["recovery_instance_id"]
    return out


def deserialize_json(data: dict) -> GetFailbackReplicationConfigurationRequest:
    out: GetFailbackReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryInstanceID") is not None:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    else:
        out["recovery_instance_id"] = ""
    return out
