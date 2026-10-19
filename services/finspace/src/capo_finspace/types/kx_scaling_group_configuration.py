"""Generated from Smithy shape ``com.amazonaws.finspace#KxScalingGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.cluster_node_count
    import capo_finspace.types.cpu_count
    import capo_finspace.types.kx_scaling_group_name
    import capo_finspace.types.memory_mib


class KxScalingGroupConfiguration(TypedDict, closed=True):
    scaling_group_name: "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    """<p>A unique identifier for the kdb scaling group. </p>"""
    memory_limit: NotRequired["capo_finspace.types.memory_mib.MemoryMib"]
    """<p> An optional hard limit on the amount of memory a kdb cluster can use. </p>"""
    memory_reservation: "capo_finspace.types.memory_mib.MemoryMib"
    """<p> A reservation of the minimum amount of memory that should be available on the scaling group for a kdb cluster to be successfully placed in a scaling group. </p>"""
    node_count: "capo_finspace.types.cluster_node_count.ClusterNodeCount"
    """<p> The number of kdb cluster nodes. </p>"""
    cpu: NotRequired["capo_finspace.types.cpu_count.CpuCount"]
    """<p> The number of vCPUs that you want to reserve for each node of this kdb cluster on the scaling group host. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxScalingGroupConfiguration) -> dict:
    out: dict = {}
    out["scalingGroupName"] = value["scaling_group_name"]
    if "memory_limit" in value:
        out["memoryLimit"] = value["memory_limit"]
    out["memoryReservation"] = value["memory_reservation"]
    out["nodeCount"] = value["node_count"]
    if "cpu" in value:
        out["cpu"] = (
            "NaN"
            if value["cpu"] != value["cpu"]
            else "Infinity"
            if value["cpu"] == float("inf")
            else "-Infinity"
            if value["cpu"] == float("-inf")
            else value["cpu"]
        )
    return out


def deserialize_json(data: dict) -> KxScalingGroupConfiguration:
    out: KxScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scalingGroupName") is not None:
        out["scaling_group_name"] = data["scalingGroupName"]
    else:
        out["scaling_group_name"] = ""
    if data.get("memoryLimit") is not None:
        out["memory_limit"] = data["memoryLimit"]
    if data.get("memoryReservation") is not None:
        out["memory_reservation"] = data["memoryReservation"]
    else:
        out["memory_reservation"] = 0
    if data.get("nodeCount") is not None:
        out["node_count"] = data["nodeCount"]
    else:
        out["node_count"] = 0
    if data.get("cpu") is not None:
        out["cpu"] = float(data["cpu"])
    return out
