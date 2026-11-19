from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_route53globalresolver._auth._signers
import capo_route53globalresolver._auth._sigv4
from capo_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items
    import capo_route53globalresolver.types.core_network_endpoints_item
    import capo_route53globalresolver.types.create_core_network_endpoint_input
    import capo_route53globalresolver.types.create_core_network_endpoint_output
    import capo_route53globalresolver.types.delete_core_network_endpoint_input
    import capo_route53globalresolver.types.delete_core_network_endpoint_output
    import capo_route53globalresolver.types.filters
    import capo_route53globalresolver.types.get_core_network_endpoint_input
    import capo_route53globalresolver.types.get_core_network_endpoint_output
    import capo_route53globalresolver.types.list_core_network_endpoints_input
    import capo_route53globalresolver.types.list_core_network_endpoints_output
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.tags
    import capo_route53globalresolver.types.update_core_network_endpoint_input
    import capo_route53globalresolver.types.update_core_network_endpoint_output
    import capo_route53globalresolver.types.update_ip_address_list
    from capo_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from capo_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class CoreNetworkEndpoint:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        core_network_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        ip_addresses: "capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items.CoreNetworkEndpointDnsIpInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_core_network_endpoint_output.CreateCoreNetworkEndpointOutput":
        """<p>Creates a core network endpoint, which enables DNS resolution for Amazon Web Services Cloud WAN core network segments. The endpoint connects a Route 53 Global Resolver to an Amazon Web Services Cloud WAN core network so that resources attached to the core network can send DNS queries to the resolver.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier that ensures the request is idempotent. Making the same request multiple times with the same <code>clientToken</code> produces the same result every time.</p>
            core_network_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Cloud WAN core network to connect to this endpoint.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to associate with this core network endpoint.</p>
            ip_addresses: <p>The IP addresses that the core network endpoint uses to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>
            name: <p>A descriptive name for the core network endpoint.</p>
            tags: <p>An array of user-defined keys and optional values that you can use to categorize and organize the core network endpoint.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.create_core_network_endpoint_input.CreateCoreNetworkEndpointInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.create_core_network_endpoint_output.CreateCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_core_network_endpoint

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_core_network_endpoint.create_core_network_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.create_core_network_endpoint_input.CreateCoreNetworkEndpointInput = {
            "core_network_arn": core_network_arn,
            "global_resolver_id": global_resolver_id,
            "ip_addresses": ip_addresses,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    def read(
        self,
        core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_core_network_endpoint_output.GetCoreNetworkEndpointOutput":
        """<p>Retrieves information about a core network endpoint.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            core_network_endpoint_id: <p>The unique identifier of the core network endpoint to retrieve information about.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.get_core_network_endpoint_input.GetCoreNetworkEndpointInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.get_core_network_endpoint_output.GetCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_core_network_endpoint

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_core_network_endpoint.get_core_network_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.get_core_network_endpoint_input.GetCoreNetworkEndpointInput = {
            "core_network_endpoint_id": core_network_endpoint_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        update_ip_addresses: Optional[
            "capo_route53globalresolver.types.update_ip_address_list.UpdateIpAddressList"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_core_network_endpoint_output.UpdateCoreNetworkEndpointOutput":
        """<p>Updates the configuration of a core network endpoint. You can change the name and modify the IP addresses that the endpoint uses for DNS resolution.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            core_network_endpoint_id: <p>The unique identifier of the core network endpoint to update.</p>
            name: <p>The name of the core network endpoint.</p>
            update_ip_addresses: <p>The IP address changes to apply to the core network endpoint. Use this parameter to add or remove the IP addresses that the endpoint uses to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.update_core_network_endpoint_input.UpdateCoreNetworkEndpointInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.update_core_network_endpoint_output.UpdateCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_core_network_endpoint

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_core_network_endpoint.update_core_network_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.update_core_network_endpoint_input.UpdateCoreNetworkEndpointInput = {
            "core_network_endpoint_id": core_network_endpoint_id
        }
        if name is not None:
            input_["name"] = name
        if update_ip_addresses is not None:
            input_["update_ip_addresses"] = update_ip_addresses

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_core_network_endpoint_output.DeleteCoreNetworkEndpointOutput":
        """<p>Deletes a core network endpoint. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            core_network_endpoint_id: <p>The unique identifier of the core network endpoint to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.delete_core_network_endpoint_input.DeleteCoreNetworkEndpointInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.delete_core_network_endpoint_output.DeleteCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_core_network_endpoint

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_core_network_endpoint.delete_core_network_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.delete_core_network_endpoint_input.DeleteCoreNetworkEndpointInput = {
            "core_network_endpoint_id": core_network_endpoint_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_core_network_endpoints_output.ListCoreNetworkEndpointsOutput":
        """<p>Lists the core network endpoints in your Amazon Web Services account, with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_core_network_endpoints_input.ListCoreNetworkEndpointsInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_core_network_endpoints_output.ListCoreNetworkEndpointsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_core_network_endpoints

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_core_network_endpoints.list_core_network_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCoreNetworkEndpoints")
        )
        input_: capo_route53globalresolver.types.list_core_network_endpoints_input.ListCoreNetworkEndpointsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCoreNetworkEndpoint:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        core_network_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn",
        global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        ip_addresses: "capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items.CoreNetworkEndpointDnsIpInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_route53globalresolver.types.tags.Tags"] = None,
    ) -> "capo_route53globalresolver.types.create_core_network_endpoint_output.CreateCoreNetworkEndpointOutput":
        """<p>Creates a core network endpoint, which enables DNS resolution for Amazon Web Services Cloud WAN core network segments. The endpoint connects a Route 53 Global Resolver to an Amazon Web Services Cloud WAN core network so that resources attached to the core network can send DNS queries to the resolver.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier that ensures the request is idempotent. Making the same request multiple times with the same <code>clientToken</code> produces the same result every time.</p>
            core_network_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Cloud WAN core network to connect to this endpoint.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to associate with this core network endpoint.</p>
            ip_addresses: <p>The IP addresses that the core network endpoint uses to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>
            name: <p>A descriptive name for the core network endpoint.</p>
            tags: <p>An array of user-defined keys and optional values that you can use to categorize and organize the core network endpoint.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_core_network_endpoint_input.CreateCoreNetworkEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_core_network_endpoint_output.CreateCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_core_network_endpoint

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_core_network_endpoint.async_create_core_network_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.create_core_network_endpoint_input.CreateCoreNetworkEndpointInput = {
            "core_network_arn": core_network_arn,
            "global_resolver_id": global_resolver_id,
            "ip_addresses": ip_addresses,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    async def read(
        self,
        core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_core_network_endpoint_output.GetCoreNetworkEndpointOutput":
        """<p>Retrieves information about a core network endpoint.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            core_network_endpoint_id: <p>The unique identifier of the core network endpoint to retrieve information about.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_core_network_endpoint_input.GetCoreNetworkEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_core_network_endpoint_output.GetCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_core_network_endpoint

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_core_network_endpoint.async_get_core_network_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.get_core_network_endpoint_input.GetCoreNetworkEndpointInput = {
            "core_network_endpoint_id": core_network_endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        update_ip_addresses: Optional[
            "capo_route53globalresolver.types.update_ip_address_list.UpdateIpAddressList"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_core_network_endpoint_output.UpdateCoreNetworkEndpointOutput":
        """<p>Updates the configuration of a core network endpoint. You can change the name and modify the IP addresses that the endpoint uses for DNS resolution.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            core_network_endpoint_id: <p>The unique identifier of the core network endpoint to update.</p>
            name: <p>The name of the core network endpoint.</p>
            update_ip_addresses: <p>The IP address changes to apply to the core network endpoint. Use this parameter to add or remove the IP addresses that the endpoint uses to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_core_network_endpoint_input.UpdateCoreNetworkEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_core_network_endpoint_output.UpdateCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_core_network_endpoint

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_core_network_endpoint.async_update_core_network_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.update_core_network_endpoint_input.UpdateCoreNetworkEndpointInput = {
            "core_network_endpoint_id": core_network_endpoint_id
        }
        if name is not None:
            input_["name"] = name
        if update_ip_addresses is not None:
            input_["update_ip_addresses"] = update_ip_addresses

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        core_network_endpoint_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_core_network_endpoint_output.DeleteCoreNetworkEndpointOutput":
        """<p>Deletes a core network endpoint. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            core_network_endpoint_id: <p>The unique identifier of the core network endpoint to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_core_network_endpoint_input.DeleteCoreNetworkEndpointInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_core_network_endpoint_output.DeleteCoreNetworkEndpointOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_core_network_endpoint

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_core_network_endpoint.async_delete_core_network_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCoreNetworkEndpoint")
        )
        input_: capo_route53globalresolver.types.delete_core_network_endpoint_input.DeleteCoreNetworkEndpointInput = {
            "core_network_endpoint_id": core_network_endpoint_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_core_network_endpoints_output.ListCoreNetworkEndpointsOutput":
        """<p>Lists the core network endpoints in your Amazon Web Services account, with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions, but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_core_network_endpoints_input.ListCoreNetworkEndpointsInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_core_network_endpoints_output.ListCoreNetworkEndpointsOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_core_network_endpoints

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_core_network_endpoints.async_list_core_network_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCoreNetworkEndpoints")
        )
        input_: capo_route53globalresolver.types.list_core_network_endpoints_input.ListCoreNetworkEndpointsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
