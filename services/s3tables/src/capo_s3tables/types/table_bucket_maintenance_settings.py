"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketMaintenanceSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError, SerializationError
from capo_s3tables.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_unreferenced_file_removal_settings


class _TableBucketMaintenanceSettings_icebergUnreferencedFileRemoval(
    TypedDict, closed=True
):
    icebergUnreferencedFileRemoval: "capo_s3tables.types.iceberg_unreferenced_file_removal_settings.IcebergUnreferencedFileRemovalSettings"


TableBucketMaintenanceSettings: TypeAlias = (
    _TableBucketMaintenanceSettings_icebergUnreferencedFileRemoval | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketMaintenanceSettings) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TableBucketMaintenanceSettings: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "icebergUnreferencedFileRemoval" in value:
        import capo_s3tables.types.iceberg_unreferenced_file_removal_settings

        return {
            "icebergUnreferencedFileRemoval": capo_s3tables.types.iceberg_unreferenced_file_removal_settings.serialize_json(
                value["icebergUnreferencedFileRemoval"]
            )
        }
    else:
        raise SerializationError("TableBucketMaintenanceSettings: no variant present")


def deserialize_json(data: dict) -> TableBucketMaintenanceSettings:
    if data.get("icebergUnreferencedFileRemoval") is not None:
        import capo_s3tables.types.iceberg_unreferenced_file_removal_settings

        return {
            "icebergUnreferencedFileRemoval": capo_s3tables.types.iceberg_unreferenced_file_removal_settings.deserialize_json(
                data["icebergUnreferencedFileRemoval"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TableBucketMaintenanceSettings: no recognized variant key"
        )
