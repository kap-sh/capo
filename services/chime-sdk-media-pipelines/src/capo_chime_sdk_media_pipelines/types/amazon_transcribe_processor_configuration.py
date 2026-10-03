"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AmazonTranscribeProcessorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.boolean
    import capo_chime_sdk_media_pipelines.types.call_analytics_language_code
    import capo_chime_sdk_media_pipelines.types.content_type
    import capo_chime_sdk_media_pipelines.types.language_options
    import capo_chime_sdk_media_pipelines.types.model_name
    import capo_chime_sdk_media_pipelines.types.partial_results_stability
    import capo_chime_sdk_media_pipelines.types.pii_entity_types
    import capo_chime_sdk_media_pipelines.types.vocabulary_filter_method
    import capo_chime_sdk_media_pipelines.types.vocabulary_filter_name
    import capo_chime_sdk_media_pipelines.types.vocabulary_filter_names
    import capo_chime_sdk_media_pipelines.types.vocabulary_name
    import capo_chime_sdk_media_pipelines.types.vocabulary_names


class AmazonTranscribeProcessorConfiguration(TypedDict, closed=True):
    language_code: NotRequired[
        "capo_chime_sdk_media_pipelines.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>The language code that represents the language spoken in your audio.</p> <p>If you're unsure of the language spoken in your audio, consider using <code>IdentifyLanguage</code> to enable automatic language identification.</p> <p>For a list of languages that real-time Call Analytics supports, see the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages table</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    vocabulary_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_name.VocabularyName"
    ]
    """<p>The name of the custom vocabulary that you specified in your Call Analytics request.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 200.</p>"""
    vocabulary_filter_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the custom vocabulary filter that you specified in your Call Analytics request.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 200.</p>"""
    vocabulary_filter_method: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_filter_method.VocabularyFilterMethod"
    ]
    """<p>The vocabulary filtering method used in your Call Analytics transcription.</p>"""
    show_speaker_label: "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html">Partitioning speakers (diarization)</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    enable_partial_results_stabilization: (
        "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    )
    """<p>Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    partial_results_stability: NotRequired[
        "capo_chime_sdk_media_pipelines.types.partial_results_stability.PartialResultsStability"
    ]
    """<p>The level of stability to use when you enable partial results stabilization (<code>EnablePartialResultsStabilization</code>).</p> <p>Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    content_identification_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.content_type.ContentType"
    ]
    """<p>Labels all personally identifiable information (PII) identified in your transcript.</p> <p>Content identification is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is flagged upon complete transcription of an audio segment.</p> <p>You can’t set <code>ContentIdentificationType</code> and <code>ContentRedactionType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    content_redaction_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.content_type.ContentType"
    ]
    """<p>Redacts all personally identifiable information (PII) identified in your transcript.</p> <p>Content redaction is performed at the segment level; PII specified in PiiEntityTypes is redacted upon complete transcription of an audio segment.</p> <p>You can’t set ContentRedactionType and ContentIdentificationType in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    pii_entity_types: NotRequired[
        "capo_chime_sdk_media_pipelines.types.pii_entity_types.PiiEntityTypes"
    ]
    """<p>The types of personally identifiable information (PII) to redact from a transcript. You can include as many types as you'd like, or you can select <code>ALL</code>.</p> <p>To include <code>PiiEntityTypes</code> in your Call Analytics request, you must also include <code>ContentIdentificationType</code> or <code>ContentRedactionType</code>, but you can't include both.</p> <p>Values must be comma-separated and can include: <code>ADDRESS</code>, <code>BANK_ACCOUNT_NUMBER</code>, <code>BANK_ROUTING</code>, <code>CREDIT_DEBIT_CVV</code>, <code>CREDIT_DEBIT_EXPIRY</code>, <code>CREDIT_DEBIT_NUMBER</code>, <code>EMAIL</code>, <code>NAME</code>, <code>PHONE</code>, <code>PIN</code>, <code>SSN</code>, or <code>ALL</code>.</p> <p>If you leave this parameter empty, the default behavior is equivalent to <code>ALL</code>.</p>"""
    language_model_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.model_name.ModelName"
    ]
    """<p>The name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.</p> <p>The language of the specified language model must match the language code you specify in your transcription request. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html">Custom language models</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    filter_partial_results: "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>If true, <code>TranscriptEvents</code> with <code>IsPartial: true</code> are filtered out of the insights target.</p>"""
    identify_language: "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>Turns language identification on or off.</p>"""
    identify_multiple_languages: "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>Turns language identification on or off for multiple languages.</p> <note> <p>Calls to this API must include a <code>LanguageCode</code>, <code>IdentifyLanguage</code>, or <code>IdentifyMultipleLanguages</code> parameter. If you include more than one of those parameters, your transcription job fails.</p> </note>"""
    language_options: NotRequired[
        "capo_chime_sdk_media_pipelines.types.language_options.LanguageOptions"
    ]
    """<p>The language options for the transcription, such as automatic language detection.</p>"""
    preferred_language: NotRequired[
        "capo_chime_sdk_media_pipelines.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>The preferred language for the transcription.</p>"""
    vocabulary_names: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_names.VocabularyNames"
    ]
    """<p>The names of the custom vocabulary or vocabularies used during transcription.</p>"""
    vocabulary_filter_names: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_filter_names.VocabularyFilterNames"
    ]
    """<p>The names of the custom vocabulary filter or filters using during transcription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonTranscribeProcessorConfiguration) -> dict:
    out: dict = {}
    if "language_code" in value:
        import capo_chime_sdk_media_pipelines.types.call_analytics_language_code

        out["LanguageCode"] = (
            capo_chime_sdk_media_pipelines.types.call_analytics_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "vocabulary_filter_method" in value:
        import capo_chime_sdk_media_pipelines.types.vocabulary_filter_method

        out["VocabularyFilterMethod"] = (
            capo_chime_sdk_media_pipelines.types.vocabulary_filter_method.serialize_json(
                value["vocabulary_filter_method"]
            )
        )
    out["ShowSpeakerLabel"] = value.get("show_speaker_label", False)
    out["EnablePartialResultsStabilization"] = value.get(
        "enable_partial_results_stabilization", False
    )
    if "partial_results_stability" in value:
        import capo_chime_sdk_media_pipelines.types.partial_results_stability

        out["PartialResultsStability"] = (
            capo_chime_sdk_media_pipelines.types.partial_results_stability.serialize_json(
                value["partial_results_stability"]
            )
        )
    if "content_identification_type" in value:
        import capo_chime_sdk_media_pipelines.types.content_type

        out["ContentIdentificationType"] = (
            capo_chime_sdk_media_pipelines.types.content_type.serialize_json(
                value["content_identification_type"]
            )
        )
    if "content_redaction_type" in value:
        import capo_chime_sdk_media_pipelines.types.content_type

        out["ContentRedactionType"] = (
            capo_chime_sdk_media_pipelines.types.content_type.serialize_json(
                value["content_redaction_type"]
            )
        )
    if "pii_entity_types" in value:
        out["PiiEntityTypes"] = value["pii_entity_types"]
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
    out["FilterPartialResults"] = value.get("filter_partial_results", False)
    out["IdentifyLanguage"] = value.get("identify_language", False)
    out["IdentifyMultipleLanguages"] = value.get("identify_multiple_languages", False)
    if "language_options" in value:
        out["LanguageOptions"] = value["language_options"]
    if "preferred_language" in value:
        import capo_chime_sdk_media_pipelines.types.call_analytics_language_code

        out["PreferredLanguage"] = (
            capo_chime_sdk_media_pipelines.types.call_analytics_language_code.serialize_json(
                value["preferred_language"]
            )
        )
    if "vocabulary_names" in value:
        out["VocabularyNames"] = value["vocabulary_names"]
    if "vocabulary_filter_names" in value:
        out["VocabularyFilterNames"] = value["vocabulary_filter_names"]
    return out


def deserialize_json(data: dict) -> AmazonTranscribeProcessorConfiguration:
    out: AmazonTranscribeProcessorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_chime_sdk_media_pipelines.types.call_analytics_language_code

        out["language_code"] = (
            capo_chime_sdk_media_pipelines.types.call_analytics_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if data.get("VocabularyName") is not None:
        out["vocabulary_name"] = data["VocabularyName"]
    if data.get("VocabularyFilterName") is not None:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if data.get("VocabularyFilterMethod") is not None:
        import capo_chime_sdk_media_pipelines.types.vocabulary_filter_method

        out["vocabulary_filter_method"] = (
            capo_chime_sdk_media_pipelines.types.vocabulary_filter_method.deserialize_json(
                data["VocabularyFilterMethod"]
            )
        )
    if data.get("ShowSpeakerLabel") is not None:
        out["show_speaker_label"] = data["ShowSpeakerLabel"]
    else:
        out["show_speaker_label"] = False
    if data.get("EnablePartialResultsStabilization") is not None:
        out["enable_partial_results_stabilization"] = data[
            "EnablePartialResultsStabilization"
        ]
    else:
        out["enable_partial_results_stabilization"] = False
    if data.get("PartialResultsStability") is not None:
        import capo_chime_sdk_media_pipelines.types.partial_results_stability

        out["partial_results_stability"] = (
            capo_chime_sdk_media_pipelines.types.partial_results_stability.deserialize_json(
                data["PartialResultsStability"]
            )
        )
    if data.get("ContentIdentificationType") is not None:
        import capo_chime_sdk_media_pipelines.types.content_type

        out["content_identification_type"] = (
            capo_chime_sdk_media_pipelines.types.content_type.deserialize_json(
                data["ContentIdentificationType"]
            )
        )
    if data.get("ContentRedactionType") is not None:
        import capo_chime_sdk_media_pipelines.types.content_type

        out["content_redaction_type"] = (
            capo_chime_sdk_media_pipelines.types.content_type.deserialize_json(
                data["ContentRedactionType"]
            )
        )
    if data.get("PiiEntityTypes") is not None:
        out["pii_entity_types"] = data["PiiEntityTypes"]
    if data.get("LanguageModelName") is not None:
        out["language_model_name"] = data["LanguageModelName"]
    if data.get("FilterPartialResults") is not None:
        out["filter_partial_results"] = data["FilterPartialResults"]
    else:
        out["filter_partial_results"] = False
    if data.get("IdentifyLanguage") is not None:
        out["identify_language"] = data["IdentifyLanguage"]
    else:
        out["identify_language"] = False
    if data.get("IdentifyMultipleLanguages") is not None:
        out["identify_multiple_languages"] = data["IdentifyMultipleLanguages"]
    else:
        out["identify_multiple_languages"] = False
    if data.get("LanguageOptions") is not None:
        out["language_options"] = data["LanguageOptions"]
    if data.get("PreferredLanguage") is not None:
        import capo_chime_sdk_media_pipelines.types.call_analytics_language_code

        out["preferred_language"] = (
            capo_chime_sdk_media_pipelines.types.call_analytics_language_code.deserialize_json(
                data["PreferredLanguage"]
            )
        )
    if data.get("VocabularyNames") is not None:
        out["vocabulary_names"] = data["VocabularyNames"]
    if data.get("VocabularyFilterNames") is not None:
        out["vocabulary_filter_names"] = data["VocabularyFilterNames"]
    return out
