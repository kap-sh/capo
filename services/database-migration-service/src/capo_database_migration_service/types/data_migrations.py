"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataMigrations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_migration

DataMigrations: TypeAlias = list[
    "capo_database_migration_service.types.data_migration.DataMigration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataMigrations) -> list:
    import capo_database_migration_service.types.data_migration

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.data_migration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataMigrations:
    import capo_database_migration_service.types.data_migration

    out: DataMigrations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_database_migration_service.types.data_migration.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: DataMigrations) -> list[Any]:
    import capo_database_migration_service.types.data_migration

    return [
        capo_database_migration_service.types.data_migration.redact_sensitive(item)
        for item in value
    ]
