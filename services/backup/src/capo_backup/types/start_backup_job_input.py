"""Generated from Smithy shape ``com.amazonaws.backup#StartBackupJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_options
    import capo_backup.types.backup_vault_name
    import capo_backup.types.iam_role_arn
    import capo_backup.types.index
    import capo_backup.types.lifecycle
    import capo_backup.types.string
    import capo_backup.types.tags
    import capo_backup.types.window_minutes


class StartBackupJobInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    logically_air_gapped_backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The ARN of a logically air-gapped vault. ARN must be in the same account and Region. If provided, supported fully managed resources back up directly to logically air-gapped vault, while other supported resources create a temporary (billable) snapshot in backup vault, then copy it to logically air-gapped vault. Unsupported resources only back up to the specified backup vault.</p>"""
    resource_arn: "capo_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    iam_role_arn: "capo_backup.types.iam_role_arn.IAMRoleArn"
    """<p>Specifies the IAM role ARN used to create the target recovery point; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>StartBackupJob</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""
    start_window_minutes: NotRequired["capo_backup.types.window_minutes.WindowMinutes"]
    """<p>A value in minutes after a backup is scheduled before a job will be canceled if it doesn't start successfully. This value is optional, and the default is 8 hours. If this value is included, it must be at least 60 minutes to avoid errors.</p> <p>This parameter has a maximum value of 100 years (52,560,000 minutes).</p> <p>During the start window, the backup job status remains in <code>CREATED</code> status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to <code>RUNNING</code>) or until the job status changes to <code>EXPIRED</code> (which is expected to occur when the start window time is over).</p>"""
    complete_window_minutes: NotRequired[
        "capo_backup.types.window_minutes.WindowMinutes"
    ]
    """<p>A value in minutes during which a successfully started backup must complete, or else Backup will cancel the job. This value is optional. This value begins counting down from when the backup was scheduled. It does not add additional time for <code>StartWindowMinutes</code>, or if the backup started later than scheduled.</p> <p>Like <code>StartWindowMinutes</code>, this parameter has a maximum value of 100 years (52,560,000 minutes).</p>"""
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    """<p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup will transition and expire backups automatically according to the lifecycle that you define. </p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. </p> <p>Resource types that can transition to cold storage are listed in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p> <p>This parameter has a maximum value of 100 years (36,500 days).</p>"""
    recovery_point_tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>The tags to assign to the resources.</p>"""
    backup_options: NotRequired["capo_backup.types.backup_options.BackupOptions"]
    """<p>The backup option for a selected resource. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs.</p> <p>Valid values: Set to <code>"WindowsVSS":"enabled"</code> to enable the <code>WindowsVSS</code> backup option and create a Windows VSS backup. Set to <code>"WindowsVSS""disabled"</code> to create a regular backup. The <code>WindowsVSS</code> option is not enabled by default.</p>"""
    index: NotRequired["capo_backup.types.index.Index"]
    """<p>Include this parameter to enable index creation if your backup job has a resource type that supports backup indexes.</p> <p>Resource types that support backup indexes include:</p> <ul> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul> <p>Index can have 1 of 2 possible values, either <code>ENABLED</code> or <code>DISABLED</code>.</p> <p>To create a backup index for an eligible <code>ACTIVE</code> recovery point that does not yet have a backup index, set value to <code>ENABLED</code>.</p> <p>To delete a backup index, set value to <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBackupJobInput) -> dict:
    out: dict = {}
    out["BackupVaultName"] = value["backup_vault_name"]
    if "logically_air_gapped_backup_vault_arn" in value:
        out["LogicallyAirGappedBackupVaultArn"] = value[
            "logically_air_gapped_backup_vault_arn"
        ]
    out["ResourceArn"] = value["resource_arn"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "start_window_minutes" in value:
        out["StartWindowMinutes"] = value["start_window_minutes"]
    if "complete_window_minutes" in value:
        out["CompleteWindowMinutes"] = value["complete_window_minutes"]
    if "lifecycle" in value:
        import capo_backup.types.lifecycle

        out["Lifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    if "recovery_point_tags" in value:
        import capo_backup.types.tags

        out["RecoveryPointTags"] = capo_backup.types.tags.serialize_json(
            value["recovery_point_tags"]
        )
    if "backup_options" in value:
        import capo_backup.types.backup_options

        out["BackupOptions"] = capo_backup.types.backup_options.serialize_json(
            value["backup_options"]
        )
    if "index" in value:
        import capo_backup.types.index

        out["Index"] = capo_backup.types.index.serialize_json(value["index"])
    return out


def deserialize_json(data: dict) -> StartBackupJobInput:
    out: StartBackupJobInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        raise DeserializationError("StartBackupJobInput.backup_vault_name required")
    if data.get("LogicallyAirGappedBackupVaultArn") is not None:
        out["logically_air_gapped_backup_vault_arn"] = data[
            "LogicallyAirGappedBackupVaultArn"
        ]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("StartBackupJobInput.resource_arn required")
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("StartBackupJobInput.iam_role_arn required")
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("StartWindowMinutes") is not None:
        out["start_window_minutes"] = data["StartWindowMinutes"]
    if data.get("CompleteWindowMinutes") is not None:
        out["complete_window_minutes"] = data["CompleteWindowMinutes"]
    if data.get("Lifecycle") is not None:
        import capo_backup.types.lifecycle

        out["lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    if data.get("RecoveryPointTags") is not None:
        import capo_backup.types.tags

        out["recovery_point_tags"] = capo_backup.types.tags.deserialize_json(
            data["RecoveryPointTags"]
        )
    if data.get("BackupOptions") is not None:
        import capo_backup.types.backup_options

        out["backup_options"] = capo_backup.types.backup_options.deserialize_json(
            data["BackupOptions"]
        )
    if data.get("Index") is not None:
        import capo_backup.types.index

        out["index"] = capo_backup.types.index.deserialize_json(data["Index"])
    return out
