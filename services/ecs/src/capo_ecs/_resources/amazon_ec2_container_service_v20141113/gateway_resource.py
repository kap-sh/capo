from __future__ import annotations

import uuid
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
    import capo_ecs.types.associate_gateway_with_cluster_request
    import capo_ecs.types.associate_gateway_with_cluster_response
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.create_gateway_request
    import capo_ecs.types.create_gateway_response
    import capo_ecs.types.delete_gateway_request
    import capo_ecs.types.delete_gateway_response
    import capo_ecs.types.describe_gateway_request
    import capo_ecs.types.describe_gateway_resources_request
    import capo_ecs.types.describe_gateway_resources_response
    import capo_ecs.types.describe_gateway_response
    import capo_ecs.types.disassociate_gateway_from_cluster_request
    import capo_ecs.types.disassociate_gateway_from_cluster_response
    import capo_ecs.types.gateway_cluster_association_status_list
    import capo_ecs.types.gateway_cluster_association_summary
    import capo_ecs.types.gateway_configuration
    import capo_ecs.types.gateway_status_list
    import capo_ecs.types.gateway_summary
    import capo_ecs.types.list_gateway_cluster_associations_request
    import capo_ecs.types.list_gateway_cluster_associations_response
    import capo_ecs.types.list_gateways_request
    import capo_ecs.types.list_gateways_response
    import capo_ecs.types.propagate_gateway_tags
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags
    import capo_ecs.types.update_gateway_configuration
    import capo_ecs.types.update_gateway_request
    import capo_ecs.types.update_gateway_response
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class GatewayResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def associate_gateway_with_cluster(
        self,
        gateway: "capo_ecs.types.string.String",
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.associate_gateway_with_cluster_response.AssociateGatewayWithClusterResponse":
        """<p>Associates a gateway with an Amazon ECS cluster. After a cluster is associated with a gateway, services in that cluster can use the gateway for ingress. No changes take effect until you update a service in the cluster to use the gateway. A single cluster can be associated with up to 5 gateways.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to associate.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of the cluster to associate the gateway with.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To associate a gateway with a cluster
            This example associates the gateway named my-gateway with the cluster named my-cluster so that services in the cluster can use the gateway for ingress.

            >>> client.associate_gateway_with_cluster(gateway='my-gateway', cluster='my-cluster')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.associate_gateway_with_cluster_request.AssociateGatewayWithClusterRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.associate_gateway_with_cluster_response.AssociateGatewayWithClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.associate_gateway_with_cluster

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.associate_gateway_with_cluster.associate_gateway_with_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateGatewayWithCluster")
        )
        input_: capo_ecs.types.associate_gateway_with_cluster_request.AssociateGatewayWithClusterRequest = {
            "gateway": gateway,
            "cluster": cluster,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_gateway(
        self,
        name: "capo_ecs.types.string.String",
        infrastructure_role_arn: "capo_ecs.types.string.String",
        configuration: "capo_ecs.types.gateway_configuration.GatewayConfiguration",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        deletion_protection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
        ] = None,
    ) -> "capo_ecs.types.create_gateway_response.CreateGatewayResponse":
        """<p>Creates a gateway. A gateway defines and dynamically manages ingress paths for your Amazon ECS services, handling traffic routing and infrastructure across multiple services while optimizing infrastructure usage. <code>CreateGateway</code> is a synchronous operation and the gateway is returned with a status of <code>ACTIVE</code>. The load balancers and other infrastructure that a gateway manages aren't created until a service in an associated cluster begins using the gateway.</p> <p>To use this operation, you must have the <code>iam:PassRole</code> permission for the infrastructure role that you specify in <code>infrastructureRoleArn</code>.</p>

        Args:
            name: <p>The name for the gateway. The name must be unique within your account and can be up to 255 characters.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to create and manage infrastructure on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            deletion_protection: <p>Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted, and the gateway propagates this setting to the load balancers it manages. The default is <code>true</code>.</p>
            configuration: <p>The type-specific configuration for the gateway. Exactly one configuration variant must be set, and it determines the gateway type. For example, <code>hostSharedAlb</code> configures a gateway that uses Application Load Balancers with host-based routing.</p>
            tags: <p>The metadata that you apply to the gateway to help you categorize and organize it. Each tag consists of a key and an optional value. Depending on <code>propagateTags</code>, these tags can be applied to the infrastructure the gateway manages.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. The default is <code>GATEWAY</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a gateway
            This example creates a gateway named my-gateway that uses internet-facing Application Load Balancers with host-based routing in the specified subnets.

            >>> client.create_gateway(name='my-gateway', infrastructure_role_arn='arn:aws:iam::123456789012:role/ecsInfrastructureRole', configuration={'hostSharedAlb': {'networkConfiguration': {'subnets': ['subnet-0123456789abcdef0', 'subnet-0fedcba9876543210'], 'ipAddressType': 'ipv4'}, 'scheme': 'internet-facing', 'protocol': 'HTTPS', 'port': 443, 'maxAlbCount': 10, 'httpDesync': 'defensive'}}, tags=[{'key': 'team', 'value': 'web'}], propagate_tags='GATEWAY')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.create_gateway_request.CreateGatewayRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_gateway

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGateway")
        )
        input_: capo_ecs.types.create_gateway_request.CreateGatewayRequest = {
            "name": name,
            "infrastructure_role_arn": infrastructure_role_arn,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_gateway_response.DeleteGatewayResponse":
        """<p>Deletes a gateway. Before you can delete a gateway, deletion protection must be disabled and the gateway must not have any cluster associations that are in the <code>ACTIVE</code> or <code>DISASSOCIATING</code> state. If associations exist, the operation fails; disassociate all clusters first. <code>DeleteGateway</code> is a synchronous operation. After you delete a gateway, subsequent requests for it return a <code>GatewayNotFoundException</code>.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a gateway
            This example deletes the gateway named my-gateway. Deletion protection must be disabled and the gateway must not be associated with any clusters.

            >>> client.delete_gateway(gateway='my-gateway')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_gateway

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGateway")
        )
        input_: capo_ecs.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway": gateway
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_gateway(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_gateway_response.DescribeGatewayResponse":
        """<p>Describes a gateway, including its configuration, status, and the type-specific infrastructure settings that it uses.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a gateway
            This example describes the gateway named my-gateway.

            >>> client.describe_gateway(gateway='my-gateway')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway.describe_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGateway")
        )
        input_: capo_ecs.types.describe_gateway_request.DescribeGatewayRequest = {
            "gateway": gateway
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_gateway_resources(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.describe_gateway_resources_response.DescribeGatewayResourcesResponse":
        """<p>Returns the infrastructure that a gateway has created and manages, so that you can follow the traffic path from top-level shared resources, such as load balancers, to the service-specific resources represented as gateway routes. Responses include only the Amazon Resource Names (ARNs) of gateway-managed infrastructure. For the current state of a resource, describe it with the corresponding Amazon Web Services service (Elastic Load Balancing, Amazon EC2, or Amazon Web Services Certificate Manager). The results are paginated.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway.</p>
            max_results: <p>The maximum number of results that the operation returns in a single page. The maximum value is 20 and the default is 10.</p>
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
            To describe the infrastructure that a gateway manages
            This example returns the load balancers, listeners, and gateway routes that the gateway named my-gateway manages.

            >>> client.describe_gateway_resources(gateway='my-gateway')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_gateway_resources_request.DescribeGatewayResourcesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_gateway_resources_response.DescribeGatewayResourcesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_resources

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_resources.describe_gateway_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGatewayResources")
        )
        input_: capo_ecs.types.describe_gateway_resources_request.DescribeGatewayResourcesRequest = {
            "gateway": gateway
        }
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

    def disassociate_gateway_from_cluster(
        self,
        gateway: "capo_ecs.types.string.String",
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.disassociate_gateway_from_cluster_response.DisassociateGatewayFromClusterResponse":
        """<p>Removes the association between a gateway and an Amazon ECS cluster. The association remains in the <code>DISASSOCIATING</code> state until you remove all of the gateway routes for the cluster by updating the associated services. You can use <code>ListGatewayRoutes</code> with a cluster filter to determine which routes are preventing disassociation. No infrastructure changes are made until the affected services are updated.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to disassociate.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of the cluster to disassociate the gateway from.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disassociate a gateway from a cluster
            This example removes the association between the gateway named my-gateway and the cluster named my-cluster. The association remains in the DISASSOCIATING state until all gateway routes for the cluster are removed.

            >>> client.disassociate_gateway_from_cluster(gateway='my-gateway', cluster='my-cluster')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.disassociate_gateway_from_cluster_request.DisassociateGatewayFromClusterRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.disassociate_gateway_from_cluster_response.DisassociateGatewayFromClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.disassociate_gateway_from_cluster

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.disassociate_gateway_from_cluster.disassociate_gateway_from_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateGatewayFromCluster")
        )
        input_: capo_ecs.types.disassociate_gateway_from_cluster_request.DisassociateGatewayFromClusterRequest = {
            "gateway": gateway,
            "cluster": cluster,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_cluster_associations(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        gateway: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.gateway_cluster_association_status_list.GatewayClusterAssociationStatusList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_gateway_cluster_associations_response.ListGatewayClusterAssociationsResponse":
        """<p>Returns a list of the associations between gateways and clusters. You can filter the results by gateway, cluster, and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of a gateway to filter the results by.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of a cluster to filter the results by.</p>
            status: <p>The association status to filter the results by.</p>
            max_results: <p>The maximum number of results that the operation returns in a single page. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the clusters associated with a gateway
            This example lists the clusters that are associated with the gateway named my-gateway.

            >>> client.list_gateway_cluster_associations(gateway='my-gateway')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_gateway_cluster_associations_request.ListGatewayClusterAssociationsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_gateway_cluster_associations_response.ListGatewayClusterAssociationsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_cluster_associations

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_cluster_associations.list_gateway_cluster_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGatewayClusterAssociations")
        )
        input_: capo_ecs.types.list_gateway_cluster_associations_request.ListGatewayClusterAssociationsRequest = {}
        if gateway is not None:
            input_["gateway"] = gateway
        if cluster is not None:
            input_["cluster"] = cluster
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

    def list_gateways(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        names: Optional["capo_ecs.types.string_list.StringList"] = None,
        status: Optional["capo_ecs.types.gateway_status_list.GatewayStatusList"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_gateways_response.ListGatewaysResponse":
        """<p>Returns a list of gateways in your account. You can filter the results by gateway name and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            names: <p>The gateway names to filter the results by. You can specify up to 10 names.</p>
            status: <p>The gateway statuses to filter the results by.</p>
            max_results: <p>The maximum number of gateway results that <code>ListGateways</code> returns in a single page. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListGateways</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list active gateways
            This example lists the gateways in your account that have a status of ACTIVE.

            >>> client.list_gateways(status=['ACTIVE'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_gateways_request.ListGatewaysRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateways

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGateways")
        )
        input_: capo_ecs.types.list_gateways_request.ListGatewaysRequest = {}
        if names is not None:
            input_["names"] = names
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

    def update_gateway(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        infrastructure_role_arn: Optional["capo_ecs.types.string.String"] = None,
        deletion_protection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        configuration: Optional[
            "capo_ecs.types.update_gateway_configuration.UpdateGatewayConfiguration"
        ] = None,
        propagate_tags: Optional[
            "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
        ] = None,
    ) -> "capo_ecs.types.update_gateway_response.UpdateGatewayResponse":
        """<p>Modifies the configuration of a gateway. You can change only the properties that can be applied without interrupting traffic, and the configuration variant that you provide must match the gateway's type. <code>UpdateGateway</code> is an asynchronous operation: the changes are applied to each load balancer the gateway manages, and the gateway reports a status of <code>UPDATE_IN_PROGRESS</code> until the update completes. If Amazon ECS can't update one or more resources, it makes a best effort to update the rest and the gateway status changes to <code>UPDATE_FAILED</code>. Use <code>DescribeGateway</code> to inspect the gateway's <code>statusReason</code> and failures list, which gives the ARN of each load balancer that was not updated and the operation, error code, and message for each failure.</p> <p>If you specify <code>infrastructureRoleArn</code>, you must have the <code>iam:PassRole</code> permission for that role.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to update.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to manage infrastructure on your behalf.</p>
            deletion_protection: <p>Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted.</p>
            configuration: <p>The updated type-specific configuration for the gateway. The configuration variant must match the gateway's existing type, and only mutable fields can be changed.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. If you don't specify a value, the gateway's existing setting is unchanged.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a gateway
            This example raises the maximum number of Application Load Balancers that the gateway named my-gateway manages, and changes the desync mitigation mode to strictest.

            >>> client.update_gateway(gateway='my-gateway', configuration={'hostSharedAlb': {'maxAlbCount': 20, 'httpDesync': 'strictest'}})
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_gateway_response.UpdateGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_gateway

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_gateway.update_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGateway")
        )
        input_: capo_ecs.types.update_gateway_request.UpdateGatewayRequest = {
            "gateway": gateway
        }
        if infrastructure_role_arn is not None:
            input_["infrastructure_role_arn"] = infrastructure_role_arn
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if configuration is not None:
            input_["configuration"] = configuration
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGatewayResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def associate_gateway_with_cluster(
        self,
        gateway: "capo_ecs.types.string.String",
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.associate_gateway_with_cluster_response.AssociateGatewayWithClusterResponse":
        """<p>Associates a gateway with an Amazon ECS cluster. After a cluster is associated with a gateway, services in that cluster can use the gateway for ingress. No changes take effect until you update a service in the cluster to use the gateway. A single cluster can be associated with up to 5 gateways.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to associate.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of the cluster to associate the gateway with.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To associate a gateway with a cluster
            This example associates the gateway named my-gateway with the cluster named my-cluster so that services in the cluster can use the gateway for ingress.

            >>> await client.associate_gateway_with_cluster(gateway='my-gateway', cluster='my-cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.associate_gateway_with_cluster_request.AssociateGatewayWithClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.associate_gateway_with_cluster_response.AssociateGatewayWithClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.associate_gateway_with_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.associate_gateway_with_cluster.async_associate_gateway_with_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateGatewayWithCluster")
        )
        input_: capo_ecs.types.associate_gateway_with_cluster_request.AssociateGatewayWithClusterRequest = {
            "gateway": gateway,
            "cluster": cluster,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_gateway(
        self,
        name: "capo_ecs.types.string.String",
        infrastructure_role_arn: "capo_ecs.types.string.String",
        configuration: "capo_ecs.types.gateway_configuration.GatewayConfiguration",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        deletion_protection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
        ] = None,
    ) -> "capo_ecs.types.create_gateway_response.CreateGatewayResponse":
        """<p>Creates a gateway. A gateway defines and dynamically manages ingress paths for your Amazon ECS services, handling traffic routing and infrastructure across multiple services while optimizing infrastructure usage. <code>CreateGateway</code> is a synchronous operation and the gateway is returned with a status of <code>ACTIVE</code>. The load balancers and other infrastructure that a gateway manages aren't created until a service in an associated cluster begins using the gateway.</p> <p>To use this operation, you must have the <code>iam:PassRole</code> permission for the infrastructure role that you specify in <code>infrastructureRoleArn</code>.</p>

        Args:
            name: <p>The name for the gateway. The name must be unique within your account and can be up to 255 characters.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to create and manage infrastructure on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            deletion_protection: <p>Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted, and the gateway propagates this setting to the load balancers it manages. The default is <code>true</code>.</p>
            configuration: <p>The type-specific configuration for the gateway. Exactly one configuration variant must be set, and it determines the gateway type. For example, <code>hostSharedAlb</code> configures a gateway that uses Application Load Balancers with host-based routing.</p>
            tags: <p>The metadata that you apply to the gateway to help you categorize and organize it. Each tag consists of a key and an optional value. Depending on <code>propagateTags</code>, these tags can be applied to the infrastructure the gateway manages.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. The default is <code>GATEWAY</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a gateway
            This example creates a gateway named my-gateway that uses internet-facing Application Load Balancers with host-based routing in the specified subnets.

            >>> await client.create_gateway(name='my-gateway', infrastructure_role_arn='arn:aws:iam::123456789012:role/ecsInfrastructureRole', configuration={'hostSharedAlb': {'networkConfiguration': {'subnets': ['subnet-0123456789abcdef0', 'subnet-0fedcba9876543210'], 'ipAddressType': 'ipv4'}, 'scheme': 'internet-facing', 'protocol': 'HTTPS', 'port': 443, 'maxAlbCount': 10, 'httpDesync': 'defensive'}}, tags=[{'key': 'team', 'value': 'web'}], propagate_tags='GATEWAY')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_gateway_request.CreateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_gateway

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGateway")
        )
        input_: capo_ecs.types.create_gateway_request.CreateGatewayRequest = {
            "name": name,
            "infrastructure_role_arn": infrastructure_role_arn,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_gateway(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_gateway_response.DeleteGatewayResponse":
        """<p>Deletes a gateway. Before you can delete a gateway, deletion protection must be disabled and the gateway must not have any cluster associations that are in the <code>ACTIVE</code> or <code>DISASSOCIATING</code> state. If associations exist, the operation fails; disassociate all clusters first. <code>DeleteGateway</code> is a synchronous operation. After you delete a gateway, subsequent requests for it return a <code>GatewayNotFoundException</code>.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a gateway
            This example deletes the gateway named my-gateway. Deletion protection must be disabled and the gateway must not be associated with any clusters.

            >>> await client.delete_gateway(gateway='my-gateway')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_gateway

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGateway")
        )
        input_: capo_ecs.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway": gateway
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_gateway(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_gateway_response.DescribeGatewayResponse":
        """<p>Describes a gateway, including its configuration, status, and the type-specific infrastructure settings that it uses.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a gateway
            This example describes the gateway named my-gateway.

            >>> await client.describe_gateway(gateway='my-gateway')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway.async_describe_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGateway")
        )
        input_: capo_ecs.types.describe_gateway_request.DescribeGatewayRequest = {
            "gateway": gateway
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_gateway_resources(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.describe_gateway_resources_response.DescribeGatewayResourcesResponse":
        """<p>Returns the infrastructure that a gateway has created and manages, so that you can follow the traffic path from top-level shared resources, such as load balancers, to the service-specific resources represented as gateway routes. Responses include only the Amazon Resource Names (ARNs) of gateway-managed infrastructure. For the current state of a resource, describe it with the corresponding Amazon Web Services service (Elastic Load Balancing, Amazon EC2, or Amazon Web Services Certificate Manager). The results are paginated.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway.</p>
            max_results: <p>The maximum number of results that the operation returns in a single page. The maximum value is 20 and the default is 10.</p>
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
            To describe the infrastructure that a gateway manages
            This example returns the load balancers, listeners, and gateway routes that the gateway named my-gateway manages.

            >>> await client.describe_gateway_resources(gateway='my-gateway')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_gateway_resources_request.DescribeGatewayResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_gateway_resources_response.DescribeGatewayResourcesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_resources

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_gateway_resources.async_describe_gateway_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGatewayResources")
        )
        input_: capo_ecs.types.describe_gateway_resources_request.DescribeGatewayResourcesRequest = {
            "gateway": gateway
        }
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

    async def disassociate_gateway_from_cluster(
        self,
        gateway: "capo_ecs.types.string.String",
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.disassociate_gateway_from_cluster_response.DisassociateGatewayFromClusterResponse":
        """<p>Removes the association between a gateway and an Amazon ECS cluster. The association remains in the <code>DISASSOCIATING</code> state until you remove all of the gateway routes for the cluster by updating the associated services. You can use <code>ListGatewayRoutes</code> with a cluster filter to determine which routes are preventing disassociation. No infrastructure changes are made until the affected services are updated.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to disassociate.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of the cluster to disassociate the gateway from.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disassociate a gateway from a cluster
            This example removes the association between the gateway named my-gateway and the cluster named my-cluster. The association remains in the DISASSOCIATING state until all gateway routes for the cluster are removed.

            >>> await client.disassociate_gateway_from_cluster(gateway='my-gateway', cluster='my-cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.disassociate_gateway_from_cluster_request.DisassociateGatewayFromClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.disassociate_gateway_from_cluster_response.DisassociateGatewayFromClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.disassociate_gateway_from_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.disassociate_gateway_from_cluster.async_disassociate_gateway_from_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateGatewayFromCluster")
        )
        input_: capo_ecs.types.disassociate_gateway_from_cluster_request.DisassociateGatewayFromClusterRequest = {
            "gateway": gateway,
            "cluster": cluster,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_gateway_cluster_associations(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        gateway: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.gateway_cluster_association_status_list.GatewayClusterAssociationStatusList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_gateway_cluster_associations_response.ListGatewayClusterAssociationsResponse":
        """<p>Returns a list of the associations between gateways and clusters. You can filter the results by gateway, cluster, and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of a gateway to filter the results by.</p>
            cluster: <p>The name or Amazon Resource Name (ARN) of a cluster to filter the results by.</p>
            status: <p>The association status to filter the results by.</p>
            max_results: <p>The maximum number of results that the operation returns in a single page. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the clusters associated with a gateway
            This example lists the clusters that are associated with the gateway named my-gateway.

            >>> await client.list_gateway_cluster_associations(gateway='my-gateway')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_gateway_cluster_associations_request.ListGatewayClusterAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_gateway_cluster_associations_response.ListGatewayClusterAssociationsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_cluster_associations

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateway_cluster_associations.async_list_gateway_cluster_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGatewayClusterAssociations")
        )
        input_: capo_ecs.types.list_gateway_cluster_associations_request.ListGatewayClusterAssociationsRequest = {}
        if gateway is not None:
            input_["gateway"] = gateway
        if cluster is not None:
            input_["cluster"] = cluster
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

    async def list_gateways(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        names: Optional["capo_ecs.types.string_list.StringList"] = None,
        status: Optional["capo_ecs.types.gateway_status_list.GatewayStatusList"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_gateways_response.ListGatewaysResponse":
        """<p>Returns a list of gateways in your account. You can filter the results by gateway name and status. The results are paginated. We recommend that you use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            names: <p>The gateway names to filter the results by. You can specify up to 10 names.</p>
            status: <p>The gateway statuses to filter the results by.</p>
            max_results: <p>The maximum number of gateway results that <code>ListGateways</code> returns in a single page. The default is 100.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListGateways</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list active gateways
            This example lists the gateways in your account that have a status of ACTIVE.

            >>> await client.list_gateways(status=['ACTIVE'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_gateways_request.ListGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateways

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGateways")
        )
        input_: capo_ecs.types.list_gateways_request.ListGatewaysRequest = {}
        if names is not None:
            input_["names"] = names
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

    async def update_gateway(
        self,
        gateway: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        infrastructure_role_arn: Optional["capo_ecs.types.string.String"] = None,
        deletion_protection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        configuration: Optional[
            "capo_ecs.types.update_gateway_configuration.UpdateGatewayConfiguration"
        ] = None,
        propagate_tags: Optional[
            "capo_ecs.types.propagate_gateway_tags.PropagateGatewayTags"
        ] = None,
    ) -> "capo_ecs.types.update_gateway_response.UpdateGatewayResponse":
        """<p>Modifies the configuration of a gateway. You can change only the properties that can be applied without interrupting traffic, and the configuration variant that you provide must match the gateway's type. <code>UpdateGateway</code> is an asynchronous operation: the changes are applied to each load balancer the gateway manages, and the gateway reports a status of <code>UPDATE_IN_PROGRESS</code> until the update completes. If Amazon ECS can't update one or more resources, it makes a best effort to update the rest and the gateway status changes to <code>UPDATE_FAILED</code>. Use <code>DescribeGateway</code> to inspect the gateway's <code>statusReason</code> and failures list, which gives the ARN of each load balancer that was not updated and the operation, error code, and message for each failure.</p> <p>If you specify <code>infrastructureRoleArn</code>, you must have the <code>iam:PassRole</code> permission for that role.</p>

        Args:
            gateway: <p>The name or Amazon Resource Name (ARN) of the gateway to update.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the gateway assumes to manage infrastructure on your behalf.</p>
            deletion_protection: <p>Specifies whether to enable deletion protection for the gateway. When enabled, the gateway can't be deleted.</p>
            configuration: <p>The updated type-specific configuration for the gateway. The configuration variant must match the gateway's existing type, and only mutable fields can be changed.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the gateway to the infrastructure that the gateway manages. If you don't specify a value, the gateway's existing setting is unchanged.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.gateway_not_found_exception.GatewayNotFoundException: <p>The specified gateway wasn't found. Check that the gateway name or ARN is correct and that the gateway exists in your account and Region.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a gateway
            This example raises the maximum number of Application Load Balancers that the gateway named my-gateway manages, and changes the desync mitigation mode to strictest.

            >>> await client.update_gateway(gateway='my-gateway', configuration={'hostSharedAlb': {'maxAlbCount': 20, 'httpDesync': 'strictest'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_gateway_response.UpdateGatewayResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_gateway

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_gateway.async_update_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGateway")
        )
        input_: capo_ecs.types.update_gateway_request.UpdateGatewayRequest = {
            "gateway": gateway
        }
        if infrastructure_role_arn is not None:
            input_["infrastructure_role_arn"] = infrastructure_role_arn
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if configuration is not None:
            input_["configuration"] = configuration
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
