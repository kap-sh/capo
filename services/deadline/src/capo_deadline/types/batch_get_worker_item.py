"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.host_properties_response
    import capo_deadline.types.log_configuration
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.worker_id
    import capo_deadline.types.worker_status


class BatchGetWorkerItem(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the worker.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the worker.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID.</p>"""
    host_properties: NotRequired[
        "capo_deadline.types.host_properties_response.HostPropertiesResponse"
    ]
    """<p>The host properties for the worker.</p>"""
    status: "capo_deadline.types.worker_status.WorkerStatus"
    """<p>The status of the worker.</p>"""
    log: NotRequired["capo_deadline.types.log_configuration.LogConfiguration"]
    """<p>The log configuration for the worker.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerItem) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    if "host_properties" in value:
        import capo_deadline.types.host_properties_response

        out["hostProperties"] = (
            capo_deadline.types.host_properties_response.serialize_json(
                value["host_properties"]
            )
        )
    import capo_deadline.types.worker_status

    out["status"] = capo_deadline.types.worker_status.serialize_json(value["status"])
    if "log" in value:
        import capo_deadline.types.log_configuration

        out["log"] = capo_deadline.types.log_configuration.serialize_json(value["log"])
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


def deserialize_json(data: dict) -> BatchGetWorkerItem:
    out: BatchGetWorkerItem = {}  # type: ignore[typeddict-item]
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
    if data.get("hostProperties") is not None:
        import capo_deadline.types.host_properties_response

        out["host_properties"] = (
            capo_deadline.types.host_properties_response.deserialize_json(
                data["hostProperties"]
            )
        )
    if data.get("status") is not None:
        import capo_deadline.types.worker_status

        out["status"] = capo_deadline.types.worker_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.worker_status.WorkerStatus", ""
        )
    if data.get("log") is not None:
        import capo_deadline.types.log_configuration

        out["log"] = capo_deadline.types.log_configuration.deserialize_json(data["log"])
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
