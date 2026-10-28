"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.participant_timer_action
    import capo_connect.types.participant_timer_duration_in_minutes


class ParticipantTimerValueParticipantTimerActionMember(TypedDict, closed=True):
    ParticipantTimerAction: (
        "capo_connect.types.participant_timer_action.ParticipantTimerAction"
    )


class ParticipantTimerValueParticipantTimerDurationInMinutesMember(
    TypedDict, closed=True
):
    ParticipantTimerDurationInMinutes: "capo_connect.types.participant_timer_duration_in_minutes.ParticipantTimerDurationInMinutes"


ParticipantTimerValue: TypeAlias = (
    ParticipantTimerValueParticipantTimerActionMember
    | ParticipantTimerValueParticipantTimerDurationInMinutesMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTimerValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ParticipantTimerValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ParticipantTimerAction" in value:
        import capo_connect.types.participant_timer_action

        return {
            "ParticipantTimerAction": capo_connect.types.participant_timer_action.serialize_json(
                value["ParticipantTimerAction"]
            )
        }
    elif "ParticipantTimerDurationInMinutes" in value:
        return {
            "ParticipantTimerDurationInMinutes": value[
                "ParticipantTimerDurationInMinutes"
            ]
        }
    else:
        raise SerializationError("ParticipantTimerValue: no variant present")


def deserialize_json(data: dict) -> ParticipantTimerValue:
    if data.get("ParticipantTimerAction") is not None:
        import capo_connect.types.participant_timer_action

        return {
            "ParticipantTimerAction": capo_connect.types.participant_timer_action.deserialize_json(
                data["ParticipantTimerAction"]
            )
        }
    elif data.get("ParticipantTimerDurationInMinutes") is not None:
        return {
            "ParticipantTimerDurationInMinutes": data[
                "ParticipantTimerDurationInMinutes"
            ]
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ParticipantTimerValue: no recognized variant key")
