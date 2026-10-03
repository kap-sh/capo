"""Generated from Smithy shape ``com.amazonaws.kinesisvideowebrtcstorage#AWSAcuityRoutingServiceLambda``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_kinesis_video_webrtc_storage._auth._signers
import capo_kinesis_video_webrtc_storage._auth._sigv4
from capo_kinesis_video_webrtc_storage._auth._identity import Credentials
from capo_kinesis_video_webrtc_storage._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kinesis_video_webrtc_storage._auth._zapros_handler import AuthMiddleware
from capo_kinesis_video_webrtc_storage._services._aws_config import aaws_config
from capo_kinesis_video_webrtc_storage._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_kinesis_video_webrtc_storage.types.channel_arn
    import capo_kinesis_video_webrtc_storage.types.client_id
    import capo_kinesis_video_webrtc_storage.types.join_storage_session_as_viewer_input
    import capo_kinesis_video_webrtc_storage.types.join_storage_session_input


class AsyncKinesisVideoWebRTCStorageClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncKinesisVideoWebRTCStorageClient:
    """A client for the ``KinesisVideoWebRTCStorage`` service.

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
        self._config = AsyncKinesisVideoWebRTCStorageClientConfig(
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
        self,
        config_overrides: Optional[AsyncKinesisVideoWebRTCStorageClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKinesisVideoWebRTCStorageClientConfig = config_overrides or {}
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

    async def join_storage_session(
        self,
        channel_arn: "capo_kinesis_video_webrtc_storage.types.channel_arn.ChannelArn",
        *,
        config_overrides: Optional[AsyncKinesisVideoWebRTCStorageClientConfig] = None,
    ) -> None:
        """<note> <p>Before using this API, you must call the <code>GetSignalingChannelEndpoint</code> API to request the WEBRTC endpoint. You then specify the endpoint and region in your <code>JoinStorageSession</code> API request.</p> </note> <p>Join the ongoing one way-video and/or multi-way audio WebRTC session as a video producing device for an input channel. If there’s no existing session for the channel, a new streaming session needs to be created, and the Amazon Resource Name (ARN) of the signaling channel must be provided. </p> <p>Currently for the <code>SINGLE_MASTER</code> type, a video producing device is able to ingest both audio and video media into a stream. Only video producing devices can join the session and record media.</p> <important> <p>Both audio and video tracks are currently required for WebRTC ingestion.</p> <p>Current requirements:</p> <ul> <li> <p>Video track: H.264</p> </li> <li> <p>Audio track: Opus</p> </li> </ul> </important> <p>The resulting ingested video in the Kinesis video stream will have the following parameters: H.264 video and AAC audio.</p> <p>Once a master participant has negotiated a connection through WebRTC, the ingested media session will be stored in the Kinesis video stream. Multiple viewers are then able to play back real-time media through our Playback APIs.</p> <p>You can also use existing Kinesis Video Streams features like <code>HLS</code> or <code>DASH</code> playback, image generation via <a href="https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-getImages.html">GetImages</a>, and more with ingested WebRTC media.</p> <note> <p>S3 image delivery and notifications are not currently supported.</p> </note> <note> <p>Assume that only one video producing device client can be associated with a session for the channel. If more than one client joins the session of a specific channel as a video producing device, the most recent client request takes precedence. </p> </note> <p> <b>Additional information</b> </p> <ul> <li> <p> <b>Idempotent</b> - This API is not idempotent.</p> </li> <li> <p> <b>Retry behavior</b> - This is counted as a new API call.</p> </li> <li> <p> <b>Concurrent calls</b> - Concurrent calls are allowed. An offer is sent once per each call.</p> </li> </ul>

        Args:
            channel_arn: <p> The Amazon Resource Name (ARN) of the signaling channel. </p>

        Raises:
            capo_kinesis_video_webrtc_storage.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            capo_kinesis_video_webrtc_storage.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p> Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later. </p>
            capo_kinesis_video_webrtc_storage.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            capo_kinesis_video_webrtc_storage.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is not found.</p>
            capo_kinesis_video_webrtc_storage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kinesis_video_webrtc_storage.types.join_storage_session_input.JoinStorageSessionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_kinesis_video_webrtc_storage._operations.aws_acuity_routing_service_lambda.join_storage_session

            (
                output,
                http_response,
            ) = await capo_kinesis_video_webrtc_storage._operations.aws_acuity_routing_service_lambda.join_storage_session.async_join_storage_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_webrtc_storage.types.join_storage_session_input.JoinStorageSessionInput = {
            "channel_arn": channel_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def join_storage_session_as_viewer(
        self,
        channel_arn: "capo_kinesis_video_webrtc_storage.types.channel_arn.ChannelArn",
        client_id: "capo_kinesis_video_webrtc_storage.types.client_id.ClientId",
        *,
        config_overrides: Optional[AsyncKinesisVideoWebRTCStorageClientConfig] = None,
    ) -> None:
        """<p> Join the ongoing one way-video and/or multi-way audio WebRTC session as a viewer for an input channel. If there’s no existing session for the channel, create a new streaming session and provide the Amazon Resource Name (ARN) of the signaling channel (<code>channelArn</code>) and client id (<code>clientId</code>). </p> <p>Currently for <code>SINGLE_MASTER</code> type, a video producing device is able to ingest both audio and video media into a stream, while viewers can only ingest audio. Both a video producing device and viewers can join a session first and wait for other participants. While participants are having peer to peer conversations through WebRTC, the ingested media session will be stored into the Kinesis Video Stream. Multiple viewers are able to playback real-time media. </p> <p>Customers can also use existing Kinesis Video Streams features like <code>HLS</code> or <code>DASH</code> playback, Image generation, and more with ingested WebRTC media. If there’s an existing session with the same <code>clientId</code> that's found in the join session request, the new request takes precedence.</p>

        Args:
            channel_arn: <p> The Amazon Resource Name (ARN) of the signaling channel. </p>
            client_id: <p> The unique identifier for the sender client. </p>

        Raises:
            capo_kinesis_video_webrtc_storage.errors.access_denied_exception.AccessDeniedException: <p>You do not have required permissions to perform this operation.</p>
            capo_kinesis_video_webrtc_storage.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p> Kinesis Video Streams has throttled the request because you have exceeded the limit of allowed client calls. Try making the call later. </p>
            capo_kinesis_video_webrtc_storage.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            capo_kinesis_video_webrtc_storage.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is not found.</p>
            capo_kinesis_video_webrtc_storage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kinesis_video_webrtc_storage.types.join_storage_session_as_viewer_input.JoinStorageSessionAsViewerInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_kinesis_video_webrtc_storage._operations.aws_acuity_routing_service_lambda.join_storage_session_as_viewer

            (
                output,
                http_response,
            ) = await capo_kinesis_video_webrtc_storage._operations.aws_acuity_routing_service_lambda.join_storage_session_as_viewer.async_join_storage_session_as_viewer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_webrtc_storage.types.join_storage_session_as_viewer_input.JoinStorageSessionAsViewerInput = {
            "channel_arn": channel_arn,
            "client_id": client_id,
        }

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
