"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class GetCloudVmClusterInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudVmClusterInput) -> dict:
    out: dict = {}
    out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudVmClusterInput:
    out: GetCloudVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    else:
        out["cloud_vm_cluster_id"] = ""
    return out
