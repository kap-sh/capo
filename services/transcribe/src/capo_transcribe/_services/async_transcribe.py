"""Generated from Smithy shape ``com.amazonaws.transcribe#Transcribe``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_transcribe._auth._signers
import capo_transcribe._auth._sigv4
from capo_transcribe._auth._identity import Credentials
from capo_transcribe._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_transcribe._auth._zapros_handler import AuthMiddleware
from capo_transcribe._pagination import resolve_path as _resolve_path
from capo_transcribe._services._aws_config import aaws_config
from capo_transcribe._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_transcribe.types.base_model_name
    import capo_transcribe.types.boolean
    import capo_transcribe.types.call_analytics_job_name
    import capo_transcribe.types.call_analytics_job_settings
    import capo_transcribe.types.call_analytics_job_status
    import capo_transcribe.types.category_name
    import capo_transcribe.types.channel_definitions
    import capo_transcribe.types.clm_language_code
    import capo_transcribe.types.content_redaction
    import capo_transcribe.types.create_call_analytics_category_request
    import capo_transcribe.types.create_call_analytics_category_response
    import capo_transcribe.types.create_language_model_request
    import capo_transcribe.types.create_language_model_response
    import capo_transcribe.types.create_medical_vocabulary_request
    import capo_transcribe.types.create_medical_vocabulary_response
    import capo_transcribe.types.create_vocabulary_filter_request
    import capo_transcribe.types.create_vocabulary_filter_response
    import capo_transcribe.types.create_vocabulary_request
    import capo_transcribe.types.create_vocabulary_response
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.delete_call_analytics_category_request
    import capo_transcribe.types.delete_call_analytics_category_response
    import capo_transcribe.types.delete_call_analytics_job_request
    import capo_transcribe.types.delete_call_analytics_job_response
    import capo_transcribe.types.delete_language_model_request
    import capo_transcribe.types.delete_medical_scribe_job_request
    import capo_transcribe.types.delete_medical_transcription_job_request
    import capo_transcribe.types.delete_medical_vocabulary_request
    import capo_transcribe.types.delete_transcription_job_request
    import capo_transcribe.types.delete_vocabulary_filter_request
    import capo_transcribe.types.delete_vocabulary_request
    import capo_transcribe.types.describe_language_model_request
    import capo_transcribe.types.describe_language_model_response
    import capo_transcribe.types.encryption_configuration
    import capo_transcribe.types.get_call_analytics_category_request
    import capo_transcribe.types.get_call_analytics_category_response
    import capo_transcribe.types.get_call_analytics_job_request
    import capo_transcribe.types.get_call_analytics_job_response
    import capo_transcribe.types.get_medical_scribe_job_request
    import capo_transcribe.types.get_medical_scribe_job_response
    import capo_transcribe.types.get_medical_transcription_job_request
    import capo_transcribe.types.get_medical_transcription_job_response
    import capo_transcribe.types.get_medical_vocabulary_request
    import capo_transcribe.types.get_medical_vocabulary_response
    import capo_transcribe.types.get_transcription_job_request
    import capo_transcribe.types.get_transcription_job_response
    import capo_transcribe.types.get_vocabulary_filter_request
    import capo_transcribe.types.get_vocabulary_filter_response
    import capo_transcribe.types.get_vocabulary_request
    import capo_transcribe.types.get_vocabulary_response
    import capo_transcribe.types.input_data_config
    import capo_transcribe.types.input_type
    import capo_transcribe.types.job_execution_settings
    import capo_transcribe.types.kms_encryption_context_map
    import capo_transcribe.types.kms_key_id
    import capo_transcribe.types.language_code
    import capo_transcribe.types.language_id_settings_map
    import capo_transcribe.types.language_options
    import capo_transcribe.types.list_call_analytics_categories_request
    import capo_transcribe.types.list_call_analytics_categories_response
    import capo_transcribe.types.list_call_analytics_jobs_request
    import capo_transcribe.types.list_call_analytics_jobs_response
    import capo_transcribe.types.list_language_models_request
    import capo_transcribe.types.list_language_models_response
    import capo_transcribe.types.list_medical_scribe_jobs_request
    import capo_transcribe.types.list_medical_scribe_jobs_response
    import capo_transcribe.types.list_medical_transcription_jobs_request
    import capo_transcribe.types.list_medical_transcription_jobs_response
    import capo_transcribe.types.list_medical_vocabularies_request
    import capo_transcribe.types.list_medical_vocabularies_response
    import capo_transcribe.types.list_tags_for_resource_request
    import capo_transcribe.types.list_tags_for_resource_response
    import capo_transcribe.types.list_transcription_jobs_request
    import capo_transcribe.types.list_transcription_jobs_response
    import capo_transcribe.types.list_vocabularies_request
    import capo_transcribe.types.list_vocabularies_response
    import capo_transcribe.types.list_vocabulary_filters_request
    import capo_transcribe.types.list_vocabulary_filters_response
    import capo_transcribe.types.max_results
    import capo_transcribe.types.media
    import capo_transcribe.types.media_format
    import capo_transcribe.types.media_sample_rate_hertz
    import capo_transcribe.types.medical_content_identification_type
    import capo_transcribe.types.medical_media_sample_rate_hertz
    import capo_transcribe.types.medical_scribe_channel_definitions
    import capo_transcribe.types.medical_scribe_context
    import capo_transcribe.types.medical_scribe_job_status
    import capo_transcribe.types.medical_scribe_settings
    import capo_transcribe.types.medical_transcription_setting
    import capo_transcribe.types.model_name
    import capo_transcribe.types.model_settings
    import capo_transcribe.types.model_status
    import capo_transcribe.types.next_token
    import capo_transcribe.types.output_bucket_name
    import capo_transcribe.types.output_key
    import capo_transcribe.types.phrases
    import capo_transcribe.types.rule_list
    import capo_transcribe.types.settings
    import capo_transcribe.types.specialty
    import capo_transcribe.types.start_call_analytics_job_request
    import capo_transcribe.types.start_call_analytics_job_response
    import capo_transcribe.types.start_medical_scribe_job_request
    import capo_transcribe.types.start_medical_scribe_job_response
    import capo_transcribe.types.start_medical_transcription_job_request
    import capo_transcribe.types.start_medical_transcription_job_response
    import capo_transcribe.types.start_transcription_job_request
    import capo_transcribe.types.start_transcription_job_response
    import capo_transcribe.types.subtitles
    import capo_transcribe.types.tag_key_list
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.tag_resource_request
    import capo_transcribe.types.tag_resource_response
    import capo_transcribe.types.toxicity_detection
    import capo_transcribe.types.transcribe_arn
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.transcription_job_status
    import capo_transcribe.types.type
    import capo_transcribe.types.untag_resource_request
    import capo_transcribe.types.untag_resource_response
    import capo_transcribe.types.update_call_analytics_category_request
    import capo_transcribe.types.update_call_analytics_category_response
    import capo_transcribe.types.update_language_model_request
    import capo_transcribe.types.update_language_model_response
    import capo_transcribe.types.update_medical_vocabulary_request
    import capo_transcribe.types.update_medical_vocabulary_response
    import capo_transcribe.types.update_vocabulary_filter_request
    import capo_transcribe.types.update_vocabulary_filter_response
    import capo_transcribe.types.update_vocabulary_request
    import capo_transcribe.types.update_vocabulary_response
    import capo_transcribe.types.uri
    import capo_transcribe.types.vocabulary_filter_name
    import capo_transcribe.types.vocabulary_name
    import capo_transcribe.types.vocabulary_state
    import capo_transcribe.types.words


class AsyncTranscribeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncTranscribeClient:
    """A client for the ``Transcribe`` service.

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
        self._config = AsyncTranscribeClientConfig(
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
        self, config_overrides: Optional[AsyncTranscribeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTranscribeClientConfig = config_overrides or {}
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

    async def create_call_analytics_category(
        self,
        category_name: "capo_transcribe.types.category_name.CategoryName",
        rules: "capo_transcribe.types.rule_list.RuleList",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
        input_type: Optional["capo_transcribe.types.input_type.InputType"] = None,
    ) -> "capo_transcribe.types.create_call_analytics_category_response.CreateCallAnalyticsCategoryResponse":
        """<p>Creates a new Call Analytics category.</p> <p>All categories are automatically applied to your Call Analytics transcriptions. Note that in order to apply categories to your transcriptions, you must create them before submitting your transcription request, as categories cannot be applied retroactively.</p> <p>When creating a new category, you can use the <code>InputType</code> parameter to label the category as a <code>POST_CALL</code> or a <code>REAL_TIME</code> category. <code>POST_CALL</code> categories can only be applied to post-call transcriptions and <code>REAL_TIME</code> categories can only be applied to real-time transcriptions. If you do not include <code>InputType</code>, your category is created as a <code>POST_CALL</code> category by default.</p> <p>Call Analytics categories are composed of rules. For each category, you must create between 1 and 20 rules. Rules can include these parameters: , , , and .</p> <p>To update an existing category, see .</p> <p>To learn more about Call Analytics categories, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html">Creating categories for post-call transcriptions</a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html">Creating categories for real-time transcriptions</a>.</p>

        Args:
            category_name: <p>A unique name, chosen by you, for your Call Analytics category. It's helpful to use a detailed naming system that will make sense to you in the future. For example, it's better to use <code>sentiment-positive-last30seconds</code> for a category over a generic name like <code>test-category</code>.</p> <p>Category names are case sensitive.</p>
            rules: <p>Rules define a Call Analytics category. When creating a new category, you must create between 1 and 20 rules for that category. For each rule, you specify a filter you want applied to the attributes of a call. For example, you can choose a sentiment filter that detects if a customer's sentiment was positive during the last 30 seconds of the call.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new call analytics category at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>
            input_type: <p>Choose whether you want to create a real-time or a post-call category for your Call Analytics transcription.</p> <p>Specifying <code>POST_CALL</code> assigns your category to post-call transcriptions; categories with this input type cannot be applied to streaming (real-time) transcriptions.</p> <p>Specifying <code>REAL_TIME</code> assigns your category to streaming transcriptions; categories with this input type cannot be applied to post-call transcriptions.</p> <p>If you do not include <code>InputType</code>, your category is created as a post-call category by default.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.create_call_analytics_category_request.CreateCallAnalyticsCategoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.create_call_analytics_category_response.CreateCallAnalyticsCategoryResponse"
        ]:
            import capo_transcribe._operations.transcribe.create_call_analytics_category

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.create_call_analytics_category.async_create_call_analytics_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.create_call_analytics_category_request.CreateCallAnalyticsCategoryRequest = {
            "category_name": category_name,
            "rules": rules,
        }
        if tags is not None:
            input_["tags"] = tags
        if input_type is not None:
            input_["input_type"] = input_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_language_model(
        self,
        language_code: "capo_transcribe.types.clm_language_code.CLMLanguageCode",
        base_model_name: "capo_transcribe.types.base_model_name.BaseModelName",
        model_name: "capo_transcribe.types.model_name.ModelName",
        input_data_config: "capo_transcribe.types.input_data_config.InputDataConfig",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        encryption_configuration: Optional[
            "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
    ) -> "capo_transcribe.types.create_language_model_response.CreateLanguageModelResponse":
        """<p>Creates a new custom language model.</p> <p>When creating a new custom language model, you must specify:</p> <ul> <li> <p>If you want a Wideband (audio sample rates over 16,000 Hz) or Narrowband (audio sample rates under 16,000 Hz) base model</p> </li> <li> <p>The location of your training and tuning files (this must be an Amazon S3 URI)</p> </li> <li> <p>The language of your model</p> </li> <li> <p>A unique name for your model</p> </li> </ul>

        Args:
            language_code: <p>The language code that represents the language of your model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table. Note that US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p> <p>A custom language model can only be used to transcribe files in the same language as the model. For example, if you create a custom language model using US English (<code>en-US</code>), you can only apply this model to files that contain English audio.</p>
            base_model_name: <p>The Amazon Transcribe standard language model, or base model, used to create your custom language model. Amazon Transcribe offers two options for base models: Wideband and Narrowband.</p> <p>If the audio you want to transcribe has a sample rate of 16,000 Hz or greater, choose <code>WideBand</code>. To transcribe audio with a sample rate less than 16,000 Hz, choose <code>NarrowBand</code>.</p>
            model_name: <p>A unique name, chosen by you, for your custom language model.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom language model with the same name as an existing custom language model, you get a <code>ConflictException</code> error.</p>
            input_data_config: <p>Contains the Amazon S3 location of the training data you want to use to create a new custom language model, and permissions to access this location.</p> <p>When using <code>InputDataConfig</code>, you must include these sub-parameters: <code>S3Uri</code>, which is the Amazon S3 location of your training data, and <code>DataAccessRoleArn</code>, which is the Amazon Resource Name (ARN) of the role that has permission to access your specified Amazon S3 location. You can optionally include <code>TuningDataS3Uri</code>, which is the Amazon S3 location of your tuning data. If you specify different Amazon S3 locations for training and tuning data, the ARN you use must have permissions to access both locations.</p>
            encryption_configuration: <p>Specifies the encryption configuration for your custom language model. Your model artifacts are encrypted with the specified KMS key or with an AWS-owned key if a key is not supplied.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom language model at the time you create this new model.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.create_language_model_request.CreateLanguageModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.create_language_model_response.CreateLanguageModelResponse"
        ]:
            import capo_transcribe._operations.transcribe.create_language_model

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.create_language_model.async_create_language_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.create_language_model_request.CreateLanguageModelRequest = {
            "language_code": language_code,
            "base_model_name": base_model_name,
            "model_name": model_name,
            "input_data_config": input_data_config,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_medical_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        language_code: "capo_transcribe.types.language_code.LanguageCode",
        vocabulary_file_uri: "capo_transcribe.types.uri.Uri",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
    ) -> "capo_transcribe.types.create_medical_vocabulary_response.CreateMedicalVocabularyResponse":
        """<p>Creates a new custom medical vocabulary.</p> <p>Before creating a new custom medical vocabulary, you must first upload a text file that contains your vocabulary table into an Amazon S3 bucket. Note that this differs from , where you can include a list of terms within your request using the <code>Phrases</code> flag; <code>CreateMedicalVocabulary</code> does not support the <code>Phrases</code> flag and only accepts vocabularies in table format.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>

        Args:
            vocabulary_name: <p>A unique name, chosen by you, for your new custom medical vocabulary.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom medical vocabulary with the same name as an existing custom medical vocabulary, you get a <code>ConflictException</code> error.</p>
            language_code: <p>The language code that represents the language of the entries in your custom vocabulary. US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>
            vocabulary_file_uri: <p>The Amazon S3 location (URI) of the text file that contains your custom medical vocabulary. The URI must be in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom medical vocabulary at the time you create this new custom vocabulary.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.create_medical_vocabulary_request.CreateMedicalVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.create_medical_vocabulary_response.CreateMedicalVocabularyResponse"
        ]:
            import capo_transcribe._operations.transcribe.create_medical_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.create_medical_vocabulary.async_create_medical_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.create_medical_vocabulary_request.CreateMedicalVocabularyRequest = {
            "vocabulary_name": vocabulary_name,
            "language_code": language_code,
            "vocabulary_file_uri": vocabulary_file_uri,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        language_code: "capo_transcribe.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        phrases: Optional["capo_transcribe.types.phrases.Phrases"] = None,
        vocabulary_file_uri: Optional["capo_transcribe.types.uri.Uri"] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
        data_access_role_arn: Optional[
            "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
        ] = None,
        encryption_configuration: Optional[
            "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_transcribe.types.create_vocabulary_response.CreateVocabularyResponse":
        """<p>Creates a new custom vocabulary.</p> <p>When creating a new custom vocabulary, you can either upload a text file that contains your new entries, phrases, and terms into an Amazon S3 bucket and include the URI in your request. Or you can include a list of terms directly in your request using the <code>Phrases</code> flag.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html">Custom vocabularies</a>.</p>

        Args:
            vocabulary_name: <p>A unique name, chosen by you, for your new custom vocabulary.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom vocabulary with the same name as an existing custom vocabulary, you get a <code>ConflictException</code> error.</p>
            language_code: <p>The language code that represents the language of the entries in your custom vocabulary. Each custom vocabulary must contain terms in only one language.</p> <p>A custom vocabulary can only be used to transcribe files in the same language as the custom vocabulary. For example, if you create a custom vocabulary using US English (<code>en-US</code>), you can only apply this custom vocabulary to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>
            phrases: <p>Use this parameter if you want to create your custom vocabulary by including all desired terms, as comma-separated values, within your request. The other option for creating your custom vocabulary is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFileUri</code> parameter.</p> <p>Note that if you include <code>Phrases</code> in your request, you cannot use <code>VocabularyFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>
            vocabulary_file_uri: <p>The Amazon S3 location of the text file that contains your custom vocabulary. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p> <p>Note that if you include <code>VocabularyFileUri</code> in your request, you cannot use the <code>Phrases</code> flag; you must choose one or the other.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom vocabulary at the time you create this new custom vocabulary.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary). If you include <code>EncryptionConfiguration</code> in your request, this role must also have permissions to access the specified KMS key. If the role that you specify doesn’t have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            encryption_configuration: <p>Specifies the encryption configuration for your custom vocabulary. Your vocabulary artifacts are encrypted with the specified KMS key or with an AWS-owned key if a key is not supplied.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.create_vocabulary_request.CreateVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.create_vocabulary_response.CreateVocabularyResponse"
        ]:
            import capo_transcribe._operations.transcribe.create_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.create_vocabulary.async_create_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.create_vocabulary_request.CreateVocabularyRequest = {
            "vocabulary_name": vocabulary_name,
            "language_code": language_code,
        }
        if phrases is not None:
            input_["phrases"] = phrases
        if vocabulary_file_uri is not None:
            input_["vocabulary_file_uri"] = vocabulary_file_uri
        if tags is not None:
            input_["tags"] = tags
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_vocabulary_filter(
        self,
        vocabulary_filter_name: "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName",
        language_code: "capo_transcribe.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        words: Optional["capo_transcribe.types.words.Words"] = None,
        vocabulary_filter_file_uri: Optional["capo_transcribe.types.uri.Uri"] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
        data_access_role_arn: Optional[
            "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
        ] = None,
        encryption_configuration: Optional[
            "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_transcribe.types.create_vocabulary_filter_response.CreateVocabularyFilterResponse":
        """<p>Creates a new custom vocabulary filter.</p> <p>You can use custom vocabulary filters to mask, delete, or flag specific words from your transcript. Custom vocabulary filters are commonly used to mask profanity in transcripts.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/vocabulary-filtering.html">Vocabulary filtering</a>.</p>

        Args:
            vocabulary_filter_name: <p>A unique name, chosen by you, for your new custom vocabulary filter.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new custom vocabulary filter with the same name as an existing custom vocabulary filter, you get a <code>ConflictException</code> error.</p>
            language_code: <p>The language code that represents the language of the entries in your vocabulary filter. Each custom vocabulary filter must contain terms in only one language.</p> <p>A custom vocabulary filter can only be used to transcribe files in the same language as the filter. For example, if you create a custom vocabulary filter using US English (<code>en-US</code>), you can only apply this filter to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>
            words: <p>Use this parameter if you want to create your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for creating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFilterFileUri</code> parameter.</p> <p>Note that if you include <code>Words</code> in your request, you cannot use <code>VocabularyFilterFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>
            vocabulary_filter_file_uri: <p>The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt</code> </p> <p>Note that if you include <code>VocabularyFilterFileUri</code> in your request, you cannot use <code>Words</code>; you must choose one or the other.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new custom vocabulary filter at the time you create this new vocabulary filter.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If you include <code>EncryptionConfiguration</code> in your request, this role must also have permissions to access the specified KMS key. If the role that you specify doesn’t have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            encryption_configuration: <p>Specifies the encryption configuration for your custom vocabulary filter. Your vocabulary filter artifacts are encrypted with the specified KMS key or with an AWS-owned key if a key is not supplied.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.create_vocabulary_filter_request.CreateVocabularyFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.create_vocabulary_filter_response.CreateVocabularyFilterResponse"
        ]:
            import capo_transcribe._operations.transcribe.create_vocabulary_filter

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.create_vocabulary_filter.async_create_vocabulary_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.create_vocabulary_filter_request.CreateVocabularyFilterRequest = {
            "vocabulary_filter_name": vocabulary_filter_name,
            "language_code": language_code,
        }
        if words is not None:
            input_["words"] = words
        if vocabulary_filter_file_uri is not None:
            input_["vocabulary_filter_file_uri"] = vocabulary_filter_file_uri
        if tags is not None:
            input_["tags"] = tags
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_call_analytics_category(
        self,
        category_name: "capo_transcribe.types.category_name.CategoryName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.delete_call_analytics_category_response.DeleteCallAnalyticsCategoryResponse":
        """<p>Deletes a Call Analytics category. To use this operation, specify the name of the category you want to delete using <code>CategoryName</code>. Category names are case sensitive.</p>

        Args:
            category_name: <p>The name of the Call Analytics category you want to delete. Category names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_call_analytics_category_request.DeleteCallAnalyticsCategoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.delete_call_analytics_category_response.DeleteCallAnalyticsCategoryResponse"
        ]:
            import capo_transcribe._operations.transcribe.delete_call_analytics_category

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_call_analytics_category.async_delete_call_analytics_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_call_analytics_category_request.DeleteCallAnalyticsCategoryRequest = {
            "category_name": category_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_call_analytics_job(
        self,
        call_analytics_job_name: "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.delete_call_analytics_job_response.DeleteCallAnalyticsJobResponse":
        """<p>Deletes a Call Analytics job. To use this operation, specify the name of the job you want to delete using <code>CallAnalyticsJobName</code>. Job names are case sensitive.</p>

        Args:
            call_analytics_job_name: <p>The name of the Call Analytics job you want to delete. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_call_analytics_job_request.DeleteCallAnalyticsJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.delete_call_analytics_job_response.DeleteCallAnalyticsJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.delete_call_analytics_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_call_analytics_job.async_delete_call_analytics_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_call_analytics_job_request.DeleteCallAnalyticsJobRequest = {
            "call_analytics_job_name": call_analytics_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_language_model(
        self,
        model_name: "capo_transcribe.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a custom language model. To use this operation, specify the name of the language model you want to delete using <code>ModelName</code>. custom language model names are case sensitive.</p>

        Args:
            model_name: <p>The name of the custom language model you want to delete. Model names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_language_model_request.DeleteLanguageModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_language_model

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_language_model.async_delete_language_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_language_model_request.DeleteLanguageModelRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_medical_scribe_job(
        self,
        medical_scribe_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a Medical Scribe job. To use this operation, specify the name of the job you want to delete using <code>MedicalScribeJobName</code>. Job names are case sensitive.</p>

        Args:
            medical_scribe_job_name: <p>The name of the Medical Scribe job you want to delete. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_medical_scribe_job_request.DeleteMedicalScribeJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_medical_scribe_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_medical_scribe_job.async_delete_medical_scribe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_medical_scribe_job_request.DeleteMedicalScribeJobRequest = {
            "medical_scribe_job_name": medical_scribe_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_medical_transcription_job(
        self,
        medical_transcription_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a medical transcription job. To use this operation, specify the name of the job you want to delete using <code>MedicalTranscriptionJobName</code>. Job names are case sensitive.</p>

        Args:
            medical_transcription_job_name: <p>The name of the medical transcription job you want to delete. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_medical_transcription_job_request.DeleteMedicalTranscriptionJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_medical_transcription_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_medical_transcription_job.async_delete_medical_transcription_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_medical_transcription_job_request.DeleteMedicalTranscriptionJobRequest = {
            "medical_transcription_job_name": medical_transcription_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_medical_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a custom medical vocabulary. To use this operation, specify the name of the custom vocabulary you want to delete using <code>VocabularyName</code>. Custom vocabulary names are case sensitive.</p>

        Args:
            vocabulary_name: <p>The name of the custom medical vocabulary you want to delete. Custom medical vocabulary names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_medical_vocabulary_request.DeleteMedicalVocabularyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_medical_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_medical_vocabulary.async_delete_medical_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_medical_vocabulary_request.DeleteMedicalVocabularyRequest = {
            "vocabulary_name": vocabulary_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_transcription_job(
        self,
        transcription_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a transcription job. To use this operation, specify the name of the job you want to delete using <code>TranscriptionJobName</code>. Job names are case sensitive.</p>

        Args:
            transcription_job_name: <p>The name of the transcription job you want to delete. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_transcription_job_request.DeleteTranscriptionJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_transcription_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_transcription_job.async_delete_transcription_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_transcription_job_request.DeleteTranscriptionJobRequest = {
            "transcription_job_name": transcription_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a custom vocabulary. To use this operation, specify the name of the custom vocabulary you want to delete using <code>VocabularyName</code>. Custom vocabulary names are case sensitive.</p>

        Args:
            vocabulary_name: <p>The name of the custom vocabulary you want to delete. Custom vocabulary names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_vocabulary_request.DeleteVocabularyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_vocabulary.async_delete_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_vocabulary_request.DeleteVocabularyRequest = {
            "vocabulary_name": vocabulary_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vocabulary_filter(
        self,
        vocabulary_filter_name: "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> None:
        """<p>Deletes a custom vocabulary filter. To use this operation, specify the name of the custom vocabulary filter you want to delete using <code>VocabularyFilterName</code>. Custom vocabulary filter names are case sensitive.</p>

        Args:
            vocabulary_filter_name: <p>The name of the custom vocabulary filter you want to delete. Custom vocabulary filter names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.delete_vocabulary_filter_request.DeleteVocabularyFilterRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transcribe._operations.transcribe.delete_vocabulary_filter

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.delete_vocabulary_filter.async_delete_vocabulary_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.delete_vocabulary_filter_request.DeleteVocabularyFilterRequest = {
            "vocabulary_filter_name": vocabulary_filter_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_language_model(
        self,
        model_name: "capo_transcribe.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.describe_language_model_response.DescribeLanguageModelResponse":
        """<p>Provides information about the specified custom language model.</p> <p>This operation also shows if the base language model that you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.</p> <p>If you tried to create a new custom language model and the request wasn't successful, you can use <code>DescribeLanguageModel</code> to help identify the reason for this failure.</p>

        Args:
            model_name: <p>The name of the custom language model you want information about. Model names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.describe_language_model_request.DescribeLanguageModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.describe_language_model_response.DescribeLanguageModelResponse"
        ]:
            import capo_transcribe._operations.transcribe.describe_language_model

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.describe_language_model.async_describe_language_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.describe_language_model_request.DescribeLanguageModelRequest = {
            "model_name": model_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_call_analytics_category(
        self,
        category_name: "capo_transcribe.types.category_name.CategoryName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_call_analytics_category_response.GetCallAnalyticsCategoryResponse":
        """<p>Provides information about the specified Call Analytics category.</p> <p>To get a list of your Call Analytics categories, use the operation.</p>

        Args:
            category_name: <p>The name of the Call Analytics category you want information about. Category names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_call_analytics_category_request.GetCallAnalyticsCategoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_call_analytics_category_response.GetCallAnalyticsCategoryResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_call_analytics_category

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_call_analytics_category.async_get_call_analytics_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_call_analytics_category_request.GetCallAnalyticsCategoryRequest = {
            "category_name": category_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_call_analytics_job(
        self,
        call_analytics_job_name: "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_call_analytics_job_response.GetCallAnalyticsJobResponse":
        """<p>Provides information about the specified Call Analytics job.</p> <p>To view the job's status, refer to <code>CallAnalyticsJobStatus</code>. If the status is <code>COMPLETED</code>, the job is finished. You can find your completed transcript at the URI specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p> <p>If you enabled personally identifiable information (PII) redaction, the redacted transcript appears at the location specified in <code>RedactedTranscriptFileUri</code>.</p> <p>If you chose to redact the audio in your media file, you can find your redacted media file at the location specified in <code>RedactedMediaFileUri</code>.</p> <p>To get a list of your Call Analytics jobs, use the operation.</p>

        Args:
            call_analytics_job_name: <p>The name of the Call Analytics job you want information about. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_call_analytics_job_request.GetCallAnalyticsJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_call_analytics_job_response.GetCallAnalyticsJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_call_analytics_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_call_analytics_job.async_get_call_analytics_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_call_analytics_job_request.GetCallAnalyticsJobRequest = {
            "call_analytics_job_name": call_analytics_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_medical_scribe_job(
        self,
        medical_scribe_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_medical_scribe_job_response.GetMedicalScribeJobResponse":
        """<p>Provides information about the specified Medical Scribe job.</p> <p>To view the status of the specified medical transcription job, check the <code>MedicalScribeJobStatus</code> field. If the status is <code>COMPLETED</code>, the job is finished. You can find the results at the location specified in <code>MedicalScribeOutput</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your Medical Scribe job failed.</p> <p>To get a list of your Medical Scribe jobs, use the operation.</p>

        Args:
            medical_scribe_job_name: <p>The name of the Medical Scribe job you want information about. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_medical_scribe_job_request.GetMedicalScribeJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_medical_scribe_job_response.GetMedicalScribeJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_medical_scribe_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_medical_scribe_job.async_get_medical_scribe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_medical_scribe_job_request.GetMedicalScribeJobRequest = {
            "medical_scribe_job_name": medical_scribe_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_medical_transcription_job(
        self,
        medical_transcription_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_medical_transcription_job_response.GetMedicalTranscriptionJobResponse":
        """<p>Provides information about the specified medical transcription job.</p> <p>To view the status of the specified medical transcription job, check the <code>TranscriptionJobStatus</code> field. If the status is <code>COMPLETED</code>, the job is finished. You can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p> <p>To get a list of your medical transcription jobs, use the operation.</p>

        Args:
            medical_transcription_job_name: <p>The name of the medical transcription job you want information about. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_medical_transcription_job_request.GetMedicalTranscriptionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_medical_transcription_job_response.GetMedicalTranscriptionJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_medical_transcription_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_medical_transcription_job.async_get_medical_transcription_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_medical_transcription_job_request.GetMedicalTranscriptionJobRequest = {
            "medical_transcription_job_name": medical_transcription_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_medical_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_medical_vocabulary_response.GetMedicalVocabularyResponse":
        """<p>Provides information about the specified custom medical vocabulary.</p> <p>To view the status of the specified custom medical vocabulary, check the <code>VocabularyState</code> field. If the status is <code>READY</code>, your custom vocabulary is available to use. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your vocabulary failed.</p> <p>To get a list of your custom medical vocabularies, use the operation.</p>

        Args:
            vocabulary_name: <p>The name of the custom medical vocabulary you want information about. Custom medical vocabulary names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_medical_vocabulary_request.GetMedicalVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_medical_vocabulary_response.GetMedicalVocabularyResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_medical_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_medical_vocabulary.async_get_medical_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_medical_vocabulary_request.GetMedicalVocabularyRequest = {
            "vocabulary_name": vocabulary_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_transcription_job(
        self,
        transcription_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_transcription_job_response.GetTranscriptionJobResponse":
        """<p>Provides information about the specified transcription job.</p> <p>To view the status of the specified transcription job, check the <code>TranscriptionJobStatus</code> field. If the status is <code>COMPLETED</code>, the job is finished. You can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p> <p>If you enabled content redaction, the redacted transcript can be found at the location specified in <code>RedactedTranscriptFileUri</code>.</p> <p>To get a list of your transcription jobs, use the operation.</p>

        Args:
            transcription_job_name: <p>The name of the transcription job you want information about. Job names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_transcription_job_request.GetTranscriptionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_transcription_job_response.GetTranscriptionJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_transcription_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_transcription_job.async_get_transcription_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_transcription_job_request.GetTranscriptionJobRequest = {
            "transcription_job_name": transcription_job_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_vocabulary_response.GetVocabularyResponse":
        """<p>Provides information about the specified custom vocabulary.</p> <p>To view the status of the specified custom vocabulary, check the <code>VocabularyState</code> field. If the status is <code>READY</code>, your custom vocabulary is available to use. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your custom vocabulary failed.</p> <p>To get a list of your custom vocabularies, use the operation.</p>

        Args:
            vocabulary_name: <p>The name of the custom vocabulary you want information about. Custom vocabulary names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_vocabulary_request.GetVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_vocabulary_response.GetVocabularyResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_vocabulary.async_get_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_vocabulary_request.GetVocabularyRequest = {
            "vocabulary_name": vocabulary_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vocabulary_filter(
        self,
        vocabulary_filter_name: "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.get_vocabulary_filter_response.GetVocabularyFilterResponse":
        """<p>Provides information about the specified custom vocabulary filter.</p> <p>To get a list of your custom vocabulary filters, use the operation.</p>

        Args:
            vocabulary_filter_name: <p>The name of the custom vocabulary filter you want information about. Custom vocabulary filter names are case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.get_vocabulary_filter_request.GetVocabularyFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.get_vocabulary_filter_response.GetVocabularyFilterResponse"
        ]:
            import capo_transcribe._operations.transcribe.get_vocabulary_filter

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.get_vocabulary_filter.async_get_vocabulary_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.get_vocabulary_filter_request.GetVocabularyFilterRequest = {
            "vocabulary_filter_name": vocabulary_filter_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_call_analytics_categories(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "capo_transcribe.types.list_call_analytics_categories_response.ListCallAnalyticsCategoriesResponse":
        """<p>Provides a list of Call Analytics categories, including all rules that make up each category.</p> <p>To get detailed information about a specific Call Analytics category, use the operation.</p>

        Args:
            next_token: <p>If your <code>ListCallAnalyticsCategories</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of Call Analytics categories to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_call_analytics_categories_request.ListCallAnalyticsCategoriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_call_analytics_categories_response.ListCallAnalyticsCategoriesResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_call_analytics_categories

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_call_analytics_categories.async_list_call_analytics_categories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_call_analytics_categories_request.ListCallAnalyticsCategoriesRequest = {}
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

    async def iter_list_call_analytics_categories(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_call_analytics_categories_response.ListCallAnalyticsCategoriesResponse]":
        _token = next_token
        while True:
            _response = await self.list_call_analytics_categories(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_call_analytics_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.call_analytics_job_status.CallAnalyticsJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "capo_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse":
        """<p>Provides a list of Call Analytics jobs that match the specified criteria. If no criteria are specified, all Call Analytics jobs are returned.</p> <p>To get detailed information about a specific Call Analytics job, use the operation.</p>

        Args:
            status: <p>Returns only Call Analytics jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all Call Analytics jobs are returned.</p>
            job_name_contains: <p>Returns only the Call Analytics jobs that contain the specified string. The search is not case sensitive.</p>
            next_token: <p>If your <code>ListCallAnalyticsJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of Call Analytics jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_call_analytics_jobs_request.ListCallAnalyticsJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_call_analytics_jobs

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_call_analytics_jobs.async_list_call_analytics_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_call_analytics_jobs_request.ListCallAnalyticsJobsRequest = {}
        if status is not None:
            input_["status"] = status
        if job_name_contains is not None:
            input_["job_name_contains"] = job_name_contains
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

    async def iter_list_call_analytics_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.call_analytics_job_status.CallAnalyticsJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_call_analytics_jobs_response.ListCallAnalyticsJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_call_analytics_jobs(
                config_overrides=config_overrides,
                status=status,
                job_name_contains=job_name_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_language_models(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status_equals: Optional[
            "capo_transcribe.types.model_status.ModelStatus"
        ] = None,
        name_contains: Optional["capo_transcribe.types.model_name.ModelName"] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_transcribe.types.list_language_models_response.ListLanguageModelsResponse"
    ):
        """<p>Provides a list of custom language models that match the specified criteria. If no criteria are specified, all custom language models are returned.</p> <p>To get detailed information about a specific custom language model, use the operation.</p>

        Args:
            status_equals: <p>Returns only custom language models with the specified status. Language models are ordered by creation date, with the newest model first. If you do not include <code>StatusEquals</code>, all custom language models are returned.</p>
            name_contains: <p>Returns only the custom language models that contain the specified string. The search is not case sensitive.</p>
            next_token: <p>If your <code>ListLanguageModels</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of custom language models to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_language_models_request.ListLanguageModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_language_models_response.ListLanguageModelsResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_language_models

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_language_models.async_list_language_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_language_models_request.ListLanguageModelsRequest = {}
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
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

    async def iter_list_language_models(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status_equals: Optional[
            "capo_transcribe.types.model_status.ModelStatus"
        ] = None,
        name_contains: Optional["capo_transcribe.types.model_name.ModelName"] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_language_models_response.ListLanguageModelsResponse]":
        _token = next_token
        while True:
            _response = await self.list_language_models(
                config_overrides=config_overrides,
                status_equals=status_equals,
                name_contains=name_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_medical_scribe_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.medical_scribe_job_status.MedicalScribeJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "capo_transcribe.types.list_medical_scribe_jobs_response.ListMedicalScribeJobsResponse":
        """<p>Provides a list of Medical Scribe jobs that match the specified criteria. If no criteria are specified, all Medical Scribe jobs are returned.</p> <p>To get detailed information about a specific Medical Scribe job, use the operation.</p>

        Args:
            status: <p>Returns only Medical Scribe jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all Medical Scribe jobs are returned.</p>
            job_name_contains: <p>Returns only the Medical Scribe jobs that contain the specified string. The search is not case sensitive.</p>
            next_token: <p>If your <code>ListMedicalScribeJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of Medical Scribe jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_medical_scribe_jobs_request.ListMedicalScribeJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_medical_scribe_jobs_response.ListMedicalScribeJobsResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_medical_scribe_jobs

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_medical_scribe_jobs.async_list_medical_scribe_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_medical_scribe_jobs_request.ListMedicalScribeJobsRequest = {}
        if status is not None:
            input_["status"] = status
        if job_name_contains is not None:
            input_["job_name_contains"] = job_name_contains
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

    async def iter_list_medical_scribe_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.medical_scribe_job_status.MedicalScribeJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_medical_scribe_jobs_response.ListMedicalScribeJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_medical_scribe_jobs(
                config_overrides=config_overrides,
                status=status,
                job_name_contains=job_name_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_medical_transcription_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "capo_transcribe.types.list_medical_transcription_jobs_response.ListMedicalTranscriptionJobsResponse":
        """<p>Provides a list of medical transcription jobs that match the specified criteria. If no criteria are specified, all medical transcription jobs are returned.</p> <p>To get detailed information about a specific medical transcription job, use the operation.</p>

        Args:
            status: <p>Returns only medical transcription jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all medical transcription jobs are returned.</p>
            job_name_contains: <p>Returns only the medical transcription jobs that contain the specified string. The search is not case sensitive.</p>
            next_token: <p>If your <code>ListMedicalTranscriptionJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of medical transcription jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_medical_transcription_jobs_request.ListMedicalTranscriptionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_medical_transcription_jobs_response.ListMedicalTranscriptionJobsResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_medical_transcription_jobs

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_medical_transcription_jobs.async_list_medical_transcription_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_medical_transcription_jobs_request.ListMedicalTranscriptionJobsRequest = {}
        if status is not None:
            input_["status"] = status
        if job_name_contains is not None:
            input_["job_name_contains"] = job_name_contains
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

    async def iter_list_medical_transcription_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_medical_transcription_jobs_response.ListMedicalTranscriptionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_medical_transcription_jobs(
                config_overrides=config_overrides,
                status=status,
                job_name_contains=job_name_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_medical_vocabularies(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
        state_equals: Optional[
            "capo_transcribe.types.vocabulary_state.VocabularyState"
        ] = None,
        name_contains: Optional[
            "capo_transcribe.types.vocabulary_name.VocabularyName"
        ] = None,
    ) -> "capo_transcribe.types.list_medical_vocabularies_response.ListMedicalVocabulariesResponse":
        """<p>Provides a list of custom medical vocabularies that match the specified criteria. If no criteria are specified, all custom medical vocabularies are returned.</p> <p>To get detailed information about a specific custom medical vocabulary, use the operation.</p>

        Args:
            next_token: <p>If your <code>ListMedicalVocabularies</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of custom medical vocabularies to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>
            state_equals: <p>Returns only custom medical vocabularies with the specified state. Custom vocabularies are ordered by creation date, with the newest vocabulary first. If you do not include <code>StateEquals</code>, all custom medical vocabularies are returned.</p>
            name_contains: <p>Returns only the custom medical vocabularies that contain the specified string. The search is not case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_medical_vocabularies_request.ListMedicalVocabulariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_medical_vocabularies_response.ListMedicalVocabulariesResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_medical_vocabularies

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_medical_vocabularies.async_list_medical_vocabularies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_medical_vocabularies_request.ListMedicalVocabulariesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state_equals is not None:
            input_["state_equals"] = state_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_medical_vocabularies(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
        state_equals: Optional[
            "capo_transcribe.types.vocabulary_state.VocabularyState"
        ] = None,
        name_contains: Optional[
            "capo_transcribe.types.vocabulary_name.VocabularyName"
        ] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_medical_vocabularies_response.ListMedicalVocabulariesResponse]":
        _token = next_token
        while True:
            _response = await self.list_medical_vocabularies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                state_equals=state_equals,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_transcribe.types.transcribe_arn.TranscribeArn",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags associated with the specified transcription job, vocabulary, model, or resource.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>

        Args:
            resource_arn: <p>Returns a list of all tags associated with the specified Amazon Resource Name (ARN). ARNs have the format <code>arn:partition:service:region:account-id:resource-type/resource-id</code>.</p> <p>For example, <code>arn:aws:transcribe:us-west-2:111122223333:transcription-job/transcription-job-name</code>.</p> <p>Valid values for <code>resource-type</code> are: <code>transcription-job</code>, <code>medical-transcription-job</code>, <code>vocabulary</code>, <code>medical-vocabulary</code>, <code>vocabulary-filter</code>, and <code>language-model</code>.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_transcription_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "capo_transcribe.types.list_transcription_jobs_response.ListTranscriptionJobsResponse":
        """<p>Provides a list of transcription jobs that match the specified criteria. If no criteria are specified, all transcription jobs are returned.</p> <p>To get detailed information about a specific transcription job, use the operation.</p>

        Args:
            status: <p>Returns only transcription jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all transcription jobs are returned.</p>
            job_name_contains: <p>Returns only the transcription jobs that contain the specified string. The search is not case sensitive.</p>
            next_token: <p>If your <code>ListTranscriptionJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of transcription jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_transcription_jobs_request.ListTranscriptionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_transcription_jobs_response.ListTranscriptionJobsResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_transcription_jobs

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_transcription_jobs.async_list_transcription_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_transcription_jobs_request.ListTranscriptionJobsRequest = {}
        if status is not None:
            input_["status"] = status
        if job_name_contains is not None:
            input_["job_name_contains"] = job_name_contains
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

    async def iter_list_transcription_jobs(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        status: Optional[
            "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
        ] = None,
        job_name_contains: Optional[
            "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
        ] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_transcription_jobs_response.ListTranscriptionJobsResponse]":
        _token = next_token
        while True:
            _response = await self.list_transcription_jobs(
                config_overrides=config_overrides,
                status=status,
                job_name_contains=job_name_contains,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_vocabularies(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
        state_equals: Optional[
            "capo_transcribe.types.vocabulary_state.VocabularyState"
        ] = None,
        name_contains: Optional[
            "capo_transcribe.types.vocabulary_name.VocabularyName"
        ] = None,
    ) -> "capo_transcribe.types.list_vocabularies_response.ListVocabulariesResponse":
        """<p>Provides a list of custom vocabularies that match the specified criteria. If no criteria are specified, all custom vocabularies are returned.</p> <p>To get detailed information about a specific custom vocabulary, use the operation.</p>

        Args:
            next_token: <p>If your <code>ListVocabularies</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of custom vocabularies to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>
            state_equals: <p>Returns only custom vocabularies with the specified state. Vocabularies are ordered by creation date, with the newest vocabulary first. If you do not include <code>StateEquals</code>, all custom medical vocabularies are returned.</p>
            name_contains: <p>Returns only the custom vocabularies that contain the specified string. The search is not case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_vocabularies_request.ListVocabulariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_vocabularies_response.ListVocabulariesResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_vocabularies

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_vocabularies.async_list_vocabularies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_vocabularies_request.ListVocabulariesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state_equals is not None:
            input_["state_equals"] = state_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_vocabularies(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
        state_equals: Optional[
            "capo_transcribe.types.vocabulary_state.VocabularyState"
        ] = None,
        name_contains: Optional[
            "capo_transcribe.types.vocabulary_name.VocabularyName"
        ] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_vocabularies_response.ListVocabulariesResponse]":
        _token = next_token
        while True:
            _response = await self.list_vocabularies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                state_equals=state_equals,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_vocabulary_filters(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
        name_contains: Optional[
            "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
        ] = None,
    ) -> "capo_transcribe.types.list_vocabulary_filters_response.ListVocabularyFiltersResponse":
        """<p>Provides a list of custom vocabulary filters that match the specified criteria. If no criteria are specified, all custom vocabularies are returned.</p> <p>To get detailed information about a specific custom vocabulary filter, use the operation.</p>

        Args:
            next_token: <p>If your <code>ListVocabularyFilters</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>
            max_results: <p>The maximum number of custom vocabulary filters to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>
            name_contains: <p>Returns only the custom vocabulary filters that contain the specified string. The search is not case sensitive.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.list_vocabulary_filters_request.ListVocabularyFiltersRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.list_vocabulary_filters_response.ListVocabularyFiltersResponse"
        ]:
            import capo_transcribe._operations.transcribe.list_vocabulary_filters

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.list_vocabulary_filters.async_list_vocabulary_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.list_vocabulary_filters_request.ListVocabularyFiltersRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if name_contains is not None:
            input_["name_contains"] = name_contains

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_vocabulary_filters(
        self,
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        next_token: Optional["capo_transcribe.types.next_token.NextToken"] = None,
        max_results: Optional["capo_transcribe.types.max_results.MaxResults"] = None,
        name_contains: Optional[
            "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName"
        ] = None,
    ) -> "AsyncIterator[capo_transcribe.types.list_vocabulary_filters_response.ListVocabularyFiltersResponse]":
        _token = next_token
        while True:
            _response = await self.list_vocabulary_filters(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                name_contains=name_contains,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_call_analytics_job(
        self,
        call_analytics_job_name: "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName",
        media: "capo_transcribe.types.media.Media",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        output_location: Optional["capo_transcribe.types.uri.Uri"] = None,
        output_encryption_kms_key_id: Optional[
            "capo_transcribe.types.kms_key_id.KMSKeyId"
        ] = None,
        data_access_role_arn: Optional[
            "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
        ] = None,
        settings: Optional[
            "capo_transcribe.types.call_analytics_job_settings.CallAnalyticsJobSettings"
        ] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
        channel_definitions: Optional[
            "capo_transcribe.types.channel_definitions.ChannelDefinitions"
        ] = None,
    ) -> "capo_transcribe.types.start_call_analytics_job_response.StartCallAnalyticsJobResponse":
        """<p>Transcribes the audio from a customer service call and applies any additional Request Parameters you choose to include in your request.</p> <p>In addition to many standard transcription features, Call Analytics provides you with call characteristics, call summarization, speaker sentiment, and optional redaction of your text transcript and your audio file. You can also apply custom categories to flag specified conditions. To learn more about these features and insights, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html">Analyzing call center audio with Call Analytics</a>.</p> <p>If you want to apply categories to your Call Analytics job, you must create them before submitting your job request. Categories cannot be retroactively applied to a job. To create a new category, use the operation. To learn more about Call Analytics categories, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html">Creating categories for post-call transcriptions</a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html">Creating categories for real-time transcriptions</a>.</p> <p>To make a <code>StartCallAnalyticsJob</code> request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the <code>Media</code> parameter.</p> <p>Job queuing is available for Call Analytics jobs. If you pass a <code>DataAccessRoleArn</code> in your request and you exceed your Concurrent Job Limit, your job will automatically be added to a queue to be processed once your concurrent job count is below the limit.</p> <p>You must include the following parameters in your <code>StartCallAnalyticsJob</code> request:</p> <ul> <li> <p> <code>region</code>: The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html">Amazon Transcribe endpoints and quotas</a>.</p> </li> <li> <p> <code>CallAnalyticsJobName</code>: A custom name that you create for your transcription job that's unique within your Amazon Web Services account.</p> </li> <li> <p> <code>Media</code> (<code>MediaFileUri</code> or <code>RedactedMediaFileUri</code>): The Amazon S3 location of your media file.</p> </li> </ul> <note> <p>With Call Analytics, you can redact the audio contained in your media file by including <code>RedactedMediaFileUri</code>, instead of <code>MediaFileUri</code>, to specify the location of your input audio. If you choose to redact your audio, you can find your redacted media at the location specified in the <code>RedactedMediaFileUri</code> field of your response.</p> </note>

        Args:
            call_analytics_job_name: <p>A unique name, chosen by you, for your Call Analytics job.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>
            media: <p>Describes the Amazon S3 location of the media file you want to use in your Call Analytics request.</p>
            output_location: <p>The Amazon S3 location where you want your Call Analytics transcription output stored. You can use any of the following formats to specify the output location:</p> <ol> <li> <p>s3://DOC-EXAMPLE-BUCKET</p> </li> <li> <p>s3://DOC-EXAMPLE-BUCKET/my-output-folder/</p> </li> <li> <p>s3://DOC-EXAMPLE-BUCKET/my-output-folder/my-call-analytics-job.json</p> </li> </ol> <p>Unless you specify a file name (option 3), the name of your output file has a default value that matches the name you specified for your transcription job using the <code>CallAnalyticsJobName</code> parameter.</p> <p>You can specify a KMS key to encrypt your output using the <code>OutputEncryptionKMSKeyId</code> parameter. If you do not specify a KMS key, Amazon Transcribe uses the default Amazon S3 key for server-side encryption.</p> <p>If you do not specify <code>OutputLocation</code>, your transcript is placed in a service-managed Amazon S3 bucket and you are provided with a URI to access your transcript.</p>
            output_encryption_kms_key_id: <p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your Call Analytics output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            settings: <p>Specify additional optional settings in your request, including content redaction; allows you to apply custom language models, vocabulary filters, and custom vocabularies to your Call Analytics job.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new call analytics job at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>
            channel_definitions: <p>Makes it possible to specify which speaker is on which channel. For example, if your agent is the first participant to speak, you would set <code>ChannelId</code> to <code>0</code> (to indicate the first channel) and <code>ParticipantRole</code> to <code>AGENT</code> (to indicate that it's the agent speaking).</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.start_call_analytics_job_request.StartCallAnalyticsJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.start_call_analytics_job_response.StartCallAnalyticsJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.start_call_analytics_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.start_call_analytics_job.async_start_call_analytics_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.start_call_analytics_job_request.StartCallAnalyticsJobRequest = {
            "call_analytics_job_name": call_analytics_job_name,
            "media": media,
        }
        if output_location is not None:
            input_["output_location"] = output_location
        if output_encryption_kms_key_id is not None:
            input_["output_encryption_kms_key_id"] = output_encryption_kms_key_id
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if settings is not None:
            input_["settings"] = settings
        if tags is not None:
            input_["tags"] = tags
        if channel_definitions is not None:
            input_["channel_definitions"] = channel_definitions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_medical_scribe_job(
        self,
        medical_scribe_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        media: "capo_transcribe.types.media.Media",
        output_bucket_name: "capo_transcribe.types.output_bucket_name.OutputBucketName",
        data_access_role_arn: "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn",
        settings: "capo_transcribe.types.medical_scribe_settings.MedicalScribeSettings",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        output_encryption_kms_key_id: Optional[
            "capo_transcribe.types.kms_key_id.KMSKeyId"
        ] = None,
        kms_encryption_context: Optional[
            "capo_transcribe.types.kms_encryption_context_map.KMSEncryptionContextMap"
        ] = None,
        channel_definitions: Optional[
            "capo_transcribe.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
        ] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
        medical_scribe_context: Optional[
            "capo_transcribe.types.medical_scribe_context.MedicalScribeContext"
        ] = None,
    ) -> "capo_transcribe.types.start_medical_scribe_job_response.StartMedicalScribeJobResponse":
        """<p>Transcribes patient-clinician conversations and generates clinical notes. </p> <p>Amazon Web Services HealthScribe automatically provides rich conversation transcripts, identifies speaker roles, classifies dialogues, extracts medical terms, and generates preliminary clinical notes. To learn more about these features, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe.html">Amazon Web Services HealthScribe</a>.</p> <p>To make a <code>StartMedicalScribeJob</code> request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the <code>Media</code> parameter.</p> <p>You must include the following parameters in your <code>StartMedicalTranscriptionJob</code> request:</p> <ul> <li> <p> <code>DataAccessRoleArn</code>: The ARN of an IAM role with the these minimum permissions: read permission on input file Amazon S3 bucket specified in <code>Media</code>, write permission on the Amazon S3 bucket specified in <code>OutputBucketName</code>, and full permissions on the KMS key specified in <code>OutputEncryptionKMSKeyId</code> (if set). The role should also allow <code>transcribe.amazonaws.com</code> to assume it. </p> </li> <li> <p> <code>Media</code> (<code>MediaFileUri</code>): The Amazon S3 location of your media file.</p> </li> <li> <p> <code>MedicalScribeJobName</code>: A custom name you create for your MedicalScribe job that is unique within your Amazon Web Services account.</p> </li> <li> <p> <code>OutputBucketName</code>: The Amazon S3 bucket where you want your output files stored.</p> </li> <li> <p> <code>Settings</code>: A <code>MedicalScribeSettings</code> object that must set exactly one of <code>ShowSpeakerLabels</code> or <code>ChannelIdentification</code> to true. If <code>ShowSpeakerLabels</code> is true, <code>MaxSpeakerLabels</code> must also be set. </p> </li> <li> <p> <code>ChannelDefinitions</code>: A <code>MedicalScribeChannelDefinitions</code> array should be set if and only if the <code>ChannelIdentification</code> value of <code>Settings</code> is set to true. </p> </li> </ul>

        Args:
            medical_scribe_job_name: <p>A unique name, chosen by you, for your Medical Scribe job.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>
            output_bucket_name: <p>The name of the Amazon S3 bucket where you want your Medical Scribe output stored. Do not include the <code>S3://</code> prefix of the specified bucket.</p> <p>Note that the role specified in the <code>DataAccessRoleArn</code> request parameter must have permission to use the specified location. You can change Amazon S3 permissions using the <a href="https://console.aws.amazon.com/s3">Amazon Web Services Management Console</a>. See also <a href="https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user">Permissions Required for IAM User Roles</a>.</p>
            output_encryption_kms_key_id: <p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your Medical Scribe output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>
            kms_encryption_context: <p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context">KMS encryption context</a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html">Asymmetric keys in KMS</a>.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            settings: <p>Makes it possible to control how your Medical Scribe job is processed using a <code>MedicalScribeSettings</code> object. Specify <code>ChannelIdentification</code> if <code>ChannelDefinitions</code> are set. Enabled <code>ShowSpeakerLabels</code> if <code>ChannelIdentification</code> and <code>ChannelDefinitions</code> are not set. One and only one of <code>ChannelIdentification</code> and <code>ShowSpeakerLabels</code> must be set. If <code>ShowSpeakerLabels</code> is set, <code>MaxSpeakerLabels</code> must also be set. Use <code>Settings</code> to specify a vocabulary or vocabulary filter or both using <code>VocabularyName</code>, <code>VocabularyFilterName</code>. <code>VocabularyFilterMethod</code> must be specified if <code>VocabularyFilterName</code> is set. </p>
            channel_definitions: <p>Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set <code>ChannelId</code> of the first <code>ChannelDefinition</code> in the list to <code>0</code> (to indicate the first channel) and <code>ParticipantRole</code> to <code>CLINICIAN</code> (to indicate that it's the clinician speaking). Then you would set the <code>ChannelId</code> of the second <code>ChannelDefinition</code> in the list to <code>1</code> (to indicate the second channel) and <code>ParticipantRole</code> to <code>PATIENT</code> (to indicate that it's the patient speaking). </p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to the Medical Scribe job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>
            medical_scribe_context: <p>The <code>MedicalScribeContext</code> object that contains contextual information which is used during clinical note generation to add relevant context to the note.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.start_medical_scribe_job_request.StartMedicalScribeJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.start_medical_scribe_job_response.StartMedicalScribeJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.start_medical_scribe_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.start_medical_scribe_job.async_start_medical_scribe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.start_medical_scribe_job_request.StartMedicalScribeJobRequest = {
            "medical_scribe_job_name": medical_scribe_job_name,
            "media": media,
            "output_bucket_name": output_bucket_name,
            "data_access_role_arn": data_access_role_arn,
            "settings": settings,
        }
        if output_encryption_kms_key_id is not None:
            input_["output_encryption_kms_key_id"] = output_encryption_kms_key_id
        if kms_encryption_context is not None:
            input_["kms_encryption_context"] = kms_encryption_context
        if channel_definitions is not None:
            input_["channel_definitions"] = channel_definitions
        if tags is not None:
            input_["tags"] = tags
        if medical_scribe_context is not None:
            input_["medical_scribe_context"] = medical_scribe_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_medical_transcription_job(
        self,
        medical_transcription_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        language_code: "capo_transcribe.types.language_code.LanguageCode",
        media: "capo_transcribe.types.media.Media",
        output_bucket_name: "capo_transcribe.types.output_bucket_name.OutputBucketName",
        specialty: "capo_transcribe.types.specialty.Specialty",
        type: "capo_transcribe.types.type.Type",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        media_sample_rate_hertz: Optional[
            "capo_transcribe.types.medical_media_sample_rate_hertz.MedicalMediaSampleRateHertz"
        ] = None,
        media_format: Optional["capo_transcribe.types.media_format.MediaFormat"] = None,
        output_key: Optional["capo_transcribe.types.output_key.OutputKey"] = None,
        output_encryption_kms_key_id: Optional[
            "capo_transcribe.types.kms_key_id.KMSKeyId"
        ] = None,
        kms_encryption_context: Optional[
            "capo_transcribe.types.kms_encryption_context_map.KMSEncryptionContextMap"
        ] = None,
        settings: Optional[
            "capo_transcribe.types.medical_transcription_setting.MedicalTranscriptionSetting"
        ] = None,
        content_identification_type: Optional[
            "capo_transcribe.types.medical_content_identification_type.MedicalContentIdentificationType"
        ] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
    ) -> "capo_transcribe.types.start_medical_transcription_job_response.StartMedicalTranscriptionJobResponse":
        """<p>Transcribes the audio from a medical dictation or conversation and applies any additional Request Parameters you choose to include in your request.</p> <p>In addition to many standard transcription features, Amazon Transcribe Medical provides you with a robust medical vocabulary and, optionally, content identification, which adds flags to personal health information (PHI). To learn more about these features, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works-med.html">How Amazon Transcribe Medical works</a>.</p> <p>To make a <code>StartMedicalTranscriptionJob</code> request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the <code>Media</code> parameter.</p> <p>You must include the following parameters in your <code>StartMedicalTranscriptionJob</code> request:</p> <ul> <li> <p> <code>region</code>: The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html">Amazon Transcribe endpoints and quotas</a>.</p> </li> <li> <p> <code>MedicalTranscriptionJobName</code>: A custom name you create for your transcription job that is unique within your Amazon Web Services account.</p> </li> <li> <p> <code>Media</code> (<code>MediaFileUri</code>): The Amazon S3 location of your media file.</p> </li> <li> <p> <code>LanguageCode</code>: This must be <code>en-US</code>.</p> </li> <li> <p> <code>OutputBucketName</code>: The Amazon S3 bucket where you want your transcript stored. If you want your output stored in a sub-folder of this bucket, you must also include <code>OutputKey</code>.</p> </li> <li> <p> <code>Specialty</code>: This must be <code>PRIMARYCARE</code>.</p> </li> <li> <p> <code>Type</code>: Choose whether your audio is a conversation or a dictation.</p> </li> </ul>

        Args:
            medical_transcription_job_name: <p>A unique name, chosen by you, for your medical transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the <code>OutputKey</code> parameter.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>
            language_code: <p>The language code that represents the language spoken in the input media file. US English (<code>en-US</code>) is the only valid value for medical transcription jobs. Any other value you enter for language code results in a <code>BadRequestException</code> error.</p>
            media_sample_rate_hertz: <p>The sample rate, in hertz, of the audio track in your input media file.</p> <p>If you do not specify the media sample rate, Amazon Transcribe Medical determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe Medical; if there's a mismatch between the value that you specify and the value detected, your job fails. Therefore, in most cases, it's advised to omit <code>MediaSampleRateHertz</code> and let Amazon Transcribe Medical determine the sample rate.</p>
            media_format: <p>Specify the format of your input media file.</p>
            output_bucket_name: <p>The name of the Amazon S3 bucket where you want your medical transcription output stored. Do not include the <code>S3://</code> prefix of the specified bucket.</p> <p>If you want your output to go to a sub-folder of this bucket, specify it using the <code>OutputKey</code> parameter; <code>OutputBucketName</code> only accepts the name of a bucket.</p> <p>For example, if you want your output stored in <code>S3://DOC-EXAMPLE-BUCKET</code>, set <code>OutputBucketName</code> to <code>DOC-EXAMPLE-BUCKET</code>. However, if you want your output stored in <code>S3://DOC-EXAMPLE-BUCKET/test-files/</code>, set <code>OutputBucketName</code> to <code>DOC-EXAMPLE-BUCKET</code> and <code>OutputKey</code> to <code>test-files/</code>.</p> <p>Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the <a href="https://console.aws.amazon.com/s3">Amazon Web Services Management Console</a>. See also <a href="https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user">Permissions Required for IAM User Roles</a>.</p>
            output_key: <p>Use in combination with <code>OutputBucketName</code> to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your medical transcription job (<code>MedicalTranscriptionJobName</code>).</p> <p>Here are some examples of how you can use <code>OutputKey</code>:</p> <ul> <li> <p>If you specify 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code> and 'my-transcript.json' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/my-transcript.json</code>.</p> </li> <li> <p>If you specify 'my-first-transcription' as the <code>MedicalTranscriptionJobName</code>, 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code>, and 'my-transcript' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json</code>.</p> </li> <li> <p>If you specify 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code> and 'test-files/my-transcript.json' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json</code>.</p> </li> <li> <p>If you specify 'my-first-transcription' as the <code>MedicalTranscriptionJobName</code>, 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code>, and 'test-files/my-transcript' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json</code>.</p> </li> </ul> <p>If you specify the name of an Amazon S3 bucket sub-folder that doesn't exist, one is created for you.</p>
            output_encryption_kms_key_id: <p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your medical transcription output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>
            kms_encryption_context: <p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context">KMS encryption context</a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html">Asymmetric keys in KMS</a>.</p>
            settings: <p>Specify additional optional settings in your request, including channel identification, alternative transcriptions, and speaker partitioning. You can use that to apply custom vocabularies to your transcription job.</p>
            content_identification_type: <p>Labels all personal health information (PHI) identified in your transcript. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html">Identifying personal health information (PHI) in a transcription</a>.</p>
            specialty: <p>Specify the predominant medical specialty represented in your media. For batch transcriptions, <code>PRIMARYCARE</code> is the only valid value. If you require additional specialties, refer to .</p>
            type: <p>Specify whether your input media contains only one person (<code>DICTATION</code>) or contains a conversation between two people (<code>CONVERSATION</code>).</p> <p>For example, <code>DICTATION</code> could be used for a medical professional wanting to transcribe voice memos; <code>CONVERSATION</code> could be used for transcribing the doctor-patient dialogue during the patient's office visit.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new medical transcription job at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.start_medical_transcription_job_request.StartMedicalTranscriptionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.start_medical_transcription_job_response.StartMedicalTranscriptionJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.start_medical_transcription_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.start_medical_transcription_job.async_start_medical_transcription_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.start_medical_transcription_job_request.StartMedicalTranscriptionJobRequest = {
            "medical_transcription_job_name": medical_transcription_job_name,
            "language_code": language_code,
            "media": media,
            "output_bucket_name": output_bucket_name,
            "specialty": specialty,
            "type": type,
        }
        if media_sample_rate_hertz is not None:
            input_["media_sample_rate_hertz"] = media_sample_rate_hertz
        if media_format is not None:
            input_["media_format"] = media_format
        if output_key is not None:
            input_["output_key"] = output_key
        if output_encryption_kms_key_id is not None:
            input_["output_encryption_kms_key_id"] = output_encryption_kms_key_id
        if kms_encryption_context is not None:
            input_["kms_encryption_context"] = kms_encryption_context
        if settings is not None:
            input_["settings"] = settings
        if content_identification_type is not None:
            input_["content_identification_type"] = content_identification_type
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_transcription_job(
        self,
        transcription_job_name: "capo_transcribe.types.transcription_job_name.TranscriptionJobName",
        media: "capo_transcribe.types.media.Media",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        language_code: Optional[
            "capo_transcribe.types.language_code.LanguageCode"
        ] = None,
        media_sample_rate_hertz: Optional[
            "capo_transcribe.types.media_sample_rate_hertz.MediaSampleRateHertz"
        ] = None,
        media_format: Optional["capo_transcribe.types.media_format.MediaFormat"] = None,
        output_bucket_name: Optional[
            "capo_transcribe.types.output_bucket_name.OutputBucketName"
        ] = None,
        output_key: Optional["capo_transcribe.types.output_key.OutputKey"] = None,
        output_encryption_kms_key_id: Optional[
            "capo_transcribe.types.kms_key_id.KMSKeyId"
        ] = None,
        kms_encryption_context: Optional[
            "capo_transcribe.types.kms_encryption_context_map.KMSEncryptionContextMap"
        ] = None,
        settings: Optional["capo_transcribe.types.settings.Settings"] = None,
        model_settings: Optional[
            "capo_transcribe.types.model_settings.ModelSettings"
        ] = None,
        job_execution_settings: Optional[
            "capo_transcribe.types.job_execution_settings.JobExecutionSettings"
        ] = None,
        content_redaction: Optional[
            "capo_transcribe.types.content_redaction.ContentRedaction"
        ] = None,
        identify_language: Optional["capo_transcribe.types.boolean.Boolean"] = None,
        identify_multiple_languages: Optional[
            "capo_transcribe.types.boolean.Boolean"
        ] = None,
        language_options: Optional[
            "capo_transcribe.types.language_options.LanguageOptions"
        ] = None,
        subtitles: Optional["capo_transcribe.types.subtitles.Subtitles"] = None,
        tags: Optional["capo_transcribe.types.tag_list.TagList"] = None,
        language_id_settings: Optional[
            "capo_transcribe.types.language_id_settings_map.LanguageIdSettingsMap"
        ] = None,
        toxicity_detection: Optional[
            "capo_transcribe.types.toxicity_detection.ToxicityDetection"
        ] = None,
    ) -> "capo_transcribe.types.start_transcription_job_response.StartTranscriptionJobResponse":
        """<p>Transcribes the audio from a media file and applies any additional Request Parameters you choose to include in your request.</p> <p>To make a <code>StartTranscriptionJob</code> request, you must first upload your media file into an Amazon S3 bucket; you can then specify the Amazon S3 location of the file using the <code>Media</code> parameter.</p> <p>You must include the following parameters in your <code>StartTranscriptionJob</code> request:</p> <ul> <li> <p> <code>region</code>: The Amazon Web Services Region where you are making your request. For a list of Amazon Web Services Regions supported with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html">Amazon Transcribe endpoints and quotas</a>.</p> </li> <li> <p> <code>TranscriptionJobName</code>: A custom name you create for your transcription job that is unique within your Amazon Web Services account.</p> </li> <li> <p> <code>Media</code> (<code>MediaFileUri</code>): The Amazon S3 location of your media file.</p> </li> <li> <p>One of <code>LanguageCode</code>, <code>IdentifyLanguage</code>, or <code>IdentifyMultipleLanguages</code>: If you know the language of your media file, specify it using the <code>LanguageCode</code> parameter; you can find all valid language codes in the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table. If you do not know the languages spoken in your media, use either <code>IdentifyLanguage</code> or <code>IdentifyMultipleLanguages</code> and let Amazon Transcribe identify the languages for you.</p> </li> </ul>

        Args:
            transcription_job_name: <p>A unique name, chosen by you, for your transcription job. The name that you specify is also used as the default name of your transcription output file. If you want to specify a different name for your transcription output, use the <code>OutputKey</code> parameter.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>
            language_code: <p>The language code that represents the language spoken in the input media file.</p> <p>If you're unsure of the language spoken in your media file, consider using <code>IdentifyLanguage</code> or <code>IdentifyMultipleLanguages</code> to enable automatic language identification.</p> <p>Note that you must include one of <code>LanguageCode</code>, <code>IdentifyLanguage</code>, or <code>IdentifyMultipleLanguages</code> in your request. If you include more than one of these parameters, your transcription job fails.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p> <note> <p>To transcribe speech in Modern Standard Arabic (<code>ar-SA</code>) in Amazon Web Services GovCloud (US) (US-West, us-gov-west-1), Amazon Web Services GovCloud (US) (US-East, us-gov-east-1), Canada (Calgary, ca-west-1) and Africa (Cape Town, af-south-1), your media file must be encoded at a sample rate of 16,000 Hz or higher.</p> </note>
            media_sample_rate_hertz: <p>The sample rate, in hertz, of the audio track in your input media file.</p> <p>If you do not specify the media sample rate, Amazon Transcribe determines it for you. If you specify the sample rate, it must match the rate detected by Amazon Transcribe. If there's a mismatch between the value that you specify and the value detected, your job fails. In most cases, you can omit <code>MediaSampleRateHertz</code> and let Amazon Transcribe determine the sample rate.</p>
            media_format: <p>Specify the format of your input media file.</p>
            media: <p>Describes the Amazon S3 location of the media file you want to use in your request.</p>
            output_bucket_name: <p>The name of the Amazon S3 bucket where you want your transcription output stored. Do not include the <code>S3://</code> prefix of the specified bucket.</p> <p>If you want your output to go to a sub-folder of this bucket, specify it using the <code>OutputKey</code> parameter; <code>OutputBucketName</code> only accepts the name of a bucket.</p> <p>For example, if you want your output stored in <code>S3://DOC-EXAMPLE-BUCKET</code>, set <code>OutputBucketName</code> to <code>DOC-EXAMPLE-BUCKET</code>. However, if you want your output stored in <code>S3://DOC-EXAMPLE-BUCKET/test-files/</code>, set <code>OutputBucketName</code> to <code>DOC-EXAMPLE-BUCKET</code> and <code>OutputKey</code> to <code>test-files/</code>.</p> <p>Note that Amazon Transcribe must have permission to use the specified location. You can change Amazon S3 permissions using the <a href="https://console.aws.amazon.com/s3">Amazon Web Services Management Console</a>. See also <a href="https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user">Permissions Required for IAM User Roles</a>.</p> <p>If you do not specify <code>OutputBucketName</code>, your transcript is placed in a service-managed Amazon S3 bucket and you are provided with a URI to access your transcript.</p>
            output_key: <p>Use in combination with <code>OutputBucketName</code> to specify the output location of your transcript and, optionally, a unique name for your output file. The default name for your transcription output is the same as the name you specified for your transcription job (<code>TranscriptionJobName</code>).</p> <p>Here are some examples of how you can use <code>OutputKey</code>:</p> <ul> <li> <p>If you specify 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code> and 'my-transcript.json' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/my-transcript.json</code>.</p> </li> <li> <p>If you specify 'my-first-transcription' as the <code>TranscriptionJobName</code>, 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code>, and 'my-transcript' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/my-transcript/my-first-transcription.json</code>.</p> </li> <li> <p>If you specify 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code> and 'test-files/my-transcript.json' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript.json</code>.</p> </li> <li> <p>If you specify 'my-first-transcription' as the <code>TranscriptionJobName</code>, 'DOC-EXAMPLE-BUCKET' as the <code>OutputBucketName</code>, and 'test-files/my-transcript' as the <code>OutputKey</code>, your transcription output path is <code>s3://DOC-EXAMPLE-BUCKET/test-files/my-transcript/my-first-transcription.json</code>.</p> </li> </ul> <p>If you specify the name of an Amazon S3 bucket sub-folder that doesn't exist, one is created for you.</p>
            output_encryption_kms_key_id: <p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your transcription output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>
            kms_encryption_context: <p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context">KMS encryption context</a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html">Asymmetric keys in KMS</a>.</p>
            settings: <p>Specify additional optional settings in your request, including channel identification, alternative transcriptions, speaker partitioning. You can use that to apply custom vocabularies and vocabulary filters.</p> <p>If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but <b>do not</b> want to use automatic language identification, use <code>Settings</code> with the <code>VocabularyName</code> or <code>VocabularyFilterName</code> (or both) sub-parameter.</p> <p>If you're using automatic language identification with your request and want to include a custom language model, a custom vocabulary, or a custom vocabulary filter, use instead the <code></code> parameter with the <code>LanguageModelName</code>, <code>VocabularyName</code> or <code>VocabularyFilterName</code> sub-parameters.</p>
            model_settings: <p>Specify the custom language model you want to include with your transcription job. If you include <code>ModelSettings</code> in your request, you must include the <code>LanguageModelName</code> sub-parameter.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html">Custom language models</a>.</p>
            job_execution_settings: <p>Makes it possible to control how your transcription job is processed. Currently, the only <code>JobExecutionSettings</code> modification you can choose is enabling job queueing using the <code>AllowDeferredExecution</code> sub-parameter.</p> <p>If you include <code>JobExecutionSettings</code> in your request, you must also include the sub-parameters: <code>AllowDeferredExecution</code> and <code>DataAccessRoleArn</code>.</p>
            content_redaction: <p>Makes it possible to redact or flag specified personally identifiable information (PII) in your transcript. If you use <code>ContentRedaction</code>, you must also include the sub-parameters: <code>RedactionOutput</code> and <code>RedactionType</code>. You can optionally include <code>PiiEntityTypes</code> to choose which types of PII you want to redact. If you do not include <code>PiiEntityTypes</code> in your request, all PII is redacted.</p>
            identify_language: <p>Enables automatic language identification in your transcription job request. Use this parameter if your media file contains only one language. If your media contains multiple languages, use <code>IdentifyMultipleLanguages</code> instead.</p> <p>If you include <code>IdentifyLanguage</code>, you can optionally include a list of language codes, using <code>LanguageOptions</code>, that you think may be present in your media file. Including <code>LanguageOptions</code> restricts <code>IdentifyLanguage</code> to only the language options that you specify, which can improve transcription accuracy.</p> <p>If you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter to your automatic language identification request, include <code>LanguageIdSettings</code> with the relevant sub-parameters (<code>VocabularyName</code>, <code>LanguageModelName</code>, and <code>VocabularyFilterName</code>). If you include <code>LanguageIdSettings</code>, also include <code>LanguageOptions</code>.</p> <p>Note that you must include one of <code>LanguageCode</code>, <code>IdentifyLanguage</code>, or <code>IdentifyMultipleLanguages</code> in your request. If you include more than one of these parameters, your transcription job fails.</p>
            identify_multiple_languages: <p>Enables automatic multi-language identification in your transcription job request. Use this parameter if your media file contains more than one language. If your media contains only one language, use <code>IdentifyLanguage</code> instead.</p> <p>If you include <code>IdentifyMultipleLanguages</code>, you can optionally include a list of language codes, using <code>LanguageOptions</code>, that you think may be present in your media file. Including <code>LanguageOptions</code> restricts <code>IdentifyLanguage</code> to only the language options that you specify, which can improve transcription accuracy.</p> <p>If you want to apply a custom vocabulary or a custom vocabulary filter to your automatic language identification request, include <code>LanguageIdSettings</code> with the relevant sub-parameters (<code>VocabularyName</code> and <code>VocabularyFilterName</code>). If you include <code>LanguageIdSettings</code>, also include <code>LanguageOptions</code>.</p> <p>Note that you must include one of <code>LanguageCode</code>, <code>IdentifyLanguage</code>, or <code>IdentifyMultipleLanguages</code> in your request. If you include more than one of these parameters, your transcription job fails.</p>
            language_options: <p>You can specify two or more language codes that represent the languages you think may be present in your media. Including more than five is not recommended. If you're unsure what languages are present, do not include this parameter.</p> <p>If you include <code>LanguageOptions</code> in your request, you must also include <code>IdentifyLanguage</code>.</p> <p>For more information, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a>.</p> <p>To transcribe speech in Modern Standard Arabic (<code>ar-SA</code>)in Amazon Web Services GovCloud (US) (US-West, us-gov-west-1), Amazon Web Services GovCloud (US) (US-East, us-gov-east-1), in Canada (Calgary) ca-west-1 and Africa (Cape Town) af-south-1, your media file must be encoded at a sample rate of 16,000 Hz or higher.</p>
            subtitles: <p>Produces subtitle files for your input media. You can specify WebVTT (*.vtt) and SubRip (*.srt) formats.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to a new transcription job at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>
            language_id_settings: <p>If using automatic language identification in your request and you want to apply a custom language model, a custom vocabulary, or a custom vocabulary filter, include <code>LanguageIdSettings</code> with the relevant sub-parameters (<code>VocabularyName</code>, <code>LanguageModelName</code>, and <code>VocabularyFilterName</code>). Note that multi-language identification (<code>IdentifyMultipleLanguages</code>) doesn't support custom language models.</p> <p> <code>LanguageIdSettings</code> supports two to five language codes. Each language code you include can have an associated custom language model, custom vocabulary, and custom vocabulary filter. The language codes that you specify must match the languages of the associated custom language models, custom vocabularies, and custom vocabulary filters.</p> <p>It's recommended that you include <code>LanguageOptions</code> when using <code>LanguageIdSettings</code> to ensure that the correct language dialect is identified. For example, if you specify a custom vocabulary that is in <code>en-US</code> but Amazon Transcribe determines that the language spoken in your media is <code>en-AU</code>, your custom vocabulary <i>is not</i> applied to your transcription. If you include <code>LanguageOptions</code> and include <code>en-US</code> as the only English language dialect, your custom vocabulary <i>is</i> applied to your transcription.</p> <p>If you want to include a custom language model with your request but <b>do not</b> want to use automatic language identification, use instead the <code></code> parameter with the <code>LanguageModelName</code> sub-parameter. If you want to include a custom vocabulary or a custom vocabulary filter (or both) with your request but <b>do not</b> want to use automatic language identification, use instead the <code></code> parameter with the <code>VocabularyName</code> or <code>VocabularyFilterName</code> (or both) sub-parameter.</p>
            toxicity_detection: <p>Enables toxic speech detection in your transcript. If you include <code>ToxicityDetection</code> in your request, you must also include <code>ToxicityCategories</code>.</p> <p>For information on the types of toxic speech Amazon Transcribe can detect, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/toxic-language.html">Detecting toxic speech</a>.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.start_transcription_job_request.StartTranscriptionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.start_transcription_job_response.StartTranscriptionJobResponse"
        ]:
            import capo_transcribe._operations.transcribe.start_transcription_job

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.start_transcription_job.async_start_transcription_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.start_transcription_job_request.StartTranscriptionJobRequest = {
            "transcription_job_name": transcription_job_name,
            "media": media,
        }
        if language_code is not None:
            input_["language_code"] = language_code
        if media_sample_rate_hertz is not None:
            input_["media_sample_rate_hertz"] = media_sample_rate_hertz
        if media_format is not None:
            input_["media_format"] = media_format
        if output_bucket_name is not None:
            input_["output_bucket_name"] = output_bucket_name
        if output_key is not None:
            input_["output_key"] = output_key
        if output_encryption_kms_key_id is not None:
            input_["output_encryption_kms_key_id"] = output_encryption_kms_key_id
        if kms_encryption_context is not None:
            input_["kms_encryption_context"] = kms_encryption_context
        if settings is not None:
            input_["settings"] = settings
        if model_settings is not None:
            input_["model_settings"] = model_settings
        if job_execution_settings is not None:
            input_["job_execution_settings"] = job_execution_settings
        if content_redaction is not None:
            input_["content_redaction"] = content_redaction
        if identify_language is not None:
            input_["identify_language"] = identify_language
        if identify_multiple_languages is not None:
            input_["identify_multiple_languages"] = identify_multiple_languages
        if language_options is not None:
            input_["language_options"] = language_options
        if subtitles is not None:
            input_["subtitles"] = subtitles
        if tags is not None:
            input_["tags"] = tags
        if language_id_settings is not None:
            input_["language_id_settings"] = language_id_settings
        if toxicity_detection is not None:
            input_["toxicity_detection"] = toxicity_detection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_transcribe.types.transcribe_arn.TranscribeArn",
        tags: "capo_transcribe.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.tag_resource_response.TagResourceResponse":
        """<p>Adds one or more custom tags, each in the form of a key:value pair, to the specified resource.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to tag. ARNs have the format <code>arn:partition:service:region:account-id:resource-type/resource-id</code>.</p> <p>For example, <code>arn:aws:transcribe:us-west-2:111122223333:transcription-job/transcription-job-name</code>.</p> <p>Valid values for <code>resource-type</code> are: <code>transcription-job</code>, <code>medical-transcription-job</code>, <code>vocabulary</code>, <code>medical-vocabulary</code>, <code>vocabulary-filter</code>, and <code>language-model</code>.</p>
            tags: <p>Adds one or more custom tags, each in the form of a key:value pair, to the specified resource.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_transcribe._operations.transcribe.tag_resource

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_transcribe.types.transcribe_arn.TranscribeArn",
        tag_keys: "capo_transcribe.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified Amazon Transcribe resource.</p> <p>If you include <code>UntagResource</code> in your request, you must also include <code>ResourceArn</code> and <code>TagKeys</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Transcribe resource you want to remove tags from. ARNs have the format <code>arn:partition:service:region:account-id:resource-type/resource-id</code>.</p> <p>For example, <code>arn:aws:transcribe:us-west-2:111122223333:transcription-job/transcription-job-name</code>.</p> <p>Valid values for <code>resource-type</code> are: <code>transcription-job</code>, <code>medical-transcription-job</code>, <code>vocabulary</code>, <code>medical-vocabulary</code>, <code>vocabulary-filter</code>, and <code>language-model</code>.</p>
            tag_keys: <p>Removes the specified tag keys from the specified Amazon Transcribe resource.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_transcribe._operations.transcribe.untag_resource

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_call_analytics_category(
        self,
        category_name: "capo_transcribe.types.category_name.CategoryName",
        rules: "capo_transcribe.types.rule_list.RuleList",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        input_type: Optional["capo_transcribe.types.input_type.InputType"] = None,
    ) -> "capo_transcribe.types.update_call_analytics_category_response.UpdateCallAnalyticsCategoryResponse":
        """<p>Updates the specified Call Analytics category with new rules. Note that the <code>UpdateCallAnalyticsCategory</code> operation overwrites all existing rules contained in the specified category. You cannot append additional rules onto an existing category.</p> <p>To create a new category, see .</p>

        Args:
            category_name: <p>The name of the Call Analytics category you want to update. Category names are case sensitive.</p>
            rules: <p>The rules used for the updated Call Analytics category. The rules you provide in this field replace the ones that are currently being used in the specified category.</p>
            input_type: <p>Choose whether you want to update a real-time or a post-call category. The input type you specify must match the input type specified when the category was created. For example, if you created a category with the <code>POST_CALL</code> input type, you must use <code>POST_CALL</code> as the input type when updating this category.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.update_call_analytics_category_request.UpdateCallAnalyticsCategoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.update_call_analytics_category_response.UpdateCallAnalyticsCategoryResponse"
        ]:
            import capo_transcribe._operations.transcribe.update_call_analytics_category

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.update_call_analytics_category.async_update_call_analytics_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.update_call_analytics_category_request.UpdateCallAnalyticsCategoryRequest = {
            "category_name": category_name,
            "rules": rules,
        }
        if input_type is not None:
            input_["input_type"] = input_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_language_model(
        self,
        model_name: "capo_transcribe.types.model_name.ModelName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        data_access_role_arn: Optional[
            "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
        ] = None,
        encryption_configuration: Optional[
            "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_transcribe.types.update_language_model_response.UpdateLanguageModelResponse":
        """<p>Updates the encryption configuration for an existing custom language model. You can use this operation to change the KMS key used to encrypt your model artifacts. The model artifacts are re-encrypted in place. No model training is required.</p> <p>Your custom language model must not be in the <code>IN_PROGRESS</code> state when you call this operation. You cannot submit another update while a previous update is in progress. Use to check the current state of your model.</p> <p>Your custom language model remains available for transcription jobs while the update is being processed.</p>

        Args:
            model_name: <p>The name of the custom language model you want to update. Model names are case sensitive.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role. If you include <code>EncryptionConfiguration</code> in your request, this role must have permissions to access the specified KMS key. If the role that you specify doesn't have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            encryption_configuration: <p>Specifies the new encryption configuration for your custom language model. The model artifacts are re-encrypted in place using the specified KMS key or with an AWS-owned key if a key is not supplied.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.update_language_model_request.UpdateLanguageModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.update_language_model_response.UpdateLanguageModelResponse"
        ]:
            import capo_transcribe._operations.transcribe.update_language_model

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.update_language_model.async_update_language_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.update_language_model_request.UpdateLanguageModelRequest = {
            "model_name": model_name
        }
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_medical_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        language_code: "capo_transcribe.types.language_code.LanguageCode",
        vocabulary_file_uri: "capo_transcribe.types.uri.Uri",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
    ) -> "capo_transcribe.types.update_medical_vocabulary_response.UpdateMedicalVocabularyResponse":
        """<p>Updates an existing custom medical vocabulary with new values. This operation overwrites all existing information with your new values; you cannot append new terms onto an existing custom vocabulary.</p>

        Args:
            vocabulary_name: <p>The name of the custom medical vocabulary you want to update. Custom medical vocabulary names are case sensitive.</p>
            language_code: <p>The language code that represents the language of the entries in the custom vocabulary you want to update. US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>
            vocabulary_file_uri: <p>The Amazon S3 location of the text file that contains your custom medical vocabulary. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.update_medical_vocabulary_request.UpdateMedicalVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.update_medical_vocabulary_response.UpdateMedicalVocabularyResponse"
        ]:
            import capo_transcribe._operations.transcribe.update_medical_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.update_medical_vocabulary.async_update_medical_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.update_medical_vocabulary_request.UpdateMedicalVocabularyRequest = {
            "vocabulary_name": vocabulary_name,
            "language_code": language_code,
            "vocabulary_file_uri": vocabulary_file_uri,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_vocabulary(
        self,
        vocabulary_name: "capo_transcribe.types.vocabulary_name.VocabularyName",
        language_code: "capo_transcribe.types.language_code.LanguageCode",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        phrases: Optional["capo_transcribe.types.phrases.Phrases"] = None,
        vocabulary_file_uri: Optional["capo_transcribe.types.uri.Uri"] = None,
        data_access_role_arn: Optional[
            "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
        ] = None,
        encryption_configuration: Optional[
            "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_transcribe.types.update_vocabulary_response.UpdateVocabularyResponse":
        """<p>Updates an existing custom vocabulary with new values. This operation overwrites all existing information with your new values; you cannot append new terms onto an existing custom vocabulary.</p> <p>Your custom vocabulary must be in a terminal state (<code>READY</code> or <code>FAILED</code>) before you can update it. You must include either <code>Phrases</code> or <code>VocabularyFileUri</code> in your request.</p>

        Args:
            vocabulary_name: <p>The name of the custom vocabulary you want to update. Custom vocabulary names are case sensitive.</p>
            language_code: <p>The language code that represents the language of the entries in the custom vocabulary you want to update. Each custom vocabulary must contain terms in only one language.</p> <p>A custom vocabulary can only be used to transcribe files in the same language as the custom vocabulary. For example, if you create a custom vocabulary using US English (<code>en-US</code>), you can only apply this custom vocabulary to files that contain English audio.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href="https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html">Supported languages</a> table.</p>
            phrases: <p>Use this parameter if you want to update your custom vocabulary by including all desired terms, as comma-separated values, within your request. The other option for updating your custom vocabulary is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFileUri</code> parameter.</p> <p>Note that if you include <code>Phrases</code> in your request, you cannot use <code>VocabularyFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>
            vocabulary_file_uri: <p>The Amazon S3 location of the text file that contains your custom vocabulary. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-file.txt</code> </p> <p>Note that if you include <code>VocabularyFileUri</code> in your request, you cannot use the <code>Phrases</code> flag; you must choose one or the other.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary). If you include <code>EncryptionConfiguration</code> in your request, this role must also have permissions to access the specified KMS key. If the role that you specify doesn’t have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            encryption_configuration: <p>Specifies the new encryption configuration for your custom vocabulary. The vocabulary artifacts are re-encrypted in place using the specified KMS key or with an AWS-owned key if a key is not supplied.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.update_vocabulary_request.UpdateVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.update_vocabulary_response.UpdateVocabularyResponse"
        ]:
            import capo_transcribe._operations.transcribe.update_vocabulary

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.update_vocabulary.async_update_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.update_vocabulary_request.UpdateVocabularyRequest = {
            "vocabulary_name": vocabulary_name,
            "language_code": language_code,
        }
        if phrases is not None:
            input_["phrases"] = phrases
        if vocabulary_file_uri is not None:
            input_["vocabulary_file_uri"] = vocabulary_file_uri
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_vocabulary_filter(
        self,
        vocabulary_filter_name: "capo_transcribe.types.vocabulary_filter_name.VocabularyFilterName",
        *,
        config_overrides: Optional[AsyncTranscribeClientConfig] = None,
        words: Optional["capo_transcribe.types.words.Words"] = None,
        vocabulary_filter_file_uri: Optional["capo_transcribe.types.uri.Uri"] = None,
        data_access_role_arn: Optional[
            "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
        ] = None,
        encryption_configuration: Optional[
            "capo_transcribe.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
    ) -> "capo_transcribe.types.update_vocabulary_filter_response.UpdateVocabularyFilterResponse":
        """<p>Updates an existing custom vocabulary filter with a new list of words. The new list you provide overwrites all previous entries; you cannot append new terms onto an existing custom vocabulary filter.</p> <p>You must include either <code>Words</code> or <code>VocabularyFilterFileUri</code> in your request.</p>

        Args:
            vocabulary_filter_name: <p>The name of the custom vocabulary filter you want to update. Custom vocabulary filter names are case sensitive.</p>
            words: <p>Use this parameter if you want to update your custom vocabulary filter by including all desired terms, as comma-separated values, within your request. The other option for updating your vocabulary filter is to save your entries in a text file and upload them to an Amazon S3 bucket, then specify the location of your file using the <code>VocabularyFilterFileUri</code> parameter.</p> <p>Note that if you include <code>Words</code> in your request, you cannot use <code>VocabularyFilterFileUri</code>; you must choose one or the other.</p> <p>Each language has a character set that contains all allowed characters for that specific language. If you use unsupported characters, your custom vocabulary filter request fails. Refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/charsets.html">Character Sets for Custom Vocabularies</a> to get the character set for your language.</p>
            vocabulary_filter_file_uri: <p>The Amazon S3 location of the text file that contains your custom vocabulary filter terms. The URI must be located in the same Amazon Web Services Region as the resource you're calling.</p> <p>Here's an example URI path: <code>s3://DOC-EXAMPLE-BUCKET/my-vocab-filter-file.txt</code> </p> <p>Note that if you include <code>VocabularyFilterFileUri</code> in your request, you cannot use <code>Words</code>; you must choose one or the other.</p>
            data_access_role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files (in this case, your custom vocabulary filter). If you include <code>EncryptionConfiguration</code> in your request, this role must also have permissions to access the specified KMS key. If the role that you specify doesn’t have the appropriate permissions, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>
            encryption_configuration: <p>Specifies the new encryption configuration for your custom vocabulary filter. The vocabulary filter artifacts are re-encrypted in place using the specified KMS key or with an AWS-owned key if a key is not supplied.</p>

        Raises:
            capo_transcribe.errors.bad_request_exception.BadRequestException: <p>Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as <code>IN PROGRESS</code>). See the exception message field for more information.</p>
            capo_transcribe.errors.conflict_exception.ConflictException: <p>A resource already exists with this name. Resource names must be unique within an Amazon Web Services account.</p>
            capo_transcribe.errors.internal_failure_exception.InternalFailureException: <p>There was an internal error. Check the error message, correct the issue, and try your request again.</p>
            capo_transcribe.errors.limit_exceeded_exception.LimitExceededException: <p>You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.</p>
            capo_transcribe.errors.not_found_exception.NotFoundException: <p>We can't find the requested resource. Check that the specified name is correct and try your request again.</p>
            capo_transcribe.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transcribe.types.update_vocabulary_filter_request.UpdateVocabularyFilterRequest]",
        ) -> AsyncOperationResponse[
            "capo_transcribe.types.update_vocabulary_filter_response.UpdateVocabularyFilterResponse"
        ]:
            import capo_transcribe._operations.transcribe.update_vocabulary_filter

            (
                output,
                http_response,
            ) = await capo_transcribe._operations.transcribe.update_vocabulary_filter.async_update_vocabulary_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_transcribe.types.update_vocabulary_filter_request.UpdateVocabularyFilterRequest = {
            "vocabulary_filter_name": vocabulary_filter_name
        }
        if words is not None:
            input_["words"] = words
        if vocabulary_filter_file_uri is not None:
            input_["vocabulary_filter_file_uri"] = vocabulary_filter_file_uri
        if data_access_role_arn is not None:
            input_["data_access_role_arn"] = data_access_role_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration

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
