"""Generated from Smithy shape ``com.amazonaws.storagegateway#CachediSCSIVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.created_date
    import capo_storage_gateway.types.double_object
    import capo_storage_gateway.types.kms_key
    import capo_storage_gateway.types.long
    import capo_storage_gateway.types.snapshot_id
    import capo_storage_gateway.types.target_name
    import capo_storage_gateway.types.volume_arn
    import capo_storage_gateway.types.volume_attachment_status
    import capo_storage_gateway.types.volume_id
    import capo_storage_gateway.types.volume_status
    import capo_storage_gateway.types.volume_type
    import capo_storage_gateway.types.volume_used_in_bytes
    import capo_storage_gateway.types.volumei_scsi_attributes


class CachediSCSIVolume(TypedDict, closed=True):
    volume_arn: NotRequired["capo_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) of the storage volume.</p>"""
    volume_id: NotRequired["capo_storage_gateway.types.volume_id.VolumeId"]
    """<p>The unique identifier of the volume, e.g., vol-AE4B946D.</p>"""
    volume_type: NotRequired["capo_storage_gateway.types.volume_type.VolumeType"]
    """<p>One of the VolumeType enumeration values that describes the type of the volume.</p>"""
    volume_status: NotRequired["capo_storage_gateway.types.volume_status.VolumeStatus"]
    """<p>One of the VolumeStatus values that indicates the state of the storage volume.</p>"""
    volume_attachment_status: NotRequired[
        "capo_storage_gateway.types.volume_attachment_status.VolumeAttachmentStatus"
    ]
    """<p>A value that indicates whether a storage volume is attached to or detached from a gateway. For more information, see <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume">Moving your volumes to a different gateway</a>.</p>"""
    volume_size_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The size, in bytes, of the volume capacity.</p>"""
    volume_progress: NotRequired[
        "capo_storage_gateway.types.double_object.DoubleObject"
    ]
    """<p>Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the cached volume is not restoring or bootstrapping.</p>"""
    source_snapshot_id: NotRequired["capo_storage_gateway.types.snapshot_id.SnapshotId"]
    """<p>If the cached volume was created from a snapshot, this field contains the snapshot ID used, e.g., snap-78e22663. Otherwise, this field is not included.</p>"""
    volumei_scsi_attributes: NotRequired[
        "capo_storage_gateway.types.volumei_scsi_attributes.VolumeiSCSIAttributes"
    ]
    """<p>An <a>VolumeiSCSIAttributes</a> object that represents a collection of iSCSI attributes for one stored volume.</p>"""
    created_date: NotRequired["capo_storage_gateway.types.created_date.CreatedDate"]
    """<p>The date the volume was created. Volumes created prior to March 28, 2017 don’t have this timestamp.</p>"""
    volume_used_in_bytes: NotRequired[
        "capo_storage_gateway.types.volume_used_in_bytes.VolumeUsedInBytes"
    ]
    """<p>The size of the data stored on the volume in bytes. This value is calculated based on the number of blocks that are touched, instead of the actual amount of data written. This value can be useful for sequential write patterns but less accurate for random write patterns. <code>VolumeUsedInBytes</code> is different from the compressed size of the volume, which is the value that is used to calculate your bill.</p> <note> <p>This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.</p> <p>If you use a delete tool that overwrites the data on your volume with random data, your usage will not be reduced. This is because the random data is not compressible. If you want to reduce the amount of billed storage on your volume, we recommend overwriting your files with zeros to compress the data to a negligible amount of actual storage.</p> </note>"""
    kms_key: NotRequired["capo_storage_gateway.types.kms_key.KMSKey"]
    target_name: NotRequired["capo_storage_gateway.types.target_name.TargetName"]
    """<p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CachediSCSIVolume) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "volume_type" in value:
        out["VolumeType"] = value["volume_type"]
    if "volume_status" in value:
        out["VolumeStatus"] = value["volume_status"]
    if "volume_attachment_status" in value:
        out["VolumeAttachmentStatus"] = value["volume_attachment_status"]
    out["VolumeSizeInBytes"] = value.get("volume_size_in_bytes", 0)
    if "volume_progress" in value:
        out["VolumeProgress"] = (
            "NaN"
            if value["volume_progress"] != value["volume_progress"]
            else "Infinity"
            if value["volume_progress"] == float("inf")
            else "-Infinity"
            if value["volume_progress"] == float("-inf")
            else value["volume_progress"]
        )
    if "source_snapshot_id" in value:
        out["SourceSnapshotId"] = value["source_snapshot_id"]
    if "volumei_scsi_attributes" in value:
        import capo_storage_gateway.types.volumei_scsi_attributes

        out["VolumeiSCSIAttributes"] = (
            capo_storage_gateway.types.volumei_scsi_attributes.serialize_aws_json_1_1(
                value["volumei_scsi_attributes"]
            )
        )
    if "created_date" in value:
        import capo_storage_gateway.types.created_date

        out["CreatedDate"] = (
            capo_storage_gateway.types.created_date.serialize_aws_json_1_1(
                value["created_date"]
            )
        )
    if "volume_used_in_bytes" in value:
        out["VolumeUsedInBytes"] = value["volume_used_in_bytes"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "target_name" in value:
        out["TargetName"] = value["target_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CachediSCSIVolume:
    out: CachediSCSIVolume = {}  # type: ignore[typeddict-item]
    if data.get("VolumeARN") is not None:
        out["volume_arn"] = data["VolumeARN"]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    if data.get("VolumeType") is not None:
        out["volume_type"] = data["VolumeType"]
    if data.get("VolumeStatus") is not None:
        out["volume_status"] = data["VolumeStatus"]
    if data.get("VolumeAttachmentStatus") is not None:
        out["volume_attachment_status"] = data["VolumeAttachmentStatus"]
    if data.get("VolumeSizeInBytes") is not None:
        out["volume_size_in_bytes"] = data["VolumeSizeInBytes"]
    else:
        out["volume_size_in_bytes"] = 0
    if data.get("VolumeProgress") is not None:
        out["volume_progress"] = float(data["VolumeProgress"])
    if data.get("SourceSnapshotId") is not None:
        out["source_snapshot_id"] = data["SourceSnapshotId"]
    if data.get("VolumeiSCSIAttributes") is not None:
        import capo_storage_gateway.types.volumei_scsi_attributes

        out["volumei_scsi_attributes"] = (
            capo_storage_gateway.types.volumei_scsi_attributes.deserialize_aws_json_1_1(
                data["VolumeiSCSIAttributes"]
            )
        )
    if data.get("CreatedDate") is not None:
        import capo_storage_gateway.types.created_date

        out["created_date"] = (
            capo_storage_gateway.types.created_date.deserialize_aws_json_1_1(
                data["CreatedDate"]
            )
        )
    if data.get("VolumeUsedInBytes") is not None:
        out["volume_used_in_bytes"] = data["VolumeUsedInBytes"]
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("TargetName") is not None:
        out["target_name"] = data["TargetName"]
    return out
