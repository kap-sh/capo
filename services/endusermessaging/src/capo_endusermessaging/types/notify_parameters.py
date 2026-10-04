"""Generated from Smithy shape ``com.amazonaws.endusermessaging#NotifyParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.notify_template_id
    import capo_endusermessaging.types.voice_id


class NotifyParameters(TypedDict, closed=True):
    notify_template_id: NotRequired[
        "capo_endusermessaging.types.notify_template_id.NotifyTemplateId"
    ]
    """<p>The identifier of a preapproved notify template for the SMS or voice channels.</p>"""
    voice_id: NotRequired["capo_endusermessaging.types.voice_id.VoiceId"]
    """<p>The Amazon Polly voice ID used when the notify template is delivered over the voice channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyParameters) -> dict:
    out: dict = {}
    if "notify_template_id" in value:
        out["notifyTemplateId"] = value["notify_template_id"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> NotifyParameters:
    out: NotifyParameters = {}  # type: ignore[typeddict-item]
    if data.get("notifyTemplateId") is not None:
        out["notify_template_id"] = data["notifyTemplateId"]
    if data.get("voiceId") is not None:
        out["voice_id"] = data["voiceId"]
    return out
