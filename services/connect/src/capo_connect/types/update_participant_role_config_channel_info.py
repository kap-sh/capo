"""Generated from Smithy shape ``com.amazonaws.connect#UpdateParticipantRoleConfigChannelInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.chat_participant_role_config


class _UpdateParticipantRoleConfigChannelInfo_Chat(TypedDict, closed=True):
    Chat: "capo_connect.types.chat_participant_role_config.ChatParticipantRoleConfig"


UpdateParticipantRoleConfigChannelInfo: TypeAlias = (
    _UpdateParticipantRoleConfigChannelInfo_Chat | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParticipantRoleConfigChannelInfo) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateParticipantRoleConfigChannelInfo: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Chat" in value:
        import capo_connect.types.chat_participant_role_config

        return {
            "Chat": capo_connect.types.chat_participant_role_config.serialize_json(
                value["Chat"]
            )
        }
    else:
        raise SerializationError(
            "UpdateParticipantRoleConfigChannelInfo: no variant present"
        )


def deserialize_json(data: dict) -> UpdateParticipantRoleConfigChannelInfo:
    if data.get("Chat") is not None:
        import capo_connect.types.chat_participant_role_config

        return {
            "Chat": capo_connect.types.chat_participant_role_config.deserialize_json(
                data["Chat"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateParticipantRoleConfigChannelInfo: no recognized variant key"
        )
