"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.worker_id


class DeleteWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the worker to delete."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the worker to delete."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID of the worker to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkerRequest:
    out: DeleteWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
