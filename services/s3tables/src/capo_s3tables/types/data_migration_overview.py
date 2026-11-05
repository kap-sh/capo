"""Generated from Smithy shape ``com.amazonaws.s3tables#DataMigrationOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.maintenance_settings
    import capo_s3tables.types.migration_policies


class DataMigrationOverview(TypedDict, closed=True):
    maintenance_settings: "capo_s3tables.types.maintenance_settings.MaintenanceSettings"
    """<p>The maintenance settings for the destination table. The migration applies them when it creates the table: snapshot management starts then, and compaction starts after you complete the migration. If you don't specify a setting, the migration uses its default: a target file size of 512 MB, the binpack compaction strategy, at least 3 snapshots, and a maximum snapshot age of 120 hours. Unreferenced file removal follows the table bucket's configuration after you complete the migration.</p>"""
    migration_policies: "capo_s3tables.types.migration_policies.MigrationPolicies"
    """<p>The policies for source data that doesn't fit the destination schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataMigrationOverview) -> dict:
    out: dict = {}
    import capo_s3tables.types.maintenance_settings

    out["maintenanceSettings"] = (
        capo_s3tables.types.maintenance_settings.serialize_json(
            value["maintenance_settings"]
        )
    )
    import capo_s3tables.types.migration_policies

    out["migrationPolicies"] = capo_s3tables.types.migration_policies.serialize_json(
        value["migration_policies"]
    )
    return out


def deserialize_json(data: dict) -> DataMigrationOverview:
    out: DataMigrationOverview = {}  # type: ignore[typeddict-item]
    if data.get("maintenanceSettings") is not None:
        import capo_s3tables.types.maintenance_settings

        out["maintenance_settings"] = (
            capo_s3tables.types.maintenance_settings.deserialize_json(
                data["maintenanceSettings"]
            )
        )
    else:
        raise DeserializationError(
            "DataMigrationOverview.maintenance_settings required"
        )
    if data.get("migrationPolicies") is not None:
        import capo_s3tables.types.migration_policies

        out["migration_policies"] = (
            capo_s3tables.types.migration_policies.deserialize_json(
                data["migrationPolicies"]
            )
        )
    else:
        raise DeserializationError("DataMigrationOverview.migration_policies required")
    return out
