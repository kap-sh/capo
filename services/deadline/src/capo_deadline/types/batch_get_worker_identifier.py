"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.worker_id


class BatchGetWorkerIdentifier(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the worker."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the worker."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerIdentifier) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    return out


def deserialize_json(data: dict) -> BatchGetWorkerIdentifier:
    out: BatchGetWorkerIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("workerId") is not None:
        out["worker_id"] = data["workerId"]
    else:
        out["worker_id"] = ""
    return out
