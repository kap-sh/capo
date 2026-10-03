"""Generated from Smithy shape ``com.amazonaws.backup#CopyJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.account_id
    import capo_backup.types.arn
    import capo_backup.types.boolean2
    import capo_backup.types.copy_job_child_jobs_in_state
    import capo_backup.types.copy_job_state
    import capo_backup.types.iam_role_arn
    import capo_backup.types.lifecycle
    import capo_backup.types.long
    import capo_backup.types.recovery_point_creator
    import capo_backup.types.resource_type
    import capo_backup.types.string
    import capo_backup.types.timestamp


class CopyJob(TypedDict, closed=True):
    account_id: NotRequired["capo_backup.types.account_id.AccountId"]
    """<p>The account ID that owns the copy job.</p>"""
    copy_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a copy job.</p>"""
    source_backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a source copy vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>. </p>"""
    source_recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a source recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    destination_backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a destination copy vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    destination_vault_type: NotRequired["capo_backup.types.string.string"]
    """<p>The type of destination backup vault where the copied recovery point is stored. Valid values are <code>BACKUP_VAULT</code> for standard backup vaults and <code>LOGICALLY_AIR_GAPPED_BACKUP_VAULT</code> for logically air-gapped vaults.</p>"""
    destination_vault_lock_state: NotRequired["capo_backup.types.string.string"]
    """<p>The lock state of the destination backup vault. For logically air-gapped vaults, this indicates whether the vault is locked in compliance mode. Valid values include <code>LOCKED</code> and <code>UNLOCKED</code>.</p>"""
    destination_recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a destination recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    destination_encryption_key_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the copied backup in the destination vault. This can be a customer-managed key or an Amazon Web Services managed key.</p>"""
    destination_recovery_point_lifecycle: NotRequired[
        "capo_backup.types.lifecycle.Lifecycle"
    ]
    resource_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The Amazon Web Services resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a copy job is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    completion_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a copy job is completed, in Unix format and Coordinated Universal Time (UTC). The value of <code>CompletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    state: NotRequired["capo_backup.types.copy_job_state.CopyJobState"]
    """<p>The current state of a copy job.</p>"""
    status_message: NotRequired["capo_backup.types.string.string"]
    """<p>A detailed message explaining the status of the job to copy a resource.</p>"""
    backup_size_in_bytes: NotRequired["capo_backup.types.long.Long"]
    """<p>The size, in bytes, of a copy job.</p>"""
    iam_role_arn: NotRequired["capo_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>Specifies the IAM role ARN used to copy the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    created_by: NotRequired[
        "capo_backup.types.recovery_point_creator.RecoveryPointCreator"
    ]
    created_by_backup_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>The backup job ID that initiated this copy job. Only applicable to scheduled copy jobs and automatic copy jobs to logically air-gapped vault.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource to be copied; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.</p>"""
    parent_job_id: NotRequired["capo_backup.types.string.string"]
    """<p>This uniquely identifies a request to Backup to copy a resource. The return will be the parent (composite) job ID.</p>"""
    is_parent: "capo_backup.types.boolean2.Boolean2"
    """<p>This is a boolean value indicating this is a parent (composite) copy job.</p>"""
    composite_member_identifier: NotRequired["capo_backup.types.string.string"]
    """<p>The identifier of a resource within a composite group, such as nested (child) recovery point belonging to a composite (parent) stack. The ID is transferred from the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html#resources-section-structure-syntax"> logical ID</a> within a stack.</p>"""
    number_of_child_jobs: NotRequired["capo_backup.types.long.Long"]
    """<p>The number of child (nested) copy jobs.</p>"""
    child_jobs_in_state: NotRequired[
        "capo_backup.types.copy_job_child_jobs_in_state.CopyJobChildJobsInState"
    ]
    """<p>This returns the statistics of the included child (nested) copy jobs.</p>"""
    resource_name: NotRequired["capo_backup.types.string.string"]
    """<p>The non-unique name of the resource that belongs to the specified backup.</p>"""
    message_category: NotRequired["capo_backup.types.string.string"]
    """<p>This parameter is the job count for the specified message category.</p> <p>Example strings may include <code>AccessDenied</code>, <code>SUCCESS</code>, <code>AGGREGATE_ALL</code>, and <code>InvalidParameters</code>. See <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html">Monitoring</a> for a list of MessageCategory strings.</p> <p>The the value ANY returns count of all message categories.</p> <p> <code>AGGREGATE_ALL</code> aggregates job counts for all message categories and returns the sum</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyJob) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "copy_job_id" in value:
        out["CopyJobId"] = value["copy_job_id"]
    if "source_backup_vault_arn" in value:
        out["SourceBackupVaultArn"] = value["source_backup_vault_arn"]
    if "source_recovery_point_arn" in value:
        out["SourceRecoveryPointArn"] = value["source_recovery_point_arn"]
    if "destination_backup_vault_arn" in value:
        out["DestinationBackupVaultArn"] = value["destination_backup_vault_arn"]
    if "destination_vault_type" in value:
        out["DestinationVaultType"] = value["destination_vault_type"]
    if "destination_vault_lock_state" in value:
        out["DestinationVaultLockState"] = value["destination_vault_lock_state"]
    if "destination_recovery_point_arn" in value:
        out["DestinationRecoveryPointArn"] = value["destination_recovery_point_arn"]
    if "destination_encryption_key_arn" in value:
        out["DestinationEncryptionKeyArn"] = value["destination_encryption_key_arn"]
    if "destination_recovery_point_lifecycle" in value:
        import capo_backup.types.lifecycle

        out["DestinationRecoveryPointLifecycle"] = (
            capo_backup.types.lifecycle.serialize_json(
                value["destination_recovery_point_lifecycle"]
            )
        )
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
        import capo_backup.types.copy_job_state

        out["State"] = capo_backup.types.copy_job_state.serialize_json(value["state"])
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "backup_size_in_bytes" in value:
        out["BackupSizeInBytes"] = value["backup_size_in_bytes"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "created_by" in value:
        import capo_backup.types.recovery_point_creator

        out["CreatedBy"] = capo_backup.types.recovery_point_creator.serialize_json(
            value["created_by"]
        )
    if "created_by_backup_job_id" in value:
        out["CreatedByBackupJobId"] = value["created_by_backup_job_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "parent_job_id" in value:
        out["ParentJobId"] = value["parent_job_id"]
    out["IsParent"] = value.get("is_parent", False)
    if "composite_member_identifier" in value:
        out["CompositeMemberIdentifier"] = value["composite_member_identifier"]
    if "number_of_child_jobs" in value:
        out["NumberOfChildJobs"] = value["number_of_child_jobs"]
    if "child_jobs_in_state" in value:
        import capo_backup.types.copy_job_child_jobs_in_state

        out["ChildJobsInState"] = (
            capo_backup.types.copy_job_child_jobs_in_state.serialize_json(
                value["child_jobs_in_state"]
            )
        )
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "message_category" in value:
        out["MessageCategory"] = value["message_category"]
    return out


def deserialize_json(data: dict) -> CopyJob:
    out: CopyJob = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("CopyJobId") is not None:
        out["copy_job_id"] = data["CopyJobId"]
    if data.get("SourceBackupVaultArn") is not None:
        out["source_backup_vault_arn"] = data["SourceBackupVaultArn"]
    if data.get("SourceRecoveryPointArn") is not None:
        out["source_recovery_point_arn"] = data["SourceRecoveryPointArn"]
    if data.get("DestinationBackupVaultArn") is not None:
        out["destination_backup_vault_arn"] = data["DestinationBackupVaultArn"]
    if data.get("DestinationVaultType") is not None:
        out["destination_vault_type"] = data["DestinationVaultType"]
    if data.get("DestinationVaultLockState") is not None:
        out["destination_vault_lock_state"] = data["DestinationVaultLockState"]
    if data.get("DestinationRecoveryPointArn") is not None:
        out["destination_recovery_point_arn"] = data["DestinationRecoveryPointArn"]
    if data.get("DestinationEncryptionKeyArn") is not None:
        out["destination_encryption_key_arn"] = data["DestinationEncryptionKeyArn"]
    if data.get("DestinationRecoveryPointLifecycle") is not None:
        import capo_backup.types.lifecycle

        out["destination_recovery_point_lifecycle"] = (
            capo_backup.types.lifecycle.deserialize_json(
                data["DestinationRecoveryPointLifecycle"]
            )
        )
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
        import capo_backup.types.copy_job_state

        out["state"] = capo_backup.types.copy_job_state.deserialize_json(data["State"])
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("BackupSizeInBytes") is not None:
        out["backup_size_in_bytes"] = data["BackupSizeInBytes"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("CreatedBy") is not None:
        import capo_backup.types.recovery_point_creator

        out["created_by"] = capo_backup.types.recovery_point_creator.deserialize_json(
            data["CreatedBy"]
        )
    if data.get("CreatedByBackupJobId") is not None:
        out["created_by_backup_job_id"] = data["CreatedByBackupJobId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ParentJobId") is not None:
        out["parent_job_id"] = data["ParentJobId"]
    if data.get("IsParent") is not None:
        out["is_parent"] = data["IsParent"]
    else:
        out["is_parent"] = False
    if data.get("CompositeMemberIdentifier") is not None:
        out["composite_member_identifier"] = data["CompositeMemberIdentifier"]
    if data.get("NumberOfChildJobs") is not None:
        out["number_of_child_jobs"] = data["NumberOfChildJobs"]
    if data.get("ChildJobsInState") is not None:
        import capo_backup.types.copy_job_child_jobs_in_state

        out["child_jobs_in_state"] = (
            capo_backup.types.copy_job_child_jobs_in_state.deserialize_json(
                data["ChildJobsInState"]
            )
        )
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    if data.get("MessageCategory") is not None:
        out["message_category"] = data["MessageCategory"]
    return out
