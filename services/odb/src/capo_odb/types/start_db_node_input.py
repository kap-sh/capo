"""Generated from Smithy shape ``com.amazonaws.odb#StartDbNodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id


class StartDbNodeInput(TypedDict, closed=True):
    cloud_vm_cluster_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the VM cluster that contains the DB node to start. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>"""
    exadb_vm_cluster_id: NotRequired["capo_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the Exascale VM cluster that contains the DB node to start. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>"""
    db_node_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the DB node to start.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartDbNodeInput) -> dict:
    out: dict = {}
    if "cloud_vm_cluster_id" in value:
        out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    if "exadb_vm_cluster_id" in value:
        out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    out["dbNodeId"] = value["db_node_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartDbNodeInput:
    out: StartDbNodeInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    if data.get("dbNodeId") is not None:
        out["db_node_id"] = data["dbNodeId"]
    else:
        out["db_node_id"] = ""
    return out
