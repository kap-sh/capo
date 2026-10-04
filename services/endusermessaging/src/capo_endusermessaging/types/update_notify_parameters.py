"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateNotifyParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.update_notify_template_id
    import capo_endusermessaging.types.update_voice_id


class UpdateNotifyParameters(TypedDict, closed=True):
    notify_template_id: NotRequired[
        "capo_endusermessaging.types.update_notify_template_id.UpdateNotifyTemplateId"
    ]
    """<p>The updated identifier of a preapproved notify template for the SMS or voice channels. An empty string clears the previously stored value.</p>"""
    voice_id: NotRequired["capo_endusermessaging.types.update_voice_id.UpdateVoiceId"]
    """<p>The updated Amazon Polly voice ID. An empty string clears the previously stored value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotifyParameters) -> dict:
    out: dict = {}
    if "notify_template_id" in value:
        out["notifyTemplateId"] = value["notify_template_id"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    return out


def deserialize_json(data: dict) -> UpdateNotifyParameters:
    out: UpdateNotifyParameters = {}  # type: ignore[typeddict-item]
    if data.get("notifyTemplateId") is not None:
        out["notify_template_id"] = data["notifyTemplateId"]
    if data.get("voiceId") is not None:
        out["voice_id"] = data["voiceId"]
    return out
