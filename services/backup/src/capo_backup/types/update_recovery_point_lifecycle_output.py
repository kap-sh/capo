"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRecoveryPointLifecycleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.calculated_lifecycle
    import capo_backup.types.lifecycle


class UpdateRecoveryPointLifecycleOutput(TypedDict, closed=True):
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    """<p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold.</p> <p>Resource types that can transition to cold storage are listed in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p>"""
    calculated_lifecycle: NotRequired[
        "capo_backup.types.calculated_lifecycle.CalculatedLifecycle"
    ]
    """<p>A <code>CalculatedLifecycle</code> object containing <code>DeleteAt</code> and <code>MoveToColdStorageAt</code> timestamps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPointLifecycleOutput) -> dict:
    out: dict = {}
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "lifecycle" in value:
        import capo_backup.types.lifecycle

        out["Lifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    if "calculated_lifecycle" in value:
        import capo_backup.types.calculated_lifecycle

        out["CalculatedLifecycle"] = (
            capo_backup.types.calculated_lifecycle.serialize_json(
                value["calculated_lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPointLifecycleOutput:
    out: UpdateRecoveryPointLifecycleOutput = {}  # type: ignore[typeddict-item]
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if data.get("Lifecycle") is not None:
        import capo_backup.types.lifecycle

        out["lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    if data.get("CalculatedLifecycle") is not None:
        import capo_backup.types.calculated_lifecycle

        out["calculated_lifecycle"] = (
            capo_backup.types.calculated_lifecycle.deserialize_json(
                data["CalculatedLifecycle"]
            )
        )
    return out
