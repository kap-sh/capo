"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_id


class CreateQueueFleetAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The ID of the farm that the queue and fleet belong to.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["fleetId"] = value["fleet_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueFleetAssociationRequest:
    out: CreateQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    return out
