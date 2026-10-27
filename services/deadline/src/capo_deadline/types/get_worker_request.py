"""Generated from Smithy shape ``com.amazonaws.deadline#GetWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.worker_id


class GetWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the worker."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the worker."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkerRequest:
    out: GetWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
