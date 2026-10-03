"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.flag
    import capo_fsx.types.integer_no_max
    import capo_fsx.types.integer_record_size_ki_b
    import capo_fsx.types.open_zfs_copy_strategy
    import capo_fsx.types.open_zfs_data_compression_type
    import capo_fsx.types.open_zfs_nfs_exports
    import capo_fsx.types.open_zfs_origin_snapshot_configuration
    import capo_fsx.types.open_zfs_user_and_group_quotas
    import capo_fsx.types.read_only
    import capo_fsx.types.resource_arn
    import capo_fsx.types.snapshot_id
    import capo_fsx.types.volume_id
    import capo_fsx.types.volume_path


class OpenZFSVolumeConfiguration(TypedDict, closed=True):
    parent_volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the parent volume.</p>"""
    volume_path: NotRequired["capo_fsx.types.volume_path.VolumePath"]
    """<p>The path to the volume from the root volume. For example, <code>fsx/parentVolume/volume1</code>.</p>"""
    storage_capacity_reservation_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max.IntegerNoMax"
    ]
    """<p>The amount of storage in gibibytes (GiB) to reserve from the parent volume. You can't reserve more storage than the parent volume has reserved.</p>"""
    storage_capacity_quota_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max.IntegerNoMax"
    ]
    """<p>The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume.</p>"""
    record_size_ki_b: NotRequired[
        "capo_fsx.types.integer_record_size_ki_b.IntegerRecordSizeKiB"
    ]
    """<p>The record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. For guidance on when to set a custom record size, see the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    data_compression_type: NotRequired[
        "capo_fsx.types.open_zfs_data_compression_type.OpenZFSDataCompressionType"
    ]
    """<p>Specifies the method used to compress the data on the volume. The compression type is <code>NONE</code> by default.</p> <ul> <li> <p> <code>NONE</code> - Doesn't compress the data on the volume. <code>NONE</code> is the default.</p> </li> <li> <p> <code>ZSTD</code> - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.</p> </li> <li> <p> <code>LZ4</code> - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.</p> </li> </ul>"""
    copy_tags_to_snapshots: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is <code>true</code> and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.</p>"""
    origin_snapshot: NotRequired[
        "capo_fsx.types.open_zfs_origin_snapshot_configuration.OpenZFSOriginSnapshotConfiguration"
    ]
    """<p>The configuration object that specifies the snapshot to use as the origin of the data for the volume.</p>"""
    read_only: NotRequired["capo_fsx.types.read_only.ReadOnly"]
    """<p>A Boolean value indicating whether the volume is read-only.</p>"""
    nfs_exports: NotRequired["capo_fsx.types.open_zfs_nfs_exports.OpenZFSNfsExports"]
    """<p>The configuration object for mounting a Network File System (NFS) file system.</p>"""
    user_and_group_quotas: NotRequired[
        "capo_fsx.types.open_zfs_user_and_group_quotas.OpenZFSUserAndGroupQuotas"
    ]
    """<p>An object specifying how much storage users or groups can use on the volume.</p>"""
    restore_to_snapshot: NotRequired["capo_fsx.types.snapshot_id.SnapshotId"]
    """<p>Specifies the ID of the snapshot to which the volume was restored.</p>"""
    delete_intermediate_snaphots: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether snapshots between the current state and the specified snapshot should be deleted when a volume is restored from snapshot.</p>"""
    delete_cloned_volumes: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether dependent clone volumes created from intermediate snapshots should be deleted when a volume is restored from snapshot.</p>"""
    delete_intermediate_data: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether snapshot data that differs between the current state and the specified snapshot should be overwritten when a volume is restored from a snapshot.</p>"""
    source_snapshot_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    destination_snapshot: NotRequired["capo_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot that's being copied or was most recently copied to the destination volume.</p>"""
    copy_strategy: NotRequired[
        "capo_fsx.types.open_zfs_copy_strategy.OpenZFSCopyStrategy"
    ]
    """<p>Specifies the strategy used when copying data from the snapshot to the new volume. </p> <ul> <li> <p> <code>CLONE</code> - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data.</p> </li> <li> <p> <code>FULL_COPY</code> - Copies all data from the snapshot to the new volume.</p> <p>Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.</p> </li> </ul> <note> <p>The <code>INCREMENTAL_COPY</code> option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html">CopySnapshotAndUpdateVolume</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSVolumeConfiguration) -> dict:
    out: dict = {}
    if "parent_volume_id" in value:
        out["ParentVolumeId"] = value["parent_volume_id"]
    if "volume_path" in value:
        out["VolumePath"] = value["volume_path"]
    if "storage_capacity_reservation_gi_b" in value:
        out["StorageCapacityReservationGiB"] = value[
            "storage_capacity_reservation_gi_b"
        ]
    if "storage_capacity_quota_gi_b" in value:
        out["StorageCapacityQuotaGiB"] = value["storage_capacity_quota_gi_b"]
    if "record_size_ki_b" in value:
        out["RecordSizeKiB"] = value["record_size_ki_b"]
    if "data_compression_type" in value:
        import capo_fsx.types.open_zfs_data_compression_type

        out["DataCompressionType"] = (
            capo_fsx.types.open_zfs_data_compression_type.serialize_aws_json_1_1(
                value["data_compression_type"]
            )
        )
    if "copy_tags_to_snapshots" in value:
        out["CopyTagsToSnapshots"] = value["copy_tags_to_snapshots"]
    if "origin_snapshot" in value:
        import capo_fsx.types.open_zfs_origin_snapshot_configuration

        out["OriginSnapshot"] = (
            capo_fsx.types.open_zfs_origin_snapshot_configuration.serialize_aws_json_1_1(
                value["origin_snapshot"]
            )
        )
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    if "nfs_exports" in value:
        import capo_fsx.types.open_zfs_nfs_exports

        out["NfsExports"] = capo_fsx.types.open_zfs_nfs_exports.serialize_aws_json_1_1(
            value["nfs_exports"]
        )
    if "user_and_group_quotas" in value:
        import capo_fsx.types.open_zfs_user_and_group_quotas

        out["UserAndGroupQuotas"] = (
            capo_fsx.types.open_zfs_user_and_group_quotas.serialize_aws_json_1_1(
                value["user_and_group_quotas"]
            )
        )
    if "restore_to_snapshot" in value:
        out["RestoreToSnapshot"] = value["restore_to_snapshot"]
    if "delete_intermediate_snaphots" in value:
        out["DeleteIntermediateSnaphots"] = value["delete_intermediate_snaphots"]
    if "delete_cloned_volumes" in value:
        out["DeleteClonedVolumes"] = value["delete_cloned_volumes"]
    if "delete_intermediate_data" in value:
        out["DeleteIntermediateData"] = value["delete_intermediate_data"]
    if "source_snapshot_arn" in value:
        out["SourceSnapshotARN"] = value["source_snapshot_arn"]
    if "destination_snapshot" in value:
        out["DestinationSnapshot"] = value["destination_snapshot"]
    if "copy_strategy" in value:
        import capo_fsx.types.open_zfs_copy_strategy

        out["CopyStrategy"] = (
            capo_fsx.types.open_zfs_copy_strategy.serialize_aws_json_1_1(
                value["copy_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSVolumeConfiguration:
    out: OpenZFSVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ParentVolumeId") is not None:
        out["parent_volume_id"] = data["ParentVolumeId"]
    if data.get("VolumePath") is not None:
        out["volume_path"] = data["VolumePath"]
    if data.get("StorageCapacityReservationGiB") is not None:
        out["storage_capacity_reservation_gi_b"] = data["StorageCapacityReservationGiB"]
    if data.get("StorageCapacityQuotaGiB") is not None:
        out["storage_capacity_quota_gi_b"] = data["StorageCapacityQuotaGiB"]
    if data.get("RecordSizeKiB") is not None:
        out["record_size_ki_b"] = data["RecordSizeKiB"]
    if data.get("DataCompressionType") is not None:
        import capo_fsx.types.open_zfs_data_compression_type

        out["data_compression_type"] = (
            capo_fsx.types.open_zfs_data_compression_type.deserialize_aws_json_1_1(
                data["DataCompressionType"]
            )
        )
    if data.get("CopyTagsToSnapshots") is not None:
        out["copy_tags_to_snapshots"] = data["CopyTagsToSnapshots"]
    if data.get("OriginSnapshot") is not None:
        import capo_fsx.types.open_zfs_origin_snapshot_configuration

        out["origin_snapshot"] = (
            capo_fsx.types.open_zfs_origin_snapshot_configuration.deserialize_aws_json_1_1(
                data["OriginSnapshot"]
            )
        )
    if data.get("ReadOnly") is not None:
        out["read_only"] = data["ReadOnly"]
    if data.get("NfsExports") is not None:
        import capo_fsx.types.open_zfs_nfs_exports

        out["nfs_exports"] = (
            capo_fsx.types.open_zfs_nfs_exports.deserialize_aws_json_1_1(
                data["NfsExports"]
            )
        )
    if data.get("UserAndGroupQuotas") is not None:
        import capo_fsx.types.open_zfs_user_and_group_quotas

        out["user_and_group_quotas"] = (
            capo_fsx.types.open_zfs_user_and_group_quotas.deserialize_aws_json_1_1(
                data["UserAndGroupQuotas"]
            )
        )
    if data.get("RestoreToSnapshot") is not None:
        out["restore_to_snapshot"] = data["RestoreToSnapshot"]
    if data.get("DeleteIntermediateSnaphots") is not None:
        out["delete_intermediate_snaphots"] = data["DeleteIntermediateSnaphots"]
    if data.get("DeleteClonedVolumes") is not None:
        out["delete_cloned_volumes"] = data["DeleteClonedVolumes"]
    if data.get("DeleteIntermediateData") is not None:
        out["delete_intermediate_data"] = data["DeleteIntermediateData"]
    if data.get("SourceSnapshotARN") is not None:
        out["source_snapshot_arn"] = data["SourceSnapshotARN"]
    if data.get("DestinationSnapshot") is not None:
        out["destination_snapshot"] = data["DestinationSnapshot"]
    if data.get("CopyStrategy") is not None:
        import capo_fsx.types.open_zfs_copy_strategy

        out["copy_strategy"] = (
            capo_fsx.types.open_zfs_copy_strategy.deserialize_aws_json_1_1(
                data["CopyStrategy"]
            )
        )
    return out
