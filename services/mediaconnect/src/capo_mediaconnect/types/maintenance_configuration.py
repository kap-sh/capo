"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.default_maintenance_configuration
    import capo_mediaconnect.types.preferred_day_time_maintenance_configuration


class _MaintenanceConfiguration_PreferredDayTime(TypedDict, closed=True):
    PreferredDayTime: "capo_mediaconnect.types.preferred_day_time_maintenance_configuration.PreferredDayTimeMaintenanceConfiguration"


class _MaintenanceConfiguration_Default(TypedDict, closed=True):
    Default: "capo_mediaconnect.types.default_maintenance_configuration.DefaultMaintenanceConfiguration"


MaintenanceConfiguration: TypeAlias = (
    _MaintenanceConfiguration_PreferredDayTime
    | _MaintenanceConfiguration_Default
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MaintenanceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PreferredDayTime" in value:
        import capo_mediaconnect.types.preferred_day_time_maintenance_configuration

        return {
            "preferredDayTime": capo_mediaconnect.types.preferred_day_time_maintenance_configuration.serialize_json(
                value["PreferredDayTime"]
            )
        }
    elif "Default" in value:
        import capo_mediaconnect.types.default_maintenance_configuration

        return {
            "default": capo_mediaconnect.types.default_maintenance_configuration.serialize_json(
                value["Default"]
            )
        }
    else:
        raise SerializationError("MaintenanceConfiguration: no variant present")


def deserialize_json(data: dict) -> MaintenanceConfiguration:
    if data.get("preferredDayTime") is not None:
        import capo_mediaconnect.types.preferred_day_time_maintenance_configuration

        return {
            "PreferredDayTime": capo_mediaconnect.types.preferred_day_time_maintenance_configuration.deserialize_json(
                data["preferredDayTime"]
            )
        }
    elif data.get("default") is not None:
        import capo_mediaconnect.types.default_maintenance_configuration

        return {
            "Default": capo_mediaconnect.types.default_maintenance_configuration.deserialize_json(
                data["default"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MaintenanceConfiguration: no recognized variant key"
        )
