"""Generated from Smithy shape ``com.amazonaws.odb#GetExadbVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class GetExadbVmClusterInput(TypedDict, closed=True):
    exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetExadbVmClusterInput) -> dict:
    out: dict = {}
    out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetExadbVmClusterInput:
    out: GetExadbVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    else:
        out["exadb_vm_cluster_id"] = ""
    return out
