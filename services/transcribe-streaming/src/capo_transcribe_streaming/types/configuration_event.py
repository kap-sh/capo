"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ConfigurationEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.channel_definitions
    import capo_transcribe_streaming.types.post_call_analytics_settings


class ConfigurationEvent(TypedDict, closed=True):
    channel_definitions: NotRequired[
        "capo_transcribe_streaming.types.channel_definitions.ChannelDefinitions"
    ]
    """<p>Indicates which speaker is on which audio channel.</p>"""
    post_call_analytics_settings: NotRequired[
        "capo_transcribe_streaming.types.post_call_analytics_settings.PostCallAnalyticsSettings"
    ]
    r"""<p>Provides additional optional settings for your Call Analytics post-call request, including encryption and output locations for your redacted transcript.</p> <p> <code>PostCallAnalyticsSettings</code> provides you with the same insights as a Call Analytics post-call transcription. Refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html\">Post-call analytics</a> for more information on this feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "channel_definitions" in value:
        import capo_transcribe_streaming.types.channel_definitions

        out["ChannelDefinitions"] = (
            capo_transcribe_streaming.types.channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "post_call_analytics_settings" in value:
        import capo_transcribe_streaming.types.post_call_analytics_settings

        out["PostCallAnalyticsSettings"] = (
            capo_transcribe_streaming.types.post_call_analytics_settings.serialize_json(
                value["post_call_analytics_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if data.get("ChannelDefinitions") is not None:
        import capo_transcribe_streaming.types.channel_definitions

        out["channel_definitions"] = (
            capo_transcribe_streaming.types.channel_definitions.deserialize_json(
                data["ChannelDefinitions"]
            )
        )
    if data.get("PostCallAnalyticsSettings") is not None:
        import capo_transcribe_streaming.types.post_call_analytics_settings

        out["post_call_analytics_settings"] = (
            capo_transcribe_streaming.types.post_call_analytics_settings.deserialize_json(
                data["PostCallAnalyticsSettings"]
            )
        )
    return out


def serialize_event_json(value: ConfigurationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ConfigurationEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConfigurationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
