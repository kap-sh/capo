"""Generated from Smithy shape ``com.amazonaws.healthlake#RestoreConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError
from capo_healthlake.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_healthlake.types.continuous_backup_restore_configuration


class _RestoreConfiguration_ContinuousBackupRestoreConfiguration(
    TypedDict, closed=True
):
    ContinuousBackupRestoreConfiguration: "capo_healthlake.types.continuous_backup_restore_configuration.ContinuousBackupRestoreConfiguration"


RestoreConfiguration: TypeAlias = (
    _RestoreConfiguration_ContinuousBackupRestoreConfiguration | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RestoreConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ContinuousBackupRestoreConfiguration" in value:
        import capo_healthlake.types.continuous_backup_restore_configuration

        return {
            "ContinuousBackupRestoreConfiguration": capo_healthlake.types.continuous_backup_restore_configuration.serialize_aws_json_1_0(
                value["ContinuousBackupRestoreConfiguration"]
            )
        }
    else:
        raise SerializationError("RestoreConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RestoreConfiguration:
    if data.get("ContinuousBackupRestoreConfiguration") is not None:
        import capo_healthlake.types.continuous_backup_restore_configuration

        return {
            "ContinuousBackupRestoreConfiguration": capo_healthlake.types.continuous_backup_restore_configuration.deserialize_aws_json_1_0(
                data["ContinuousBackupRestoreConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RestoreConfiguration: no recognized variant key")
