"""Generated from Smithy shape ``com.amazonaws.ivs#AmazonInteractiveVideoService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ivs._auth._signers
import capo_ivs._auth._sigv4
from capo_ivs._auth._identity import Credentials
from capo_ivs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ivs._auth._zapros_handler import AuthMiddleware
from capo_ivs._pagination import resolve_path as _resolve_path
from capo_ivs._services._aws_config import aws_config
from capo_ivs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_arn
    import capo_ivs.types.ad_configuration_name
    import capo_ivs.types.ad_configuration_summary
    import capo_ivs.types.ad_duration_seconds
    import capo_ivs.types.batch_get_channel_request
    import capo_ivs.types.batch_get_channel_response
    import capo_ivs.types.batch_get_stream_key_request
    import capo_ivs.types.batch_get_stream_key_response
    import capo_ivs.types.batch_start_viewer_session_revocation_request
    import capo_ivs.types.batch_start_viewer_session_revocation_response
    import capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list
    import capo_ivs.types.boolean
    import capo_ivs.types.channel_ad_configuration_arn
    import capo_ivs.types.channel_arn
    import capo_ivs.types.channel_arn_list
    import capo_ivs.types.channel_latency_mode
    import capo_ivs.types.channel_name
    import capo_ivs.types.channel_playback_restriction_policy_arn
    import capo_ivs.types.channel_recording_configuration_arn
    import capo_ivs.types.channel_type
    import capo_ivs.types.container_format
    import capo_ivs.types.create_ad_configuration_request
    import capo_ivs.types.create_ad_configuration_response
    import capo_ivs.types.create_channel_request
    import capo_ivs.types.create_channel_response
    import capo_ivs.types.create_playback_restriction_policy_request
    import capo_ivs.types.create_playback_restriction_policy_response
    import capo_ivs.types.create_recording_configuration_request
    import capo_ivs.types.create_recording_configuration_response
    import capo_ivs.types.create_stream_key_request
    import capo_ivs.types.create_stream_key_response
    import capo_ivs.types.delete_ad_configuration_request
    import capo_ivs.types.delete_channel_request
    import capo_ivs.types.delete_playback_key_pair_request
    import capo_ivs.types.delete_playback_key_pair_response
    import capo_ivs.types.delete_playback_restriction_policy_request
    import capo_ivs.types.delete_recording_configuration_request
    import capo_ivs.types.delete_stream_key_request
    import capo_ivs.types.destination_configuration
    import capo_ivs.types.get_ad_configuration_request
    import capo_ivs.types.get_ad_configuration_response
    import capo_ivs.types.get_channel_request
    import capo_ivs.types.get_channel_response
    import capo_ivs.types.get_playback_key_pair_request
    import capo_ivs.types.get_playback_key_pair_response
    import capo_ivs.types.get_playback_restriction_policy_request
    import capo_ivs.types.get_playback_restriction_policy_response
    import capo_ivs.types.get_recording_configuration_request
    import capo_ivs.types.get_recording_configuration_response
    import capo_ivs.types.get_stream_key_request
    import capo_ivs.types.get_stream_key_response
    import capo_ivs.types.get_stream_request
    import capo_ivs.types.get_stream_response
    import capo_ivs.types.get_stream_session_request
    import capo_ivs.types.get_stream_session_response
    import capo_ivs.types.import_playback_key_pair_request
    import capo_ivs.types.import_playback_key_pair_response
    import capo_ivs.types.insert_ad_break_request
    import capo_ivs.types.insert_ad_break_response
    import capo_ivs.types.list_ad_configurations_request
    import capo_ivs.types.list_ad_configurations_response
    import capo_ivs.types.list_channels_request
    import capo_ivs.types.list_channels_response
    import capo_ivs.types.list_playback_key_pairs_request
    import capo_ivs.types.list_playback_key_pairs_response
    import capo_ivs.types.list_playback_restriction_policies_request
    import capo_ivs.types.list_playback_restriction_policies_response
    import capo_ivs.types.list_recording_configurations_request
    import capo_ivs.types.list_recording_configurations_response
    import capo_ivs.types.list_stream_keys_request
    import capo_ivs.types.list_stream_keys_response
    import capo_ivs.types.list_stream_sessions_request
    import capo_ivs.types.list_stream_sessions_response
    import capo_ivs.types.list_streams_request
    import capo_ivs.types.list_streams_response
    import capo_ivs.types.list_tags_for_resource_request
    import capo_ivs.types.list_tags_for_resource_response
    import capo_ivs.types.max_ad_configuration_results
    import capo_ivs.types.max_channel_results
    import capo_ivs.types.max_playback_key_pair_results
    import capo_ivs.types.max_playback_restriction_policy_results
    import capo_ivs.types.max_recording_configuration_results
    import capo_ivs.types.max_stream_key_results
    import capo_ivs.types.max_stream_results
    import capo_ivs.types.media_tailor_playback_configurations_list
    import capo_ivs.types.multitrack_input_configuration
    import capo_ivs.types.pagination_token
    import capo_ivs.types.playback_key_pair_arn
    import capo_ivs.types.playback_key_pair_name
    import capo_ivs.types.playback_public_key_material
    import capo_ivs.types.playback_restriction_policy_allowed_country_list
    import capo_ivs.types.playback_restriction_policy_allowed_origin_list
    import capo_ivs.types.playback_restriction_policy_arn
    import capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement
    import capo_ivs.types.playback_restriction_policy_name
    import capo_ivs.types.post_roll_configuration
    import capo_ivs.types.put_metadata_request
    import capo_ivs.types.recording_configuration_arn
    import capo_ivs.types.recording_configuration_name
    import capo_ivs.types.recording_reconnect_window_seconds
    import capo_ivs.types.rendition_configuration
    import capo_ivs.types.resource_arn
    import capo_ivs.types.start_viewer_session_revocation_request
    import capo_ivs.types.start_viewer_session_revocation_response
    import capo_ivs.types.stop_stream_request
    import capo_ivs.types.stop_stream_response
    import capo_ivs.types.stream_filters
    import capo_ivs.types.stream_id
    import capo_ivs.types.stream_key_arn
    import capo_ivs.types.stream_key_arn_list
    import capo_ivs.types.stream_metadata
    import capo_ivs.types.tag_key_list
    import capo_ivs.types.tag_resource_request
    import capo_ivs.types.tag_resource_response
    import capo_ivs.types.tags
    import capo_ivs.types.thumbnail_configuration
    import capo_ivs.types.transcode_preset
    import capo_ivs.types.untag_resource_request
    import capo_ivs.types.untag_resource_response
    import capo_ivs.types.update_ad_configuration_request
    import capo_ivs.types.update_ad_configuration_response
    import capo_ivs.types.update_channel_request
    import capo_ivs.types.update_channel_response
    import capo_ivs.types.update_playback_restriction_policy_request
    import capo_ivs.types.update_playback_restriction_policy_response
    import capo_ivs.types.viewer_id
    import capo_ivs.types.viewer_session_version


class ivsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ivsClient:
    """A client for the ``ivs`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = ivsClientConfig(
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
        self, config_overrides: Optional[ivsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ivsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def batch_get_channel(
        self,
        arns: "capo_ivs.types.channel_arn_list.ChannelArnList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.batch_get_channel_response.BatchGetChannelResponse":
        """<p>Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p>

        Args:
            arns: <p>Array of ARNs, one per channel.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.service_unavailable.ServiceUnavailable: <p>The service is temporarily unavailable.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.batch_get_channel_request.BatchGetChannelRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.batch_get_channel_response.BatchGetChannelResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.batch_get_channel

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.batch_get_channel.batch_get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.batch_get_channel_request.BatchGetChannelRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_stream_key(
        self,
        arns: "capo_ivs.types.stream_key_arn_list.StreamKeyArnList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.batch_get_stream_key_response.BatchGetStreamKeyResponse":
        """<p>Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p>

        Args:
            arns: <p>Array of ARNs, one per stream key.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.service_unavailable.ServiceUnavailable: <p>The service is temporarily unavailable.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.batch_get_stream_key_request.BatchGetStreamKeyRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.batch_get_stream_key_response.BatchGetStreamKeyResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.batch_get_stream_key

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.batch_get_stream_key.batch_get_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.batch_get_stream_key_request.BatchGetStreamKeyRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_start_viewer_session_revocation(
        self,
        viewer_sessions: "capo_ivs.types.batch_start_viewer_session_revocation_viewer_session_list.BatchStartViewerSessionRevocationViewerSessionList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse":
        """<p>Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p>

        Args:
            viewer_sessions: <p>Array of viewer sessions, one per channel-ARN and viewer-ID pair.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.batch_start_viewer_session_revocation_response.BatchStartViewerSessionRevocationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.batch_start_viewer_session_revocation

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.batch_start_viewer_session_revocation.batch_start_viewer_session_revocation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.batch_start_viewer_session_revocation_request.BatchStartViewerSessionRevocationRequest = {
            "viewer_sessions": viewer_sessions
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_ad_configuration(
        self,
        media_tailor_playback_configurations: "capo_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "capo_ivs.types.ad_configuration_name.AdConfigurationName"
        ] = None,
        post_roll_configuration: Optional[
            "capo_ivs.types.post_roll_configuration.PostRollConfiguration"
        ] = None,
        tags: Optional["capo_ivs.types.tags.Tags"] = None,
    ) -> (
        "capo_ivs.types.create_ad_configuration_response.CreateAdConfigurationResponse"
    ):
        """<p>Creates a new ad configuration to be used for server-side ad insertion.</p>

        Args:
            name: <p>Ad configuration name. Defaults to “”.</p>
            media_tailor_playback_configurations: <p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html">Generate and Sign IVS Playback Tokens</a>.</p>
            post_roll_configuration: <p>Configuration for the post-roll ad break to use for this ad configuration. Default: disabled (<code>enabled</code> set to false, <code>durationSeconds</code> set to 15).</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.create_ad_configuration_request.CreateAdConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.create_ad_configuration_response.CreateAdConfigurationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.create_ad_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.create_ad_configuration.create_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.create_ad_configuration_request.CreateAdConfigurationRequest = {
            "media_tailor_playback_configurations": media_tailor_playback_configurations
        }
        if name is not None:
            input_["name"] = name
        if post_roll_configuration is not None:
            input_["post_roll_configuration"] = post_roll_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional["capo_ivs.types.channel_name.ChannelName"] = None,
        latency_mode: Optional[
            "capo_ivs.types.channel_latency_mode.ChannelLatencyMode"
        ] = None,
        type: Optional["capo_ivs.types.channel_type.ChannelType"] = None,
        authorized: Optional["capo_ivs.types.boolean.Boolean"] = None,
        recording_configuration_arn: Optional[
            "capo_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        tags: Optional["capo_ivs.types.tags.Tags"] = None,
        insecure_ingest: Optional["capo_ivs.types.boolean.Boolean"] = None,
        preset: Optional["capo_ivs.types.transcode_preset.TranscodePreset"] = None,
        playback_restriction_policy_arn: Optional[
            "capo_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        multitrack_input_configuration: Optional[
            "capo_ivs.types.multitrack_input_configuration.MultitrackInputConfiguration"
        ] = None,
        container_format: Optional[
            "capo_ivs.types.container_format.ContainerFormat"
        ] = None,
        ad_configuration_arn: Optional[
            "capo_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
    ) -> "capo_ivs.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a new channel and an associated stream key to start streaming.</p>

        Args:
            name: <p>Channel name.</p>
            latency_mode: <p>Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers. Default: <code>LOW</code>.</p>
            type: <p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html">Channel Types</a>.</p>
            authorized: <p>Whether the channel is private (enabled for playback authorization). Default: <code>false</code>.</p>
            recording_configuration_arn: <p>Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. Default: "" (empty string, recording is disabled).</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
            insecure_ingest: <p>Whether the channel allows insecure RTMP and SRT ingest. Default: <code>false</code>.</p>
            preset: <p>Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>""</code>).</p>
            playback_restriction_policy_arn: <p>Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. Default: "" (empty string, no playback restriction policy is applied).</p>
            multitrack_input_configuration: <p>Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.</p>
            container_format: <p>Indicates which content-packaging format is used (MPEG-TS or fMP4). If <code>multitrackInputConfiguration</code> is specified and <code>enabled</code> is <code>true</code>, then <code>containerFormat</code> is required and must be set to <code>FRAGMENTED_MP4</code>. Otherwise, <code>containerFormat</code> may be set to <code>TS</code> or <code>FRAGMENTED_MP4</code>. Default: <code>TS</code>.</p>
            ad_configuration_arn: <p>ARN of the ad configuration associated with the channel.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.create_channel

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.create_channel_request.CreateChannelRequest = {}
        if name is not None:
            input_["name"] = name
        if latency_mode is not None:
            input_["latency_mode"] = latency_mode
        if type is not None:
            input_["type"] = type
        if authorized is not None:
            input_["authorized"] = authorized
        if recording_configuration_arn is not None:
            input_["recording_configuration_arn"] = recording_configuration_arn
        if tags is not None:
            input_["tags"] = tags
        if insecure_ingest is not None:
            input_["insecure_ingest"] = insecure_ingest
        if preset is not None:
            input_["preset"] = preset
        if playback_restriction_policy_arn is not None:
            input_["playback_restriction_policy_arn"] = playback_restriction_policy_arn
        if multitrack_input_configuration is not None:
            input_["multitrack_input_configuration"] = multitrack_input_configuration
        if container_format is not None:
            input_["container_format"] = container_format
        if ad_configuration_arn is not None:
            input_["ad_configuration_arn"] = ad_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_playback_restriction_policy(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        allowed_countries: Optional[
            "capo_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
        ] = None,
        allowed_origins: Optional[
            "capo_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
        ] = None,
        enable_strict_origin_enforcement: Optional[
            "capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
        ] = None,
        name: Optional[
            "capo_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
        ] = None,
        tags: Optional["capo_ivs.types.tags.Tags"] = None,
    ) -> "capo_ivs.types.create_playback_restriction_policy_response.CreatePlaybackRestrictionPolicyResponse":
        """<p>Creates a new playback restriction policy, for constraining playback by countries and/or origins.</p>

        Args:
            allowed_countries: <p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>
            allowed_origins: <p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>
            enable_strict_origin_enforcement: <p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>
            name: <p>Playback-restriction-policy name. The value does not need to be unique.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.create_playback_restriction_policy_request.CreatePlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.create_playback_restriction_policy_response.CreatePlaybackRestrictionPolicyResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.create_playback_restriction_policy

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.create_playback_restriction_policy.create_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.create_playback_restriction_policy_request.CreatePlaybackRestrictionPolicyRequest = {}
        if allowed_countries is not None:
            input_["allowed_countries"] = allowed_countries
        if allowed_origins is not None:
            input_["allowed_origins"] = allowed_origins
        if enable_strict_origin_enforcement is not None:
            input_["enable_strict_origin_enforcement"] = (
                enable_strict_origin_enforcement
            )
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_recording_configuration(
        self,
        destination_configuration: "capo_ivs.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "capo_ivs.types.recording_configuration_name.RecordingConfigurationName"
        ] = None,
        tags: Optional["capo_ivs.types.tags.Tags"] = None,
        thumbnail_configuration: Optional[
            "capo_ivs.types.thumbnail_configuration.ThumbnailConfiguration"
        ] = None,
        recording_reconnect_window_seconds: Optional[
            "capo_ivs.types.recording_reconnect_window_seconds.RecordingReconnectWindowSeconds"
        ] = None,
        rendition_configuration: Optional[
            "capo_ivs.types.rendition_configuration.RenditionConfiguration"
        ] = None,
    ) -> "capo_ivs.types.create_recording_configuration_response.CreateRecordingConfigurationResponse":
        """<p>Creates a new recording configuration, used to enable recording to Amazon S3.</p> <p> <b>Known issue:</b> In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the <code>state</code> of the recording configuration is <code>CREATE_FAILED</code> (instead of <code>ACTIVE</code>). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)</p> <p> <b>Workaround:</b> Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.</p>

        Args:
            name: <p>Recording-configuration name. The value does not need to be unique.</p>
            destination_configuration: <p>A complex type that contains a destination configuration for where recorded video will be stored.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>
            thumbnail_configuration: <p>A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.</p>
            recording_reconnect_window_seconds: <p>If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.</p>
            rendition_configuration: <p>Object that describes which renditions should be recorded for a stream.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.create_recording_configuration_request.CreateRecordingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.create_recording_configuration_response.CreateRecordingConfigurationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.create_recording_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.create_recording_configuration.create_recording_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.create_recording_configuration_request.CreateRecordingConfigurationRequest = {
            "destination_configuration": destination_configuration
        }
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if thumbnail_configuration is not None:
            input_["thumbnail_configuration"] = thumbnail_configuration
        if recording_reconnect_window_seconds is not None:
            input_["recording_reconnect_window_seconds"] = (
                recording_reconnect_window_seconds
            )
        if rendition_configuration is not None:
            input_["rendition_configuration"] = rendition_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stream_key(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        tags: Optional["capo_ivs.types.tags.Tags"] = None,
    ) -> "capo_ivs.types.create_stream_key_response.CreateStreamKeyResponse":
        """<p>Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> <p>Note that <a>CreateChannel</a> creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use <a>DeleteStreamKey</a> and then CreateStreamKey.</p>

        Args:
            channel_arn: <p>ARN of the channel for which to create the stream key.</p>
            tags: <p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.create_stream_key_request.CreateStreamKeyRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.create_stream_key_response.CreateStreamKeyResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.create_stream_key

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.create_stream_key.create_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.create_stream_key_request.CreateStreamKeyRequest = {
            "channel_arn": channel_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_ad_configuration(
        self,
        arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified ad configuration.</p>

        Args:
            arn: <p>ARN of the ad configuration to be deleted.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.delete_ad_configuration_request.DeleteAdConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_ivs._operations.amazon_interactive_video_service.delete_ad_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.delete_ad_configuration.delete_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.delete_ad_configuration_request.DeleteAdConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel(
        self,
        arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified channel and its associated stream keys.</p> <p>If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call <a>StopStream</a>, wait for the Amazon EventBridge "Stream End" event (to verify that the stream's state is no longer Live), then call DeleteChannel. (See <a href="https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html"> Using EventBridge with Amazon IVS</a>.) </p>

        Args:
            arn: <p>ARN of the channel to be deleted.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[None]:
            import capo_ivs._operations.amazon_interactive_video_service.delete_channel

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.delete_channel_request.DeleteChannelRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_playback_key_pair(
        self,
        arn: "capo_ivs.types.playback_key_pair_arn.PlaybackKeyPairArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> (
        "capo_ivs.types.delete_playback_key_pair_response.DeletePlaybackKeyPairResponse"
    ):
        """<p>Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>. For more information, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            arn: <p>ARN of the key pair to be deleted.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.delete_playback_key_pair_request.DeletePlaybackKeyPairRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.delete_playback_key_pair_response.DeletePlaybackKeyPairResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.delete_playback_key_pair

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.delete_playback_key_pair.delete_playback_key_pair(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.delete_playback_key_pair_request.DeletePlaybackKeyPairRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_playback_restriction_policy(
        self,
        arn: "capo_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified playback restriction policy.</p>

        Args:
            arn: <p>ARN of the playback restriction policy to be deleted.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.delete_playback_restriction_policy_request.DeletePlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_ivs._operations.amazon_interactive_video_service.delete_playback_restriction_policy

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.delete_playback_restriction_policy.delete_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.delete_playback_restriction_policy_request.DeletePlaybackRestrictionPolicyRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recording_configuration(
        self,
        arn: "capo_ivs.types.recording_configuration_arn.RecordingConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the recording configuration for the specified ARN.</p> <p>If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use <a>UpdateChannel</a> to set the <code>recordingConfigurationArn</code> field to an empty string, then use DeleteRecordingConfiguration.</p>

        Args:
            arn: <p>ARN of the recording configuration to be deleted.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.delete_recording_configuration_request.DeleteRecordingConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_ivs._operations.amazon_interactive_video_service.delete_recording_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.delete_recording_configuration.delete_recording_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.delete_recording_configuration_request.DeleteRecordingConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stream_key(
        self,
        arn: "capo_ivs.types.stream_key_arn.StreamKeyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p>

        Args:
            arn: <p>ARN of the stream key to be deleted.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.delete_stream_key_request.DeleteStreamKeyRequest]",
        ) -> OperationResponse[None]:
            import capo_ivs._operations.amazon_interactive_video_service.delete_stream_key

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.delete_stream_key.delete_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.delete_stream_key_request.DeleteStreamKeyRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ad_configuration(
        self,
        arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_ad_configuration_response.GetAdConfigurationResponse":
        """<p>Gets the ad configuration represented by the specified ARN.</p>

        Args:
            arn: <p>ARN of the ad configuration to be retrieved.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_ad_configuration_request.GetAdConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_ad_configuration_response.GetAdConfigurationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_ad_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_ad_configuration.get_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_ad_configuration_request.GetAdConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel(
        self,
        arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_channel_response.GetChannelResponse":
        """<p>Gets the channel configuration for the specified channel ARN. See also <a>BatchGetChannel</a>.</p>

        Args:
            arn: <p>ARN of the channel for which the configuration is to be retrieved.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_channel_request.GetChannelRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_channel_response.GetChannelResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_channel

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_channel.get_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_channel_request.GetChannelRequest = {"arn": arn}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_playback_key_pair(
        self,
        arn: "capo_ivs.types.playback_key_pair_arn.PlaybackKeyPairArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_playback_key_pair_response.GetPlaybackKeyPairResponse":
        """<p>Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            arn: <p>ARN of the key pair to be returned.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_playback_key_pair_request.GetPlaybackKeyPairRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_playback_key_pair_response.GetPlaybackKeyPairResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_playback_key_pair

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_playback_key_pair.get_playback_key_pair(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_playback_key_pair_request.GetPlaybackKeyPairRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_playback_restriction_policy(
        self,
        arn: "capo_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_playback_restriction_policy_response.GetPlaybackRestrictionPolicyResponse":
        """<p>Gets the specified playback restriction policy.</p>

        Args:
            arn: <p>ARN of the playback restriction policy to be returned.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_playback_restriction_policy_request.GetPlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_playback_restriction_policy_response.GetPlaybackRestrictionPolicyResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_playback_restriction_policy

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_playback_restriction_policy.get_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_playback_restriction_policy_request.GetPlaybackRestrictionPolicyRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recording_configuration(
        self,
        arn: "capo_ivs.types.recording_configuration_arn.RecordingConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_recording_configuration_response.GetRecordingConfigurationResponse":
        """<p>Gets the recording configuration for the specified ARN.</p>

        Args:
            arn: <p>ARN of the recording configuration to be retrieved.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_recording_configuration_request.GetRecordingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_recording_configuration_response.GetRecordingConfigurationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_recording_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_recording_configuration.get_recording_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_recording_configuration_request.GetRecordingConfigurationRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stream(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_stream_response.GetStreamResponse":
        """<p>Gets information about the active (live) stream on a specified channel.</p>

        Args:
            channel_arn: <p>Channel ARN for stream to be accessed.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.channel_not_broadcasting.ChannelNotBroadcasting: <p>The stream is offline for the given channel ARN.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_stream_request.GetStreamRequest]",
        ) -> OperationResponse["capo_ivs.types.get_stream_response.GetStreamResponse"]:
            import capo_ivs._operations.amazon_interactive_video_service.get_stream

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_stream.get_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_stream_request.GetStreamRequest = {
            "channel_arn": channel_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stream_key(
        self,
        arn: "capo_ivs.types.stream_key_arn.StreamKeyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.get_stream_key_response.GetStreamKeyResponse":
        """<p>Gets stream-key information for a specified ARN.</p>

        Args:
            arn: <p>ARN for the stream key to be retrieved.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_stream_key_request.GetStreamKeyRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_stream_key_response.GetStreamKeyResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_stream_key

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_stream_key.get_stream_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_stream_key_request.GetStreamKeyRequest = {"arn": arn}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stream_session(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        stream_id: Optional["capo_ivs.types.stream_id.StreamId"] = None,
    ) -> "capo_ivs.types.get_stream_session_response.GetStreamSessionResponse":
        """<p>Gets metadata on a specified stream.</p>

        Args:
            channel_arn: <p>ARN of the channel resource</p>
            stream_id: <p>Unique identifier for a live or previously live stream in the specified channel. If no <code>streamId</code> is provided, this returns the most recent stream session for the channel, if it exists.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.get_stream_session_request.GetStreamSessionRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.get_stream_session_response.GetStreamSessionResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.get_stream_session

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.get_stream_session.get_stream_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.get_stream_session_request.GetStreamSessionRequest = {
            "channel_arn": channel_arn
        }
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_playback_key_pair(
        self,
        public_key_material: "capo_ivs.types.playback_public_key_material.PlaybackPublicKeyMaterial",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "capo_ivs.types.playback_key_pair_name.PlaybackKeyPairName"
        ] = None,
        tags: Optional["capo_ivs.types.tags.Tags"] = None,
    ) -> (
        "capo_ivs.types.import_playback_key_pair_response.ImportPlaybackKeyPairResponse"
    ):
        """<p>Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            public_key_material: <p>The public portion of a customer-generated key pair.</p>
            name: <p>Playback-key-pair name. The value does not need to be unique.</p>
            tags: <p>Any tags provided with the request are added to the playback key pair tags. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.import_playback_key_pair_request.ImportPlaybackKeyPairRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.import_playback_key_pair_response.ImportPlaybackKeyPairResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.import_playback_key_pair

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.import_playback_key_pair.import_playback_key_pair(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.import_playback_key_pair_request.ImportPlaybackKeyPairRequest = {
            "public_key_material": public_key_material
        }
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def insert_ad_break(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        duration_seconds: "capo_ivs.types.ad_duration_seconds.AdDurationSeconds",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.insert_ad_break_response.InsertAdBreakResponse":
        """<p>Inserts an ad marker in the playlist for the specified channel and duration using the ad configuration associated with the channel.</p> <p> <b>Note:</b> AWS Elemental MediaTailor (EMT), the service that handles ad requests, provides CloudWatch metrics to help you monitor the success or failure of each InsertAdBreak operation. See <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch-metrics.html">Monitoring AWS Elemental MediaTailor with Amazon CloudWatch</a> metrics in the <i>AWS Elemental MediaTailor User Guide</i> for details on available metrics.</p>

        Args:
            channel_arn: <p>ARN of the channel into which the ad break is inserted.</p>
            duration_seconds: <p>Duration of the ad break, in seconds.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.channel_not_broadcasting.ChannelNotBroadcasting: <p>The stream is offline for the given channel ARN.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.insert_ad_break_request.InsertAdBreakRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.insert_ad_break_response.InsertAdBreakResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.insert_ad_break

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.insert_ad_break.insert_ad_break(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.insert_ad_break_request.InsertAdBreakRequest = {
            "channel_arn": channel_arn,
            "duration_seconds": duration_seconds,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ad_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_ad_configuration_results.MaxAdConfigurationResults"
        ] = None,
    ) -> "capo_ivs.types.list_ad_configurations_response.ListAdConfigurationsResponse":
        """<p>Gets summary information about all ad configurations in your account, in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first ad configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of ad configurations to return. Default: your service quota or 100, whichever is smaller.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_ad_configurations_request.ListAdConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_ad_configurations_response.ListAdConfigurationsResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_ad_configurations

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_ad_configurations.list_ad_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_ad_configurations_request.ListAdConfigurationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_ad_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_ad_configuration_results.MaxAdConfigurationResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.ad_configuration_summary.AdConfigurationSummary]":
        _token = next_token
        while True:
            _response = self.list_ad_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("ad_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        filter_by_name: Optional["capo_ivs.types.channel_name.ChannelName"] = None,
        filter_by_recording_configuration_arn: Optional[
            "capo_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        filter_by_playback_restriction_policy_arn: Optional[
            "capo_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        filter_by_ad_configuration_arn: Optional[
            "capo_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_channel_results.MaxChannelResults"
        ] = None,
    ) -> "capo_ivs.types.list_channels_response.ListChannelsResponse":
        """<p>Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).</p>

        Args:
            filter_by_name: <p>Filters the channel list to match the specified name.</p>
            filter_by_recording_configuration_arn: <p>Filters the channel list to match the specified recording-configuration ARN.</p>
            filter_by_playback_restriction_policy_arn: <p>Filters the channel list to match the specified policy.</p>
            filter_by_ad_configuration_arn: <p>Filters the channel list to match the specified ad configuration ARN.</p>
            next_token: <p>The first channel to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of channels to return. Default: 100.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_channels

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_channels_request.ListChannelsRequest = {}
        if filter_by_name is not None:
            input_["filter_by_name"] = filter_by_name
        if filter_by_recording_configuration_arn is not None:
            input_["filter_by_recording_configuration_arn"] = (
                filter_by_recording_configuration_arn
            )
        if filter_by_playback_restriction_policy_arn is not None:
            input_["filter_by_playback_restriction_policy_arn"] = (
                filter_by_playback_restriction_policy_arn
            )
        if filter_by_ad_configuration_arn is not None:
            input_["filter_by_ad_configuration_arn"] = filter_by_ad_configuration_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channels(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        filter_by_name: Optional["capo_ivs.types.channel_name.ChannelName"] = None,
        filter_by_recording_configuration_arn: Optional[
            "capo_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        filter_by_playback_restriction_policy_arn: Optional[
            "capo_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        filter_by_ad_configuration_arn: Optional[
            "capo_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_channel_results.MaxChannelResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_channels_response.ListChannelsResponse]":
        _token = next_token
        while True:
            _response = self.list_channels(
                config_overrides=config_overrides,
                filter_by_name=filter_by_name,
                filter_by_recording_configuration_arn=filter_by_recording_configuration_arn,
                filter_by_playback_restriction_policy_arn=filter_by_playback_restriction_policy_arn,
                filter_by_ad_configuration_arn=filter_by_ad_configuration_arn,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_playback_key_pairs(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_playback_key_pair_results.MaxPlaybackKeyPairResults"
        ] = None,
    ) -> "capo_ivs.types.list_playback_key_pairs_response.ListPlaybackKeyPairsResponse":
        """<p>Gets summary information about playback key pairs. For more information, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            next_token: <p>The first key pair to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of key pairs to return. Default: your service quota or 100, whichever is smaller.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_playback_key_pairs_request.ListPlaybackKeyPairsRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_playback_key_pairs_response.ListPlaybackKeyPairsResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_playback_key_pairs

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_playback_key_pairs.list_playback_key_pairs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_playback_key_pairs_request.ListPlaybackKeyPairsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_playback_key_pairs(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_playback_key_pair_results.MaxPlaybackKeyPairResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_playback_key_pairs_response.ListPlaybackKeyPairsResponse]":
        _token = next_token
        while True:
            _response = self.list_playback_key_pairs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_playback_restriction_policies(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_playback_restriction_policy_results.MaxPlaybackRestrictionPolicyResults"
        ] = None,
    ) -> "capo_ivs.types.list_playback_restriction_policies_response.ListPlaybackRestrictionPoliciesResponse":
        """<p>Gets summary information about playback restriction policies.</p>

        Args:
            next_token: <p>The first policy to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of policies to return. Default: 1.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_playback_restriction_policies_request.ListPlaybackRestrictionPoliciesRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_playback_restriction_policies_response.ListPlaybackRestrictionPoliciesResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_playback_restriction_policies

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_playback_restriction_policies.list_playback_restriction_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_playback_restriction_policies_request.ListPlaybackRestrictionPoliciesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_playback_restriction_policies(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_playback_restriction_policy_results.MaxPlaybackRestrictionPolicyResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_playback_restriction_policies_response.ListPlaybackRestrictionPoliciesResponse]":
        _token = next_token
        while True:
            _response = self.list_playback_restriction_policies(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recording_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_recording_configuration_results.MaxRecordingConfigurationResults"
        ] = None,
    ) -> "capo_ivs.types.list_recording_configurations_response.ListRecordingConfigurationsResponse":
        """<p>Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p>

        Args:
            next_token: <p>The first recording configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of recording configurations to return. Default: your service quota or 100, whichever is smaller. </p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_recording_configurations_request.ListRecordingConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_recording_configurations_response.ListRecordingConfigurationsResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_recording_configurations

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_recording_configurations.list_recording_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_recording_configurations_request.ListRecordingConfigurationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recording_configurations(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_recording_configuration_results.MaxRecordingConfigurationResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_recording_configurations_response.ListRecordingConfigurationsResponse]":
        _token = next_token
        while True:
            _response = self.list_recording_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stream_keys(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_stream_key_results.MaxStreamKeyResults"
        ] = None,
    ) -> "capo_ivs.types.list_stream_keys_response.ListStreamKeysResponse":
        """<p>Gets summary information about stream keys for the specified channel.</p>

        Args:
            channel_arn: <p>Channel ARN used to filter the list.</p>
            next_token: <p>The first stream key to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of streamKeys to return. Default: 1.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_stream_keys_request.ListStreamKeysRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_stream_keys_response.ListStreamKeysResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_stream_keys

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_stream_keys.list_stream_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_stream_keys_request.ListStreamKeysRequest = {
            "channel_arn": channel_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stream_keys(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_stream_key_results.MaxStreamKeyResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_stream_keys_response.ListStreamKeysResponse]":
        _token = next_token
        while True:
            _response = self.list_stream_keys(
                channel_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_streams(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        filter_by: Optional["capo_ivs.types.stream_filters.StreamFilters"] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_stream_results.MaxStreamResults"
        ] = None,
    ) -> "capo_ivs.types.list_streams_response.ListStreamsResponse":
        """<p>Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p>

        Args:
            filter_by: <p>Filters the stream list to match the specified criterion.</p>
            next_token: <p>The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of streams to return. Default: 100.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_streams_request.ListStreamsRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_streams_response.ListStreamsResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_streams

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_streams_request.ListStreamsRequest = {}
        if filter_by is not None:
            input_["filter_by"] = filter_by
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_streams(
        self,
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        filter_by: Optional["capo_ivs.types.stream_filters.StreamFilters"] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_stream_results.MaxStreamResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_streams_response.ListStreamsResponse]":
        _token = next_token
        while True:
            _response = self.list_streams(
                config_overrides=config_overrides,
                filter_by=filter_by,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stream_sessions(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_stream_results.MaxStreamResults"
        ] = None,
    ) -> "capo_ivs.types.list_stream_sessions_response.ListStreamSessionsResponse":
        """<p>Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p>

        Args:
            channel_arn: <p>Channel ARN used to filter the list.</p>
            next_token: <p>The first stream to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of streams to return. Default: 100.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_stream_sessions_request.ListStreamSessionsRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_stream_sessions_response.ListStreamSessionsResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_stream_sessions

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_stream_sessions.list_stream_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_stream_sessions_request.ListStreamSessionsRequest = {
            "channel_arn": channel_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stream_sessions(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        next_token: Optional["capo_ivs.types.pagination_token.PaginationToken"] = None,
        max_results: Optional[
            "capo_ivs.types.max_stream_results.MaxStreamResults"
        ] = None,
    ) -> "Iterator[capo_ivs.types.list_stream_sessions_response.ListStreamSessionsResponse]":
        _token = next_token
        while True:
            _response = self.list_stream_sessions(
                channel_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_ivs.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets information about Amazon Web Services tags for the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be retrieved. The ARN must be URL-encoded.</p>

        Raises:
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.list_tags_for_resource

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_metadata(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        metadata: "capo_ivs.types.stream_metadata.StreamMetadata",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> None:
        """<p>Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html">Embedding Metadata within a Video Stream</a> in the <i>Amazon IVS User Guide</i>.</p>

        Args:
            channel_arn: <p>ARN of the channel into which metadata is inserted. This channel must have an active stream.</p>
            metadata: <p>Metadata to insert into the stream. Maximum: 1 KB per request.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.channel_not_broadcasting.ChannelNotBroadcasting: <p>The stream is offline for the given channel ARN.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.put_metadata_request.PutMetadataRequest]",
        ) -> OperationResponse[None]:
            import capo_ivs._operations.amazon_interactive_video_service.put_metadata

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.put_metadata.put_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.put_metadata_request.PutMetadataRequest = {
            "channel_arn": channel_arn,
            "metadata": metadata,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_viewer_session_revocation(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        viewer_id: "capo_ivs.types.viewer_id.ViewerId",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        viewer_session_versions_less_than_or_equal_to: Optional[
            "capo_ivs.types.viewer_session_version.ViewerSessionVersion"
        ] = None,
    ) -> "capo_ivs.types.start_viewer_session_revocation_response.StartViewerSessionRevocationResponse":
        """<p>Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html">Setting Up Private Channels</a>.</p>

        Args:
            channel_arn: <p>The ARN of the channel associated with the viewer session to revoke.</p>
            viewer_id: <p>The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information.</p>
            viewer_session_versions_less_than_or_equal_to: <p>An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.start_viewer_session_revocation_request.StartViewerSessionRevocationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.start_viewer_session_revocation_response.StartViewerSessionRevocationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.start_viewer_session_revocation

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.start_viewer_session_revocation.start_viewer_session_revocation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.start_viewer_session_revocation_request.StartViewerSessionRevocationRequest = {
            "channel_arn": channel_arn,
            "viewer_id": viewer_id,
        }
        if viewer_session_versions_less_than_or_equal_to is not None:
            input_["viewer_session_versions_less_than_or_equal_to"] = (
                viewer_session_versions_less_than_or_equal_to
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_stream(
        self,
        channel_arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.stop_stream_response.StopStreamResponse":
        """<p>Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> <note> <p>Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the <code>streamKey</code> attached to the channel.</p> </note>

        Args:
            channel_arn: <p>ARN of the channel for which the stream is to be stopped.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.channel_not_broadcasting.ChannelNotBroadcasting: <p>The stream is offline for the given channel ARN.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.stream_unavailable.StreamUnavailable: <p>The stream is temporarily unavailable.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.stop_stream_request.StopStreamRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.stop_stream_response.StopStreamResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.stop_stream

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.stop_stream.stop_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.stop_stream_request.StopStreamRequest = {
            "channel_arn": channel_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_ivs.types.resource_arn.ResourceArn",
        tags: "capo_ivs.types.tags.Tags",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded.</p>
            tags: <p>Array of tags to be added or updated. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>

        Raises:
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.tag_resource

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_ivs.types.resource_arn.ResourceArn",
        tag_keys: "capo_ivs.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
    ) -> "capo_ivs.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the resource with the specified ARN.</p>

        Args:
            resource_arn: <p>ARN of the resource for which tags are to be removed. The ARN must be URL-encoded.</p>
            tag_keys: <p>Array of tag keys (strings) for the tags to be removed. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>

        Raises:
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.untag_resource

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_ad_configuration(
        self,
        arn: "capo_ivs.types.ad_configuration_arn.AdConfigurationArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional[
            "capo_ivs.types.ad_configuration_name.AdConfigurationName"
        ] = None,
        media_tailor_playback_configurations: Optional[
            "capo_ivs.types.media_tailor_playback_configurations_list.MediaTailorPlaybackConfigurationsList"
        ] = None,
        post_roll_configuration: Optional[
            "capo_ivs.types.post_roll_configuration.PostRollConfiguration"
        ] = None,
    ) -> (
        "capo_ivs.types.update_ad_configuration_response.UpdateAdConfigurationResponse"
    ):
        """<p>Updates a specified ad configuration.</p>

        Args:
            arn: <p>ARN of the ad configuration to be updated.</p>
            name: <p>Ad configuration name. The value does not need to be unique.</p>
            media_tailor_playback_configurations: <p>List of integration configurations with MediaTailor resources. The first item in the list is the default playback configuration used for the ad configuration. To select a different configuration per viewing session, see <a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/private-channels-generate-tokens.html">Generate and Sign IVS Playback Tokens</a>.</p>
            post_roll_configuration: <p>Configuration for the post-roll ad break to use for this ad configuration.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_ivs.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.update_ad_configuration_request.UpdateAdConfigurationRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.update_ad_configuration_response.UpdateAdConfigurationResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.update_ad_configuration

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.update_ad_configuration.update_ad_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.update_ad_configuration_request.UpdateAdConfigurationRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if media_tailor_playback_configurations is not None:
            input_["media_tailor_playback_configurations"] = (
                media_tailor_playback_configurations
            )
        if post_roll_configuration is not None:
            input_["post_roll_configuration"] = post_roll_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        arn: "capo_ivs.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        name: Optional["capo_ivs.types.channel_name.ChannelName"] = None,
        latency_mode: Optional[
            "capo_ivs.types.channel_latency_mode.ChannelLatencyMode"
        ] = None,
        type: Optional["capo_ivs.types.channel_type.ChannelType"] = None,
        authorized: Optional["capo_ivs.types.boolean.Boolean"] = None,
        recording_configuration_arn: Optional[
            "capo_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
        ] = None,
        insecure_ingest: Optional["capo_ivs.types.boolean.Boolean"] = None,
        preset: Optional["capo_ivs.types.transcode_preset.TranscodePreset"] = None,
        playback_restriction_policy_arn: Optional[
            "capo_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
        ] = None,
        multitrack_input_configuration: Optional[
            "capo_ivs.types.multitrack_input_configuration.MultitrackInputConfiguration"
        ] = None,
        container_format: Optional[
            "capo_ivs.types.container_format.ContainerFormat"
        ] = None,
        ad_configuration_arn: Optional[
            "capo_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
        ] = None,
    ) -> "capo_ivs.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates a channel's configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.</p>

        Args:
            arn: <p>ARN of the channel to be updated.</p>
            name: <p>Channel name.</p>
            latency_mode: <p>Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers.</p>
            type: <p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Default: <code>STANDARD</code>. For details, see <a href="https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/channel-types.html">Channel Types</a>.</p>
            authorized: <p>Whether the channel is private (enabled for playback authorization).</p>
            recording_configuration_arn: <p>Recording-configuration ARN. A valid ARN value here both specifies the ARN and enables recording. If this is set to an empty string, recording is disabled.</p>
            insecure_ingest: <p>Whether the channel allows insecure RTMP and SRT ingest. Default: <code>false</code>.</p>
            preset: <p>Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>""</code>).</p>
            playback_restriction_policy_arn: <p>Playback-restriction-policy ARN. A valid ARN value here both specifies the ARN and enables playback restriction. If this is set to an empty string, playback restriction policy is disabled.</p>
            multitrack_input_configuration: <p>Object specifying multitrack input configuration. Default: no multitrack input configuration is specified.</p>
            container_format: <p>Indicates which content-packaging format is used (MPEG-TS or fMP4). If <code>multitrackInputConfiguration</code> is specified and <code>enabled</code> is <code>true</code>, then <code>containerFormat</code> is required and must be set to <code>FRAGMENTED_MP4</code>. Otherwise, <code>containerFormat</code> may be set to <code>TS</code> or <code>FRAGMENTED_MP4</code>. Default: <code>TS</code>.</p>
            ad_configuration_arn: <p>ARN of the ad configuration associated with the channel.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.update_channel

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.update_channel_request.UpdateChannelRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if latency_mode is not None:
            input_["latency_mode"] = latency_mode
        if type is not None:
            input_["type"] = type
        if authorized is not None:
            input_["authorized"] = authorized
        if recording_configuration_arn is not None:
            input_["recording_configuration_arn"] = recording_configuration_arn
        if insecure_ingest is not None:
            input_["insecure_ingest"] = insecure_ingest
        if preset is not None:
            input_["preset"] = preset
        if playback_restriction_policy_arn is not None:
            input_["playback_restriction_policy_arn"] = playback_restriction_policy_arn
        if multitrack_input_configuration is not None:
            input_["multitrack_input_configuration"] = multitrack_input_configuration
        if container_format is not None:
            input_["container_format"] = container_format
        if ad_configuration_arn is not None:
            input_["ad_configuration_arn"] = ad_configuration_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_playback_restriction_policy(
        self,
        arn: "capo_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn",
        *,
        config_overrides: Optional[ivsClientConfig] = None,
        allowed_countries: Optional[
            "capo_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
        ] = None,
        allowed_origins: Optional[
            "capo_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
        ] = None,
        enable_strict_origin_enforcement: Optional[
            "capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
        ] = None,
        name: Optional[
            "capo_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
        ] = None,
    ) -> "capo_ivs.types.update_playback_restriction_policy_response.UpdatePlaybackRestrictionPolicyResponse":
        """<p>Updates a specified playback restriction policy.</p>

        Args:
            arn: <p>ARN of the playback-restriction-policy to be updated.</p>
            allowed_countries: <p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>
            allowed_origins: <p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>
            enable_strict_origin_enforcement: <p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>
            name: <p>Playback-restriction-policy name. The value does not need to be unique.</p>

        Raises:
            capo_ivs.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_ivs.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_ivs.errors.pending_verification.PendingVerification: <p>Your account is pending verification.</p>
            capo_ivs.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_ivs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_ivs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ivs.types.update_playback_restriction_policy_request.UpdatePlaybackRestrictionPolicyRequest]",
        ) -> OperationResponse[
            "capo_ivs.types.update_playback_restriction_policy_response.UpdatePlaybackRestrictionPolicyResponse"
        ]:
            import capo_ivs._operations.amazon_interactive_video_service.update_playback_restriction_policy

            output, http_response = (
                capo_ivs._operations.amazon_interactive_video_service.update_playback_restriction_policy.update_playback_restriction_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivs.types.update_playback_restriction_policy_request.UpdatePlaybackRestrictionPolicyRequest = {
            "arn": arn
        }
        if allowed_countries is not None:
            input_["allowed_countries"] = allowed_countries
        if allowed_origins is not None:
            input_["allowed_origins"] = allowed_origins
        if enable_strict_origin_enforcement is not None:
            input_["enable_strict_origin_enforcement"] = (
                enable_strict_origin_enforcement
            )
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
