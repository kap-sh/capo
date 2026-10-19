"""Generated from Smithy shape ``com.amazonaws.odb#AssociateVirtualMachinesToExadbVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class AssociateVirtualMachinesToExadbVmClusterInput(TypedDict, closed=True):
    exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale VM cluster to add virtual machines to.</p>"""
    desired_node_count: "int"
    """<p>The desired number of nodes in the Exascale VM cluster after the association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: AssociateVirtualMachinesToExadbVmClusterInput,
) -> dict:
    out: dict = {}
    out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    out["desiredNodeCount"] = value["desired_node_count"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> AssociateVirtualMachinesToExadbVmClusterInput:
    out: AssociateVirtualMachinesToExadbVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    else:
        out["exadb_vm_cluster_id"] = ""
    if data.get("desiredNodeCount") is not None:
        out["desired_node_count"] = data["desiredNodeCount"]
    else:
        out["desired_node_count"] = 0
    return out
