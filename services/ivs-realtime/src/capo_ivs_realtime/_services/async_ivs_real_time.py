"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#AmazonInteractiveVideoServiceRealTime``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ivs_realtime._auth._signers
import capo_ivs_realtime._auth._sigv4
from capo_ivs_realtime._auth._identity import Credentials
from capo_ivs_realtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ivs_realtime._auth._zapros_handler import AuthMiddleware
from capo_ivs_realtime._pagination import resolve_path as _resolve_path
from capo_ivs_realtime._services._aws_config import aaws_config
from capo_ivs_realtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ivs_realtime.types.auto_participant_recording_configuration
    import capo_ivs_realtime.types.boolean
    import capo_ivs_realtime.types.composition_arn
    import capo_ivs_realtime.types.composition_client_token
    import capo_ivs_realtime.types.create_encoder_configuration_request
    import capo_ivs_realtime.types.create_encoder_configuration_response
    import capo_ivs_realtime.types.create_ingest_configuration_request
    import capo_ivs_realtime.types.create_ingest_configuration_response
    import capo_ivs_realtime.types.create_participant_token_request
    import capo_ivs_realtime.types.create_participant_token_response
    import capo_ivs_realtime.types.create_stage_request
    import capo_ivs_realtime.types.create_stage_response
    import capo_ivs_realtime.types.create_storage_configuration_request
    import capo_ivs_realtime.types.create_storage_configuration_response
    import capo_ivs_realtime.types.delete_encoder_configuration_request
    import capo_ivs_realtime.types.delete_encoder_configuration_response
    import capo_ivs_realtime.types.delete_ingest_configuration_request
    import capo_ivs_realtime.types.delete_ingest_configuration_response
    import capo_ivs_realtime.types.delete_public_key_request
    import capo_ivs_realtime.types.delete_public_key_response
    import capo_ivs_realtime.types.delete_stage_request
    import capo_ivs_realtime.types.delete_stage_response
    import capo_ivs_realtime.types.delete_storage_configuration_request
    import capo_ivs_realtime.types.delete_storage_configuration_response
    import capo_ivs_realtime.types.destination_configuration_list
    import capo_ivs_realtime.types.disconnect_participant_reason
    import capo_ivs_realtime.types.disconnect_participant_request
    import capo_ivs_realtime.types.disconnect_participant_response
    import capo_ivs_realtime.types.encoder_configuration_arn
    import capo_ivs_realtime.types.encoder_configuration_name
    import capo_ivs_realtime.types.get_composition_request
    import capo_ivs_realtime.types.get_composition_response
    import capo_ivs_realtime.types.get_encoder_configuration_request
    import capo_ivs_realtime.types.get_encoder_configuration_response
    import capo_ivs_realtime.types.get_ingest_configuration_request
    import capo_ivs_realtime.types.get_ingest_configuration_response
    import capo_ivs_realtime.types.get_participant_request
    import capo_ivs_realtime.types.get_participant_response
    import capo_ivs_realtime.types.get_public_key_request
    import capo_ivs_realtime.types.get_public_key_response
    import capo_ivs_realtime.types.get_stage_request
    import capo_ivs_realtime.types.get_stage_response
    import capo_ivs_realtime.types.get_stage_session_request
    import capo_ivs_realtime.types.get_stage_session_response
    import capo_ivs_realtime.types.get_storage_configuration_request
    import capo_ivs_realtime.types.get_storage_configuration_response
    import capo_ivs_realtime.types.import_public_key_request
    import capo_ivs_realtime.types.import_public_key_response
    import capo_ivs_realtime.types.ingest_configuration_arn
    import capo_ivs_realtime.types.ingest_configuration_name
    import capo_ivs_realtime.types.ingest_configuration_stage_arn
    import capo_ivs_realtime.types.ingest_configuration_state
    import capo_ivs_realtime.types.ingest_configuration_summary
    import capo_ivs_realtime.types.ingest_protocol
    import capo_ivs_realtime.types.insecure_ingest
    import capo_ivs_realtime.types.layout_configuration
    import capo_ivs_realtime.types.list_compositions_request
    import capo_ivs_realtime.types.list_compositions_response
    import capo_ivs_realtime.types.list_encoder_configurations_request
    import capo_ivs_realtime.types.list_encoder_configurations_response
    import capo_ivs_realtime.types.list_ingest_configurations_request
    import capo_ivs_realtime.types.list_ingest_configurations_response
    import capo_ivs_realtime.types.list_participant_events_request
    import capo_ivs_realtime.types.list_participant_events_response
    import capo_ivs_realtime.types.list_participant_replicas_request
    import capo_ivs_realtime.types.list_participant_replicas_response
    import capo_ivs_realtime.types.list_participants_request
    import capo_ivs_realtime.types.list_participants_response
    import capo_ivs_realtime.types.list_public_keys_request
    import capo_ivs_realtime.types.list_public_keys_response
    import capo_ivs_realtime.types.list_stage_sessions_request
    import capo_ivs_realtime.types.list_stage_sessions_response
    import capo_ivs_realtime.types.list_stages_request
    import capo_ivs_realtime.types.list_stages_response
    import capo_ivs_realtime.types.list_storage_configurations_request
    import capo_ivs_realtime.types.list_storage_configurations_response
    import capo_ivs_realtime.types.list_tags_for_resource_request
    import capo_ivs_realtime.types.list_tags_for_resource_response
    import capo_ivs_realtime.types.max_composition_results
    import capo_ivs_realtime.types.max_encoder_configuration_results
    import capo_ivs_realtime.types.max_ingest_configuration_results
    import capo_ivs_realtime.types.max_participant_event_results
    import capo_ivs_realtime.types.max_participant_replica_results
    import capo_ivs_realtime.types.max_participant_results
    import capo_ivs_realtime.types.max_public_key_results
    import capo_ivs_realtime.types.max_stage_results
    import capo_ivs_realtime.types.max_stage_session_results
    import capo_ivs_realtime.types.max_storage_configuration_results
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.participant_attributes
    import capo_ivs_realtime.types.participant_id
    import capo_ivs_realtime.types.participant_recording_filter_by_recording_state
    import capo_ivs_realtime.types.participant_replica
    import capo_ivs_realtime.types.participant_state
    import capo_ivs_realtime.types.participant_token_attributes
    import capo_ivs_realtime.types.participant_token_capabilities
    import capo_ivs_realtime.types.participant_token_configurations
    import capo_ivs_realtime.types.participant_token_duration_minutes
    import capo_ivs_realtime.types.participant_token_id
    import capo_ivs_realtime.types.participant_token_user_id
    import capo_ivs_realtime.types.public_key_arn
    import capo_ivs_realtime.types.public_key_material
    import capo_ivs_realtime.types.public_key_name
    import capo_ivs_realtime.types.public_key_summary
    import capo_ivs_realtime.types.published
    import capo_ivs_realtime.types.reconnect_window_seconds
    import capo_ivs_realtime.types.redundant_ingest
    import capo_ivs_realtime.types.resource_arn
    import capo_ivs_realtime.types.s3_storage_configuration
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.stage_name
    import capo_ivs_realtime.types.stage_session_id
    import capo_ivs_realtime.types.start_composition_request
    import capo_ivs_realtime.types.start_composition_response
    import capo_ivs_realtime.types.start_participant_replication_request
    import capo_ivs_realtime.types.start_participant_replication_response
    import capo_ivs_realtime.types.stop_composition_request
    import capo_ivs_realtime.types.stop_composition_response
    import capo_ivs_realtime.types.stop_participant_replication_request
    import capo_ivs_realtime.types.stop_participant_replication_response
    import capo_ivs_realtime.types.storage_configuration_arn
    import capo_ivs_realtime.types.storage_configuration_name
    import capo_ivs_realtime.types.tag_key_list
    import capo_ivs_realtime.types.tag_resource_request
    import capo_ivs_realtime.types.tag_resource_response
    import capo_ivs_realtime.types.tags
    import capo_ivs_realtime.types.untag_resource_request
    import capo_ivs_realtime.types.untag_resource_response
    import capo_ivs_realtime.types.update_ingest_configuration_request
    import capo_ivs_realtime.types.update_ingest_configuration_response
    import capo_ivs_realtime.types.update_stage_request
    import capo_ivs_realtime.types.update_stage_response
    import capo_ivs_realtime.types.user_id
    import capo_ivs_realtime.types.video


class AsyncIVSRealTimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncIVSRealTimeClient:
    """A client for the ``IVSRealTime`` service.

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
        self._config = AsyncIVSRealTimeClientConfig(
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
        self, config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIVSRealTimeClientConfig = config_overrides or {}
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

    async def create_encoder_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        name: Optional[
            "capo_ivs_realtime.types.encoder_configuration_name.EncoderConfigurationName"
        ] = None,
        video: Optional["capo_ivs_realtime.types.video.Video"] = None,
        tags: Optional["capo_ivs_realtime.types.tags.Tags"] = None,
    ) -> "capo_ivs_realtime.types.create_encoder_configuration_response.CreateEncoderConfigurationResponse":
        """<p>Creates an EncoderConfiguration object.</p>

        Args:
            name: <p>Optional name to identify the resource.</p>
            video: <p>Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps.</p>
            tags: <p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.create_encoder_configuration_request.CreateEncoderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.create_encoder_configuration_response.CreateEncoderConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_encoder_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_encoder_configuration.async_create_encoder_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.create_encoder_configuration_request.CreateEncoderConfigurationRequest = {}
        if name is not None:
            input_["name"] = name
        if video is not None:
            input_["video"] = video
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ingest_configuration(
        self,
        ingest_protocol: "capo_ivs_realtime.types.ingest_protocol.IngestProtocol",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        name: Optional[
            "capo_ivs_realtime.types.ingest_configuration_name.IngestConfigurationName"
        ] = None,
        stage_arn: Optional[
            "capo_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
        ] = None,
        user_id: Optional["capo_ivs_realtime.types.user_id.UserId"] = None,
        attributes: Optional[
            "capo_ivs_realtime.types.participant_attributes.ParticipantAttributes"
        ] = None,
        insecure_ingest: Optional[
            "capo_ivs_realtime.types.insecure_ingest.InsecureIngest"
        ] = None,
        redundant_ingest: Optional[
            "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
        ] = None,
        tags: Optional["capo_ivs_realtime.types.tags.Tags"] = None,
    ) -> "capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse":
        """<p>Creates a new IngestConfiguration resource, used to specify the ingest protocol for a stage.</p>

        Args:
            name: <p>Optional name that can be specified for the IngestConfiguration being created.</p>
            stage_arn: <p>ARN of the stage with which the IngestConfiguration is associated.</p>
            user_id: <p>Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>
            attributes: <p>Application-provided attributes to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>
            ingest_protocol: <p>Type of ingest protocol that the user employs to broadcast. If this is set to <code>RTMP</code>, <code>insecureIngest</code> must be set to <code>true</code>.</p>
            insecure_ingest: <p>Whether the stage allows insecure RTMP ingest. This must be set to <code>true</code>, if <code>ingestProtocol</code> is set to <code>RTMP</code>. Default: <code>false</code>. </p>
            redundant_ingest: <p>Indicates whether redundant ingest is enabled for the ingest configuration. Default: <code>false</code>. </p>
            tags: <p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.create_ingest_configuration_request.CreateIngestConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.create_ingest_configuration_response.CreateIngestConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_ingest_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_ingest_configuration.async_create_ingest_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.create_ingest_configuration_request.CreateIngestConfigurationRequest = {
            "ingest_protocol": ingest_protocol
        }
        if name is not None:
            input_["name"] = name
        if stage_arn is not None:
            input_["stage_arn"] = stage_arn
        if user_id is not None:
            input_["user_id"] = user_id
        if attributes is not None:
            input_["attributes"] = attributes
        if insecure_ingest is not None:
            input_["insecure_ingest"] = insecure_ingest
        if redundant_ingest is not None:
            input_["redundant_ingest"] = redundant_ingest
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_participant_token(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        duration: Optional[
            "capo_ivs_realtime.types.participant_token_duration_minutes.ParticipantTokenDurationMinutes"
        ] = None,
        user_id: Optional[
            "capo_ivs_realtime.types.participant_token_user_id.ParticipantTokenUserId"
        ] = None,
        attributes: Optional[
            "capo_ivs_realtime.types.participant_token_attributes.ParticipantTokenAttributes"
        ] = None,
        capabilities: Optional[
            "capo_ivs_realtime.types.participant_token_capabilities.ParticipantTokenCapabilities"
        ] = None,
    ) -> "capo_ivs_realtime.types.create_participant_token_response.CreateParticipantTokenResponse":
        """<p>Creates an additional token for a specified stage. This can be done after stage creation or when tokens expire. Tokens always are scoped to the stage for which they are created.</p> <p>Encryption keys are owned by Amazon IVS and never used directly by your application.</p>

        Args:
            stage_arn: <p>ARN of the stage to which this token is scoped.</p>
            duration: <p>Duration (in minutes), after which the token expires. Default: 720 (12 hours).</p>
            user_id: <p>Name that can be specified to help identify the token. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>
            attributes: <p>Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>
            capabilities: <p>Set of capabilities that the user is allowed to perform in the stage. Default: <code>PUBLISH, SUBSCRIBE</code>.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.create_participant_token_request.CreateParticipantTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.create_participant_token_response.CreateParticipantTokenResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_participant_token

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_participant_token.async_create_participant_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.create_participant_token_request.CreateParticipantTokenRequest = {
            "stage_arn": stage_arn
        }
        if duration is not None:
            input_["duration"] = duration
        if user_id is not None:
            input_["user_id"] = user_id
        if attributes is not None:
            input_["attributes"] = attributes
        if capabilities is not None:
            input_["capabilities"] = capabilities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_stage(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        name: Optional["capo_ivs_realtime.types.stage_name.StageName"] = None,
        participant_token_configurations: Optional[
            "capo_ivs_realtime.types.participant_token_configurations.ParticipantTokenConfigurations"
        ] = None,
        tags: Optional["capo_ivs_realtime.types.tags.Tags"] = None,
        auto_participant_recording_configuration: Optional[
            "capo_ivs_realtime.types.auto_participant_recording_configuration.AutoParticipantRecordingConfiguration"
        ] = None,
    ) -> "capo_ivs_realtime.types.create_stage_response.CreateStageResponse":
        """<p>Creates a new stage (and optionally participant tokens).</p>

        Args:
            name: <p>Optional name that can be specified for the stage being created.</p>
            participant_token_configurations: <p>Array of participant token configuration objects to attach to the new stage.</p>
            tags: <p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there. </p>
            auto_participant_recording_configuration: <p>Configuration object for individual participant recording, to attach to the new stage.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.create_stage_request.CreateStageRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.create_stage_response.CreateStageResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_stage

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_stage.async_create_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.create_stage_request.CreateStageRequest = {}
        if name is not None:
            input_["name"] = name
        if participant_token_configurations is not None:
            input_["participant_token_configurations"] = (
                participant_token_configurations
            )
        if tags is not None:
            input_["tags"] = tags
        if auto_participant_recording_configuration is not None:
            input_["auto_participant_recording_configuration"] = (
                auto_participant_recording_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_storage_configuration(
        self,
        s3: "capo_ivs_realtime.types.s3_storage_configuration.S3StorageConfiguration",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        name: Optional[
            "capo_ivs_realtime.types.storage_configuration_name.StorageConfigurationName"
        ] = None,
        tags: Optional["capo_ivs_realtime.types.tags.Tags"] = None,
    ) -> "capo_ivs_realtime.types.create_storage_configuration_response.CreateStorageConfigurationResponse":
        """<p>Creates a new storage configuration, used to enable recording to Amazon S3. When a StorageConfiguration is created, IVS will modify the S3 bucketPolicy of the provided bucket. This will ensure that IVS has sufficient permissions to write content to the provided bucket.</p>

        Args:
            name: <p>Storage configuration name. The value does not need to be unique.</p>
            s3: <p>A complex type that contains a storage configuration for where recorded video will be stored.</p>
            tags: <p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.create_storage_configuration_request.CreateStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.create_storage_configuration_response.CreateStorageConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_storage_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.create_storage_configuration.async_create_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.create_storage_configuration_request.CreateStorageConfigurationRequest = {
            "s3": s3
        }
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_encoder_configuration(
        self,
        arn: "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.delete_encoder_configuration_response.DeleteEncoderConfigurationResponse":
        """<p>Deletes an EncoderConfiguration resource. Ensures that no Compositions are using this template; otherwise, returns an error.</p>

        Args:
            arn: <p>ARN of the EncoderConfiguration.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.delete_encoder_configuration_request.DeleteEncoderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.delete_encoder_configuration_response.DeleteEncoderConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_encoder_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_encoder_configuration.async_delete_encoder_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.delete_encoder_configuration_request.DeleteEncoderConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ingest_configuration(
        self,
        arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        force: Optional["capo_ivs_realtime.types.boolean.Boolean"] = None,
    ) -> "capo_ivs_realtime.types.delete_ingest_configuration_response.DeleteIngestConfigurationResponse":
        """<p>Deletes a specified IngestConfiguration, so it can no longer be used to broadcast. An IngestConfiguration cannot be deleted if the publisher is actively streaming to a stage, unless <code>force</code> is set to <code>true</code>.</p>

        Args:
            arn: <p>ARN of the IngestConfiguration.</p>
            force: <p>Optional field to force deletion of the IngestConfiguration. If this is set to <code>true</code> when a participant is actively publishing, the participant is disconnected from the stage, followed by deletion of the IngestConfiguration. Default: <code>false</code>.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.delete_ingest_configuration_request.DeleteIngestConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.delete_ingest_configuration_response.DeleteIngestConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_ingest_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_ingest_configuration.async_delete_ingest_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.delete_ingest_configuration_request.DeleteIngestConfigurationRequest = {
            "arn": arn
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_public_key(
        self,
        arn: "capo_ivs_realtime.types.public_key_arn.PublicKeyArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.delete_public_key_response.DeletePublicKeyResponse":
        """<p>Deletes the specified public key used to sign stage participant tokens. This invalidates future participant tokens generated using the key pair’s private key. </p>

        Args:
            arn: <p>ARN of the public key to be deleted.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.delete_public_key_request.DeletePublicKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.delete_public_key_response.DeletePublicKeyResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_public_key

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_public_key.async_delete_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.delete_public_key_request.DeletePublicKeyRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_stage(
        self,
        arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.delete_stage_response.DeleteStageResponse":
        """<p>Shuts down and deletes the specified stage (disconnecting all participants). This operation also removes the <code>stageArn</code> from the associated <a>IngestConfiguration</a>, if there are participants using the IngestConfiguration to publish to the stage.</p>

        Args:
            arn: <p>ARN of the stage to be deleted.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.delete_stage_request.DeleteStageRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.delete_stage_response.DeleteStageResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_stage

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_stage.async_delete_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.delete_stage_request.DeleteStageRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_storage_configuration(
        self,
        arn: "capo_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.delete_storage_configuration_response.DeleteStorageConfigurationResponse":
        """<p>Deletes the storage configuration for the specified ARN.</p> <p>If you try to delete a storage configuration that is used by a Composition, you will get an error (409 ConflictException). To avoid this, for all Compositions that reference the storage configuration, first use <a>StopComposition</a> and wait for it to complete, then use DeleteStorageConfiguration.</p>

        Args:
            arn: <p>ARN of the storage configuration to be deleted.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.delete_storage_configuration_request.DeleteStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.delete_storage_configuration_response.DeleteStorageConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_storage_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.delete_storage_configuration.async_delete_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.delete_storage_configuration_request.DeleteStorageConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disconnect_participant(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        participant_id: "capo_ivs_realtime.types.participant_token_id.ParticipantTokenId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        reason: Optional[
            "capo_ivs_realtime.types.disconnect_participant_reason.DisconnectParticipantReason"
        ] = None,
    ) -> "capo_ivs_realtime.types.disconnect_participant_response.DisconnectParticipantResponse":
        """<p>Disconnects a specified participant from a specified stage. If the participant is publishing using an <a>IngestConfiguration</a>, DisconnectParticipant also updates the <code>stageArn</code> in the IngestConfiguration to be an empty string.</p>

        Args:
            stage_arn: <p>ARN of the stage to which the participant is attached.</p>
            participant_id: <p>Identifier of the participant to be disconnected. IVS assigns this; it is returned by <a>CreateParticipantToken</a> (for streams using WebRTC ingest) or <a>CreateIngestConfiguration</a> (for streams using RTMP ingest).</p>
            reason: <p>Description of why this participant is being disconnected.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.disconnect_participant_request.DisconnectParticipantRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.disconnect_participant_response.DisconnectParticipantResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.disconnect_participant

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.disconnect_participant.async_disconnect_participant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.disconnect_participant_request.DisconnectParticipantRequest = {
            "stage_arn": stage_arn,
            "participant_id": participant_id,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_composition(
        self,
        arn: "capo_ivs_realtime.types.composition_arn.CompositionArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_composition_response.GetCompositionResponse":
        """<p>Get information about the specified Composition resource.</p>

        Args:
            arn: <p>ARN of the Composition resource.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_composition_request.GetCompositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_composition_response.GetCompositionResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_composition

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_composition.async_get_composition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_composition_request.GetCompositionRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_encoder_configuration(
        self,
        arn: "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_encoder_configuration_response.GetEncoderConfigurationResponse":
        """<p>Gets information about the specified EncoderConfiguration resource. </p>

        Args:
            arn: <p>ARN of the EncoderConfiguration resource.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_encoder_configuration_request.GetEncoderConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_encoder_configuration_response.GetEncoderConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_encoder_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_encoder_configuration.async_get_encoder_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_encoder_configuration_request.GetEncoderConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ingest_configuration(
        self,
        arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_ingest_configuration_response.GetIngestConfigurationResponse":
        """<p>Gets information about the specified IngestConfiguration.</p>

        Args:
            arn: <p>ARN of the ingest for which the information is to be retrieved.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_ingest_configuration_request.GetIngestConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_ingest_configuration_response.GetIngestConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_ingest_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_ingest_configuration.async_get_ingest_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_ingest_configuration_request.GetIngestConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_participant(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_participant_response.GetParticipantResponse":
        """<p>Gets information about the specified participant token.</p>

        Args:
            stage_arn: <p>Stage ARN.</p>
            session_id: <p>ID of a session within the stage.</p>
            participant_id: <p>Unique identifier for the participant. This is assigned by IVS and returned by <a>CreateParticipantToken</a>.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_participant_request.GetParticipantRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_participant_response.GetParticipantResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_participant

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_participant.async_get_participant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_participant_request.GetParticipantRequest = {
            "stage_arn": stage_arn,
            "session_id": session_id,
            "participant_id": participant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_public_key(
        self,
        arn: "capo_ivs_realtime.types.public_key_arn.PublicKeyArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_public_key_response.GetPublicKeyResponse":
        """<p>Gets information for the specified public key.</p>

        Args:
            arn: <p>ARN of the public key for which the information is to be retrieved.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_public_key_request.GetPublicKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_public_key_response.GetPublicKeyResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_public_key

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_public_key.async_get_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_public_key_request.GetPublicKeyRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_stage(
        self,
        arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_stage_response.GetStageResponse":
        """<p>Gets information for the specified stage.</p>

        Args:
            arn: <p>ARN of the stage for which the information is to be retrieved.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_stage_request.GetStageRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_stage_response.GetStageResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_stage

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_stage.async_get_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_stage_request.GetStageRequest = {"arn": arn}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_stage_session(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_stage_session_response.GetStageSessionResponse":
        """<p>Gets information for the specified stage session.</p>

        Args:
            stage_arn: <p>ARN of the stage for which the information is to be retrieved.</p>
            session_id: <p>ID of a session within the stage.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_stage_session_request.GetStageSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_stage_session_response.GetStageSessionResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_stage_session

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_stage_session.async_get_stage_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_stage_session_request.GetStageSessionRequest = {
            "stage_arn": stage_arn,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_storage_configuration(
        self,
        arn: "capo_ivs_realtime.types.storage_configuration_arn.StorageConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.get_storage_configuration_response.GetStorageConfigurationResponse":
        """<p>Gets the storage configuration for the specified ARN.</p>

        Args:
            arn: <p>ARN of the storage configuration to be retrieved.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.get_storage_configuration_request.GetStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.get_storage_configuration_response.GetStorageConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_storage_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.get_storage_configuration.async_get_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.get_storage_configuration_request.GetStorageConfigurationRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_public_key(
        self,
        public_key_material: "capo_ivs_realtime.types.public_key_material.PublicKeyMaterial",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        name: Optional["capo_ivs_realtime.types.public_key_name.PublicKeyName"] = None,
        tags: Optional["capo_ivs_realtime.types.tags.Tags"] = None,
    ) -> "capo_ivs_realtime.types.import_public_key_response.ImportPublicKeyResponse":
        """<p>Import a public key to be used for signing stage participant tokens.</p>

        Args:
            public_key_material: <p>The content of the public key to be imported.</p>
            name: <p>Name of the public key to be imported.</p>
            tags: <p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.import_public_key_request.ImportPublicKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.import_public_key_response.ImportPublicKeyResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.import_public_key

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.import_public_key.async_import_public_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.import_public_key_request.ImportPublicKeyRequest = {
            "public_key_material": public_key_material
        }
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_compositions(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        filter_by_stage_arn: Optional[
            "capo_ivs_realtime.types.stage_arn.StageArn"
        ] = None,
        filter_by_encoder_configuration_arn: Optional[
            "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
        ] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_composition_results.MaxCompositionResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_compositions_response.ListCompositionsResponse":
        """<p>Gets summary information about all Compositions in your account, in the AWS region where the API request is processed. </p>

        Args:
            filter_by_stage_arn: <p>Filters the Composition list to match the specified Stage ARN.</p>
            filter_by_encoder_configuration_arn: <p>Filters the Composition list to match the specified EncoderConfiguration attached to at least one of its output.</p>
            next_token: <p>The first Composition to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 100.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_compositions_request.ListCompositionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_compositions_response.ListCompositionsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_compositions

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_compositions.async_list_compositions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_compositions_request.ListCompositionsRequest = {}
        if filter_by_stage_arn is not None:
            input_["filter_by_stage_arn"] = filter_by_stage_arn
        if filter_by_encoder_configuration_arn is not None:
            input_["filter_by_encoder_configuration_arn"] = (
                filter_by_encoder_configuration_arn
            )
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

    async def iter_list_compositions(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        filter_by_stage_arn: Optional[
            "capo_ivs_realtime.types.stage_arn.StageArn"
        ] = None,
        filter_by_encoder_configuration_arn: Optional[
            "capo_ivs_realtime.types.encoder_configuration_arn.EncoderConfigurationArn"
        ] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_composition_results.MaxCompositionResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.list_compositions_response.ListCompositionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_compositions(
                config_overrides=config_overrides,
                filter_by_stage_arn=filter_by_stage_arn,
                filter_by_encoder_configuration_arn=filter_by_encoder_configuration_arn,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_encoder_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_encoder_configuration_results.MaxEncoderConfigurationResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_encoder_configurations_response.ListEncoderConfigurationsResponse":
        """<p>Gets summary information about all EncoderConfigurations in your account, in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first encoder configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 100.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_encoder_configurations_request.ListEncoderConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_encoder_configurations_response.ListEncoderConfigurationsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_encoder_configurations

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_encoder_configurations.async_list_encoder_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_encoder_configurations_request.ListEncoderConfigurationsRequest = {}
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

    async def iter_list_encoder_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_encoder_configuration_results.MaxEncoderConfigurationResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.list_encoder_configurations_response.ListEncoderConfigurationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_encoder_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ingest_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        filter_by_stage_arn: Optional[
            "capo_ivs_realtime.types.stage_arn.StageArn"
        ] = None,
        filter_by_state: Optional[
            "capo_ivs_realtime.types.ingest_configuration_state.IngestConfigurationState"
        ] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_ingest_configuration_results.MaxIngestConfigurationResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_ingest_configurations_response.ListIngestConfigurationsResponse":
        """<p>Lists all IngestConfigurations in your account, in the AWS region where the API request is processed.</p>

        Args:
            filter_by_stage_arn: <p>Filters the response list to match the specified stage ARN. Only one filter (by stage ARN or by state) can be used at a time.</p>
            filter_by_state: <p>Filters the response list to match the specified state. Only one filter (by stage ARN or by state) can be used at a time.</p>
            next_token: <p>The first IngestConfiguration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_ingest_configurations_request.ListIngestConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_ingest_configurations_response.ListIngestConfigurationsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_ingest_configurations

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_ingest_configurations.async_list_ingest_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_ingest_configurations_request.ListIngestConfigurationsRequest = {}
        if filter_by_stage_arn is not None:
            input_["filter_by_stage_arn"] = filter_by_stage_arn
        if filter_by_state is not None:
            input_["filter_by_state"] = filter_by_state
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

    async def iter_list_ingest_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        filter_by_stage_arn: Optional[
            "capo_ivs_realtime.types.stage_arn.StageArn"
        ] = None,
        filter_by_state: Optional[
            "capo_ivs_realtime.types.ingest_configuration_state.IngestConfigurationState"
        ] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_ingest_configuration_results.MaxIngestConfigurationResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.ingest_configuration_summary.IngestConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_ingest_configurations(
                config_overrides=config_overrides,
                filter_by_stage_arn=filter_by_stage_arn,
                filter_by_state=filter_by_state,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("ingest_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_participant_events(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_participant_event_results.MaxParticipantEventResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_participant_events_response.ListParticipantEventsResponse":
        """<p>Lists events for a specified participant that occurred during a specified stage session.</p>

        Args:
            stage_arn: <p>Stage ARN.</p>
            session_id: <p>ID of a session within the stage.</p>
            participant_id: <p>Unique identifier for this participant. This is assigned by IVS and returned by <a>CreateParticipantToken</a>.</p>
            next_token: <p>The first participant event to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_participant_events_request.ListParticipantEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_participant_events_response.ListParticipantEventsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_participant_events

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_participant_events.async_list_participant_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_participant_events_request.ListParticipantEventsRequest = {
            "stage_arn": stage_arn,
            "session_id": session_id,
            "participant_id": participant_id,
        }
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

    async def iter_list_participant_events(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_participant_event_results.MaxParticipantEventResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.list_participant_events_response.ListParticipantEventsResponse]":
        _token = next_token
        while True:
            _response = await self.list_participant_events(
                stage_arn,
                session_id,
                participant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_participant_replicas(
        self,
        source_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_participant_replica_results.MaxParticipantReplicaResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_participant_replicas_response.ListParticipantReplicasResponse":
        """<p>Lists all the replicas for a participant from a source stage.</p>

        Args:
            source_stage_arn: <p>ARN of the stage where the participant is publishing.</p>
            participant_id: <p>Participant ID of the publisher that has been replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed">create a self signed token</a>.</p>
            next_token: <p>The first participant to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_participant_replicas_request.ListParticipantReplicasRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_participant_replicas_response.ListParticipantReplicasResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_participant_replicas

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_participant_replicas.async_list_participant_replicas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_participant_replicas_request.ListParticipantReplicasRequest = {
            "source_stage_arn": source_stage_arn,
            "participant_id": participant_id,
        }
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

    async def iter_list_participant_replicas(
        self,
        source_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_participant_replica_results.MaxParticipantReplicaResults"
        ] = None,
    ) -> (
        "AsyncIterator[capo_ivs_realtime.types.participant_replica.ParticipantReplica]"
    ):
        _token = next_token
        while True:
            _response = await self.list_participant_replicas(
                source_stage_arn,
                participant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("replicas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_participants(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        filter_by_user_id: Optional["capo_ivs_realtime.types.user_id.UserId"] = None,
        filter_by_published: Optional[
            "capo_ivs_realtime.types.published.Published"
        ] = None,
        filter_by_state: Optional[
            "capo_ivs_realtime.types.participant_state.ParticipantState"
        ] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_participant_results.MaxParticipantResults"
        ] = None,
        filter_by_recording_state: Optional[
            "capo_ivs_realtime.types.participant_recording_filter_by_recording_state.ParticipantRecordingFilterByRecordingState"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_participants_response.ListParticipantsResponse":
        """<p>Lists all participants in a specified stage session.</p>

        Args:
            stage_arn: <p>Stage ARN.</p>
            session_id: <p>ID of the session within the stage.</p>
            filter_by_user_id: <p>Filters the response list to match the specified user ID. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request. A <code>userId</code> is a customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems.</p>
            filter_by_published: <p>Filters the response list to only show participants who published during the stage session. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request.</p>
            filter_by_state: <p>Filters the response list to only show participants in the specified state. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request.</p>
            next_token: <p>The first participant to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>
            filter_by_recording_state: <p>Filters the response list to only show participants with the specified recording state. Only one of <code>filterByUserId</code>, <code>filterByPublished</code>, <code>filterByState</code>, or <code>filterByRecordingState</code> can be provided per request.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_participants_request.ListParticipantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_participants_response.ListParticipantsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_participants

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_participants.async_list_participants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_participants_request.ListParticipantsRequest = {
            "stage_arn": stage_arn,
            "session_id": session_id,
        }
        if filter_by_user_id is not None:
            input_["filter_by_user_id"] = filter_by_user_id
        if filter_by_published is not None:
            input_["filter_by_published"] = filter_by_published
        if filter_by_state is not None:
            input_["filter_by_state"] = filter_by_state
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter_by_recording_state is not None:
            input_["filter_by_recording_state"] = filter_by_recording_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_participants(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        session_id: "capo_ivs_realtime.types.stage_session_id.StageSessionId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        filter_by_user_id: Optional["capo_ivs_realtime.types.user_id.UserId"] = None,
        filter_by_published: Optional[
            "capo_ivs_realtime.types.published.Published"
        ] = None,
        filter_by_state: Optional[
            "capo_ivs_realtime.types.participant_state.ParticipantState"
        ] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_participant_results.MaxParticipantResults"
        ] = None,
        filter_by_recording_state: Optional[
            "capo_ivs_realtime.types.participant_recording_filter_by_recording_state.ParticipantRecordingFilterByRecordingState"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.list_participants_response.ListParticipantsResponse]":
        _token = next_token
        while True:
            _response = await self.list_participants(
                stage_arn,
                session_id,
                config_overrides=config_overrides,
                filter_by_user_id=filter_by_user_id,
                filter_by_published=filter_by_published,
                filter_by_state=filter_by_state,
                next_token=_token,
                max_results=max_results,
                filter_by_recording_state=filter_by_recording_state,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_public_keys(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_public_key_results.MaxPublicKeyResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_public_keys_response.ListPublicKeysResponse":
        """<p>Gets summary information about all public keys in your account, in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first public key to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_public_keys_request.ListPublicKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_public_keys_response.ListPublicKeysResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_public_keys

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_public_keys.async_list_public_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_public_keys_request.ListPublicKeysRequest = {}
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

    async def iter_list_public_keys(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_public_key_results.MaxPublicKeyResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.public_key_summary.PublicKeySummary]":
        _token = next_token
        while True:
            _response = await self.list_public_keys(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("public_keys",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_stages(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_stage_results.MaxStageResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_stages_response.ListStagesResponse":
        """<p>Gets summary information about all stages in your account, in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first stage to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_stages_request.ListStagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_stages_response.ListStagesResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_stages

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_stages.async_list_stages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_stages_request.ListStagesRequest = {}
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

    async def iter_list_stages(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_stage_results.MaxStageResults"
        ] = None,
    ) -> (
        "AsyncIterator[capo_ivs_realtime.types.list_stages_response.ListStagesResponse]"
    ):
        _token = next_token
        while True:
            _response = await self.list_stages(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_stage_sessions(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_stage_session_results.MaxStageSessionResults"
        ] = None,
    ) -> (
        "capo_ivs_realtime.types.list_stage_sessions_response.ListStageSessionsResponse"
    ):
        """<p>Gets all sessions for a specified stage.</p>

        Args:
            stage_arn: <p>Stage ARN.</p>
            next_token: <p>The first stage session to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of results to return. Default: 50.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_stage_sessions_request.ListStageSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_stage_sessions_response.ListStageSessionsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_stage_sessions

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_stage_sessions.async_list_stage_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_stage_sessions_request.ListStageSessionsRequest = {
            "stage_arn": stage_arn
        }
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

    async def iter_list_stage_sessions(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_stage_session_results.MaxStageSessionResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.list_stage_sessions_response.ListStageSessionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_stage_sessions(
                stage_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_storage_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_storage_configuration_results.MaxStorageConfigurationResults"
        ] = None,
    ) -> "capo_ivs_realtime.types.list_storage_configurations_response.ListStorageConfigurationsResponse":
        """<p>Gets summary information about all storage configurations in your account, in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first storage configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of storage configurations to return. Default: your service quota or 100, whichever is smaller.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_storage_configurations_request.ListStorageConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_storage_configurations_response.ListStorageConfigurationsResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_storage_configurations

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_storage_configurations.async_list_storage_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_storage_configurations_request.ListStorageConfigurationsRequest = {}
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

    async def iter_list_storage_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        next_token: Optional[
            "capo_ivs_realtime.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivs_realtime.types.max_storage_configuration_results.MaxStorageConfigurationResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivs_realtime.types.list_storage_configurations_response.ListStorageConfigurationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_storage_configurations(
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
        resource_arn: "capo_ivs_realtime.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets information about AWS tags for the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be retrieved. The ARN must be URL-encoded.</p>

        Raises:
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_composition(
        self,
        stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        destinations: "capo_ivs_realtime.types.destination_configuration_list.DestinationConfigurationList",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        idempotency_token: Optional[
            "capo_ivs_realtime.types.composition_client_token.CompositionClientToken"
        ] = None,
        layout: Optional[
            "capo_ivs_realtime.types.layout_configuration.LayoutConfiguration"
        ] = None,
        tags: Optional["capo_ivs_realtime.types.tags.Tags"] = None,
    ) -> "capo_ivs_realtime.types.start_composition_response.StartCompositionResponse":
        """<p>Starts a Composition from a stage based on the configuration provided in the request.</p> <p>A Composition is an ephemeral resource that exists after this operation returns successfully. Composition stops and the resource is deleted:</p> <ul> <li> <p>When <a>StopComposition</a> is called.</p> </li> <li> <p>After a 1-minute timeout, when all participants are disconnected from the stage.</p> </li> <li> <p>After a 1-minute timeout, if there are no participants in the stage when StartComposition is called.</p> </li> <li> <p>When broadcasting to the IVS channel fails and all retries are exhausted.</p> </li> <li> <p>When broadcasting is disconnected and all attempts to reconnect are exhausted.</p> </li> </ul>

        Args:
            stage_arn: <p>ARN of the stage to be used for compositing.</p>
            idempotency_token: <p>Idempotency token.</p>
            layout: <p>Layout object to configure composition parameters.</p>
            destinations: <p>Array of destination configuration.</p>
            tags: <p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.start_composition_request.StartCompositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.start_composition_response.StartCompositionResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.start_composition

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.start_composition.async_start_composition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.start_composition_request.StartCompositionRequest = {
            "stage_arn": stage_arn,
            "destinations": destinations,
        }
        if idempotency_token is None:
            idempotency_token = str(uuid.uuid4())
        input_["idempotency_token"] = idempotency_token
        if layout is not None:
            input_["layout"] = layout
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_participant_replication(
        self,
        source_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        destination_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        reconnect_window_seconds: Optional[
            "capo_ivs_realtime.types.reconnect_window_seconds.ReconnectWindowSeconds"
        ] = None,
        attributes: Optional[
            "capo_ivs_realtime.types.participant_attributes.ParticipantAttributes"
        ] = None,
    ) -> "capo_ivs_realtime.types.start_participant_replication_response.StartParticipantReplicationResponse":
        """<p>Starts replicating a publishing participant from a source stage to a destination stage.</p>

        Args:
            source_stage_arn: <p>ARN of the stage where the participant is publishing.</p>
            destination_stage_arn: <p>ARN of the stage to which the participant will be replicated.</p>
            participant_id: <p>Participant ID of the publisher that will be replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed">create a self signed token</a>. </p>
            reconnect_window_seconds: <p>If the participant disconnects and then reconnects within the specified interval, replication will continue to be <code>ACTIVE</code>. Default: 0.</p>
            attributes: <p>Application-provided attributes to set on the replicated participant in the destination stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p> <p>These attributes are merged with any attributes set for this participant when creating the token. If there is overlap in keys, the values in these attributes are replaced.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.start_participant_replication_request.StartParticipantReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.start_participant_replication_response.StartParticipantReplicationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.start_participant_replication

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.start_participant_replication.async_start_participant_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.start_participant_replication_request.StartParticipantReplicationRequest = {
            "source_stage_arn": source_stage_arn,
            "destination_stage_arn": destination_stage_arn,
            "participant_id": participant_id,
        }
        if reconnect_window_seconds is not None:
            input_["reconnect_window_seconds"] = reconnect_window_seconds
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_composition(
        self,
        arn: "capo_ivs_realtime.types.composition_arn.CompositionArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.stop_composition_response.StopCompositionResponse":
        """<p>Stops and deletes a Composition resource. Any broadcast from the Composition resource is stopped.</p>

        Args:
            arn: <p>ARN of the Composition.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.stop_composition_request.StopCompositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.stop_composition_response.StopCompositionResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.stop_composition

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.stop_composition.async_stop_composition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.stop_composition_request.StopCompositionRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_participant_replication(
        self,
        source_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        destination_stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        participant_id: "capo_ivs_realtime.types.participant_id.ParticipantId",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.stop_participant_replication_response.StopParticipantReplicationResponse":
        """<p>Stops a replicated participant session.</p>

        Args:
            source_stage_arn: <p>ARN of the stage where the participant is publishing.</p>
            destination_stage_arn: <p>ARN of the stage where the participant has been replicated.</p>
            participant_id: <p>Participant ID of the publisher that has been replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href="https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed"> create a self signed token</a>.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.stop_participant_replication_request.StopParticipantReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.stop_participant_replication_response.StopParticipantReplicationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.stop_participant_replication

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.stop_participant_replication.async_stop_participant_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.stop_participant_replication_request.StopParticipantReplicationRequest = {
            "source_stage_arn": source_stage_arn,
            "destination_stage_arn": destination_stage_arn,
            "participant_id": participant_id,
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
        resource_arn: "capo_ivs_realtime.types.resource_arn.ResourceArn",
        tags: "capo_ivs_realtime.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for the AWS resource with the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged. The ARN must be URL-encoded.</p>
            tags: <p>Array of tags to be added or updated. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.tag_resource

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_ivs_realtime.types.resource_arn.ResourceArn",
        tag_keys: "capo_ivs_realtime.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
    ) -> "capo_ivs_realtime.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the resource with the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be untagged. The ARN must be URL-encoded.</p>
            tag_keys: <p>Array of tag keys (strings) for the tags to be removed. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivs_realtime.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.untag_resource

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_ingest_configuration(
        self,
        arn: "capo_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        stage_arn: Optional[
            "capo_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
        ] = None,
        redundant_ingest: Optional[
            "capo_ivs_realtime.types.redundant_ingest.RedundantIngest"
        ] = None,
    ) -> "capo_ivs_realtime.types.update_ingest_configuration_response.UpdateIngestConfigurationResponse":
        """<p>Updates a specified IngestConfiguration. Only the stage ARN attached to the IngestConfiguration can be updated. An IngestConfiguration that is active cannot be updated.</p>

        Args:
            arn: <p>ARN of the IngestConfiguration, for which the related stage ARN needs to be updated.</p>
            stage_arn: <p>Stage ARN that needs to be updated.</p>
            redundant_ingest: <p>Indicates whether redundant ingest is enabled for the ingest configuration. Default: <code>false</code>. </p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.update_ingest_configuration_request.UpdateIngestConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.update_ingest_configuration_response.UpdateIngestConfigurationResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.update_ingest_configuration

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.update_ingest_configuration.async_update_ingest_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.update_ingest_configuration_request.UpdateIngestConfigurationRequest = {
            "arn": arn
        }
        if stage_arn is not None:
            input_["stage_arn"] = stage_arn
        if redundant_ingest is not None:
            input_["redundant_ingest"] = redundant_ingest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_stage(
        self,
        arn: "capo_ivs_realtime.types.stage_arn.StageArn",
        *,
        config_overrides: Optional[AsyncIVSRealTimeClientConfig] = None,
        name: Optional["capo_ivs_realtime.types.stage_name.StageName"] = None,
        auto_participant_recording_configuration: Optional[
            "capo_ivs_realtime.types.auto_participant_recording_configuration.AutoParticipantRecordingConfiguration"
        ] = None,
    ) -> "capo_ivs_realtime.types.update_stage_response.UpdateStageResponse":
        """<p>Updates a stage’s configuration.</p>

        Args:
            arn: <p>ARN of the stage to be updated.</p>
            name: <p>Name of the stage to be updated.</p>
            auto_participant_recording_configuration: <p>Configuration object for individual participant recording, to attach to the stage. Note that this cannot be updated while recording is active.</p>

        Raises:
            capo_ivs_realtime.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs_realtime.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs_realtime.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs_realtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs_realtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs_realtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs_realtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivs_realtime.types.update_stage_request.UpdateStageRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivs_realtime.types.update_stage_response.UpdateStageResponse"
        ]:
            import capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.update_stage

            (
                output,
                http_response,
            ) = await capo_ivs_realtime._operations.amazon_interactive_video_service_real_time.update_stage.async_update_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs_realtime.types.update_stage_request.UpdateStageRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if auto_participant_recording_configuration is not None:
            input_["auto_participant_recording_configuration"] = (
                auto_participant_recording_configuration
            )

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
