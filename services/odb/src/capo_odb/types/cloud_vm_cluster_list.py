"""Generated from Smithy shape ``com.amazonaws.odb#CloudVmClusterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.cloud_vm_cluster_summary

CloudVmClusterList: TypeAlias = list[
    "capo_odb.types.cloud_vm_cluster_summary.CloudVmClusterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudVmClusterList) -> list:
    import capo_odb.types.cloud_vm_cluster_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.cloud_vm_cluster_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CloudVmClusterList:
    import capo_odb.types.cloud_vm_cluster_summary

    out: CloudVmClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_odb.types.cloud_vm_cluster_summary.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: CloudVmClusterList) -> list[Any]:
    import capo_odb.types.cloud_vm_cluster_summary

    return [
        capo_odb.types.cloud_vm_cluster_summary.redact_sensitive(item) for item in value
    ]
