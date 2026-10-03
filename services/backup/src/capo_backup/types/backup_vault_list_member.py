"""Generated from Smithy shape ``com.amazonaws.backup#BackupVaultListMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.boolean
    import capo_backup.types.encryption_key_type
    import capo_backup.types.long
    import capo_backup.types.long2
    import capo_backup.types.string
    import capo_backup.types.timestamp
    import capo_backup.types.vault_state
    import capo_backup.types.vault_type


class BackupVaultListMember(TypedDict, closed=True):
    backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    vault_type: NotRequired["capo_backup.types.vault_type.VaultType"]
    """<p>The type of vault in which the described recovery point is stored.</p>"""
    vault_state: NotRequired["capo_backup.types.vault_state.VaultState"]
    """<p>The current state of the vault.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a resource backup is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    encryption_key_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>A server-side encryption key you can specify to encrypt your backups from services that support full Backup management; for example, <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, Backup creates a KMS key for you by default.</p> <p>To learn which Backup services support full Backup management and how Backup handles encryption for backups from services that do not yet support full Backup, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html"> Encryption for backups in Backup</a> </p>"""
    creator_request_id: NotRequired["capo_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    number_of_recovery_points: "capo_backup.types.long2.Long2"
    """<p>The number of recovery points that are stored in a backup vault. Recovery point count value displayed in the console can be an approximation.</p>"""
    locked: NotRequired["capo_backup.types.boolean.Boolean"]
    """<p>A Boolean value that indicates whether Backup Vault Lock applies to the selected backup vault. If <code>true</code>, Vault Lock prevents delete and update operations on the recovery points in the selected vault.</p>"""
    min_retention_days: NotRequired["capo_backup.types.long.Long"]
    """<p>The Backup Vault Lock setting that specifies the minimum retention period that the vault retains its recovery points. If this parameter is not specified, Vault Lock does not enforce a minimum retention period.</p> <p>If specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already stored in the vault prior to Vault Lock are not affected.</p>"""
    max_retention_days: NotRequired["capo_backup.types.long.Long"]
    """<p>The Backup Vault Lock setting that specifies the maximum retention period that the vault retains its recovery points. If this parameter is not specified, Vault Lock does not enforce a maximum retention period on the recovery points in the vault (allowing indefinite storage).</p> <p>If specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already stored in the vault prior to Vault Lock are not affected.</p>"""
    lock_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time when Backup Vault Lock configuration becomes immutable, meaning it cannot be changed or deleted.</p> <p>If you applied Vault Lock to your vault without specifying a lock date, you can change your Vault Lock settings, or delete Vault Lock from the vault entirely, at any time.</p> <p>This value is in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    encryption_key_type: NotRequired[
        "capo_backup.types.encryption_key_type.EncryptionKeyType"
    ]
    """<p>The type of encryption key used for the backup vault. Valid values are CUSTOMER_MANAGED_KMS_KEY for customer-managed keys or Amazon Web Services_OWNED_KMS_KEY for Amazon Web Services-owned keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupVaultListMember) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "vault_type" in value:
        import capo_backup.types.vault_type

        out["VaultType"] = capo_backup.types.vault_type.serialize_json(
            value["vault_type"]
        )
    if "vault_state" in value:
        import capo_backup.types.vault_state

        out["VaultState"] = capo_backup.types.vault_state.serialize_json(
            value["vault_state"]
        )
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    out["NumberOfRecoveryPoints"] = value.get("number_of_recovery_points", 0)
    if "locked" in value:
        out["Locked"] = value["locked"]
    if "min_retention_days" in value:
        out["MinRetentionDays"] = value["min_retention_days"]
    if "max_retention_days" in value:
        out["MaxRetentionDays"] = value["max_retention_days"]
    if "lock_date" in value:
        import capo_backup.types.timestamp

        out["LockDate"] = capo_backup.types.timestamp.serialize_json(value["lock_date"])
    if "encryption_key_type" in value:
        import capo_backup.types.encryption_key_type

        out["EncryptionKeyType"] = capo_backup.types.encryption_key_type.serialize_json(
            value["encryption_key_type"]
        )
    return out


def deserialize_json(data: dict) -> BackupVaultListMember:
    out: BackupVaultListMember = {}  # type: ignore[typeddict-item]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("VaultType") is not None:
        import capo_backup.types.vault_type

        out["vault_type"] = capo_backup.types.vault_type.deserialize_json(
            data["VaultType"]
        )
    if data.get("VaultState") is not None:
        import capo_backup.types.vault_state

        out["vault_state"] = capo_backup.types.vault_state.deserialize_json(
            data["VaultState"]
        )
    if data.get("CreationDate") is not None:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("NumberOfRecoveryPoints") is not None:
        out["number_of_recovery_points"] = data["NumberOfRecoveryPoints"]
    else:
        out["number_of_recovery_points"] = 0
    if data.get("Locked") is not None:
        out["locked"] = data["Locked"]
    if data.get("MinRetentionDays") is not None:
        out["min_retention_days"] = data["MinRetentionDays"]
    if data.get("MaxRetentionDays") is not None:
        out["max_retention_days"] = data["MaxRetentionDays"]
    if data.get("LockDate") is not None:
        import capo_backup.types.timestamp

        out["lock_date"] = capo_backup.types.timestamp.deserialize_json(
            data["LockDate"]
        )
    if data.get("EncryptionKeyType") is not None:
        import capo_backup.types.encryption_key_type

        out["encryption_key_type"] = (
            capo_backup.types.encryption_key_type.deserialize_json(
                data["EncryptionKeyType"]
            )
        )
    return out
