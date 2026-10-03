"""Generated from Smithy shape ``com.amazonaws.backup#DescribeRecoveryPointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.boolean2
    import capo_backup.types.calculated_lifecycle
    import capo_backup.types.encryption_key_type
    import capo_backup.types.iam_role_arn
    import capo_backup.types.index_status
    import capo_backup.types.lifecycle
    import capo_backup.types.long
    import capo_backup.types.recovery_point_creator
    import capo_backup.types.recovery_point_status
    import capo_backup.types.resource_type
    import capo_backup.types.scan_results
    import capo_backup.types.storage_class
    import capo_backup.types.string
    import capo_backup.types.timestamp
    import capo_backup.types.vault_type


class DescribeRecoveryPointOutput(TypedDict, closed=True):
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>"""
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    source_backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the source vault where the resource was originally backed up in; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>. If the recovery is restored to the same Amazon Web Services account or Region, this value will be <code>null</code>.</p>"""
    resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource to save as a recovery point; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>"""
    created_by: NotRequired[
        "capo_backup.types.recovery_point_creator.RecoveryPointCreator"
    ]
    """<p>Contains identifying information about the creation of a recovery point, including the <code>BackupPlanArn</code>, <code>BackupPlanId</code>, <code>BackupPlanVersion</code>, and <code>BackupRuleId</code> of the backup plan used to create it.</p>"""
    iam_role_arn: NotRequired["capo_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    status: NotRequired["capo_backup.types.recovery_point_status.RecoveryPointStatus"]
    """<p>A status code specifying the state of the recovery point. For more information, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/applicationstackbackups.html#cfnrecoverypointstatus"> Recovery point status</a> in the <i>Backup Developer Guide</i>.</p> <ul> <li> <p> <code>CREATING</code> status indicates that an Backup job has been initiated for a resource. The backup process has started and is actively processing a backup job for the associated recovery point.</p> </li> <li> <p> <code>AVAILABLE</code> status indicates that the backup was successfully created for the recovery point. The backup process has completed without any issues, and the recovery point is now ready for use.</p> </li> <li> <p> <code>PARTIAL</code> status indicates a composite recovery point has one or more nested recovery points that were not in the backup.</p> </li> <li> <p> <code>EXPIRED</code> status indicates that the recovery point has exceeded its retention period, but Backup lacks permission or is otherwise unable to delete it. To manually delete these recovery points, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/gs-cleanup-resources.html#cleanup-backups"> Step 3: Delete the recovery points</a> in the <i>Clean up resources</i> section of <i>Getting started</i>.</p> </li> <li> <p> <code>STOPPED</code> status occurs on a continuous backup where a user has taken some action that causes the continuous backup to be disabled. This can be caused by the removal of permissions, turning off versioning, turning off events being sent to EventBridge, or disabling the EventBridge rules that are put in place by Backup. For recovery points of Amazon S3, Amazon RDS, and Amazon Aurora resources, this status occurs when the retention period of a continuous backup rule is changed.</p> <p>To resolve <code>STOPPED</code> status, ensure that all requested permissions are in place and that versioning is enabled on the S3 bucket. Once these conditions are met, the next instance of a backup rule running will result in a new continuous recovery point being created. The recovery points with STOPPED status do not need to be deleted.</p> <p>For SAP HANA on Amazon EC2 <code>STOPPED</code> status occurs due to user action, application misconfiguration, or backup failure. To ensure that future continuous backups succeed, refer to the recovery point status and check SAP HANA for details.</p> </li> </ul>"""
    status_message: NotRequired["capo_backup.types.string.string"]
    """<p>A status message explaining the status of the recovery point.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a recovery point is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    initiation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time when the backup job that created this recovery point was initiated, in Unix format and Coordinated Universal Time (UTC).</p>"""
    completion_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a job to create a recovery point is completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    backup_size_in_bytes: NotRequired["capo_backup.types.long.Long"]
    """<p>The size, in bytes, of a backup.</p>"""
    calculated_lifecycle: NotRequired[
        "capo_backup.types.calculated_lifecycle.CalculatedLifecycle"
    ]
    """<p>A <code>CalculatedLifecycle</code> object containing <code>DeleteAt</code> and <code>MoveToColdStorageAt</code> timestamps.</p>"""
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    """<p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.</p> <p>Backups that are transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. </p> <p>Resource types that can transition to cold storage are listed in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p>"""
    encryption_key_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The server-side encryption key used to protect your backups; for example, <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p>"""
    is_encrypted: "capo_backup.types.boolean2.Boolean2"
    """<p>A Boolean value that is returned as <code>TRUE</code> if the specified recovery point is encrypted, or <code>FALSE</code> if the recovery point is not encrypted.</p>"""
    storage_class: NotRequired["capo_backup.types.storage_class.StorageClass"]
    """<p>Specifies the storage class of the recovery point. Valid values are <code>WARM</code> or <code>COLD</code>.</p>"""
    last_restore_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a recovery point was last restored, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastRestoreTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    parent_recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>This is an ARN that uniquely identifies a parent (composite) recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    composite_member_identifier: NotRequired["capo_backup.types.string.string"]
    """<p>The identifier of a resource within a composite group, such as nested (child) recovery point belonging to a composite (parent) stack. The ID is transferred from the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-syntax"> logical ID</a> within a stack.</p>"""
    is_parent: "capo_backup.types.boolean2.Boolean2"
    """<p>This returns the boolean value that a recovery point is a parent (composite) job.</p>"""
    resource_name: NotRequired["capo_backup.types.string.string"]
    """<p>The name of the resource that belongs to the specified backup.</p>"""
    vault_type: NotRequired["capo_backup.types.vault_type.VaultType"]
    """<p>The type of vault in which the described recovery point is stored.</p>"""
    index_status: NotRequired["capo_backup.types.index_status.IndexStatus"]
    """<p>This is the current status for the backup index associated with the specified recovery point.</p> <p>Statuses are: <code>PENDING</code> | <code>ACTIVE</code> | <code>FAILED</code> | <code>DELETING</code> </p> <p>A recovery point with an index that has the status of <code>ACTIVE</code> can be included in a search.</p>"""
    index_status_message: NotRequired["capo_backup.types.string.string"]
    """<p>A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.</p>"""
    encryption_key_type: NotRequired[
        "capo_backup.types.encryption_key_type.EncryptionKeyType"
    ]
    """<p>The type of encryption key used for the recovery point. Valid values are CUSTOMER_MANAGED_KMS_KEY for customer-managed keys or Amazon Web Services_OWNED_KMS_KEY for Amazon Web Services-owned keys.</p>"""
    scan_results: NotRequired["capo_backup.types.scan_results.ScanResults"]
    """<p>Contains the latest scanning results against the recovery point and currently include <code>MalwareScanner</code>, <code>ScanJobState</code>, <code>Findings</code>, and <code>LastScanTimestamp</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryPointOutput) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "source_backup_vault_arn" in value:
        out["SourceBackupVaultArn"] = value["source_backup_vault_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "created_by" in value:
        import capo_backup.types.recovery_point_creator

        out["CreatedBy"] = capo_backup.types.recovery_point_creator.serialize_json(
            value["created_by"]
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "status" in value:
        import capo_backup.types.recovery_point_status

        out["Status"] = capo_backup.types.recovery_point_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "initiation_date" in value:
        import capo_backup.types.timestamp

        out["InitiationDate"] = capo_backup.types.timestamp.serialize_json(
            value["initiation_date"]
        )
    if "completion_date" in value:
        import capo_backup.types.timestamp

        out["CompletionDate"] = capo_backup.types.timestamp.serialize_json(
            value["completion_date"]
        )
    if "backup_size_in_bytes" in value:
        out["BackupSizeInBytes"] = value["backup_size_in_bytes"]
    if "calculated_lifecycle" in value:
        import capo_backup.types.calculated_lifecycle

        out["CalculatedLifecycle"] = (
            capo_backup.types.calculated_lifecycle.serialize_json(
                value["calculated_lifecycle"]
            )
        )
    if "lifecycle" in value:
        import capo_backup.types.lifecycle

        out["Lifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["IsEncrypted"] = value.get("is_encrypted", False)
    if "storage_class" in value:
        import capo_backup.types.storage_class

        out["StorageClass"] = capo_backup.types.storage_class.serialize_json(
            value["storage_class"]
        )
    if "last_restore_time" in value:
        import capo_backup.types.timestamp

        out["LastRestoreTime"] = capo_backup.types.timestamp.serialize_json(
            value["last_restore_time"]
        )
    if "parent_recovery_point_arn" in value:
        out["ParentRecoveryPointArn"] = value["parent_recovery_point_arn"]
    if "composite_member_identifier" in value:
        out["CompositeMemberIdentifier"] = value["composite_member_identifier"]
    out["IsParent"] = value.get("is_parent", False)
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "vault_type" in value:
        import capo_backup.types.vault_type

        out["VaultType"] = capo_backup.types.vault_type.serialize_json(
            value["vault_type"]
        )
    if "index_status" in value:
        import capo_backup.types.index_status

        out["IndexStatus"] = capo_backup.types.index_status.serialize_json(
            value["index_status"]
        )
    if "index_status_message" in value:
        out["IndexStatusMessage"] = value["index_status_message"]
    if "encryption_key_type" in value:
        import capo_backup.types.encryption_key_type

        out["EncryptionKeyType"] = capo_backup.types.encryption_key_type.serialize_json(
            value["encryption_key_type"]
        )
    if "scan_results" in value:
        import capo_backup.types.scan_results

        out["ScanResults"] = capo_backup.types.scan_results.serialize_json(
            value["scan_results"]
        )
    return out


def deserialize_json(data: dict) -> DescribeRecoveryPointOutput:
    out: DescribeRecoveryPointOutput = {}  # type: ignore[typeddict-item]
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("SourceBackupVaultArn") is not None:
        out["source_backup_vault_arn"] = data["SourceBackupVaultArn"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("CreatedBy") is not None:
        import capo_backup.types.recovery_point_creator

        out["created_by"] = capo_backup.types.recovery_point_creator.deserialize_json(
            data["CreatedBy"]
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("Status") is not None:
        import capo_backup.types.recovery_point_status

        out["status"] = capo_backup.types.recovery_point_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreationDate") is not None:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("InitiationDate") is not None:
        import capo_backup.types.timestamp

        out["initiation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["InitiationDate"]
        )
    if data.get("CompletionDate") is not None:
        import capo_backup.types.timestamp

        out["completion_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CompletionDate"]
        )
    if data.get("BackupSizeInBytes") is not None:
        out["backup_size_in_bytes"] = data["BackupSizeInBytes"]
    if data.get("CalculatedLifecycle") is not None:
        import capo_backup.types.calculated_lifecycle

        out["calculated_lifecycle"] = (
            capo_backup.types.calculated_lifecycle.deserialize_json(
                data["CalculatedLifecycle"]
            )
        )
    if data.get("Lifecycle") is not None:
        import capo_backup.types.lifecycle

        out["lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("IsEncrypted") is not None:
        out["is_encrypted"] = data["IsEncrypted"]
    else:
        out["is_encrypted"] = False
    if data.get("StorageClass") is not None:
        import capo_backup.types.storage_class

        out["storage_class"] = capo_backup.types.storage_class.deserialize_json(
            data["StorageClass"]
        )
    if data.get("LastRestoreTime") is not None:
        import capo_backup.types.timestamp

        out["last_restore_time"] = capo_backup.types.timestamp.deserialize_json(
            data["LastRestoreTime"]
        )
    if data.get("ParentRecoveryPointArn") is not None:
        out["parent_recovery_point_arn"] = data["ParentRecoveryPointArn"]
    if data.get("CompositeMemberIdentifier") is not None:
        out["composite_member_identifier"] = data["CompositeMemberIdentifier"]
    if data.get("IsParent") is not None:
        out["is_parent"] = data["IsParent"]
    else:
        out["is_parent"] = False
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("VaultType") is not None:
        import capo_backup.types.vault_type

        out["vault_type"] = capo_backup.types.vault_type.deserialize_json(
            data["VaultType"]
        )
    if data.get("IndexStatus") is not None:
        import capo_backup.types.index_status

        out["index_status"] = capo_backup.types.index_status.deserialize_json(
            data["IndexStatus"]
        )
    if data.get("IndexStatusMessage") is not None:
        out["index_status_message"] = data["IndexStatusMessage"]
    if data.get("EncryptionKeyType") is not None:
        import capo_backup.types.encryption_key_type

        out["encryption_key_type"] = (
            capo_backup.types.encryption_key_type.deserialize_json(
                data["EncryptionKeyType"]
            )
        )
    if data.get("ScanResults") is not None:
        import capo_backup.types.scan_results

        out["scan_results"] = capo_backup.types.scan_results.deserialize_json(
            data["ScanResults"]
        )
    return out
