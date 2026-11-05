"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.data_migration_overview
    import capo_s3tables.types.migration_failure_reason
    import capo_s3tables.types.migration_id
    import capo_s3tables.types.migration_output_overview
    import capo_s3tables.types.migration_source_type
    import capo_s3tables.types.migration_state
    import capo_s3tables.types.migration_stats
    import capo_s3tables.types.migration_type
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.planning_stats
    import capo_s3tables.types.role_arn
    import capo_s3tables.types.source_configuration
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name


class GetTableMigrationResponse(TypedDict, closed=True):
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
    """<p>The state of the migration. Valid values:</p> <ul> <li> <p> <code>new</code> - S3 Tables accepted the request.</p> </li> <li> <p> <code>planning</code> - The migration is checking the source table, its objects and the destination for compatibility, and writing the compatibility reports.</p> </li> <li> <p> <code>pendingReview</code> - Planning finished, and the migration waits for you to continue or cancel it with <code>UpdateTableMigration</code>.</p> </li> <li> <p> <code>queued</code> - The migration is waiting to start migrating data.</p> </li> <li> <p> <code>migrating</code> - The migration is running the plan from the <code>planning</code> state: it copies data and commits it to the destination table. A migration reaches this state only if <code>hasValidPlan</code> is <code>true</code>.</p> </li> <li> <p> <code>succeeded</code> - Every planned object migrated.</p> </li> <li> <p> <code>failed</code> - The migration failed. Check <code>failureReason</code> for the cause.</p> </li> <li> <p> <code>cancelling</code> - You cancelled the migration, and it is finishing the work in progress.</p> </li> <li> <p> <code>cancelled</code> - The migration is cancelled.</p> </li> </ul> <p>A migration ends in the <code>succeeded</code>, <code>failed</code> or <code>cancelled</code> state. You can cancel it until it ends.</p>"""
    role_arn: "capo_s3tables.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the migration uses.</p>"""
    review_migration_plan: "bool"
    """<p>A Boolean value that specifies whether the migration waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data.</p>"""
    has_valid_plan: NotRequired["bool"]
    """<p>A Boolean value that specifies whether planning produced a plan that the migration can run. If planning hasn't finished, this value isn't returned.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the migration was created.</p>"""
    state_updated_at: "datetime.datetime"
    """<p>The date and time that the migration's state last changed.</p>"""
    failure_reason: NotRequired[
        "capo_s3tables.types.migration_failure_reason.MigrationFailureReason"
    ]
    """<p>The reason that the migration failed. The code names the cause, such as a migration role that S3 Tables can't assume or an Amazon Web Services Glue table that doesn't exist, or the report that lists the findings. This value is returned only when the migration is in the <code>failed</code> state.</p>"""
    planning_stats: NotRequired["capo_s3tables.types.planning_stats.PlanningStats"]
    """<p>Statistics about the source and the partitions in the migration. This value is returned after planning finishes.</p>"""
    migration_stats: NotRequired["capo_s3tables.types.migration_stats.MigrationStats"]
    """<p>The number of objects that migrated, failed or are pending. These counts are set when planning finishes and updated when the migration ends.</p>"""
    source_type: "capo_s3tables.types.migration_source_type.MigrationSourceType"
    """<p>The type of the migration's source.</p>"""
    source: "capo_s3tables.types.source_configuration.SourceConfiguration"
    """<p>The source table of the migration.</p>"""
    data_migration: "capo_s3tables.types.data_migration_overview.DataMigrationOverview"
    """<p>The maintenance settings and migration policies for the destination table.</p>"""
    migration_output: (
        "capo_s3tables.types.migration_output_overview.MigrationOutputOverview"
    )
    """<p>The bucket and prefixes for the migration's reports, and the location of each report once it is written.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableMigrationResponse) -> dict:
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
    out["roleARN"] = value["role_arn"]
    out["reviewMigrationPlan"] = value["review_migration_plan"]
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
    if "failure_reason" in value:
        import capo_s3tables.types.migration_failure_reason

        out["failureReason"] = (
            capo_s3tables.types.migration_failure_reason.serialize_json(
                value["failure_reason"]
            )
        )
    if "planning_stats" in value:
        import capo_s3tables.types.planning_stats

        out["planningStats"] = capo_s3tables.types.planning_stats.serialize_json(
            value["planning_stats"]
        )
    if "migration_stats" in value:
        import capo_s3tables.types.migration_stats

        out["migrationStats"] = capo_s3tables.types.migration_stats.serialize_json(
            value["migration_stats"]
        )
    import capo_s3tables.types.migration_source_type

    out["sourceType"] = capo_s3tables.types.migration_source_type.serialize_json(
        value["source_type"]
    )
    import capo_s3tables.types.source_configuration

    out["source"] = capo_s3tables.types.source_configuration.serialize_json(
        value["source"]
    )
    import capo_s3tables.types.data_migration_overview

    out["dataMigration"] = capo_s3tables.types.data_migration_overview.serialize_json(
        value["data_migration"]
    )
    import capo_s3tables.types.migration_output_overview

    out["migrationOutput"] = (
        capo_s3tables.types.migration_output_overview.serialize_json(
            value["migration_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableMigrationResponse:
    out: GetTableMigrationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("roleARN") is not None:
        out["role_arn"] = data["roleARN"]
    else:
        out["role_arn"] = ""
    if data.get("reviewMigrationPlan") is not None:
        out["review_migration_plan"] = data["reviewMigrationPlan"]
    else:
        out["review_migration_plan"] = False
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
    if data.get("failureReason") is not None:
        import capo_s3tables.types.migration_failure_reason

        out["failure_reason"] = (
            capo_s3tables.types.migration_failure_reason.deserialize_json(
                data["failureReason"]
            )
        )
    if data.get("planningStats") is not None:
        import capo_s3tables.types.planning_stats

        out["planning_stats"] = capo_s3tables.types.planning_stats.deserialize_json(
            data["planningStats"]
        )
    if data.get("migrationStats") is not None:
        import capo_s3tables.types.migration_stats

        out["migration_stats"] = capo_s3tables.types.migration_stats.deserialize_json(
            data["migrationStats"]
        )
    if data.get("sourceType") is not None:
        import capo_s3tables.types.migration_source_type

        out["source_type"] = capo_s3tables.types.migration_source_type.deserialize_json(
            data["sourceType"]
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_s3tables.types.migration_source_type.MigrationSourceType", ""
        )
    if data.get("source") is not None:
        import capo_s3tables.types.source_configuration

        out["source"] = capo_s3tables.types.source_configuration.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("dataMigration") is not None:
        import capo_s3tables.types.data_migration_overview

        out["data_migration"] = (
            capo_s3tables.types.data_migration_overview.deserialize_json(
                data["dataMigration"]
            )
        )
    else:
        raise DeserializationError("GetTableMigrationResponse.data_migration required")
    if data.get("migrationOutput") is not None:
        import capo_s3tables.types.migration_output_overview

        out["migration_output"] = (
            capo_s3tables.types.migration_output_overview.deserialize_json(
                data["migrationOutput"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableMigrationResponse.migration_output required"
        )
    return out
