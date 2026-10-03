"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#StartCallAnalyticsStreamTranscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.audio_stream
    import capo_transcribe_streaming.types.boolean
    import capo_transcribe_streaming.types.call_analytics_language_code
    import capo_transcribe_streaming.types.content_identification_type
    import capo_transcribe_streaming.types.content_redaction_type
    import capo_transcribe_streaming.types.language_options
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.media_sample_rate_hertz
    import capo_transcribe_streaming.types.model_name
    import capo_transcribe_streaming.types.partial_results_stability
    import capo_transcribe_streaming.types.pii_entity_types
    import capo_transcribe_streaming.types.session_id
    import capo_transcribe_streaming.types.vocabulary_filter_method
    import capo_transcribe_streaming.types.vocabulary_filter_name
    import capo_transcribe_streaming.types.vocabulary_filter_names
    import capo_transcribe_streaming.types.vocabulary_name
    import capo_transcribe_streaming.types.vocabulary_names


class StartCallAnalyticsStreamTranscriptionRequest(TypedDict, closed=True):
    language_code: NotRequired[
        "capo_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>Specify the language code that represents the language spoken in your audio.</p> <p>For a list of languages supported with real-time Call Analytics, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>"""
    media_sample_rate_hertz: (
        "capo_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz"
    )
    """<p>The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.</p>"""
    media_encoding: "capo_transcribe_streaming.types.media_encoding.MediaEncoding"
    """<p>Specify the encoding of your input audio. Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV)</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a>.</p>"""
    vocabulary_name: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
    ]
    """<p>Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p> <p>If the language of the specified custom vocabulary doesn't match the language identified in your media, the custom vocabulary is not applied to your transcription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>"""
    session_id: NotRequired["capo_transcribe_streaming.types.session_id.SessionId"]
    """<p>Specify a name for your Call Analytics transcription session. If you don't include this parameter in your request, Amazon Transcribe generates an ID and returns it in the response.</p>"""
    audio_stream: "capo_transcribe_streaming.types.audio_stream.AudioStream"
    """<p>An encoded stream of audio blobs. Audio streams are encoded as either HTTP/2 or WebSocket data frames.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html">Transcribing streaming audio</a>.</p>"""
    vocabulary_filter_name: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>Specify the name of the custom vocabulary filter that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive.</p> <p>If the language of the specified custom vocabulary filter doesn't match the language identified in your media, the vocabulary filter is not applied to your transcription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a>.</p>"""
    vocabulary_filter_method: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_filter_method.VocabularyFilterMethod"
    ]
    """<p>Specify how you want your vocabulary filter applied to your transcript.</p> <p>To replace words with <code>***</code>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>.</p>"""
    language_model_name: NotRequired[
        "capo_transcribe_streaming.types.model_name.ModelName"
    ]
    """<p>Specify the name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.</p> <p>The language of the specified language model must match the language code you specify in your transcription request. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html">Custom language models</a>.</p>"""
    identify_language: "capo_transcribe_streaming.types.boolean.Boolean"
    """<p>Enables automatic language identification for your Call Analytics transcription.</p> <p>If you include <code>IdentifyLanguage</code>, you must include a list of language codes, using <code>LanguageOptions</code>, that you think may be present in your audio stream. You must provide a minimum of two language selections.</p> <p>You can also include a preferred language using <code>PreferredLanguage</code>. Adding a preferred language can help Amazon Transcribe identify the language faster than if you omit this parameter.</p> <p>Note that you must include either <code>LanguageCode</code> or <code>IdentifyLanguage</code> in your request. If you include both parameters, your transcription job fails.</p>"""
    language_options: NotRequired[
        "capo_transcribe_streaming.types.language_options.LanguageOptions"
    ]
    """<p>Specify two or more language codes that represent the languages you think may be present in your media.</p> <p>Including language options can improve the accuracy of language identification.</p> <p>If you include <code>LanguageOptions</code> in your request, you must also include <code>IdentifyLanguage</code>.</p> <p>For a list of languages supported with Call Analytics streaming, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p> <important> <p>You can only include one language dialect per language per stream. For example, you cannot include <code>en-US</code> and <code>en-AU</code> in the same request.</p> </important>"""
    preferred_language: NotRequired[
        "capo_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
    ]
    """<p>Specify a preferred language from the subset of languages codes you specified in <code>LanguageOptions</code>.</p> <p>You can only use this parameter if you've included <code>IdentifyLanguage</code> and <code>LanguageOptions</code> in your request.</p>"""
    vocabulary_names: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_names.VocabularyNames"
    ]
    """<p>Specify the names of the custom vocabularies that you want to use when processing your Call Analytics transcription. Note that vocabulary names are case sensitive.</p> <p>If the custom vocabulary's language doesn't match the identified media language, it won't be applied to the transcription.</p> <important> <p>This parameter is only intended for use <b>with</b> the <code>IdentifyLanguage</code> parameter. If you're <b>not</b> including <code>IdentifyLanguage</code> in your request and want to use a custom vocabulary with your transcription, use the <code>VocabularyName</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>"""
    vocabulary_filter_names: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_filter_names.VocabularyFilterNames"
    ]
    """<p>Specify the names of the custom vocabulary filters that you want to use when processing your Call Analytics transcription. Note that vocabulary filter names are case sensitive.</p> <p>These filters serve to customize the transcript output.</p> <important> <p>This parameter is only intended for use <b>with</b> the <code>IdentifyLanguage</code> parameter. If you're <b>not</b> including <code>IdentifyLanguage</code> in your request and want to use a custom vocabulary filter with your transcription, use the <code>VocabularyFilterName</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a>.</p>"""
    enable_partial_results_stabilization: (
        "capo_transcribe_streaming.types.boolean.Boolean"
    )
    """<p>Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a>.</p>"""
    partial_results_stability: NotRequired[
        "capo_transcribe_streaming.types.partial_results_stability.PartialResultsStability"
    ]
    """<p>Specify the level of stability to use when you enable partial results stabilization (<code>EnablePartialResultsStabilization</code>).</p> <p>Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a>.</p>"""
    content_identification_type: NotRequired[
        "capo_transcribe_streaming.types.content_identification_type.ContentIdentificationType"
    ]
    """<p>Labels all personally identifiable information (PII) identified in your transcript.</p> <p>Content identification is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is flagged upon complete transcription of an audio segment. If you don't include <code>PiiEntityTypes</code> in your request, all PII is identified.</p> <p>You can’t set <code>ContentIdentificationType</code> and <code>ContentRedactionType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a>.</p>"""
    content_redaction_type: NotRequired[
        "capo_transcribe_streaming.types.content_redaction_type.ContentRedactionType"
    ]
    """<p>Redacts all personally identifiable information (PII) identified in your transcript.</p> <p>Content redaction is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is redacted upon complete transcription of an audio segment. If you don't include <code>PiiEntityTypes</code> in your request, all PII is redacted.</p> <p>You can’t set <code>ContentRedactionType</code> and <code>ContentIdentificationType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a>.</p>"""
    pii_entity_types: NotRequired[
        "capo_transcribe_streaming.types.pii_entity_types.PiiEntityTypes"
    ]
    """<p>Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select <code>ALL</code>.</p> <p>Values must be comma-separated and can include: <code>ADDRESS</code>, <code>BANK_ACCOUNT_NUMBER</code>, <code>BANK_ROUTING</code>, <code>CREDIT_DEBIT_CVV</code>, <code>CREDIT_DEBIT_EXPIRY</code>, <code>CREDIT_DEBIT_NUMBER</code>, <code>EMAIL</code>, <code>NAME</code>, <code>PHONE</code>, <code>PIN</code>, <code>SSN</code>, or <code>ALL</code>.</p> <p>Note that if you include <code>PiiEntityTypes</code> in your request, you must also include <code>ContentIdentificationType</code> or <code>ContentRedactionType</code>.</p> <p>If you include <code>ContentRedactionType</code> or <code>ContentIdentificationType</code> in your request, but do not include <code>PiiEntityTypes</code>, all PII is redacted or identified.</p>"""
