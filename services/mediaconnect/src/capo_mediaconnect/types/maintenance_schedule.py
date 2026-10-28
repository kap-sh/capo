"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceSchedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.window_maintenance_schedule


class MaintenanceScheduleWindowMember(TypedDict, closed=True):
    Window: (
        "capo_mediaconnect.types.window_maintenance_schedule.WindowMaintenanceSchedule"
    )


MaintenanceSchedule: TypeAlias = MaintenanceScheduleWindowMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceSchedule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MaintenanceSchedule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Window" in value:
        import capo_mediaconnect.types.window_maintenance_schedule

        return {
            "window": capo_mediaconnect.types.window_maintenance_schedule.serialize_json(
                value["Window"]
            )
        }
    else:
        raise SerializationError("MaintenanceSchedule: no variant present")


def deserialize_json(data: dict) -> MaintenanceSchedule:
    if data.get("window") is not None:
        import capo_mediaconnect.types.window_maintenance_schedule

        return {
            "Window": capo_mediaconnect.types.window_maintenance_schedule.deserialize_json(
                data["window"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MaintenanceSchedule: no recognized variant key")
