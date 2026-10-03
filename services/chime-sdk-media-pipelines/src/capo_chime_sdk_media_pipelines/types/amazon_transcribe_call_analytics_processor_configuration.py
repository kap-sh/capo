"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AmazonTranscribeCallAnalyticsProcessorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.boolean
    import capo_chime_sdk_media_pipelines.types.call_analytics_language_code
    import capo_chime_sdk_media_pipelines.types.category_name_list
    import capo_chime_sdk_media_pipelines.types.content_type
    import capo_chime_sdk_media_pipelines.types.model_name
    import capo_chime_sdk_media_pipelines.types.partial_results_stability
    import capo_chime_sdk_media_pipelines.types.pii_entity_types
    import capo_chime_sdk_media_pipelines.types.post_call_analytics_settings
    import capo_chime_sdk_media_pipelines.types.vocabulary_filter_method
    import capo_chime_sdk_media_pipelines.types.vocabulary_filter_name
    import capo_chime_sdk_media_pipelines.types.vocabulary_name


class AmazonTranscribeCallAnalyticsProcessorConfiguration(TypedDict, closed=True):
    language_code: "capo_chime_sdk_media_pipelines.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    """<p>The language code in the configuration.</p>"""
    vocabulary_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_name.VocabularyName"
    ]
    """<p>Specifies the name of the custom vocabulary to use when processing a transcription. Note that vocabulary names are case sensitive.</p> <p>If the language of the specified custom vocabulary doesn't match the language identified in your media, the custom vocabulary is not applied to your transcription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a> in the <i>Amazon Transcribe Developer Guide</i>.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 200. </p>"""
    vocabulary_filter_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>Specifies the name of the custom vocabulary filter to use when processing a transcription. Note that vocabulary filter names are case sensitive.</p> <p>If the language of the specified custom vocabulary filter doesn't match the language identified in your media, the vocabulary filter is not applied to your transcription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a> in the <i>Amazon Transcribe Developer Guide</i>.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 200. </p>"""
    vocabulary_filter_method: NotRequired[
        "capo_chime_sdk_media_pipelines.types.vocabulary_filter_method.VocabularyFilterMethod"
    ]
    """<p>Specifies how to apply a vocabulary filter to a transcript.</p> <p>To replace words with <b>***</b>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>. </p>"""
    language_model_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.model_name.ModelName"
    ]
    """<p>Specifies the name of the custom language model to use when processing a transcription. Note that language model names are case sensitive.</p> <p>The language of the specified language model must match the language code specified in the transcription request. If the languages don't match, the custom language model isn't applied. Language mismatches don't generate errors or warnings.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html">Custom language models</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    enable_partial_results_stabilization: (
        "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    )
    """<p>Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    partial_results_stability: NotRequired[
        "capo_chime_sdk_media_pipelines.types.partial_results_stability.PartialResultsStability"
    ]
    """<p>Specifies the level of stability to use when you enable partial results stabilization (<code>EnablePartialResultsStabilization</code>).</p> <p>Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    content_identification_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.content_type.ContentType"
    ]
    """<p>Labels all personally identifiable information (PII) identified in your transcript.</p> <p>Content identification is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is flagged upon complete transcription of an audio segment.</p> <p>You can’t set <code>ContentIdentificationType</code> and <code>ContentRedactionType</code> in the same request. If you do, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    content_redaction_type: NotRequired[
        "capo_chime_sdk_media_pipelines.types.content_type.ContentType"
    ]
    """<p>Redacts all personally identifiable information (PII) identified in your transcript.</p> <p>Content redaction is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is redacted upon complete transcription of an audio segment.</p> <p>You can’t set <code>ContentRedactionType</code> and <code>ContentIdentificationType</code> in the same request. If you do, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    pii_entity_types: NotRequired[
        "capo_chime_sdk_media_pipelines.types.pii_entity_types.PiiEntityTypes"
    ]
    """<p>Specifies the types of personally identifiable information (PII) to redact from a transcript. You can include as many types as you'd like, or you can select <code>ALL</code>.</p> <p>To include <code>PiiEntityTypes</code> in your Call Analytics request, you must also include <code>ContentIdentificationType</code> or <code>ContentRedactionType</code>, but you can't include both. </p> <p>Values must be comma-separated and can include: <code>ADDRESS</code>, <code>BANK_ACCOUNT_NUMBER</code>, <code>BANK_ROUTING</code>, <code>CREDIT_DEBIT_CVV</code>, <code>CREDIT_DEBIT_EXPIRY</code>, <code>CREDIT_DEBIT_NUMBER</code>, <code>EMAIL</code>, <code>NAME</code>, <code>PHONE</code>, <code>PIN</code>, <code>SSN</code>, or <code>ALL</code>.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 300.</p>"""
    filter_partial_results: "capo_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>If true, <code>UtteranceEvents</code> with <code>IsPartial: true</code> are filtered out of the insights target.</p>"""
    post_call_analytics_settings: NotRequired[
        "capo_chime_sdk_media_pipelines.types.post_call_analytics_settings.PostCallAnalyticsSettings"
    ]
    """<p>The settings for a post-call analysis task in an analytics configuration.</p>"""
    call_analytics_stream_categories: NotRequired[
        "capo_chime_sdk_media_pipelines.types.category_name_list.CategoryNameList"
    ]
    """<p>By default, all <code>CategoryEvents</code> are sent to the insights target. If this parameter is specified, only included categories are sent to the insights target. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonTranscribeCallAnalyticsProcessorConfiguration) -> dict:
    out: dict = {}
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
    if "language_model_name" in value:
        out["LanguageModelName"] = value["language_model_name"]
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
    out["FilterPartialResults"] = value.get("filter_partial_results", False)
    if "post_call_analytics_settings" in value:
        import capo_chime_sdk_media_pipelines.types.post_call_analytics_settings

        out["PostCallAnalyticsSettings"] = (
            capo_chime_sdk_media_pipelines.types.post_call_analytics_settings.serialize_json(
                value["post_call_analytics_settings"]
            )
        )
    if "call_analytics_stream_categories" in value:
        import capo_chime_sdk_media_pipelines.types.category_name_list

        out["CallAnalyticsStreamCategories"] = (
            capo_chime_sdk_media_pipelines.types.category_name_list.serialize_json(
                value["call_analytics_stream_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> AmazonTranscribeCallAnalyticsProcessorConfiguration:
    out: AmazonTranscribeCallAnalyticsProcessorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LanguageCode") is not None:
        import capo_chime_sdk_media_pipelines.types.call_analytics_language_code

        out["language_code"] = (
            capo_chime_sdk_media_pipelines.types.call_analytics_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "AmazonTranscribeCallAnalyticsProcessorConfiguration.language_code required"
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
    if data.get("LanguageModelName") is not None:
        out["language_model_name"] = data["LanguageModelName"]
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
    if data.get("FilterPartialResults") is not None:
        out["filter_partial_results"] = data["FilterPartialResults"]
    else:
        out["filter_partial_results"] = False
    if data.get("PostCallAnalyticsSettings") is not None:
        import capo_chime_sdk_media_pipelines.types.post_call_analytics_settings

        out["post_call_analytics_settings"] = (
            capo_chime_sdk_media_pipelines.types.post_call_analytics_settings.deserialize_json(
                data["PostCallAnalyticsSettings"]
            )
        )
    if data.get("CallAnalyticsStreamCategories") is not None:
        import capo_chime_sdk_media_pipelines.types.category_name_list

        out["call_analytics_stream_categories"] = (
            capo_chime_sdk_media_pipelines.types.category_name_list.deserialize_json(
                data["CallAnalyticsStreamCategories"]
            )
        )
    return out
