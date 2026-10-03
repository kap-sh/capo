"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateOntapVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.flag
    import capo_fsx.types.junction_path
    import capo_fsx.types.security_style
    import capo_fsx.types.snapshot_policy
    import capo_fsx.types.tiering_policy
    import capo_fsx.types.update_snaplock_configuration
    import capo_fsx.types.volume_capacity
    import capo_fsx.types.volume_capacity_bytes


class UpdateOntapVolumeConfiguration(TypedDict, closed=True):
    junction_path: NotRequired["capo_fsx.types.junction_path.JunctionPath"]
    """<p>Specifies the location in the SVM's namespace where the volume is mounted. The <code>JunctionPath</code> must have a leading forward slash, such as <code>/vol3</code>.</p>"""
    security_style: NotRequired["capo_fsx.types.security_style.SecurityStyle"]
    """<p>The security style for the volume, which can be <code>UNIX</code>, <code>NTFS</code>, or <code>MIXED</code>.</p>"""
    size_in_megabytes: NotRequired["capo_fsx.types.volume_capacity.VolumeCapacity"]
    """<p>Specifies the size of the volume in megabytes.</p>"""
    storage_efficiency_enabled: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>Default is <code>false</code>. Set to true to enable the deduplication, compression, and compaction storage efficiency features on the volume.</p>"""
    tiering_policy: NotRequired["capo_fsx.types.tiering_policy.TieringPolicy"]
    """<p>Update the volume's data tiering policy.</p>"""
    snapshot_policy: NotRequired["capo_fsx.types.snapshot_policy.SnapshotPolicy"]
    """<p>Specifies the snapshot policy for the volume. There are three built-in snapshot policies:</p> <ul> <li> <p> <code>default</code>: This is the default policy. A maximum of six hourly snapshots taken five minutes past the hour. A maximum of two daily snapshots taken Monday through Saturday at 10 minutes after midnight. A maximum of two weekly snapshots taken every Sunday at 15 minutes after midnight.</p> </li> <li> <p> <code>default-1weekly</code>: This policy is the same as the <code>default</code> policy except that it only retains one snapshot from the weekly schedule.</p> </li> <li> <p> <code>none</code>: This policy does not take any snapshots. This policy can be assigned to volumes to prevent automatic snapshots from being taken.</p> </li> </ul> <p>You can also provide the name of a custom policy that you created with the ONTAP CLI or REST API.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snapshots-ontap.html#snapshot-policies">Snapshot policies</a> in the <i>Amazon FSx for NetApp ONTAP User Guide</i>.</p>"""
    copy_tags_to_backups: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A boolean flag indicating whether tags for the volume should be copied to backups. This value defaults to false. If it's set to true, all tags for the volume are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the volume, regardless of this value.</p>"""
    snaplock_configuration: NotRequired[
        "capo_fsx.types.update_snaplock_configuration.UpdateSnaplockConfiguration"
    ]
    """<p>The configuration object for updating the SnapLock configuration of an FSx for ONTAP SnapLock volume. </p>"""
    size_in_bytes: NotRequired[
        "capo_fsx.types.volume_capacity_bytes.VolumeCapacityBytes"
    ]
    """<p>The configured size of the volume, in bytes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOntapVolumeConfiguration) -> dict:
    out: dict = {}
    if "junction_path" in value:
        out["JunctionPath"] = value["junction_path"]
    if "security_style" in value:
        import capo_fsx.types.security_style

        out["SecurityStyle"] = capo_fsx.types.security_style.serialize_aws_json_1_1(
            value["security_style"]
        )
    if "size_in_megabytes" in value:
        out["SizeInMegabytes"] = value["size_in_megabytes"]
    if "storage_efficiency_enabled" in value:
        out["StorageEfficiencyEnabled"] = value["storage_efficiency_enabled"]
    if "tiering_policy" in value:
        import capo_fsx.types.tiering_policy

        out["TieringPolicy"] = capo_fsx.types.tiering_policy.serialize_aws_json_1_1(
            value["tiering_policy"]
        )
    if "snapshot_policy" in value:
        out["SnapshotPolicy"] = value["snapshot_policy"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "snaplock_configuration" in value:
        import capo_fsx.types.update_snaplock_configuration

        out["SnaplockConfiguration"] = (
            capo_fsx.types.update_snaplock_configuration.serialize_aws_json_1_1(
                value["snaplock_configuration"]
            )
        )
    if "size_in_bytes" in value:
        out["SizeInBytes"] = value["size_in_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOntapVolumeConfiguration:
    out: UpdateOntapVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("JunctionPath") is not None:
        out["junction_path"] = data["JunctionPath"]
    if data.get("SecurityStyle") is not None:
        import capo_fsx.types.security_style

        out["security_style"] = capo_fsx.types.security_style.deserialize_aws_json_1_1(
            data["SecurityStyle"]
        )
    if data.get("SizeInMegabytes") is not None:
        out["size_in_megabytes"] = data["SizeInMegabytes"]
    if data.get("StorageEfficiencyEnabled") is not None:
        out["storage_efficiency_enabled"] = data["StorageEfficiencyEnabled"]
    if data.get("TieringPolicy") is not None:
        import capo_fsx.types.tiering_policy

        out["tiering_policy"] = capo_fsx.types.tiering_policy.deserialize_aws_json_1_1(
            data["TieringPolicy"]
        )
    if data.get("SnapshotPolicy") is not None:
        out["snapshot_policy"] = data["SnapshotPolicy"]
    if data.get("CopyTagsToBackups") is not None:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if data.get("SnaplockConfiguration") is not None:
        import capo_fsx.types.update_snaplock_configuration

        out["snaplock_configuration"] = (
            capo_fsx.types.update_snaplock_configuration.deserialize_aws_json_1_1(
                data["SnaplockConfiguration"]
            )
        )
    if data.get("SizeInBytes") is not None:
        out["size_in_bytes"] = data["SizeInBytes"]
    return out
