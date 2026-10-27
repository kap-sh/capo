"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_properties_response
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.worker_id
    import capo_deadline.types.worker_status


class WorkerSearchSummary(TypedDict, closed=True):
    fleet_id: NotRequired["capo_deadline.types.fleet_id.FleetId"]
    """The fleet ID."""
    worker_id: NotRequired["capo_deadline.types.worker_id.WorkerId"]
    """The worker ID."""
    status: NotRequired["capo_deadline.types.worker_status.WorkerStatus"]
    """The status of the worker search."""
    host_properties: NotRequired[
        "capo_deadline.types.host_properties_response.HostPropertiesResponse"
    ]
    """Provides the Amazon EC2 instance properties of the worker host."""
    created_by: NotRequired["capo_deadline.types.created_by.CreatedBy"]
    """The user or system that created this resource."""
    created_at: NotRequired["capo_deadline.types.created_at.CreatedAt"]
    """The date and time the resource was created."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSearchSummary) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["fleetId"] = value["fleet_id"]
    if "worker_id" in value:
        out["workerId"] = value["worker_id"]
    if "status" in value:
        import capo_deadline.types.worker_status

        out["status"] = capo_deadline.types.worker_status.serialize_json(
            value["status"]
        )
    if "host_properties" in value:
        import capo_deadline.types.host_properties_response

        out["hostProperties"] = (
            capo_deadline.types.host_properties_response.serialize_json(
                value["host_properties"]
            )
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_deadline.types.created_at

        out["createdAt"] = capo_deadline.types.created_at.serialize_json(
            value["created_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> WorkerSearchSummary:
    out: WorkerSearchSummary = {}  # type: ignore[typeddict-item]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    if data.get("workerId") is not None:
        out["worker_id"] = data["workerId"]
    if data.get("status") is not None:
        import capo_deadline.types.worker_status

        out["status"] = capo_deadline.types.worker_status.deserialize_json(
            data["status"]
        )
    if data.get("hostProperties") is not None:
        import capo_deadline.types.host_properties_response

        out["host_properties"] = (
            capo_deadline.types.host_properties_response.deserialize_json(
                data["hostProperties"]
            )
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    return out
