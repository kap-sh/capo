"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RTBFabric``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_rtbfabric._auth._signers
import capo_rtbfabric._auth._sigv4
from capo_rtbfabric._auth._identity import Credentials
from capo_rtbfabric._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rtbfabric._auth._zapros_handler import AuthMiddleware
from capo_rtbfabric._pagination import resolve_path as _resolve_path
from capo_rtbfabric._resources.rtb_fabric.gateway import AsyncGateway
from capo_rtbfabric._resources.rtb_fabric.requester_gateway import AsyncRequesterGateway
from capo_rtbfabric._resources.rtb_fabric.responder_gateway import AsyncResponderGateway
from capo_rtbfabric._services._aws_config import aaws_config
from capo_rtbfabric._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_rtbfabric.types.accept_link_request
    import capo_rtbfabric.types.accept_link_response
    import capo_rtbfabric.types.acm_certificate_arn
    import capo_rtbfabric.types.associate_certificate_request
    import capo_rtbfabric.types.associate_certificate_response
    import capo_rtbfabric.types.certificate_association_summary
    import capo_rtbfabric.types.client_routing_policy
    import capo_rtbfabric.types.create_inbound_external_link_request
    import capo_rtbfabric.types.create_inbound_external_link_response
    import capo_rtbfabric.types.create_link_request
    import capo_rtbfabric.types.create_link_response
    import capo_rtbfabric.types.create_link_routing_rule_request
    import capo_rtbfabric.types.create_link_routing_rule_response
    import capo_rtbfabric.types.create_outbound_external_link_request
    import capo_rtbfabric.types.create_outbound_external_link_response
    import capo_rtbfabric.types.create_requester_gateway_request
    import capo_rtbfabric.types.create_requester_gateway_response
    import capo_rtbfabric.types.create_responder_gateway_request
    import capo_rtbfabric.types.create_responder_gateway_response
    import capo_rtbfabric.types.delete_inbound_external_link_request
    import capo_rtbfabric.types.delete_inbound_external_link_response
    import capo_rtbfabric.types.delete_link_request
    import capo_rtbfabric.types.delete_link_response
    import capo_rtbfabric.types.delete_link_routing_rule_request
    import capo_rtbfabric.types.delete_link_routing_rule_response
    import capo_rtbfabric.types.delete_outbound_external_link_request
    import capo_rtbfabric.types.delete_outbound_external_link_response
    import capo_rtbfabric.types.delete_requester_gateway_request
    import capo_rtbfabric.types.delete_requester_gateway_response
    import capo_rtbfabric.types.delete_responder_gateway_request
    import capo_rtbfabric.types.delete_responder_gateway_response
    import capo_rtbfabric.types.disassociate_certificate_request
    import capo_rtbfabric.types.disassociate_certificate_response
    import capo_rtbfabric.types.domain_name
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.gateway_type
    import capo_rtbfabric.types.get_certificate_association_request
    import capo_rtbfabric.types.get_certificate_association_response
    import capo_rtbfabric.types.get_inbound_external_link_request
    import capo_rtbfabric.types.get_inbound_external_link_response
    import capo_rtbfabric.types.get_link_request
    import capo_rtbfabric.types.get_link_response
    import capo_rtbfabric.types.get_link_routing_rule_request
    import capo_rtbfabric.types.get_link_routing_rule_response
    import capo_rtbfabric.types.get_outbound_external_link_request
    import capo_rtbfabric.types.get_outbound_external_link_response
    import capo_rtbfabric.types.get_requester_gateway_request
    import capo_rtbfabric.types.get_requester_gateway_response
    import capo_rtbfabric.types.get_responder_gateway_request
    import capo_rtbfabric.types.get_responder_gateway_response
    import capo_rtbfabric.types.link_attributes
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_log_settings
    import capo_rtbfabric.types.link_routing_rule_summary
    import capo_rtbfabric.types.link_timeout_in_millis
    import capo_rtbfabric.types.list_certificate_associations_request
    import capo_rtbfabric.types.list_certificate_associations_response
    import capo_rtbfabric.types.list_link_routing_rules_request
    import capo_rtbfabric.types.list_link_routing_rules_response
    import capo_rtbfabric.types.list_links_request
    import capo_rtbfabric.types.list_links_response
    import capo_rtbfabric.types.list_links_response_structure
    import capo_rtbfabric.types.list_requester_gateways_request
    import capo_rtbfabric.types.list_requester_gateways_response
    import capo_rtbfabric.types.list_responder_gateways_request
    import capo_rtbfabric.types.list_responder_gateways_response
    import capo_rtbfabric.types.list_tags_for_resource_request
    import capo_rtbfabric.types.list_tags_for_resource_response
    import capo_rtbfabric.types.listener_config
    import capo_rtbfabric.types.managed_endpoint_configuration
    import capo_rtbfabric.types.module_configuration_list
    import capo_rtbfabric.types.protocol
    import capo_rtbfabric.types.reject_link_request
    import capo_rtbfabric.types.reject_link_response
    import capo_rtbfabric.types.rtb_taggable_resource_arn
    import capo_rtbfabric.types.rule_condition
    import capo_rtbfabric.types.rule_id
    import capo_rtbfabric.types.rule_priority
    import capo_rtbfabric.types.security_group_id_list
    import capo_rtbfabric.types.subnet_id_list
    import capo_rtbfabric.types.tag_key_list
    import capo_rtbfabric.types.tag_resource_request
    import capo_rtbfabric.types.tag_resource_response
    import capo_rtbfabric.types.tags_map
    import capo_rtbfabric.types.trust_store_configuration
    import capo_rtbfabric.types.untag_resource_request
    import capo_rtbfabric.types.untag_resource_response
    import capo_rtbfabric.types.update_link_module_flow_request
    import capo_rtbfabric.types.update_link_module_flow_response
    import capo_rtbfabric.types.update_link_request
    import capo_rtbfabric.types.update_link_response
    import capo_rtbfabric.types.update_link_routing_rule_request
    import capo_rtbfabric.types.update_link_routing_rule_response
    import capo_rtbfabric.types.update_requester_gateway_request
    import capo_rtbfabric.types.update_requester_gateway_response
    import capo_rtbfabric.types.update_responder_gateway_request
    import capo_rtbfabric.types.update_responder_gateway_response
    import capo_rtbfabric.types.url
    import capo_rtbfabric.types.vpc_id


class AsyncRTBFabricClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRTBFabricClient:
    """A client for the ``RTBFabric`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncRTBFabricClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.gateway = AsyncGateway(self)
        self.requester_gateway = AsyncRequesterGateway(self)
        self.responder_gateway = AsyncResponderGateway(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRTBFabricClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRTBFabricClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_requester_gateways(
        self,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rtbfabric.types.list_requester_gateways_response.ListRequesterGatewaysResponse":
        """<p>Lists requester gateways.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>

        Raises:
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List requester gateways with default pagination
            Lists requester gateways using default pagination settings

            >>> await client.list_requester_gateways(max_results=10)
            List requester gateways with pagination token
            Lists requester gateways using a pagination token to get the next page

            >>> await client.list_requester_gateways(max_results=5, next_token='eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7IlMiOiJydGJhcHAtcmVxLTEyMzQ1In19fQ==')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_requester_gateways_request.ListRequesterGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_requester_gateways_response.ListRequesterGatewaysResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_requester_gateways

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_requester_gateways.async_list_requester_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_requester_gateways_request.ListRequesterGatewaysRequest = {}
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

    async def iter_list_requester_gateways(
        self,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_rtbfabric.types.gateway_id.GatewayId]":
        _token = next_token
        while True:
            _response = await self.list_requester_gateways(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("gateway_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_responder_gateways(
        self,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_rtbfabric.types.list_responder_gateways_response.ListResponderGatewaysResponse":
        """<p>Lists reponder gateways.</p>

        Args:
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>

        Raises:
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List responder gateways with default pagination
            Lists responder gateways using default pagination settings

            >>> await client.list_responder_gateways(max_results=10)
            List responder gateways with pagination token
            Lists responder gateways using a pagination token to get the next page

            >>> await client.list_responder_gateways(max_results=3, next_token='eyJsYXN0RXZhbHVhdGVkS2V5Ijp7ImlkIjp7IlMiOiJydGJhcHAtcmVzcC01NDMyMSJ9fX0=')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_responder_gateways_request.ListResponderGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_responder_gateways_response.ListResponderGatewaysResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_responder_gateways

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_responder_gateways.async_list_responder_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_responder_gateways_request.ListResponderGatewaysRequest = {}
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

    async def iter_list_responder_gateways(
        self,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_rtbfabric.types.gateway_id.GatewayId]":
        _token = next_token
        while True:
            _response = await self.list_responder_gateways(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("gateway_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List tags for a resource
            Lists tags for a resource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        tags: "capo_rtbfabric.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Add tags to a resource
            Adds tags to a resource

            >>> await client.tag_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678', tags={'Environment': 'Production', 'Team': 'RTB'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.tag_resource

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_rtbfabric.types.rtb_taggable_resource_arn.RtbTaggableResourceArn",
        tag_keys: "capo_rtbfabric.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The keys of the key-value pairs for the tag or tags you want to remove from the specified resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove tags from a resource
            Removes tags from a resource

            >>> await client.untag_resource(resource_arn='arn:aws:rtbfabric:us-east-1:123456789012:gateway/rtb-gw-12345678', tag_keys=['Environment', 'Team'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.untag_resource

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        peer_gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        log_settings: "capo_rtbfabric.types.link_log_settings.LinkLogSettings",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        attributes: Optional[
            "capo_rtbfabric.types.link_attributes.LinkAttributes"
        ] = None,
        http_responder_allowed: Optional[bool] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
        timeout_in_millis: Optional[
            "capo_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
        ] = None,
    ) -> "capo_rtbfabric.types.create_link_response.CreateLinkResponse":
        """<p>Creates a new link between gateways.</p> <p>Establishes a connection that allows gateways to communicate and exchange bid requests and responses.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            peer_gateway_id: <p>The unique identifier of the peer gateway.</p>
            attributes: <p>Attributes of the link.</p>
            http_responder_allowed: <p>Boolean to specify if an HTTP responder is allowed.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            log_settings: <p>Application log settings for the link. This value is required. Under <code>applicationLogs.sampling</code>, the <code>errorLog</code> and <code>filterLog</code> fields set the percentage of eligible events to log. Valid values range from <code>0</code> through <code>100</code>. To turn off application logs, set both fields to <code>0</code>, as in <code>{"applicationLogs":{"sampling":{"errorLog":0,"filterLog":0}}}</code>.</p>
            timeout_in_millis: <p>The timeout value in milliseconds.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a standard link between gateways
            Creates a new link between two RTB applications. Requires peerGatewayId to specify the target gateway.

            >>> await client.create_link(gateway_id='rtb-gw-12345678', peer_gateway_id='rtb-gw-87654321', log_settings={'applicationLogs': {'sampling': {'errorLog': 100.0, 'filterLog': 0.0}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_link_request.CreateLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_link_response.CreateLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_link.async_create_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_link_request.CreateLinkRequest = {
            "gateway_id": gateway_id,
            "peer_gateway_id": peer_gateway_id,
            "log_settings": log_settings,
        }
        if attributes is not None:
            input_["attributes"] = attributes
        if http_responder_allowed is not None:
            input_["http_responder_allowed"] = http_responder_allowed
        if tags is not None:
            input_["tags"] = tags
        if timeout_in_millis is not None:
            input_["timeout_in_millis"] = timeout_in_millis

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_link_response.GetLinkResponse":
        """<p>Retrieves information about a link between gateways.</p> <p>Returns detailed information about the link configuration, status, and associated gateways.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get link details
            Retrieves details of a specific link

            >>> await client.get_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_link_request.GetLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_link_response.GetLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_link.async_get_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_link_request.GetLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_link_response.DeleteLinkResponse":
        """<p>Deletes a link between gateways.</p> <p>Permanently removes the connection between gateways. This action cannot be undone.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a link
            Deletes an existing link

            >>> await client.delete_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_link_request.DeleteLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_link_response.DeleteLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_link.async_delete_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_link_request.DeleteLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_links(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_rtbfabric.types.list_links_response.ListLinksResponse":
        """<p>Lists links associated with gateways.</p> <p>Returns a list of all links for the specified gateways, including their status and configuration details.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List links for a gateway
            Lists all links for the specified gateway

            >>> await client.list_links(gateway_id='rtb-gw-12345678', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_links_request.ListLinksRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_links_response.ListLinksResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_links

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_links.async_list_links(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_links_request.ListLinksRequest = {
            "gateway_id": gateway_id
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

    async def iter_list_links(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_rtbfabric.types.list_links_response_structure.ListLinksResponseStructure]":
        _token = next_token
        while True:
            _response = await self.list_links(
                gateway_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("links",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def accept_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        log_settings: "capo_rtbfabric.types.link_log_settings.LinkLogSettings",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        attributes: Optional[
            "capo_rtbfabric.types.link_attributes.LinkAttributes"
        ] = None,
        timeout_in_millis: Optional[
            "capo_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
        ] = None,
    ) -> "capo_rtbfabric.types.accept_link_response.AcceptLinkResponse":
        """<p>Accepts a link request between gateways.</p> <p>When a requester gateway requests to link with a responder gateway, the responder can use this operation to accept the link request and establish the connection.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            attributes: <p>Attributes of the link.</p>
            log_settings: <p>Settings for the application logs.</p>
            timeout_in_millis: <p>The timeout value in milliseconds.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Accept a link request
            Accepts a link request from requester gateway

            >>> await client.accept_link(gateway_id='rtb-gw-12345678', link_id='link-87654321', log_settings={'applicationLogs': {'sampling': {'errorLog': 100.0, 'filterLog': 0.0}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.accept_link_request.AcceptLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.accept_link_response.AcceptLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.accept_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.accept_link.async_accept_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.accept_link_request.AcceptLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
            "log_settings": log_settings,
        }
        if attributes is not None:
            input_["attributes"] = attributes
        if timeout_in_millis is not None:
            input_["timeout_in_millis"] = timeout_in_millis

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.reject_link_response.RejectLinkResponse":
        """<p>Rejects a link request between gateways.</p> <p>When a requester gateway requests to link with a responder gateway, the responder can use this operation to decline the link request.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Reject a link request
            Rejects a requested link request

            >>> await client.reject_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.reject_link_request.RejectLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.reject_link_response.RejectLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.reject_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.reject_link.async_reject_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.reject_link_request.RejectLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        log_settings: Optional[
            "capo_rtbfabric.types.link_log_settings.LinkLogSettings"
        ] = None,
        timeout_in_millis: Optional[
            "capo_rtbfabric.types.link_timeout_in_millis.LinkTimeoutInMillis"
        ] = None,
    ) -> "capo_rtbfabric.types.update_link_response.UpdateLinkResponse":
        """<p>Updates the configuration of a link between gateways.</p> <p>Allows you to modify settings and parameters for an existing link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            log_settings: <p>Settings for the application logs.</p>
            timeout_in_millis: <p>The timeout value in milliseconds.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update link settings
            Updates configuration settings for an existing link

            >>> await client.update_link(gateway_id='rtb-gw-12345678', link_id='link-87654321', log_settings={'applicationLogs': {'sampling': {'errorLog': 100.0, 'filterLog': 10.0}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_link_request.UpdateLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_link_response.UpdateLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_link.async_update_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_link_request.UpdateLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }
        if log_settings is not None:
            input_["log_settings"] = log_settings
        if timeout_in_millis is not None:
            input_["timeout_in_millis"] = timeout_in_millis

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_link_module_flow(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        modules: "capo_rtbfabric.types.module_configuration_list.ModuleConfigurationList",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.update_link_module_flow_response.UpdateLinkModuleFlowResponse":
        """<p>Updates a link module flow.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            modules: <p>The configuration of a module.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update link module flow
            Update link module flow for link

            >>> await client.update_link_module_flow(gateway_id='rtb-gw-12345678', link_id='link-87654321', client_token='randomClientToken', modules=[{'name': 'noBidModule', 'version': '1dot0dot0', 'dependsOn': [], 'moduleParameters': {'noBid': {'reason': 'test', 'reasonCode': 1, 'passThroughPercentage': 50.0}}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_link_module_flow_request.UpdateLinkModuleFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_link_module_flow_response.UpdateLinkModuleFlowResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_link_module_flow

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_link_module_flow.async_update_link_module_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_link_module_flow_request.UpdateLinkModuleFlowRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
            "link_id": link_id,
            "modules": modules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_link_routing_rule(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        priority: "capo_rtbfabric.types.rule_priority.RulePriority",
        conditions: "capo_rtbfabric.types.rule_condition.RuleCondition",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "capo_rtbfabric.types.create_link_routing_rule_response.CreateLinkRoutingRuleResponse":
        """<p>Creates a routing rule for a link.</p> <p>Routing rules use priority-based evaluation where lower priority numbers are evaluated first. Each rule specifies conditions that must all match for the rule to apply.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            priority: <p>The priority of the routing rule. Lower numbers are evaluated first. Valid values are 1 to 1000. Priority must be unique among non-deleted rules within a link.</p>
            conditions: <p>The conditions for the routing rule. All specified fields must match for the rule to apply. At least one condition field must be set.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a link routing rule
            Create a routing rule with host header and path prefix conditions

            >>> await client.create_link_routing_rule(gateway_id='rtb-gw-12345678', link_id='link-87654321', priority=10, conditions={'hostHeader': 'api.customer.com', 'pathPrefix': '/openrtb/'}, client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_link_routing_rule_request.CreateLinkRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_link_routing_rule_response.CreateLinkRoutingRuleResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_link_routing_rule

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_link_routing_rule.async_create_link_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_link_routing_rule_request.CreateLinkRoutingRuleRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
            "link_id": link_id,
            "priority": priority,
            "conditions": conditions,
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

    async def get_link_routing_rule(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        rule_id: "capo_rtbfabric.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> (
        "capo_rtbfabric.types.get_link_routing_rule_response.GetLinkRoutingRuleResponse"
    ):
        """<p>Retrieves the details of a routing rule for a link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            rule_id: <p>The unique identifier of the routing rule.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get link routing rule details
            Get details of a link routing rule

            >>> await client.get_link_routing_rule(gateway_id='rtb-gw-12345678', link_id='link-87654321', rule_id='rule-abc123def456')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_link_routing_rule_request.GetLinkRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_link_routing_rule_response.GetLinkRoutingRuleResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_link_routing_rule

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_link_routing_rule.async_get_link_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_link_routing_rule_request.GetLinkRoutingRuleRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
            "rule_id": rule_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_link_routing_rule(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        rule_id: "capo_rtbfabric.types.rule_id.RuleId",
        priority: "capo_rtbfabric.types.rule_priority.RulePriority",
        conditions: "capo_rtbfabric.types.rule_condition.RuleCondition",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.update_link_routing_rule_response.UpdateLinkRoutingRuleResponse":
        """<p>Updates a routing rule for a link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            rule_id: <p>The unique identifier of the routing rule.</p>
            priority: <p>The updated priority of the routing rule. Lower numbers are evaluated first. Valid values are 1 to 1000. Priority must be unique among non-deleted rules within a link.</p>
            conditions: <p>The updated conditions for the routing rule. All specified fields must match for the rule to apply. At least one condition field must be set.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a link routing rule
            Update the conditions of a routing rule

            >>> await client.update_link_routing_rule(gateway_id='rtb-gw-12345678', link_id='link-87654321', rule_id='rule-abc123def456', priority=20, conditions={'hostHeader': 'api.customer.com', 'pathPrefix': '/openrtb/'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_link_routing_rule_request.UpdateLinkRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_link_routing_rule_response.UpdateLinkRoutingRuleResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_link_routing_rule

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_link_routing_rule.async_update_link_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_link_routing_rule_request.UpdateLinkRoutingRuleRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
            "rule_id": rule_id,
            "priority": priority,
            "conditions": conditions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_link_routing_rule(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        rule_id: "capo_rtbfabric.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_link_routing_rule_response.DeleteLinkRoutingRuleResponse":
        """<p>Deletes a routing rule from a link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            rule_id: <p>The unique identifier of the routing rule.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a link routing rule
            Delete a link routing rule

            >>> await client.delete_link_routing_rule(gateway_id='rtb-gw-12345678', link_id='link-87654321', rule_id='rule-abc123def456')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_link_routing_rule_request.DeleteLinkRoutingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_link_routing_rule_response.DeleteLinkRoutingRuleResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_link_routing_rule

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_link_routing_rule.async_delete_link_routing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_link_routing_rule_request.DeleteLinkRoutingRuleRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
            "rule_id": rule_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_link_routing_rules(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_rtbfabric.types.list_link_routing_rules_response.ListLinkRoutingRulesResponse":
        """<p>Lists the routing rules for a link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List link routing rules
            List all routing rules for a link

            >>> await client.list_link_routing_rules(gateway_id='rtb-gw-12345678', link_id='link-87654321', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_link_routing_rules_request.ListLinkRoutingRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_link_routing_rules_response.ListLinkRoutingRulesResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_link_routing_rules

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_link_routing_rules.async_list_link_routing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_link_routing_rules_request.ListLinkRoutingRulesRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
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

    async def iter_list_link_routing_rules(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_rtbfabric.types.link_routing_rule_summary.LinkRoutingRuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_link_routing_rules(
                gateway_id,
                link_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_requester_gateway(
        self,
        vpc_id: "capo_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "capo_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse":
        """<p>Creates a requester gateway.</p>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            description: <p>An optional description for the requester gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a requester gateway
            Create requester gateway

            >>> await client.create_requester_gateway(description='My requester gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_requester_gateway.async_create_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_requester_gateway(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse":
        """<p>Retrieves information about a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get requester gateway details
            Get requester gateway

            >>> await client.get_requester_gateway(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_requester_gateway.async_get_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_requester_gateway(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse":
        """<p>Deletes a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a requester gateway
            Delete requester gateway

            >>> await client.delete_requester_gateway(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_requester_gateway.async_delete_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_requester_gateway(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        description: Optional[str] = None,
    ) -> "capo_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse":
        """<p>Updates a requester gateway.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the requester gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update requester gateway
            Update requester gateway

            >>> await client.update_requester_gateway(gateway_id='rtb-gw-12345678', description='Updated requester gateway description', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_requester_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_requester_gateway.async_update_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_outbound_external_link(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        public_endpoint: "capo_rtbfabric.types.url.URL",
        log_settings: "capo_rtbfabric.types.link_log_settings.LinkLogSettings",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        attributes: Optional[
            "capo_rtbfabric.types.link_attributes.LinkAttributes"
        ] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "capo_rtbfabric.types.create_outbound_external_link_response.CreateOutboundExternalLinkResponse":
        """<p>Creates an outbound external link.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            attributes: <p>Attributes of the link.</p>
            public_endpoint: <p>The public endpoint of the link.</p>
            log_settings: <p>Settings for the application logs.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an outbound external link
            Create an outbound external link for a requester gateway to connect to external public responder endpoints

            >>> await client.create_outbound_external_link(gateway_id='rtb-gw-12345678', public_endpoint='https://external-responder.example.com', client_token='12345678-1234-1234-1234-123456789012', log_settings={'applicationLogs': {'sampling': {'errorLog': 100.0, 'filterLog': 0.0}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_outbound_external_link_request.CreateOutboundExternalLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_outbound_external_link_response.CreateOutboundExternalLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_outbound_external_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_outbound_external_link.async_create_outbound_external_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_outbound_external_link_request.CreateOutboundExternalLinkRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
            "public_endpoint": public_endpoint,
            "log_settings": log_settings,
        }
        if attributes is not None:
            input_["attributes"] = attributes
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_outbound_external_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_outbound_external_link_response.DeleteOutboundExternalLinkResponse":
        """<p>Deletes an outbound external link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an outbound external link
            Delete an outbound external link

            >>> await client.delete_outbound_external_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_outbound_external_link_request.DeleteOutboundExternalLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_outbound_external_link_response.DeleteOutboundExternalLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_outbound_external_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_outbound_external_link.async_delete_outbound_external_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_outbound_external_link_request.DeleteOutboundExternalLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_outbound_external_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_outbound_external_link_response.GetOutboundExternalLinkResponse":
        """<p>Retrieves information about an outbound external link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get outbound external link details
            Get details of a specific outbound external link

            >>> await client.get_outbound_external_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_outbound_external_link_request.GetOutboundExternalLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_outbound_external_link_response.GetOutboundExternalLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_outbound_external_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_outbound_external_link.async_get_outbound_external_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_outbound_external_link_request.GetOutboundExternalLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_responder_gateway(
        self,
        vpc_id: "capo_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "capo_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        port: int,
        protocol: "capo_rtbfabric.types.protocol.Protocol",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        domain_name: Optional["capo_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "capo_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
        gateway_type: Optional["capo_rtbfabric.types.gateway_type.GatewayType"] = None,
        client_routing_policy: Optional[
            "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
        ] = None,
    ) -> "capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse":
        """<p>Creates a responder gateway.</p> <important> <p>A domain name or managed endpoint is required.</p> </important>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>Unique identifiers of the subnets. A service quota for your account sets the number of Availability Zones that your subnets can span. By default, this quota is one Availability Zone. To span more Availability Zones, request a quota increase.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            description: <p>An optional description for the responder gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            gateway_type: <p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>
            client_routing_policy: <p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, RTB Fabric uses <code>AVAILABILITY_ZONE_AFFINITY</code>. To get the behavior of <code>ANY_AVAILABILITY_ZONE</code>, create the gateway with subnets in more than one Availability Zone. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a responder gateway
            Create responder gateway

            >>> await client.create_responder_gateway(description='My responder gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], port=443, protocol='HTTPS', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_responder_gateway.async_create_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
            "port": port,
            "protocol": protocol,
            "client_token": client_token,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if gateway_type is not None:
            input_["gateway_type"] = gateway_type
        if client_routing_policy is not None:
            input_["client_routing_policy"] = client_routing_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_responder_gateway(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse":
        """<p>Retrieves information about a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get responder gateway details
            Get responder gateway

            >>> await client.get_responder_gateway(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_responder_gateway.async_get_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_responder_gateway(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse":
        """<p>Deletes a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a responder gateway
            Delete responder gateway

            >>> await client.delete_responder_gateway(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_responder_gateway.async_delete_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_certificate(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse":
        """<p>Associates an ACM certificate with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to associate.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate a certificate with a responder gateway
            Associate an ACM certificate with a responder gateway

            >>> await client.associate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.associate_certificate

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.associate_certificate.async_associate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_certificate(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """<p>Removes a certificate association from a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to disassociate.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Disassociate a certificate from a responder gateway
            Remove an ACM certificate association from a responder gateway

            >>> await client.disassociate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.disassociate_certificate

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.disassociate_certificate.async_disassociate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_certificate_association(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "capo_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse":
        """<p>Retrieves the details of a certificate association with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get certificate association details from a responder gateway
            Retrieve details of an ACM certificate association with a responder gateway

            >>> await client.get_certificate_association(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_certificate_association

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_certificate_association.async_get_certificate_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest = {
            "gateway_id": gateway_id,
            "acm_certificate_arn": acm_certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_certificate_associations(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse":
        """<p>Lists the certificate associations for a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List certificate associations for a responder gateway
            Retrieve all certificate associations for a responder gateway

            >>> await client.list_certificate_associations(gateway_id='rtb-gw-12345678', max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.list_certificate_associations

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.list_certificate_associations.async_list_certificate_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest = {
            "gateway_id": gateway_id
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

    async def iter_list_certificate_associations(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_rtbfabric.types.certificate_association_summary.CertificateAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_certificate_associations(
                gateway_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("certificate_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_responder_gateway(
        self,
        port: int,
        protocol: "capo_rtbfabric.types.protocol.Protocol",
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        domain_name: Optional["capo_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "capo_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "capo_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "capo_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        client_routing_policy: Optional[
            "capo_rtbfabric.types.client_routing_policy.ClientRoutingPolicy"
        ] = None,
    ) -> "capo_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse":
        """<p>Updates the description, Auto Scaling group managed endpoint configuration, trust store configuration, and client routing policy of a responder gateway. This operation also updates the <code>protocols</code> list in the listener configuration.</p> <p>You cannot change the <code>domainName</code>, <code>port</code>, and <code>protocol</code> values that you set when you create a responder gateway. To change any of them, delete the gateway and create a new one.</p>

        Args:
            domain_name: <p>Domain name for the responder gateway. This operation does not change the domain name of an existing gateway. To use a different domain name, delete the gateway and create a new one.</p>
            port: <p>Networking port to use. This operation does not change the port of an existing gateway. To use a different port, delete the gateway and create a new one.</p>
            protocol: <p>Networking protocol to use. This operation does not change the protocol of an existing gateway. To use a different protocol, delete the gateway and create a new one.</p>
            listener_config: <p>The listener configuration for the responder gateway.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the responder gateway.</p>
            client_routing_policy: <p>The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. Valid values are the following:</p> <ul> <li> <p> <code>AVAILABILITY_ZONE_AFFINITY</code>: RTB Fabric routes each requester's traffic to gateway capacity in the requester's own Availability Zone when the gateway has capacity available there. Otherwise, RTB Fabric routes the traffic to gateway capacity in the other Availability Zones of the gateway.</p> </li> <li> <p> <code>ANY_AVAILABILITY_ZONE</code>: RTB Fabric routes each requester's traffic to gateway capacity in every Availability Zone that the subnets of the gateway span. The Availability Zone that the requester is in does not change this.</p> </li> </ul> <p>If you don't specify a value, the gateway keeps its current client routing policy. Changing the policy sets the gateway status to <code>PENDING_UPDATE</code> until the change is complete. RTB Fabric does not support partial Availability Zone affinity, so <code>PARTIAL_AVAILABILITY_ZONE_AFFINITY</code> is not a valid value. For more information, see <a href="https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity">Configuring Availability Zone affinity</a> in the <i>Amazon Web Services RTB Fabric User Guide</i>.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update responder gateway
            Update responder gateway

            >>> await client.update_responder_gateway(gateway_id='rtb-gw-12345678', description='Updated responder gateway description', port=8080, protocol='HTTP', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.update_responder_gateway

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.update_responder_gateway.async_update_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest = {
            "port": port,
            "protocol": protocol,
            "client_token": client_token,
            "gateway_id": gateway_id,
        }
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        if description is not None:
            input_["description"] = description
        if client_routing_policy is not None:
            input_["client_routing_policy"] = client_routing_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_inbound_external_link(
        self,
        client_token: str,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        log_settings: "capo_rtbfabric.types.link_log_settings.LinkLogSettings",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        attributes: Optional[
            "capo_rtbfabric.types.link_attributes.LinkAttributes"
        ] = None,
        tags: Optional["capo_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "capo_rtbfabric.types.create_inbound_external_link_response.CreateInboundExternalLinkResponse":
        """<p>Creates an inbound external link.</p>

        Args:
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            attributes: <p>Attributes of the link.</p>
            log_settings: <p>Settings for the application logs.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because you exceeded a service quota.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an inbound external link
            Create an inbound external link for a responder gateway

            >>> await client.create_inbound_external_link(gateway_id='rtb-gw-12345678', client_token='randomClientToken', log_settings={'applicationLogs': {'sampling': {'errorLog': 100.0, 'filterLog': 0.0}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.create_inbound_external_link_request.CreateInboundExternalLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.create_inbound_external_link_response.CreateInboundExternalLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.create_inbound_external_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.create_inbound_external_link.async_create_inbound_external_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.create_inbound_external_link_request.CreateInboundExternalLinkRequest = {
            "client_token": client_token,
            "gateway_id": gateway_id,
            "log_settings": log_settings,
        }
        if attributes is not None:
            input_["attributes"] = attributes
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_inbound_external_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.delete_inbound_external_link_response.DeleteInboundExternalLinkResponse":
        """<p>Deletes an inbound external link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.conflict_exception.ConflictException: <p>The request could not be completed because of a conflict in the current state of the resource.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an inbound external link
            Delete an inbound external link

            >>> await client.delete_inbound_external_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.delete_inbound_external_link_request.DeleteInboundExternalLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.delete_inbound_external_link_response.DeleteInboundExternalLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.delete_inbound_external_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.delete_inbound_external_link.async_delete_inbound_external_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.delete_inbound_external_link_request.DeleteInboundExternalLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_inbound_external_link(
        self,
        gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId",
        link_id: "capo_rtbfabric.types.link_id.LinkId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "capo_rtbfabric.types.get_inbound_external_link_response.GetInboundExternalLinkResponse":
        """<p>Retrieves information about an inbound external link.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            link_id: <p>The unique identifier of the link.</p>

        Raises:
            capo_rtbfabric.errors.access_denied_exception.AccessDeniedException: <p>The request could not be completed because you do not have sufficient access to perform this action.</p>
            capo_rtbfabric.errors.internal_server_exception.InternalServerException: <p>The request could not be completed because of an internal server error. Try your call again.</p>
            capo_rtbfabric.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request could not be completed because the resource does not exist.</p>
            capo_rtbfabric.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_rtbfabric.errors.validation_exception.ValidationException: <p>The request could not be completed because it fails satisfy the constraints specified by the service.</p>
            capo_rtbfabric.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get inbound external link details
            Get details of an inbound external link

            >>> await client.get_inbound_external_link(gateway_id='rtb-gw-12345678', link_id='link-87654321')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rtbfabric.types.get_inbound_external_link_request.GetInboundExternalLinkRequest]",
        ) -> AsyncOperationResponse[
            "capo_rtbfabric.types.get_inbound_external_link_response.GetInboundExternalLinkResponse"
        ]:
            import capo_rtbfabric._operations.rtb_fabric.get_inbound_external_link

            (
                output,
                http_response,
            ) = await capo_rtbfabric._operations.rtb_fabric.get_inbound_external_link.async_get_inbound_external_link(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rtbfabric.types.get_inbound_external_link_request.GetInboundExternalLinkRequest = {
            "gateway_id": gateway_id,
            "link_id": link_id,
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
