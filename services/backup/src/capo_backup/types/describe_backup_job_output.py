"""Generated from Smithy shape ``com.amazonaws.backup#DescribeBackupJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.arn
    import capo_backup.types.backup_job_child_jobs_in_state
    import capo_backup.types.backup_job_state
    import capo_backup.types.backup_options
    import capo_backup.types.backup_vault_name
    import capo_backup.types.boolean2
    import capo_backup.types.iam_role_arn
    import capo_backup.types.lifecycle
    import capo_backup.types.long
    import capo_backup.types.recovery_point_creator
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class DescribeBackupJobOutput(TypedDict, closed=True):
    account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>Returns the account ID that owns the backup job.</p>"""
    backup_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a request to Backup to back up a resource.</p>"""
    backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    recovery_point_lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    vault_type: NotRequired["capo_backup.types.string.string"]
    """<p>The type of backup vault where the recovery point is stored. Valid values are <code>BACKUP_VAULT</code> for standard backup vaults and <code>LOGICALLY_AIR_GAPPED_BACKUP_VAULT</code> for logically air-gapped vaults.</p>"""
    vault_lock_state: NotRequired["capo_backup.types.string.string"]
    """<p>The lock state of the backup vault. For logically air-gapped vaults, this indicates whether the vault is locked in compliance mode. Valid values include <code>LOCKED</code> and <code>UNLOCKED</code>.</p>"""
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    encryption_key_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the backup. This can be a customer-managed key or an Amazon Web Services managed key, depending on the vault configuration.</p>"""
    is_encrypted: "capo_backup.types.boolean2.Boolean2"
    """<p>A boolean value indicating whether the backup is encrypted. All backups in Backup are encrypted, but this field indicates the encryption status for transparency.</p>"""
    resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a saved resource. The format of the ARN depends on the resource type.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    completion_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a job to create a backup job is completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    state: NotRequired["capo_backup.types.backup_job_state.BackupJobState"]
    """<p>The current state of a backup job.</p>"""
    status_message: NotRequired["capo_backup.types.string.string"]
    """<p>A detailed message explaining the status of the job to back up a resource.</p>"""
    percent_done: NotRequired["capo_backup.types.string.string"]
    """<p>Contains an estimated percentage that is complete of a job at the time the job status was queried.</p>"""
    backup_size_in_bytes: NotRequired["capo_backup.types.long.Long"]
    """<p>The size, in bytes, of a backup (recovery point).</p> <p>This value can render differently depending on the resource type as Backup pulls in data information from other Amazon Web Services services. For example, the value returned may show a value of <code>0</code>, which may differ from the anticipated value.</p> <p>The expected behavior for values by resource type are described as follows:</p> <ul> <li> <p>Amazon Aurora, Amazon DocumentDB, and Amazon Neptune do not have this value populate from the operation <code>GetBackupJobStatus</code>.</p> </li> <li> <p>For Amazon DynamoDB with advanced features, this value refers to the size of the recovery point (backup).</p> </li> <li> <p>Amazon EC2 and Amazon EBS show volume size (provisioned storage) returned as part of this value. Amazon EBS does not return backup size information; snapshot size will have the same value as the original resource that was backed up.</p> </li> <li> <p>For Amazon EFS, this value refers to the delta bytes transferred during a backup.</p> </li> <li> <p>For Amazon EKS, this value refers to the size of your nested EKS recovery point.</p> </li> <li> <p>Amazon FSx does not populate this value from the operation <code>GetBackupJobStatus</code> for FSx file systems.</p> </li> <li> <p>An Amazon RDS instance will show as <code>0</code>.</p> </li> <li> <p>For virtual machines running VMware, this value is passed to Backup through an asynchronous workflow, which can mean this displayed value can under-represent the actual backup size.</p> </li> </ul>"""
    iam_role_arn: NotRequired["capo_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    created_by: NotRequired[
        "capo_backup.types.recovery_point_creator.RecoveryPointCreator"
    ]
    """<p>Contains identifying information about the creation of a backup job, including the <code>BackupPlanArn</code>, <code>BackupPlanId</code>, <code>BackupPlanVersion</code>, and <code>BackupRuleId</code> of the backup plan that is used to create it.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>"""
    bytes_transferred: NotRequired["capo_backup.types.long.Long"]
    """<p>The size in bytes transferred to a backup vault at the time that the job status was queried.</p>"""
    expected_completion_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a job to back up resources is expected to be completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>ExpectedCompletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    start_by: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>Specifies the time in Unix format and Coordinated Universal Time (UTC) when a backup job must be started before it is canceled. The value is calculated by adding the start window to the scheduled time. So if the scheduled time were 6:00 PM and the start window is 2 hours, the <code>StartBy</code> time would be 8:00 PM on the date specified. The value of <code>StartBy</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    backup_options: NotRequired["capo_backup.types.backup_options.BackupOptions"]
    """<p>Represents the options specified as part of backup plan or on-demand backup job.</p>"""
    backup_type: NotRequired["capo_backup.types.string.string"]
    """<p>Represents the actual backup type selected for a backup job. For example, if a successful Windows Volume Shadow Copy Service (VSS) backup was taken, <code>BackupType</code> returns <code>"WindowsVSS"</code>. If <code>BackupType</code> is empty, then the backup type was a regular backup.</p>"""
    parent_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>This returns the parent (composite) resource backup job ID.</p>"""
    is_parent: "capo_backup.types.boolean2.Boolean2"
    """<p>This returns the boolean value that a backup job is a parent (composite) job.</p>"""
    number_of_child_jobs: NotRequired["capo_backup.types.long.Long"]
    """<p>This returns the number of child (nested) backup jobs.</p>"""
    child_jobs_in_state: NotRequired[
        "capo_backup.types.backup_job_child_jobs_in_state.BackupJobChildJobsInState"
    ]
    """<p>This returns the statistics of the included child (nested) backup jobs.</p>"""
    resource_name: NotRequired["capo_backup.types.string.string"]
    """<p>The non-unique name of the resource that belongs to the specified backup.</p>"""
    initiation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date a backup job was initiated.</p>"""
    message_category: NotRequired["capo_backup.types.string.string"]
    """<p>The job count for the specified message category.</p> <p>Example strings may include <code>AccessDenied</code>, <code>SUCCESS</code>, <code>AGGREGATE_ALL</code>, and <code>INVALIDPARAMETERS</code>. View <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of accepted MessageCategory strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBackupJobOutput) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "backup_job_id" in value:
        out["BackupJobId"] = value["backup_job_id"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "recovery_point_lifecycle" in value:
        import capo_backup.types.lifecycle

        out["RecoveryPointLifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["recovery_point_lifecycle"]
        )
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "vault_type" in value:
        out["VaultType"] = value["vault_type"]
    if "vault_lock_state" in value:
        out["VaultLockState"] = value["vault_lock_state"]
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["IsEncrypted"] = value.get("is_encrypted", False)
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "completion_date" in value:
        import capo_backup.types.timestamp

        out["CompletionDate"] = capo_backup.types.timestamp.serialize_json(
            value["completion_date"]
        )
    if "state" in value:
        import capo_backup.types.backup_job_state

        out["State"] = capo_backup.types.backup_job_state.serialize_json(value["state"])
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "percent_done" in value:
        out["PercentDone"] = value["percent_done"]
    if "backup_size_in_bytes" in value:
        out["BackupSizeInBytes"] = value["backup_size_in_bytes"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "created_by" in value:
        import capo_backup.types.recovery_point_creator

        out["CreatedBy"] = capo_backup.types.recovery_point_creator.serialize_json(
            value["created_by"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "bytes_transferred" in value:
        out["BytesTransferred"] = value["bytes_transferred"]
    if "expected_completion_date" in value:
        import capo_backup.types.timestamp

        out["ExpectedCompletionDate"] = capo_backup.types.timestamp.serialize_json(
            value["expected_completion_date"]
        )
    if "start_by" in value:
        import capo_backup.types.timestamp

        out["StartBy"] = capo_backup.types.timestamp.serialize_json(value["start_by"])
    if "backup_options" in value:
        import capo_backup.types.backup_options

        out["BackupOptions"] = capo_backup.types.backup_options.serialize_json(
            value["backup_options"]
        )
    if "backup_type" in value:
        out["BackupType"] = value["backup_type"]
    if "parent_job_id" in value:
        out["ParentJobId"] = value["parent_job_id"]
    out["IsParent"] = value.get("is_parent", False)
    if "number_of_child_jobs" in value:
        out["NumberOfChildJobs"] = value["number_of_child_jobs"]
    if "child_jobs_in_state" in value:
        import capo_backup.types.backup_job_child_jobs_in_state

        out["ChildJobsInState"] = (
            capo_backup.types.backup_job_child_jobs_in_state.serialize_json(
                value["child_jobs_in_state"]
            )
        )
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "initiation_date" in value:
        import capo_backup.types.timestamp

        out["InitiationDate"] = capo_backup.types.timestamp.serialize_json(
            value["initiation_date"]
        )
    if "message_category" in value:
        out["MessageCategory"] = value["message_category"]
    return out


def deserialize_json(data: dict) -> DescribeBackupJobOutput:
    out: DescribeBackupJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("BackupJobId") is not None:
        out["backup_job_id"] = data["BackupJobId"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("RecoveryPointLifecycle") is not None:
        import capo_backup.types.lifecycle

        out["recovery_point_lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["RecoveryPointLifecycle"]
        )
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("VaultType") is not None:
        out["vault_type"] = data["VaultType"]
    if data.get("VaultLockState") is not None:
        out["vault_lock_state"] = data["VaultLockState"]
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("IsEncrypted") is not None:
        out["is_encrypted"] = data["IsEncrypted"]
    else:
        out["is_encrypted"] = False
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("CreationDate") is not None:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("CompletionDate") is not None:
        import capo_backup.types.timestamp

        out["completion_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CompletionDate"]
        )
    if data.get("State") is not None:
        import capo_backup.types.backup_job_state

        out["state"] = capo_backup.types.backup_job_state.deserialize_json(
            data["State"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("PercentDone") is not None:
        out["percent_done"] = data["PercentDone"]
    if data.get("BackupSizeInBytes") is not None:
        out["backup_size_in_bytes"] = data["BackupSizeInBytes"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("CreatedBy") is not None:
        import capo_backup.types.recovery_point_creator

        out["created_by"] = capo_backup.types.recovery_point_creator.deserialize_json(
            data["CreatedBy"]
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("BytesTransferred") is not None:
        out["bytes_transferred"] = data["BytesTransferred"]
    if data.get("ExpectedCompletionDate") is not None:
        import capo_backup.types.timestamp

        out["expected_completion_date"] = capo_backup.types.timestamp.deserialize_json(
            data["ExpectedCompletionDate"]
        )
    if data.get("StartBy") is not None:
        import capo_backup.types.timestamp

        out["start_by"] = capo_backup.types.timestamp.deserialize_json(data["StartBy"])
    if data.get("BackupOptions") is not None:
        import capo_backup.types.backup_options

        out["backup_options"] = capo_backup.types.backup_options.deserialize_json(
            data["BackupOptions"]
        )
    if data.get("BackupType") is not None:
        out["backup_type"] = data["BackupType"]
    if data.get("ParentJobId") is not None:
        out["parent_job_id"] = data["ParentJobId"]
    if data.get("IsParent") is not None:
        out["is_parent"] = data["IsParent"]
    else:
        out["is_parent"] = False
    if data.get("NumberOfChildJobs") is not None:
        out["number_of_child_jobs"] = data["NumberOfChildJobs"]
    if data.get("ChildJobsInState") is not None:
        import capo_backup.types.backup_job_child_jobs_in_state

        out["child_jobs_in_state"] = (
            capo_backup.types.backup_job_child_jobs_in_state.deserialize_json(
                data["ChildJobsInState"]
            )
        )
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("InitiationDate") is not None:
        import capo_backup.types.timestamp

        out["initiation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["InitiationDate"]
        )
    if data.get("MessageCategory") is not None:
        out["message_category"] = data["MessageCategory"]
    return out
