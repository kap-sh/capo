"""Generated from Smithy shape ``com.amazonaws.iotdataplane#IotMoonrakerService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iot_data_plane._auth._signers
import capo_iot_data_plane._auth._sigv4
from capo_iot_data_plane._auth._identity import Credentials
from capo_iot_data_plane._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iot_data_plane._auth._zapros_handler import AuthMiddleware
from capo_iot_data_plane._pagination import resolve_path as _resolve_path
from capo_iot_data_plane._services._aws_config import aaws_config
from capo_iot_data_plane._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iot_data_plane.types.clean_session
    import capo_iot_data_plane.types.client_id
    import capo_iot_data_plane.types.confirmation
    import capo_iot_data_plane.types.content_type
    import capo_iot_data_plane.types.correlation_data
    import capo_iot_data_plane.types.delete_connection_request
    import capo_iot_data_plane.types.delete_thing_shadow_request
    import capo_iot_data_plane.types.delete_thing_shadow_response
    import capo_iot_data_plane.types.get_connection_request
    import capo_iot_data_plane.types.get_connection_response
    import capo_iot_data_plane.types.get_retained_message_request
    import capo_iot_data_plane.types.get_retained_message_response
    import capo_iot_data_plane.types.get_thing_shadow_request
    import capo_iot_data_plane.types.get_thing_shadow_response
    import capo_iot_data_plane.types.include_socket_information
    import capo_iot_data_plane.types.json_document
    import capo_iot_data_plane.types.list_named_shadows_for_thing_request
    import capo_iot_data_plane.types.list_named_shadows_for_thing_response
    import capo_iot_data_plane.types.list_retained_messages_request
    import capo_iot_data_plane.types.list_retained_messages_response
    import capo_iot_data_plane.types.list_subscriptions_request
    import capo_iot_data_plane.types.list_subscriptions_response
    import capo_iot_data_plane.types.max_results
    import capo_iot_data_plane.types.message_expiry
    import capo_iot_data_plane.types.next_token
    import capo_iot_data_plane.types.page_size
    import capo_iot_data_plane.types.payload
    import capo_iot_data_plane.types.payload_format_indicator
    import capo_iot_data_plane.types.prevent_will_message
    import capo_iot_data_plane.types.publish_request
    import capo_iot_data_plane.types.qos
    import capo_iot_data_plane.types.response_topic
    import capo_iot_data_plane.types.retain
    import capo_iot_data_plane.types.retained_message_summary
    import capo_iot_data_plane.types.send_direct_message_request
    import capo_iot_data_plane.types.send_direct_message_response
    import capo_iot_data_plane.types.shadow_name
    import capo_iot_data_plane.types.subscription_summary
    import capo_iot_data_plane.types.synthesized_json_user_properties
    import capo_iot_data_plane.types.thing_name
    import capo_iot_data_plane.types.timeout_in_seconds
    import capo_iot_data_plane.types.topic
    import capo_iot_data_plane.types.update_thing_shadow_request
    import capo_iot_data_plane.types.update_thing_shadow_response


class AsyncIoTDataPlaneClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncIoTDataPlaneClient:
    """A client for the ``IoTDataPlane`` service.

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
        self._config = AsyncIoTDataPlaneClientConfig(
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
        self, config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTDataPlaneClientConfig = config_overrides or {}
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

    async def delete_connection(
        self,
        client_id: "capo_iot_data_plane.types.client_id.ClientId",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        clean_session: Optional[
            "capo_iot_data_plane.types.clean_session.CleanSession"
        ] = None,
        prevent_will_message: Optional[
            "capo_iot_data_plane.types.prevent_will_message.PreventWillMessage"
        ] = None,
    ) -> None:
        """<p>Disconnects a connected MQTT client from Amazon Web Services IoT Core. When you disconnect a client, Amazon Web Services IoT Core closes the client's network connection and optionally cleans the session state.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">DeleteConnection</a> action.</p>

        Args:
            client_id: <p>The unique identifier of the MQTT client to disconnect. The client ID can't start with a dollar sign ($).</p> <p>MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.</p>
            clean_session: <p>Specifies whether to remove the client's persistent session state when disconnecting. Set to <code>TRUE</code> to delete all session information, including subscriptions and queued messages. Set to <code>FALSE</code> to preserve the session state for <a href="https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-persistent-sessions">persistent sessions</a>. For clean sessions this parameter will be ignored. By default, this is set to <code>FALSE</code> (preserves the session state).</p>
            prevent_will_message: <p>Controls if Amazon Web Services IoT Core publishes the client's Last Will and Testament (LWT) message upon disconnection. Set to <code>TRUE</code> to prevent publishing the LWT message. Set to <code>FALSE</code> to ensure that LWT is published. By default, this is set to <code>FALSE</code> (LWT message is published).</p>

        Raises:
            capo_iot_data_plane.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_data_plane._operations.iot_moonraker_service.delete_connection

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.delete_connection_request.DeleteConnectionRequest = {
            "client_id": client_id
        }
        if clean_session is not None:
            input_["clean_session"] = clean_session
        if prevent_will_message is not None:
            input_["prevent_will_message"] = prevent_will_message

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_thing_shadow(
        self,
        thing_name: "capo_iot_data_plane.types.thing_name.ThingName",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        shadow_name: Optional[
            "capo_iot_data_plane.types.shadow_name.ShadowName"
        ] = None,
    ) -> "capo_iot_data_plane.types.delete_thing_shadow_response.DeleteThingShadowResponse":
        """<p>Deletes the shadow for the specified thing.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">DeleteThingShadow</a> action.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html">DeleteThingShadow</a> in the IoT Developer Guide.</p>

        Args:
            thing_name: <p>The name of the thing.</p>
            shadow_name: <p>The name of the shadow.</p>

        Raises:
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.unsupported_document_encoding_exception.UnsupportedDocumentEncodingException: <p>The document encoding is not supported.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.delete_thing_shadow_request.DeleteThingShadowRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.delete_thing_shadow_response.DeleteThingShadowResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.delete_thing_shadow

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.delete_thing_shadow.async_delete_thing_shadow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.delete_thing_shadow_request.DeleteThingShadowRequest = {
            "thing_name": thing_name
        }
        if shadow_name is not None:
            input_["shadow_name"] = shadow_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection(
        self,
        client_id: "capo_iot_data_plane.types.client_id.ClientId",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        include_socket_information: Optional[
            "capo_iot_data_plane.types.include_socket_information.IncludeSocketInformation"
        ] = None,
    ) -> "capo_iot_data_plane.types.get_connection_response.GetConnectionResponse":
        """<p>Retrieves connection information for the specified MQTT client.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">GetConnection</a> action.</p>

        Args:
            client_id: <p>The unique identifier of the MQTT client to retrieve connection information. The client ID can't start with a dollar sign ($).</p> <p>MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.</p>
            include_socket_information: <p>Specifies if socket information (sourcePort, targetPort, sourceIp, targetIp) should be included in the GetConnection response. Set to <code>TRUE</code> to include socket information. Set to <code>FALSE</code> to omit socket information. By default, this is set to <code>FALSE</code>. See the <a href="https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-client-disconnect">developer guide</a> for how to authorize this parameter.</p>

        Raises:
            capo_iot_data_plane.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.get_connection_request.GetConnectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.get_connection

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.get_connection_request.GetConnectionRequest = {
            "client_id": client_id
        }
        if include_socket_information is not None:
            input_["include_socket_information"] = include_socket_information

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_retained_message(
        self,
        topic: "capo_iot_data_plane.types.topic.Topic",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
    ) -> "capo_iot_data_plane.types.get_retained_message_response.GetRetainedMessageResponse":
        """<p>Gets the details of a single retained message for the specified topic.</p> <p>This action returns the message payload of the retained message, which can incur messaging costs. To list only the topic names of the retained messages, call <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html">ListRetainedMessages</a>.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html">GetRetainedMessage</a> action.</p> <p>For more information about messaging costs, see <a href="http://aws.amazon.com/iot-core/pricing/#Messaging">Amazon Web Services IoT Core pricing - Messaging</a>.</p>

        Args:
            topic: <p>The topic name of the retained message to retrieve.</p>

        Raises:
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.get_retained_message_request.GetRetainedMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.get_retained_message_response.GetRetainedMessageResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.get_retained_message

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.get_retained_message.async_get_retained_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.get_retained_message_request.GetRetainedMessageRequest = {
            "topic": topic
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_thing_shadow(
        self,
        thing_name: "capo_iot_data_plane.types.thing_name.ThingName",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        shadow_name: Optional[
            "capo_iot_data_plane.types.shadow_name.ShadowName"
        ] = None,
    ) -> "capo_iot_data_plane.types.get_thing_shadow_response.GetThingShadowResponse":
        """<p>Gets the shadow for the specified thing.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">GetThingShadow</a> action.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html">GetThingShadow</a> in the IoT Developer Guide.</p>

        Args:
            thing_name: <p>The name of the thing.</p>
            shadow_name: <p>The name of the shadow.</p>

        Raises:
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.unsupported_document_encoding_exception.UnsupportedDocumentEncodingException: <p>The document encoding is not supported.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.get_thing_shadow_request.GetThingShadowRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.get_thing_shadow_response.GetThingShadowResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.get_thing_shadow

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.get_thing_shadow.async_get_thing_shadow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.get_thing_shadow_request.GetThingShadowRequest = {
            "thing_name": thing_name
        }
        if shadow_name is not None:
            input_["shadow_name"] = shadow_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_named_shadows_for_thing(
        self,
        thing_name: "capo_iot_data_plane.types.thing_name.ThingName",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        next_token: Optional["capo_iot_data_plane.types.next_token.NextToken"] = None,
        page_size: Optional["capo_iot_data_plane.types.page_size.PageSize"] = None,
    ) -> "capo_iot_data_plane.types.list_named_shadows_for_thing_response.ListNamedShadowsForThingResponse":
        """<p>Lists the shadows for the specified thing.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">ListNamedShadowsForThing</a> action.</p>

        Args:
            thing_name: <p>The name of the thing.</p>
            next_token: <p>The token to retrieve the next set of results.</p>
            page_size: <p>The result page size.</p>

        Raises:
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.list_named_shadows_for_thing_request.ListNamedShadowsForThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.list_named_shadows_for_thing_response.ListNamedShadowsForThingResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.list_named_shadows_for_thing

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.list_named_shadows_for_thing.async_list_named_shadows_for_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.list_named_shadows_for_thing_request.ListNamedShadowsForThingRequest = {
            "thing_name": thing_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_retained_messages(
        self,
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        next_token: Optional["capo_iot_data_plane.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_data_plane.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_data_plane.types.list_retained_messages_response.ListRetainedMessagesResponse":
        """<p>Lists summary information about the retained messages stored for the account.</p> <p>This action returns only the topic names of the retained messages. It doesn't return any message payloads. Although this action doesn't return a message payload, it can still incur messaging costs.</p> <p>To get the message payload of a retained message, call <a href="https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html">GetRetainedMessage</a> with the topic name of the retained message.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html">ListRetainedMessages</a> action.</p> <p>For more information about messaging costs, see <a href="http://aws.amazon.com/iot-core/pricing/#Messaging">Amazon Web Services IoT Core pricing - Messaging</a>.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.list_retained_messages_request.ListRetainedMessagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.list_retained_messages_response.ListRetainedMessagesResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.list_retained_messages

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.list_retained_messages.async_list_retained_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.list_retained_messages_request.ListRetainedMessagesRequest = {}
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

    async def iter_list_retained_messages(
        self,
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        next_token: Optional["capo_iot_data_plane.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_data_plane.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_data_plane.types.retained_message_summary.RetainedMessageSummary]":
        _token = next_token
        while True:
            _response = await self.list_retained_messages(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("retained_topics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions(
        self,
        client_id: "capo_iot_data_plane.types.client_id.ClientId",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        next_token: Optional["capo_iot_data_plane.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_data_plane.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_data_plane.types.list_subscriptions_response.ListSubscriptionsResponse":
        """<p>Returns a list of all subscriptions for MQTT clients with active sessions, including offline clients with persistent sessions.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">ListSubscriptions</a> action.</p>

        Args:
            client_id: <p>The unique identifier of the MQTT client to list subscriptions for. The client ID can't start with a dollar sign ($).</p> <p>MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of subscriptions to return in a single request. By default, this is set to 20.</p>

        Raises:
            capo_iot_data_plane.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.list_subscriptions_request.ListSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.list_subscriptions_response.ListSubscriptionsResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.list_subscriptions

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.list_subscriptions_request.ListSubscriptionsRequest = {
            "client_id": client_id
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

    async def iter_list_subscriptions(
        self,
        client_id: "capo_iot_data_plane.types.client_id.ClientId",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        next_token: Optional["capo_iot_data_plane.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iot_data_plane.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_data_plane.types.subscription_summary.SubscriptionSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                client_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def publish(
        self,
        topic: "capo_iot_data_plane.types.topic.Topic",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        qos: Optional["capo_iot_data_plane.types.qos.Qos"] = None,
        retain: Optional["capo_iot_data_plane.types.retain.Retain"] = None,
        payload: Optional["capo_iot_data_plane.types.payload.Payload"] = None,
        user_properties: Optional[
            "capo_iot_data_plane.types.synthesized_json_user_properties.SynthesizedJsonUserProperties"
        ] = None,
        payload_format_indicator: Optional[
            "capo_iot_data_plane.types.payload_format_indicator.PayloadFormatIndicator"
        ] = None,
        content_type: Optional[
            "capo_iot_data_plane.types.content_type.ContentType"
        ] = None,
        response_topic: Optional[
            "capo_iot_data_plane.types.response_topic.ResponseTopic"
        ] = None,
        correlation_data: Optional[
            "capo_iot_data_plane.types.correlation_data.CorrelationData"
        ] = None,
        message_expiry: Optional[
            "capo_iot_data_plane.types.message_expiry.MessageExpiry"
        ] = None,
    ) -> None:
        """<p>Publishes an MQTT message.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">Publish</a> action.</p> <p>For more information about MQTT messages, see <a href="http://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html">MQTT Protocol</a> in the IoT Developer Guide.</p> <p>For more information about messaging costs, see <a href="http://aws.amazon.com/iot-core/pricing/#Messaging">Amazon Web Services IoT Core pricing - Messaging</a>.</p>

        Args:
            topic: <p>The name of the MQTT topic.</p>
            qos: <p>The Quality of Service (QoS) level. The default QoS level is 0.</p>
            retain: <p>A Boolean value that determines whether to set the RETAIN flag when the message is published.</p> <p>Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default value: <code>false</code> </p>
            payload: <p>The message body. MQTT accepts text, binary, and empty (null) message payloads.</p> <p>Publishing an empty (null) payload with <b>retain</b> = <code>true</code> deletes the retained message identified by <b>topic</b> from Amazon Web Services IoT Core.</p>
            user_properties: <p>A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. <code>userProperties</code> is an HTTP header value in the API.</p> <p>The following example <code>userProperties</code> parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:</p> <p> <code>[{"deviceName": "alpha"}, {"deviceCnt": "45"}]</code> </p>
            payload_format_indicator: <p>An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8. <code>payloadFormatIndicator</code> is an HTTP header value in the API.</p>
            content_type: <p>A UTF-8 encoded string that describes the content of the publishing message.</p>
            response_topic: <p>A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.</p>
            correlation_data: <p>The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. <code>correlationData</code> is an HTTP header value in the API.</p>
            message_expiry: <p>A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn't expire. For more information about the limits of <code>messageExpiry</code>, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas </a> from the Amazon Web Services Reference Guide.</p>

        Raises:
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.publish_request.PublishRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_data_plane._operations.iot_moonraker_service.publish

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.publish.async_publish(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.publish_request.PublishRequest = {
            "topic": topic
        }
        if qos is not None:
            input_["qos"] = qos
        if retain is not None:
            input_["retain"] = retain
        if payload is not None:
            input_["payload"] = payload
        if user_properties is not None:
            input_["user_properties"] = user_properties
        if payload_format_indicator is not None:
            input_["payload_format_indicator"] = payload_format_indicator
        if content_type is not None:
            input_["content_type"] = content_type
        if response_topic is not None:
            input_["response_topic"] = response_topic
        if correlation_data is not None:
            input_["correlation_data"] = correlation_data
        if message_expiry is not None:
            input_["message_expiry"] = message_expiry

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_direct_message(
        self,
        client_id: "capo_iot_data_plane.types.client_id.ClientId",
        topic: "capo_iot_data_plane.types.topic.Topic",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        content_type: Optional[
            "capo_iot_data_plane.types.content_type.ContentType"
        ] = None,
        response_topic: Optional[
            "capo_iot_data_plane.types.response_topic.ResponseTopic"
        ] = None,
        confirmation: Optional[
            "capo_iot_data_plane.types.confirmation.Confirmation"
        ] = None,
        timeout: Optional[
            "capo_iot_data_plane.types.timeout_in_seconds.TimeoutInSeconds"
        ] = None,
        payload: Optional["capo_iot_data_plane.types.payload.Payload"] = None,
        user_properties: Optional[
            "capo_iot_data_plane.types.synthesized_json_user_properties.SynthesizedJsonUserProperties"
        ] = None,
        payload_format_indicator: Optional[
            "capo_iot_data_plane.types.payload_format_indicator.PayloadFormatIndicator"
        ] = None,
        correlation_data: Optional[
            "capo_iot_data_plane.types.correlation_data.CorrelationData"
        ] = None,
    ) -> "capo_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse":
        """<p>Sends an MQTT message directly to a specific client identified by its client ID.</p> <p> <code>SendDirectMessage</code> targets a single client ID. The receiving client does not need to subscribe to the topic, but the receiver's policy must allow <code>iot:Receive</code> on the specified topic.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">SendDirectMessage</a> action.</p> <p>For more information about messaging costs, see <a href="http://aws.amazon.com/iot-core/pricing/">Amazon Web Services IoT Core pricing</a>.</p>

        Args:
            client_id: <p>The unique identifier of the MQTT client to send the message to.</p> <p>Client IDs must not exceed 128 characters and can't start with a dollar sign ($). MQTT client IDs must be URL encoded (percent-encoded) when they contain characters that are not valid in HTTP requests, such as spaces, forward slashes (/), and UTF-8 characters. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas</a>.</p>
            topic: <p>The topic of the outbound MQTT Publish message to the receiving client. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas</a>.</p>
            content_type: <p>The MQTT5 content type property forwarded to the receiving client (for example, <code>application/json</code>).</p>
            response_topic: <p>A UTF-8 encoded string that's used as the topic name for a response message. The response topic describes the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits">Amazon Web Services IoT Core message broker and protocol limits and quotas</a>.</p>
            confirmation: <p>A Boolean value that specifies whether to wait for delivery confirmation from the receiving client.</p> <p>When set to <code>true</code>, the API delivers the message at QoS 1 and waits for the client to send a delivery confirmation (PUBACK) before returning a successful response. If delivery confirmation is not received within the specified <code>timeout</code> period, the API returns HTTP 504.</p> <p>When set to <code>false</code>, the API delivers the message at QoS 0 and returns after Amazon Web Services IoT Core attempts to deliver the message.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default value: <code>false</code> </p>
            timeout: <p>An integer that represents the maximum time, in seconds, to wait for a delivery confirmation (PUBACK) from the receiving client after the message has been delivered. This parameter is only used when <code>confirmation</code> is set to <code>true</code>. If <code>confirmation</code> is <code>false</code>, this parameter is ignored.</p> <p>The total API response time may be higher than this value due to internal processing. Set your HTTP client timeout to a value greater than this parameter.</p> <p>Valid range: 1 to 15 seconds.</p> <p>Default value: <code>5</code> seconds.</p>
            payload: <p>The message body. MQTT accepts text, binary, and empty (null) message payloads.</p>
            user_properties: <p>A JSON string that contains an array of JSON objects. If you don't use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. <code>userProperties</code> is an HTTP header value in the API.</p> <p>For MQTT 3.1.1 clients, user properties are silently dropped.</p> <p>The following example <code>userProperties</code> parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:</p> <p> <code>[{"deviceName": "alpha"}, {"deviceCnt": "45"}]</code> </p>
            payload_format_indicator: <p>An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8. <code>payloadFormatIndicator</code> is an HTTP header value in the API.</p>
            correlation_data: <p>The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. <code>correlationData</code> is an HTTP header value in the API.</p>

        Raises:
            capo_iot_data_plane.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_iot_data_plane.errors.gateway_timeout_exception.GatewayTimeoutException: <p>The delivery confirmation was not received from the client within the specified timeout period.</p>
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.request_entity_too_large_exception.RequestEntityTooLargeException: <p>The payload exceeds the maximum size allowed.</p>
            capo_iot_data_plane.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.send_direct_message_request.SendDirectMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.send_direct_message_response.SendDirectMessageResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.send_direct_message

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.send_direct_message.async_send_direct_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.send_direct_message_request.SendDirectMessageRequest = {
            "client_id": client_id,
            "topic": topic,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if response_topic is not None:
            input_["response_topic"] = response_topic
        if confirmation is not None:
            input_["confirmation"] = confirmation
        if timeout is not None:
            input_["timeout"] = timeout
        if payload is not None:
            input_["payload"] = payload
        if user_properties is not None:
            input_["user_properties"] = user_properties
        if payload_format_indicator is not None:
            input_["payload_format_indicator"] = payload_format_indicator
        if correlation_data is not None:
            input_["correlation_data"] = correlation_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_thing_shadow(
        self,
        thing_name: "capo_iot_data_plane.types.thing_name.ThingName",
        payload: "capo_iot_data_plane.types.json_document.JsonDocument",
        *,
        config_overrides: Optional[AsyncIoTDataPlaneClientConfig] = None,
        shadow_name: Optional[
            "capo_iot_data_plane.types.shadow_name.ShadowName"
        ] = None,
    ) -> "capo_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse":
        """<p>Updates the shadow for the specified thing.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">UpdateThingShadow</a> action.</p> <p>For more information, see <a href="http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html">UpdateThingShadow</a> in the IoT Developer Guide.</p>

        Args:
            thing_name: <p>The name of the thing.</p>
            shadow_name: <p>The name of the shadow.</p>
            payload: <p>The state information, in JSON format.</p>

        Raises:
            capo_iot_data_plane.errors.conflict_exception.ConflictException: <p>The specified version does not match the version of the document.</p>
            capo_iot_data_plane.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_data_plane.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_data_plane.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The specified combination of HTTP verb and URI is not supported.</p>
            capo_iot_data_plane.errors.request_entity_too_large_exception.RequestEntityTooLargeException: <p>The payload exceeds the maximum size allowed.</p>
            capo_iot_data_plane.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_data_plane.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_data_plane.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_data_plane.errors.unsupported_document_encoding_exception.UnsupportedDocumentEncodingException: <p>The document encoding is not supported.</p>
            capo_iot_data_plane.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_data_plane.types.update_thing_shadow_request.UpdateThingShadowRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_data_plane.types.update_thing_shadow_response.UpdateThingShadowResponse"
        ]:
            import capo_iot_data_plane._operations.iot_moonraker_service.update_thing_shadow

            (
                output,
                http_response,
            ) = await capo_iot_data_plane._operations.iot_moonraker_service.update_thing_shadow.async_update_thing_shadow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_data_plane.types.update_thing_shadow_request.UpdateThingShadowRequest = {
            "thing_name": thing_name,
            "payload": payload,
        }
        if shadow_name is not None:
            input_["shadow_name"] = shadow_name

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
