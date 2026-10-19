"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterFsxLustreConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_dns_name
    import capo_sagemaker.types.cluster_fsx_mount_path
    import capo_sagemaker.types.cluster_mount_name


class ClusterFsxLustreConfig(TypedDict, closed=True):
    dns_name: "capo_sagemaker.types.cluster_dns_name.ClusterDnsName"
    """<p>The DNS name of the Amazon FSx for Lustre file system.</p>"""
    mount_name: "capo_sagemaker.types.cluster_mount_name.ClusterMountName"
    """<p>The mount name of the Amazon FSx for Lustre file system.</p>"""
    mount_path: NotRequired[
        "capo_sagemaker.types.cluster_fsx_mount_path.ClusterFsxMountPath"
    ]
    """<p>The local path where the Amazon FSx for Lustre file system is mounted on instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterFsxLustreConfig) -> dict:
    out: dict = {}
    out["DnsName"] = value["dns_name"]
    out["MountName"] = value["mount_name"]
    if "mount_path" in value:
        out["MountPath"] = value["mount_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterFsxLustreConfig:
    out: ClusterFsxLustreConfig = {}  # type: ignore[typeddict-item]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    else:
        out["dns_name"] = ""
    if data.get("MountName") is not None:
        out["mount_name"] = data["MountName"]
    else:
        out["mount_name"] = ""
    if data.get("MountPath") is not None:
        out["mount_path"] = data["MountPath"]
    return out
