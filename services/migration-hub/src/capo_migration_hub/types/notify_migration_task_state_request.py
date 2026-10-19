"""Generated from Smithy shape ``com.amazonaws.migrationhub#NotifyMigrationTaskStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub.types.dry_run
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.next_update_seconds
    import capo_migration_hub.types.progress_update_stream
    import capo_migration_hub.types.task
    import capo_migration_hub.types.update_date_time


class NotifyMigrationTaskStateRequest(TypedDict, closed=True):
    progress_update_stream: (
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. </p>"""
    migration_task_name: (
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    task: "capo_migration_hub.types.task.Task"
    """<p>Information about the task's progress and status.</p>"""
    update_date_time: "capo_migration_hub.types.update_date_time.UpdateDateTime"
    """<p>The timestamp when the task was gathered.</p>"""
    next_update_seconds: (
        "capo_migration_hub.types.next_update_seconds.NextUpdateSeconds"
    )
    """<p>Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.</p>"""
    dry_run: NotRequired["capo_migration_hub.types.dry_run.DryRun"]
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyMigrationTaskStateRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    import capo_migration_hub.types.task

    out["Task"] = capo_migration_hub.types.task.serialize_aws_json_1_1(value["task"])
    import capo_migration_hub.types.update_date_time

    out["UpdateDateTime"] = (
        capo_migration_hub.types.update_date_time.serialize_aws_json_1_1(
            value["update_date_time"]
        )
    )
    out["NextUpdateSeconds"] = value["next_update_seconds"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyMigrationTaskStateRequest:
    out: NotifyMigrationTaskStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProgressUpdateStream") is not None:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        out["progress_update_stream"] = ""
    if data.get("MigrationTaskName") is not None:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        out["migration_task_name"] = ""
    if data.get("Task") is not None:
        import capo_migration_hub.types.task

        out["task"] = capo_migration_hub.types.task.deserialize_aws_json_1_1(
            data["Task"]
        )
    else:
        raise DeserializationError("NotifyMigrationTaskStateRequest.task required")
    if data.get("UpdateDateTime") is not None:
        import capo_migration_hub.types.update_date_time

        out["update_date_time"] = (
            capo_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("NextUpdateSeconds") is not None:
        out["next_update_seconds"] = data["NextUpdateSeconds"]
    else:
        out["next_update_seconds"] = 0
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
