"""Generated from Smithy shape ``com.amazonaws.connect#ChatParticipantRoleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.participant_timer_config_list


class ChatParticipantRoleConfig(TypedDict, closed=True):
    participant_timer_config_list: (
        "capo_connect.types.participant_timer_config_list.ParticipantTimerConfigList"
    )
    """<p>A list of participant timers. You can specify any unique combination of role and timer type. Duplicate entries error out the request with a 400.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatParticipantRoleConfig) -> dict:
    out: dict = {}
    import capo_connect.types.participant_timer_config_list

    out["ParticipantTimerConfigList"] = (
        capo_connect.types.participant_timer_config_list.serialize_json(
            value["participant_timer_config_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChatParticipantRoleConfig:
    out: ChatParticipantRoleConfig = {}  # type: ignore[typeddict-item]
    if data.get("ParticipantTimerConfigList") is not None:
        import capo_connect.types.participant_timer_config_list

        out["participant_timer_config_list"] = (
            capo_connect.types.participant_timer_config_list.deserialize_json(
                data["ParticipantTimerConfigList"]
            )
        )
    else:
        out["participant_timer_config_list"] = []
    return out
