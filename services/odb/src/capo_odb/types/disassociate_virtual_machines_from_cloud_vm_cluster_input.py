"""Generated from Smithy shape ``com.amazonaws.odb#DisassociateVirtualMachinesFromCloudVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id
    import capo_odb.types.string_list


class DisassociateVirtualMachinesFromCloudVmClusterInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster to remove virtual machines from.</p>"""
    db_servers: "capo_odb.types.string_list.StringList"
    """<p>The list of database server IDs for the virtual machines to remove from the VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DisassociateVirtualMachinesFromCloudVmClusterInput,
) -> dict:
    out: dict = {}
    out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    import capo_odb.types.string_list

    out["dbServers"] = capo_odb.types.string_list.serialize_aws_json_1_0(
        value["db_servers"]
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DisassociateVirtualMachinesFromCloudVmClusterInput:
    out: DisassociateVirtualMachinesFromCloudVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    else:
        out["cloud_vm_cluster_id"] = ""
    if data.get("dbServers") is not None:
        import capo_odb.types.string_list

        out["db_servers"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    else:
        out["db_servers"] = []
    return out
