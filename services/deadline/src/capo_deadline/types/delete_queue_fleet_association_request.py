"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_id


class DeleteQueueFleetAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm that holds the queue-fleet association."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the queue-fleet association."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the queue-fleet association."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueFleetAssociationRequest:
    out: DeleteQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
