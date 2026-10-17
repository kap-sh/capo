"""Generated from Smithy shape ``com.amazonaws.deadline#PersistentVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.mount_path
    import capo_deadline.types.persistent_volume_iops
    import capo_deadline.types.persistent_volume_size_gi_b
    import capo_deadline.types.persistent_volume_throughput_mi_b
    import capo_deadline.types.persistent_volume_ttl_hours


class PersistentVolumeConfiguration(TypedDict, closed=True):
    size_gi_b: "capo_deadline.types.persistent_volume_size_gi_b.PersistentVolumeSizeGiB"
    """<p>The persistent volume size in GiB. The default is 250.</p>"""
    iops: "capo_deadline.types.persistent_volume_iops.PersistentVolumeIops"
    """<p>The IOPS per persistent volume. The default is 3000.</p>"""
    throughput_mi_b: "capo_deadline.types.persistent_volume_throughput_mi_b.PersistentVolumeThroughputMiB"
    """<p>The throughput per persistent volume in MiB. The default is 125.</p>"""
    mount_path: "capo_deadline.types.mount_path.MountPath"
    """<p>The file system path where the persistent volume is mounted on the worker instance.</p>"""
    last_used_ttl_hours: (
        "capo_deadline.types.persistent_volume_ttl_hours.PersistentVolumeTtlHours"
    )
    """<p>The number of hours a persistent volume can remain unused before it is deleted. The default is 168 (7 days).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersistentVolumeConfiguration) -> dict:
    out: dict = {}
    out["sizeGiB"] = value.get("size_gi_b", 250)
    out["iops"] = value.get("iops", 3000)
    out["throughputMiB"] = value.get("throughput_mi_b", 125)
    out["mountPath"] = value["mount_path"]
    out["lastUsedTtlHours"] = value.get("last_used_ttl_hours", 168)
    return out


def deserialize_json(data: dict) -> PersistentVolumeConfiguration:
    out: PersistentVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sizeGiB") is not None:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        out["size_gi_b"] = 250
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    else:
        out["iops"] = 3000
    if data.get("throughputMiB") is not None:
        out["throughput_mi_b"] = data["throughputMiB"]
    else:
        out["throughput_mi_b"] = 125
    if data.get("mountPath") is not None:
        out["mount_path"] = data["mountPath"]
    else:
        raise DeserializationError("PersistentVolumeConfiguration.mount_path required")
    if data.get("lastUsedTtlHours") is not None:
        out["last_used_ttl_hours"] = data["lastUsedTtlHours"]
    else:
        out["last_used_ttl_hours"] = 168
    return out
