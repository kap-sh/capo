"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateChannelParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.update_notify_parameters
    import capo_endusermessaging.types.update_text_parameters
    import capo_endusermessaging.types.update_voice_parameters
    import capo_endusermessaging.types.update_whats_app_parameters


class UpdateChannelParameters(TypedDict, closed=True):
    text: NotRequired[
        "capo_endusermessaging.types.update_text_parameters.UpdateTextParameters"
    ]
    """<p>The text-channel parameters to update. Omit this member to leave the text-channel parameters unchanged.</p>"""
    voice: NotRequired[
        "capo_endusermessaging.types.update_voice_parameters.UpdateVoiceParameters"
    ]
    """<p>The voice-channel parameters to update. Omit this member to leave the voice-channel parameters unchanged.</p>"""
    notify: NotRequired[
        "capo_endusermessaging.types.update_notify_parameters.UpdateNotifyParameters"
    ]
    """<p>The notify-template-route parameters to update. Omit this member to leave them unchanged.</p>"""
    whats_app: NotRequired[
        "capo_endusermessaging.types.update_whats_app_parameters.UpdateWhatsAppParameters"
    ]
    """<p>The WhatsApp-channel parameters to update. Omit this member to leave the WhatsApp-channel parameters unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelParameters) -> dict:
    out: dict = {}
    if "text" in value:
        import capo_endusermessaging.types.update_text_parameters

        out["text"] = capo_endusermessaging.types.update_text_parameters.serialize_json(
            value["text"]
        )
    if "voice" in value:
        import capo_endusermessaging.types.update_voice_parameters

        out["voice"] = (
            capo_endusermessaging.types.update_voice_parameters.serialize_json(
                value["voice"]
            )
        )
    if "notify" in value:
        import capo_endusermessaging.types.update_notify_parameters

        out["notify"] = (
            capo_endusermessaging.types.update_notify_parameters.serialize_json(
                value["notify"]
            )
        )
    if "whats_app" in value:
        import capo_endusermessaging.types.update_whats_app_parameters

        out["whatsApp"] = (
            capo_endusermessaging.types.update_whats_app_parameters.serialize_json(
                value["whats_app"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelParameters:
    out: UpdateChannelParameters = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        import capo_endusermessaging.types.update_text_parameters

        out["text"] = (
            capo_endusermessaging.types.update_text_parameters.deserialize_json(
                data["text"]
            )
        )
    if data.get("voice") is not None:
        import capo_endusermessaging.types.update_voice_parameters

        out["voice"] = (
            capo_endusermessaging.types.update_voice_parameters.deserialize_json(
                data["voice"]
            )
        )
    if data.get("notify") is not None:
        import capo_endusermessaging.types.update_notify_parameters

        out["notify"] = (
            capo_endusermessaging.types.update_notify_parameters.deserialize_json(
                data["notify"]
            )
        )
    if data.get("whatsApp") is not None:
        import capo_endusermessaging.types.update_whats_app_parameters

        out["whats_app"] = (
            capo_endusermessaging.types.update_whats_app_parameters.deserialize_json(
                data["whatsApp"]
            )
        )
    return out
