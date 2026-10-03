"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskStats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer
    import capo_database_migration_service.types.long
    import capo_database_migration_service.types.t_stamp


class ReplicationTaskStats(TypedDict, closed=True):
    full_load_progress_percent: "capo_database_migration_service.types.integer.Integer"
    """<p>The percent complete for the full load migration task.</p>"""
    elapsed_time_millis: "capo_database_migration_service.types.long.Long"
    """<p>The elapsed time of the task, in milliseconds.</p>"""
    tables_loaded: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of tables loaded for this task.</p>"""
    tables_loading: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of tables currently loading for this task.</p>"""
    tables_queued: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of tables queued for this task.</p>"""
    tables_errored: "capo_database_migration_service.types.integer.Integer"
    """<p>The number of errors that have occurred during this task.</p>"""
    fresh_start_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task was started either with a fresh start or a target reload.</p>"""
    start_date: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p>The date the replication task was started either with a fresh start or a resume. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType">StartReplicationTaskType</a>.</p>"""
    stop_date: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p>The date the replication task was stopped.</p>"""
    full_load_start_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task full load was started.</p>"""
    full_load_finish_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the replication task full load was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskStats) -> dict:
    out: dict = {}
    out["FullLoadProgressPercent"] = value.get("full_load_progress_percent", 0)
    out["ElapsedTimeMillis"] = value.get("elapsed_time_millis", 0)
    out["TablesLoaded"] = value.get("tables_loaded", 0)
    out["TablesLoading"] = value.get("tables_loading", 0)
    out["TablesQueued"] = value.get("tables_queued", 0)
    out["TablesErrored"] = value.get("tables_errored", 0)
    if "fresh_start_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["FreshStartDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["fresh_start_date"]
            )
        )
    if "start_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["StartDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["start_date"]
            )
        )
    if "stop_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["StopDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["stop_date"]
            )
        )
    if "full_load_start_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["FullLoadStartDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["full_load_start_date"]
            )
        )
    if "full_load_finish_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["FullLoadFinishDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["full_load_finish_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTaskStats:
    out: ReplicationTaskStats = {}  # type: ignore[typeddict-item]
    if data.get("FullLoadProgressPercent") is not None:
        out["full_load_progress_percent"] = data["FullLoadProgressPercent"]
    else:
        out["full_load_progress_percent"] = 0
    if data.get("ElapsedTimeMillis") is not None:
        out["elapsed_time_millis"] = data["ElapsedTimeMillis"]
    else:
        out["elapsed_time_millis"] = 0
    if data.get("TablesLoaded") is not None:
        out["tables_loaded"] = data["TablesLoaded"]
    else:
        out["tables_loaded"] = 0
    if data.get("TablesLoading") is not None:
        out["tables_loading"] = data["TablesLoading"]
    else:
        out["tables_loading"] = 0
    if data.get("TablesQueued") is not None:
        out["tables_queued"] = data["TablesQueued"]
    else:
        out["tables_queued"] = 0
    if data.get("TablesErrored") is not None:
        out["tables_errored"] = data["TablesErrored"]
    else:
        out["tables_errored"] = 0
    if data.get("FreshStartDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["fresh_start_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FreshStartDate"]
            )
        )
    if data.get("StartDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["start_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["StartDate"]
            )
        )
    if data.get("StopDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["stop_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["StopDate"]
            )
        )
    if data.get("FullLoadStartDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["full_load_start_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FullLoadStartDate"]
            )
        )
    if data.get("FullLoadFinishDate") is not None:
        import capo_database_migration_service.types.t_stamp

        out["full_load_finish_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["FullLoadFinishDate"]
            )
        )
    return out
