"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueFleetAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.update_queue_fleet_association_status


class UpdateQueueFleetAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID to update.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID to update.</p>"""
    status: "capo_deadline.types.update_queue_fleet_association_status.UpdateQueueFleetAssociationStatus"
    """<p>The status to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueFleetAssociationRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.update_queue_fleet_association_status

    out["status"] = (
        capo_deadline.types.update_queue_fleet_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQueueFleetAssociationRequest:
    out: UpdateQueueFleetAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_deadline.types.update_queue_fleet_association_status

        out["status"] = (
            capo_deadline.types.update_queue_fleet_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.update_queue_fleet_association_status.UpdateQueueFleetAssociationStatus",
            "",
        )
    return out
