"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateSlackChannelConfigurationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chatbot.types.slack_channel_configuration


class UpdateSlackChannelConfigurationResult(TypedDict, closed=True):
    channel_configuration: NotRequired[
        "capo_chatbot.types.slack_channel_configuration.SlackChannelConfiguration"
    ]
    """<p>The configuration for a Slack channel configured with AWS Chatbot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSlackChannelConfigurationResult) -> dict:
    out: dict = {}
    if "channel_configuration" in value:
        import capo_chatbot.types.slack_channel_configuration

        out["ChannelConfiguration"] = (
            capo_chatbot.types.slack_channel_configuration.serialize_json(
                value["channel_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSlackChannelConfigurationResult:
    out: UpdateSlackChannelConfigurationResult = {}  # type: ignore[typeddict-item]
    if data.get("ChannelConfiguration") is not None:
        import capo_chatbot.types.slack_channel_configuration

        out["channel_configuration"] = (
            capo_chatbot.types.slack_channel_configuration.deserialize_json(
                data["ChannelConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateSlackChannelConfigurationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channel_configuration" in value:
        import capo_chatbot.types.slack_channel_configuration

        out["channel_configuration"] = (
            capo_chatbot.types.slack_channel_configuration.redact_sensitive(
                value["channel_configuration"]
            )
        )
    return out
