from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_ecs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_ecs.types.describe_service_deployments_request
    import capo_ecs.types.describe_service_deployments_response
    import capo_ecs.types.string_list
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class ServiceDeploymentResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_service_deployments(
        self,
        service_deployment_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse":
        """<p>Describes one or more of your service deployments.</p> <p>A service deployment happens when you release a software update for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html">View service history using Amazon ECS service deployments</a>.</p>

        Args:
            service_deployment_arns: <p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service deployment
            This example describes a service deployment for the service sd-example in the example cluster.

            >>> client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5'])
            To describe a service deployment with a paused lifecycle hook
            This example describes a service deployment that is currently paused at a lifecycle hook. The lifecycleHookDetails field shows the status of the pause hook, including when it will expire and what action will be taken if the timeout is reached.

            >>> client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments.describe_service_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest = {
            "service_deployment_arns": service_deployment_arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceDeploymentResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_service_deployments(
        self,
        service_deployment_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse":
        """<p>Describes one or more of your service deployments.</p> <p>A service deployment happens when you release a software update for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html">View service history using Amazon ECS service deployments</a>.</p>

        Args:
            service_deployment_arns: <p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service deployment
            This example describes a service deployment for the service sd-example in the example cluster.

            >>> await client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-west-2:123456789012:service-deployment/example/sd-example/NCWGC2ZR-taawPAYrIaU5'])
            To describe a service deployment with a paused lifecycle hook
            This example describes a service deployment that is currently paused at a lifecycle hook. The lifecycleHookDetails field shows the status of the pause hook, including when it will expire and what action will be taken if the timeout is reached.

            >>> await client.describe_service_deployments(service_deployment_arns=['arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_service_deployments_response.DescribeServiceDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_deployments.async_describe_service_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_service_deployments_request.DescribeServiceDeploymentsRequest = {
            "service_deployment_arns": service_deployment_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
