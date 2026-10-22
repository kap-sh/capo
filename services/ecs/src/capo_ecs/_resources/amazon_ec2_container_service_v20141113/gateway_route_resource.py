from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_ecs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.describe_gateway_route_request
    import capo_ecs.types.describe_gateway_route_response
    import capo_ecs.types.gateway_route_status_list
    import capo_ecs.types.gateway_route_summary
    import capo_ecs.types.list_gateway_routes_request
    import capo_ecs.types.list_gateway_routes_response
    import capo_ecs.types.string
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class GatewayRouteResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_gateway_route(
        self,
        gateway_route_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_gateway_route_response.DescribeGatewayRouteResponse":
        """<p>Describes a gateway route, including its status, the service it routes traffic to, and the service-specific infrastructure, such as target groups and listener rules, that the gateway manages for it.</p>

        Args:
            gateway_route_arn: <p>The Amazon Resource Name (ARN) of the gateway route to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a gateway route
            This example describes the specified gateway route, including the service URL and the load balancer resources that the gateway manages for the route.

            >>> client.describe_gateway_route(gateway_route_arn='arn:aws:ecs:us-east-1:123456789012:gateway-route/my-gateway/a1b2c3d4e5f6478890abcdef12345678/f0e1d2c3b4a5968778695a4b3c2d1e0f')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_gateway_route_request.DescribeGatewayRouteRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_gateway_route_response.DescribeGatewayRouteResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_route

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_route.describe_gateway_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGatewayRoute")
        )
        input_: capo_ecs.types.describe_gateway_route_request.DescribeGatewayRouteRequest = {
            "gateway_route_arn": gateway_route_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_routes(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        gateway: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        service: Optional["capo_ecs.types.string.String"] = None,
        service_container_port_name: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.gateway_route_status_list.GatewayRouteStatusList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_gateway_routes_response.ListGatewayRoutesResponse":
        """<p>Returns a list of gateway routes. A gateway route represents the association between a service and a gateway and the service-specific infrastructure the gateway manages for it. You can filter the results by gateway, cluster, service, container port name, and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of a gateway to filter the results by.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of a cluster to filter the results by.</p>
            service: <p>The name or Amazon Resource Name (ARN) of a service to filter the results by. Because services can span clusters, a service name isn't necessarily unique and can match multiple services.</p>
            service_container_port_name: <p>The name of a task definition container port to filter the results by.</p>
            status: <p>The gateway route status to filter the results by.</p>
            max_results: <p>The maximum number of results that the operation returns in a single page. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the gateway routes for a gateway
            This example lists the gateway routes for the gateway named my-gateway in the cluster named my-cluster.

            >>> client.list_gateway_routes(gateway='my-gateway', cluster='my-cluster')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_gateway_routes_request.ListGatewayRoutesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_gateway_routes_response.ListGatewayRoutesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_routes

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_routes.list_gateway_routes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGatewayRoutes")
        )
        input_: capo_ecs.types.list_gateway_routes_request.ListGatewayRoutesRequest = {}
        if gateway is not None:
            input_["gateway"] = gateway
        if cluster is not None:
            input_["cluster"] = cluster
        if service is not None:
            input_["service"] = service
        if service_container_port_name is not None:
            input_["service_container_port_name"] = service_container_port_name
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGatewayRouteResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_gateway_route(
        self,
        gateway_route_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_gateway_route_response.DescribeGatewayRouteResponse":
        """<p>Describes a gateway route, including its status, the service it routes traffic to, and the service-specific infrastructure, such as target groups and listener rules, that the gateway manages for it.</p>

        Args:
            gateway_route_arn: <p>The Amazon Resource Name (ARN) of the gateway route to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a gateway route
            This example describes the specified gateway route, including the service URL and the load balancer resources that the gateway manages for the route.

            >>> await client.describe_gateway_route(gateway_route_arn='arn:aws:ecs:us-east-1:123456789012:gateway-route/my-gateway/a1b2c3d4e5f6478890abcdef12345678/f0e1d2c3b4a5968778695a4b3c2d1e0f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_gateway_route_request.DescribeGatewayRouteRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_gateway_route_response.DescribeGatewayRouteResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_route

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_route.async_describe_gateway_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGatewayRoute")
        )
        input_: capo_ecs.types.describe_gateway_route_request.DescribeGatewayRouteRequest = {
            "gateway_route_arn": gateway_route_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_gateway_routes(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        gateway: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        service: Optional["capo_ecs.types.string.String"] = None,
        service_container_port_name: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.gateway_route_status_list.GatewayRouteStatusList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_gateway_routes_response.ListGatewayRoutesResponse":
        """<p>Returns a list of gateway routes. A gateway route represents the association between a service and a gateway and the service-specific infrastructure the gateway manages for it. You can filter the results by gateway, cluster, service, container port name, and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of a gateway to filter the results by.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of a cluster to filter the results by.</p>
            service: <p>The name or Amazon Resource Name (ARN) of a service to filter the results by. Because services can span clusters, a service name isn't necessarily unique and can match multiple services.</p>
            service_container_port_name: <p>The name of a task definition container port to filter the results by.</p>
            status: <p>The gateway route status to filter the results by.</p>
            max_results: <p>The maximum number of results that the operation returns in a single page. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the gateway routes for a gateway
            This example lists the gateway routes for the gateway named my-gateway in the cluster named my-cluster.

            >>> await client.list_gateway_routes(gateway='my-gateway', cluster='my-cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_gateway_routes_request.ListGatewayRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_gateway_routes_response.ListGatewayRoutesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_routes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_routes.async_list_gateway_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGatewayRoutes")
        )
        input_: capo_ecs.types.list_gateway_routes_request.ListGatewayRoutesRequest = {}
        if gateway is not None:
            input_["gateway"] = gateway
        if cluster is not None:
            input_["cluster"] = cluster
        if service is not None:
            input_["service"] = service
        if service_container_port_name is not None:
            input_["service_container_port_name"] = service_container_port_name
        if status is not None:
            input_["status"] = status
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
