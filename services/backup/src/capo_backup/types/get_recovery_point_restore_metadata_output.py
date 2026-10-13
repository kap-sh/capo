"""Generated from Smithy shape ``com.amazonaws.backup#GetRecoveryPointRestoreMetadataOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.metadata
    import capo_backup.types.resource_type


class GetRecoveryPointRestoreMetadataOutput(TypedDict, closed=True):
    backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    recovery_point_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    restore_metadata: NotRequired["capo_backup.types.metadata.Metadata"]
    """<p>The set of metadata key-value pairs that describe the original configuration of the backed-up resource. These values vary depending on the service that is being restored.</p>"""
    resource_type: NotRequired["capo_backup.types.resource_type.ResourceType"]
    """<p>The resource type of the recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPointRestoreMetadataOutput) -> dict:
    out: dict = {}
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "recovery_point_arn" in value:
        out["RecoveryPointArn"] = value["recovery_point_arn"]
    if "restore_metadata" in value:
        import capo_backup.types.metadata

        out["RestoreMetadata"] = capo_backup.types.metadata.serialize_json(
            value["restore_metadata"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> GetRecoveryPointRestoreMetadataOutput:
    out: GetRecoveryPointRestoreMetadataOutput = {}  # type: ignore[typeddict-item]
    if data.get("BackupVaultArn") is not None:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if data.get("RecoveryPointArn") is not None:
        out["recovery_point_arn"] = data["RecoveryPointArn"]
    if data.get("RestoreMetadata") is not None:
        import capo_backup.types.metadata

        out["restore_metadata"] = capo_backup.types.metadata.deserialize_json(
            data["RestoreMetadata"]
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


def redact_sensitive(value: GetRecoveryPointRestoreMetadataOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "restore_metadata" in value:
        out["restore_metadata"] = "*** Sensitive Data Redacted ***"
    return out
