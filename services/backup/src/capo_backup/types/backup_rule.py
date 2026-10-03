"""Generated from Smithy shape ``com.amazonaws.backup#BackupRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_rule_name
    import capo_backup.types.backup_vault_name
    import capo_backup.types.boolean
    import capo_backup.types.copy_actions
    import capo_backup.types.cron_expression
    import capo_backup.types.index_actions
    import capo_backup.types.lifecycle
    import capo_backup.types.scan_actions
    import capo_backup.types.string
    import capo_backup.types.tags
    import capo_backup.types.timezone
    import capo_backup.types.window_minutes


class BackupRule(TypedDict, closed=True):
    rule_name: "capo_backup.types.backup_rule_name.BackupRuleName"
    """<p>A display name for a backup rule. Must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    target_backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    target_logically_air_gapped_backup_vault_arn: NotRequired[
        "capo_backup.types.arn.ARN"
    ]
    """<p>The ARN of a logically air-gapped vault. ARN must be in the same account and Region. If provided, supported fully managed resources back up directly to logically air-gapped vault, while other supported resources create a temporary (billable) snapshot in backup vault, then copy it to logically air-gapped vault. Unsupported resources only back up to the specified backup vault.</p>"""
    schedule_expression: NotRequired["capo_backup.types.cron_expression.CronExpression"]
    """<p>A cron expression in UTC specifying when Backup initiates a backup job. When no CRON expression is provided, Backup will use the default expression <code>cron(0 5 ? * * *)</code>.</p> <p>For more information about Amazon Web Services cron expressions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html">Schedule Expressions for Rules</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> <p>Two examples of Amazon Web Services cron expressions are <code> 15 * ? * * *</code> (take a backup every hour at 15 minutes past the hour) and <code>0 12 * * ? *</code> (take a backup every day at 12 noon UTC).</p> <p>For a table of examples, click the preceding link and scroll down the page.</p>"""
    start_window_minutes: NotRequired["capo_backup.types.window_minutes.WindowMinutes"]
    """<p>A value in minutes after a backup is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, it must be at least 60 minutes to avoid errors.</p> <p>During the start window, the backup job status remains in <code>CREATED</code> status until it has successfully begun or until the start window time has run out. If within the start window time Backup receives an error that allows the job to be retried, Backup will automatically retry to begin the job at least every 10 minutes until the backup successfully begins (the job status changes to <code>RUNNING</code>) or until the job status changes to <code>EXPIRED</code> (which is expected to occur when the start window time is over).</p>"""
    completion_window_minutes: NotRequired[
        "capo_backup.types.window_minutes.WindowMinutes"
    ]
    """<p>A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by Backup. This value is optional.</p>"""
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    """<p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define. </p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. </p> <p>Resource types that can transition to cold storage are listed in the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table. Backup ignores this expression for other resource types.</p>"""
    recovery_point_tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>The tags that are assigned to resources that are associated with this rule when restored from backup.</p>"""
    rule_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a rule that is used to schedule the backup of a selection of resources.</p>"""
    copy_actions: NotRequired["capo_backup.types.copy_actions.CopyActions"]
    """<p>An array of <code>CopyAction</code> objects, which contains the details of the copy operation.</p>"""
    enable_continuous_backup: NotRequired["capo_backup.types.boolean.Boolean"]
    """<p>Specifies whether Backup creates continuous backups. True causes Backup to create continuous backups capable of point-in-time restore (PITR). False (or not specified) causes Backup to create snapshot backups.</p>"""
    schedule_expression_timezone: NotRequired["capo_backup.types.timezone.Timezone"]
    """<p>The timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.</p>"""
    index_actions: NotRequired["capo_backup.types.index_actions.IndexActions"]
    """<p>IndexActions is an array you use to specify how backup data should be indexed.</p> <p>eEach BackupRule can have 0 or 1 IndexAction, as each backup can have up to one index associated with it.</p> <p>Within the array is ResourceType. Only one will be accepted for each BackupRule.</p>"""
    scan_actions: NotRequired["capo_backup.types.scan_actions.ScanActions"]
    """<p>Contains your scanning configuration for the backup rule and includes the malware scanner, and scan mode of either full or incremental.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupRule) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    out["TargetBackupVaultName"] = value["target_backup_vault_name"]
    if "target_logically_air_gapped_backup_vault_arn" in value:
        out["TargetLogicallyAirGappedBackupVaultArn"] = value[
            "target_logically_air_gapped_backup_vault_arn"
        ]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "start_window_minutes" in value:
        out["StartWindowMinutes"] = value["start_window_minutes"]
    if "completion_window_minutes" in value:
        out["CompletionWindowMinutes"] = value["completion_window_minutes"]
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
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "copy_actions" in value:
        import capo_backup.types.copy_actions

        out["CopyActions"] = capo_backup.types.copy_actions.serialize_json(
            value["copy_actions"]
        )
    if "enable_continuous_backup" in value:
        out["EnableContinuousBackup"] = value["enable_continuous_backup"]
    if "schedule_expression_timezone" in value:
        out["ScheduleExpressionTimezone"] = value["schedule_expression_timezone"]
    if "index_actions" in value:
        import capo_backup.types.index_actions

        out["IndexActions"] = capo_backup.types.index_actions.serialize_json(
            value["index_actions"]
        )
    if "scan_actions" in value:
        import capo_backup.types.scan_actions

        out["ScanActions"] = capo_backup.types.scan_actions.serialize_json(
            value["scan_actions"]
        )
    return out


def deserialize_json(data: dict) -> BackupRule:
    out: BackupRule = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("BackupRule.rule_name required")
    if data.get("TargetBackupVaultName") is not None:
        out["target_backup_vault_name"] = data["TargetBackupVaultName"]
    else:
        raise DeserializationError("BackupRule.target_backup_vault_name required")
    if data.get("TargetLogicallyAirGappedBackupVaultArn") is not None:
        out["target_logically_air_gapped_backup_vault_arn"] = data[
            "TargetLogicallyAirGappedBackupVaultArn"
        ]
    if data.get("ScheduleExpression") is not None:
        out["schedule_expression"] = data["ScheduleExpression"]
    if data.get("StartWindowMinutes") is not None:
        out["start_window_minutes"] = data["StartWindowMinutes"]
    if data.get("CompletionWindowMinutes") is not None:
        out["completion_window_minutes"] = data["CompletionWindowMinutes"]
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
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    if data.get("CopyActions") is not None:
        import capo_backup.types.copy_actions

        out["copy_actions"] = capo_backup.types.copy_actions.deserialize_json(
            data["CopyActions"]
        )
    if data.get("EnableContinuousBackup") is not None:
        out["enable_continuous_backup"] = data["EnableContinuousBackup"]
    if data.get("ScheduleExpressionTimezone") is not None:
        out["schedule_expression_timezone"] = data["ScheduleExpressionTimezone"]
    if data.get("IndexActions") is not None:
        import capo_backup.types.index_actions

        out["index_actions"] = capo_backup.types.index_actions.deserialize_json(
            data["IndexActions"]
        )
    if data.get("ScanActions") is not None:
        import capo_backup.types.scan_actions

        out["scan_actions"] = capo_backup.types.scan_actions.deserialize_json(
            data["ScanActions"]
        )
    return out
