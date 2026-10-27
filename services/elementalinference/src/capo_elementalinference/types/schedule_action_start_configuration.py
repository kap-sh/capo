"""Generated from Smithy shape ``com.amazonaws.elementalinference#ScheduleActionStartConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, SerializationError
from capo_elementalinference.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_elementalinference.types.fixed_mode_schedule_action_start_settings


class _ScheduleActionStartConfiguration_fixedModeScheduleActionStartSettings(
    TypedDict, closed=True
):
    fixedModeScheduleActionStartSettings: "capo_elementalinference.types.fixed_mode_schedule_action_start_settings.FixedModeScheduleActionStartSettings"


ScheduleActionStartConfiguration: TypeAlias = (
    _ScheduleActionStartConfiguration_fixedModeScheduleActionStartSettings
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleActionStartConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ScheduleActionStartConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fixedModeScheduleActionStartSettings" in value:
        import capo_elementalinference.types.fixed_mode_schedule_action_start_settings

        return {
            "fixedModeScheduleActionStartSettings": capo_elementalinference.types.fixed_mode_schedule_action_start_settings.serialize_json(
                value["fixedModeScheduleActionStartSettings"]
            )
        }
    else:
        raise SerializationError("ScheduleActionStartConfiguration: no variant present")


def deserialize_json(data: dict) -> ScheduleActionStartConfiguration:
    if data.get("fixedModeScheduleActionStartSettings") is not None:
        import capo_elementalinference.types.fixed_mode_schedule_action_start_settings

        return {
            "fixedModeScheduleActionStartSettings": capo_elementalinference.types.fixed_mode_schedule_action_start_settings.deserialize_json(
                data["fixedModeScheduleActionStartSettings"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ScheduleActionStartConfiguration: no recognized variant key"
        )
