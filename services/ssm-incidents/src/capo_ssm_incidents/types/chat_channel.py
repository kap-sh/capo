"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ChatChannel``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.chatbot_sns_configuration_set
    import capo_ssm_incidents.types.empty_chat_channel


class _ChatChannel_empty(TypedDict, closed=True):
    empty: "capo_ssm_incidents.types.empty_chat_channel.EmptyChatChannel"


class _ChatChannel_chatbotSns(TypedDict, closed=True):
    chatbotSns: "capo_ssm_incidents.types.chatbot_sns_configuration_set.ChatbotSnsConfigurationSet"


ChatChannel: TypeAlias = (
    _ChatChannel_empty | _ChatChannel_chatbotSns | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ChatChannel) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ChatChannel: cannot serialize unknown variant {value.name!r}"
        )
    elif "empty" in value:
        import capo_ssm_incidents.types.empty_chat_channel

        return {
            "empty": capo_ssm_incidents.types.empty_chat_channel.serialize_json(
                value["empty"]
            )
        }
    elif "chatbotSns" in value:
        import capo_ssm_incidents.types.chatbot_sns_configuration_set

        return {
            "chatbotSns": capo_ssm_incidents.types.chatbot_sns_configuration_set.serialize_json(
                value["chatbotSns"]
            )
        }
    else:
        raise SerializationError("ChatChannel: no variant present")


def deserialize_json(data: dict) -> ChatChannel:
    if data.get("empty") is not None:
        import capo_ssm_incidents.types.empty_chat_channel

        return {
            "empty": capo_ssm_incidents.types.empty_chat_channel.deserialize_json(
                data["empty"]
            )
        }
    elif data.get("chatbotSns") is not None:
        import capo_ssm_incidents.types.chatbot_sns_configuration_set

        return {
            "chatbotSns": capo_ssm_incidents.types.chatbot_sns_configuration_set.deserialize_json(
                data["chatbotSns"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ChatChannel: no recognized variant key")
