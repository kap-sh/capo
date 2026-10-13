"""Generated from Smithy shape ``com.amazonaws.chatbot#TeamChannelConfigurationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.teams_channel_configuration

TeamChannelConfigurationsList: TypeAlias = list[
    "capo_chatbot.types.teams_channel_configuration.TeamsChannelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TeamChannelConfigurationsList) -> list:
    import capo_chatbot.types.teams_channel_configuration

    out: list = []
    for item in value:
        out.append(capo_chatbot.types.teams_channel_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> TeamChannelConfigurationsList:
    import capo_chatbot.types.teams_channel_configuration

    out: TeamChannelConfigurationsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chatbot.types.teams_channel_configuration.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TeamChannelConfigurationsList) -> list[Any]:
    import capo_chatbot.types.teams_channel_configuration

    return [
        capo_chatbot.types.teams_channel_configuration.redact_sensitive(item)
        for item in value
    ]
