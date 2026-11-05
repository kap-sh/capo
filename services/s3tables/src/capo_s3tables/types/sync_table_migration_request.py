"""Generated from Smithy shape ``com.amazonaws.s3tables#SyncTableMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.migration_output_configuration
    import capo_s3tables.types.role_arn
    import capo_s3tables.types.table_arn


class SyncTableMigrationRequest(TypedDict, closed=True):
    role_arn: "capo_s3tables.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the sync uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow <code>migration.s3tables.amazonaws.com</code> to assume it. You can limit the trust policy to the destination table bucket with the <code>aws:SourceArn</code> and <code>aws:SourceAccount</code> condition keys.</p>"""
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the destination table to sync. The table must have a migration, and you must not have called <code>CompleteTableMigration</code> for it.</p>"""
    review_migration_plan: NotRequired["bool"]
    """<p>Specifies whether the sync waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data. If <code>true</code>, the migration continues when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. The default is <code>false</code>.</p>"""
    migration_output: "capo_s3tables.types.migration_output_configuration.MigrationOutputConfiguration"
    """<p>The bucket and prefixes that the sync writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncTableMigrationRequest) -> dict:
    out: dict = {}
    out["roleARN"] = value["role_arn"]
    out["tableARN"] = value["table_arn"]
    if "review_migration_plan" in value:
        out["reviewMigrationPlan"] = value["review_migration_plan"]
    import capo_s3tables.types.migration_output_configuration

    out["migrationOutput"] = (
        capo_s3tables.types.migration_output_configuration.serialize_json(
            value["migration_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> SyncTableMigrationRequest:
    out: SyncTableMigrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleARN") is not None:
        out["role_arn"] = data["roleARN"]
    else:
        out["role_arn"] = ""
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    else:
        out["table_arn"] = ""
    if data.get("reviewMigrationPlan") is not None:
        out["review_migration_plan"] = data["reviewMigrationPlan"]
    if data.get("migrationOutput") is not None:
        import capo_s3tables.types.migration_output_configuration

        out["migration_output"] = (
            capo_s3tables.types.migration_output_configuration.deserialize_json(
                data["migrationOutput"]
            )
        )
    else:
        raise DeserializationError(
            "SyncTableMigrationRequest.migration_output required"
        )
    return out
