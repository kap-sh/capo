"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterFsxOpenZfsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_dns_name
    import capo_sagemaker.types.cluster_fsx_mount_path


class ClusterFsxOpenZfsConfig(TypedDict, closed=True):
    dns_name: "capo_sagemaker.types.cluster_dns_name.ClusterDnsName"
    """<p>The DNS name of the Amazon FSx for OpenZFS file system.</p>"""
    mount_path: NotRequired[
        "capo_sagemaker.types.cluster_fsx_mount_path.ClusterFsxMountPath"
    ]
    """<p>The local path where the Amazon FSx for OpenZFS file system is mounted on instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterFsxOpenZfsConfig) -> dict:
    out: dict = {}
    out["DnsName"] = value["dns_name"]
    if "mount_path" in value:
        out["MountPath"] = value["mount_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterFsxOpenZfsConfig:
    out: ClusterFsxOpenZfsConfig = {}  # type: ignore[typeddict-item]
    if data.get("DnsName") is not None:
        out["dns_name"] = data["DnsName"]
    else:
        out["dns_name"] = ""
    if data.get("MountPath") is not None:
        out["mount_path"] = data["MountPath"]
    return out
