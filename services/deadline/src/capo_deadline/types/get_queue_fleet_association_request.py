"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_id


class GetQueueFleetAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm that contains the queue-fleet association."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the queue-fleet association."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID for the queue-fleet association."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueFleetAssociationRequest:
    out: GetQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
