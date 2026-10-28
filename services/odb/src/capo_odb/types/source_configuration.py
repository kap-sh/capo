"""Generated from Smithy shape ``com.amazonaws.odb#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError, SerializationError
from capo_odb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_odb.types.clone_to_refreshable_configuration
    import capo_odb.types.cross_region_data_guard_configuration
    import capo_odb.types.cross_region_disaster_recovery_configuration
    import capo_odb.types.database_clone_configuration
    import capo_odb.types.point_in_time_restore_configuration
    import capo_odb.types.restore_from_backup_configuration


class SourceConfigurationDatabaseCloneMember(TypedDict, closed=True):
    databaseClone: (
        "capo_odb.types.database_clone_configuration.DatabaseCloneConfiguration"
    )


class SourceConfigurationRestoreFromBackupMember(TypedDict, closed=True):
    restoreFromBackup: "capo_odb.types.restore_from_backup_configuration.RestoreFromBackupConfiguration"


class SourceConfigurationPointInTimeRestoreMember(TypedDict, closed=True):
    pointInTimeRestore: "capo_odb.types.point_in_time_restore_configuration.PointInTimeRestoreConfiguration"


class SourceConfigurationCrossRegionDataGuardMember(TypedDict, closed=True):
    crossRegionDataGuard: "capo_odb.types.cross_region_data_guard_configuration.CrossRegionDataGuardConfiguration"


class SourceConfigurationCrossRegionDisasterRecoveryMember(TypedDict, closed=True):
    crossRegionDisasterRecovery: "capo_odb.types.cross_region_disaster_recovery_configuration.CrossRegionDisasterRecoveryConfiguration"


class SourceConfigurationCloneToRefreshableMember(TypedDict, closed=True):
    cloneToRefreshable: "capo_odb.types.clone_to_refreshable_configuration.CloneToRefreshableConfiguration"


SourceConfiguration: TypeAlias = (
    SourceConfigurationDatabaseCloneMember
    | SourceConfigurationRestoreFromBackupMember
    | SourceConfigurationPointInTimeRestoreMember
    | SourceConfigurationCrossRegionDataGuardMember
    | SourceConfigurationCrossRegionDisasterRecoveryMember
    | SourceConfigurationCloneToRefreshableMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "databaseClone" in value:
        import capo_odb.types.database_clone_configuration

        return {
            "databaseClone": capo_odb.types.database_clone_configuration.serialize_aws_json_1_0(
                value["databaseClone"]
            )
        }
    elif "restoreFromBackup" in value:
        import capo_odb.types.restore_from_backup_configuration

        return {
            "restoreFromBackup": capo_odb.types.restore_from_backup_configuration.serialize_aws_json_1_0(
                value["restoreFromBackup"]
            )
        }
    elif "pointInTimeRestore" in value:
        import capo_odb.types.point_in_time_restore_configuration

        return {
            "pointInTimeRestore": capo_odb.types.point_in_time_restore_configuration.serialize_aws_json_1_0(
                value["pointInTimeRestore"]
            )
        }
    elif "crossRegionDataGuard" in value:
        import capo_odb.types.cross_region_data_guard_configuration

        return {
            "crossRegionDataGuard": capo_odb.types.cross_region_data_guard_configuration.serialize_aws_json_1_0(
                value["crossRegionDataGuard"]
            )
        }
    elif "crossRegionDisasterRecovery" in value:
        import capo_odb.types.cross_region_disaster_recovery_configuration

        return {
            "crossRegionDisasterRecovery": capo_odb.types.cross_region_disaster_recovery_configuration.serialize_aws_json_1_0(
                value["crossRegionDisasterRecovery"]
            )
        }
    elif "cloneToRefreshable" in value:
        import capo_odb.types.clone_to_refreshable_configuration

        return {
            "cloneToRefreshable": capo_odb.types.clone_to_refreshable_configuration.serialize_aws_json_1_0(
                value["cloneToRefreshable"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SourceConfiguration:
    if data.get("databaseClone") is not None:
        import capo_odb.types.database_clone_configuration

        return {
            "databaseClone": capo_odb.types.database_clone_configuration.deserialize_aws_json_1_0(
                data["databaseClone"]
            )
        }
    elif data.get("restoreFromBackup") is not None:
        import capo_odb.types.restore_from_backup_configuration

        return {
            "restoreFromBackup": capo_odb.types.restore_from_backup_configuration.deserialize_aws_json_1_0(
                data["restoreFromBackup"]
            )
        }
    elif data.get("pointInTimeRestore") is not None:
        import capo_odb.types.point_in_time_restore_configuration

        return {
            "pointInTimeRestore": capo_odb.types.point_in_time_restore_configuration.deserialize_aws_json_1_0(
                data["pointInTimeRestore"]
            )
        }
    elif data.get("crossRegionDataGuard") is not None:
        import capo_odb.types.cross_region_data_guard_configuration

        return {
            "crossRegionDataGuard": capo_odb.types.cross_region_data_guard_configuration.deserialize_aws_json_1_0(
                data["crossRegionDataGuard"]
            )
        }
    elif data.get("crossRegionDisasterRecovery") is not None:
        import capo_odb.types.cross_region_disaster_recovery_configuration

        return {
            "crossRegionDisasterRecovery": capo_odb.types.cross_region_disaster_recovery_configuration.deserialize_aws_json_1_0(
                data["crossRegionDisasterRecovery"]
            )
        }
    elif data.get("cloneToRefreshable") is not None:
        import capo_odb.types.clone_to_refreshable_configuration

        return {
            "cloneToRefreshable": capo_odb.types.clone_to_refreshable_configuration.deserialize_aws_json_1_0(
                data["cloneToRefreshable"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceConfiguration: no recognized variant key")
