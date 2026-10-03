"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#AWSAcuitySignalingService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_kinesis_video_signaling._auth._signers
import capo_kinesis_video_signaling._auth._sigv4
from capo_kinesis_video_signaling._auth._identity import Credentials
from capo_kinesis_video_signaling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_kinesis_video_signaling._auth._zapros_handler import AuthMiddleware
from capo_kinesis_video_signaling._services._aws_config import aaws_config
from capo_kinesis_video_signaling._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.client_id
    import capo_kinesis_video_signaling.types.get_ice_server_config_request
    import capo_kinesis_video_signaling.types.get_ice_server_config_response
    import capo_kinesis_video_signaling.types.message_payload
    import capo_kinesis_video_signaling.types.resource_arn
    import capo_kinesis_video_signaling.types.send_alexa_offer_to_master_request
    import capo_kinesis_video_signaling.types.send_alexa_offer_to_master_response
    import capo_kinesis_video_signaling.types.service
    import capo_kinesis_video_signaling.types.username


class AsyncKinesisVideoSignalingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncKinesisVideoSignalingClient:
    """A client for the ``KinesisVideoSignaling`` service.

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
        self._config = AsyncKinesisVideoSignalingClientConfig(
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
        self, config_overrides: Optional[AsyncKinesisVideoSignalingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncKinesisVideoSignalingClientConfig = config_overrides or {}
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

    async def get_ice_server_config(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoSignalingClientConfig] = None,
        channel_arn: Optional[
            "capo_kinesis_video_signaling.types.resource_arn.ResourceARN"
        ] = None,
        client_id: Optional[
            "capo_kinesis_video_signaling.types.client_id.ClientId"
        ] = None,
        service: Optional["capo_kinesis_video_signaling.types.service.Service"] = None,
        username: Optional[
            "capo_kinesis_video_signaling.types.username.Username"
        ] = None,
    ) -> "capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse":
        """<p>Gets the Interactive Connectivity Establishment (ICE) server configuration information, including URIs, username, and password which can be used to configure the WebRTC connection. The ICE component uses this configuration information to setup the WebRTC connection, including authenticating with the Traversal Using Relays around NAT (TURN) relay server. </p> <p>TURN is a protocol that is used to improve the connectivity of peer-to-peer applications. By providing a cloud-based relay service, TURN ensures that a connection can be established even when one or more peers are incapable of a direct peer-to-peer connection. For more information, see <a href="https://tools.ietf.org/html/draft-uberti-rtcweb-turn-rest-00">A REST API For Access To TURN Services</a>.</p> <p> You can invoke this API to establish a fallback mechanism in case either of the peers is unable to establish a direct peer-to-peer connection over a signaling channel. You must specify either a signaling channel ARN or the client ID in order to invoke this API.</p>

        Args:
            channel_arn: <p>The ARN of the signaling channel to be used for the peer-to-peer connection between configured peers. </p>
            client_id: <p>Unique identifier for the viewer. Must be unique within the signaling channel.</p>
            service: <p>Specifies the desired service. Currently, <code>TURN</code> is the only valid value.</p>
            username: <p>An optional user ID to be associated with the credentials.</p>

        Raises:
            capo_kinesis_video_signaling.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Your request was throttled because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            capo_kinesis_video_signaling.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            capo_kinesis_video_signaling.errors.invalid_client_exception.InvalidClientException: <p>The specified client is invalid.</p>
            capo_kinesis_video_signaling.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            capo_kinesis_video_signaling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is not found.</p>
            capo_kinesis_video_signaling.errors.session_expired_exception.SessionExpiredException: <p>If the client session is expired. Once the client is connected, the session is valid for 45 minutes. Client should reconnect to the channel to continue sending/receiving messages.</p>
            capo_kinesis_video_signaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_kinesis_video_signaling.types.get_ice_server_config_response.GetIceServerConfigResponse"
        ]:
            import capo_kinesis_video_signaling._operations.aws_acuity_signaling_service.get_ice_server_config

            (
                output,
                http_response,
            ) = await capo_kinesis_video_signaling._operations.aws_acuity_signaling_service.get_ice_server_config.async_get_ice_server_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_signaling.types.get_ice_server_config_request.GetIceServerConfigRequest = {}
        if channel_arn is not None:
            input_["channel_arn"] = channel_arn
        if client_id is not None:
            input_["client_id"] = client_id
        if service is not None:
            input_["service"] = service
        if username is not None:
            input_["username"] = username

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_alexa_offer_to_master(
        self,
        *,
        config_overrides: Optional[AsyncKinesisVideoSignalingClientConfig] = None,
        channel_arn: Optional[
            "capo_kinesis_video_signaling.types.resource_arn.ResourceARN"
        ] = None,
        sender_client_id: Optional[
            "capo_kinesis_video_signaling.types.client_id.ClientId"
        ] = None,
        message_payload: Optional[
            "capo_kinesis_video_signaling.types.message_payload.MessagePayload"
        ] = None,
    ) -> "capo_kinesis_video_signaling.types.send_alexa_offer_to_master_response.SendAlexaOfferToMasterResponse":
        """<p>This API allows you to connect WebRTC-enabled devices with Alexa display devices. When invoked, it sends the Alexa Session Description Protocol (SDP) offer to the master peer. The offer is delivered as soon as the master is connected to the specified signaling channel. This API returns the SDP answer from the connected master. If the master is not connected to the signaling channel, redelivery requests are made until the message expires.</p>

        Args:
            channel_arn: <p>The ARN of the signaling channel by which Alexa and the master peer communicate.</p>
            sender_client_id: <p>The unique identifier for the sender client.</p>
            message_payload: <p>The base64-encoded SDP offer content.</p>

        Raises:
            capo_kinesis_video_signaling.errors.client_limit_exceeded_exception.ClientLimitExceededException: <p>Your request was throttled because you have exceeded the limit of allowed client calls. Try making the call later.</p>
            capo_kinesis_video_signaling.errors.invalid_argument_exception.InvalidArgumentException: <p>The value for this input parameter is invalid.</p>
            capo_kinesis_video_signaling.errors.not_authorized_exception.NotAuthorizedException: <p>The caller is not authorized to perform this operation.</p>
            capo_kinesis_video_signaling.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource is not found.</p>
            capo_kinesis_video_signaling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_kinesis_video_signaling.types.send_alexa_offer_to_master_request.SendAlexaOfferToMasterRequest]",
        ) -> AsyncOperationResponse[
            "capo_kinesis_video_signaling.types.send_alexa_offer_to_master_response.SendAlexaOfferToMasterResponse"
        ]:
            import capo_kinesis_video_signaling._operations.aws_acuity_signaling_service.send_alexa_offer_to_master

            (
                output,
                http_response,
            ) = await capo_kinesis_video_signaling._operations.aws_acuity_signaling_service.send_alexa_offer_to_master.async_send_alexa_offer_to_master(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_kinesis_video_signaling.types.send_alexa_offer_to_master_request.SendAlexaOfferToMasterRequest = {}
        if channel_arn is not None:
            input_["channel_arn"] = channel_arn
        if sender_client_id is not None:
            input_["sender_client_id"] = sender_client_id
        if message_payload is not None:
            input_["message_payload"] = message_payload

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
