"""Generated from Smithy shape ``com.amazonaws.odb#ListExadbVmClustersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.exadb_vm_cluster_list


class ListExadbVmClustersOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    exadb_vm_clusters: "capo_odb.types.exadb_vm_cluster_list.ExadbVmClusterList"
    """<p>The list of Exascale VM clusters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExadbVmClustersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.exadb_vm_cluster_list

    out["exadbVmClusters"] = (
        capo_odb.types.exadb_vm_cluster_list.serialize_aws_json_1_0(
            value["exadb_vm_clusters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExadbVmClustersOutput:
    out: ListExadbVmClustersOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("exadbVmClusters") is not None:
        import capo_odb.types.exadb_vm_cluster_list

        out["exadb_vm_clusters"] = (
            capo_odb.types.exadb_vm_cluster_list.deserialize_aws_json_1_0(
                data["exadbVmClusters"]
            )
        )
    else:
        out["exadb_vm_clusters"] = []
    return out
