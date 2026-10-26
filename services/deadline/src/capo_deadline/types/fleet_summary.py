"""Generated from Smithy shape ``com.amazonaws.deadline#FleetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.auto_scaling_status
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_configuration
    import capo_deadline.types.fleet_id
    import capo_deadline.types.fleet_status
    import capo_deadline.types.integer
    import capo_deadline.types.min_zero_max_integer
    import capo_deadline.types.resource_name
    import capo_deadline.types.string
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class FleetSummary(TypedDict, closed=True):
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the fleet summary to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: "capo_deadline.types.fleet_status.FleetStatus"
    """<p>The status of the fleet.</p>"""
    status_message: NotRequired["capo_deadline.types.string.String"]
    """<p>A message that communicates a suspended status of the fleet.</p>"""
    auto_scaling_status: NotRequired[
        "capo_deadline.types.auto_scaling_status.AutoScalingStatus"
    ]
    """<p>The Auto Scaling status of a fleet.</p>"""
    target_worker_count: NotRequired["capo_deadline.types.integer.Integer"]
    """<p>The target number of workers in a fleet.</p>"""
    worker_count: "capo_deadline.types.integer.Integer"
    """<p>The number of workers in the fleet summary.</p>"""
    min_worker_count: "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The minimum number of workers in the fleet.</p>"""
    max_worker_count: "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The maximum number of workers specified in the fleet.</p>"""
    configuration: "capo_deadline.types.fleet_configuration.FleetConfiguration"
    """<p>The configuration details for the fleet.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FleetSummary) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    out["farmId"] = value["farm_id"]
    out["displayName"] = value["display_name"]
    import capo_deadline.types.fleet_status

    out["status"] = capo_deadline.types.fleet_status.serialize_json(value["status"])
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "auto_scaling_status" in value:
        import capo_deadline.types.auto_scaling_status

        out["autoScalingStatus"] = (
            capo_deadline.types.auto_scaling_status.serialize_json(
                value["auto_scaling_status"]
            )
        )
    if "target_worker_count" in value:
        out["targetWorkerCount"] = value["target_worker_count"]
    out["workerCount"] = value["worker_count"]
    out["minWorkerCount"] = value["min_worker_count"]
    out["maxWorkerCount"] = value["max_worker_count"]
    import capo_deadline.types.fleet_configuration

    out["configuration"] = capo_deadline.types.fleet_configuration.serialize_json(
        value["configuration"]
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


def deserialize_json(data: dict) -> FleetSummary:
    out: FleetSummary = {}  # type: ignore[typeddict-item]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.fleet_status

        out["status"] = capo_deadline.types.fleet_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_deadline.types.fleet_status.FleetStatus", "")
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("autoScalingStatus") is not None:
        import capo_deadline.types.auto_scaling_status

        out["auto_scaling_status"] = (
            capo_deadline.types.auto_scaling_status.deserialize_json(
                data["autoScalingStatus"]
            )
        )
    if data.get("targetWorkerCount") is not None:
        out["target_worker_count"] = data["targetWorkerCount"]
    if data.get("workerCount") is not None:
        out["worker_count"] = data["workerCount"]
    else:
        out["worker_count"] = 0
    if data.get("minWorkerCount") is not None:
        out["min_worker_count"] = data["minWorkerCount"]
    else:
        out["min_worker_count"] = 0
    if data.get("maxWorkerCount") is not None:
        out["max_worker_count"] = data["maxWorkerCount"]
    else:
        out["max_worker_count"] = 0
    if data.get("configuration") is not None:
        import capo_deadline.types.fleet_configuration

        out["configuration"] = capo_deadline.types.fleet_configuration.deserialize_json(
            data["configuration"]
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
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
