"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateOpenZFSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.integer_no_max_from_negative_one
    import capo_fsx.types.integer_record_size_ki_b
    import capo_fsx.types.open_zfs_data_compression_type
    import capo_fsx.types.open_zfs_nfs_exports
    import capo_fsx.types.open_zfs_user_and_group_quotas
    import capo_fsx.types.read_only


class UpdateOpenZFSVolumeConfiguration(TypedDict, closed=True):
    storage_capacity_reservation_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max_from_negative_one.IntegerNoMaxFromNegativeOne"
    ]
    """<p>The amount of storage in gibibytes (GiB) to reserve from the parent volume. You can't reserve more storage than the parent volume has reserved. You can specify a value of <code>-1</code> to unset a volume's storage capacity reservation.</p>"""
    storage_capacity_quota_gi_b: NotRequired[
        "capo_fsx.types.integer_no_max_from_negative_one.IntegerNoMaxFromNegativeOne"
    ]
    """<p>The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume. You can specify a value of <code>-1</code> to unset a volume's storage capacity quota.</p>"""
    record_size_ki_b: NotRequired[
        "capo_fsx.types.integer_record_size_ki_b.IntegerRecordSizeKiB"
    ]
    """<p>Specifies the record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on when to set a custom record size, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs"> Tips for maximizing performance</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    data_compression_type: NotRequired[
        "capo_fsx.types.open_zfs_data_compression_type.OpenZFSDataCompressionType"
    ]
    """<p>Specifies the method used to compress the data on the volume. The compression type is <code>NONE</code> by default.</p> <ul> <li> <p> <code>NONE</code> - Doesn't compress the data on the volume. <code>NONE</code> is the default.</p> </li> <li> <p> <code>ZSTD</code> - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.</p> </li> <li> <p> <code>LZ4</code> - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.</p> </li> </ul>"""
    nfs_exports: NotRequired["capo_fsx.types.open_zfs_nfs_exports.OpenZFSNfsExports"]
    """<p>The configuration object for mounting a Network File System (NFS) file system.</p>"""
    user_and_group_quotas: NotRequired[
        "capo_fsx.types.open_zfs_user_and_group_quotas.OpenZFSUserAndGroupQuotas"
    ]
    """<p>An object specifying how much storage users or groups can use on the volume.</p>"""
    read_only: NotRequired["capo_fsx.types.read_only.ReadOnly"]
    """<p>A Boolean value indicating whether the volume is read-only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOpenZFSVolumeConfiguration) -> dict:
    out: dict = {}
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
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOpenZFSVolumeConfiguration:
    out: UpdateOpenZFSVolumeConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("ReadOnly") is not None:
        out["read_only"] = data["ReadOnly"]
    return out
