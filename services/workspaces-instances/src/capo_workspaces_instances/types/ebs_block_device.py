"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EbsBlockDevice``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.kms_key_id
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.volume_type_enum


class EbsBlockDevice(TypedDict, closed=True):
    volume_type: NotRequired[
        "capo_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"
    ]
    """<p>Type of EBS volume (e.g., gp2, io1).</p>"""
    encrypted: NotRequired["bool"]
    """<p>Indicates if the volume is encrypted.</p>"""
    kms_key_id: NotRequired["capo_workspaces_instances.types.kms_key_id.KmsKeyId"]
    """<p>KMS key used for volume encryption.</p>"""
    iops: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Input/output operations per second for the volume.</p>"""
    throughput: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Volume data transfer rate.</p>"""
    volume_size: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Size of the EBS volume in gigabytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EbsBlockDevice) -> dict:
    out: dict = {}
    if "volume_type" in value:
        import capo_workspaces_instances.types.volume_type_enum

        out["VolumeType"] = (
            capo_workspaces_instances.types.volume_type_enum.serialize_aws_json_1_0(
                value["volume_type"]
            )
        )
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EbsBlockDevice:
    out: EbsBlockDevice = {}  # type: ignore[typeddict-item]
    if data.get("VolumeType") is not None:
        import capo_workspaces_instances.types.volume_type_enum

        out["volume_type"] = (
            capo_workspaces_instances.types.volume_type_enum.deserialize_aws_json_1_0(
                data["VolumeType"]
            )
        )
    if data.get("Encrypted") is not None:
        out["encrypted"] = data["Encrypted"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("Iops") is not None:
        out["iops"] = data["Iops"]
    if data.get("Throughput") is not None:
        out["throughput"] = data["Throughput"]
    if data.get("VolumeSize") is not None:
        out["volume_size"] = data["VolumeSize"]
    return out


def redact_sensitive(value: EbsBlockDevice) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kms_key_id" in value:
        out["kms_key_id"] = "*** Sensitive Data Redacted ***"
    return out
