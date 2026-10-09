"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ChimeSDKMediaPipelinesService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_chime_sdk_media_pipelines._auth._signers
import capo_chime_sdk_media_pipelines._auth._sigv4
from capo_chime_sdk_media_pipelines._auth._identity import Credentials
from capo_chime_sdk_media_pipelines._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_chime_sdk_media_pipelines._auth._zapros_handler import AuthMiddleware
from capo_chime_sdk_media_pipelines._pagination import resolve_path as _resolve_path
from capo_chime_sdk_media_pipelines._services._aws_config import aaws_config
from capo_chime_sdk_media_pipelines._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_resource_name
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.concatenation_sink_list
    import capo_chime_sdk_media_pipelines.types.concatenation_source_list
    import capo_chime_sdk_media_pipelines.types.create_media_capture_pipeline_request
    import capo_chime_sdk_media_pipelines.types.create_media_capture_pipeline_response
    import capo_chime_sdk_media_pipelines.types.create_media_concatenation_pipeline_request
    import capo_chime_sdk_media_pipelines.types.create_media_concatenation_pipeline_response
    import capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_configuration_request
    import capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_configuration_response
    import capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_request
    import capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_response
    import capo_chime_sdk_media_pipelines.types.create_media_live_connector_pipeline_request
    import capo_chime_sdk_media_pipelines.types.create_media_live_connector_pipeline_response
    import capo_chime_sdk_media_pipelines.types.create_media_pipeline_kinesis_video_stream_pool_request
    import capo_chime_sdk_media_pipelines.types.create_media_pipeline_kinesis_video_stream_pool_response
    import capo_chime_sdk_media_pipelines.types.create_media_stream_pipeline_request
    import capo_chime_sdk_media_pipelines.types.create_media_stream_pipeline_response
    import capo_chime_sdk_media_pipelines.types.delete_media_capture_pipeline_request
    import capo_chime_sdk_media_pipelines.types.delete_media_insights_pipeline_configuration_request
    import capo_chime_sdk_media_pipelines.types.delete_media_pipeline_kinesis_video_stream_pool_request
    import capo_chime_sdk_media_pipelines.types.delete_media_pipeline_request
    import capo_chime_sdk_media_pipelines.types.get_media_capture_pipeline_request
    import capo_chime_sdk_media_pipelines.types.get_media_capture_pipeline_response
    import capo_chime_sdk_media_pipelines.types.get_media_insights_pipeline_configuration_request
    import capo_chime_sdk_media_pipelines.types.get_media_insights_pipeline_configuration_response
    import capo_chime_sdk_media_pipelines.types.get_media_pipeline_kinesis_video_stream_pool_request
    import capo_chime_sdk_media_pipelines.types.get_media_pipeline_kinesis_video_stream_pool_response
    import capo_chime_sdk_media_pipelines.types.get_media_pipeline_request
    import capo_chime_sdk_media_pipelines.types.get_media_pipeline_response
    import capo_chime_sdk_media_pipelines.types.get_speaker_search_task_request
    import capo_chime_sdk_media_pipelines.types.get_speaker_search_task_response
    import capo_chime_sdk_media_pipelines.types.get_voice_tone_analysis_task_request
    import capo_chime_sdk_media_pipelines.types.get_voice_tone_analysis_task_response
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration
    import capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_request
    import capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_response
    import capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_request
    import capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_response
    import capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_request
    import capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_response
    import capo_chime_sdk_media_pipelines.types.list_media_pipelines_request
    import capo_chime_sdk_media_pipelines.types.list_media_pipelines_response
    import capo_chime_sdk_media_pipelines.types.list_tags_for_resource_request
    import capo_chime_sdk_media_pipelines.types.list_tags_for_resource_response
    import capo_chime_sdk_media_pipelines.types.live_connector_sink_list
    import capo_chime_sdk_media_pipelines.types.live_connector_source_list
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string
    import capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata
    import capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type
    import capo_chime_sdk_media_pipelines.types.media_pipeline_source_type
    import capo_chime_sdk_media_pipelines.types.media_pipeline_status_update
    import capo_chime_sdk_media_pipelines.types.media_stream_sink_list
    import capo_chime_sdk_media_pipelines.types.media_stream_source_list
    import capo_chime_sdk_media_pipelines.types.non_empty_string
    import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration
    import capo_chime_sdk_media_pipelines.types.result_max
    import capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration
    import capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params
    import capo_chime_sdk_media_pipelines.types.start_speaker_search_task_request
    import capo_chime_sdk_media_pipelines.types.start_speaker_search_task_response
    import capo_chime_sdk_media_pipelines.types.start_voice_tone_analysis_task_request
    import capo_chime_sdk_media_pipelines.types.start_voice_tone_analysis_task_response
    import capo_chime_sdk_media_pipelines.types.stop_speaker_search_task_request
    import capo_chime_sdk_media_pipelines.types.stop_voice_tone_analysis_task_request
    import capo_chime_sdk_media_pipelines.types.string
    import capo_chime_sdk_media_pipelines.types.tag_key_list
    import capo_chime_sdk_media_pipelines.types.tag_list
    import capo_chime_sdk_media_pipelines.types.tag_resource_request
    import capo_chime_sdk_media_pipelines.types.tag_resource_response
    import capo_chime_sdk_media_pipelines.types.untag_resource_request
    import capo_chime_sdk_media_pipelines.types.untag_resource_response
    import capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_configuration_request
    import capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_configuration_response
    import capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request
    import capo_chime_sdk_media_pipelines.types.update_media_pipeline_kinesis_video_stream_pool_request
    import capo_chime_sdk_media_pipelines.types.update_media_pipeline_kinesis_video_stream_pool_response
    import capo_chime_sdk_media_pipelines.types.voice_analytics_language_code


class AsyncChimeSDKMediaPipelinesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncChimeSDKMediaPipelinesClient:
    """A client for the ``ChimeSDKMediaPipelines`` service.

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
        self._config = AsyncChimeSDKMediaPipelinesClientConfig(
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
        self, config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncChimeSDKMediaPipelinesClientConfig = config_overrides or {}
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

    async def create_media_capture_pipeline(
        self,
        source_type: "capo_chime_sdk_media_pipelines.types.media_pipeline_source_type.MediaPipelineSourceType",
        source_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn",
        sink_type: "capo_chime_sdk_media_pipelines.types.media_pipeline_sink_type.MediaPipelineSinkType",
        sink_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
        chime_sdk_meeting_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_configuration.ChimeSdkMeetingConfiguration"
        ] = None,
        sse_aws_key_management_params: Optional[
            "capo_chime_sdk_media_pipelines.types.sse_aws_key_management_params.SseAwsKeyManagementParams"
        ] = None,
        sink_iam_role_arn: Optional[
            "capo_chime_sdk_media_pipelines.types.arn.Arn"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_capture_pipeline_response.CreateMediaCapturePipelineResponse":
        """<p>Creates a media pipeline.</p>

        Args:
            source_type: <p>Source type from which the media artifacts are captured. A Chime SDK Meeting is the only supported source.</p>
            source_arn: <p>ARN of the source from which the media artifacts are captured.</p>
            sink_type: <p>Destination type to which the media artifacts are saved. You must use an S3 bucket.</p>
            sink_arn: <p>The ARN of the sink type.</p>
            client_request_token: <p>The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media pipeline request.</p>
            chime_sdk_meeting_configuration: <p>The configuration for a specified media pipeline. <code>SourceType</code> must be <code>ChimeSdkMeeting</code>.</p>
            sse_aws_key_management_params: <p>An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.</p>
            sink_iam_role_arn: <p>The Amazon Resource Name (ARN) of the sink role to be used with <code>AwsKmsKeyId</code> in <code>SseAwsKeyManagementParams</code>. Can only interact with <code>S3Bucket</code> sink type. The role must belong to the caller’s account and be able to act on behalf of the caller during the API call. All minimum policy permissions requirements for the caller to perform sink-related actions are the same for <code>SinkIamRoleArn</code>.</p> <p>Additionally, the role must have permission to <code>kms:GenerateDataKey</code> using KMS key supplied as <code>AwsKmsKeyId</code> in <code>SseAwsKeyManagementParams</code>. If media concatenation will be required later, the role must also have permission to <code>kms:Decrypt</code> for the same KMS key.</p>
            tags: <p>The tag key-value pairs.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_capture_pipeline_request.CreateMediaCapturePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_capture_pipeline_response.CreateMediaCapturePipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_capture_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_capture_pipeline.async_create_media_capture_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_capture_pipeline_request.CreateMediaCapturePipelineRequest = {
            "source_type": source_type,
            "source_arn": source_arn,
            "sink_type": sink_type,
            "sink_arn": sink_arn,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if chime_sdk_meeting_configuration is not None:
            input_["chime_sdk_meeting_configuration"] = chime_sdk_meeting_configuration
        if sse_aws_key_management_params is not None:
            input_["sse_aws_key_management_params"] = sse_aws_key_management_params
        if sink_iam_role_arn is not None:
            input_["sink_iam_role_arn"] = sink_iam_role_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_media_concatenation_pipeline(
        self,
        sources: "capo_chime_sdk_media_pipelines.types.concatenation_source_list.ConcatenationSourceList",
        sinks: "capo_chime_sdk_media_pipelines.types.concatenation_sink_list.ConcatenationSinkList",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_concatenation_pipeline_response.CreateMediaConcatenationPipelineResponse":
        """<p>Creates a media concatenation pipeline.</p>

        Args:
            sources: <p>An object that specifies the sources for the media concatenation pipeline.</p>
            sinks: <p>An object that specifies the data sinks for the media concatenation pipeline.</p>
            client_request_token: <p>The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media concatenation pipeline request.</p>
            tags: <p>The tags associated with the media concatenation pipeline.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_concatenation_pipeline_request.CreateMediaConcatenationPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_concatenation_pipeline_response.CreateMediaConcatenationPipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_concatenation_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_concatenation_pipeline.async_create_media_concatenation_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_concatenation_pipeline_request.CreateMediaConcatenationPipelineRequest = {
            "sources": sources,
            "sinks": sinks,
        }
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

    async def create_media_insights_pipeline(
        self,
        media_insights_pipeline_configuration_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        kinesis_video_stream_source_runtime_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.KinesisVideoStreamSourceRuntimeConfiguration"
        ] = None,
        media_insights_runtime_metadata: Optional[
            "capo_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.MediaInsightsRuntimeMetadata"
        ] = None,
        kinesis_video_stream_recording_source_runtime_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.KinesisVideoStreamRecordingSourceRuntimeConfiguration"
        ] = None,
        s3_recording_sink_runtime_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.S3RecordingSinkRuntimeConfiguration"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_response.CreateMediaInsightsPipelineResponse":
        """<p>Creates a media insights pipeline.</p>

        Args:
            media_insights_pipeline_configuration_arn: <p>The ARN of the pipeline's configuration.</p>
            kinesis_video_stream_source_runtime_configuration: <p>The runtime configuration for the Kinesis video stream source of the media insights pipeline.</p>
            media_insights_runtime_metadata: <p>The runtime metadata for the media insights pipeline. Consists of a key-value map of strings.</p>
            kinesis_video_stream_recording_source_runtime_configuration: <p>The runtime configuration for the Kinesis video recording stream source.</p>
            s3_recording_sink_runtime_configuration: <p>The runtime configuration for the S3 recording sink. If specified, the settings in this structure override any settings in <code>S3RecordingSinkConfiguration</code>.</p>
            tags: <p>The tags assigned to the media insights pipeline.</p>
            client_request_token: <p>The unique identifier for the media insights pipeline request.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_request.CreateMediaInsightsPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_response.CreateMediaInsightsPipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_insights_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_insights_pipeline.async_create_media_insights_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_request.CreateMediaInsightsPipelineRequest = {
            "media_insights_pipeline_configuration_arn": media_insights_pipeline_configuration_arn
        }
        if kinesis_video_stream_source_runtime_configuration is not None:
            input_["kinesis_video_stream_source_runtime_configuration"] = (
                kinesis_video_stream_source_runtime_configuration
            )
        if media_insights_runtime_metadata is not None:
            input_["media_insights_runtime_metadata"] = media_insights_runtime_metadata
        if kinesis_video_stream_recording_source_runtime_configuration is not None:
            input_["kinesis_video_stream_recording_source_runtime_configuration"] = (
                kinesis_video_stream_recording_source_runtime_configuration
            )
        if s3_recording_sink_runtime_configuration is not None:
            input_["s3_recording_sink_runtime_configuration"] = (
                s3_recording_sink_runtime_configuration
            )
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_media_insights_pipeline_configuration(
        self,
        media_insights_pipeline_configuration_name: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string.MediaInsightsPipelineConfigurationNameString",
        resource_access_role_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn",
        elements: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        real_time_alert_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_configuration_response.CreateMediaInsightsPipelineConfigurationResponse":
        """<p>A structure that contains the static configurations for a media insights pipeline.</p>

        Args:
            media_insights_pipeline_configuration_name: <p>The name of the media insights pipeline configuration.</p>
            resource_access_role_arn: <p>The ARN of the role used by the service to access Amazon Web Services resources, including <code>Transcribe</code> and <code>Transcribe Call Analytics</code>, on the caller’s behalf.</p>
            real_time_alert_configuration: <p>The configuration settings for the real-time alerts in a media insights pipeline configuration.</p>
            elements: <p>The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream.</p>
            tags: <p>The tags assigned to the media insights pipeline configuration.</p>
            client_request_token: <p>The unique identifier for the media insights pipeline configuration request.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_configuration_request.CreateMediaInsightsPipelineConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_configuration_response.CreateMediaInsightsPipelineConfigurationResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_insights_pipeline_configuration

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_insights_pipeline_configuration.async_create_media_insights_pipeline_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_insights_pipeline_configuration_request.CreateMediaInsightsPipelineConfigurationRequest = {
            "media_insights_pipeline_configuration_name": media_insights_pipeline_configuration_name,
            "resource_access_role_arn": resource_access_role_arn,
            "elements": elements,
        }
        if real_time_alert_configuration is not None:
            input_["real_time_alert_configuration"] = real_time_alert_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_media_live_connector_pipeline(
        self,
        sources: "capo_chime_sdk_media_pipelines.types.live_connector_source_list.LiveConnectorSourceList",
        sinks: "capo_chime_sdk_media_pipelines.types.live_connector_sink_list.LiveConnectorSinkList",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_live_connector_pipeline_response.CreateMediaLiveConnectorPipelineResponse":
        """<p>Creates a media live connector pipeline in an Amazon Chime SDK meeting.</p>

        Args:
            sources: <p>The media live connector pipeline's data sources.</p>
            sinks: <p>The media live connector pipeline's data sinks.</p>
            client_request_token: <p>The token assigned to the client making the request.</p>
            tags: <p>The tags associated with the media live connector pipeline.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_live_connector_pipeline_request.CreateMediaLiveConnectorPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_live_connector_pipeline_response.CreateMediaLiveConnectorPipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_live_connector_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_live_connector_pipeline.async_create_media_live_connector_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_live_connector_pipeline_request.CreateMediaLiveConnectorPipelineRequest = {
            "sources": sources,
            "sinks": sinks,
        }
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

    async def create_media_pipeline_kinesis_video_stream_pool(
        self,
        stream_configuration: "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.KinesisVideoStreamConfiguration",
        pool_name: "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name.KinesisVideoStreamPoolName",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_pipeline_kinesis_video_stream_pool_response.CreateMediaPipelineKinesisVideoStreamPoolResponse":
        """<p>Creates an Amazon Kinesis Video Stream pool for use with media stream pipelines.</p> <note> <p>If a meeting uses an opt-in Region as its <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html#chimesdk-meeting-chime_CreateMeeting-request-MediaRegion">MediaRegion</a>, the KVS stream must be in that same Region. For example, if a meeting uses the <code>af-south-1</code> Region, the KVS stream must also be in <code>af-south-1</code>. However, if the meeting uses a Region that AWS turns on by default, the KVS stream can be in any available Region, including an opt-in Region. For example, if the meeting uses <code>ca-central-1</code>, the KVS stream can be in <code>eu-west-2</code>, <code>us-east-1</code>, <code>af-south-1</code>, or any other Region that the Amazon Chime SDK supports.</p> <p>To learn which AWS Region a meeting uses, call the <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html">GetMeeting</a> API and use the <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html#chimesdk-meeting-chime_CreateMeeting-request-MediaRegion">MediaRegion</a> parameter from the response.</p> <p>For more information about opt-in Regions, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html">Available Regions</a> in the <i>Amazon Chime SDK Developer Guide</i>, and <a href="https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#rande-manage-enable.html">Specify which AWS Regions your account can use</a>, in the <i>AWS Account Management Reference Guide</i>.</p> </note>

        Args:
            stream_configuration: <p>The configuration settings for the stream.</p>
            pool_name: <p>The name of the pool.</p>
            client_request_token: <p>The token assigned to the client making the request.</p>
            tags: <p>The tags assigned to the stream pool.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_pipeline_kinesis_video_stream_pool_request.CreateMediaPipelineKinesisVideoStreamPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_pipeline_kinesis_video_stream_pool_response.CreateMediaPipelineKinesisVideoStreamPoolResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_pipeline_kinesis_video_stream_pool

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_pipeline_kinesis_video_stream_pool.async_create_media_pipeline_kinesis_video_stream_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_pipeline_kinesis_video_stream_pool_request.CreateMediaPipelineKinesisVideoStreamPoolRequest = {
            "stream_configuration": stream_configuration,
            "pool_name": pool_name,
        }
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

    async def create_media_stream_pipeline(
        self,
        sources: "capo_chime_sdk_media_pipelines.types.media_stream_source_list.MediaStreamSourceList",
        sinks: "capo_chime_sdk_media_pipelines.types.media_stream_sink_list.MediaStreamSinkList",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_chime_sdk_media_pipelines.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.create_media_stream_pipeline_response.CreateMediaStreamPipelineResponse":
        """<p>Creates a streaming media pipeline.</p>

        Args:
            sources: <p>The data sources for the media pipeline.</p>
            sinks: <p>The data sink for the media pipeline.</p>
            client_request_token: <p>The token assigned to the client making the request.</p>
            tags: <p>The tags assigned to the media pipeline.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.create_media_stream_pipeline_request.CreateMediaStreamPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.create_media_stream_pipeline_response.CreateMediaStreamPipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_stream_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.create_media_stream_pipeline.async_create_media_stream_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.create_media_stream_pipeline_request.CreateMediaStreamPipelineRequest = {
            "sources": sources,
            "sinks": sinks,
        }
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

    async def delete_media_capture_pipeline(
        self,
        media_pipeline_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Deletes the media pipeline.</p>

        Args:
            media_pipeline_id: <p>The ID of the media pipeline being deleted. </p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.delete_media_capture_pipeline_request.DeleteMediaCapturePipelineRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_capture_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_capture_pipeline.async_delete_media_capture_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.delete_media_capture_pipeline_request.DeleteMediaCapturePipelineRequest = {
            "media_pipeline_id": media_pipeline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_media_insights_pipeline_configuration(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configuration settings.</p>

        Args:
            identifier: <p>The unique identifier of the resource to be deleted. Valid values include the name and ARN of the media insights pipeline configuration.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.delete_media_insights_pipeline_configuration_request.DeleteMediaInsightsPipelineConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_insights_pipeline_configuration

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_insights_pipeline_configuration.async_delete_media_insights_pipeline_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.delete_media_insights_pipeline_configuration_request.DeleteMediaInsightsPipelineConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_media_pipeline(
        self,
        media_pipeline_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Deletes the media pipeline.</p>

        Args:
            media_pipeline_id: <p>The ID of the media pipeline to delete.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.delete_media_pipeline_request.DeleteMediaPipelineRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_pipeline.async_delete_media_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.delete_media_pipeline_request.DeleteMediaPipelineRequest = {
            "media_pipeline_id": media_pipeline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_media_pipeline_kinesis_video_stream_pool(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Kinesis Video Stream pool.</p>

        Args:
            identifier: <p>The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.delete_media_pipeline_kinesis_video_stream_pool_request.DeleteMediaPipelineKinesisVideoStreamPoolRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_pipeline_kinesis_video_stream_pool

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.delete_media_pipeline_kinesis_video_stream_pool.async_delete_media_pipeline_kinesis_video_stream_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.delete_media_pipeline_kinesis_video_stream_pool_request.DeleteMediaPipelineKinesisVideoStreamPoolRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_media_capture_pipeline(
        self,
        media_pipeline_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.get_media_capture_pipeline_response.GetMediaCapturePipelineResponse":
        """<p>Gets an existing media pipeline.</p>

        Args:
            media_pipeline_id: <p>The ID of the pipeline that you want to get.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.get_media_capture_pipeline_request.GetMediaCapturePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.get_media_capture_pipeline_response.GetMediaCapturePipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_capture_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_capture_pipeline.async_get_media_capture_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.get_media_capture_pipeline_request.GetMediaCapturePipelineRequest = {
            "media_pipeline_id": media_pipeline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_media_insights_pipeline_configuration(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.get_media_insights_pipeline_configuration_response.GetMediaInsightsPipelineConfigurationResponse":
        """<p>Gets the configuration settings for a media insights pipeline.</p>

        Args:
            identifier: <p>The unique identifier of the requested resource. Valid values include the name and ARN of the media insights pipeline configuration.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.get_media_insights_pipeline_configuration_request.GetMediaInsightsPipelineConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.get_media_insights_pipeline_configuration_response.GetMediaInsightsPipelineConfigurationResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_insights_pipeline_configuration

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_insights_pipeline_configuration.async_get_media_insights_pipeline_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.get_media_insights_pipeline_configuration_request.GetMediaInsightsPipelineConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_media_pipeline(
        self,
        media_pipeline_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.get_media_pipeline_response.GetMediaPipelineResponse":
        """<p>Gets an existing media pipeline.</p>

        Args:
            media_pipeline_id: <p>The ID of the pipeline that you want to get.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.get_media_pipeline_request.GetMediaPipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.get_media_pipeline_response.GetMediaPipelineResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_pipeline

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_pipeline.async_get_media_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.get_media_pipeline_request.GetMediaPipelineRequest = {
            "media_pipeline_id": media_pipeline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_media_pipeline_kinesis_video_stream_pool(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.get_media_pipeline_kinesis_video_stream_pool_response.GetMediaPipelineKinesisVideoStreamPoolResponse":
        """<p>Gets an Kinesis video stream pool.</p>

        Args:
            identifier: <p>The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.get_media_pipeline_kinesis_video_stream_pool_request.GetMediaPipelineKinesisVideoStreamPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.get_media_pipeline_kinesis_video_stream_pool_response.GetMediaPipelineKinesisVideoStreamPoolResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_pipeline_kinesis_video_stream_pool

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_media_pipeline_kinesis_video_stream_pool.async_get_media_pipeline_kinesis_video_stream_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.get_media_pipeline_kinesis_video_stream_pool_request.GetMediaPipelineKinesisVideoStreamPoolRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_speaker_search_task(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        speaker_search_task_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.get_speaker_search_task_response.GetSpeakerSearchTaskResponse":
        """<p>Retrieves the details of the specified speaker search task.</p>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            speaker_search_task_id: <p>The ID of the speaker search task.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.get_speaker_search_task_request.GetSpeakerSearchTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.get_speaker_search_task_response.GetSpeakerSearchTaskResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_speaker_search_task

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_speaker_search_task.async_get_speaker_search_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.get_speaker_search_task_request.GetSpeakerSearchTaskRequest = {
            "identifier": identifier,
            "speaker_search_task_id": speaker_search_task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_voice_tone_analysis_task(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        voice_tone_analysis_task_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.get_voice_tone_analysis_task_response.GetVoiceToneAnalysisTaskResponse":
        """<p>Retrieves the details of a voice tone analysis task.</p>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            voice_tone_analysis_task_id: <p>The ID of the voice tone analysis task.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.get_voice_tone_analysis_task_request.GetVoiceToneAnalysisTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.get_voice_tone_analysis_task_response.GetVoiceToneAnalysisTaskResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_voice_tone_analysis_task

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.get_voice_tone_analysis_task.async_get_voice_tone_analysis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.get_voice_tone_analysis_task_request.GetVoiceToneAnalysisTaskRequest = {
            "identifier": identifier,
            "voice_tone_analysis_task_id": voice_tone_analysis_task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_media_capture_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_response.ListMediaCapturePipelinesResponse":
        """<p>Returns a list of media pipelines.</p>

        Args:
            next_token: <p>The token used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid Range: 1 - 99.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_request.ListMediaCapturePipelinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_response.ListMediaCapturePipelinesResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_capture_pipelines

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_capture_pipelines.async_list_media_capture_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_request.ListMediaCapturePipelinesRequest = {}
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

    async def iter_list_media_capture_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_media_pipelines.types.list_media_capture_pipelines_response.ListMediaCapturePipelinesResponse]":
        _token = next_token
        while True:
            _response = await self.list_media_capture_pipelines(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_media_insights_pipeline_configurations(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_response.ListMediaInsightsPipelineConfigurationsResponse":
        """<p>Lists the available media insights pipeline configurations.</p>

        Args:
            next_token: <p>The token used to return the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_request.ListMediaInsightsPipelineConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_response.ListMediaInsightsPipelineConfigurationsResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_insights_pipeline_configurations

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_insights_pipeline_configurations.async_list_media_insights_pipeline_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_request.ListMediaInsightsPipelineConfigurationsRequest = {}
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

    async def iter_list_media_insights_pipeline_configurations(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_media_pipelines.types.list_media_insights_pipeline_configurations_response.ListMediaInsightsPipelineConfigurationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_media_insights_pipeline_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_media_pipeline_kinesis_video_stream_pools(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_response.ListMediaPipelineKinesisVideoStreamPoolsResponse":
        """<p>Lists the video stream pools in the media pipeline.</p>

        Args:
            next_token: <p>The token used to return the next page of results. </p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_request.ListMediaPipelineKinesisVideoStreamPoolsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_response.ListMediaPipelineKinesisVideoStreamPoolsResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_pipeline_kinesis_video_stream_pools

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_pipeline_kinesis_video_stream_pools.async_list_media_pipeline_kinesis_video_stream_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_request.ListMediaPipelineKinesisVideoStreamPoolsRequest = {}
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

    async def iter_list_media_pipeline_kinesis_video_stream_pools(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_media_pipelines.types.list_media_pipeline_kinesis_video_stream_pools_response.ListMediaPipelineKinesisVideoStreamPoolsResponse]":
        _token = next_token
        while True:
            _response = await self.list_media_pipeline_kinesis_video_stream_pools(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_media_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.list_media_pipelines_response.ListMediaPipelinesResponse":
        """<p>Returns a list of media pipelines.</p>

        Args:
            next_token: <p>The token used to retrieve the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid Range: 1 - 99.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.list_media_pipelines_request.ListMediaPipelinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.list_media_pipelines_response.ListMediaPipelinesResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_pipelines

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_media_pipelines.async_list_media_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.list_media_pipelines_request.ListMediaPipelinesRequest = {}
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

    async def iter_list_media_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        next_token: Optional[
            "capo_chime_sdk_media_pipelines.types.string.String"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_media_pipelines.types.result_max.ResultMax"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_media_pipelines.types.list_media_pipelines_response.ListMediaPipelinesResponse]":
        _token = next_token
        while True:
            _response = await self.list_media_pipelines(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags available for a media pipeline.</p>

        Args:
            resource_arn: <p>The ARN of the media pipeline associated with any tags. The ARN consists of the pipeline's region, resource ID, and pipeline ID.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_speaker_search_task(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        voice_profile_domain_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        kinesis_video_stream_source_task_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.KinesisVideoStreamSourceTaskConfiguration"
        ] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.start_speaker_search_task_response.StartSpeakerSearchTaskResponse":
        """<p>Starts a speaker search task.</p> <important> <p>Before starting any speaker search tasks, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the <a href="https://aws.amazon.com/service-terms/">AWS service terms</a> for the Amazon Chime SDK.</p> </important>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            voice_profile_domain_arn: <p>The ARN of the voice profile domain that will store the voice profile.</p>
            kinesis_video_stream_source_task_configuration: <p>The task configuration for the Kinesis video stream source of the media insights pipeline.</p>
            client_request_token: <p>The unique identifier for the client request. Use a different token for different speaker search tasks.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.start_speaker_search_task_request.StartSpeakerSearchTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.start_speaker_search_task_response.StartSpeakerSearchTaskResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.start_speaker_search_task

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.start_speaker_search_task.async_start_speaker_search_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.start_speaker_search_task_request.StartSpeakerSearchTaskRequest = {
            "identifier": identifier,
            "voice_profile_domain_arn": voice_profile_domain_arn,
        }
        if kinesis_video_stream_source_task_configuration is not None:
            input_["kinesis_video_stream_source_task_configuration"] = (
                kinesis_video_stream_source_task_configuration
            )
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_voice_tone_analysis_task(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        language_code: "capo_chime_sdk_media_pipelines.types.voice_analytics_language_code.VoiceAnalyticsLanguageCode",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        kinesis_video_stream_source_task_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_source_task_configuration.KinesisVideoStreamSourceTaskConfiguration"
        ] = None,
        client_request_token: Optional[
            "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.start_voice_tone_analysis_task_response.StartVoiceToneAnalysisTaskResponse":
        """<p>Starts a voice tone analysis task. For more information about voice tone analysis, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-analytics.html">Using Amazon Chime SDK voice analytics</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p> <important> <p>Before starting any voice tone analysis tasks, you must provide all notices and obtain all consents from the speaker as required under applicable privacy and biometrics laws, and as required under the <a href="https://aws.amazon.com/service-terms/">AWS service terms</a> for the Amazon Chime SDK.</p> </important>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            language_code: <p>The language code.</p>
            kinesis_video_stream_source_task_configuration: <p>The task configuration for the Kinesis video stream source of the media insights pipeline.</p>
            client_request_token: <p>The unique identifier for the client request. Use a different token for different voice tone analysis tasks.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.start_voice_tone_analysis_task_request.StartVoiceToneAnalysisTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.start_voice_tone_analysis_task_response.StartVoiceToneAnalysisTaskResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.start_voice_tone_analysis_task

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.start_voice_tone_analysis_task.async_start_voice_tone_analysis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.start_voice_tone_analysis_task_request.StartVoiceToneAnalysisTaskRequest = {
            "identifier": identifier,
            "language_code": language_code,
        }
        if kinesis_video_stream_source_task_configuration is not None:
            input_["kinesis_video_stream_source_task_configuration"] = (
                kinesis_video_stream_source_task_configuration
            )
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_speaker_search_task(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        speaker_search_task_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Stops a speaker search task.</p>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            speaker_search_task_id: <p>The speaker search task ID.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.stop_speaker_search_task_request.StopSpeakerSearchTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.stop_speaker_search_task

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.stop_speaker_search_task.async_stop_speaker_search_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.stop_speaker_search_task_request.StopSpeakerSearchTaskRequest = {
            "identifier": identifier,
            "speaker_search_task_id": speaker_search_task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_voice_tone_analysis_task(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        voice_tone_analysis_task_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Stops a voice tone analysis task.</p>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            voice_tone_analysis_task_id: <p>The ID of the voice tone analysis task.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.stop_voice_tone_analysis_task_request.StopVoiceToneAnalysisTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.stop_voice_tone_analysis_task

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.stop_voice_tone_analysis_task.async_stop_voice_tone_analysis_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.stop_voice_tone_analysis_task_request.StopVoiceToneAnalysisTaskRequest = {
            "identifier": identifier,
            "voice_tone_analysis_task_id": voice_tone_analysis_task_id,
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
        resource_arn: "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_chime_sdk_media_pipelines.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> (
        "capo_chime_sdk_media_pipelines.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>The ARN of the media pipeline that you want to tag. Consists of the pipeline's endpoint region, resource ID, and pipeline ID.</p>

        Args:
            resource_arn: <p>The ARN of the media pipeline associated with any tags. The ARN consists of the pipeline's endpoint region, resource ID, and pipeline ID.</p>
            tags: <p>The tags associated with the specified media pipeline.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_chime_sdk_media_pipelines.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes any tags from a media pipeline.</p>

        Args:
            resource_arn: <p>The ARN of the pipeline that you want to untag.</p>
            tag_keys: <p>The key/value pairs in the tag that you want to remove.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_media_insights_pipeline_configuration(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        resource_access_role_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn",
        elements: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        real_time_alert_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_configuration_response.UpdateMediaInsightsPipelineConfigurationResponse":
        """<p>Updates the media insights pipeline's configuration settings.</p>

        Args:
            identifier: <p>The unique identifier for the resource to be updated. Valid values include the name and ARN of the media insights pipeline configuration.</p>
            resource_access_role_arn: <p>The ARN of the role used by the service to access Amazon Web Services resources.</p>
            real_time_alert_configuration: <p>The configuration settings for real-time alerts for the media insights pipeline.</p>
            elements: <p>The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream..</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_configuration_request.UpdateMediaInsightsPipelineConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_configuration_response.UpdateMediaInsightsPipelineConfigurationResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.update_media_insights_pipeline_configuration

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.update_media_insights_pipeline_configuration.async_update_media_insights_pipeline_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_configuration_request.UpdateMediaInsightsPipelineConfigurationRequest = {
            "identifier": identifier,
            "resource_access_role_arn": resource_access_role_arn,
            "elements": elements,
        }
        if real_time_alert_configuration is not None:
            input_["real_time_alert_configuration"] = real_time_alert_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_media_insights_pipeline_status(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        update_status: "capo_chime_sdk_media_pipelines.types.media_pipeline_status_update.MediaPipelineStatusUpdate",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
    ) -> None:
        """<p>Updates the status of a media insights pipeline.</p>

        Args:
            identifier: <p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>
            update_status: <p>The requested status of the media insights pipeline.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request.UpdateMediaInsightsPipelineStatusRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.update_media_insights_pipeline_status

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.update_media_insights_pipeline_status.async_update_media_insights_pipeline_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.update_media_insights_pipeline_status_request.UpdateMediaInsightsPipelineStatusRequest = {
            "identifier": identifier,
            "update_status": update_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_media_pipeline_kinesis_video_stream_pool(
        self,
        identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncChimeSDKMediaPipelinesClientConfig] = None,
        stream_configuration: Optional[
            "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update.KinesisVideoStreamConfigurationUpdate"
        ] = None,
    ) -> "capo_chime_sdk_media_pipelines.types.update_media_pipeline_kinesis_video_stream_pool_response.UpdateMediaPipelineKinesisVideoStreamPoolResponse":
        """<p>Updates an Amazon Kinesis Video Stream pool in a media pipeline.</p>

        Args:
            identifier: <p>The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.</p>
            stream_configuration: <p>The configuration settings for the video stream.</p>

        Raises:
            capo_chime_sdk_media_pipelines.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_media_pipelines.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_media_pipelines.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_media_pipelines.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_media_pipelines.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_media_pipelines.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_media_pipelines.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_media_pipelines.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_media_pipelines.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_media_pipelines.types.update_media_pipeline_kinesis_video_stream_pool_request.UpdateMediaPipelineKinesisVideoStreamPoolRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_media_pipelines.types.update_media_pipeline_kinesis_video_stream_pool_response.UpdateMediaPipelineKinesisVideoStreamPoolResponse"
        ]:
            import capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.update_media_pipeline_kinesis_video_stream_pool

            (
                output,
                http_response,
            ) = await capo_chime_sdk_media_pipelines._operations.chime_sdk_media_pipelines_service.update_media_pipeline_kinesis_video_stream_pool.async_update_media_pipeline_kinesis_video_stream_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_media_pipelines.types.update_media_pipeline_kinesis_video_stream_pool_request.UpdateMediaPipelineKinesisVideoStreamPoolRequest = {
            "identifier": identifier
        }
        if stream_configuration is not None:
            input_["stream_configuration"] = stream_configuration

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
