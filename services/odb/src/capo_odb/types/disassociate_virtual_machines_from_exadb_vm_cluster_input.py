"""Generated from Smithy shape ``com.amazonaws.odb#DisassociateVirtualMachinesFromExadbVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_list
    import capo_odb.types.resource_id_or_arn


class DisassociateVirtualMachinesFromExadbVmClusterInput(TypedDict, closed=True):
    exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale VM cluster to remove virtual machines from.</p>"""
    db_node_ids: "capo_odb.types.resource_id_list.ResourceIdList"
    """<p>The list of DB node IDs to remove from the Exascale VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DisassociateVirtualMachinesFromExadbVmClusterInput,
) -> dict:
    out: dict = {}
    out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    import capo_odb.types.resource_id_list

    out["dbNodeIds"] = capo_odb.types.resource_id_list.serialize_aws_json_1_0(
        value["db_node_ids"]
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DisassociateVirtualMachinesFromExadbVmClusterInput:
    out: DisassociateVirtualMachinesFromExadbVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    else:
        out["exadb_vm_cluster_id"] = ""
    if data.get("dbNodeIds") is not None:
        import capo_odb.types.resource_id_list

        out["db_node_ids"] = capo_odb.types.resource_id_list.deserialize_aws_json_1_0(
            data["dbNodeIds"]
        )
    else:
        out["db_node_ids"] = []
    return out
