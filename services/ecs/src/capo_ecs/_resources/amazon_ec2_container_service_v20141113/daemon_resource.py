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
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.create_daemon_request
    import capo_ecs.types.create_daemon_response
    import capo_ecs.types.created_at
    import capo_ecs.types.daemon_deployment_configuration
    import capo_ecs.types.daemon_deployment_status_list
    import capo_ecs.types.daemon_propagate_tags
    import capo_ecs.types.delete_daemon_request
    import capo_ecs.types.delete_daemon_response
    import capo_ecs.types.describe_daemon_request
    import capo_ecs.types.describe_daemon_response
    import capo_ecs.types.list_daemon_deployments_request
    import capo_ecs.types.list_daemon_deployments_response
    import capo_ecs.types.list_daemons_request
    import capo_ecs.types.list_daemons_response
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags
    import capo_ecs.types.update_daemon_request
    import capo_ecs.types.update_daemon_response
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class DaemonResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def create_daemon(
        self,
        daemon_name: "capo_ecs.types.string.String",
        daemon_task_definition_arn: "capo_ecs.types.string.String",
        capacity_provider_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster_arn: Optional["capo_ecs.types.string.String"] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
        ] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        critical: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.create_daemon_response.CreateDaemonResponse":
        """<p>Creates a new daemon in the specified cluster and capacity providers. A daemon deploys cross-cutting software agents such as security monitoring, telemetry, and logging independently across your Amazon ECS infrastructure.</p> <p>Amazon ECS deploys exactly one daemon task on each container instance of the specified capacity providers. When a container instance registers with the cluster, Amazon ECS automatically starts daemon tasks. Amazon ECS starts a daemon task before scheduling other tasks.</p> <p>Daemons are essential for instance health - if a daemon task stops, Amazon ECS automatically drains and replaces that container instance.</p> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_name: <p>The name of the daemon. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to create the daemon in.</p>
            daemon_task_definition_arn: <p>The Amazon Resource Name (ARN) of the daemon task definition to use for the daemon.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon. The daemon deploys tasks on container instances managed by these capacity providers.</p>
            deployment_configuration: <p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>
            tags: <p>The metadata that you apply to the daemon to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            propagate_tags: <p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Determines whether the execute command functionality is turned on for the daemon. If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            critical: <p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a daemon
            This example creates a daemon named my-monitoring-daemon in the specified cluster that uses the monitoring-agent daemon task definition and deploys to the specified capacity provider.

            >>> client.create_daemon(daemon_name='my-monitoring-daemon', cluster_arn='arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster', daemon_task_definition_arn='arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1', capacity_provider_arns=['arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider'], deployment_configuration={'drainPercent': 10.0, 'bakeTimeInMinutes': 5})
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.create_daemon_request.CreateDaemonRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.create_daemon_response.CreateDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_daemon

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.create_daemon.create_daemon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_daemon_request.CreateDaemonRequest = {
            "daemon_name": daemon_name,
            "daemon_task_definition_arn": daemon_task_definition_arn,
            "capacity_provider_arns": capacity_provider_arns,
        }
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if client_token is not None:
            input_["client_token"] = client_token
        if critical is not None:
            input_["critical"] = critical

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_daemon_response.DeleteDaemonResponse":
        """<p>Deletes the specified daemon. The daemon must be in an <code>ACTIVE</code> state to be deleted. Deleting a daemon stops all running daemon tasks on the associated container instances. Amazon ECS drains existing container instances and provisions new instances without the deleted daemon. Amazon ECS automatically launches replacement tasks for your Amazon ECS services.</p> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_active_exception.DaemonNotActiveException: <p>The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html">CreateDaemon</a>.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a daemon
            This example deletes the my-monitoring-daemon daemon.

            >>> client.delete_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_daemon_request.DeleteDaemonRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_daemon_response.DeleteDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon.delete_daemon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_daemon_request.DeleteDaemonRequest = {
            "daemon_arn": daemon_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_response.DescribeDaemonResponse":
        """<p>Describes the specified daemon.</p>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a daemon
            This example describes the my-monitoring-daemon daemon.

            >>> client.describe_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_daemon_request.DescribeDaemonRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_daemon_response.DescribeDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon.describe_daemon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_request.DescribeDaemonRequest = {
            "daemon_arn": daemon_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_daemon_deployments(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        status: Optional[
            "capo_ecs.types.daemon_deployment_status_list.DaemonDeploymentStatusList"
        ] = None,
        created_at: Optional["capo_ecs.types.created_at.CreatedAt"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> (
        "capo_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse"
    ):
        """<p>Returns a list of daemon deployments for a specified daemon. You can filter the results by status or creation time.</p>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to list deployments for.</p>
            status: <p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by deployment status. If you don't specify a status, all deployments are returned.</p>
            created_at: <p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by creation time. If you don't specify a time range, all deployments are returned.</p>
            max_results: <p>The maximum number of daemon deployment results that <code>ListDaemonDeployments</code> returned in paginated output. When this parameter is used, <code>ListDaemonDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemonDeployments</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemon deployments
            This example lists all successful daemon deployments for the my-monitoring-daemon daemon.

            >>> client.list_daemon_deployments(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon', status=['SUCCESSFUL'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_deployments

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_deployments.list_daemon_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest = {
            "daemon_arn": daemon_arn
        }
        if status is not None:
            input_["status"] = status
        if created_at is not None:
            input_["created_at"] = created_at
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

    def list_daemons(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster_arn: Optional["capo_ecs.types.string.String"] = None,
        capacity_provider_arns: Optional[
            "capo_ecs.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_daemons_response.ListDaemonsResponse":
        """<p>Returns a list of daemons. You can filter the results by cluster or capacity provider.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to filter daemons by. If you do not specify a cluster, the default cluster is assumed.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to filter daemons by. Only daemons associated with the specified capacity providers are returned.</p>
            max_results: <p>The maximum number of daemon results that <code>ListDaemons</code> returned in paginated output. When this parameter is used, <code>ListDaemons</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemons</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemons</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemons</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemons in a cluster
            This example lists all daemons in the specified cluster.

            >>> client.list_daemons(cluster_arn='arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_daemons_request.ListDaemonsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_daemons_response.ListDaemonsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemons

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemons.list_daemons(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemons_request.ListDaemonsRequest = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if capacity_provider_arns is not None:
            input_["capacity_provider_arns"] = capacity_provider_arns
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

    def update_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        daemon_task_definition_arn: "capo_ecs.types.string.String",
        capacity_provider_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
        ] = None,
        propagate_tags: Optional[
            "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
        ] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        critical: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.update_daemon_response.UpdateDaemonResponse":
        """<p>Updates the specified daemon. When you update a daemon, a new deployment is triggered that progressively rolls out the changes to the container instances associated with the daemon's capacity providers. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-deployments.html">Daemon deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Amazon ECS drains existing container instances and provisions new instances with the updated daemon. Amazon ECS automatically launches replacement tasks for your services.</p> <important> <p>Updating a daemon triggers a rolling deployment that drains and replaces container instances. Plan updates during maintenance windows to minimize impact on running services.</p> </important> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to update.</p>
            daemon_task_definition_arn: <p>The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.</p>
            deployment_configuration: <p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.</p>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon. If <code>false</code>, the execute command functionality is turned off.</p>
            critical: <p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_active_exception.DaemonNotActiveException: <p>The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html">CreateDaemon</a>.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a daemon
            This example updates the my-monitoring-daemon daemon to use a new daemon task definition revision.

            >>> client.update_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon', daemon_task_definition_arn='arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:2', capacity_provider_arns=['arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider'], deployment_configuration={'drainPercent': 10.0, 'bakeTimeInMinutes': 5})
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_daemon_request.UpdateDaemonRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_daemon_response.UpdateDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_daemon

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_daemon.update_daemon(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_daemon_request.UpdateDaemonRequest = {
            "daemon_arn": daemon_arn,
            "daemon_task_definition_arn": daemon_task_definition_arn,
            "capacity_provider_arns": capacity_provider_arns,
        }
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if critical is not None:
            input_["critical"] = critical

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDaemonResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def create_daemon(
        self,
        daemon_name: "capo_ecs.types.string.String",
        daemon_task_definition_arn: "capo_ecs.types.string.String",
        capacity_provider_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster_arn: Optional["capo_ecs.types.string.String"] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        propagate_tags: Optional[
            "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
        ] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        critical: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.create_daemon_response.CreateDaemonResponse":
        """<p>Creates a new daemon in the specified cluster and capacity providers. A daemon deploys cross-cutting software agents such as security monitoring, telemetry, and logging independently across your Amazon ECS infrastructure.</p> <p>Amazon ECS deploys exactly one daemon task on each container instance of the specified capacity providers. When a container instance registers with the cluster, Amazon ECS automatically starts daemon tasks. Amazon ECS starts a daemon task before scheduling other tasks.</p> <p>Daemons are essential for instance health - if a daemon task stops, Amazon ECS automatically drains and replaces that container instance.</p> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_name: <p>The name of the daemon. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to create the daemon in.</p>
            daemon_task_definition_arn: <p>The Amazon Resource Name (ARN) of the daemon task definition to use for the daemon.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon. The daemon deploys tasks on container instances managed by these capacity providers.</p>
            deployment_configuration: <p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>
            tags: <p>The metadata that you apply to the daemon to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            propagate_tags: <p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Determines whether the execute command functionality is turned on for the daemon. If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            critical: <p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a daemon
            This example creates a daemon named my-monitoring-daemon in the specified cluster that uses the monitoring-agent daemon task definition and deploys to the specified capacity provider.

            >>> await client.create_daemon(daemon_name='my-monitoring-daemon', cluster_arn='arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster', daemon_task_definition_arn='arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:1', capacity_provider_arns=['arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider'], deployment_configuration={'drainPercent': 10.0, 'bakeTimeInMinutes': 5})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_daemon_request.CreateDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_daemon_response.CreateDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_daemon.async_create_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_daemon_request.CreateDaemonRequest = {
            "daemon_name": daemon_name,
            "daemon_task_definition_arn": daemon_task_definition_arn,
            "capacity_provider_arns": capacity_provider_arns,
        }
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if tags is not None:
            input_["tags"] = tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if client_token is not None:
            input_["client_token"] = client_token
        if critical is not None:
            input_["critical"] = critical

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_daemon_response.DeleteDaemonResponse":
        """<p>Deletes the specified daemon. The daemon must be in an <code>ACTIVE</code> state to be deleted. Deleting a daemon stops all running daemon tasks on the associated container instances. Amazon ECS drains existing container instances and provisions new instances without the deleted daemon. Amazon ECS automatically launches replacement tasks for your Amazon ECS services.</p> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_active_exception.DaemonNotActiveException: <p>The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html">CreateDaemon</a>.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a daemon
            This example deletes the my-monitoring-daemon daemon.

            >>> await client.delete_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_daemon_request.DeleteDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_daemon_response.DeleteDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon.async_delete_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_daemon_request.DeleteDaemonRequest = {
            "daemon_arn": daemon_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_response.DescribeDaemonResponse":
        """<p>Describes the specified daemon.</p>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a daemon
            This example describes the my-monitoring-daemon daemon.

            >>> await client.describe_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_daemon_request.DescribeDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_daemon_response.DescribeDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon.async_describe_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_request.DescribeDaemonRequest = {
            "daemon_arn": daemon_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_daemon_deployments(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        status: Optional[
            "capo_ecs.types.daemon_deployment_status_list.DaemonDeploymentStatusList"
        ] = None,
        created_at: Optional["capo_ecs.types.created_at.CreatedAt"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> (
        "capo_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse"
    ):
        """<p>Returns a list of daemon deployments for a specified daemon. You can filter the results by status or creation time.</p>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to list deployments for.</p>
            status: <p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by deployment status. If you don't specify a status, all deployments are returned.</p>
            created_at: <p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by creation time. If you don't specify a time range, all deployments are returned.</p>
            max_results: <p>The maximum number of daemon deployment results that <code>ListDaemonDeployments</code> returned in paginated output. When this parameter is used, <code>ListDaemonDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemonDeployments</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemon deployments
            This example lists all successful daemon deployments for the my-monitoring-daemon daemon.

            >>> await client.list_daemon_deployments(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon', status=['SUCCESSFUL'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_daemon_deployments_response.ListDaemonDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_deployments.async_list_daemon_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemon_deployments_request.ListDaemonDeploymentsRequest = {
            "daemon_arn": daemon_arn
        }
        if status is not None:
            input_["status"] = status
        if created_at is not None:
            input_["created_at"] = created_at
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

    async def list_daemons(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster_arn: Optional["capo_ecs.types.string.String"] = None,
        capacity_provider_arns: Optional[
            "capo_ecs.types.string_list.StringList"
        ] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.list_daemons_response.ListDaemonsResponse":
        """<p>Returns a list of daemons. You can filter the results by cluster or capacity provider.</p>

        Args:
            cluster_arn: <p>The Amazon Resource Name (ARN) of the cluster to filter daemons by. If you do not specify a cluster, the default cluster is assumed.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to filter daemons by. Only daemons associated with the specified capacity providers are returned.</p>
            max_results: <p>The maximum number of daemon results that <code>ListDaemons</code> returned in paginated output. When this parameter is used, <code>ListDaemons</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemons</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemons</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemons</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemons in a cluster
            This example lists all daemons in the specified cluster.

            >>> await client.list_daemons(cluster_arn='arn:aws:ecs:us-east-1:123456789012:cluster/my-cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_daemons_request.ListDaemonsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_daemons_response.ListDaemonsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemons

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemons.async_list_daemons(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemons_request.ListDaemonsRequest = {}
        if cluster_arn is not None:
            input_["cluster_arn"] = cluster_arn
        if capacity_provider_arns is not None:
            input_["capacity_provider_arns"] = capacity_provider_arns
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

    async def update_daemon(
        self,
        daemon_arn: "capo_ecs.types.string.String",
        daemon_task_definition_arn: "capo_ecs.types.string.String",
        capacity_provider_arns: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.daemon_deployment_configuration.DaemonDeploymentConfiguration"
        ] = None,
        propagate_tags: Optional[
            "capo_ecs.types.daemon_propagate_tags.DaemonPropagateTags"
        ] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        critical: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.update_daemon_response.UpdateDaemonResponse":
        """<p>Updates the specified daemon. When you update a daemon, a new deployment is triggered that progressively rolls out the changes to the container instances associated with the daemon's capacity providers. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-deployments.html">Daemon deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Amazon ECS drains existing container instances and provisions new instances with the updated daemon. Amazon ECS automatically launches replacement tasks for your services.</p> <important> <p>Updating a daemon triggers a rolling deployment that drains and replaces container instances. Plan updates during maintenance windows to minimize impact on running services.</p> </important> <note> <p>ECS Managed Daemons is only supported for Amazon ECS Managed Instances Capacity Providers.</p> </note>

        Args:
            daemon_arn: <p>The Amazon Resource Name (ARN) of the daemon to update.</p>
            daemon_task_definition_arn: <p>The Amazon Resource Name (ARN) of the daemon task definition to use for the updated daemon.</p>
            capacity_provider_arns: <p>The Amazon Resource Names (ARNs) of the capacity providers to associate with the daemon.</p>
            deployment_configuration: <p>Optional deployment parameters that control how the daemon rolls out updates, including the drain percentage, alarm-based rollback, and bake time.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the daemon to the daemon tasks. If you don't specify a value, the tags aren't propagated. You can only propagate tags to daemon tasks during task creation.</p>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks in the daemon. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>If <code>true</code>, the execute command functionality is turned on for all tasks in the daemon. If <code>false</code>, the execute command functionality is turned off.</p>
            critical: <p>If the <code>critical</code> parameter of a daemon is <code>true</code>, and the daemon task fails, stops, or becomes unhealthy, Amazon ECS drains the container instance and stops the other tasks running on it. If the <code>critical</code> parameter is <code>false</code>, the daemon task failure doesn't affect the other tasks on the instance. The default value is <code>true</code>.</p> <p>A non-critical daemon doesn't block instance registration. The container instance becomes active and continues to run your other tasks, whether the daemon task fails during scale-out or during a deployment.</p> <p>Amazon ECS emits an EventBridge event when a daemon task fails to start, for both critical and non-critical daemons.</p> <p>Daemon task launch failures during a deployment are still counted by the deployment circuit breaker. The circuit breaker can roll back an unstable target revision.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.daemon_not_active_exception.DaemonNotActiveException: <p>The specified daemon isn't active. You can't update a daemon that's inactive. If you have previously deleted a daemon, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateDaemon.html">CreateDaemon</a>.</p>
            capo_ecs.errors.daemon_not_found_exception.DaemonNotFoundException: <p>The specified daemon wasn't found. You can view your available daemons with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListDaemons.html">ListDaemons</a>. Amazon ECS daemons are cluster specific and Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a daemon
            This example updates the my-monitoring-daemon daemon to use a new daemon task definition revision.

            >>> await client.update_daemon(daemon_arn='arn:aws:ecs:us-east-1:123456789012:daemon/my-cluster/my-monitoring-daemon', daemon_task_definition_arn='arn:aws:ecs:us-east-1:123456789012:daemon-task-definition/monitoring-agent:2', capacity_provider_arns=['arn:aws:ecs:us-east-1:123456789012:capacity-provider/my-capacity-provider'], deployment_configuration={'drainPercent': 10.0, 'bakeTimeInMinutes': 5})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_daemon_request.UpdateDaemonRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_daemon_response.UpdateDaemonResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_daemon

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_daemon.async_update_daemon(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_daemon_request.UpdateDaemonRequest = {
            "daemon_arn": daemon_arn,
            "daemon_task_definition_arn": daemon_task_definition_arn,
            "capacity_provider_arns": capacity_provider_arns,
        }
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if critical is not None:
            input_["critical"] = critical

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
