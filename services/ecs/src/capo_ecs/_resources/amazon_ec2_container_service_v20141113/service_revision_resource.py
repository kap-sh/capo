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
    import capo_ecs.types.describe_service_revisions_request
    import capo_ecs.types.describe_service_revisions_response
    import capo_ecs.types.string_list
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class ServiceRevisionResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_service_revisions(
        self,
        service_revision_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse":
        """<p>Describes one or more service revisions.</p> <p>A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html">Amazon ECS service revisions</a>.</p> <p>You can't describe a service revision that was created before October 25, 2024.</p>

        Args:
            service_revision_arns: <p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html">ListServiceDeployments</a> to get the ARNs.</p>

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
            To describe a service revision
            This example describes a service revision with the specified ARN

            >>> client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095'])
            To describe a service revision with a monitoring configuration
            This example describes a service revision that has a monitoring configuration with 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics.

            >>> client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-east-1:012345678910:service-revision/default/ecs-monitored-service/8675309012345678901'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions.describe_service_revisions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest = {
            "service_revision_arns": service_revision_arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceRevisionResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_service_revisions(
        self,
        service_revision_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse":
        """<p>Describes one or more service revisions.</p> <p>A service revision is a version of the service that includes the values for the Amazon ECS resources (for example, task definition) and the environment resources (for example, load balancers, subnets, and security groups). For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html">Amazon ECS service revisions</a>.</p> <p>You can't describe a service revision that was created before October 25, 2024.</p>

        Args:
            service_revision_arns: <p>The ARN of the service revision. </p> <p>You can specify a maximum of 20 ARNs.</p> <p>You can call <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServiceDeployments.html">ListServiceDeployments</a> to get the ARNs.</p>

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
            To describe a service revision
            This example describes a service revision with the specified ARN

            >>> await client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-west-2:123456789012:service-revision/testc/sd1/4980306466373577095'])
            To describe a service revision with a monitoring configuration
            This example describes a service revision that has a monitoring configuration with 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics.

            >>> await client.describe_service_revisions(service_revision_arns=['arn:aws:ecs:us-east-1:012345678910:service-revision/default/ecs-monitored-service/8675309012345678901'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_service_revisions_response.DescribeServiceRevisionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_service_revisions.async_describe_service_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_service_revisions_request.DescribeServiceRevisionsRequest = {
            "service_revision_arns": service_revision_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
