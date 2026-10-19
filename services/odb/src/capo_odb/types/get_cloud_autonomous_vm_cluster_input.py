"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudAutonomousVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class GetCloudAutonomousVmClusterInput(TypedDict, closed=True):
    cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudAutonomousVmClusterInput) -> dict:
    out: dict = {}
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudAutonomousVmClusterInput:
    out: GetCloudAutonomousVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudAutonomousVmClusterId") is not None:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        out["cloud_autonomous_vm_cluster_id"] = ""
    return out
