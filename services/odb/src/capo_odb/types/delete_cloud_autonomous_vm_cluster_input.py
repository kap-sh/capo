"""Generated from Smithy shape ``com.amazonaws.odb#DeleteCloudAutonomousVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class DeleteCloudAutonomousVmClusterInput(TypedDict, closed=True):
    cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous VM cluster to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCloudAutonomousVmClusterInput) -> dict:
    out: dict = {}
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCloudAutonomousVmClusterInput:
    out: DeleteCloudAutonomousVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudAutonomousVmClusterId") is not None:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        out["cloud_autonomous_vm_cluster_id"] = ""
    return out
