"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreateVolumeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_instances.types.client_token
    import capo_workspaces_instances.types.kms_key_id
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.snapshot_id
    import capo_workspaces_instances.types.string64
    import capo_workspaces_instances.types.tag_specifications
    import capo_workspaces_instances.types.volume_type_enum


class CreateVolumeRequest(TypedDict, closed=True):
    availability_zone: "capo_workspaces_instances.types.string64.String64"
    """<p>Availability zone for the volume.</p>"""
    client_token: NotRequired[
        "capo_workspaces_instances.types.client_token.ClientToken"
    ]
    """<p>Unique token to prevent duplicate volume creation.</p>"""
    encrypted: NotRequired["bool"]
    """<p>Indicates if the volume should be encrypted.</p>"""
    iops: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Input/output operations per second for the volume.</p>"""
    kms_key_id: NotRequired["capo_workspaces_instances.types.kms_key_id.KmsKeyId"]
    """<p>KMS key for volume encryption.</p>"""
    size_in_gb: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Volume size in gigabytes.</p>"""
    snapshot_id: NotRequired["capo_workspaces_instances.types.snapshot_id.SnapshotId"]
    """<p>Source snapshot for volume creation.</p>"""
    tag_specifications: NotRequired[
        "capo_workspaces_instances.types.tag_specifications.TagSpecifications"
    ]
    """<p>Metadata tags for the volume.</p>"""
    throughput: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Volume throughput performance.</p>"""
    volume_type: NotRequired[
        "capo_workspaces_instances.types.volume_type_enum.VolumeTypeEnum"
    ]
    """<p>Type of EBS volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVolumeRequest) -> dict:
    out: dict = {}
    out["AvailabilityZone"] = value["availability_zone"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "size_in_gb" in value:
        out["SizeInGB"] = value["size_in_gb"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "tag_specifications" in value:
        import capo_workspaces_instances.types.tag_specifications

        out["TagSpecifications"] = (
            capo_workspaces_instances.types.tag_specifications.serialize_aws_json_1_0(
                value["tag_specifications"]
            )
        )
    if "throughput" in value:
        out["Throughput"] = value["throughput"]
    if "volume_type" in value:
        import capo_workspaces_instances.types.volume_type_enum

        out["VolumeType"] = (
            capo_workspaces_instances.types.volume_type_enum.serialize_aws_json_1_0(
                value["volume_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVolumeRequest:
    out: CreateVolumeRequest = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    else:
        raise DeserializationError("CreateVolumeRequest.availability_zone required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Encrypted") is not None:
        out["encrypted"] = data["Encrypted"]
    if data.get("Iops") is not None:
        out["iops"] = data["Iops"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("SizeInGB") is not None:
        out["size_in_gb"] = data["SizeInGB"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("TagSpecifications") is not None:
        import capo_workspaces_instances.types.tag_specifications

        out["tag_specifications"] = (
            capo_workspaces_instances.types.tag_specifications.deserialize_aws_json_1_0(
                data["TagSpecifications"]
            )
        )
    if data.get("Throughput") is not None:
        out["throughput"] = data["Throughput"]
    if data.get("VolumeType") is not None:
        import capo_workspaces_instances.types.volume_type_enum

        out["volume_type"] = (
            capo_workspaces_instances.types.volume_type_enum.deserialize_aws_json_1_0(
                data["VolumeType"]
            )
        )
    return out


def redact_sensitive(value: CreateVolumeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    if "kms_key_id" in value:
        out["kms_key_id"] = "*** Sensitive Data Redacted ***"
    return out
