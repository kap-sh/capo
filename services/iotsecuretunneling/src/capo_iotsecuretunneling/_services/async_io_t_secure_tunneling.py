"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#IoTSecuredTunneling``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iotsecuretunneling._auth._signers
import capo_iotsecuretunneling._auth._sigv4
from capo_iotsecuretunneling._auth._identity import Credentials
from capo_iotsecuretunneling._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iotsecuretunneling._auth._zapros_handler import AuthMiddleware
from capo_iotsecuretunneling._pagination import resolve_path as _resolve_path
from capo_iotsecuretunneling._services._aws_config import aaws_config
from capo_iotsecuretunneling._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.amazon_resource_name
    import capo_iotsecuretunneling.types.client_mode
    import capo_iotsecuretunneling.types.close_tunnel_request
    import capo_iotsecuretunneling.types.close_tunnel_response
    import capo_iotsecuretunneling.types.delete_flag
    import capo_iotsecuretunneling.types.describe_tunnel_request
    import capo_iotsecuretunneling.types.describe_tunnel_response
    import capo_iotsecuretunneling.types.description
    import capo_iotsecuretunneling.types.destination_config
    import capo_iotsecuretunneling.types.list_tags_for_resource_request
    import capo_iotsecuretunneling.types.list_tags_for_resource_response
    import capo_iotsecuretunneling.types.list_tunnels_request
    import capo_iotsecuretunneling.types.list_tunnels_response
    import capo_iotsecuretunneling.types.max_results
    import capo_iotsecuretunneling.types.next_token
    import capo_iotsecuretunneling.types.open_tunnel_request
    import capo_iotsecuretunneling.types.open_tunnel_response
    import capo_iotsecuretunneling.types.rotate_tunnel_access_token_request
    import capo_iotsecuretunneling.types.rotate_tunnel_access_token_response
    import capo_iotsecuretunneling.types.tag_key_list
    import capo_iotsecuretunneling.types.tag_list
    import capo_iotsecuretunneling.types.tag_resource_request
    import capo_iotsecuretunneling.types.tag_resource_response
    import capo_iotsecuretunneling.types.thing_name
    import capo_iotsecuretunneling.types.timeout_config
    import capo_iotsecuretunneling.types.tunnel_id
    import capo_iotsecuretunneling.types.untag_resource_request
    import capo_iotsecuretunneling.types.untag_resource_response


class AsyncIoTSecureTunnelingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncIoTSecureTunnelingClient:
    """A client for the ``IoTSecureTunneling`` service.

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
        self._config = AsyncIoTSecureTunnelingClientConfig(
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
        self, config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTSecureTunnelingClientConfig = config_overrides or {}
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

    async def close_tunnel(
        self,
        tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId",
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
        delete: Optional["capo_iotsecuretunneling.types.delete_flag.DeleteFlag"] = None,
    ) -> "capo_iotsecuretunneling.types.close_tunnel_response.CloseTunnelResponse":
        """<p>Closes a tunnel identified by the unique tunnel id. When a <code>CloseTunnel</code> request is received, we close the WebSocket connections between the client and proxy server so no data can be transmitted.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">CloseTunnel</a> action.</p>

        Args:
            tunnel_id: <p>The ID of the tunnel to close.</p>
            delete: <p>When set to true, IoT Secure Tunneling deletes the tunnel data immediately.</p>

        Raises:
            capo_iotsecuretunneling.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when an operation is attempted on a resource that does not exist.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.close_tunnel_request.CloseTunnelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.close_tunnel_response.CloseTunnelResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.close_tunnel

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.close_tunnel.async_close_tunnel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.close_tunnel_request.CloseTunnelRequest = {
            "tunnel_id": tunnel_id
        }
        if delete is not None:
            input_["delete"] = delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_tunnel(
        self,
        tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId",
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
    ) -> (
        "capo_iotsecuretunneling.types.describe_tunnel_response.DescribeTunnelResponse"
    ):
        """<p>Gets information about a tunnel identified by the unique tunnel id.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">DescribeTunnel</a> action.</p>

        Args:
            tunnel_id: <p>The tunnel to describe.</p>

        Raises:
            capo_iotsecuretunneling.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when an operation is attempted on a resource that does not exist.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.describe_tunnel_request.DescribeTunnelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.describe_tunnel_response.DescribeTunnelResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.describe_tunnel

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.describe_tunnel.async_describe_tunnel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.describe_tunnel_request.DescribeTunnelRequest = {
            "tunnel_id": tunnel_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
    ) -> "capo_iotsecuretunneling.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>

        Raises:
            capo_iotsecuretunneling.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when an operation is attempted on a resource that does not exist.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tunnels(
        self,
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
        thing_name: Optional[
            "capo_iotsecuretunneling.types.thing_name.ThingName"
        ] = None,
        max_results: Optional[
            "capo_iotsecuretunneling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsecuretunneling.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iotsecuretunneling.types.list_tunnels_response.ListTunnelsResponse":
        """<p>List all tunnels for an Amazon Web Services account. Tunnels are listed by creation time in descending order, newer tunnels will be listed before older tunnels.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">ListTunnels</a> action.</p>

        Args:
            thing_name: <p>The name of the IoT thing associated with the destination device.</p>
            max_results: <p>The maximum number of results to return at once.</p>
            next_token: <p>To retrieve the next set of results, the nextToken value from a previous response; otherwise null to receive the first set of results.</p>

        Raises:
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.list_tunnels_request.ListTunnelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.list_tunnels_response.ListTunnelsResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.list_tunnels

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.list_tunnels.async_list_tunnels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.list_tunnels_request.ListTunnelsRequest = {}
        if thing_name is not None:
            input_["thing_name"] = thing_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tunnels(
        self,
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
        thing_name: Optional[
            "capo_iotsecuretunneling.types.thing_name.ThingName"
        ] = None,
        max_results: Optional[
            "capo_iotsecuretunneling.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsecuretunneling.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iotsecuretunneling.types.list_tunnels_response.ListTunnelsResponse]":
        _token = next_token
        while True:
            _response = await self.list_tunnels(
                config_overrides=config_overrides,
                thing_name=thing_name,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def open_tunnel(
        self,
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
        description: Optional[
            "capo_iotsecuretunneling.types.description.Description"
        ] = None,
        tags: Optional["capo_iotsecuretunneling.types.tag_list.TagList"] = None,
        destination_config: Optional[
            "capo_iotsecuretunneling.types.destination_config.DestinationConfig"
        ] = None,
        timeout_config: Optional[
            "capo_iotsecuretunneling.types.timeout_config.TimeoutConfig"
        ] = None,
    ) -> "capo_iotsecuretunneling.types.open_tunnel_response.OpenTunnelResponse":
        """<p>Creates a new tunnel, and returns two client access tokens for clients to use to connect to the IoT Secure Tunneling proxy server.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">OpenTunnel</a> action.</p>

        Args:
            description: <p>A short text description of the tunnel. </p>
            tags: <p>A collection of tag metadata.</p>
            destination_config: <p>The destination configuration for the OpenTunnel request.</p>
            timeout_config: <p>Timeout configuration for a tunnel.</p>

        Raises:
            capo_iotsecuretunneling.errors.limit_exceeded_exception.LimitExceededException: <p>Thrown when a tunnel limit is exceeded.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.open_tunnel_request.OpenTunnelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.open_tunnel_response.OpenTunnelResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.open_tunnel

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.open_tunnel.async_open_tunnel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.open_tunnel_request.OpenTunnelRequest = {}
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if destination_config is not None:
            input_["destination_config"] = destination_config
        if timeout_config is not None:
            input_["timeout_config"] = timeout_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rotate_tunnel_access_token(
        self,
        tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId",
        client_mode: "capo_iotsecuretunneling.types.client_mode.ClientMode",
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
        destination_config: Optional[
            "capo_iotsecuretunneling.types.destination_config.DestinationConfig"
        ] = None,
    ) -> "capo_iotsecuretunneling.types.rotate_tunnel_access_token_response.RotateTunnelAccessTokenResponse":
        """<p>Revokes the current client access token (CAT) and returns new CAT for clients to use when reconnecting to secure tunneling to access the same tunnel.</p> <p>Requires permission to access the <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions">RotateTunnelAccessToken</a> action.</p> <note> <p>Rotating the CAT doesn't extend the tunnel duration. For example, say the tunnel duration is 12 hours and the tunnel has already been open for 4 hours. When you rotate the access tokens, the new tokens that are generated can only be used for the remaining 8 hours.</p> </note>

        Args:
            tunnel_id: <p>The tunnel for which you want to rotate the access tokens.</p>
            client_mode: <p>The mode of the client that will use the client token, which can be either the source or destination, or both source and destination.</p>

        Raises:
            capo_iotsecuretunneling.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when an operation is attempted on a resource that does not exist.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.rotate_tunnel_access_token_request.RotateTunnelAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.rotate_tunnel_access_token_response.RotateTunnelAccessTokenResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.rotate_tunnel_access_token

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.rotate_tunnel_access_token.async_rotate_tunnel_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.rotate_tunnel_access_token_request.RotateTunnelAccessTokenRequest = {
            "tunnel_id": tunnel_id,
            "client_mode": client_mode,
        }
        if destination_config is not None:
            input_["destination_config"] = destination_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_iotsecuretunneling.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
    ) -> "capo_iotsecuretunneling.types.tag_resource_response.TagResourceResponse":
        """<p>A resource tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags for the resource.</p>

        Raises:
            capo_iotsecuretunneling.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when an operation is attempted on a resource that does not exist.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.tag_resource

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_iotsecuretunneling.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTSecureTunnelingClientConfig] = None,
    ) -> "capo_iotsecuretunneling.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The keys of the tags to remove.</p>

        Raises:
            capo_iotsecuretunneling.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when an operation is attempted on a resource that does not exist.</p>
            capo_iotsecuretunneling.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsecuretunneling.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsecuretunneling.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iotsecuretunneling._operations.io_t_secured_tunneling.untag_resource

            (
                output,
                http_response,
            ) = await capo_iotsecuretunneling._operations.io_t_secured_tunneling.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsecuretunneling.types.untag_resource_request.UntagResourceRequest = {
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
