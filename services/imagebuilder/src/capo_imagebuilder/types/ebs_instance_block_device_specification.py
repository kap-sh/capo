"""Generated from Smithy shape ``com.amazonaws.imagebuilder#EbsInstanceBlockDeviceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ebs_iops_integer
    import capo_imagebuilder.types.ebs_volume_size_integer
    import capo_imagebuilder.types.ebs_volume_throughput
    import capo_imagebuilder.types.ebs_volume_type
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean


class EbsInstanceBlockDeviceSpecification(TypedDict, closed=True):
    encrypted: NotRequired["capo_imagebuilder.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to encrypt the device.</p>"""
    delete_on_termination: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to delete the associated device on termination.</p>"""
    iops: NotRequired["capo_imagebuilder.types.ebs_iops_integer.EbsIopsInteger"]
    """<p>The IOPS value for the device. Required only when volumeType is io1 or io2.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the KMS key to use when encrypting the device. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    snapshot_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The snapshot that defines the device contents.</p>"""
    volume_size: NotRequired[
        "capo_imagebuilder.types.ebs_volume_size_integer.EbsVolumeSizeInteger"
    ]
    """<p>Overrides the volume size for the device.</p>"""
    volume_type: NotRequired["capo_imagebuilder.types.ebs_volume_type.EbsVolumeType"]
    """<p>Overrides the volume type for the device.</p>"""
    throughput: NotRequired[
        "capo_imagebuilder.types.ebs_volume_throughput.EbsVolumeThroughput"
    ]
    """<p> <b>For GP3 volumes only</b> – The throughput in MiB/s that the volume supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsInstanceBlockDeviceSpecification) -> dict:
    out: dict = {}
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "delete_on_termination" in value:
        out["deleteOnTermination"] = value["delete_on_termination"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "snapshot_id" in value:
        out["snapshotId"] = value["snapshot_id"]
    if "volume_size" in value:
        out["volumeSize"] = value["volume_size"]
    if "volume_type" in value:
        import capo_imagebuilder.types.ebs_volume_type

        out["volumeType"] = capo_imagebuilder.types.ebs_volume_type.serialize_json(
            value["volume_type"]
        )
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    return out


def deserialize_json(data: dict) -> EbsInstanceBlockDeviceSpecification:
    out: EbsInstanceBlockDeviceSpecification = {}  # type: ignore[typeddict-item]
    if data.get("encrypted") is not None:
        out["encrypted"] = data["encrypted"]
    if data.get("deleteOnTermination") is not None:
        out["delete_on_termination"] = data["deleteOnTermination"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("snapshotId") is not None:
        out["snapshot_id"] = data["snapshotId"]
    if data.get("volumeSize") is not None:
        out["volume_size"] = data["volumeSize"]
    if data.get("volumeType") is not None:
        import capo_imagebuilder.types.ebs_volume_type

        out["volume_type"] = capo_imagebuilder.types.ebs_volume_type.deserialize_json(
            data["volumeType"]
        )
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    return out
