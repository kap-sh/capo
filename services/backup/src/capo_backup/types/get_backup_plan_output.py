"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.advanced_backup_settings
    import capo_backup.types.arn
    import capo_backup.types.backup_plan
    import capo_backup.types.scheduled_runs_preview
    import capo_backup.types.string
    import capo_backup.types.timestamp


class GetBackupPlanOutput(TypedDict, closed=True):
    backup_plan: NotRequired["capo_backup.types.backup_plan.BackupPlan"]
    """<p>Specifies the body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""
    backup_plan_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    backup_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    version_id: NotRequired["capo_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>"""
    creator_request_id: NotRequired["capo_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. </p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    deletion_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of <code>DeletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    last_execution_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The last time this backup plan was run. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastExecutionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    advanced_backup_settings: NotRequired[
        "capo_backup.types.advanced_backup_settings.AdvancedBackupSettings"
    ]
    """<p>Contains a list of <code>BackupOptions</code> for each resource type. The list is populated only if the advanced option is set for the backup plan.</p>"""
    scheduled_runs_preview: NotRequired[
        "capo_backup.types.scheduled_runs_preview.ScheduledRunsPreview"
    ]
    """<p>List of upcoming scheduled backup runs. Only included when <code>MaxScheduledRunsPreview</code> parameter is greater than 0. Contains up to 10 future backup executions with their scheduled times, execution types, and associated rule IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanOutput) -> dict:
    out: dict = {}
    if "backup_plan" in value:
        import capo_backup.types.backup_plan

        out["BackupPlan"] = capo_backup.types.backup_plan.serialize_json(
            value["backup_plan"]
        )
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "deletion_date" in value:
        import capo_backup.types.timestamp

        out["DeletionDate"] = capo_backup.types.timestamp.serialize_json(
            value["deletion_date"]
        )
    if "last_execution_date" in value:
        import capo_backup.types.timestamp

        out["LastExecutionDate"] = capo_backup.types.timestamp.serialize_json(
            value["last_execution_date"]
        )
    if "advanced_backup_settings" in value:
        import capo_backup.types.advanced_backup_settings

        out["AdvancedBackupSettings"] = (
            capo_backup.types.advanced_backup_settings.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    if "scheduled_runs_preview" in value:
        import capo_backup.types.scheduled_runs_preview

        out["ScheduledRunsPreview"] = (
            capo_backup.types.scheduled_runs_preview.serialize_json(
                value["scheduled_runs_preview"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBackupPlanOutput:
    out: GetBackupPlanOutput = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlan") is not None:
        import capo_backup.types.backup_plan

        out["backup_plan"] = capo_backup.types.backup_plan.deserialize_json(
            data["BackupPlan"]
        )
    if data.get("BackupPlanId") is not None:
        out["backup_plan_id"] = data["BackupPlanId"]
    if data.get("BackupPlanArn") is not None:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("CreationDate") is not None:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("DeletionDate") is not None:
        import capo_backup.types.timestamp

        out["deletion_date"] = capo_backup.types.timestamp.deserialize_json(
            data["DeletionDate"]
        )
    if data.get("LastExecutionDate") is not None:
        import capo_backup.types.timestamp

        out["last_execution_date"] = capo_backup.types.timestamp.deserialize_json(
            data["LastExecutionDate"]
        )
    if data.get("AdvancedBackupSettings") is not None:
        import capo_backup.types.advanced_backup_settings

        out["advanced_backup_settings"] = (
            capo_backup.types.advanced_backup_settings.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    if data.get("ScheduledRunsPreview") is not None:
        import capo_backup.types.scheduled_runs_preview

        out["scheduled_runs_preview"] = (
            capo_backup.types.scheduled_runs_preview.deserialize_json(
                data["ScheduledRunsPreview"]
            )
        )
    return out


def redact_sensitive(value: GetBackupPlanOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup_plan" in value:
        import capo_backup.types.backup_plan

        out["backup_plan"] = capo_backup.types.backup_plan.redact_sensitive(
            value["backup_plan"]
        )
    return out
