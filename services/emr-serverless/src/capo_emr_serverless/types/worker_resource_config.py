"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.cpu_size
    import capo_emr_serverless.types.disk_size
    import capo_emr_serverless.types.disk_type
    import capo_emr_serverless.types.memory_size


class WorkerResourceConfig(TypedDict, closed=True):
    cpu: "capo_emr_serverless.types.cpu_size.CpuSize"
    """<p>The CPU requirements for every worker instance of the worker type.</p>"""
    memory: "capo_emr_serverless.types.memory_size.MemorySize"
    """<p>The memory requirements for every worker instance of the worker type.</p>"""
    disk: NotRequired["capo_emr_serverless.types.disk_size.DiskSize"]
    """<p>The disk requirements for every worker instance of the worker type.</p>"""
    disk_type: NotRequired["capo_emr_serverless.types.disk_type.DiskType"]
    """<p>The disk type for every worker instance of the work type. Shuffle optimized disks have higher performance characteristics and are better for shuffle heavy workloads. Default is <code>STANDARD</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerResourceConfig) -> dict:
    out: dict = {}
    out["cpu"] = value["cpu"]
    out["memory"] = value["memory"]
    if "disk" in value:
        out["disk"] = value["disk"]
    if "disk_type" in value:
        out["diskType"] = value["disk_type"]
    return out


def deserialize_json(data: dict) -> WorkerResourceConfig:
    out: WorkerResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    else:
        out["cpu"] = ""
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    else:
        out["memory"] = ""
    if data.get("disk") is not None:
        out["disk"] = data["disk"]
    if data.get("diskType") is not None:
        out["disk_type"] = data["diskType"]
    return out
