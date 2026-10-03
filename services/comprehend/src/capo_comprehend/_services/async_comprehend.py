"""Generated from Smithy shape ``com.amazonaws.comprehend#Comprehend_20171127``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_comprehend._auth._signers
import capo_comprehend._auth._sigv4
from capo_comprehend._auth._identity import Credentials
from capo_comprehend._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_comprehend._auth._zapros_handler import AuthMiddleware
from capo_comprehend._pagination import resolve_path as _resolve_path
from capo_comprehend._services._aws_config import aaws_config
from capo_comprehend._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_comprehend.types.batch_detect_dominant_language_request
    import capo_comprehend.types.batch_detect_dominant_language_response
    import capo_comprehend.types.batch_detect_entities_request
    import capo_comprehend.types.batch_detect_entities_response
    import capo_comprehend.types.batch_detect_key_phrases_request
    import capo_comprehend.types.batch_detect_key_phrases_response
    import capo_comprehend.types.batch_detect_sentiment_request
    import capo_comprehend.types.batch_detect_sentiment_response
    import capo_comprehend.types.batch_detect_syntax_request
    import capo_comprehend.types.batch_detect_syntax_response
    import capo_comprehend.types.batch_detect_targeted_sentiment_request
    import capo_comprehend.types.batch_detect_targeted_sentiment_response
    import capo_comprehend.types.classify_document_request
    import capo_comprehend.types.classify_document_response
    import capo_comprehend.types.client_request_token_string
    import capo_comprehend.types.comprehend_arn
    import capo_comprehend.types.comprehend_arn_name
    import capo_comprehend.types.comprehend_dataset_arn
    import capo_comprehend.types.comprehend_endpoint_arn
    import capo_comprehend.types.comprehend_endpoint_name
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.contains_pii_entities_request
    import capo_comprehend.types.contains_pii_entities_response
    import capo_comprehend.types.create_dataset_request
    import capo_comprehend.types.create_dataset_response
    import capo_comprehend.types.create_document_classifier_request
    import capo_comprehend.types.create_document_classifier_response
    import capo_comprehend.types.create_endpoint_request
    import capo_comprehend.types.create_endpoint_response
    import capo_comprehend.types.create_entity_recognizer_request
    import capo_comprehend.types.create_entity_recognizer_response
    import capo_comprehend.types.create_flywheel_request
    import capo_comprehend.types.create_flywheel_response
    import capo_comprehend.types.customer_input_string
    import capo_comprehend.types.customer_input_string_list
    import capo_comprehend.types.data_security_config
    import capo_comprehend.types.dataset_filter
    import capo_comprehend.types.dataset_input_data_config
    import capo_comprehend.types.dataset_type
    import capo_comprehend.types.delete_document_classifier_request
    import capo_comprehend.types.delete_document_classifier_response
    import capo_comprehend.types.delete_endpoint_request
    import capo_comprehend.types.delete_endpoint_response
    import capo_comprehend.types.delete_entity_recognizer_request
    import capo_comprehend.types.delete_entity_recognizer_response
    import capo_comprehend.types.delete_flywheel_request
    import capo_comprehend.types.delete_flywheel_response
    import capo_comprehend.types.delete_resource_policy_request
    import capo_comprehend.types.delete_resource_policy_response
    import capo_comprehend.types.describe_dataset_request
    import capo_comprehend.types.describe_dataset_response
    import capo_comprehend.types.describe_document_classification_job_request
    import capo_comprehend.types.describe_document_classification_job_response
    import capo_comprehend.types.describe_document_classifier_request
    import capo_comprehend.types.describe_document_classifier_response
    import capo_comprehend.types.describe_dominant_language_detection_job_request
    import capo_comprehend.types.describe_dominant_language_detection_job_response
    import capo_comprehend.types.describe_endpoint_request
    import capo_comprehend.types.describe_endpoint_response
    import capo_comprehend.types.describe_entities_detection_job_request
    import capo_comprehend.types.describe_entities_detection_job_response
    import capo_comprehend.types.describe_entity_recognizer_request
    import capo_comprehend.types.describe_entity_recognizer_response
    import capo_comprehend.types.describe_events_detection_job_request
    import capo_comprehend.types.describe_events_detection_job_response
    import capo_comprehend.types.describe_flywheel_iteration_request
    import capo_comprehend.types.describe_flywheel_iteration_response
    import capo_comprehend.types.describe_flywheel_request
    import capo_comprehend.types.describe_flywheel_response
    import capo_comprehend.types.describe_key_phrases_detection_job_request
    import capo_comprehend.types.describe_key_phrases_detection_job_response
    import capo_comprehend.types.describe_pii_entities_detection_job_request
    import capo_comprehend.types.describe_pii_entities_detection_job_response
    import capo_comprehend.types.describe_resource_policy_request
    import capo_comprehend.types.describe_resource_policy_response
    import capo_comprehend.types.describe_sentiment_detection_job_request
    import capo_comprehend.types.describe_sentiment_detection_job_response
    import capo_comprehend.types.describe_targeted_sentiment_detection_job_request
    import capo_comprehend.types.describe_targeted_sentiment_detection_job_response
    import capo_comprehend.types.describe_topics_detection_job_request
    import capo_comprehend.types.describe_topics_detection_job_response
    import capo_comprehend.types.description
    import capo_comprehend.types.detect_dominant_language_request
    import capo_comprehend.types.detect_dominant_language_response
    import capo_comprehend.types.detect_entities_request
    import capo_comprehend.types.detect_entities_response
    import capo_comprehend.types.detect_key_phrases_request
    import capo_comprehend.types.detect_key_phrases_response
    import capo_comprehend.types.detect_pii_entities_request
    import capo_comprehend.types.detect_pii_entities_response
    import capo_comprehend.types.detect_sentiment_request
    import capo_comprehend.types.detect_sentiment_response
    import capo_comprehend.types.detect_syntax_request
    import capo_comprehend.types.detect_syntax_response
    import capo_comprehend.types.detect_targeted_sentiment_request
    import capo_comprehend.types.detect_targeted_sentiment_response
    import capo_comprehend.types.detect_toxic_content_request
    import capo_comprehend.types.detect_toxic_content_response
    import capo_comprehend.types.document_classification_job_filter
    import capo_comprehend.types.document_classifier_arn
    import capo_comprehend.types.document_classifier_endpoint_arn
    import capo_comprehend.types.document_classifier_filter
    import capo_comprehend.types.document_classifier_input_data_config
    import capo_comprehend.types.document_classifier_mode
    import capo_comprehend.types.document_classifier_output_data_config
    import capo_comprehend.types.document_reader_config
    import capo_comprehend.types.dominant_language_detection_job_filter
    import capo_comprehend.types.endpoint_filter
    import capo_comprehend.types.endpoint_properties
    import capo_comprehend.types.entities_detection_job_filter
    import capo_comprehend.types.entity_recognizer_arn
    import capo_comprehend.types.entity_recognizer_endpoint_arn
    import capo_comprehend.types.entity_recognizer_filter
    import capo_comprehend.types.entity_recognizer_input_data_config
    import capo_comprehend.types.events_detection_job_filter
    import capo_comprehend.types.flywheel_filter
    import capo_comprehend.types.flywheel_iteration_filter
    import capo_comprehend.types.flywheel_iteration_id
    import capo_comprehend.types.flywheel_s3_uri
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.import_model_request
    import capo_comprehend.types.import_model_response
    import capo_comprehend.types.inference_units_integer
    import capo_comprehend.types.input_data_config
    import capo_comprehend.types.job_id
    import capo_comprehend.types.job_name
    import capo_comprehend.types.key_phrases_detection_job_filter
    import capo_comprehend.types.kms_key_id
    import capo_comprehend.types.language_code
    import capo_comprehend.types.list_datasets_request
    import capo_comprehend.types.list_datasets_response
    import capo_comprehend.types.list_document_classification_jobs_request
    import capo_comprehend.types.list_document_classification_jobs_response
    import capo_comprehend.types.list_document_classifier_summaries_request
    import capo_comprehend.types.list_document_classifier_summaries_response
    import capo_comprehend.types.list_document_classifiers_request
    import capo_comprehend.types.list_document_classifiers_response
    import capo_comprehend.types.list_dominant_language_detection_jobs_request
    import capo_comprehend.types.list_dominant_language_detection_jobs_response
    import capo_comprehend.types.list_endpoints_request
    import capo_comprehend.types.list_endpoints_response
    import capo_comprehend.types.list_entities_detection_jobs_request
    import capo_comprehend.types.list_entities_detection_jobs_response
    import capo_comprehend.types.list_entity_recognizer_summaries_request
    import capo_comprehend.types.list_entity_recognizer_summaries_response
    import capo_comprehend.types.list_entity_recognizers_request
    import capo_comprehend.types.list_entity_recognizers_response
    import capo_comprehend.types.list_events_detection_jobs_request
    import capo_comprehend.types.list_events_detection_jobs_response
    import capo_comprehend.types.list_flywheel_iteration_history_request
    import capo_comprehend.types.list_flywheel_iteration_history_response
    import capo_comprehend.types.list_flywheels_request
    import capo_comprehend.types.list_flywheels_response
    import capo_comprehend.types.list_key_phrases_detection_jobs_request
    import capo_comprehend.types.list_key_phrases_detection_jobs_response
    import capo_comprehend.types.list_of_text_segments
    import capo_comprehend.types.list_pii_entities_detection_jobs_request
    import capo_comprehend.types.list_pii_entities_detection_jobs_response
    import capo_comprehend.types.list_sentiment_detection_jobs_request
    import capo_comprehend.types.list_sentiment_detection_jobs_response
    import capo_comprehend.types.list_tags_for_resource_request
    import capo_comprehend.types.list_tags_for_resource_response
    import capo_comprehend.types.list_targeted_sentiment_detection_jobs_request
    import capo_comprehend.types.list_targeted_sentiment_detection_jobs_response
    import capo_comprehend.types.list_topics_detection_jobs_request
    import capo_comprehend.types.list_topics_detection_jobs_response
    import capo_comprehend.types.max_results_integer
    import capo_comprehend.types.model_type
    import capo_comprehend.types.number_of_topics_integer
    import capo_comprehend.types.output_data_config
    import capo_comprehend.types.pii_entities_detection_job_filter
    import capo_comprehend.types.pii_entities_detection_job_properties
    import capo_comprehend.types.pii_entities_detection_mode
    import capo_comprehend.types.policy
    import capo_comprehend.types.policy_revision_id
    import capo_comprehend.types.put_resource_policy_request
    import capo_comprehend.types.put_resource_policy_response
    import capo_comprehend.types.redaction_config
    import capo_comprehend.types.semi_structured_document_blob
    import capo_comprehend.types.sentiment_detection_job_filter
    import capo_comprehend.types.start_document_classification_job_request
    import capo_comprehend.types.start_document_classification_job_response
    import capo_comprehend.types.start_dominant_language_detection_job_request
    import capo_comprehend.types.start_dominant_language_detection_job_response
    import capo_comprehend.types.start_entities_detection_job_request
    import capo_comprehend.types.start_entities_detection_job_response
    import capo_comprehend.types.start_events_detection_job_request
    import capo_comprehend.types.start_events_detection_job_response
    import capo_comprehend.types.start_flywheel_iteration_request
    import capo_comprehend.types.start_flywheel_iteration_response
    import capo_comprehend.types.start_key_phrases_detection_job_request
    import capo_comprehend.types.start_key_phrases_detection_job_response
    import capo_comprehend.types.start_pii_entities_detection_job_request
    import capo_comprehend.types.start_pii_entities_detection_job_response
    import capo_comprehend.types.start_sentiment_detection_job_request
    import capo_comprehend.types.start_sentiment_detection_job_response
    import capo_comprehend.types.start_targeted_sentiment_detection_job_request
    import capo_comprehend.types.start_targeted_sentiment_detection_job_response
    import capo_comprehend.types.start_topics_detection_job_request
    import capo_comprehend.types.start_topics_detection_job_response
    import capo_comprehend.types.stop_dominant_language_detection_job_request
    import capo_comprehend.types.stop_dominant_language_detection_job_response
    import capo_comprehend.types.stop_entities_detection_job_request
    import capo_comprehend.types.stop_entities_detection_job_response
    import capo_comprehend.types.stop_events_detection_job_request
    import capo_comprehend.types.stop_events_detection_job_response
    import capo_comprehend.types.stop_key_phrases_detection_job_request
    import capo_comprehend.types.stop_key_phrases_detection_job_response
    import capo_comprehend.types.stop_pii_entities_detection_job_request
    import capo_comprehend.types.stop_pii_entities_detection_job_response
    import capo_comprehend.types.stop_sentiment_detection_job_request
    import capo_comprehend.types.stop_sentiment_detection_job_response
    import capo_comprehend.types.stop_targeted_sentiment_detection_job_request
    import capo_comprehend.types.stop_targeted_sentiment_detection_job_response
    import capo_comprehend.types.stop_training_document_classifier_request
    import capo_comprehend.types.stop_training_document_classifier_response
    import capo_comprehend.types.stop_training_entity_recognizer_request
    import capo_comprehend.types.stop_training_entity_recognizer_response
    import capo_comprehend.types.string
    import capo_comprehend.types.syntax_language_code
    import capo_comprehend.types.tag_key_list
    import capo_comprehend.types.tag_list
    import capo_comprehend.types.tag_resource_request
    import capo_comprehend.types.tag_resource_response
    import capo_comprehend.types.target_event_types
    import capo_comprehend.types.targeted_sentiment_detection_job_filter
    import capo_comprehend.types.task_config
    import capo_comprehend.types.topics_detection_job_filter
    import capo_comprehend.types.untag_resource_request
    import capo_comprehend.types.untag_resource_response
    import capo_comprehend.types.update_data_security_config
    import capo_comprehend.types.update_endpoint_request
    import capo_comprehend.types.update_endpoint_response
    import capo_comprehend.types.update_flywheel_request
    import capo_comprehend.types.update_flywheel_response
    import capo_comprehend.types.version_name
    import capo_comprehend.types.vpc_config


class AsyncComprehendClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncComprehendClient:
    """A client for the ``Comprehend`` service.

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
        self._config = AsyncComprehendClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncComprehendClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncComprehendClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def batch_detect_dominant_language(
        self,
        text_list: "capo_comprehend.types.customer_input_string_list.CustomerInputStringList",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.batch_detect_dominant_language_response.BatchDetectDominantLanguageResponse":
        """<p>Determines the dominant language of the input text for a batch of documents. For a list of languages that Amazon Comprehend can detect, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html">Amazon Comprehend Supported Languages</a>. </p>

        Args:
            text_list: <p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. Each document should contain at least 20 characters. The maximum size of each document is 5 KB.</p>

        Raises:
            capo_comprehend.errors.batch_size_limit_exceeded_exception.BatchSizeLimitExceededException: <p>The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.</p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.batch_detect_dominant_language_request.BatchDetectDominantLanguageRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.batch_detect_dominant_language_response.BatchDetectDominantLanguageResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.batch_detect_dominant_language

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.batch_detect_dominant_language.async_batch_detect_dominant_language(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.batch_detect_dominant_language_request.BatchDetectDominantLanguageRequest = {
            "text_list": text_list
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_detect_entities(
        self,
        text_list: "capo_comprehend.types.customer_input_string_list.CustomerInputStringList",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.batch_detect_entities_response.BatchDetectEntitiesResponse":
        """<p>Inspects the text of a batch of documents for named entities and returns information about them. For more information about named entities, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html">Entities</a> in the Comprehend Developer Guide. </p>

        Args:
            text_list: <p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>

        Raises:
            capo_comprehend.errors.batch_size_limit_exceeded_exception.BatchSizeLimitExceededException: <p>The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.</p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.batch_detect_entities_request.BatchDetectEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.batch_detect_entities_response.BatchDetectEntitiesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.batch_detect_entities

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.batch_detect_entities.async_batch_detect_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.batch_detect_entities_request.BatchDetectEntitiesRequest = {
            "text_list": text_list,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_detect_key_phrases(
        self,
        text_list: "capo_comprehend.types.customer_input_string_list.CustomerInputStringList",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.batch_detect_key_phrases_response.BatchDetectKeyPhrasesResponse":
        """<p>Detects the key noun phrases found in a batch of documents.</p>

        Args:
            text_list: <p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>

        Raises:
            capo_comprehend.errors.batch_size_limit_exceeded_exception.BatchSizeLimitExceededException: <p>The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.</p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.batch_detect_key_phrases_request.BatchDetectKeyPhrasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.batch_detect_key_phrases_response.BatchDetectKeyPhrasesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.batch_detect_key_phrases

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.batch_detect_key_phrases.async_batch_detect_key_phrases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.batch_detect_key_phrases_request.BatchDetectKeyPhrasesRequest = {
            "text_list": text_list,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_detect_sentiment(
        self,
        text_list: "capo_comprehend.types.customer_input_string_list.CustomerInputStringList",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.batch_detect_sentiment_response.BatchDetectSentimentResponse":
        """<p>Inspects a batch of documents and returns an inference of the prevailing sentiment, <code>POSITIVE</code>, <code>NEUTRAL</code>, <code>MIXED</code>, or <code>NEGATIVE</code>, in each one.</p>

        Args:
            text_list: <p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB. </p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>

        Raises:
            capo_comprehend.errors.batch_size_limit_exceeded_exception.BatchSizeLimitExceededException: <p>The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.</p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.batch_detect_sentiment_request.BatchDetectSentimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.batch_detect_sentiment_response.BatchDetectSentimentResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.batch_detect_sentiment

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.batch_detect_sentiment.async_batch_detect_sentiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.batch_detect_sentiment_request.BatchDetectSentimentRequest = {
            "text_list": text_list,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_detect_syntax(
        self,
        text_list: "capo_comprehend.types.customer_input_string_list.CustomerInputStringList",
        language_code: "capo_comprehend.types.syntax_language_code.SyntaxLanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.batch_detect_syntax_response.BatchDetectSyntaxResponse":
        """<p>Inspects the text of a batch of documents for the syntax and part of speech of the words in the document and returns information about them. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html">Syntax</a> in the Comprehend Developer Guide. </p>

        Args:
            text_list: <p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size for each document is 5 KB.</p>
            language_code: <p>The language of the input documents. You can specify any of the following languages supported by Amazon Comprehend: German ("de"), English ("en"), Spanish ("es"), French ("fr"), Italian ("it"), or Portuguese ("pt"). All documents must be in the same language.</p>

        Raises:
            capo_comprehend.errors.batch_size_limit_exceeded_exception.BatchSizeLimitExceededException: <p>The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.</p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.batch_detect_syntax_request.BatchDetectSyntaxRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.batch_detect_syntax_response.BatchDetectSyntaxResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.batch_detect_syntax

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.batch_detect_syntax.async_batch_detect_syntax(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.batch_detect_syntax_request.BatchDetectSyntaxRequest = {
            "text_list": text_list,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_detect_targeted_sentiment(
        self,
        text_list: "capo_comprehend.types.customer_input_string_list.CustomerInputStringList",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.batch_detect_targeted_sentiment_response.BatchDetectTargetedSentimentResponse":
        """<p>Inspects a batch of documents and returns a sentiment analysis for each entity identified in the documents.</p> <p>For more information about targeted sentiment, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html">Targeted sentiment</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            text_list: <p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. The maximum size of each document is 5 KB.</p>
            language_code: <p>The language of the input documents. Currently, English is the only supported language.</p>

        Raises:
            capo_comprehend.errors.batch_size_limit_exceeded_exception.BatchSizeLimitExceededException: <p>The number of documents in the request exceeds the limit of 25. Try your request again with fewer documents.</p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.batch_detect_targeted_sentiment_request.BatchDetectTargetedSentimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.batch_detect_targeted_sentiment_response.BatchDetectTargetedSentimentResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.batch_detect_targeted_sentiment

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.batch_detect_targeted_sentiment.async_batch_detect_targeted_sentiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.batch_detect_targeted_sentiment_request.BatchDetectTargetedSentimentRequest = {
            "text_list": text_list,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def classify_document(
        self,
        endpoint_arn: "capo_comprehend.types.document_classifier_endpoint_arn.DocumentClassifierEndpointArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        text: Optional[
            "capo_comprehend.types.customer_input_string.CustomerInputString"
        ] = None,
        bytes: Optional[
            "capo_comprehend.types.semi_structured_document_blob.SemiStructuredDocumentBlob"
        ] = None,
        document_reader_config: Optional[
            "capo_comprehend.types.document_reader_config.DocumentReaderConfig"
        ] = None,
    ) -> "capo_comprehend.types.classify_document_response.ClassifyDocumentResponse":
        """<p>Creates a classification request to analyze a single document in real-time. <code>ClassifyDocument</code> supports the following model types:</p> <ul> <li> <p>Custom classifier - a custom model that you have created and trained. For input, you can provide plain text, a single-page document (PDF, Word, or image), or Amazon Textract API output. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html">Custom classification</a> in the <i>Amazon Comprehend Developer Guide</i>.</p> </li> <li> <p>Prompt safety classifier - Amazon Comprehend provides a pre-trained model for classifying input prompts for generative AI applications. For input, you provide English plain text input. For prompt safety classification, the response includes only the <code>Classes</code> field. For more information about prompt safety classifiers, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification">Prompt safety classification</a> in the <i>Amazon Comprehend Developer Guide</i>.</p> </li> </ul> <p>If the system detects errors while processing a page in the input document, the API response includes an <code>Errors</code> field that describes the errors.</p> <p>If the system detects a document-level error in your input document, the API returns an <code>InvalidRequestException</code> error response. For details about this exception, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync-err.html"> Errors in semi-structured documents</a> in the Comprehend Developer Guide. </p>

        Args:
            text: <p>The document text to be analyzed. If you enter text using this parameter, do not use the <code>Bytes</code> parameter.</p>
            endpoint_arn: <p>The Amazon Resource Number (ARN) of the endpoint. </p> <p>For prompt safety classification, Amazon Comprehend provides the endpoint ARN. For more information about prompt safety classifiers, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#prompt-classification">Prompt safety classification</a> in the <i>Amazon Comprehend Developer Guide</i> </p> <p>For custom classification, you create an endpoint for your custom model. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/using-endpoints.html">Using Amazon Comprehend endpoints</a>.</p>
            bytes: <p>Use the <code>Bytes</code> parameter to input a text, PDF, Word or image file.</p> <p>When you classify a document using a custom model, you can also use the <code>Bytes</code> parameter to input an Amazon Textract <code>DetectDocumentText</code> or <code>AnalyzeDocument</code> output file.</p> <p>To classify a document using the prompt safety classifier, use the <code>Text</code> parameter for input.</p> <p>Provide the input document as a sequence of base64-encoded bytes. If your code uses an Amazon Web Services SDK to classify documents, the SDK may encode the document file bytes for you. </p> <p>The maximum length of this field depends on the input document type. For details, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html"> Inputs for real-time custom analysis</a> in the Comprehend Developer Guide. </p> <p>If you use the <code>Bytes</code> parameter, do not use the <code>Text</code> parameter.</p>
            document_reader_config: <p>Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.classify_document_request.ClassifyDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.classify_document_response.ClassifyDocumentResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.classify_document

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.classify_document.async_classify_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.classify_document_request.ClassifyDocumentRequest = {
            "endpoint_arn": endpoint_arn
        }
        if text is not None:
            input_["text"] = text
        if bytes is not None:
            input_["bytes"] = bytes
        if document_reader_config is not None:
            input_["document_reader_config"] = document_reader_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def contains_pii_entities(
        self,
        text: "capo_comprehend.types.string.String",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.contains_pii_entities_response.ContainsPiiEntitiesResponse":
        """<p>Analyzes input text for the presence of personally identifiable information (PII) and returns the labels of identified PII entity types such as name, address, bank account number, or phone number.</p>

        Args:
            text: <p>A UTF-8 text string. The maximum string size is 100 KB.</p>
            language_code: <p>The language of the input documents.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.contains_pii_entities_request.ContainsPiiEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.contains_pii_entities_response.ContainsPiiEntitiesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.contains_pii_entities

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.contains_pii_entities.async_contains_pii_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.contains_pii_entities_request.ContainsPiiEntitiesRequest = {
            "text": text,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        dataset_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName",
        input_data_config: "capo_comprehend.types.dataset_input_data_config.DatasetInputDataConfig",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        dataset_type: Optional["capo_comprehend.types.dataset_type.DatasetType"] = None,
        description: Optional["capo_comprehend.types.description.Description"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a dataset to upload training or test data for a model associated with a flywheel. For more information about datasets, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel of the flywheel to receive the data.</p>
            dataset_name: <p>Name of the dataset.</p>
            dataset_type: <p>The dataset type. You can specify that the data in a dataset is for training the model or for testing the model.</p>
            description: <p>Description of the dataset.</p>
            input_data_config: <p>Information about the input data configuration. The type of input data varies based on the format of the input and whether the data is for a classifier model or an entity recognition model.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            tags: <p>Tags for the dataset.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.create_dataset

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.create_dataset_request.CreateDatasetRequest = {
            "flywheel_arn": flywheel_arn,
            "dataset_name": dataset_name,
            "input_data_config": input_data_config,
        }
        if dataset_type is not None:
            input_["dataset_type"] = dataset_type
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_document_classifier(
        self,
        document_classifier_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        input_data_config: "capo_comprehend.types.document_classifier_input_data_config.DocumentClassifierInputDataConfig",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        version_name: Optional["capo_comprehend.types.version_name.VersionName"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
        output_data_config: Optional[
            "capo_comprehend.types.document_classifier_output_data_config.DocumentClassifierOutputDataConfig"
        ] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        mode: Optional[
            "capo_comprehend.types.document_classifier_mode.DocumentClassifierMode"
        ] = None,
        model_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        model_policy: Optional["capo_comprehend.types.policy.Policy"] = None,
    ) -> "capo_comprehend.types.create_document_classifier_response.CreateDocumentClassifierResponse":
        r"""<p>Creates a new document classifier that you can use to categorize documents. To create a classifier, you provide a set of training documents that are labeled with the categories that you want to use. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/training-classifier-model.html">Training classifier models</a> in the Comprehend Developer Guide. </p>

        Args:
            document_classifier_name: <p>The name of the document classifier.</p>
            version_name: <p>The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the Amazon Web Services account/Amazon Web Services Region.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>
            tags: <p>Tags to associate with the document classifier. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department. </p>
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies the location for the output files from a custom classifier job. This parameter is required for a request that creates a native document model.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            language_code: <p>The language of the input documents. You can specify any of the languages supported by Amazon Comprehend. All documents must be in the same language.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            mode: <p>Indicates the mode in which the classifier will be trained. The classifier can be trained in multi-class (single-label) mode or multi-label mode. Multi-class mode identifies a single class label for each document and multi-label mode identifies one or more class labels for each document. Multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (|).</p>
            model_kms_key_id: <p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            model_policy: <p>The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{"attribute": "value", "attribute": ["value"]}'</code> </p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.create_document_classifier_request.CreateDocumentClassifierRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.create_document_classifier_response.CreateDocumentClassifierResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.create_document_classifier

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.create_document_classifier.async_create_document_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.create_document_classifier_request.CreateDocumentClassifierRequest = {
            "document_classifier_name": document_classifier_name,
            "data_access_role_arn": data_access_role_arn,
            "input_data_config": input_data_config,
            "language_code": language_code,
        }
        if version_name is not None:
            input_["version_name"] = version_name
        if tags is not None:
            input_["tags"] = tags
        if output_data_config is not None:
            input_["output_data_config"] = output_data_config
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if mode is not None:
            input_["mode"] = mode
        if model_kms_key_id is not None:
            input_["model_kms_key_id"] = model_kms_key_id
        if model_policy is not None:
            input_["model_policy"] = model_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_endpoint(
        self,
        endpoint_name: "capo_comprehend.types.comprehend_endpoint_name.ComprehendEndpointName",
        desired_inference_units: "capo_comprehend.types.inference_units_integer.InferenceUnitsInteger",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        model_arn: Optional[
            "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
        ] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
        data_access_role_arn: Optional[
            "capo_comprehend.types.iam_role_arn.IamRoleArn"
        ] = None,
        flywheel_arn: Optional[
            "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
        ] = None,
    ) -> "capo_comprehend.types.create_endpoint_response.CreateEndpointResponse":
        """<p>Creates a model-specific endpoint for synchronous inference for a previously trained custom model For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>

        Args:
            endpoint_name: <p>This is the descriptive suffix that becomes part of the <code>EndpointArn</code> used for all subsequent requests to this resource. </p>
            model_arn: <p>The Amazon Resource Number (ARN) of the model to which the endpoint will be attached.</p>
            desired_inference_units: <p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>
            client_request_token: <p>An idempotency token provided by the customer. If this token matches a previous endpoint creation request, Amazon Comprehend will not return a <code>ResourceInUseException</code>. </p>
            tags: <p>Tags to associate with the endpoint. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with "Sales" as the key might be added to an endpoint to indicate its use by the sales department. </p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel to which the endpoint will be attached.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.create_endpoint_request.CreateEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.create_endpoint_response.CreateEndpointResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.create_endpoint

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.create_endpoint.async_create_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.create_endpoint_request.CreateEndpointRequest = {
            "endpoint_name": endpoint_name,
            "desired_inference_units": desired_inference_units,
        }
        if model_arn is not None:
            input_["model_arn"] = model_arn
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if flywheel_arn is not None:
            input_["flywheel_arn"] = flywheel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_entity_recognizer(
        self,
        recognizer_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        input_data_config: "capo_comprehend.types.entity_recognizer_input_data_config.EntityRecognizerInputDataConfig",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        version_name: Optional["capo_comprehend.types.version_name.VersionName"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        model_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        model_policy: Optional["capo_comprehend.types.policy.Policy"] = None,
    ) -> "capo_comprehend.types.create_entity_recognizer_response.CreateEntityRecognizerResponse":
        r"""<p>Creates an entity recognizer using submitted files. After your <code>CreateEntityRecognizer</code> request is submitted, you can check job status using the <code>DescribeEntityRecognizer</code> API. </p>

        Args:
            recognizer_name: <p>The name given to the newly created recognizer. Recognizer names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The name must be unique in the account/Region.</p>
            version_name: <p>The version name given to the newly created recognizer. Version names can be a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same recognizer name in the account/Region.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>
            tags: <p>Tags to associate with the entity recognizer. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department. </p>
            input_data_config: <p>Specifies the format and location of the input data. The S3 bucket containing the input data must be located in the same Region as the entity recognizer being created. </p>
            client_request_token: <p> A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            language_code: <p> You can specify any of the following languages: English ("en"), Spanish ("es"), French ("fr"), Italian ("it"), German ("de"), or Portuguese ("pt"). If you plan to use this entity recognizer with PDF, Word, or image input files, you must specify English as the language. All training documents must be in the same language.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom entity recognizer. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            model_kms_key_id: <p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            model_policy: <p>The JSON resource-based policy to attach to your custom entity recognizer model. You can use this policy to allow another Amazon Web Services account to import your custom model.</p> <p>Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{"attribute": "value", "attribute": ["value"]}'</code> </p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.create_entity_recognizer_request.CreateEntityRecognizerRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.create_entity_recognizer_response.CreateEntityRecognizerResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.create_entity_recognizer

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.create_entity_recognizer.async_create_entity_recognizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.create_entity_recognizer_request.CreateEntityRecognizerRequest = {
            "recognizer_name": recognizer_name,
            "data_access_role_arn": data_access_role_arn,
            "input_data_config": input_data_config,
            "language_code": language_code,
        }
        if version_name is not None:
            input_["version_name"] = version_name
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if model_kms_key_id is not None:
            input_["model_kms_key_id"] = model_kms_key_id
        if model_policy is not None:
            input_["model_policy"] = model_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_flywheel(
        self,
        flywheel_name: "capo_comprehend.types.comprehend_arn_name.ComprehendArnName",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        data_lake_s3_uri: "capo_comprehend.types.flywheel_s3_uri.FlywheelS3Uri",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        active_model_arn: Optional[
            "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
        ] = None,
        task_config: Optional["capo_comprehend.types.task_config.TaskConfig"] = None,
        model_type: Optional["capo_comprehend.types.model_type.ModelType"] = None,
        data_security_config: Optional[
            "capo_comprehend.types.data_security_config.DataSecurityConfig"
        ] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.create_flywheel_response.CreateFlywheelResponse":
        """<p>A flywheel is an Amazon Web Services resource that orchestrates the ongoing training of a model for custom classification or custom entity recognition. You can create a flywheel to start with an existing trained model, or Comprehend can create and train a new model.</p> <p>When you create the flywheel, Comprehend creates a data lake in your account. The data lake holds the training data and test data for all versions of the model.</p> <p>To use a flywheel with an existing trained model, you specify the active model version. Comprehend copies the model's training data and test data into the flywheel's data lake.</p> <p>To use the flywheel with a new model, you need to provide a dataset for training data (and optional test data) when you create the flywheel.</p> <p>For more information about flywheels, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_name: <p>Name for the flywheel.</p>
            active_model_arn: <p>To associate an existing model with the flywheel, specify the Amazon Resource Number (ARN) of the model version. Do not set <code>TaskConfig</code> or <code>ModelType</code> if you specify an <code>ActiveModelArn</code>.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend the permissions required to access the flywheel data in the data lake.</p>
            task_config: <p>Configuration about the model associated with the flywheel. You need to set <code>TaskConfig</code> if you are creating a flywheel for a new model.</p>
            model_type: <p>The model type. You need to set <code>ModelType</code> if you are creating a flywheel for a new model.</p>
            data_lake_s3_uri: <p>Enter the S3 location for the data lake. You can specify a new S3 bucket or a new folder of an existing S3 bucket. The flywheel creates the data lake at this location.</p>
            data_security_config: <p>Data security configurations.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            tags: <p>The tags to associate with this flywheel.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.create_flywheel_request.CreateFlywheelRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.create_flywheel_response.CreateFlywheelResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.create_flywheel

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.create_flywheel.async_create_flywheel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.create_flywheel_request.CreateFlywheelRequest = {
            "flywheel_name": flywheel_name,
            "data_access_role_arn": data_access_role_arn,
            "data_lake_s3_uri": data_lake_s3_uri,
        }
        if active_model_arn is not None:
            input_["active_model_arn"] = active_model_arn
        if task_config is not None:
            input_["task_config"] = task_config
        if model_type is not None:
            input_["model_type"] = model_type
        if data_security_config is not None:
            input_["data_security_config"] = data_security_config
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_document_classifier(
        self,
        document_classifier_arn: "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.delete_document_classifier_response.DeleteDocumentClassifierResponse":
        """<p>Deletes a previously created document classifier</p> <p>Only those classifiers that are in terminated states (IN_ERROR, TRAINED) will be deleted. If an active inference job is using the model, a <code>ResourceInUseException</code> will be returned.</p> <p>This is an asynchronous action that puts the classifier into a DELETING state, and it is then removed by a background job. Once removed, the classifier disappears from your account and is no longer available for use. </p>

        Args:
            document_classifier_arn: <p>The Amazon Resource Name (ARN) that identifies the document classifier. </p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.delete_document_classifier_request.DeleteDocumentClassifierRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.delete_document_classifier_response.DeleteDocumentClassifierResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.delete_document_classifier

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.delete_document_classifier.async_delete_document_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.delete_document_classifier_request.DeleteDocumentClassifierRequest = {
            "document_classifier_arn": document_classifier_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_endpoint(
        self,
        endpoint_arn: "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.delete_endpoint_response.DeleteEndpointResponse":
        """<p>Deletes a model-specific endpoint for a previously-trained custom model. All endpoints must be deleted in order for the model to be deleted. For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Number (ARN) of the endpoint being deleted.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.delete_endpoint_request.DeleteEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.delete_endpoint_response.DeleteEndpointResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.delete_endpoint

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.delete_endpoint.async_delete_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.delete_endpoint_request.DeleteEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_entity_recognizer(
        self,
        entity_recognizer_arn: "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.delete_entity_recognizer_response.DeleteEntityRecognizerResponse":
        """<p>Deletes an entity recognizer.</p> <p>Only those recognizers that are in terminated states (IN_ERROR, TRAINED) will be deleted. If an active inference job is using the model, a <code>ResourceInUseException</code> will be returned.</p> <p>This is an asynchronous action that puts the recognizer into a DELETING state, and it is then removed by a background job. Once removed, the recognizer disappears from your account and is no longer available for use. </p>

        Args:
            entity_recognizer_arn: <p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.delete_entity_recognizer_request.DeleteEntityRecognizerRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.delete_entity_recognizer_response.DeleteEntityRecognizerResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.delete_entity_recognizer

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.delete_entity_recognizer.async_delete_entity_recognizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.delete_entity_recognizer_request.DeleteEntityRecognizerRequest = {
            "entity_recognizer_arn": entity_recognizer_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_flywheel(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.delete_flywheel_response.DeleteFlywheelResponse":
        """<p>Deletes a flywheel. When you delete the flywheel, Amazon Comprehend does not delete the data lake or the model associated with the flywheel.</p> <p>For more information about flywheels, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel to delete.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.delete_flywheel_request.DeleteFlywheelRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.delete_flywheel_response.DeleteFlywheelResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.delete_flywheel

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.delete_flywheel.async_delete_flywheel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.delete_flywheel_request.DeleteFlywheelRequest = {
            "flywheel_arn": flywheel_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        policy_revision_id: Optional[
            "capo_comprehend.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_comprehend.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource-based policy that is attached to a custom model.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the custom model version that has the policy to delete.</p>
            policy_revision_id: <p>The revision ID of the policy to delete.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset(
        self,
        dataset_arn: "capo_comprehend.types.comprehend_dataset_arn.ComprehendDatasetArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Returns information about the dataset that you specify. For more information about datasets, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            dataset_arn: <p>The ARN of the dataset.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_dataset

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_dataset_request.DescribeDatasetRequest = {
            "dataset_arn": dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_document_classification_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_document_classification_job_response.DescribeDocumentClassificationJobResponse":
        """<p>Gets the properties associated with a document classification job. Use this operation to get the status of a classification job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The <code>StartDocumentClassificationJob</code> operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_document_classification_job_request.DescribeDocumentClassificationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_document_classification_job_response.DescribeDocumentClassificationJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_document_classification_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_document_classification_job.async_describe_document_classification_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_document_classification_job_request.DescribeDocumentClassificationJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_document_classifier(
        self,
        document_classifier_arn: "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_document_classifier_response.DescribeDocumentClassifierResponse":
        """<p>Gets the properties associated with a document classifier.</p>

        Args:
            document_classifier_arn: <p>The Amazon Resource Name (ARN) that identifies the document classifier. The <code>CreateDocumentClassifier</code> operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_document_classifier_request.DescribeDocumentClassifierRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_document_classifier_response.DescribeDocumentClassifierResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_document_classifier

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_document_classifier.async_describe_document_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_document_classifier_request.DescribeDocumentClassifierRequest = {
            "document_classifier_arn": document_classifier_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dominant_language_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_dominant_language_detection_job_response.DescribeDominantLanguageDetectionJobResponse":
        """<p>Gets the properties associated with a dominant language detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The <code>StartDominantLanguageDetectionJob</code> operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_dominant_language_detection_job_request.DescribeDominantLanguageDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_dominant_language_detection_job_response.DescribeDominantLanguageDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_dominant_language_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_dominant_language_detection_job.async_describe_dominant_language_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_dominant_language_detection_job_request.DescribeDominantLanguageDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_endpoint(
        self,
        endpoint_arn: "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_endpoint_response.DescribeEndpointResponse":
        """<p>Gets the properties associated with a specific endpoint. Use this operation to get the status of an endpoint. For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Number (ARN) of the endpoint being described.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_endpoint_request.DescribeEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_endpoint_response.DescribeEndpointResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_endpoint

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_endpoint.async_describe_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_endpoint_request.DescribeEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_entities_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_entities_detection_job_response.DescribeEntitiesDetectionJobResponse":
        """<p>Gets the properties associated with an entities detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The <code>StartEntitiesDetectionJob</code> operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_entities_detection_job_request.DescribeEntitiesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_entities_detection_job_response.DescribeEntitiesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_entities_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_entities_detection_job.async_describe_entities_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_entities_detection_job_request.DescribeEntitiesDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_entity_recognizer(
        self,
        entity_recognizer_arn: "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_entity_recognizer_response.DescribeEntityRecognizerResponse":
        """<p>Provides details about an entity recognizer including status, S3 buckets containing training data, recognizer metadata, metrics, and so on.</p>

        Args:
            entity_recognizer_arn: <p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_entity_recognizer_request.DescribeEntityRecognizerRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_entity_recognizer_response.DescribeEntityRecognizerResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_entity_recognizer

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_entity_recognizer.async_describe_entity_recognizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_entity_recognizer_request.DescribeEntityRecognizerRequest = {
            "entity_recognizer_arn": entity_recognizer_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_events_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_events_detection_job_response.DescribeEventsDetectionJobResponse":
        """<p>Gets the status and details of an events detection job.</p>

        Args:
            job_id: <p>The identifier of the events detection job.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_events_detection_job_request.DescribeEventsDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_events_detection_job_response.DescribeEventsDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_events_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_events_detection_job.async_describe_events_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_events_detection_job_request.DescribeEventsDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_flywheel(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_flywheel_response.DescribeFlywheelResponse":
        """<p>Provides configuration information about the flywheel. For more information about flywheels, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_flywheel_request.DescribeFlywheelRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_flywheel_response.DescribeFlywheelResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_flywheel

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_flywheel.async_describe_flywheel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_flywheel_request.DescribeFlywheelRequest = {
            "flywheel_arn": flywheel_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_flywheel_iteration(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        flywheel_iteration_id: "capo_comprehend.types.flywheel_iteration_id.FlywheelIterationId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_flywheel_iteration_response.DescribeFlywheelIterationResponse":
        """<p>Retrieve the configuration properties of a flywheel iteration. For more information about flywheels, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p></p>
            flywheel_iteration_id: <p></p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_flywheel_iteration_request.DescribeFlywheelIterationRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_flywheel_iteration_response.DescribeFlywheelIterationResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_flywheel_iteration

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_flywheel_iteration.async_describe_flywheel_iteration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_flywheel_iteration_request.DescribeFlywheelIterationRequest = {
            "flywheel_arn": flywheel_arn,
            "flywheel_iteration_id": flywheel_iteration_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_key_phrases_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_key_phrases_detection_job_response.DescribeKeyPhrasesDetectionJobResponse":
        """<p>Gets the properties associated with a key phrases detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The <code>StartKeyPhrasesDetectionJob</code> operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_key_phrases_detection_job_request.DescribeKeyPhrasesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_key_phrases_detection_job_response.DescribeKeyPhrasesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_key_phrases_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_key_phrases_detection_job.async_describe_key_phrases_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_key_phrases_detection_job_request.DescribeKeyPhrasesDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_pii_entities_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_pii_entities_detection_job_response.DescribePiiEntitiesDetectionJobResponse":
        """<p>Gets the properties associated with a PII entities detection job. For example, you can use this operation to get the job status.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_pii_entities_detection_job_request.DescribePiiEntitiesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_pii_entities_detection_job_response.DescribePiiEntitiesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_pii_entities_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_pii_entities_detection_job.async_describe_pii_entities_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_pii_entities_detection_job_request.DescribePiiEntitiesDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_resource_policy(
        self,
        resource_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_resource_policy_response.DescribeResourcePolicyResponse":
        """<p>Gets the details of a resource-based policy that is attached to a custom model, including the JSON body of the policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the custom model version that has the resource policy.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_resource_policy_request.DescribeResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_resource_policy_response.DescribeResourcePolicyResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_resource_policy

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_resource_policy.async_describe_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_resource_policy_request.DescribeResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_sentiment_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_sentiment_detection_job_response.DescribeSentimentDetectionJobResponse":
        """<p>Gets the properties associated with a sentiment detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_sentiment_detection_job_request.DescribeSentimentDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_sentiment_detection_job_response.DescribeSentimentDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_sentiment_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_sentiment_detection_job.async_describe_sentiment_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_sentiment_detection_job_request.DescribeSentimentDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_targeted_sentiment_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_targeted_sentiment_detection_job_response.DescribeTargetedSentimentDetectionJobResponse":
        """<p>Gets the properties associated with a targeted sentiment detection job. Use this operation to get the status of the job.</p>

        Args:
            job_id: <p>The identifier that Amazon Comprehend generated for the job. The <code>StartTargetedSentimentDetectionJob</code> operation returns this identifier in its response.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_targeted_sentiment_detection_job_request.DescribeTargetedSentimentDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_targeted_sentiment_detection_job_response.DescribeTargetedSentimentDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_targeted_sentiment_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_targeted_sentiment_detection_job.async_describe_targeted_sentiment_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_targeted_sentiment_detection_job_request.DescribeTargetedSentimentDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_topics_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.describe_topics_detection_job_response.DescribeTopicsDetectionJobResponse":
        """<p>Gets the properties associated with a topic detection job. Use this operation to get the status of a detection job.</p>

        Args:
            job_id: <p>The identifier assigned by the user to the detection job.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.describe_topics_detection_job_request.DescribeTopicsDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.describe_topics_detection_job_response.DescribeTopicsDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.describe_topics_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.describe_topics_detection_job.async_describe_topics_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.describe_topics_detection_job_request.DescribeTopicsDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_dominant_language(
        self,
        text: "capo_comprehend.types.customer_input_string.CustomerInputString",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.detect_dominant_language_response.DetectDominantLanguageResponse":
        """<p>Determines the dominant language of the input text. For a list of languages that Amazon Comprehend can detect, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html">Amazon Comprehend Supported Languages</a>. </p>

        Args:
            text: <p>A UTF-8 text string. The string must contain at least 20 characters. The maximum string size is 100 KB.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_dominant_language_request.DetectDominantLanguageRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_dominant_language_response.DetectDominantLanguageResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_dominant_language

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_dominant_language.async_detect_dominant_language(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_dominant_language_request.DetectDominantLanguageRequest = {
            "text": text
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_entities(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        text: Optional[
            "capo_comprehend.types.customer_input_string.CustomerInputString"
        ] = None,
        language_code: Optional[
            "capo_comprehend.types.language_code.LanguageCode"
        ] = None,
        endpoint_arn: Optional[
            "capo_comprehend.types.entity_recognizer_endpoint_arn.EntityRecognizerEndpointArn"
        ] = None,
        bytes: Optional[
            "capo_comprehend.types.semi_structured_document_blob.SemiStructuredDocumentBlob"
        ] = None,
        document_reader_config: Optional[
            "capo_comprehend.types.document_reader_config.DocumentReaderConfig"
        ] = None,
    ) -> "capo_comprehend.types.detect_entities_response.DetectEntitiesResponse":
        """<p>Detects named entities in input text when you use the pre-trained model. Detects custom entities if you have a custom entity recognition model. </p> <p> When detecting named entities using the pre-trained model, use plain text as the input. For more information about named entities, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html">Entities</a> in the Comprehend Developer Guide.</p> <p>When you use a custom entity recognition model, you can input plain text or you can upload a single-page input document (text, PDF, Word, or image). </p> <p>If the system detects errors while processing a page in the input document, the API response includes an entry in <code>Errors</code> for each error. </p> <p>If the system detects a document-level error in your input document, the API returns an <code>InvalidRequestException</code> error response. For details about this exception, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync-err.html"> Errors in semi-structured documents</a> in the Comprehend Developer Guide. </p>

        Args:
            text: <p>A UTF-8 text string. The maximum string size is 100 KB. If you enter text using this parameter, do not use the <code>Bytes</code> parameter.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. If your request includes the endpoint for a custom entity recognition model, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you specify here.</p> <p>All input documents must be in the same language.</p>
            endpoint_arn: <p>The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model. Provide an endpoint if you want to detect entities by using your own custom model instead of the default model that is used by Amazon Comprehend.</p> <p>If you specify an endpoint, Amazon Comprehend uses the language of your custom model, and it ignores any language code that you provide in your request.</p> <p>For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>
            bytes: <p>This field applies only when you use a custom entity recognition model that was trained with PDF annotations. For other cases, enter your text input in the <code>Text</code> field.</p> <p> Use the <code>Bytes</code> parameter to input a text, PDF, Word or image file. Using a plain-text file in the <code>Bytes</code> parameter is equivelent to using the <code>Text</code> parameter (the <code>Entities</code> field in the response is identical).</p> <p>You can also use the <code>Bytes</code> parameter to input an Amazon Textract <code>DetectDocumentText</code> or <code>AnalyzeDocument</code> output file.</p> <p>Provide the input document as a sequence of base64-encoded bytes. If your code uses an Amazon Web Services SDK to detect entities, the SDK may encode the document file bytes for you. </p> <p>The maximum length of this field depends on the input document type. For details, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/idp-inputs-sync.html"> Inputs for real-time custom analysis</a> in the Comprehend Developer Guide. </p> <p>If you use the <code>Bytes</code> parameter, do not use the <code>Text</code> parameter.</p>
            document_reader_config: <p>Provides configuration parameters to override the default actions for extracting text from PDF documents and image files.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_entities_request.DetectEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_entities_response.DetectEntitiesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_entities

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_entities.async_detect_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_entities_request.DetectEntitiesRequest = {}
        if text is not None:
            input_["text"] = text
        if language_code is not None:
            input_["language_code"] = language_code
        if endpoint_arn is not None:
            input_["endpoint_arn"] = endpoint_arn
        if bytes is not None:
            input_["bytes"] = bytes
        if document_reader_config is not None:
            input_["document_reader_config"] = document_reader_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_key_phrases(
        self,
        text: "capo_comprehend.types.customer_input_string.CustomerInputString",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.detect_key_phrases_response.DetectKeyPhrasesResponse":
        """<p>Detects the key noun phrases found in the text. </p>

        Args:
            text: <p>A UTF-8 text string. The string must contain less than 100 KB of UTF-8 encoded characters.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_key_phrases_request.DetectKeyPhrasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_key_phrases_response.DetectKeyPhrasesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_key_phrases

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_key_phrases.async_detect_key_phrases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_key_phrases_request.DetectKeyPhrasesRequest = {
            "text": text,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_pii_entities(
        self,
        text: "capo_comprehend.types.string.String",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.detect_pii_entities_response.DetectPiiEntitiesResponse":
        """<p>Inspects the input text for entities that contain personally identifiable information (PII) and returns information about them.</p>

        Args:
            text: <p>A UTF-8 text string. The maximum string size is 100 KB.</p>
            language_code: <p>The language of the input text. Enter the language code for English (en) or Spanish (es).</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_pii_entities_request.DetectPiiEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_pii_entities_response.DetectPiiEntitiesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_pii_entities

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_pii_entities.async_detect_pii_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_pii_entities_request.DetectPiiEntitiesRequest = {
            "text": text,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_sentiment(
        self,
        text: "capo_comprehend.types.customer_input_string.CustomerInputString",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.detect_sentiment_response.DetectSentimentResponse":
        """<p>Inspects text and returns an inference of the prevailing sentiment (<code>POSITIVE</code>, <code>NEUTRAL</code>, <code>MIXED</code>, or <code>NEGATIVE</code>). </p>

        Args:
            text: <p>A UTF-8 text string. The maximum string size is 5 KB.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_sentiment_request.DetectSentimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_sentiment_response.DetectSentimentResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_sentiment

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_sentiment.async_detect_sentiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_sentiment_request.DetectSentimentRequest = {
            "text": text,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_syntax(
        self,
        text: "capo_comprehend.types.customer_input_string.CustomerInputString",
        language_code: "capo_comprehend.types.syntax_language_code.SyntaxLanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse":
        """<p>Inspects text for syntax and the part of speech of words in the document. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html">Syntax</a> in the Comprehend Developer Guide. </p>

        Args:
            text: <p>A UTF-8 string. The maximum string size is 5 KB.</p>
            language_code: <p>The language code of the input documents. You can specify any of the following languages supported by Amazon Comprehend: German ("de"), English ("en"), Spanish ("es"), French ("fr"), Italian ("it"), or Portuguese ("pt").</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_syntax_request.DetectSyntaxRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_syntax_response.DetectSyntaxResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_syntax

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_syntax.async_detect_syntax(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_syntax_request.DetectSyntaxRequest = {
            "text": text,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_targeted_sentiment(
        self,
        text: "capo_comprehend.types.customer_input_string.CustomerInputString",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.detect_targeted_sentiment_response.DetectTargetedSentimentResponse":
        """<p>Inspects the input text and returns a sentiment analysis for each entity identified in the text.</p> <p>For more information about targeted sentiment, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html">Targeted sentiment</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            text: <p>A UTF-8 text string. The maximum string length is 5 KB.</p>
            language_code: <p>The language of the input documents. Currently, English is the only supported language.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_targeted_sentiment_request.DetectTargetedSentimentRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_targeted_sentiment_response.DetectTargetedSentimentResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_targeted_sentiment

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_targeted_sentiment.async_detect_targeted_sentiment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_targeted_sentiment_request.DetectTargetedSentimentRequest = {
            "text": text,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detect_toxic_content(
        self,
        text_segments: "capo_comprehend.types.list_of_text_segments.ListOfTextSegments",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> (
        "capo_comprehend.types.detect_toxic_content_response.DetectToxicContentResponse"
    ):
        """<p>Performs toxicity analysis on the list of text strings that you provide as input. The API response contains a results list that matches the size of the input list. For more information about toxicity detection, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/toxicity-detection.html">Toxicity detection</a> in the <i>Amazon Comprehend Developer Guide</i>. </p>

        Args:
            text_segments: <p>A list of up to 10 text strings. Each string has a maximum size of 1 KB, and the maximum size of the list is 10 KB.</p>
            language_code: <p>The language of the input text. Currently, English is the only supported language.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.text_size_limit_exceeded_exception.TextSizeLimitExceededException: <p>The size of the input text exceeds the limit. Use a smaller document.</p>
            capo_comprehend.errors.unsupported_language_exception.UnsupportedLanguageException: <p>Amazon Comprehend can't process the language of the input text. For a list of supported languages, <a href="https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html">Supported languages</a> in the Comprehend Developer Guide. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.detect_toxic_content_request.DetectToxicContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.detect_toxic_content_response.DetectToxicContentResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.detect_toxic_content

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.detect_toxic_content.async_detect_toxic_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.detect_toxic_content_request.DetectToxicContentRequest = {
            "text_segments": text_segments,
            "language_code": language_code,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_model(
        self,
        source_model_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        model_name: Optional[
            "capo_comprehend.types.comprehend_arn_name.ComprehendArnName"
        ] = None,
        version_name: Optional["capo_comprehend.types.version_name.VersionName"] = None,
        model_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        data_access_role_arn: Optional[
            "capo_comprehend.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.import_model_response.ImportModelResponse":
        """<p>Creates a new custom model that replicates a source custom model that you import. The source model can be in your Amazon Web Services account or another one.</p> <p>If the source model is in another Amazon Web Services account, then it must have a resource-based policy that authorizes you to import it.</p> <p>The source model must be in the same Amazon Web Services Region that you're using when you import. You can't import a model that's in a different Region.</p>

        Args:
            source_model_arn: <p>The Amazon Resource Name (ARN) of the custom model to import.</p>
            model_name: <p>The name to assign to the custom model that is created in Amazon Comprehend by this import.</p>
            version_name: <p>The version name given to the custom model that is created by this import. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (_) are allowed. The version name must be unique among all models with the same classifier name in the account/Region.</p>
            model_kms_key_id: <p>ID for the KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to use Amazon Key Management Service (KMS) to encrypt or decrypt the custom model.</p>
            tags: <p>Tags to associate with the custom model that is created by this import. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.import_model_request.ImportModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.import_model_response.ImportModelResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.import_model

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.import_model.async_import_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.import_model_request.ImportModelRequest = {
            "source_model_arn": source_model_arn
        }
        if model_name is not None:
            input_["model_name"] = model_name
        if version_name is not None:
            input_["version_name"] = version_name
        if model_kms_key_id is not None:
            input_["model_kms_key_id"] = model_kms_key_id
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        flywheel_arn: Optional[
            "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
        ] = None,
        filter: Optional["capo_comprehend.types.dataset_filter.DatasetFilter"] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_datasets_response.ListDatasetsResponse":
        """<p>List the datasets that you have configured in this Region. For more information about datasets, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel.</p>
            filter: <p>Filters the datasets to be returned in the response.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>Maximum number of results to return in a response. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_datasets

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_datasets_request.ListDatasetsRequest = {}
        if flywheel_arn is not None:
            input_["flywheel_arn"] = flywheel_arn
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        flywheel_arn: Optional[
            "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
        ] = None,
        filter: Optional["capo_comprehend.types.dataset_filter.DatasetFilter"] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_datasets_response.ListDatasetsResponse]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                config_overrides=config_overrides,
                flywheel_arn=flywheel_arn,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_document_classification_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.document_classification_job_filter.DocumentClassificationJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_document_classification_jobs_response.ListDocumentClassificationJobsResponse":
        """<p>Gets a list of the documentation classification jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_document_classification_jobs_request.ListDocumentClassificationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_document_classification_jobs_response.ListDocumentClassificationJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_document_classification_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_document_classification_jobs.async_list_document_classification_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_document_classification_jobs_request.ListDocumentClassificationJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_document_classification_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.document_classification_job_filter.DocumentClassificationJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_document_classification_jobs_response.ListDocumentClassificationJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_document_classification_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_document_classifiers(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.document_classifier_filter.DocumentClassifierFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_document_classifiers_response.ListDocumentClassifiersResponse":
        """<p>Gets a list of the document classifiers that you have created.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_document_classifiers_request.ListDocumentClassifiersRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_document_classifiers_response.ListDocumentClassifiersResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_document_classifiers

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_document_classifiers.async_list_document_classifiers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_document_classifiers_request.ListDocumentClassifiersRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_document_classifiers(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.document_classifier_filter.DocumentClassifierFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_document_classifiers_response.ListDocumentClassifiersResponse]":
        _token = next_token
        while True:
            _response = await self.list_document_classifiers(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_document_classifier_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_document_classifier_summaries_response.ListDocumentClassifierSummariesResponse":
        """<p>Gets a list of summaries of the document classifiers that you have created</p>

        Args:
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return on each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_document_classifier_summaries_request.ListDocumentClassifierSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_document_classifier_summaries_response.ListDocumentClassifierSummariesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_document_classifier_summaries

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_document_classifier_summaries.async_list_document_classifier_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_document_classifier_summaries_request.ListDocumentClassifierSummariesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_document_classifier_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_document_classifier_summaries_response.ListDocumentClassifierSummariesResponse]":
        _token = next_token
        while True:
            _response = await self.list_document_classifier_summaries(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dominant_language_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.dominant_language_detection_job_filter.DominantLanguageDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_dominant_language_detection_jobs_response.ListDominantLanguageDetectionJobsResponse":
        """<p>Gets a list of the dominant language detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters that jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_dominant_language_detection_jobs_request.ListDominantLanguageDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_dominant_language_detection_jobs_response.ListDominantLanguageDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_dominant_language_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_dominant_language_detection_jobs.async_list_dominant_language_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_dominant_language_detection_jobs_request.ListDominantLanguageDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_dominant_language_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.dominant_language_detection_job_filter.DominantLanguageDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_dominant_language_detection_jobs_response.ListDominantLanguageDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_dominant_language_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional["capo_comprehend.types.endpoint_filter.EndpointFilter"] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_endpoints_response.ListEndpointsResponse":
        """<p>Gets a list of all existing endpoints that you've created. For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>

        Args:
            filter: <p>Filters the endpoints that are returned. You can filter endpoints on their name, model, status, or the date and time that they were created. You can only set one filter at a time. </p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_endpoints_request.ListEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_endpoints_response.ListEndpointsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_endpoints

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_endpoints.async_list_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_endpoints_request.ListEndpointsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional["capo_comprehend.types.endpoint_filter.EndpointFilter"] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.endpoint_properties.EndpointProperties]":
        _token = next_token
        while True:
            _response = await self.list_endpoints(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("endpoint_properties_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_entities_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.entities_detection_job_filter.EntitiesDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_entities_detection_jobs_response.ListEntitiesDetectionJobsResponse":
        """<p>Gets a list of the entity detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_entities_detection_jobs_request.ListEntitiesDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_entities_detection_jobs_response.ListEntitiesDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_entities_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_entities_detection_jobs.async_list_entities_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_entities_detection_jobs_request.ListEntitiesDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_entities_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.entities_detection_job_filter.EntitiesDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_entities_detection_jobs_response.ListEntitiesDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_entities_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_entity_recognizers(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.entity_recognizer_filter.EntityRecognizerFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_entity_recognizers_response.ListEntityRecognizersResponse":
        """<p>Gets a list of the properties of all entity recognizers that you created, including recognizers currently in training. Allows you to filter the list of recognizers based on criteria such as status and submission time. This call returns up to 500 entity recognizers in the list, with a default number of 100 recognizers in the list.</p> <p>The results of this list are not in any particular order. Please get the list and sort locally if needed.</p>

        Args:
            filter: <p>Filters the list of entities returned. You can filter on <code>Status</code>, <code>SubmitTimeBefore</code>, or <code>SubmitTimeAfter</code>. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p> The maximum number of results to return on each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_entity_recognizers_request.ListEntityRecognizersRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_entity_recognizers_response.ListEntityRecognizersResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_entity_recognizers

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_entity_recognizers.async_list_entity_recognizers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_entity_recognizers_request.ListEntityRecognizersRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_entity_recognizers(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.entity_recognizer_filter.EntityRecognizerFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_entity_recognizers_response.ListEntityRecognizersResponse]":
        _token = next_token
        while True:
            _response = await self.list_entity_recognizers(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_entity_recognizer_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_entity_recognizer_summaries_response.ListEntityRecognizerSummariesResponse":
        """<p>Gets a list of summaries for the entity recognizers that you have created.</p>

        Args:
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return on each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_entity_recognizer_summaries_request.ListEntityRecognizerSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_entity_recognizer_summaries_response.ListEntityRecognizerSummariesResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_entity_recognizer_summaries

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_entity_recognizer_summaries.async_list_entity_recognizer_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_entity_recognizer_summaries_request.ListEntityRecognizerSummariesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_entity_recognizer_summaries(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_entity_recognizer_summaries_response.ListEntityRecognizerSummariesResponse]":
        _token = next_token
        while True:
            _response = await self.list_entity_recognizer_summaries(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_events_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.events_detection_job_filter.EventsDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_events_detection_jobs_response.ListEventsDetectionJobsResponse":
        """<p>Gets a list of the events detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_events_detection_jobs_request.ListEventsDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_events_detection_jobs_response.ListEventsDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_events_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_events_detection_jobs.async_list_events_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_events_detection_jobs_request.ListEventsDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_events_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.events_detection_job_filter.EventsDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_events_detection_jobs_response.ListEventsDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_events_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_flywheel_iteration_history(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.flywheel_iteration_filter.FlywheelIterationFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_flywheel_iteration_history_response.ListFlywheelIterationHistoryResponse":
        """<p>Information about the history of a flywheel iteration. For more information about flywheels, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p>The ARN of the flywheel.</p>
            filter: <p>Filter the flywheel iteration history based on creation time.</p>
            next_token: <p>Next token</p>
            max_results: <p>Maximum number of iteration history results to return</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_flywheel_iteration_history_request.ListFlywheelIterationHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_flywheel_iteration_history_response.ListFlywheelIterationHistoryResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_flywheel_iteration_history

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_flywheel_iteration_history.async_list_flywheel_iteration_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_flywheel_iteration_history_request.ListFlywheelIterationHistoryRequest = {
            "flywheel_arn": flywheel_arn
        }
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_flywheel_iteration_history(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.flywheel_iteration_filter.FlywheelIterationFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_flywheel_iteration_history_response.ListFlywheelIterationHistoryResponse]":
        _token = next_token
        while True:
            _response = await self.list_flywheel_iteration_history(
                flywheel_arn,
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_flywheels(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional["capo_comprehend.types.flywheel_filter.FlywheelFilter"] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_flywheels_response.ListFlywheelsResponse":
        """<p>Gets a list of the flywheels that you have created.</p>

        Args:
            filter: <p>Filters the flywheels that are returned. You can filter flywheels on their status, or the date and time that they were submitted. You can only set one filter at a time. </p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>Maximum number of results to return in a response. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_flywheels_request.ListFlywheelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_flywheels_response.ListFlywheelsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_flywheels

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_flywheels.async_list_flywheels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_flywheels_request.ListFlywheelsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_flywheels(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional["capo_comprehend.types.flywheel_filter.FlywheelFilter"] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_flywheels_response.ListFlywheelsResponse]":
        _token = next_token
        while True:
            _response = await self.list_flywheels(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_key_phrases_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.key_phrases_detection_job_filter.KeyPhrasesDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_key_phrases_detection_jobs_response.ListKeyPhrasesDetectionJobsResponse":
        """<p>Get a list of key phrase detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_key_phrases_detection_jobs_request.ListKeyPhrasesDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_key_phrases_detection_jobs_response.ListKeyPhrasesDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_key_phrases_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_key_phrases_detection_jobs.async_list_key_phrases_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_key_phrases_detection_jobs_request.ListKeyPhrasesDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_key_phrases_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.key_phrases_detection_job_filter.KeyPhrasesDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_key_phrases_detection_jobs_response.ListKeyPhrasesDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_key_phrases_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pii_entities_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.pii_entities_detection_job_filter.PiiEntitiesDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_pii_entities_detection_jobs_response.ListPiiEntitiesDetectionJobsResponse":
        """<p>Gets a list of the PII entity detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_pii_entities_detection_jobs_request.ListPiiEntitiesDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_pii_entities_detection_jobs_response.ListPiiEntitiesDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_pii_entities_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_pii_entities_detection_jobs.async_list_pii_entities_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_pii_entities_detection_jobs_request.ListPiiEntitiesDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_pii_entities_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.pii_entities_detection_job_filter.PiiEntitiesDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.pii_entities_detection_job_properties.PiiEntitiesDetectionJobProperties]":
        _token = next_token
        while True:
            _response = await self.list_pii_entities_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("pii_entities_detection_job_properties_list",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sentiment_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.sentiment_detection_job_filter.SentimentDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_sentiment_detection_jobs_response.ListSentimentDetectionJobsResponse":
        """<p>Gets a list of sentiment detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_sentiment_detection_jobs_request.ListSentimentDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_sentiment_detection_jobs_response.ListSentimentDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_sentiment_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_sentiment_detection_jobs.async_list_sentiment_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_sentiment_detection_jobs_request.ListSentimentDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_sentiment_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.sentiment_detection_job_filter.SentimentDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_sentiment_detection_jobs_response.ListSentimentDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_sentiment_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_comprehend.types.comprehend_arn.ComprehendArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with a given Amazon Comprehend resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the given Amazon Comprehend resource you are querying. </p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_targeted_sentiment_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.targeted_sentiment_detection_job_filter.TargetedSentimentDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_targeted_sentiment_detection_jobs_response.ListTargetedSentimentDetectionJobsResponse":
        """<p>Gets a list of targeted sentiment detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. You can filter jobs on their name, status, or the date and time that they were submitted. You can only set one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_targeted_sentiment_detection_jobs_request.ListTargetedSentimentDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_targeted_sentiment_detection_jobs_response.ListTargetedSentimentDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_targeted_sentiment_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_targeted_sentiment_detection_jobs.async_list_targeted_sentiment_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_targeted_sentiment_detection_jobs_request.ListTargetedSentimentDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_targeted_sentiment_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.targeted_sentiment_detection_job_filter.TargetedSentimentDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_targeted_sentiment_detection_jobs_response.ListTargetedSentimentDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_targeted_sentiment_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_topics_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.topics_detection_job_filter.TopicsDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "capo_comprehend.types.list_topics_detection_jobs_response.ListTopicsDetectionJobsResponse":
        """<p>Gets a list of the topic detection jobs that you have submitted.</p>

        Args:
            filter: <p>Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and time that they were submitted. You can set only one filter at a time.</p>
            next_token: <p>Identifies the next page of results to return.</p>
            max_results: <p>The maximum number of results to return in each page. The default is 100.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_filter_exception.InvalidFilterException: <p>The filter specified for the operation is invalid. Specify a different filter.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.list_topics_detection_jobs_request.ListTopicsDetectionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.list_topics_detection_jobs_response.ListTopicsDetectionJobsResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.list_topics_detection_jobs

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.list_topics_detection_jobs.async_list_topics_detection_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.list_topics_detection_jobs_request.ListTopicsDetectionJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_topics_detection_jobs(
        self,
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        filter: Optional[
            "capo_comprehend.types.topics_detection_job_filter.TopicsDetectionJobFilter"
        ] = None,
        next_token: Optional["capo_comprehend.types.string.String"] = None,
        max_results: Optional[
            "capo_comprehend.types.max_results_integer.MaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_comprehend.types.list_topics_detection_jobs_response.ListTopicsDetectionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_topics_detection_jobs(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_resource_policy(
        self,
        resource_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn",
        resource_policy: "capo_comprehend.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        policy_revision_id: Optional[
            "capo_comprehend.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_comprehend.types.put_resource_policy_response.PutResourcePolicyResponse":
        r"""<p>Attaches a resource-based policy to a custom model. You can use this policy to authorize an entity in another Amazon Web Services account to import the custom model, which replicates it in Amazon Comprehend in their account.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the custom model to attach the policy to.</p>
            resource_policy: <p>The JSON resource-based policy to attach to your custom model. Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{"attribute": "value", "attribute": ["value"]}'</code> </p>
            policy_revision_id: <p>The revision ID that Amazon Comprehend assigned to the policy that you are updating. If you are creating a new policy that has no prior version, don't use this parameter. Amazon Comprehend creates the revision ID for you.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "resource_policy": resource_policy,
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_document_classification_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        document_classifier_arn: Optional[
            "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn"
        ] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
        flywheel_arn: Optional[
            "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
        ] = None,
    ) -> "capo_comprehend.types.start_document_classification_job_response.StartDocumentClassificationJobResponse":
        """<p>Starts an asynchronous document classification job using a custom classification model. Use the <code>DescribeDocumentClassificationJob</code> operation to track the progress of the job.</p>

        Args:
            job_name: <p>The identifier of the job.</p>
            document_classifier_arn: <p>The Amazon Resource Name (ARN) of the document classifier to use to process the job.</p>
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>
            client_request_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your document classification job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            tags: <p>Tags to associate with the document classification job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel associated with the model to use.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_document_classification_job_request.StartDocumentClassificationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_document_classification_job_response.StartDocumentClassificationJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_document_classification_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_document_classification_job.async_start_document_classification_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_document_classification_job_request.StartDocumentClassificationJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if document_classifier_arn is not None:
            input_["document_classifier_arn"] = document_classifier_arn
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags
        if flywheel_arn is not None:
            input_["flywheel_arn"] = flywheel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_dominant_language_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_dominant_language_detection_job_response.StartDominantLanguageDetectionJobResponse":
        """<p>Starts an asynchronous dominant language detection job for a collection of documents. Use the operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>
            job_name: <p>An identifier for the job.</p>
            client_request_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your dominant language detection job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            tags: <p>Tags to associate with the dominant language detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_dominant_language_detection_job_request.StartDominantLanguageDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_dominant_language_detection_job_response.StartDominantLanguageDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_dominant_language_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_dominant_language_detection_job.async_start_dominant_language_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_dominant_language_detection_job_request.StartDominantLanguageDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_entities_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        entity_recognizer_arn: Optional[
            "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
        ] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
        flywheel_arn: Optional[
            "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
        ] = None,
    ) -> "capo_comprehend.types.start_entities_detection_job_response.StartEntitiesDetectionJobResponse":
        """<p>Starts an asynchronous entity detection job for a collection of documents. Use the operation to track the status of a job.</p> <p>This API can be used for either standard entity detection or custom entity recognition. In order to be used for custom entity recognition, the optional <code>EntityRecognizerArn</code> must be used in order to provide access to the recognizer being used to detect the custom entity.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>
            job_name: <p>The identifier of the job.</p>
            entity_recognizer_arn: <p>The Amazon Resource Name (ARN) that identifies the specific entity recognizer to be used by the <code>StartEntitiesDetectionJob</code>. This ARN is optional and is only used for a custom entity recognition job.</p>
            language_code: <p>The language of the input documents. All documents must be in the same language. You can specify any of the languages supported by Amazon Comprehend. If custom entities recognition is used, this parameter is ignored and the language used for training the model is used instead.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your entity detection job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            tags: <p>Tags to associate with the entities detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel associated with the model to use.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_entities_detection_job_request.StartEntitiesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_entities_detection_job_response.StartEntitiesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_entities_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_entities_detection_job.async_start_entities_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_entities_detection_job_request.StartEntitiesDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
            "language_code": language_code,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if entity_recognizer_arn is not None:
            input_["entity_recognizer_arn"] = entity_recognizer_arn
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags
        if flywheel_arn is not None:
            input_["flywheel_arn"] = flywheel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_events_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        target_event_types: "capo_comprehend.types.target_event_types.TargetEventTypes",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_events_detection_job_response.StartEventsDetectionJobResponse":
        """<p>Starts an asynchronous event detection job for a collection of documents.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>
            job_name: <p>The identifier of the events detection job.</p>
            language_code: <p>The language code of the input documents.</p>
            client_request_token: <p>An unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            target_event_types: <p>The types of events to detect in the input documents.</p>
            tags: <p>Tags to associate with the events detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_events_detection_job_request.StartEventsDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_events_detection_job_response.StartEventsDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_events_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_events_detection_job.async_start_events_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_events_detection_job_request.StartEventsDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
            "language_code": language_code,
            "target_event_types": target_event_types,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_flywheel_iteration(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
    ) -> "capo_comprehend.types.start_flywheel_iteration_response.StartFlywheelIterationResponse":
        """<p>Start the flywheel iteration.This operation uses any new datasets to train a new model version. For more information about flywheels, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html"> Flywheel overview</a> in the <i>Amazon Comprehend Developer Guide</i>.</p>

        Args:
            flywheel_arn: <p>The ARN of the flywheel.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_flywheel_iteration_request.StartFlywheelIterationRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_flywheel_iteration_response.StartFlywheelIterationResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_flywheel_iteration

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_flywheel_iteration.async_start_flywheel_iteration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_flywheel_iteration_request.StartFlywheelIterationRequest = {
            "flywheel_arn": flywheel_arn
        }
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_key_phrases_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_key_phrases_detection_job_response.StartKeyPhrasesDetectionJobResponse":
        """<p>Starts an asynchronous key phrase detection job for a collection of documents. Use the operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>
            job_name: <p>The identifier of the job.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p> Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your key phrases detection job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            tags: <p>Tags to associate with the key phrases detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_key_phrases_detection_job_request.StartKeyPhrasesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_key_phrases_detection_job_response.StartKeyPhrasesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_key_phrases_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_key_phrases_detection_job.async_start_key_phrases_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_key_phrases_detection_job_request.StartKeyPhrasesDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
            "language_code": language_code,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_pii_entities_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        mode: "capo_comprehend.types.pii_entities_detection_mode.PiiEntitiesDetectionMode",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        redaction_config: Optional[
            "capo_comprehend.types.redaction_config.RedactionConfig"
        ] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_pii_entities_detection_job_response.StartPiiEntitiesDetectionJobResponse":
        """<p>Starts an asynchronous PII entity detection job for a collection of documents.</p>

        Args:
            input_data_config: <p>The input properties for a PII entities detection job.</p>
            output_data_config: <p>Provides conﬁguration parameters for the output of PII entity detection jobs.</p>
            mode: <p>Specifies whether the output provides the locations (offsets) of PII entities or a file in which PII entities are redacted.</p>
            redaction_config: <p>Provides configuration parameters for PII entity redaction.</p> <p>This parameter is required if you set the <code>Mode</code> parameter to <code>ONLY_REDACTION</code>. In that case, you must provide a <code>RedactionConfig</code> definition that includes the <code>PiiEntityTypes</code> parameter.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>
            job_name: <p>The identifier of the job.</p>
            language_code: <p>The language of the input documents. Enter the language code for English (en) or Spanish (es).</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            tags: <p>Tags to associate with the PII entities detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_pii_entities_detection_job_request.StartPiiEntitiesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_pii_entities_detection_job_response.StartPiiEntitiesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_pii_entities_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_pii_entities_detection_job.async_start_pii_entities_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_pii_entities_detection_job_request.StartPiiEntitiesDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "mode": mode,
            "data_access_role_arn": data_access_role_arn,
            "language_code": language_code,
        }
        if redaction_config is not None:
            input_["redaction_config"] = redaction_config
        if job_name is not None:
            input_["job_name"] = job_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_sentiment_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_sentiment_detection_job_response.StartSentimentDetectionJobResponse":
        """<p>Starts an asynchronous sentiment detection job for a collection of documents. Use the operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files. </p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>
            job_name: <p>The identifier of the job.</p>
            language_code: <p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your sentiment detection job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            tags: <p>Tags to associate with the sentiment detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_sentiment_detection_job_request.StartSentimentDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_sentiment_detection_job_response.StartSentimentDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_sentiment_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_sentiment_detection_job.async_start_sentiment_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_sentiment_detection_job_request.StartSentimentDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
            "language_code": language_code,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_targeted_sentiment_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        language_code: "capo_comprehend.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_targeted_sentiment_detection_job_response.StartTargetedSentimentDetectionJobResponse":
        """<p>Starts an asynchronous targeted sentiment detection job for a collection of documents. Use the <code>DescribeTargetedSentimentDetectionJob</code> operation to track the status of a job.</p>

        Args:
            output_data_config: <p>Specifies where to send the output files. </p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>
            job_name: <p>The identifier of the job.</p>
            language_code: <p>The language of the input documents. Currently, English is the only supported language.</p>
            client_request_token: <p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the KMS key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            tags: <p>Tags to associate with the targeted sentiment detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_targeted_sentiment_detection_job_request.StartTargetedSentimentDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_targeted_sentiment_detection_job_response.StartTargetedSentimentDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_targeted_sentiment_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_targeted_sentiment_detection_job.async_start_targeted_sentiment_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_targeted_sentiment_detection_job_request.StartTargetedSentimentDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
            "language_code": language_code,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_topics_detection_job(
        self,
        input_data_config: "capo_comprehend.types.input_data_config.InputDataConfig",
        output_data_config: "capo_comprehend.types.output_data_config.OutputDataConfig",
        data_access_role_arn: "capo_comprehend.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        job_name: Optional["capo_comprehend.types.job_name.JobName"] = None,
        number_of_topics: Optional[
            "capo_comprehend.types.number_of_topics_integer.NumberOfTopicsInteger"
        ] = None,
        client_request_token: Optional[
            "capo_comprehend.types.client_request_token_string.ClientRequestTokenString"
        ] = None,
        volume_kms_key_id: Optional["capo_comprehend.types.kms_key_id.KmsKeyId"] = None,
        vpc_config: Optional["capo_comprehend.types.vpc_config.VpcConfig"] = None,
        tags: Optional["capo_comprehend.types.tag_list.TagList"] = None,
    ) -> "capo_comprehend.types.start_topics_detection_job_response.StartTopicsDetectionJobResponse":
        """<p>Starts an asynchronous topic detection job. Use the <code>DescribeTopicDetectionJob</code> operation to track the status of a job.</p>

        Args:
            input_data_config: <p>Specifies the format and location of the input data for the job.</p>
            output_data_config: <p>Specifies where to send the output files. The output is a compressed archive with two files, <code>topic-terms.csv</code> that lists the terms associated with each topic, and <code>doc-topics.csv</code> that lists the documents associated with each topic</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data. For more information, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/security_iam_id-based-policy-examples.html#auth-role-permissions">Role-based permissions</a>.</p>
            job_name: <p>The identifier of the job.</p>
            number_of_topics: <p>The number of topics to detect.</p>
            client_request_token: <p>A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.</p>
            volume_kms_key_id: <p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>"1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"</code> </p> </li> </ul>
            vpc_config: <p>Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your topic detection job. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html">Amazon VPC</a>. </p>
            tags: <p>Tags to associate with the topics detection job. A tag is a key-value pair that adds metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.start_topics_detection_job_request.StartTopicsDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.start_topics_detection_job_response.StartTopicsDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.start_topics_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.start_topics_detection_job.async_start_topics_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.start_topics_detection_job_request.StartTopicsDetectionJobRequest = {
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
            "data_access_role_arn": data_access_role_arn,
        }
        if job_name is not None:
            input_["job_name"] = job_name
        if number_of_topics is not None:
            input_["number_of_topics"] = number_of_topics
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if volume_kms_key_id is not None:
            input_["volume_kms_key_id"] = volume_kms_key_id
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_dominant_language_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_dominant_language_detection_job_response.StopDominantLanguageDetectionJobResponse":
        """<p>Stops a dominant language detection job in progress.</p> <p>If the job state is <code>IN_PROGRESS</code> the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the job completes before it can be stopped, it is put into the <code>COMPLETED</code> state; otherwise the job is stopped and put into the <code>STOPPED</code> state.</p> <p>If the job is in the <code>COMPLETED</code> or <code>FAILED</code> state when you call the <code>StopDominantLanguageDetectionJob</code> operation, the operation returns a 400 Internal Request Exception. </p> <p>When a job is stopped, any documents already processed are written to the output location.</p>

        Args:
            job_id: <p>The identifier of the dominant language detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_dominant_language_detection_job_request.StopDominantLanguageDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_dominant_language_detection_job_response.StopDominantLanguageDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_dominant_language_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_dominant_language_detection_job.async_stop_dominant_language_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_dominant_language_detection_job_request.StopDominantLanguageDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_entities_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_entities_detection_job_response.StopEntitiesDetectionJobResponse":
        """<p>Stops an entities detection job in progress.</p> <p>If the job state is <code>IN_PROGRESS</code> the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the job completes before it can be stopped, it is put into the <code>COMPLETED</code> state; otherwise the job is stopped and put into the <code>STOPPED</code> state.</p> <p>If the job is in the <code>COMPLETED</code> or <code>FAILED</code> state when you call the <code>StopDominantLanguageDetectionJob</code> operation, the operation returns a 400 Internal Request Exception. </p> <p>When a job is stopped, any documents already processed are written to the output location.</p>

        Args:
            job_id: <p>The identifier of the entities detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_entities_detection_job_request.StopEntitiesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_entities_detection_job_response.StopEntitiesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_entities_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_entities_detection_job.async_stop_entities_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_entities_detection_job_request.StopEntitiesDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_events_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_events_detection_job_response.StopEventsDetectionJobResponse":
        """<p>Stops an events detection job in progress.</p>

        Args:
            job_id: <p>The identifier of the events detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_events_detection_job_request.StopEventsDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_events_detection_job_response.StopEventsDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_events_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_events_detection_job.async_stop_events_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_events_detection_job_request.StopEventsDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_key_phrases_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_key_phrases_detection_job_response.StopKeyPhrasesDetectionJobResponse":
        """<p>Stops a key phrases detection job in progress.</p> <p>If the job state is <code>IN_PROGRESS</code> the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the job completes before it can be stopped, it is put into the <code>COMPLETED</code> state; otherwise the job is stopped and put into the <code>STOPPED</code> state.</p> <p>If the job is in the <code>COMPLETED</code> or <code>FAILED</code> state when you call the <code>StopDominantLanguageDetectionJob</code> operation, the operation returns a 400 Internal Request Exception. </p> <p>When a job is stopped, any documents already processed are written to the output location.</p>

        Args:
            job_id: <p>The identifier of the key phrases detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_key_phrases_detection_job_request.StopKeyPhrasesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_key_phrases_detection_job_response.StopKeyPhrasesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_key_phrases_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_key_phrases_detection_job.async_stop_key_phrases_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_key_phrases_detection_job_request.StopKeyPhrasesDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_pii_entities_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_pii_entities_detection_job_response.StopPiiEntitiesDetectionJobResponse":
        """<p>Stops a PII entities detection job in progress.</p>

        Args:
            job_id: <p>The identifier of the PII entities detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_pii_entities_detection_job_request.StopPiiEntitiesDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_pii_entities_detection_job_response.StopPiiEntitiesDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_pii_entities_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_pii_entities_detection_job.async_stop_pii_entities_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_pii_entities_detection_job_request.StopPiiEntitiesDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_sentiment_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_sentiment_detection_job_response.StopSentimentDetectionJobResponse":
        """<p>Stops a sentiment detection job in progress.</p> <p>If the job state is <code>IN_PROGRESS</code>, the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the job completes before it can be stopped, it is put into the <code>COMPLETED</code> state; otherwise the job is be stopped and put into the <code>STOPPED</code> state.</p> <p>If the job is in the <code>COMPLETED</code> or <code>FAILED</code> state when you call the <code>StopDominantLanguageDetectionJob</code> operation, the operation returns a 400 Internal Request Exception. </p> <p>When a job is stopped, any documents already processed are written to the output location.</p>

        Args:
            job_id: <p>The identifier of the sentiment detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_sentiment_detection_job_request.StopSentimentDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_sentiment_detection_job_response.StopSentimentDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_sentiment_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_sentiment_detection_job.async_stop_sentiment_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_sentiment_detection_job_request.StopSentimentDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_targeted_sentiment_detection_job(
        self,
        job_id: "capo_comprehend.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_targeted_sentiment_detection_job_response.StopTargetedSentimentDetectionJobResponse":
        """<p>Stops a targeted sentiment detection job in progress.</p> <p>If the job state is <code>IN_PROGRESS</code>, the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the job completes before it can be stopped, it is put into the <code>COMPLETED</code> state; otherwise the job is be stopped and put into the <code>STOPPED</code> state.</p> <p>If the job is in the <code>COMPLETED</code> or <code>FAILED</code> state when you call the <code>StopDominantLanguageDetectionJob</code> operation, the operation returns a 400 Internal Request Exception. </p> <p>When a job is stopped, any documents already processed are written to the output location.</p>

        Args:
            job_id: <p>The identifier of the targeted sentiment detection job to stop.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.job_not_found_exception.JobNotFoundException: <p>The specified job was not found. Check the job ID and try again.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_targeted_sentiment_detection_job_request.StopTargetedSentimentDetectionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_targeted_sentiment_detection_job_response.StopTargetedSentimentDetectionJobResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_targeted_sentiment_detection_job

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_targeted_sentiment_detection_job.async_stop_targeted_sentiment_detection_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_targeted_sentiment_detection_job_request.StopTargetedSentimentDetectionJobRequest = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_training_document_classifier(
        self,
        document_classifier_arn: "capo_comprehend.types.document_classifier_arn.DocumentClassifierArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_training_document_classifier_response.StopTrainingDocumentClassifierResponse":
        """<p>Stops a document classifier training job while in progress.</p> <p>If the training job state is <code>TRAINING</code>, the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the training job completes before it can be stopped, it is put into the <code>TRAINED</code>; otherwise the training job is stopped and put into the <code>STOPPED</code> state and the service sends back an HTTP 200 response with an empty HTTP body. </p>

        Args:
            document_classifier_arn: <p>The Amazon Resource Name (ARN) that identifies the document classifier currently being trained.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_training_document_classifier_request.StopTrainingDocumentClassifierRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_training_document_classifier_response.StopTrainingDocumentClassifierResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_training_document_classifier

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_training_document_classifier.async_stop_training_document_classifier(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_training_document_classifier_request.StopTrainingDocumentClassifierRequest = {
            "document_classifier_arn": document_classifier_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_training_entity_recognizer(
        self,
        entity_recognizer_arn: "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.stop_training_entity_recognizer_response.StopTrainingEntityRecognizerResponse":
        """<p>Stops an entity recognizer training job while in progress.</p> <p>If the training job state is <code>TRAINING</code>, the job is marked for termination and put into the <code>STOP_REQUESTED</code> state. If the training job completes before it can be stopped, it is put into the <code>TRAINED</code>; otherwise the training job is stopped and putted into the <code>STOPPED</code> state and the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            entity_recognizer_arn: <p>The Amazon Resource Name (ARN) that identifies the entity recognizer currently being trained.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.stop_training_entity_recognizer_request.StopTrainingEntityRecognizerRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.stop_training_entity_recognizer_response.StopTrainingEntityRecognizerResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.stop_training_entity_recognizer

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.stop_training_entity_recognizer.async_stop_training_entity_recognizer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.stop_training_entity_recognizer_request.StopTrainingEntityRecognizerRequest = {
            "entity_recognizer_arn": entity_recognizer_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_comprehend.types.comprehend_arn.ComprehendArn",
        tags: "capo_comprehend.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.tag_resource_response.TagResourceResponse":
        """<p>Associates a specific tag with an Amazon Comprehend resource. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the given Amazon Comprehend resource to which you want to associate the tags. </p>
            tags: <p>Tags being associated with a specific Amazon Comprehend resource. There can be a maximum of 50 tags (both existing and pending) associated with a specific resource. </p>

        Raises:
            capo_comprehend.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Concurrent modification of the tags associated with an Amazon Comprehend resource is not supported. </p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.tag_resource

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_comprehend.types.comprehend_arn.ComprehendArn",
        tag_keys: "capo_comprehend.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
    ) -> "capo_comprehend.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a specific tag associated with an Amazon Comprehend resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the given Amazon Comprehend resource from which you want to remove the tags. </p>
            tag_keys: <p>The initial part of a key-value pair that forms a tag being removed from a given resource. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department. Keys must be unique and cannot be duplicated for a particular resource. </p>

        Raises:
            capo_comprehend.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Concurrent modification of the tags associated with an Amazon Comprehend resource is not supported. </p>
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_tag_keys_exception.TooManyTagKeysException: <p>The request contains more tag keys than can be associated with a resource (50 tag keys per resource).</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.untag_resource

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_endpoint(
        self,
        endpoint_arn: "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        desired_model_arn: Optional[
            "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
        ] = None,
        desired_inference_units: Optional[
            "capo_comprehend.types.inference_units_integer.InferenceUnitsInteger"
        ] = None,
        desired_data_access_role_arn: Optional[
            "capo_comprehend.types.iam_role_arn.IamRoleArn"
        ] = None,
        flywheel_arn: Optional[
            "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
        ] = None,
    ) -> "capo_comprehend.types.update_endpoint_response.UpdateEndpointResponse":
        """<p>Updates information about the specified endpoint. For information about endpoints, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html">Managing endpoints</a>.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Number (ARN) of the endpoint being updated.</p>
            desired_model_arn: <p>The ARN of the new model to use when updating an existing endpoint.</p>
            desired_inference_units: <p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>
            desired_data_access_role_arn: <p>Data access role ARN to use in case the new model is encrypted with a customer CMK.</p>
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource name is already in use. Use a different name and try your request again.</p>
            capo_comprehend.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available. Check the resource and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.update_endpoint_request.UpdateEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.update_endpoint_response.UpdateEndpointResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.update_endpoint

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.update_endpoint.async_update_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.update_endpoint_request.UpdateEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }
        if desired_model_arn is not None:
            input_["desired_model_arn"] = desired_model_arn
        if desired_inference_units is not None:
            input_["desired_inference_units"] = desired_inference_units
        if desired_data_access_role_arn is not None:
            input_["desired_data_access_role_arn"] = desired_data_access_role_arn
        if flywheel_arn is not None:
            input_["flywheel_arn"] = flywheel_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_flywheel(
        self,
        flywheel_arn: "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn",
        *,
        config_overrides: Optional[AsyncComprehendClientConfig] = None,
        active_model_arn: Optional[
            "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
        ] = None,
        data_access_role_arn: Optional[
            "capo_comprehend.types.iam_role_arn.IamRoleArn"
        ] = None,
        data_security_config: Optional[
            "capo_comprehend.types.update_data_security_config.UpdateDataSecurityConfig"
        ] = None,
    ) -> "capo_comprehend.types.update_flywheel_response.UpdateFlywheelResponse":
        """<p>Update the configuration information for an existing flywheel.</p>

        Args:
            flywheel_arn: <p>The Amazon Resource Number (ARN) of the flywheel to update.</p>
            active_model_arn: <p>The Amazon Resource Number (ARN) of the active model version.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.</p>
            data_security_config: <p>Flywheel data security configuration.</p>

        Raises:
            capo_comprehend.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_comprehend.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid.</p>
            capo_comprehend.errors.kms_key_validation_exception.KmsKeyValidationException: <p>The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.</p>
            capo_comprehend.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. Check the ARN and try your request again.</p>
            capo_comprehend.errors.too_many_requests_exception.TooManyRequestsException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_comprehend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_comprehend.types.update_flywheel_request.UpdateFlywheelRequest]",
        ) -> AsyncOperationResponse[
            "capo_comprehend.types.update_flywheel_response.UpdateFlywheelResponse"
        ]:
            import capo_comprehend._operations.comprehend_20171127.update_flywheel

            (
                output,
                http_response,
            ) = await capo_comprehend._operations.comprehend_20171127.update_flywheel.async_update_flywheel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_comprehend.types.update_flywheel_request.UpdateFlywheelRequest = {
            "flywheel_arn": flywheel_arn
        }
        if active_model_arn is not None:
            input_["active_model_arn"] = active_model_arn
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if data_security_config is not None:
            input_["data_security_config"] = data_security_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
