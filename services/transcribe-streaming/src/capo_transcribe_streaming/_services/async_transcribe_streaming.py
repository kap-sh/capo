"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Transcribe``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_transcribe_streaming._auth._signers
import capo_transcribe_streaming._auth._sigv4
from capo_transcribe_streaming._auth._identity import Credentials
from capo_transcribe_streaming._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_transcribe_streaming._auth._zapros_handler import AuthMiddleware
from capo_transcribe_streaming._iter import ensure_async_iterator
from capo_transcribe_streaming._services._aws_config import aaws_config
from capo_transcribe_streaming._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.audio_stream
    import capo_transcribe_streaming.types.boolean
    import capo_transcribe_streaming.types.call_analytics_language_code
    import capo_transcribe_streaming.types.content_identification_type
    import capo_transcribe_streaming.types.content_redaction_type
    import capo_transcribe_streaming.types.get_medical_scribe_stream_request
    import capo_transcribe_streaming.types.get_medical_scribe_stream_response
    import capo_transcribe_streaming.types.language_code
    import capo_transcribe_streaming.types.language_options
    import capo_transcribe_streaming.types.media_encoding
    import capo_transcribe_streaming.types.media_sample_rate_hertz
    import capo_transcribe_streaming.types.medical_content_identification_type
    import capo_transcribe_streaming.types.medical_scribe_input_stream
    import capo_transcribe_streaming.types.medical_scribe_language_code
    import capo_transcribe_streaming.types.medical_scribe_media_encoding
    import capo_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz
    import capo_transcribe_streaming.types.model_name
    import capo_transcribe_streaming.types.number_of_channels
    import capo_transcribe_streaming.types.partial_results_stability
    import capo_transcribe_streaming.types.pii_entity_types
    import capo_transcribe_streaming.types.session_id
    import capo_transcribe_streaming.types.session_resume_window
    import capo_transcribe_streaming.types.specialty
    import capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request
    import capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response
    import capo_transcribe_streaming.types.start_medical_scribe_stream_request
    import capo_transcribe_streaming.types.start_medical_scribe_stream_response
    import capo_transcribe_streaming.types.start_medical_stream_transcription_request
    import capo_transcribe_streaming.types.start_medical_stream_transcription_response
    import capo_transcribe_streaming.types.start_stream_transcription_request
    import capo_transcribe_streaming.types.start_stream_transcription_response
    import capo_transcribe_streaming.types.transcript_format
    import capo_transcribe_streaming.types.type
    import capo_transcribe_streaming.types.vocabulary_filter_method
    import capo_transcribe_streaming.types.vocabulary_filter_name
    import capo_transcribe_streaming.types.vocabulary_filter_names
    import capo_transcribe_streaming.types.vocabulary_name
    import capo_transcribe_streaming.types.vocabulary_names


class AsyncTranscribeStreamingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncTranscribeStreamingClient:
    """A client for the ``TranscribeStreaming`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncTranscribeStreamingClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncTranscribeStreamingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTranscribeStreamingClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def get_medical_scribe_stream(
        self,
        session_id: "capo_transcribe_streaming.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncTranscribeStreamingClientConfig] = None,
    ) -> "capo_transcribe_streaming.types.get_medical_scribe_stream_response.GetMedicalScribeStreamResponse":
        """<p>Provides details about the specified Amazon Web Services HealthScribe streaming session. To view the status of the streaming session, check the <code>StreamStatus</code> field in the response. To get the details of post-stream analytics, including its status, check the <code>PostStreamAnalyticsResult</code> field in the response. </p>

        Args:
            session_id: <p>The identifier of the HealthScribe streaming session you want information about.</p>

        Raises:
            capo_transcribe_streaming.errors.bad_request_exception.BadRequestException: <p>One or more arguments to the <code>StartStreamTranscription</code>, <code>StartMedicalStreamTranscription</code>, or <code>StartCallAnalyticsStreamTranscription</code> operation was not valid. For example, <code>MediaEncoding</code> or <code>LanguageCode</code> used unsupported values. Check the specified parameters and try your request again.</p>
            capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException: <p>A problem occurred while processing the audio. Amazon Transcribe terminated processing.</p>
            capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException: <p>Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.</p>
            capo_transcribe_streaming.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which doesn't exist.</p>
            capo_transcribe_streaming.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe_streaming.types.get_medical_scribe_stream_request.GetMedicalScribeStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe_streaming.types.get_medical_scribe_stream_response.GetMedicalScribeStreamResponse"
        ]:
            import capo_transcribe_streaming._operations.transcribe.get_medical_scribe_stream

            (
                output,
                http_response,
            ) = await capo_transcribe_streaming._operations.transcribe.get_medical_scribe_stream.async_get_medical_scribe_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe_streaming.types.get_medical_scribe_stream_request.GetMedicalScribeStreamRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def start_call_analytics_stream_transcription(
        self,
        media_sample_rate_hertz: "capo_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz",
        media_encoding: "capo_transcribe_streaming.types.media_encoding.MediaEncoding",
        audio_stream: "AsyncIterator[capo_transcribe_streaming.types.audio_stream._AudioStream] | capo_transcribe_streaming.types.audio_stream._AudioStream",
        *,
        config_overrides: Optional[AsyncTranscribeStreamingClientConfig] = None,
        language_code: Optional[
            "capo_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
        ] = None,
        vocabulary_name: Optional[
            "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
        ] = None,
        session_id: Optional[
            "capo_transcribe_streaming.types.session_id.SessionId"
        ] = None,
        vocabulary_filter_name: Optional[
            "capo_transcribe_streaming.types.vocabulary_filter_name.VocabularyFilterName"
        ] = None,
        vocabulary_filter_method: Optional[
            "capo_transcribe_streaming.types.vocabulary_filter_method.VocabularyFilterMethod"
        ] = None,
        language_model_name: Optional[
            "capo_transcribe_streaming.types.model_name.ModelName"
        ] = None,
        identify_language: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        language_options: Optional[
            "capo_transcribe_streaming.types.language_options.LanguageOptions"
        ] = None,
        preferred_language: Optional[
            "capo_transcribe_streaming.types.call_analytics_language_code.CallAnalyticsLanguageCode"
        ] = None,
        vocabulary_names: Optional[
            "capo_transcribe_streaming.types.vocabulary_names.VocabularyNames"
        ] = None,
        vocabulary_filter_names: Optional[
            "capo_transcribe_streaming.types.vocabulary_filter_names.VocabularyFilterNames"
        ] = None,
        enable_partial_results_stabilization: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        partial_results_stability: Optional[
            "capo_transcribe_streaming.types.partial_results_stability.PartialResultsStability"
        ] = None,
        content_identification_type: Optional[
            "capo_transcribe_streaming.types.content_identification_type.ContentIdentificationType"
        ] = None,
        content_redaction_type: Optional[
            "capo_transcribe_streaming.types.content_redaction_type.ContentRedactionType"
        ] = None,
        pii_entity_types: Optional[
            "capo_transcribe_streaming.types.pii_entity_types.PiiEntityTypes"
        ] = None,
    ) -> "AsyncGenerator[capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse]":
        """<p>Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe and the transcription results are streamed to your application. Use this operation for <a href="https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html">Call Analytics</a> transcriptions.</p> <p>The following parameters are required:</p> <ul> <li> <p> <code>language-code</code> or <code>identify-language</code> </p> </li> <li> <p> <code>media-encoding</code> </p> </li> <li> <p> <code>sample-rate</code> </p> </li> </ul> <p>For more information on streaming with Amazon Transcribe, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html">Transcribing streaming audio</a>.</p>

        Args:
            language_code: <p>Specify the language code that represents the language spoken in your audio.</p> <p>For a list of languages supported with real-time Call Analytics, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>
            media_sample_rate_hertz: <p>The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.</p>
            media_encoding: <p>Specify the encoding of your input audio. Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV)</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a>.</p>
            vocabulary_name: <p>Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p> <p>If the language of the specified custom vocabulary doesn't match the language identified in your media, the custom vocabulary is not applied to your transcription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>
            session_id: <p>Specify a name for your Call Analytics transcription session. If you don't include this parameter in your request, Amazon Transcribe generates an ID and returns it in the response.</p>
            audio_stream: <p>An encoded stream of audio blobs. Audio streams are encoded as either HTTP/2 or WebSocket data frames.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html">Transcribing streaming audio</a>.</p>
            vocabulary_filter_name: <p>Specify the name of the custom vocabulary filter that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive.</p> <p>If the language of the specified custom vocabulary filter doesn't match the language identified in your media, the vocabulary filter is not applied to your transcription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a>.</p>
            vocabulary_filter_method: <p>Specify how you want your vocabulary filter applied to your transcript.</p> <p>To replace words with <code>***</code>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>.</p>
            language_model_name: <p>Specify the name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.</p> <p>The language of the specified language model must match the language code you specify in your transcription request. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html">Custom language models</a>.</p>
            identify_language: <p>Enables automatic language identification for your Call Analytics transcription.</p> <p>If you include <code>IdentifyLanguage</code>, you must include a list of language codes, using <code>LanguageOptions</code>, that you think may be present in your audio stream. You must provide a minimum of two language selections.</p> <p>You can also include a preferred language using <code>PreferredLanguage</code>. Adding a preferred language can help Amazon Transcribe identify the language faster than if you omit this parameter.</p> <p>Note that you must include either <code>LanguageCode</code> or <code>IdentifyLanguage</code> in your request. If you include both parameters, your transcription job fails.</p>
            language_options: <p>Specify two or more language codes that represent the languages you think may be present in your media.</p> <p>Including language options can improve the accuracy of language identification.</p> <p>If you include <code>LanguageOptions</code> in your request, you must also include <code>IdentifyLanguage</code>.</p> <p>For a list of languages supported with Call Analytics streaming, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p> <important> <p>You can only include one language dialect per language per stream. For example, you cannot include <code>en-US</code> and <code>en-AU</code> in the same request.</p> </important>
            preferred_language: <p>Specify a preferred language from the subset of languages codes you specified in <code>LanguageOptions</code>.</p> <p>You can only use this parameter if you've included <code>IdentifyLanguage</code> and <code>LanguageOptions</code> in your request.</p>
            vocabulary_names: <p>Specify the names of the custom vocabularies that you want to use when processing your Call Analytics transcription. Note that vocabulary names are case sensitive.</p> <p>If the custom vocabulary's language doesn't match the identified media language, it won't be applied to the transcription.</p> <important> <p>This parameter is only intended for use <b>with</b> the <code>IdentifyLanguage</code> parameter. If you're <b>not</b> including <code>IdentifyLanguage</code> in your request and want to use a custom vocabulary with your transcription, use the <code>VocabularyName</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>
            vocabulary_filter_names: <p>Specify the names of the custom vocabulary filters that you want to use when processing your Call Analytics transcription. Note that vocabulary filter names are case sensitive.</p> <p>These filters serve to customize the transcript output.</p> <important> <p>This parameter is only intended for use <b>with</b> the <code>IdentifyLanguage</code> parameter. If you're <b>not</b> including <code>IdentifyLanguage</code> in your request and want to use a custom vocabulary filter with your transcription, use the <code>VocabularyFilterName</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a>.</p>
            enable_partial_results_stabilization: <p>Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a>.</p>
            partial_results_stability: <p>Specify the level of stability to use when you enable partial results stabilization (<code>EnablePartialResultsStabilization</code>).</p> <p>Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a>.</p>
            content_identification_type: <p>Labels all personally identifiable information (PII) identified in your transcript.</p> <p>Content identification is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is flagged upon complete transcription of an audio segment. If you don't include <code>PiiEntityTypes</code> in your request, all PII is identified.</p> <p>You can’t set <code>ContentIdentificationType</code> and <code>ContentRedactionType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a>.</p>
            content_redaction_type: <p>Redacts all personally identifiable information (PII) identified in your transcript.</p> <p>Content redaction is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is redacted upon complete transcription of an audio segment. If you don't include <code>PiiEntityTypes</code> in your request, all PII is redacted.</p> <p>You can’t set <code>ContentRedactionType</code> and <code>ContentIdentificationType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a>.</p>
            pii_entity_types: <p>Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select <code>ALL</code>.</p> <p>Values must be comma-separated and can include: <code>ADDRESS</code>, <code>BANK_ACCOUNT_NUMBER</code>, <code>BANK_ROUTING</code>, <code>CREDIT_DEBIT_CVV</code>, <code>CREDIT_DEBIT_EXPIRY</code>, <code>CREDIT_DEBIT_NUMBER</code>, <code>EMAIL</code>, <code>NAME</code>, <code>PHONE</code>, <code>PIN</code>, <code>SSN</code>, or <code>ALL</code>.</p> <p>Note that if you include <code>PiiEntityTypes</code> in your request, you must also include <code>ContentIdentificationType</code> or <code>ContentRedactionType</code>.</p> <p>If you include <code>ContentRedactionType</code> or <code>ContentIdentificationType</code> in your request, but do not include <code>PiiEntityTypes</code>, all PII is redacted or identified.</p>

        Raises:
            capo_transcribe_streaming.errors.bad_request_exception.BadRequestException: <p>One or more arguments to the <code>StartStreamTranscription</code>, <code>StartMedicalStreamTranscription</code>, or <code>StartCallAnalyticsStreamTranscription</code> operation was not valid. For example, <code>MediaEncoding</code> or <code>LanguageCode</code> used unsupported values. Check the specified parameters and try your request again.</p>
            capo_transcribe_streaming.errors.conflict_exception.ConflictException: <p>A new stream started with the same session ID. The current stream has been terminated.</p>
            capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException: <p>A problem occurred while processing the audio. Amazon Transcribe terminated processing.</p>
            capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException: <p>Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.</p>
            capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable. Try your request later.</p>
            capo_transcribe_streaming.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request.StartCallAnalyticsStreamTranscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe_streaming.types.start_call_analytics_stream_transcription_response.StartCallAnalyticsStreamTranscriptionResponse"
        ]:
            import capo_transcribe_streaming._operations.transcribe.start_call_analytics_stream_transcription

            (
                output,
                http_response,
            ) = await capo_transcribe_streaming._operations.transcribe.start_call_analytics_stream_transcription.async_start_call_analytics_stream_transcription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe_streaming.types.start_call_analytics_stream_transcription_request.StartCallAnalyticsStreamTranscriptionRequest = {
            "media_sample_rate_hertz": media_sample_rate_hertz,
            "media_encoding": media_encoding,
            "audio_stream": ensure_async_iterator(audio_stream),
        }
        if language_code is not None:
            input_["language_code"] = language_code
        if vocabulary_name is not None:
            input_["vocabulary_name"] = vocabulary_name
        if session_id is not None:
            input_["session_id"] = session_id
        if vocabulary_filter_name is not None:
            input_["vocabulary_filter_name"] = vocabulary_filter_name
        if vocabulary_filter_method is not None:
            input_["vocabulary_filter_method"] = vocabulary_filter_method
        if language_model_name is not None:
            input_["language_model_name"] = language_model_name
        if identify_language is not None:
            input_["identify_language"] = identify_language
        if language_options is not None:
            input_["language_options"] = language_options
        if preferred_language is not None:
            input_["preferred_language"] = preferred_language
        if vocabulary_names is not None:
            input_["vocabulary_names"] = vocabulary_names
        if vocabulary_filter_names is not None:
            input_["vocabulary_filter_names"] = vocabulary_filter_names
        if enable_partial_results_stabilization is not None:
            input_["enable_partial_results_stabilization"] = (
                enable_partial_results_stabilization
            )
        if partial_results_stability is not None:
            input_["partial_results_stability"] = partial_results_stability
        if content_identification_type is not None:
            input_["content_identification_type"] = content_identification_type
        if content_redaction_type is not None:
            input_["content_redaction_type"] = content_redaction_type
        if pii_entity_types is not None:
            input_["pii_entity_types"] = pii_entity_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    @asynccontextmanager
    async def start_medical_scribe_stream(
        self,
        language_code: "capo_transcribe_streaming.types.medical_scribe_language_code.MedicalScribeLanguageCode",
        media_sample_rate_hertz: "capo_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz",
        media_encoding: "capo_transcribe_streaming.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding",
        input_stream: "AsyncIterator[capo_transcribe_streaming.types.medical_scribe_input_stream._MedicalScribeInputStream] | capo_transcribe_streaming.types.medical_scribe_input_stream._MedicalScribeInputStream",
        *,
        config_overrides: Optional[AsyncTranscribeStreamingClientConfig] = None,
        session_id: Optional[
            "capo_transcribe_streaming.types.session_id.SessionId"
        ] = None,
    ) -> "AsyncGenerator[capo_transcribe_streaming.types.start_medical_scribe_stream_response.StartMedicalScribeStreamResponse]":
        """<p>Starts a bidirectional HTTP/2 stream, where audio is streamed to Amazon Web Services HealthScribe and the transcription results are streamed to your application.</p> <p>When you start a stream, you first specify the stream configuration in a <code>MedicalScribeConfigurationEvent</code>. This event includes channel definitions, encryption settings, medical scribe context, and post-stream analytics settings, such as the output configuration for aggregated transcript and clinical note generation. These are additional streaming session configurations beyond those provided in your initial start request headers. Whether you are starting a new session or resuming an existing session, your first event must be a <code>MedicalScribeConfigurationEvent</code>. </p> <p> After you send a <code>MedicalScribeConfigurationEvent</code>, you start <code>AudioEvents</code> and Amazon Web Services HealthScribe responds with real-time transcription results. When you are finished, to start processing the results with the post-stream analytics, send a <code>MedicalScribeSessionControlEvent</code> with a <code>Type</code> of <code>END_OF_SESSION</code> and Amazon Web Services HealthScribe starts the analytics. </p> <p>You can pause or resume streaming. To pause streaming, complete the input stream without sending the <code>MedicalScribeSessionControlEvent</code>. To resume streaming, call the <code>StartMedicalScribeStream</code> and specify the same SessionId you used to start the stream. </p> <p>The following parameters are required:</p> <ul> <li> <p> <code>language-code</code> </p> </li> <li> <p> <code>media-encoding</code> </p> </li> <li> <p> <code>media-sample-rate-hertz</code> </p> </li> </ul> <p></p> <p>For more information on streaming with Amazon Web Services HealthScribe, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-streaming.html">Amazon Web Services HealthScribe</a>. </p>

        Args:
            session_id: <p>Specify an identifier for your streaming session (in UUID format). If you don't include a SessionId in your request, Amazon Web Services HealthScribe generates an ID and returns it in the response. </p>
            language_code: <p>Specify the language code for your HealthScribe streaming session.</p>
            media_sample_rate_hertz: <p>Specify the sample rate of the input audio (in hertz). Amazon Web Services HealthScribe supports a range from 16,000 Hz to 48,000 Hz. The sample rate you specify must match that of your audio. </p>
            media_encoding: <p>Specify the encoding used for the input audio.</p> <p>Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV) </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a>. </p>
            input_stream: <p>Specify the input stream where you will send events in real time.</p> <p>The first element of the input stream must be a <code>MedicalScribeConfigurationEvent</code>. </p>

        Raises:
            capo_transcribe_streaming.errors.bad_request_exception.BadRequestException: <p>One or more arguments to the <code>StartStreamTranscription</code>, <code>StartMedicalStreamTranscription</code>, or <code>StartCallAnalyticsStreamTranscription</code> operation was not valid. For example, <code>MediaEncoding</code> or <code>LanguageCode</code> used unsupported values. Check the specified parameters and try your request again.</p>
            capo_transcribe_streaming.errors.conflict_exception.ConflictException: <p>A new stream started with the same session ID. The current stream has been terminated.</p>
            capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException: <p>A problem occurred while processing the audio. Amazon Transcribe terminated processing.</p>
            capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException: <p>Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.</p>
            capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable. Try your request later.</p>
            capo_transcribe_streaming.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe_streaming.types.start_medical_scribe_stream_request.StartMedicalScribeStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe_streaming.types.start_medical_scribe_stream_response.StartMedicalScribeStreamResponse"
        ]:
            import capo_transcribe_streaming._operations.transcribe.start_medical_scribe_stream

            (
                output,
                http_response,
            ) = await capo_transcribe_streaming._operations.transcribe.start_medical_scribe_stream.async_start_medical_scribe_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe_streaming.types.start_medical_scribe_stream_request.StartMedicalScribeStreamRequest = {
            "language_code": language_code,
            "media_sample_rate_hertz": media_sample_rate_hertz,
            "media_encoding": media_encoding,
            "input_stream": ensure_async_iterator(input_stream),
        }
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    @asynccontextmanager
    async def start_medical_stream_transcription(
        self,
        language_code: "capo_transcribe_streaming.types.language_code.LanguageCode",
        media_sample_rate_hertz: "capo_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz",
        media_encoding: "capo_transcribe_streaming.types.media_encoding.MediaEncoding",
        specialty: "capo_transcribe_streaming.types.specialty.Specialty",
        type: "capo_transcribe_streaming.types.type.Type",
        audio_stream: "AsyncIterator[capo_transcribe_streaming.types.audio_stream._AudioStream] | capo_transcribe_streaming.types.audio_stream._AudioStream",
        *,
        config_overrides: Optional[AsyncTranscribeStreamingClientConfig] = None,
        vocabulary_name: Optional[
            "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
        ] = None,
        show_speaker_label: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        session_id: Optional[
            "capo_transcribe_streaming.types.session_id.SessionId"
        ] = None,
        enable_channel_identification: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        number_of_channels: Optional[
            "capo_transcribe_streaming.types.number_of_channels.NumberOfChannels"
        ] = None,
        content_identification_type: Optional[
            "capo_transcribe_streaming.types.medical_content_identification_type.MedicalContentIdentificationType"
        ] = None,
    ) -> "AsyncGenerator[capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse]":
        """<p>Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe Medical and the transcription results are streamed to your application.</p> <p>The following parameters are required:</p> <ul> <li> <p> <code>language-code</code> </p> </li> <li> <p> <code>media-encoding</code> </p> </li> <li> <p> <code>sample-rate</code> </p> </li> </ul> <p>For more information on streaming with Amazon Transcribe Medical, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html">Transcribing streaming audio</a>.</p>

        Args:
            language_code: <p>Specify the language code that represents the language spoken in your audio.</p> <important> <p>Amazon Transcribe Medical only supports US English (<code>en-US</code>).</p> </important>
            media_sample_rate_hertz: <p>The sample rate of the input audio (in hertz). Amazon Transcribe Medical supports a range from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.</p>
            media_encoding: <p>Specify the encoding used for the input audio. Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV)</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a>.</p>
            vocabulary_name: <p>Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p>
            specialty: <p>Specify the medical specialty contained in your audio.</p>
            type: <p>Specify the type of input audio. For example, choose <code>DICTATION</code> for a provider dictating patient notes and <code>CONVERSATION</code> for a dialogue between a patient and a medical professional.</p>
            show_speaker_label: <p>Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html">Partitioning speakers (diarization)</a>.</p>
            session_id: <p>Specify a name for your transcription session. If you don't include this parameter in your request, Amazon Transcribe Medical generates an ID and returns it in the response.</p>
            enable_channel_identification: <p>Enables channel identification in multi-channel audio.</p> <p>Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.</p> <p>If you have multi-channel audio and do not enable channel identification, your audio is transcribed in a continuous manner and your transcript is not separated by channel.</p> <p>If you include <code>EnableChannelIdentification</code> in your request, you must also include <code>NumberOfChannels</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html">Transcribing multi-channel audio</a>.</p>
            number_of_channels: <p>Specify the number of channels in your audio stream. This value must be <code>2</code>, as only two channels are supported. If your audio doesn't contain multiple channels, do not include this parameter in your request.</p> <p>If you include <code>NumberOfChannels</code> in your request, you must also include <code>EnableChannelIdentification</code>.</p>
            content_identification_type: <p>Labels all personal health information (PHI) identified in your transcript.</p> <p>Content identification is performed at the segment level; PHI is flagged upon complete transcription of an audio segment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html">Identifying personal health information (PHI) in a transcription</a>.</p>

        Raises:
            capo_transcribe_streaming.errors.bad_request_exception.BadRequestException: <p>One or more arguments to the <code>StartStreamTranscription</code>, <code>StartMedicalStreamTranscription</code>, or <code>StartCallAnalyticsStreamTranscription</code> operation was not valid. For example, <code>MediaEncoding</code> or <code>LanguageCode</code> used unsupported values. Check the specified parameters and try your request again.</p>
            capo_transcribe_streaming.errors.conflict_exception.ConflictException: <p>A new stream started with the same session ID. The current stream has been terminated.</p>
            capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException: <p>A problem occurred while processing the audio. Amazon Transcribe terminated processing.</p>
            capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException: <p>Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.</p>
            capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable. Try your request later.</p>
            capo_transcribe_streaming.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe_streaming.types.start_medical_stream_transcription_response.StartMedicalStreamTranscriptionResponse"
        ]:
            import capo_transcribe_streaming._operations.transcribe.start_medical_stream_transcription

            (
                output,
                http_response,
            ) = await capo_transcribe_streaming._operations.transcribe.start_medical_stream_transcription.async_start_medical_stream_transcription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe_streaming.types.start_medical_stream_transcription_request.StartMedicalStreamTranscriptionRequest = {
            "language_code": language_code,
            "media_sample_rate_hertz": media_sample_rate_hertz,
            "media_encoding": media_encoding,
            "specialty": specialty,
            "type": type,
            "audio_stream": ensure_async_iterator(audio_stream),
        }
        if vocabulary_name is not None:
            input_["vocabulary_name"] = vocabulary_name
        if show_speaker_label is not None:
            input_["show_speaker_label"] = show_speaker_label
        if session_id is not None:
            input_["session_id"] = session_id
        if enable_channel_identification is not None:
            input_["enable_channel_identification"] = enable_channel_identification
        if number_of_channels is not None:
            input_["number_of_channels"] = number_of_channels
        if content_identification_type is not None:
            input_["content_identification_type"] = content_identification_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    @asynccontextmanager
    async def start_stream_transcription(
        self,
        media_sample_rate_hertz: "capo_transcribe_streaming.types.media_sample_rate_hertz.MediaSampleRateHertz",
        media_encoding: "capo_transcribe_streaming.types.media_encoding.MediaEncoding",
        audio_stream: "AsyncIterator[capo_transcribe_streaming.types.audio_stream._AudioStream] | capo_transcribe_streaming.types.audio_stream._AudioStream",
        *,
        config_overrides: Optional[AsyncTranscribeStreamingClientConfig] = None,
        language_code: Optional[
            "capo_transcribe_streaming.types.language_code.LanguageCode"
        ] = None,
        vocabulary_name: Optional[
            "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
        ] = None,
        session_id: Optional[
            "capo_transcribe_streaming.types.session_id.SessionId"
        ] = None,
        vocabulary_filter_name: Optional[
            "capo_transcribe_streaming.types.vocabulary_filter_name.VocabularyFilterName"
        ] = None,
        vocabulary_filter_method: Optional[
            "capo_transcribe_streaming.types.vocabulary_filter_method.VocabularyFilterMethod"
        ] = None,
        show_speaker_label: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        enable_channel_identification: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        number_of_channels: Optional[
            "capo_transcribe_streaming.types.number_of_channels.NumberOfChannels"
        ] = None,
        enable_partial_results_stabilization: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        partial_results_stability: Optional[
            "capo_transcribe_streaming.types.partial_results_stability.PartialResultsStability"
        ] = None,
        content_identification_type: Optional[
            "capo_transcribe_streaming.types.content_identification_type.ContentIdentificationType"
        ] = None,
        content_redaction_type: Optional[
            "capo_transcribe_streaming.types.content_redaction_type.ContentRedactionType"
        ] = None,
        pii_entity_types: Optional[
            "capo_transcribe_streaming.types.pii_entity_types.PiiEntityTypes"
        ] = None,
        language_model_name: Optional[
            "capo_transcribe_streaming.types.model_name.ModelName"
        ] = None,
        identify_language: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        language_options: Optional[
            "capo_transcribe_streaming.types.language_options.LanguageOptions"
        ] = None,
        preferred_language: Optional[
            "capo_transcribe_streaming.types.language_code.LanguageCode"
        ] = None,
        identify_multiple_languages: Optional[
            "capo_transcribe_streaming.types.boolean.Boolean"
        ] = None,
        vocabulary_names: Optional[
            "capo_transcribe_streaming.types.vocabulary_names.VocabularyNames"
        ] = None,
        vocabulary_filter_names: Optional[
            "capo_transcribe_streaming.types.vocabulary_filter_names.VocabularyFilterNames"
        ] = None,
        session_resume_window: Optional[
            "capo_transcribe_streaming.types.session_resume_window.SessionResumeWindow"
        ] = None,
        transcript_format: Optional[
            "capo_transcribe_streaming.types.transcript_format.TranscriptFormat"
        ] = None,
    ) -> "AsyncGenerator[capo_transcribe_streaming.types.start_stream_transcription_response.StartStreamTranscriptionResponse]":
        """<p>Starts a bidirectional HTTP/2 or WebSocket stream where audio is streamed to Amazon Transcribe and the transcription results are streamed to your application.</p> <p>The following parameters are required:</p> <ul> <li> <p> <code>language-code</code> or <code>identify-language</code> or <code>identify-multiple-language</code> </p> </li> <li> <p> <code>media-encoding</code> </p> </li> <li> <p> <code>sample-rate</code> </p> </li> </ul> <p>For more information on streaming with Amazon Transcribe, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html">Transcribing streaming audio</a>.</p>

        Args:
            language_code: <p>Specify the language code that represents the language spoken in your audio.</p> <p>If you're unsure of the language spoken in your audio, consider using <code>IdentifyLanguage</code> to enable automatic language identification.</p> <p>For a list of languages supported with Amazon Transcribe streaming, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>
            media_sample_rate_hertz: <p>The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.</p>
            media_encoding: <p>Specify the encoding of your input audio. Supported formats are:</p> <ul> <li> <p>FLAC</p> </li> <li> <p>OPUS-encoded audio in an Ogg container</p> </li> <li> <p>PCM (only signed 16-bit little-endian audio formats, which does not include WAV)</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio">Media formats</a>.</p>
            vocabulary_name: <p>Specify the name of the custom vocabulary that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p> <p>If the language of the specified custom vocabulary doesn't match the language identified in your media, the custom vocabulary is not applied to your transcription.</p> <important> <p>This parameter is <b>not</b> intended for use with the <code>IdentifyLanguage</code> parameter. If you're including <code>IdentifyLanguage</code> in your request and want to use one or more custom vocabularies with your transcription, use the <code>VocabularyNames</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>
            session_id: <p>Specify a name for your transcription session. If you don't include this parameter in your request, Amazon Transcribe generates an ID and returns it in the response.</p>
            audio_stream: <p>An encoded stream of audio blobs. Audio streams are encoded as either HTTP/2 or WebSocket data frames.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html">Transcribing streaming audio</a>.</p>
            vocabulary_filter_name: <p>Specify the name of the custom vocabulary filter that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive.</p> <p>If the language of the specified custom vocabulary filter doesn't match the language identified in your media, the vocabulary filter is not applied to your transcription.</p> <important> <p>This parameter is <b>not</b> intended for use with the <code>IdentifyLanguage</code> parameter. If you're including <code>IdentifyLanguage</code> in your request and want to use one or more vocabulary filters with your transcription, use the <code>VocabularyFilterNames</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a>.</p>
            vocabulary_filter_method: <p>Specify how you want your vocabulary filter applied to your transcript.</p> <p>To replace words with <code>***</code>, choose <code>mask</code>.</p> <p>To delete words, choose <code>remove</code>.</p> <p>To flag words without changing them, choose <code>tag</code>.</p>
            show_speaker_label: <p>Enables speaker partitioning (diarization) in your transcription output. Speaker partitioning labels the speech from individual speakers in your media file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/diarization.html">Partitioning speakers (diarization)</a>.</p>
            enable_channel_identification: <p>Enables channel identification in multi-channel audio.</p> <p>Channel identification transcribes the audio on each channel independently, then appends the output for each channel into one transcript.</p> <p>If you have multi-channel audio and do not enable channel identification, your audio is transcribed in a continuous manner and your transcript is not separated by channel.</p> <p>If you include <code>EnableChannelIdentification</code> in your request, you must also include <code>NumberOfChannels</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/channel-id.html">Transcribing multi-channel audio</a>.</p>
            number_of_channels: <p>Specify the number of channels in your audio stream. This value must be <code>2</code>, as only two channels are supported. If your audio doesn't contain multiple channels, do not include this parameter in your request.</p> <p>If you include <code>NumberOfChannels</code> in your request, you must also include <code>EnableChannelIdentification</code>.</p>
            enable_partial_results_stabilization: <p>Enables partial result stabilization for your transcription. Partial result stabilization can reduce latency in your output, but may impact accuracy. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a>.</p>
            partial_results_stability: <p>Specify the level of stability to use when you enable partial results stabilization (<code>EnablePartialResultsStabilization</code>).</p> <p>Low stability provides the highest accuracy. High stability transcribes faster, but with slightly lower accuracy.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html#streaming-partial-result-stabilization">Partial-result stabilization</a>.</p>
            content_identification_type: <p>Labels all personally identifiable information (PII) identified in your transcript.</p> <p>Content identification is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is flagged upon complete transcription of an audio segment. If you don't include <code>PiiEntityTypes</code> in your request, all PII is identified.</p> <p>You can’t set <code>ContentIdentificationType</code> and <code>ContentRedactionType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a>.</p>
            content_redaction_type: <p>Redacts all personally identifiable information (PII) identified in your transcript.</p> <p>Content redaction is performed at the segment level; PII specified in <code>PiiEntityTypes</code> is redacted upon complete transcription of an audio segment. If you don't include <code>PiiEntityTypes</code> in your request, all PII is redacted.</p> <p>You can’t set <code>ContentRedactionType</code> and <code>ContentIdentificationType</code> in the same request. If you set both, your request returns a <code>BadRequestException</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction.html">Redacting or identifying personally identifiable information</a>.</p>
            pii_entity_types: <p>Specify which types of personally identifiable information (PII) you want to redact in your transcript. You can include as many types as you'd like, or you can select <code>ALL</code>.</p> <p>Values must be comma-separated and can include: <code>ADDRESS</code>, <code>BANK_ACCOUNT_NUMBER</code>, <code>BANK_ROUTING</code>, <code>CREDIT_DEBIT_CVV</code>, <code>CREDIT_DEBIT_EXPIRY</code>, <code>CREDIT_DEBIT_NUMBER</code>, <code>EMAIL</code>, <code>NAME</code>, <code>PHONE</code>, <code>PIN</code>, <code>SSN</code>, <code>AGE</code>, <code>DATE_TIME</code>, <code>LICENSE_PLATE</code>, <code>PASSPORT_NUMBER</code>, <code>PASSWORD</code>, <code>USERNAME</code>, <code>VEHICLE_IDENTIFICATION_NUMBER</code>, or <code>ALL</code>.</p> <p>Note that if you include <code>PiiEntityTypes</code> in your request, you must also include <code>ContentIdentificationType</code> or <code>ContentRedactionType</code>.</p> <p>If you include <code>ContentRedactionType</code> or <code>ContentIdentificationType</code> in your request, but do not include <code>PiiEntityTypes</code>, all PII is redacted or identified.</p>
            language_model_name: <p>Specify the name of the custom language model that you want to use when processing your transcription. Note that language model names are case sensitive.</p> <p>The language of the specified language model must match the language code you specify in your transcription request. If the languages don't match, the custom language model isn't applied. There are no errors or warnings associated with a language mismatch.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html">Custom language models</a>.</p>
            identify_language: <p>Enables automatic language identification for your transcription.</p> <p>If you include <code>IdentifyLanguage</code>, you must include a list of language codes, using <code>LanguageOptions</code>, that you think may be present in your audio stream. </p> <p>You can also include a preferred language using <code>PreferredLanguage</code>. Adding a preferred language can help Amazon Transcribe identify the language faster than if you omit this parameter.</p> <p>If you have multi-channel audio that contains different languages on each channel, and you've enabled channel identification, automatic language identification identifies the dominant language on each audio channel.</p> <p>Note that you must include either <code>LanguageCode</code> or <code>IdentifyLanguage</code> or <code>IdentifyMultipleLanguages</code> in your request. If you include more than one of these parameters, your transcription job fails.</p> <p>Streaming language identification can't be combined with custom language models or redaction.</p>
            language_options: <p>Specify two or more language codes that represent the languages you think may be present in your media; including more than five is not recommended.</p> <p>Including language options can improve the accuracy of language identification.</p> <p>If you include <code>LanguageOptions</code> in your request, you must also include <code>IdentifyLanguage</code> or <code>IdentifyMultipleLanguages</code>.</p> <p>For a list of languages supported with Amazon Transcribe streaming, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p> <important> <p>You can only include one language dialect per language per stream. For example, you cannot include <code>en-US</code> and <code>en-AU</code> in the same request.</p> </important>
            preferred_language: <p>Specify a preferred language from the subset of languages codes you specified in <code>LanguageOptions</code>.</p> <p>You can only use this parameter if you've included <code>IdentifyLanguage</code> and <code>LanguageOptions</code> in your request.</p>
            identify_multiple_languages: <p>Enables automatic multi-language identification in your transcription job request. Use this parameter if your stream contains more than one language. If your stream contains only one language, use IdentifyLanguage instead.</p> <p>If you include <code>IdentifyMultipleLanguages</code>, you must include a list of language codes, using <code>LanguageOptions</code>, that you think may be present in your stream.</p> <p>If you want to apply a custom vocabulary or a custom vocabulary filter to your automatic multiple language identification request, include <code>VocabularyNames</code> or <code>VocabularyFilterNames</code>.</p> <p>Note that you must include one of <code>LanguageCode</code>, <code>IdentifyLanguage</code>, or <code>IdentifyMultipleLanguages</code> in your request. If you include more than one of these parameters, your transcription job fails.</p>
            vocabulary_names: <p>Specify the names of the custom vocabularies that you want to use when processing your transcription. Note that vocabulary names are case sensitive.</p> <p>If none of the languages of the specified custom vocabularies match the language identified in your media, your job fails.</p> <important> <p>This parameter is only intended for use <b>with</b> the <code>IdentifyLanguage</code> parameter. If you're <b>not</b> including <code>IdentifyLanguage</code> in your request and want to use a custom vocabulary with your transcription, use the <code>VocabularyName</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>
            vocabulary_filter_names: <p>Specify the names of the custom vocabulary filters that you want to use when processing your transcription. Note that vocabulary filter names are case sensitive.</p> <p>If none of the languages of the specified custom vocabulary filters match the language identified in your media, your job fails.</p> <important> <p>This parameter is only intended for use <b>with</b> the <code>IdentifyLanguage</code> parameter. If you're <b>not</b> including <code>IdentifyLanguage</code> in your request and want to use a custom vocabulary filter with your transcription, use the <code>VocabularyFilterName</code> parameter instead.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Using vocabulary filtering with unwanted words</a>.</p>
            session_resume_window: <p>Specify the time window, in minutes, during which your transcription session can be resumed, measured from the stream start time. This optional parameter accepts integer values from 1 to 300 (5 hours).</p> <p> For example, if your stream starts at 1 PM and you specify a <code>SessionResumeWindow</code> of 30 minutes, you can reconnect to the session as many times as you want until 1:30 PM. </p>
            transcript_format: <p>Specify how numbers, dates, and other alphanumeric entities are rendered in your transcription results.</p> <ul> <li> <p> <code>WRITTEN</code> renders these entities in their standard written form (for example, <code>$50</code>, <code>10:30 AM</code>, and <code>101</code>).</p> </li> <li> <p> <code>SPOKEN</code> renders these entities as words, exactly as they were spoken (for example, <code>fifty dollars</code>, <code>ten thirty a m</code>, and <code>one oh one</code>).</p> </li> </ul> <p>If you don't specify a value, Amazon Transcribe uses <code>WRITTEN</code> by default.</p>

        Raises:
            capo_transcribe_streaming.errors.bad_request_exception.BadRequestException: <p>One or more arguments to the <code>StartStreamTranscription</code>, <code>StartMedicalStreamTranscription</code>, or <code>StartCallAnalyticsStreamTranscription</code> operation was not valid. For example, <code>MediaEncoding</code> or <code>LanguageCode</code> used unsupported values. Check the specified parameters and try your request again.</p>
            capo_transcribe_streaming.errors.conflict_exception.ConflictException: <p>A new stream started with the same session ID. The current stream has been terminated.</p>
            capo_transcribe_streaming.errors.internal_failure_exception.InternalFailureException: <p>A problem occurred while processing the audio. Amazon Transcribe terminated processing.</p>
            capo_transcribe_streaming.errors.limit_exceeded_exception.LimitExceededException: <p>Your client has exceeded one of the Amazon Transcribe limits, typically the concurrent stream service quota. This error can also occur if a stream exceeds the maximum session duration. In rare cases, this error can also occur if you increase your number of concurrent streams too quickly. Reduce your number of concurrent streams and try your request again using an exponential backoff strategy.</p>
            capo_transcribe_streaming.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable. Try your request later.</p>
            capo_transcribe_streaming.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe_streaming.types.start_stream_transcription_request.StartStreamTranscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe_streaming.types.start_stream_transcription_response.StartStreamTranscriptionResponse"
        ]:
            import capo_transcribe_streaming._operations.transcribe.start_stream_transcription

            (
                output,
                http_response,
            ) = await capo_transcribe_streaming._operations.transcribe.start_stream_transcription.async_start_stream_transcription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe_streaming.types.start_stream_transcription_request.StartStreamTranscriptionRequest = {
            "media_sample_rate_hertz": media_sample_rate_hertz,
            "media_encoding": media_encoding,
            "audio_stream": ensure_async_iterator(audio_stream),
        }
        if language_code is not None:
            input_["language_code"] = language_code
        if vocabulary_name is not None:
            input_["vocabulary_name"] = vocabulary_name
        if session_id is not None:
            input_["session_id"] = session_id
        if vocabulary_filter_name is not None:
            input_["vocabulary_filter_name"] = vocabulary_filter_name
        if vocabulary_filter_method is not None:
            input_["vocabulary_filter_method"] = vocabulary_filter_method
        if show_speaker_label is not None:
            input_["show_speaker_label"] = show_speaker_label
        if enable_channel_identification is not None:
            input_["enable_channel_identification"] = enable_channel_identification
        if number_of_channels is not None:
            input_["number_of_channels"] = number_of_channels
        if enable_partial_results_stabilization is not None:
            input_["enable_partial_results_stabilization"] = (
                enable_partial_results_stabilization
            )
        if partial_results_stability is not None:
            input_["partial_results_stability"] = partial_results_stability
        if content_identification_type is not None:
            input_["content_identification_type"] = content_identification_type
        if content_redaction_type is not None:
            input_["content_redaction_type"] = content_redaction_type
        if pii_entity_types is not None:
            input_["pii_entity_types"] = pii_entity_types
        if language_model_name is not None:
            input_["language_model_name"] = language_model_name
        if identify_language is not None:
            input_["identify_language"] = identify_language
        if language_options is not None:
            input_["language_options"] = language_options
        if preferred_language is not None:
            input_["preferred_language"] = preferred_language
        if identify_multiple_languages is not None:
            input_["identify_multiple_languages"] = identify_multiple_languages
        if vocabulary_names is not None:
            input_["vocabulary_names"] = vocabulary_names
        if vocabulary_filter_names is not None:
            input_["vocabulary_filter_names"] = vocabulary_filter_names
        if session_resume_window is not None:
            input_["session_resume_window"] = session_resume_window
        if transcript_format is not None:
            input_["transcript_format"] = transcript_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
