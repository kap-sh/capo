"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError, SerializationError
from capo_s3tables.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_compaction_settings
    import capo_s3tables.types.iceberg_snapshot_management_settings


class TableMaintenanceSettingsIcebergCompactionMember(TypedDict, closed=True):
    icebergCompaction: (
        "capo_s3tables.types.iceberg_compaction_settings.IcebergCompactionSettings"
    )


class TableMaintenanceSettingsIcebergSnapshotManagementMember(TypedDict, closed=True):
    icebergSnapshotManagement: "capo_s3tables.types.iceberg_snapshot_management_settings.IcebergSnapshotManagementSettings"


TableMaintenanceSettings: TypeAlias = (
    TableMaintenanceSettingsIcebergCompactionMember
    | TableMaintenanceSettingsIcebergSnapshotManagementMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TableMaintenanceSettings) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TableMaintenanceSettings: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "icebergCompaction" in value:
        import capo_s3tables.types.iceberg_compaction_settings

        return {
            "icebergCompaction": capo_s3tables.types.iceberg_compaction_settings.serialize_json(
                value["icebergCompaction"]
            )
        }
    elif "icebergSnapshotManagement" in value:
        import capo_s3tables.types.iceberg_snapshot_management_settings

        return {
            "icebergSnapshotManagement": capo_s3tables.types.iceberg_snapshot_management_settings.serialize_json(
                value["icebergSnapshotManagement"]
            )
        }
    else:
        raise SerializationError("TableMaintenanceSettings: no variant present")


def deserialize_json(data: dict) -> TableMaintenanceSettings:
    if data.get("icebergCompaction") is not None:
        import capo_s3tables.types.iceberg_compaction_settings

        return {
            "icebergCompaction": capo_s3tables.types.iceberg_compaction_settings.deserialize_json(
                data["icebergCompaction"]
            )
        }
    elif data.get("icebergSnapshotManagement") is not None:
        import capo_s3tables.types.iceberg_snapshot_management_settings

        return {
            "icebergSnapshotManagement": capo_s3tables.types.iceberg_snapshot_management_settings.deserialize_json(
                data["icebergSnapshotManagement"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TableMaintenanceSettings: no recognized variant key"
        )
