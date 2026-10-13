"""Generated from Smithy shape ``com.amazonaws.odb#ListCloudVmClustersOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_odb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_odb.types.cloud_vm_cluster_list


class ListCloudVmClustersOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    cloud_vm_clusters: "capo_odb.types.cloud_vm_cluster_list.CloudVmClusterList"
    """<p>The list of VM clusters along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCloudVmClustersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.cloud_vm_cluster_list

    out["cloudVmClusters"] = (
        capo_odb.types.cloud_vm_cluster_list.serialize_aws_json_1_0(
            value["cloud_vm_clusters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCloudVmClustersOutput:
    out: ListCloudVmClustersOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("cloudVmClusters") is not None:
        import capo_odb.types.cloud_vm_cluster_list

        out["cloud_vm_clusters"] = (
            capo_odb.types.cloud_vm_cluster_list.deserialize_aws_json_1_0(
                data["cloudVmClusters"]
            )
        )
    else:
        raise DeserializationError(
            "ListCloudVmClustersOutput.cloud_vm_clusters required"
        )
    return out


def redact_sensitive(value: ListCloudVmClustersOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cloud_vm_clusters" in value:
        import capo_odb.types.cloud_vm_cluster_list

        out["cloud_vm_clusters"] = (
            capo_odb.types.cloud_vm_cluster_list.redact_sensitive(
                value["cloud_vm_clusters"]
            )
        )
    return out
