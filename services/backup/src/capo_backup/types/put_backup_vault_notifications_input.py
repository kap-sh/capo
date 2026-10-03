"""Generated from Smithy shape ``com.amazonaws.backup#PutBackupVaultNotificationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_events
    import capo_backup.types.backup_vault_name


class PutBackupVaultNotificationsInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    sns_topic_arn: "capo_backup.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for example, <code>arn:aws:sns:us-west-2:111122223333:MyVaultTopic</code>.</p>"""
    backup_vault_events: "capo_backup.types.backup_vault_events.BackupVaultEvents"
    """<p>An array of events that indicate the status of jobs to back up resources to the backup vault. For the list of supported events, common use cases, and code samples, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html">Notification options with Backup</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBackupVaultNotificationsInput) -> dict:
    out: dict = {}
    out["SNSTopicArn"] = value["sns_topic_arn"]
    import capo_backup.types.backup_vault_events

    out["BackupVaultEvents"] = capo_backup.types.backup_vault_events.serialize_json(
        value["backup_vault_events"]
    )
    return out


def deserialize_json(data: dict) -> PutBackupVaultNotificationsInput:
    out: PutBackupVaultNotificationsInput = {}  # type: ignore[typeddict-item]
    if data.get("SNSTopicArn") is not None:
        out["sns_topic_arn"] = data["SNSTopicArn"]
    else:
        raise DeserializationError(
            "PutBackupVaultNotificationsInput.sns_topic_arn required"
        )
    if data.get("BackupVaultEvents") is not None:
        import capo_backup.types.backup_vault_events

        out["backup_vault_events"] = (
            capo_backup.types.backup_vault_events.deserialize_json(
                data["BackupVaultEvents"]
            )
        )
    else:
        raise DeserializationError(
            "PutBackupVaultNotificationsInput.backup_vault_events required"
        )
    return out
