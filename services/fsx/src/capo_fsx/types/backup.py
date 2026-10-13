"""Generated from Smithy shape ``com.amazonaws.fsx#Backup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.active_directory_backup_attributes
    import capo_fsx.types.aws_account_id
    import capo_fsx.types.backup_failure_details
    import capo_fsx.types.backup_id
    import capo_fsx.types.backup_lifecycle
    import capo_fsx.types.backup_type
    import capo_fsx.types.creation_time
    import capo_fsx.types.file_system
    import capo_fsx.types.kms_key_id
    import capo_fsx.types.progress_percent
    import capo_fsx.types.region
    import capo_fsx.types.resource_arn
    import capo_fsx.types.resource_type
    import capo_fsx.types.size_in_bytes
    import capo_fsx.types.tags
    import capo_fsx.types.volume


class Backup(TypedDict, closed=True):
    backup_id: NotRequired["capo_fsx.types.backup_id.BackupId"]
    """<p>The ID of the backup.</p>"""
    lifecycle: NotRequired["capo_fsx.types.backup_lifecycle.BackupLifecycle"]
    """<p>The lifecycle status of the backup.</p> <ul> <li> <p> <code>AVAILABLE</code> - The backup is fully available.</p> </li> <li> <p> <code>PENDING</code> - For user-initiated backups on Lustre file systems only; Amazon FSx hasn't started creating the backup.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the backup.</p> </li> <li> <p> <code>TRANSFERRING</code> - For user-initiated backups on Lustre file systems only; Amazon FSx is transferring the backup to Amazon S3.</p> </li> <li> <p> <code>COPYING</code> - Amazon FSx is copying the backup.</p> </li> <li> <p> <code>DELETED</code> - Amazon FSx deleted the backup and it's no longer available.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx couldn't finish the backup.</p> </li> </ul>"""
    failure_details: NotRequired[
        "capo_fsx.types.backup_failure_details.BackupFailureDetails"
    ]
    """<p>Details explaining any failures that occurred when creating a backup.</p>"""
    type: NotRequired["capo_fsx.types.backup_type.BackupType"]
    """<p>The type of the file-system backup.</p>"""
    progress_percent: NotRequired["capo_fsx.types.progress_percent.ProgressPercent"]
    creation_time: NotRequired["capo_fsx.types.creation_time.CreationTime"]
    """<p>The time when a particular backup was created.</p>"""
    kms_key_id: NotRequired["capo_fsx.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt the backup of the Amazon FSx file system's data at rest. </p>"""
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) for the backup resource.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>The tags associated with a particular file system.</p>"""
    file_system: NotRequired["capo_fsx.types.file_system.FileSystem"]
    """<p>The metadata of the file system associated with the backup. This metadata is persisted even if the file system is deleted.</p>"""
    directory_information: NotRequired[
        "capo_fsx.types.active_directory_backup_attributes.ActiveDirectoryBackupAttributes"
    ]
    """<p>The configuration of the self-managed Microsoft Active Directory directory to which the Windows File Server instance is joined.</p>"""
    owner_id: NotRequired["capo_fsx.types.aws_account_id.AWSAccountId"]
    source_backup_id: NotRequired["capo_fsx.types.backup_id.BackupId"]
    source_backup_region: NotRequired["capo_fsx.types.region.Region"]
    """<p>The source Region of the backup. Specifies the Region from where this backup is copied.</p>"""
    resource_type: NotRequired["capo_fsx.types.resource_type.ResourceType"]
    """<p>Specifies the resource type that's backed up.</p>"""
    volume: NotRequired["capo_fsx.types.volume.Volume"]
    size_in_bytes: NotRequired["capo_fsx.types.size_in_bytes.SizeInBytes"]
    """<p> The size of the backup in bytes. This represents the amount of data that the file system would contain if you restore this backup. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backup) -> dict:
    out: dict = {}
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    if "lifecycle" in value:
        import capo_fsx.types.backup_lifecycle

        out["Lifecycle"] = capo_fsx.types.backup_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "failure_details" in value:
        import capo_fsx.types.backup_failure_details

        out["FailureDetails"] = (
            capo_fsx.types.backup_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "type" in value:
        import capo_fsx.types.backup_type

        out["Type"] = capo_fsx.types.backup_type.serialize_aws_json_1_1(value["type"])
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    if "creation_time" in value:
        import capo_fsx.types.creation_time

        out["CreationTime"] = capo_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "file_system" in value:
        import capo_fsx.types.file_system

        out["FileSystem"] = capo_fsx.types.file_system.serialize_aws_json_1_1(
            value["file_system"]
        )
    if "directory_information" in value:
        import capo_fsx.types.active_directory_backup_attributes

        out["DirectoryInformation"] = (
            capo_fsx.types.active_directory_backup_attributes.serialize_aws_json_1_1(
                value["directory_information"]
            )
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "source_backup_id" in value:
        out["SourceBackupId"] = value["source_backup_id"]
    if "source_backup_region" in value:
        out["SourceBackupRegion"] = value["source_backup_region"]
    if "resource_type" in value:
        import capo_fsx.types.resource_type

        out["ResourceType"] = capo_fsx.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "volume" in value:
        import capo_fsx.types.volume

        out["Volume"] = capo_fsx.types.volume.serialize_aws_json_1_1(value["volume"])
    if "size_in_bytes" in value:
        out["SizeInBytes"] = value["size_in_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Backup:
    out: Backup = {}  # type: ignore[typeddict-item]
    if data.get("BackupId") is not None:
        out["backup_id"] = data["BackupId"]
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.backup_lifecycle

        out["lifecycle"] = capo_fsx.types.backup_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if data.get("FailureDetails") is not None:
        import capo_fsx.types.backup_failure_details

        out["failure_details"] = (
            capo_fsx.types.backup_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if data.get("Type") is not None:
        import capo_fsx.types.backup_type

        out["type"] = capo_fsx.types.backup_type.deserialize_aws_json_1_1(data["Type"])
    if data.get("ProgressPercent") is not None:
        out["progress_percent"] = data["ProgressPercent"]
    if data.get("CreationTime") is not None:
        import capo_fsx.types.creation_time

        out["creation_time"] = capo_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("FileSystem") is not None:
        import capo_fsx.types.file_system

        out["file_system"] = capo_fsx.types.file_system.deserialize_aws_json_1_1(
            data["FileSystem"]
        )
    if data.get("DirectoryInformation") is not None:
        import capo_fsx.types.active_directory_backup_attributes

        out["directory_information"] = (
            capo_fsx.types.active_directory_backup_attributes.deserialize_aws_json_1_1(
                data["DirectoryInformation"]
            )
        )
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("SourceBackupId") is not None:
        out["source_backup_id"] = data["SourceBackupId"]
    if data.get("SourceBackupRegion") is not None:
        out["source_backup_region"] = data["SourceBackupRegion"]
    if data.get("ResourceType") is not None:
        import capo_fsx.types.resource_type

        out["resource_type"] = capo_fsx.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    if data.get("Volume") is not None:
        import capo_fsx.types.volume

        out["volume"] = capo_fsx.types.volume.deserialize_aws_json_1_1(data["Volume"])
    if data.get("SizeInBytes") is not None:
        out["size_in_bytes"] = data["SizeInBytes"]
    return out


def redact_sensitive(value: Backup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_system" in value:
        import capo_fsx.types.file_system

        out["file_system"] = capo_fsx.types.file_system.redact_sensitive(
            value["file_system"]
        )
    if "volume" in value:
        import capo_fsx.types.volume

        out["volume"] = capo_fsx.types.volume.redact_sensitive(value["volume"])
    return out
