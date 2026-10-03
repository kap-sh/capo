"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotLocaleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_filler_settings
    import capo_lex_models_v2.types.confidence_threshold
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.generative_ai_settings
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.speaker_diarization_settings
    import capo_lex_models_v2.types.speech_detection_sensitivity
    import capo_lex_models_v2.types.speech_recognition_settings
    import capo_lex_models_v2.types.unified_speech_settings
    import capo_lex_models_v2.types.voice_settings


class UpdateBotLocaleRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that contains the locale.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot that contains the locale to be updated. The version can only be the <code>DRAFT</code> version.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The new description of the locale.</p>"""
    nlu_intent_confidence_threshold: (
        "capo_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    )
    """<p>The new confidence threshold where Amazon Lex inserts the <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> intents in the list of possible intents for an utterance.</p>"""
    voice_settings: NotRequired["capo_lex_models_v2.types.voice_settings.VoiceSettings"]
    """<p>The new Amazon Polly voice Amazon Lex should use for voice interaction with the user.</p>"""
    unified_speech_settings: NotRequired[
        "capo_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>Updated unified speech settings to apply to the bot locale.</p>"""
    audio_filler_settings: NotRequired[
        "capo_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>Updated audio filler settings to apply to the bot locale. When enabled, requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be configured on the bot locale.</p>"""
    speech_recognition_settings: NotRequired[
        "capo_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>Updated speech-to-text settings to apply to the bot locale.</p>"""
    generative_ai_settings: NotRequired[
        "capo_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
    ]
    """<p>Contains settings for generative AI features powered by Amazon Bedrock for your bot locale. Use this object to turn generative AI features on and off. Pricing may differ if you turn a feature on. For more information, see LINK.</p>"""
    speech_detection_sensitivity: NotRequired[
        "capo_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The new sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>"""
    speaker_diarization_settings: NotRequired[
        "capo_lex_models_v2.types.speaker_diarization_settings.SpeakerDiarizationSettings"
    ]
    """<p>The updated speaker diarization settings to apply to the bot locale. If you omit this field, Amazon Lex keeps the setting currently stored on the bot locale. To turn speaker diarization off, set <code>enabled</code> to <code>false</code> explicitly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotLocaleRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["nluIntentConfidenceThreshold"] = (
        "NaN"
        if value["nlu_intent_confidence_threshold"]
        != value["nlu_intent_confidence_threshold"]
        else "Infinity"
        if value["nlu_intent_confidence_threshold"] == float("inf")
        else "-Infinity"
        if value["nlu_intent_confidence_threshold"] == float("-inf")
        else value["nlu_intent_confidence_threshold"]
    )
    if "voice_settings" in value:
        import capo_lex_models_v2.types.voice_settings

        out["voiceSettings"] = capo_lex_models_v2.types.voice_settings.serialize_json(
            value["voice_settings"]
        )
    if "unified_speech_settings" in value:
        import capo_lex_models_v2.types.unified_speech_settings

        out["unifiedSpeechSettings"] = (
            capo_lex_models_v2.types.unified_speech_settings.serialize_json(
                value["unified_speech_settings"]
            )
        )
    if "audio_filler_settings" in value:
        import capo_lex_models_v2.types.audio_filler_settings

        out["audioFillerSettings"] = (
            capo_lex_models_v2.types.audio_filler_settings.serialize_json(
                value["audio_filler_settings"]
            )
        )
    if "speech_recognition_settings" in value:
        import capo_lex_models_v2.types.speech_recognition_settings

        out["speechRecognitionSettings"] = (
            capo_lex_models_v2.types.speech_recognition_settings.serialize_json(
                value["speech_recognition_settings"]
            )
        )
    if "generative_ai_settings" in value:
        import capo_lex_models_v2.types.generative_ai_settings

        out["generativeAISettings"] = (
            capo_lex_models_v2.types.generative_ai_settings.serialize_json(
                value["generative_ai_settings"]
            )
        )
    if "speech_detection_sensitivity" in value:
        import capo_lex_models_v2.types.speech_detection_sensitivity

        out["speechDetectionSensitivity"] = (
            capo_lex_models_v2.types.speech_detection_sensitivity.serialize_json(
                value["speech_detection_sensitivity"]
            )
        )
    if "speaker_diarization_settings" in value:
        import capo_lex_models_v2.types.speaker_diarization_settings

        out["speakerDiarizationSettings"] = (
            capo_lex_models_v2.types.speaker_diarization_settings.serialize_json(
                value["speaker_diarization_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBotLocaleRequest:
    out: UpdateBotLocaleRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nluIntentConfidenceThreshold") is not None:
        out["nlu_intent_confidence_threshold"] = float(
            data["nluIntentConfidenceThreshold"]
        )
    else:
        raise DeserializationError(
            "UpdateBotLocaleRequest.nlu_intent_confidence_threshold required"
        )
    if data.get("voiceSettings") is not None:
        import capo_lex_models_v2.types.voice_settings

        out["voice_settings"] = (
            capo_lex_models_v2.types.voice_settings.deserialize_json(
                data["voiceSettings"]
            )
        )
    if data.get("unifiedSpeechSettings") is not None:
        import capo_lex_models_v2.types.unified_speech_settings

        out["unified_speech_settings"] = (
            capo_lex_models_v2.types.unified_speech_settings.deserialize_json(
                data["unifiedSpeechSettings"]
            )
        )
    if data.get("audioFillerSettings") is not None:
        import capo_lex_models_v2.types.audio_filler_settings

        out["audio_filler_settings"] = (
            capo_lex_models_v2.types.audio_filler_settings.deserialize_json(
                data["audioFillerSettings"]
            )
        )
    if data.get("speechRecognitionSettings") is not None:
        import capo_lex_models_v2.types.speech_recognition_settings

        out["speech_recognition_settings"] = (
            capo_lex_models_v2.types.speech_recognition_settings.deserialize_json(
                data["speechRecognitionSettings"]
            )
        )
    if data.get("generativeAISettings") is not None:
        import capo_lex_models_v2.types.generative_ai_settings

        out["generative_ai_settings"] = (
            capo_lex_models_v2.types.generative_ai_settings.deserialize_json(
                data["generativeAISettings"]
            )
        )
    if data.get("speechDetectionSensitivity") is not None:
        import capo_lex_models_v2.types.speech_detection_sensitivity

        out["speech_detection_sensitivity"] = (
            capo_lex_models_v2.types.speech_detection_sensitivity.deserialize_json(
                data["speechDetectionSensitivity"]
            )
        )
    if data.get("speakerDiarizationSettings") is not None:
        import capo_lex_models_v2.types.speaker_diarization_settings

        out["speaker_diarization_settings"] = (
            capo_lex_models_v2.types.speaker_diarization_settings.deserialize_json(
                data["speakerDiarizationSettings"]
            )
        )
    return out
