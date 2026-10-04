"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ChannelParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_parameters
    import capo_endusermessaging.types.text_parameters
    import capo_endusermessaging.types.voice_parameters
    import capo_endusermessaging.types.whats_app_parameters


class ChannelParameters(TypedDict, closed=True):
    text: NotRequired["capo_endusermessaging.types.text_parameters.TextParameters"]
    """<p>The parameters for the text channel, which delivers over SMS or RCS.</p>"""
    voice: NotRequired["capo_endusermessaging.types.voice_parameters.VoiceParameters"]
    """<p>The parameters for the voice channel.</p>"""
    notify: NotRequired[
        "capo_endusermessaging.types.notify_parameters.NotifyParameters"
    ]
    """<p>The parameters for the preapproved notify-template route over the SMS or voice channels.</p>"""
    whats_app: NotRequired[
        "capo_endusermessaging.types.whats_app_parameters.WhatsAppParameters"
    ]
    """<p>The parameters for the WhatsApp channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelParameters) -> dict:
    out: dict = {}
    if "text" in value:
        import capo_endusermessaging.types.text_parameters

        out["text"] = capo_endusermessaging.types.text_parameters.serialize_json(
            value["text"]
        )
    if "voice" in value:
        import capo_endusermessaging.types.voice_parameters

        out["voice"] = capo_endusermessaging.types.voice_parameters.serialize_json(
            value["voice"]
        )
    if "notify" in value:
        import capo_endusermessaging.types.notify_parameters

        out["notify"] = capo_endusermessaging.types.notify_parameters.serialize_json(
            value["notify"]
        )
    if "whats_app" in value:
        import capo_endusermessaging.types.whats_app_parameters

        out["whatsApp"] = (
            capo_endusermessaging.types.whats_app_parameters.serialize_json(
                value["whats_app"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelParameters:
    out: ChannelParameters = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        import capo_endusermessaging.types.text_parameters

        out["text"] = capo_endusermessaging.types.text_parameters.deserialize_json(
            data["text"]
        )
    if data.get("voice") is not None:
        import capo_endusermessaging.types.voice_parameters

        out["voice"] = capo_endusermessaging.types.voice_parameters.deserialize_json(
            data["voice"]
        )
    if data.get("notify") is not None:
        import capo_endusermessaging.types.notify_parameters

        out["notify"] = capo_endusermessaging.types.notify_parameters.deserialize_json(
            data["notify"]
        )
    if data.get("whatsApp") is not None:
        import capo_endusermessaging.types.whats_app_parameters

        out["whats_app"] = (
            capo_endusermessaging.types.whats_app_parameters.deserialize_json(
                data["whatsApp"]
            )
        )
    return out
