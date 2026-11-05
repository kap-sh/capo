"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.migration_id
    import capo_s3tables.types.migration_state
    import capo_s3tables.types.migration_type
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name


class MigrationSummary(TypedDict, closed=True):
    migration_id: "capo_s3tables.types.migration_id.MigrationId"
    """<p>The ID of the migration.</p>"""
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket that contains the destination table.</p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace of the destination table.</p>"""
    table_arn: NotRequired["capo_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the destination table, once the migration creates it.</p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the destination table.</p>"""
    type: "capo_s3tables.types.migration_type.MigrationType"
    """<p>The type of the migration. Valid values:</p> <ul> <li> <p> <code>start</code> - A migration that <code>StartTableMigration</code> started.</p> </li> <li> <p> <code>sync</code> - A migration that <code>SyncTableMigration</code> started.</p> </li> </ul>"""
    state: "capo_s3tables.types.migration_state.MigrationState"
    """<p>The state of the migration. Valid values:</p> <ul> <li> <p> <code>new</code> - S3 Tables accepted the request.</p> </li> <li> <p> <code>planning</code> - The migration is checking the source table, its objects and the destination for compatibility, and writing the compatibility reports.</p> </li> <li> <p> <code>pendingReview</code> - Planning finished, and the migration waits for you to continue or cancel it with <code>UpdateTableMigration</code>.</p> </li> <li> <p> <code>queued</code> - The migration is waiting to start migrating data.</p> </li> <li> <p> <code>migrating</code> - The migration is running the plan from the <code>planning</code> state: it copies data and commits it to the destination table. A migration reaches this state only if <code>hasValidPlan</code> is <code>true</code>.</p> </li> <li> <p> <code>succeeded</code> - Every planned object migrated.</p> </li> <li> <p> <code>failed</code> - The migration failed. Check <code>failureReason</code> for the cause.</p> </li> <li> <p> <code>cancelling</code> - You cancelled the migration, and it is finishing the work in progress.</p> </li> <li> <p> <code>cancelled</code> - The migration is cancelled.</p> </li> </ul>"""
    has_valid_plan: NotRequired["bool"]
    """<p>A Boolean value that specifies whether planning produced a plan that the migration can run. If planning hasn't finished, this value isn't returned.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the migration was created.</p>"""
    state_updated_at: "datetime.datetime"
    """<p>The date and time that the migration's state last changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationSummary) -> dict:
    out: dict = {}
    out["migrationId"] = value["migration_id"]
    out["tableBucketARN"] = value["table_bucket_arn"]
    out["namespace"] = value["namespace"]
    if "table_arn" in value:
        out["tableARN"] = value["table_arn"]
    out["name"] = value["name"]
    import capo_s3tables.types.migration_type

    out["type"] = capo_s3tables.types.migration_type.serialize_json(value["type"])
    import capo_s3tables.types.migration_state

    out["state"] = capo_s3tables.types.migration_state.serialize_json(value["state"])
    if "has_valid_plan" in value:
        out["hasValidPlan"] = value["has_valid_plan"]
    import capo_s3tables._protocol.serialize

    out["createdAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_s3tables._protocol.serialize

    out["stateUpdatedAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["state_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> MigrationSummary:
    out: MigrationSummary = {}  # type: ignore[typeddict-item]
    if data.get("migrationId") is not None:
        out["migration_id"] = data["migrationId"]
    else:
        out["migration_id"] = ""
    if data.get("tableBucketARN") is not None:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        out["table_bucket_arn"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_s3tables.types.migration_type

        out["type"] = capo_s3tables.types.migration_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_s3tables.types.migration_type.MigrationType", ""
        )
    if data.get("state") is not None:
        import capo_s3tables.types.migration_state

        out["state"] = capo_s3tables.types.migration_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_s3tables.types.migration_state.MigrationState", ""
        )
    if data.get("hasValidPlan") is not None:
        out["has_valid_plan"] = data["hasValidPlan"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("stateUpdatedAt") is not None:
        import datetime

        out["state_updated_at"] = datetime.datetime.fromisoformat(
            data["stateUpdatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["state_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
