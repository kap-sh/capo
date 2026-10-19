"""Generated from Smithy shape ``com.amazonaws.deadline#VolumeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.persistent_volume_size_gi_b
    import capo_deadline.types.string
    import capo_deadline.types.volume_id
    import capo_deadline.types.volume_state
    import capo_deadline.types.worker_id


class VolumeSummary(TypedDict, closed=True):
    volume_id: "capo_deadline.types.volume_id.VolumeId"
    """<p>The volume ID.</p>"""
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that contains the fleet.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet that contains the volume.</p>"""
    state: "capo_deadline.types.volume_state.VolumeState"
    """<p>The state of the volume.</p>"""
    size_gi_b: "capo_deadline.types.persistent_volume_size_gi_b.PersistentVolumeSizeGiB"
    """<p>The volume size in GiB.</p>"""
    availability_zone_id: "capo_deadline.types.string.String"
    """<p>The Availability Zone ID of the volume.</p>"""
    attached_worker_id: NotRequired["capo_deadline.types.worker_id.WorkerId"]
    """<p>The worker ID of the worker the volume is attached to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeSummary) -> dict:
    out: dict = {}
    out["volumeId"] = value["volume_id"]
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    import capo_deadline.types.volume_state

    out["state"] = capo_deadline.types.volume_state.serialize_json(value["state"])
    out["sizeGiB"] = value["size_gi_b"]
    out["availabilityZoneId"] = value["availability_zone_id"]
    if "attached_worker_id" in value:
        out["attachedWorkerId"] = value["attached_worker_id"]
    return out


def deserialize_json(data: dict) -> VolumeSummary:
    out: VolumeSummary = {}  # type: ignore[typeddict-item]
    if data.get("volumeId") is not None:
        out["volume_id"] = data["volumeId"]
    else:
        out["volume_id"] = ""
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("state") is not None:
        import capo_deadline.types.volume_state

        out["state"] = capo_deadline.types.volume_state.deserialize_json(data["state"])
    else:
        import typing

        out["state"] = typing.cast("capo_deadline.types.volume_state.VolumeState", "")
    if data.get("sizeGiB") is not None:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        out["size_gi_b"] = 0
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    else:
        out["availability_zone_id"] = ""
    if data.get("attachedWorkerId") is not None:
        out["attached_worker_id"] = data["attachedWorkerId"]
    return out
