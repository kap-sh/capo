"""Generated from Smithy shape ``com.amazonaws.backup#StartCopyJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.iam_role_arn
    import capo_backup.types.lifecycle
    import capo_backup.types.string


class StartCopyJobInput(TypedDict, closed=True):
    recovery_point_arn: "capo_backup.types.arn.ARN"
    """<p>An ARN that uniquely identifies a recovery point to use for the copy job; for example, arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45. </p>"""
    source_backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical source container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    destination_backup_vault_arn: "capo_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a destination backup vault to copy to; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    iam_role_arn: "capo_backup.types.iam_role_arn.IAMRoleArn"
    """<p>Specifies the IAM role ARN used to copy the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartCopyJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]


# --- restJson1 ser/de ---
def serialize_json(value: StartCopyJobInput) -> dict:
    out: dict = {}
    out["RecoveryPointArn"] = value["recovery_point_arn"]
    out["SourceBackupVaultName"] = value["source_backup_vault_name"]
    out["DestinationBackupVaultArn"] = value["destination_backup_vault_arn"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "lifecycle" in value:
        import capo_backup.types.lifecycle

        out["Lifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    return out


def deserialize_json(data: dict) -> StartCopyJobInput:
    out: StartCopyJobInput = {}  # type: ignore[typeddict-item]
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    else:
        out["recovery_point_arn"] = ""
    if data.get("SourceBackupVaultName") is not None:
        out["source_backup_vault_name"] = data["SourceBackupVaultName"]
    else:
        out["source_backup_vault_name"] = ""
    if data.get("DestinationBackupVaultArn") is not None:
        out["destination_backup_vault_arn"] = data["DestinationBackupVaultArn"]
    else:
        out["destination_backup_vault_arn"] = ""
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("Lifecycle") is not None:
        import capo_backup.types.lifecycle

        out["lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    return out
