"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotLocaleRequest``."""

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


class CreateBotLocaleRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to create the locale for.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to create the locale for. This can only be the draft version of the bot.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>A description of the bot locale. Use this to help identify the bot locale in lists.</p>"""
    nlu_intent_confidence_threshold: (
        "capo_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    )
    """<p>Determines the threshold where Amazon Lex will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot.</p> <p>For example, suppose a bot is configured with the confidence threshold of 0.80 and the <code>AMAZON.FallbackIntent</code>. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the <code>RecognizeText</code> operation would be:</p> <ul> <li> <p>AMAZON.FallbackIntent</p> </li> <li> <p>IntentA</p> </li> <li> <p>IntentB</p> </li> <li> <p>IntentC</p> </li> </ul>"""
    voice_settings: NotRequired["capo_lex_models_v2.types.voice_settings.VoiceSettings"]
    """<p>The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.</p>"""
    unified_speech_settings: NotRequired[
        "capo_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>Unified speech settings to configure for the new bot locale.</p>"""
    audio_filler_settings: NotRequired[
        "capo_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>Audio filler settings to configure for the new bot locale. When enabled, Amazon Lex plays a brief background audio filler during speech-to-speech interactions to mask processing delays. Requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be configured on the bot locale.</p>"""
    speech_recognition_settings: NotRequired[
        "capo_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>Speech-to-text settings to configure for the new bot locale.</p>"""
    generative_ai_settings: NotRequired[
        "capo_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
    ]
    speech_detection_sensitivity: NotRequired[
        "capo_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>"""
    speaker_diarization_settings: NotRequired[
        "capo_lex_models_v2.types.speaker_diarization_settings.SpeakerDiarizationSettings"
    ]
    """<p>The speaker diarization settings to configure for the new bot locale. When enabled, Amazon Lex restricts speech detection to the primary (loudest) speaker during streaming audio conversations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotLocaleRequest) -> dict:
    out: dict = {}
    out["localeId"] = value["locale_id"]
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


def deserialize_json(data: dict) -> CreateBotLocaleRequest:
    out: CreateBotLocaleRequest = {}  # type: ignore[typeddict-item]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError("CreateBotLocaleRequest.locale_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("nluIntentConfidenceThreshold") is not None:
        out["nlu_intent_confidence_threshold"] = float(
            data["nluIntentConfidenceThreshold"]
        )
    else:
        raise DeserializationError(
            "CreateBotLocaleRequest.nlu_intent_confidence_threshold required"
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
