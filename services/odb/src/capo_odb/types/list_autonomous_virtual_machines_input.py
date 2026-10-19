"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousVirtualMachinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class ListAutonomousVirtualMachinesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return per page.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token to continue listing from.</p>"""
    cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster whose virtual machines you're listing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousVirtualMachinesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousVirtualMachinesInput:
    out: ListAutonomousVirtualMachinesInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudAutonomousVmClusterId") is not None:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        out["cloud_autonomous_vm_cluster_id"] = ""
    return out
