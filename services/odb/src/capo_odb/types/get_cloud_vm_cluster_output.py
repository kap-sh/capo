"""Generated from Smithy shape ``com.amazonaws.odb#GetCloudVmClusterOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cloud_vm_cluster


class GetCloudVmClusterOutput(TypedDict, closed=True):
    cloud_vm_cluster: NotRequired["capo_odb.types.cloud_vm_cluster.CloudVmCluster"]
    """<p>The VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCloudVmClusterOutput) -> dict:
    out: dict = {}
    if "cloud_vm_cluster" in value:
        import capo_odb.types.cloud_vm_cluster

        out["cloudVmCluster"] = capo_odb.types.cloud_vm_cluster.serialize_aws_json_1_0(
            value["cloud_vm_cluster"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCloudVmClusterOutput:
    out: GetCloudVmClusterOutput = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmCluster") is not None:
        import capo_odb.types.cloud_vm_cluster

        out["cloud_vm_cluster"] = (
            capo_odb.types.cloud_vm_cluster.deserialize_aws_json_1_0(
                data["cloudVmCluster"]
            )
        )
    return out


def redact_sensitive(value: GetCloudVmClusterOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cloud_vm_cluster" in value:
        import capo_odb.types.cloud_vm_cluster

        out["cloud_vm_cluster"] = capo_odb.types.cloud_vm_cluster.redact_sensitive(
            value["cloud_vm_cluster"]
        )
    return out
