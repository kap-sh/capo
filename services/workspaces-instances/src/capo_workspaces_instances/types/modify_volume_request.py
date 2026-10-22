"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ModifyVolumeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.client_token
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.volume_id
    import capo_workspaces_instances.types.volume_size_in_gb
    import capo_workspaces_instances.types.volume_type_enum


class ModifyVolumeRequest(TypedDict, closed=True):
    volume_id: "capo_workspaces_instances.types.volume_id.VolumeId"
    """<p>Specifies the identifier of the volume to modify.</p>"""
    size_in_gb: NotRequired[
        "capo_workspaces_instances.types.volume_size_in_gb.VolumeSizeInGB"
    ]
    """<p>Specifies the target size of the volume, in GiB. The target size must be greater than or equal to the current size of the volume. If you don't specify a size, the current size is retained.</p>"""
    volume_type: NotRequired[
        "capo_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"
    ]
    """<p>Specifies the target Amazon Elastic Block Store (Amazon EBS) volume type. If you don't specify a volume type, the current volume type is retained.</p>"""
    iops: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies the target IOPS rate of the volume. This parameter is valid only for <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes. If you don't specify IOPS and keep the same volume type, the current IOPS rate is retained.</p>"""
    throughput: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies the target throughput of the volume, in MiB/s. This parameter is valid only for <code>gp3</code> volumes. If you don't specify throughput and the volume remains <code>gp3</code>, the current throughput is retained.</p>"""
    client_token: NotRequired[
        "capo_workspaces_instances.types.client_token.ClientToken"
    ]
    """<p>Unique token to ensure idempotent volume modification, preventing duplicate volume modifications.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModifyVolumeRequest) -> dict:
    out: dict = {}
    out["VolumeId"] = value["volume_id"]
    if "size_in_gb" in value:
        out["SizeInGB"] = value["size_in_gb"]
    if "volume_type" in value:
        import capo_workspaces_instances.types.volume_type_enum

        out["VolumeType"] = (
            capo_workspaces_instances.types.volume_type_enum.serialize_aws_json_1_0(
                value["volume_type"]
            )
        )
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ModifyVolumeRequest:
    out: ModifyVolumeRequest = {}  # type: ignore[typeddict-item]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    else:
        out["volume_id"] = ""
    if data.get("SizeInGB") is not None:
        out["size_in_gb"] = data["SizeInGB"]
    if data.get("VolumeType") is not None:
        import capo_workspaces_instances.types.volume_type_enum

        out["volume_type"] = (
            capo_workspaces_instances.types.volume_type_enum.deserialize_aws_json_1_0(
                data["VolumeType"]
            )
        )
    if data.get("Iops") is not None:
        out["iops"] = data["Iops"]
    if data.get("Throughput") is not None:
        out["throughput"] = data["Throughput"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: ModifyVolumeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
