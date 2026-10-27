"""Generated from Smithy shape ``com.amazonaws.deadline#QueueFleetAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.fleet_id
    import capo_deadline.types.queue_fleet_association_status
    import capo_deadline.types.queue_id
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class QueueFleetAssociationSummary(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID."""
    status: (
        "capo_deadline.types.queue_fleet_association_status.QueueFleetAssociationStatus"
    )
    """<p>The status of task scheduling in the queue-fleet association.</p> <ul> <li> <p> <code>ACTIVE</code>–Association is active.</p> </li> <li> <p> <code>STOP_SCHEDULING_AND_COMPLETE_TASKS</code>–Association has stopped scheduling new tasks and is completing current tasks.</p> </li> <li> <p> <code>STOP_SCHEDULING_AND_CANCEL_TASKS</code>–Association has stopped scheduling new tasks and is canceling current tasks.</p> </li> <li> <p> <code>STOPPED</code>–Association has been stopped.</p> </li> </ul>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The date and time the resource was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user or system that created this resource."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""


# --- restJson1 ser/de ---
def serialize_json(value: QueueFleetAssociationSummary) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["fleetId"] = value["fleet_id"]
    import capo_deadline.types.queue_fleet_association_status

    out["status"] = capo_deadline.types.queue_fleet_association_status.serialize_json(
        value["status"]
    )
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> QueueFleetAssociationSummary:
    out: QueueFleetAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.queue_fleet_association_status

        out["status"] = (
            capo_deadline.types.queue_fleet_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.queue_fleet_association_status.QueueFleetAssociationStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    return out
