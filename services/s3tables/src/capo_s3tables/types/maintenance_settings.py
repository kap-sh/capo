"""Generated from Smithy shape ``com.amazonaws.s3tables#MaintenanceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.migration_compaction_settings
    import capo_s3tables.types.migration_snapshot_management_settings


class MaintenanceSettings(TypedDict, closed=True):
    iceberg_compaction: NotRequired[
        "capo_s3tables.types.migration_compaction_settings.MigrationCompactionSettings"
    ]
    """<p>The compaction settings.</p>"""
    iceberg_snapshot_management: NotRequired[
        "capo_s3tables.types.migration_snapshot_management_settings.MigrationSnapshotManagementSettings"
    ]
    """<p>The snapshot management settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceSettings) -> dict:
    out: dict = {}
    if "iceberg_compaction" in value:
        import capo_s3tables.types.migration_compaction_settings

        out["icebergCompaction"] = (
            capo_s3tables.types.migration_compaction_settings.serialize_json(
                value["iceberg_compaction"]
            )
        )
    if "iceberg_snapshot_management" in value:
        import capo_s3tables.types.migration_snapshot_management_settings

        out["icebergSnapshotManagement"] = (
            capo_s3tables.types.migration_snapshot_management_settings.serialize_json(
                value["iceberg_snapshot_management"]
            )
        )
    return out


def deserialize_json(data: dict) -> MaintenanceSettings:
    out: MaintenanceSettings = {}  # type: ignore[typeddict-item]
    if data.get("icebergCompaction") is not None:
        import capo_s3tables.types.migration_compaction_settings

        out["iceberg_compaction"] = (
            capo_s3tables.types.migration_compaction_settings.deserialize_json(
                data["icebergCompaction"]
            )
        )
    if data.get("icebergSnapshotManagement") is not None:
        import capo_s3tables.types.migration_snapshot_management_settings

        out["iceberg_snapshot_management"] = (
            capo_s3tables.types.migration_snapshot_management_settings.deserialize_json(
                data["icebergSnapshotManagement"]
            )
        )
    return out
