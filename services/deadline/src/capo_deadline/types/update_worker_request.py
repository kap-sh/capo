"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_properties_request
    import capo_deadline.types.updated_worker_status
    import capo_deadline.types.worker_capabilities
    import capo_deadline.types.worker_id


class UpdateWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID to update."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID to update."""
    status: NotRequired["capo_deadline.types.updated_worker_status.UpdatedWorkerStatus"]
    """The worker status to update."""
    capabilities: NotRequired[
        "capo_deadline.types.worker_capabilities.WorkerCapabilities"
    ]
    """The worker capabilities to update."""
    host_properties: NotRequired[
        "capo_deadline.types.host_properties_request.HostPropertiesRequest"
    ]
    """The host properties to update."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_deadline.types.updated_worker_status

        out["status"] = capo_deadline.types.updated_worker_status.serialize_json(
            value["status"]
        )
    if "capabilities" in value:
        import capo_deadline.types.worker_capabilities

        out["capabilities"] = capo_deadline.types.worker_capabilities.serialize_json(
            value["capabilities"]
        )
    if "host_properties" in value:
        import capo_deadline.types.host_properties_request

        out["hostProperties"] = (
            capo_deadline.types.host_properties_request.serialize_json(
                value["host_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkerRequest:
    out: UpdateWorkerRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_deadline.types.updated_worker_status

        out["status"] = capo_deadline.types.updated_worker_status.deserialize_json(
            data["status"]
        )
    if data.get("capabilities") is not None:
        import capo_deadline.types.worker_capabilities

        out["capabilities"] = capo_deadline.types.worker_capabilities.deserialize_json(
            data["capabilities"]
        )
    if data.get("hostProperties") is not None:
        import capo_deadline.types.host_properties_request

        out["host_properties"] = (
            capo_deadline.types.host_properties_request.deserialize_json(
                data["hostProperties"]
            )
        )
    return out
