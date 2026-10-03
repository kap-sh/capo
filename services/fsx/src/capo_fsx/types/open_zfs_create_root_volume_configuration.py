"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSCreateRootVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.flag
    import capo_fsx.types.integer_record_size_ki_b
    import capo_fsx.types.open_zfs_data_compression_type
    import capo_fsx.types.open_zfs_nfs_exports
    import capo_fsx.types.open_zfs_user_and_group_quotas
    import capo_fsx.types.read_only


class OpenZFSCreateRootVolumeConfiguration(TypedDict, closed=True):
    record_size_ki_b: NotRequired[
        "capo_fsx.types.integer_record_size_ki_b.IntegerRecordSizeKiB"
    ]
    """<p>Specifies the record size of an OpenZFS root volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on setting a custom record size, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs"> Tips for maximizing performance</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    data_compression_type: NotRequired[
        "capo_fsx.types.open_zfs_data_compression_type.OpenZFSDataCompressionType"
    ]
    """<p>Specifies the method used to compress the data on the volume. The compression type is <code>NONE</code> by default.</p> <ul> <li> <p> <code>NONE</code> - Doesn't compress the data on the volume. <code>NONE</code> is the default.</p> </li> <li> <p> <code>ZSTD</code> - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.</p> </li> <li> <p> <code>LZ4</code> - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.</p> </li> </ul>"""
    nfs_exports: NotRequired["capo_fsx.types.open_zfs_nfs_exports.OpenZFSNfsExports"]
    """<p>The configuration object for mounting a file system.</p>"""
    user_and_group_quotas: NotRequired[
        "capo_fsx.types.open_zfs_user_and_group_quotas.OpenZFSUserAndGroupQuotas"
    ]
    """<p>An object specifying how much storage users or groups can use on the volume.</p>"""
    copy_tags_to_snapshots: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the volume should be copied to snapshots of the volume. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is <code>true</code> and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value. </p>"""
    read_only: NotRequired["capo_fsx.types.read_only.ReadOnly"]
    """<p>A Boolean value indicating whether the volume is read-only. Setting this value to <code>true</code> can be useful after you have completed changes to a volume and no longer want changes to occur. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSCreateRootVolumeConfiguration) -> dict:
    out: dict = {}
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
    if "copy_tags_to_snapshots" in value:
        out["CopyTagsToSnapshots"] = value["copy_tags_to_snapshots"]
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSCreateRootVolumeConfiguration:
    out: OpenZFSCreateRootVolumeConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("CopyTagsToSnapshots") is not None:
        out["copy_tags_to_snapshots"] = data["CopyTagsToSnapshots"]
    if data.get("ReadOnly") is not None:
        out["read_only"] = data["ReadOnly"]
    return out
