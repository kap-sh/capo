"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateVoiceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.update_inline_template_body
    import capo_endusermessaging.types.update_language_code
    import capo_endusermessaging.types.update_voice_id
    import capo_endusermessaging.types.voice_message_body_text_type


class UpdateVoiceParameters(TypedDict, closed=True):
    inline_template_body: NotRequired[
        "capo_endusermessaging.types.update_inline_template_body.UpdateInlineTemplateBody"
    ]
    """<p>The updated freeform voice template body. An empty string clears the previously stored value.</p>"""
    language_code: NotRequired[
        "capo_endusermessaging.types.update_language_code.UpdateLanguageCode"
    ]
    """<p>The updated BCP 47 language code. An empty string clears the previously stored value.</p>"""
    voice_id: NotRequired["capo_endusermessaging.types.update_voice_id.UpdateVoiceId"]
    """<p>The updated Amazon Polly voice ID. An empty string clears the previously stored value.</p>"""
    voice_message_body_text_type: NotRequired[
        "capo_endusermessaging.types.voice_message_body_text_type.VoiceMessageBodyTextType"
    ]
    """<p>The updated format of the voice message body. Valid values are TEXT and SSML. Omit this member to preserve the current value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceParameters) -> dict:
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


def deserialize_json(data: dict) -> UpdateVoiceParameters:
    out: UpdateVoiceParameters = {}  # type: ignore[typeddict-item]
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
