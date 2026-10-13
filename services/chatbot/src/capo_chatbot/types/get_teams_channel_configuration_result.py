"""Generated from Smithy shape ``com.amazonaws.chatbot#GetTeamsChannelConfigurationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.teams_channel_configuration


class GetTeamsChannelConfigurationResult(TypedDict, closed=True):
    channel_configuration: NotRequired[
        "capo_chatbot.types.teams_channel_configuration.TeamsChannelConfiguration"
    ]
    """<p>The configuration for a Microsoft Teams channel configured with AWS Chatbot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTeamsChannelConfigurationResult) -> dict:
    out: dict = {}
    if "channel_configuration" in value:
        import capo_chatbot.types.teams_channel_configuration

        out["ChannelConfiguration"] = (
            capo_chatbot.types.teams_channel_configuration.serialize_json(
                value["channel_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTeamsChannelConfigurationResult:
    out: GetTeamsChannelConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("ChannelConfiguration") is not None:
        import capo_chatbot.types.teams_channel_configuration

        out["channel_configuration"] = (
            capo_chatbot.types.teams_channel_configuration.deserialize_json(
                data["ChannelConfiguration"]
            )
        )
    return out


def redact_sensitive(value: GetTeamsChannelConfigurationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_configuration" in value:
        import capo_chatbot.types.teams_channel_configuration

        out["channel_configuration"] = (
            capo_chatbot.types.teams_channel_configuration.redact_sensitive(
                value["channel_configuration"]
            )
        )
    return out
