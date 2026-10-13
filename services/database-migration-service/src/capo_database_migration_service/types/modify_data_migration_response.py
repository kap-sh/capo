"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyDataMigrationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.data_migration


class ModifyDataMigrationResponse(TypedDict, closed=True):
    data_migration: NotRequired[
        "capo_database_migration_service.types.data_migration.DataMigration"
    ]
    """<p>Information about the modified data migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDataMigrationResponse) -> dict:
    out: dict = {}
    if "data_migration" in value:
        import capo_database_migration_service.types.data_migration

        out["DataMigration"] = (
            capo_database_migration_service.types.data_migration.serialize_aws_json_1_1(
                value["data_migration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDataMigrationResponse:
    out: ModifyDataMigrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("DataMigration") is not None:
        import capo_database_migration_service.types.data_migration

        out["data_migration"] = (
            capo_database_migration_service.types.data_migration.deserialize_aws_json_1_1(
                data["DataMigration"]
            )
        )
    return out


def redact_sensitive(value: ModifyDataMigrationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_migration" in value:
        import capo_database_migration_service.types.data_migration

        out["data_migration"] = (
            capo_database_migration_service.types.data_migration.redact_sensitive(
                value["data_migration"]
            )
        )
    return out
