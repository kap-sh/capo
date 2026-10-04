"""Generated from Smithy shape ``com.amazonaws.endusermessaging#VoiceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.inline_template_body
    import capo_endusermessaging.types.language_code
    import capo_endusermessaging.types.voice_id
    import capo_endusermessaging.types.voice_message_body_text_type


class VoiceParameters(TypedDict, closed=True):
    inline_template_body: NotRequired[
        "capo_endusermessaging.types.inline_template_body.InlineTemplateBody"
    ]
    """<p>The freeform message template used to render the one-time passcode for the voice channel. The template must contain the code placeholder.</p>"""
    language_code: NotRequired["capo_endusermessaging.types.language_code.LanguageCode"]
    """<p>The BCP 47 language code used to render the voice message.</p>"""
    voice_id: NotRequired["capo_endusermessaging.types.voice_id.VoiceId"]
    """<p>The Amazon Polly voice ID used for the voice channel.</p>"""
    voice_message_body_text_type: NotRequired[
        "capo_endusermessaging.types.voice_message_body_text_type.VoiceMessageBodyTextType"
    ]
    """<p>The format of the voice message body. Valid values are TEXT and SSML.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceParameters) -> dict:
    out: dict = {}
    if "inline_template_body" in value:
        out["inlineTemplateBody"] = value["inline_template_body"]
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "voice_id" in value:
        out["voiceId"] = value["voice_id"]
    if "voice_message_body_text_type" in value:
        import capo_endusermessaging.types.voice_message_body_text_type

        out["voiceMessageBodyTextType"] = (
            capo_endusermessaging.types.voice_message_body_text_type.serialize_json(
                value["voice_message_body_text_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceParameters:
    out: VoiceParameters = {}  # type: ignore[typeddict-item]
    if data.get("inlineTemplateBody") is not None:
        out["inline_template_body"] = data["inlineTemplateBody"]
    if data.get("languageCode") is not None:
        out["language_code"] = data["languageCode"]
    if data.get("voiceId") is not None:
        out["voice_id"] = data["voiceId"]
    if data.get("voiceMessageBodyTextType") is not None:
        import capo_endusermessaging.types.voice_message_body_text_type

        out["voice_message_body_text_type"] = (
            capo_endusermessaging.types.voice_message_body_text_type.deserialize_json(
                data["voiceMessageBodyTextType"]
            )
        )
    return out
