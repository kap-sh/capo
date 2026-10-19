"""Generated from Smithy shape ``com.amazonaws.emrserverless#MaximumAllowedResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.cpu_size
    import capo_emr_serverless.types.disk_size
    import capo_emr_serverless.types.memory_size


class MaximumAllowedResources(TypedDict, closed=True):
    cpu: "capo_emr_serverless.types.cpu_size.CpuSize"
    """<p>The maximum allowed CPU for an application.</p>"""
    memory: "capo_emr_serverless.types.memory_size.MemorySize"
    """<p>The maximum allowed resources for an application.</p>"""
    disk: NotRequired["capo_emr_serverless.types.disk_size.DiskSize"]
    """<p>The maximum allowed disk for an application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaximumAllowedResources) -> dict:
    out: dict = {}
    out["cpu"] = value["cpu"]
    out["memory"] = value["memory"]
    if "disk" in value:
        out["disk"] = value["disk"]
    return out


def deserialize_json(data: dict) -> MaximumAllowedResources:
    out: MaximumAllowedResources = {}  # type: ignore[typeddict-item]
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
    return out
