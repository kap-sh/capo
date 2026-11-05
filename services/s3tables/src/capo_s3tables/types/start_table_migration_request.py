"""Generated from Smithy shape ``com.amazonaws.s3tables#StartTableMigrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.data_migration_settings
    import capo_s3tables.types.destination_table
    import capo_s3tables.types.migration_output_configuration
    import capo_s3tables.types.migration_source_type
    import capo_s3tables.types.role_arn
    import capo_s3tables.types.source_configuration


class StartTableMigrationRequest(TypedDict, closed=True):
    role_arn: "capo_s3tables.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the migration uses to read the source table and its data and to write the destination table and the reports. The role must be in your account, and its trust policy must allow <code>migration.s3tables.amazonaws.com</code> to assume it. You can limit the trust policy to the destination table bucket with the <code>aws:SourceArn</code> and <code>aws:SourceAccount</code> condition keys.</p>"""
    destination_table: "capo_s3tables.types.destination_table.DestinationTable"
    """<p>The table to create and migrate the source into.</p>"""
    source_type: "capo_s3tables.types.migration_source_type.MigrationSourceType"
    """<p>The type of the source. It must match the member that you set in <code>source</code>.</p>"""
    source: "capo_s3tables.types.source_configuration.SourceConfiguration"
    """<p>The source table to migrate.</p>"""
    data_migration: NotRequired[
        "capo_s3tables.types.data_migration_settings.DataMigrationSettings"
    ]
    """<p>The maintenance settings and migration policies for the destination table.</p>"""
    review_migration_plan: NotRequired["bool"]
    """<p>Specifies whether the migration waits in the <code>pendingReview</code> state, so that you can review the compatibility reports before it migrates any data. If <code>true</code>, the migration continues when you call <code>UpdateTableMigration</code> with <code>requestedState</code> set to <code>queued</code>. If you don't continue or cancel the migration within 30 days, the migration fails. The default is <code>false</code>.</p>"""
    migration_output: "capo_s3tables.types.migration_output_configuration.MigrationOutputConfiguration"
    """<p>The bucket and prefixes that the migration writes its reports to. The bucket must be a general purpose bucket in your account and in the same Region as the table bucket, and the migration role must be able to write objects to it. Otherwise, the migration fails when it writes its first report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTableMigrationRequest) -> dict:
    out: dict = {}
    out["roleARN"] = value["role_arn"]
    import capo_s3tables.types.destination_table

    out["destinationTable"] = capo_s3tables.types.destination_table.serialize_json(
        value["destination_table"]
    )
    import capo_s3tables.types.migration_source_type

    out["sourceType"] = capo_s3tables.types.migration_source_type.serialize_json(
        value["source_type"]
    )
    import capo_s3tables.types.source_configuration

    out["source"] = capo_s3tables.types.source_configuration.serialize_json(
        value["source"]
    )
    if "data_migration" in value:
        import capo_s3tables.types.data_migration_settings

        out["dataMigration"] = (
            capo_s3tables.types.data_migration_settings.serialize_json(
                value["data_migration"]
            )
        )
    if "review_migration_plan" in value:
        out["reviewMigrationPlan"] = value["review_migration_plan"]
    import capo_s3tables.types.migration_output_configuration

    out["migrationOutput"] = (
        capo_s3tables.types.migration_output_configuration.serialize_json(
            value["migration_output"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartTableMigrationRequest:
    out: StartTableMigrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleARN") is not None:
        out["role_arn"] = data["roleARN"]
    else:
        out["role_arn"] = ""
    if data.get("destinationTable") is not None:
        import capo_s3tables.types.destination_table

        out["destination_table"] = (
            capo_s3tables.types.destination_table.deserialize_json(
                data["destinationTable"]
            )
        )
    else:
        raise DeserializationError(
            "StartTableMigrationRequest.destination_table required"
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
        import capo_s3tables.types.data_migration_settings

        out["data_migration"] = (
            capo_s3tables.types.data_migration_settings.deserialize_json(
                data["dataMigration"]
            )
        )
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
            "StartTableMigrationRequest.migration_output required"
        )
    return out
