"""Generated from Smithy shape ``com.amazonaws.fsx#CreateOpenZFSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.create_open_zfs_origin_snapshot_configuration
    import capo_fsx.types.flag
    import capo_fsx.types.integer_no_max_from_negative_one
    import capo_fsx.types.integer_record_size_ki_b
    import capo_fsx.types.open_zfs_data_compression_type
    import capo_fsx.types.open_zfs_nfs_exports
    import capo_fsx.types.open_zfs_user_and_group_quotas
    import capo_fsx.types.read_only
    import capo_fsx.types.volume_id


class CreateOpenZFSVolumeConfiguration(TypedDict, closed=True):
    parent_volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume to use as the parent volume of the volume that you are creating.</p>"""
    storage_capacity_reservation_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max_from_negative_one.IntegerNoMaxFromNegativeOne"
    ]
    """<p>Specifies the amount of storage in gibibytes (GiB) to reserve from the parent volume. Setting <code>StorageCapacityReservationGiB</code> guarantees that the specified amount of storage space on the parent volume will always be available for the volume. You can't reserve more storage than the parent volume has. To <i>not</i> specify a storage capacity reservation, set this to <code>0</code> or <code>-1</code>. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties">Volume properties</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    storage_capacity_quota_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max_from_negative_one.IntegerNoMaxFromNegativeOne"
    ]
    """<p>Sets the maximum storage size in gibibytes (GiB) for the volume. You can specify a quota that is larger than the storage on the parent volume. A volume quota limits the amount of storage that the volume can consume to the configured amount, but does not guarantee the space will be available on the parent volume. To guarantee quota space, you must also set <code>StorageCapacityReservationGiB</code>. To <i>not</i> specify a storage capacity quota, set this to <code>-1</code>. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties">Volume properties</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    record_size_ki_b: NotRequired[
        "capo_fsx.types.integer_record_size_ki_b.IntegerRecordSizeKiB"
    ]
    """<p>Specifies the suggested block size for a volume in a ZFS dataset, in kibibytes (KiB). For file systems using the Intelligent-Tiering storage class, valid values are 128, 256, 512, 1024, 2048, or 4096 KiB, with a default of 1024 KiB. For all other file systems, valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB, with a default of 128 KiB. We recommend using the default setting for the majority of use cases. Generally, workloads that write in fixed small or large record sizes may benefit from setting a custom record size, like database workloads (small record size) or media streaming workloads (large record size). For additional guidance on when to set a custom record size, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#record-size-performance"> ZFS Record size</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    data_compression_type: NotRequired[
        "capo_fsx.types.open_zfs_data_compression_type.OpenZFSDataCompressionType"
    ]
    """<p>Specifies the method used to compress the data on the volume. The compression type is <code>NONE</code> by default.</p> <ul> <li> <p> <code>NONE</code> - Doesn't compress the data on the volume. <code>NONE</code> is the default.</p> </li> <li> <p> <code>ZSTD</code> - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. ZSTD compression provides a higher level of data compression and higher read throughput performance than LZ4 compression.</p> </li> <li> <p> <code>LZ4</code> - Compresses the data in the volume using the LZ4 compression algorithm. LZ4 compression provides a lower level of compression and higher write throughput performance than ZSTD compression.</p> </li> </ul> <p>For more information about volume compression types and the performance of your Amazon FSx for OpenZFS file system, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs"> Tips for maximizing performance</a> File system and volume settings in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    copy_tags_to_snapshots: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to <code>false</code>. If this value is set to <code>true</code>, and you do not specify any tags, all tags for the original volume are copied over to snapshots. If this value is set to <code>true</code>, and you do specify one or more tags, only the specified tags for the original volume are copied over to snapshots. If you specify one or more tags when creating a new snapshot, no tags are copied over from the original volume, regardless of this value. </p>"""
    origin_snapshot: NotRequired[
        "capo_fsx.types.create_open_zfs_origin_snapshot_configuration.CreateOpenZFSOriginSnapshotConfiguration"
    ]
    """<p>The configuration object that specifies the snapshot to use as the origin of the data for the volume.</p>"""
    read_only: NotRequired["capo_fsx.types.read_only.ReadOnly"]
    """<p>A Boolean value indicating whether the volume is read-only.</p>"""
    nfs_exports: NotRequired["capo_fsx.types.open_zfs_nfs_exports.OpenZFSNfsExports"]
    """<p>The configuration object for mounting a Network File System (NFS) file system.</p>"""
    user_and_group_quotas: NotRequired[
        "capo_fsx.types.open_zfs_user_and_group_quotas.OpenZFSUserAndGroupQuotas"
    ]
    """<p>Configures how much storage users and groups can use on the volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOpenZFSVolumeConfiguration) -> dict:
    out: dict = {}
    if "parent_volume_id" in value:
        out["ParentVolumeId"] = value["parent_volume_id"]
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
        import capo_fsx.types.create_open_zfs_origin_snapshot_configuration

        out["OriginSnapshot"] = (
            capo_fsx.types.create_open_zfs_origin_snapshot_configuration.serialize_aws_json_1_1(
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOpenZFSVolumeConfiguration:
    out: CreateOpenZFSVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ParentVolumeId") is not None:
        out["parent_volume_id"] = data["ParentVolumeId"]
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
        import capo_fsx.types.create_open_zfs_origin_snapshot_configuration

        out["origin_snapshot"] = (
            capo_fsx.types.create_open_zfs_origin_snapshot_configuration.deserialize_aws_json_1_1(
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
    return out
