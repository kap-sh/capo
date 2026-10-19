"""Generated from Smithy shape ``com.amazonaws.odb#CreateCloudAutonomousVmClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_status


class CreateCloudAutonomousVmClusterOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The display name of the created Autonomous VM cluster.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Autonomous VM cluster creation process.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous VM cluster creation process, if applicable.</p>"""
    cloud_autonomous_vm_cluster_id: "str"
    """<p>The unique identifier of the created Autonomous VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCloudAutonomousVmClusterOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["cloudAutonomousVmClusterId"] = value["cloud_autonomous_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCloudAutonomousVmClusterOutput:
    out: CreateCloudAutonomousVmClusterOutput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("cloudAutonomousVmClusterId") is not None:
        out["cloud_autonomous_vm_cluster_id"] = data["cloudAutonomousVmClusterId"]
    else:
        out["cloud_autonomous_vm_cluster_id"] = ""
    return out
