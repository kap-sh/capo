"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ModifyVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.volume_id
    import capo_workspaces_instances.types.volume_type_enum


class ModifyVolumeResponse(TypedDict, closed=True):
    volume_id: NotRequired["capo_workspaces_instances.types.volume_id.VolumeId"]
    """<p>Specifies the identifier of the modified volume.</p>"""
    target_size: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies the target size of the volume, in GiB.</p>"""
    target_volume_type: NotRequired[
        "capo_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"
    ]
    """<p>Specifies the target Amazon EBS volume type.</p>"""
    target_iops: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies the target IOPS rate of the volume.</p>"""
    target_throughput: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies the target throughput of the volume, in MiB/s.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ModifyVolumeResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "target_size" in value:
        out["TargetSize"] = value["target_size"]
    if "target_volume_type" in value:
        import capo_workspaces_instances.types.volume_type_enum

        out["TargetVolumeType"] = (
            capo_workspaces_instances.types.volume_type_enum.serialize_aws_json_1_0(
                value["target_volume_type"]
            )
        )
    if "target_iops" in value:
        out["TargetIops"] = value["target_iops"]
    if "target_throughput" in value:
        out["TargetThroughput"] = value["target_throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ModifyVolumeResponse:
    out: ModifyVolumeResponse = {}  # type: ignore[typeddict-item]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    if data.get("TargetSize") is not None:
        out["target_size"] = data["TargetSize"]
    if data.get("TargetVolumeType") is not None:
        import capo_workspaces_instances.types.volume_type_enum

        out["target_volume_type"] = (
            capo_workspaces_instances.types.volume_type_enum.deserialize_aws_json_1_0(
                data["TargetVolumeType"]
            )
        )
    if data.get("TargetIops") is not None:
        out["target_iops"] = data["TargetIops"]
    if data.get("TargetThroughput") is not None:
        out["target_throughput"] = data["TargetThroughput"]
    return out
