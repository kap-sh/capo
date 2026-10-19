"""Generated from Smithy shape ``com.amazonaws.deadline#GetVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.ebs_volume_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.persistent_volume_iops
    import capo_deadline.types.persistent_volume_size_gi_b
    import capo_deadline.types.persistent_volume_throughput_mi_b
    import capo_deadline.types.string
    import capo_deadline.types.timestamp
    import capo_deadline.types.volume_id
    import capo_deadline.types.volume_state
    import capo_deadline.types.worker_id


class GetVolumeResponse(TypedDict, closed=True):
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
    volume_type: "capo_deadline.types.ebs_volume_type.EbsVolumeType"
    """<p>The EBS volume type.</p>"""
    iops: NotRequired["capo_deadline.types.persistent_volume_iops.PersistentVolumeIops"]
    """<p>The IOPS of the volume.</p>"""
    throughput_mi_b: NotRequired[
        "capo_deadline.types.persistent_volume_throughput_mi_b.PersistentVolumeThroughputMiB"
    ]
    """<p>The throughput of the volume in MiB.</p>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    last_assigned_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the volume was last assigned to a worker.</p>"""
    last_released_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the volume was last released from a worker.</p>"""
    expires_at: NotRequired["capo_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the volume expires and will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVolumeResponse) -> dict:
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
    import capo_deadline.types.ebs_volume_type

    out["volumeType"] = capo_deadline.types.ebs_volume_type.serialize_json(
        value["volume_type"]
    )
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput_mi_b" in value:
        out["throughputMiB"] = value["throughput_mi_b"]
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    if "last_assigned_at" in value:
        import capo_deadline.types.timestamp

        out["lastAssignedAt"] = capo_deadline.types.timestamp.serialize_json(
            value["last_assigned_at"]
        )
    if "last_released_at" in value:
        import capo_deadline.types.timestamp

        out["lastReleasedAt"] = capo_deadline.types.timestamp.serialize_json(
            value["last_released_at"]
        )
    if "expires_at" in value:
        import capo_deadline.types.timestamp

        out["expiresAt"] = capo_deadline.types.timestamp.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> GetVolumeResponse:
    out: GetVolumeResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("volumeType") is not None:
        import capo_deadline.types.ebs_volume_type

        out["volume_type"] = capo_deadline.types.ebs_volume_type.deserialize_json(
            data["volumeType"]
        )
    else:
        import typing

        out["volume_type"] = typing.cast(
            "capo_deadline.types.ebs_volume_type.EbsVolumeType", ""
        )
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughputMiB") is not None:
        out["throughput_mi_b"] = data["throughputMiB"]
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastAssignedAt") is not None:
        import capo_deadline.types.timestamp

        out["last_assigned_at"] = capo_deadline.types.timestamp.deserialize_json(
            data["lastAssignedAt"]
        )
    if data.get("lastReleasedAt") is not None:
        import capo_deadline.types.timestamp

        out["last_released_at"] = capo_deadline.types.timestamp.deserialize_json(
            data["lastReleasedAt"]
        )
    if data.get("expiresAt") is not None:
        import capo_deadline.types.timestamp

        out["expires_at"] = capo_deadline.types.timestamp.deserialize_json(
            data["expiresAt"]
        )
    return out
