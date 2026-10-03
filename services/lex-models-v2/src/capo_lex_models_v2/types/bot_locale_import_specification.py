"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleImportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_filler_settings
    import capo_lex_models_v2.types.confidence_threshold
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.speaker_diarization_settings
    import capo_lex_models_v2.types.speech_detection_sensitivity
    import capo_lex_models_v2.types.speech_recognition_settings
    import capo_lex_models_v2.types.unified_speech_settings
    import capo_lex_models_v2.types.voice_settings


class BotLocaleImportSpecification(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to import the locale to.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to import the locale to. This can only be the <code>DRAFT</code> version of the bot.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""
    nlu_intent_confidence_threshold: NotRequired[
        "capo_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>Determines the threshold where Amazon Lex will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot. </p> <p>For example, suppose a bot is configured with the confidence threshold of 0.80 and the <code>AMAZON.FallbackIntent</code>. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the <code>PostText</code> operation would be:</p> <ul> <li> <p> <code>AMAZON.FallbackIntent</code> </p> </li> <li> <p> <code>IntentA</code> </p> </li> <li> <p> <code>IntentB</code> </p> </li> <li> <p> <code>IntentC</code> </p> </li> </ul>"""
    voice_settings: NotRequired["capo_lex_models_v2.types.voice_settings.VoiceSettings"]
    speech_recognition_settings: NotRequired[
        "capo_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>Speech-to-text settings to apply when importing the bot locale configuration.</p>"""
    speech_detection_sensitivity: NotRequired[
        "capo_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>"""
    unified_speech_settings: NotRequired[
        "capo_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>Unified speech settings to apply when importing the bot locale configuration.</p>"""
    audio_filler_settings: NotRequired[
        "capo_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>Audio filler settings to apply when importing the bot locale configuration. Audio filler requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be enabled when <code>enabled</code> is <code>true</code>.</p>"""
    speaker_diarization_settings: NotRequired[
        "capo_lex_models_v2.types.speaker_diarization_settings.SpeakerDiarizationSettings"
    ]
    """<p>The speaker diarization settings to apply when importing the bot locale configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleImportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    if "nlu_intent_confidence_threshold" in value:
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
    if "speech_recognition_settings" in value:
        import capo_lex_models_v2.types.speech_recognition_settings

        out["speechRecognitionSettings"] = (
            capo_lex_models_v2.types.speech_recognition_settings.serialize_json(
                value["speech_recognition_settings"]
            )
        )
    if "speech_detection_sensitivity" in value:
        import capo_lex_models_v2.types.speech_detection_sensitivity

        out["speechDetectionSensitivity"] = (
            capo_lex_models_v2.types.speech_detection_sensitivity.serialize_json(
                value["speech_detection_sensitivity"]
            )
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
    if "speaker_diarization_settings" in value:
        import capo_lex_models_v2.types.speaker_diarization_settings

        out["speakerDiarizationSettings"] = (
            capo_lex_models_v2.types.speaker_diarization_settings.serialize_json(
                value["speaker_diarization_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BotLocaleImportSpecification:
    out: BotLocaleImportSpecification = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("BotLocaleImportSpecification.bot_id required")
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError("BotLocaleImportSpecification.bot_version required")
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError("BotLocaleImportSpecification.locale_id required")
    if data.get("nluIntentConfidenceThreshold") is not None:
        out["nlu_intent_confidence_threshold"] = float(
            data["nluIntentConfidenceThreshold"]
        )
    if data.get("voiceSettings") is not None:
        import capo_lex_models_v2.types.voice_settings

        out["voice_settings"] = (
            capo_lex_models_v2.types.voice_settings.deserialize_json(
                data["voiceSettings"]
            )
        )
    if data.get("speechRecognitionSettings") is not None:
        import capo_lex_models_v2.types.speech_recognition_settings

        out["speech_recognition_settings"] = (
            capo_lex_models_v2.types.speech_recognition_settings.deserialize_json(
                data["speechRecognitionSettings"]
            )
        )
    if data.get("speechDetectionSensitivity") is not None:
        import capo_lex_models_v2.types.speech_detection_sensitivity

        out["speech_detection_sensitivity"] = (
            capo_lex_models_v2.types.speech_detection_sensitivity.deserialize_json(
                data["speechDetectionSensitivity"]
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
    if data.get("speakerDiarizationSettings") is not None:
        import capo_lex_models_v2.types.speaker_diarization_settings

        out["speaker_diarization_settings"] = (
            capo_lex_models_v2.types.speaker_diarization_settings.deserialize_json(
                data["speakerDiarizationSettings"]
            )
        )
    return out
