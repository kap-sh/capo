"""Generated from Smithy shape ``com.amazonaws.fsx#CreateOpenZFSOriginSnapshotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.open_zfs_copy_strategy
    import capo_fsx.types.resource_arn


class CreateOpenZFSOriginSnapshotConfiguration(TypedDict, closed=True):
    snapshot_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    copy_strategy: NotRequired[
        "capo_fsx.types.open_zfs_copy_strategy.OpenZFSCopyStrategy"
    ]
    """<p>Specifies the strategy used when copying data from the snapshot to the new volume. </p> <ul> <li> <p> <code>CLONE</code> - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data.</p> </li> <li> <p> <code>FULL_COPY</code> - Copies all data from the snapshot to the new volume.</p> <p>Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.</p> </li> </ul> <note> <p>The <code>INCREMENTAL_COPY</code> option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html">CopySnapshotAndUpdateVolume</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOpenZFSOriginSnapshotConfiguration) -> dict:
    out: dict = {}
    if "snapshot_arn" in value:
        out["SnapshotARN"] = value["snapshot_arn"]
    if "copy_strategy" in value:
        import capo_fsx.types.open_zfs_copy_strategy

        out["CopyStrategy"] = (
            capo_fsx.types.open_zfs_copy_strategy.serialize_aws_json_1_1(
                value["copy_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOpenZFSOriginSnapshotConfiguration:
    out: CreateOpenZFSOriginSnapshotConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotARN") is not None:
        out["snapshot_arn"] = data["SnapshotARN"]
    if data.get("CopyStrategy") is not None:
        import capo_fsx.types.open_zfs_copy_strategy

        out["copy_strategy"] = (
            capo_fsx.types.open_zfs_copy_strategy.deserialize_aws_json_1_1(
                data["CopyStrategy"]
            )
        )
    return out
