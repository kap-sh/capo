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
    import capo_ecs.types.attachment_state_changes
    import capo_ecs.types.attribute
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.cluster_configuration
    import capo_ecs.types.cluster_field_list
    import capo_ecs.types.cluster_service_connect_defaults_request
    import capo_ecs.types.cluster_settings
    import capo_ecs.types.container_instance_status
    import capo_ecs.types.container_state_changes
    import capo_ecs.types.create_cluster_request
    import capo_ecs.types.create_cluster_response
    import capo_ecs.types.delete_cluster_request
    import capo_ecs.types.delete_cluster_response
    import capo_ecs.types.deregister_container_instance_request
    import capo_ecs.types.deregister_container_instance_response
    import capo_ecs.types.describe_clusters_request
    import capo_ecs.types.describe_clusters_response
    import capo_ecs.types.execute_command_request
    import capo_ecs.types.execute_command_response
    import capo_ecs.types.list_attributes_request
    import capo_ecs.types.list_attributes_response
    import capo_ecs.types.list_clusters_request
    import capo_ecs.types.list_clusters_response
    import capo_ecs.types.list_container_instances_request
    import capo_ecs.types.list_container_instances_response
    import capo_ecs.types.managed_agent_state_changes
    import capo_ecs.types.network_bindings
    import capo_ecs.types.put_cluster_capacity_providers_request
    import capo_ecs.types.put_cluster_capacity_providers_response
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.submit_attachment_state_changes_request
    import capo_ecs.types.submit_attachment_state_changes_response
    import capo_ecs.types.submit_container_state_change_request
    import capo_ecs.types.submit_container_state_change_response
    import capo_ecs.types.submit_task_state_change_request
    import capo_ecs.types.submit_task_state_change_response
    import capo_ecs.types.tags
    import capo_ecs.types.target_type
    import capo_ecs.types.timestamp
    import capo_ecs.types.update_cluster_request
    import capo_ecs.types.update_cluster_response
    import capo_ecs.types.update_cluster_settings_request
    import capo_ecs.types.update_cluster_settings_response
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class ClusterResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def update(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        settings: Optional["capo_ecs.types.cluster_settings.ClusterSettings"] = None,
        configuration: Optional[
            "capo_ecs.types.cluster_configuration.ClusterConfiguration"
        ] = None,
        service_connect_defaults: Optional[
            "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
        ] = None,
    ) -> "capo_ecs.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates the cluster.</p>

        Args:
            cluster: <p>The name of the cluster to modify the settings for.</p>
            settings: <p>The cluster settings for your cluster.</p>
            configuration: <p>The execute command configuration for the cluster.</p>
            service_connect_defaults: <p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster's observability settings.
            This example turns on enhanced containerInsights in an existing cluster.

            >>> client.update(cluster='ECS-project-update-cluster', settings=[{'name': 'containerInsights', 'value': 'enhanced'}])
            To update a cluster's Service Connect defaults.
            This example sets a default Service Connect namespace.

            >>> client.update(cluster='ECS-project-update-cluster', service_connect_defaults={'namespace': 'test'})
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_cluster_request.UpdateClusterRequest = {
            "cluster": cluster
        }
        if settings is not None:
            input_["settings"] = settings
        if configuration is not None:
            input_["configuration"] = configuration
        if service_connect_defaults is not None:
            input_["service_connect_defaults"] = service_connect_defaults

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes the specified cluster. The cluster transitions to the <code>INACTIVE</code> state. Clusters with an <code>INACTIVE</code> status might remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> clusters persisting.</p> <p>You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html">ListContainerInstances</a> and deregister them with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html">DeregisterContainerInstance</a>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_contains_capacity_provider_exception.ClusterContainsCapacityProviderException: <p>The cluster contains one or more capacity providers that prevent the requested operation. This exception occurs when you try to delete a cluster that still has active capacity providers, including Amazon ECS Managed Instances capacity providers. You must first delete all capacity providers from the cluster before you can delete the cluster itself.</p>
            capo_ecs.errors.cluster_contains_container_instances_exception.ClusterContainsContainerInstancesException: <p>You can't delete a cluster that has registered container instances. First, deregister the container instances before you can delete the cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html">DeregisterContainerInstance</a>.</p>
            capo_ecs.errors.cluster_contains_services_exception.ClusterContainsServicesException: <p>You can't delete a cluster that contains services. First, update the service to reduce its desired task count to 0, and then delete the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html">DeleteService</a>.</p>
            capo_ecs.errors.cluster_contains_tasks_exception.ClusterContainsTasksException: <p>You can't delete a cluster that has active tasks.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an empty cluster
            This example deletes an empty cluster in your default region.

            >>> client.delete(cluster='my_cluster')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_cluster

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster": cluster
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_cluster_capacity_providers(
        self,
        cluster: "capo_ecs.types.string.String",
        capacity_providers: "capo_ecs.types.string_list.StringList",
        default_capacity_provider_strategy: "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse":
        """<p>Modifies the available capacity providers and the default capacity provider strategy for a cluster.</p> <p>You must specify both the available capacity providers and a default capacity provider strategy for the cluster. If the specified cluster has existing capacity providers associated with it, you must specify all existing capacity providers in addition to any new ones you want to add. Any existing capacity providers that are associated with a cluster that are omitted from a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API call will be disassociated with the cluster. You can only disassociate an existing capacity provider from a cluster if it's not being used by any existing tasks.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified, then the cluster's default capacity provider strategy is used. We recommend that you define a default capacity provider strategy for your cluster. However, you must specify an empty array (<code>[]</code>) to bypass defining a default strategy.</p> <p>Amazon ECS Managed Instances doesn't support this, because when you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to modify the capacity provider settings for. If you don't specify a cluster, the default cluster is assumed.</p>
            capacity_providers: <p>The name of one or more capacity providers to associate with the cluster.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>
            default_capacity_provider_strategy: <p>The capacity provider strategy to use by default for the cluster.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified then the default capacity provider strategy for the cluster is used.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in-use and can't be removed.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add an existing capacity provider to a cluuster
            This example adds an existing capacity provider "MyCapacityProvider2" to a cluster that already has the capacity provider "MyCapacityProvider1" associated with it. Both "MyCapacityProvider2" and "MyCapacityProvider1" need to be specified.

            >>> client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=['MyCapacityProvider1', 'MyCapacityProvider2'], default_capacity_provider_strategy=[{'capacityProvider': 'MyCapacityProvider1', 'weight': 1}, {'capacityProvider': 'MyCapacityProvider2', 'weight': 1}])
            To remove a capacity provider from a cluster
            This example removes a capacity provider "MyCapacityProvider2" from a cluster that has both "MyCapacityProvider2" and "MyCapacityProvider1" associated with it. Only "MyCapacityProvider1" needs to be specified in this scenario.

            >>> client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=['MyCapacityProvider1'], default_capacity_provider_strategy=[{'capacityProvider': 'MyCapacityProvider1', 'weight': 1, 'base': 0}])
            To remove all capacity providers from a cluster
            This example removes all capacity providers associated with a cluster.

            >>> client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=[], default_capacity_provider_strategy=[])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_cluster_capacity_providers

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.put_cluster_capacity_providers.put_cluster_capacity_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest = {
            "cluster": cluster,
            "capacity_providers": capacity_providers,
            "default_capacity_provider_strategy": default_capacity_provider_strategy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster_settings(
        self,
        cluster: "capo_ecs.types.string.String",
        settings: "capo_ecs.types.cluster_settings.ClusterSettings",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> (
        "capo_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse"
    ):
        """<p>Modifies the settings to use for a cluster.</p>

        Args:
            cluster: <p>The name of the cluster to modify the settings for.</p>
            settings: <p>The setting to use by default for a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p> <important> <p>Currently, if you delete an existing cluster that does not have Container Insights turned on, and then create a new cluster with the same name with Container Insights tuned on, Container Insights will not actually be turned on. If you want to preserve the same name for your existing cluster and turn on Container Insights, you must wait 7 days before you can re-create it.</p> </important>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster's settings
            This example enables CloudWatch Container Insights for the default cluster.

            >>> client.update_cluster_settings(cluster='default', settings=[{'name': 'containerInsights', 'value': 'enabled'}])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster_settings

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster_settings.update_cluster_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest = {
            "cluster": cluster,
            "settings": settings,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cluster(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster_name: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        settings: Optional["capo_ecs.types.cluster_settings.ClusterSettings"] = None,
        configuration: Optional[
            "capo_ecs.types.cluster_configuration.ClusterConfiguration"
        ] = None,
        capacity_providers: Optional["capo_ecs.types.string_list.StringList"] = None,
        default_capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        service_connect_defaults: Optional[
            "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
        ] = None,
    ) -> "capo_ecs.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a new Amazon ECS cluster. By default, your account receives a <code>default</code> cluster when you launch your first container instance. However, you can create your own cluster with a unique name.</p> <note> <p>When you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html">CreateCluster</a> API operation, Amazon ECS attempts to create the Amazon ECS service-linked role for your account. This is so that it can manage required resources in other Amazon Web Services services on your behalf. However, if the user that makes the call doesn't have permissions to create the service-linked role, it isn't created. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>

        Args:
            cluster_name: <p>The name of your cluster. If you don't specify a name for your cluster, you create a cluster that's named <code>default</code>. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. </p>
            tags: <p>The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            settings: <p>The setting to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p>
            configuration: <p>The <code>execute</code> command configuration for the cluster.</p>
            capacity_providers: <p>The short name of one or more capacity providers to associate with the cluster. A capacity provider must be associated with a cluster before it can be included as part of the default capacity provider strategy of the cluster or used in a capacity provider strategy when calling the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> actions.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must be created but not associated with another cluster. New Auto Scaling group capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutCapacityProvider.html">PutCapacityProvider</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>
            default_capacity_provider_strategy: <p>The capacity provider strategy to set as the default for the cluster. After a default capacity provider strategy is set for a cluster, when you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> APIs with no capacity provider strategy or launch type specified, the default capacity provider strategy for the cluster is used.</p> <p>If a default capacity provider strategy isn't defined for a cluster when it was created, it can be defined later with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API operation.</p>
            service_connect_defaults: <p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new cluster
            This example creates a cluster in your default region.

            >>> client.create_cluster(cluster_name='my_cluster')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_cluster

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_cluster_request.CreateClusterRequest = {}
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if tags is not None:
            input_["tags"] = tags
        if settings is not None:
            input_["settings"] = settings
        if configuration is not None:
            input_["configuration"] = configuration
        if capacity_providers is not None:
            input_["capacity_providers"] = capacity_providers
        if default_capacity_provider_strategy is not None:
            input_["default_capacity_provider_strategy"] = (
                default_capacity_provider_strategy
            )
        if service_connect_defaults is not None:
            input_["service_connect_defaults"] = service_connect_defaults

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_container_instance(
        self,
        container_instance: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.deregister_container_instance_response.DeregisterContainerInstanceResponse":
        """<p>Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.</p> <p>If you intend to use the container instance for some other purpose after deregistration, we recommend that you stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.</p> <p>Deregistering a container instance removes the instance from a cluster, but it doesn't terminate the EC2 instance. If you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.</p> <note> <p>If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents aren't automatically deregistered when terminated).</p> </note>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN of the container instance to deregister. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>
            force: <p>Forces the container instance to be deregistered. If you have tasks running on the container instance when you deregister it with the <code>force</code> option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they're orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible. </p> <p>Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a container instance from a cluster
            This example deregisters a container instance from the specified cluster in your default region. If there are still tasks running on the container instance, you must either stop those tasks before deregistering, or use the force option.

            >>> client.deregister_container_instance(cluster='default', force=True, container_instance='container_instance_UUID')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.deregister_container_instance_request.DeregisterContainerInstanceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.deregister_container_instance_response.DeregisterContainerInstanceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_container_instance

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_container_instance.deregister_container_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.deregister_container_instance_request.DeregisterContainerInstanceRequest = {
            "container_instance": container_instance
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_clusters(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        clusters: Optional["capo_ecs.types.string_list.StringList"] = None,
        include: Optional["capo_ecs.types.cluster_field_list.ClusterFieldList"] = None,
    ) -> "capo_ecs.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Describes one or more of your clusters.</p> <p> For CLI examples, see <a href="https://github.com/aws/aws-cli/blob/develop/awscli/examples/ecs/describe-clusters.rst">describe-clusters.rst</a> on GitHub.</p>

        Args:
            clusters: <p>A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.</p>
            include: <p>Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isn't included.</p> <p>If <code>ATTACHMENTS</code> is specified, the attachments for the container instances or tasks within the cluster are included, for example the capacity providers.</p> <p>If <code>SETTINGS</code> is specified, the settings for the cluster are included.</p> <p>If <code>CONFIGURATIONS</code> is specified, the configuration for the cluster is included.</p> <p>If <code>STATISTICS</code> is specified, the task and service count is included, separated by launch type.</p> <p>If <code>TAGS</code> is specified, the metadata tags associated with the cluster are included.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a cluster
            This example provides a description of the specified cluster in your default region.

            >>> client.describe_clusters(clusters=['default'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_clusters

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_clusters.describe_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_clusters_request.DescribeClustersRequest = {}
        if clusters is not None:
            input_["clusters"] = clusters
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_command(
        self,
        command: "capo_ecs.types.string.String",
        interactive: "capo_ecs.types.boolean.Boolean",
        task: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        container: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.execute_command_response.ExecuteCommandResponse":
        """<p>Runs a command remotely on a container within a task.</p> <p>If you use a condition key in your IAM policy to refine the conditions for the policy statement, for example limit the actions to a specific cluster, you receive an <code>AccessDeniedException</code> when there is a mismatch between the condition key value and the corresponding parameter value.</p> <p>For information about required permissions and considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html">Using Amazon ECS Exec for debugging</a> in the <i>Amazon ECS Developer Guide</i>. </p>

        Args:
            cluster: <p>The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.</p>
            container: <p>The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.</p>
            command: <p>The command to run on the container.</p>
            interactive: <p>Use this flag to run your command in interactive mode.</p>
            task: <p>The Amazon Resource Name (ARN) or ID of the task the container is part of.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.target_not_connected_exception.TargetNotConnectedException: <p>The execute command cannot run. This error can be caused by any of the following configuration issues:</p> <ul> <li> <p>Incorrect IAM permissions</p> </li> <li> <p>The SSM agent is not installed or is not running</p> </li> <li> <p> There is an interface Amazon VPC endpoint for Amazon ECS, but there is not one for Systems Manager Session Manager</p> </li> </ul> <p>For information about how to troubleshoot the issues, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html">Troubleshooting issues with ECS Exec</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To run a command remotely on a container in a task
            This example runs an interactive /bin/sh command on a container MyContainer.

            >>> client.execute_command(cluster='MyCluster', container='MyContainer', command='/bin/sh', interactive=True, task='arn:aws:ecs:us-east-1:123456789012:task/MyCluster/d789e94343414c25b9f6bd59eEXAMPLE')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.execute_command_request.ExecuteCommandRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.execute_command_response.ExecuteCommandResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.execute_command

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.execute_command.execute_command(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.execute_command_request.ExecuteCommandRequest = {
            "command": command,
            "interactive": interactive,
            "task": task,
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if container is not None:
            input_["container"] = container

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_attributes(
        self,
        target_type: "capo_ecs.types.target_type.TargetType",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        attribute_name: Optional["capo_ecs.types.string.String"] = None,
        attribute_value: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_attributes_response.ListAttributesResponse":
        """<p>Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, <code>ListAttributes</code> returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value. You can do this, for example, to see which container instances in a cluster are running a Linux AMI (<code>ecs.os-type=linux</code>). </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            target_type: <p>The type of the target to list attributes with.</p>
            attribute_name: <p>The name of the attribute to filter the results with. </p>
            attribute_value: <p>The value of the attribute to filter results with. You must also specify an attribute name to use this parameter.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListAttributes</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of cluster results that <code>ListAttributes</code> returned in paginated output. When this parameter is used, <code>ListAttributes</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAttributes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListAttributes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list container instances that have a specific attribute
            This example lists attributes for a container instance with the attribute "stack" equal to the value "production".

            >>> client.list_attributes(cluster='MyCluster', target_type='container-instance', attribute_name='stack', attribute_value='production')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_attributes_request.ListAttributesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_attributes_response.ListAttributesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_attributes

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_attributes.list_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_attributes_request.ListAttributesRequest = {
            "target_type": target_type
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if attribute_name is not None:
            input_["attribute_name"] = attribute_name
        if attribute_value is not None:
            input_["attribute_value"] = attribute_value
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_clusters(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of existing clusters.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListClusters</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of cluster results that <code>ListClusters</code> returned in paginated output. When this parameter is used, <code>ListClusters</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListClusters</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListClusters</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available clusters
            This example lists all of your available clusters in your default region.

            >>> client.list_clusters()
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_clusters

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_clusters_request.ListClustersRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_container_instances(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        filter: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        status: Optional[
            "capo_ecs.types.container_instance_status.ContainerInstanceStatus"
        ] = None,
    ) -> "capo_ecs.types.list_container_instances_response.ListContainerInstancesResponse":
        """<p>Returns a list of container instances in a specified cluster. You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements inside the <code>filter</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.</p>
            filter: <p>You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListContainerInstances</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of container instance results that <code>ListContainerInstances</code> returned in paginated output. When this parameter is used, <code>ListContainerInstances</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListContainerInstances</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListContainerInstances</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            status: <p>Filters the container instances by status. For example, if you specify the <code>DRAINING</code> status, the results include only container instances that have been set to <code>DRAINING</code> using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html">UpdateContainerInstancesState</a>. If you don't specify this parameter, the The default is to include container instances set to all states other than <code>INACTIVE</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available container instances in a cluster
            This example lists all of your available container instances in the specified cluster in your default region.

            >>> client.list_container_instances(cluster='default')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_container_instances_request.ListContainerInstancesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_container_instances_response.ListContainerInstancesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_container_instances

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_container_instances.list_container_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_container_instances_request.ListContainerInstancesRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_attachment_state_changes(
        self,
        attachments: "capo_ecs.types.attachment_state_changes.AttachmentStateChanges",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that an attachment changed states.</p>

        Args:
            cluster: <p>The short name or full ARN of the cluster that hosts the container instance the attachment belongs to.</p>
            attachments: <p>Any attachments associated with the state change request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_attachment_state_changes

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_attachment_state_changes.submit_attachment_state_changes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest = {
            "attachments": attachments
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_container_state_change(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task: Optional["capo_ecs.types.string.String"] = None,
        container_name: Optional["capo_ecs.types.string.String"] = None,
        runtime_id: Optional["capo_ecs.types.string.String"] = None,
        status: Optional["capo_ecs.types.string.String"] = None,
        exit_code: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
        network_bindings: Optional[
            "capo_ecs.types.network_bindings.NetworkBindings"
        ] = None,
    ) -> "capo_ecs.types.submit_container_state_change_response.SubmitContainerStateChangeResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that a container changed states.</p>

        Args:
            cluster: <p>The short name or full ARN of the cluster that hosts the container.</p>
            task: <p>The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.</p>
            container_name: <p>The name of the container.</p>
            runtime_id: <p>The ID of the Docker container.</p>
            status: <p>The status of the state change request.</p>
            exit_code: <p>The exit code that's returned for the state change request.</p>
            reason: <p>The reason for the state change request.</p>
            network_bindings: <p>The network bindings of the container.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.submit_container_state_change_request.SubmitContainerStateChangeRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.submit_container_state_change_response.SubmitContainerStateChangeResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_container_state_change

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_container_state_change.submit_container_state_change(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.submit_container_state_change_request.SubmitContainerStateChangeRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if task is not None:
            input_["task"] = task
        if container_name is not None:
            input_["container_name"] = container_name
        if runtime_id is not None:
            input_["runtime_id"] = runtime_id
        if status is not None:
            input_["status"] = status
        if exit_code is not None:
            input_["exit_code"] = exit_code
        if reason is not None:
            input_["reason"] = reason
        if network_bindings is not None:
            input_["network_bindings"] = network_bindings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def submit_task_state_change(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task: Optional["capo_ecs.types.string.String"] = None,
        status: Optional["capo_ecs.types.string.String"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
        containers: Optional[
            "capo_ecs.types.container_state_changes.ContainerStateChanges"
        ] = None,
        attachments: Optional[
            "capo_ecs.types.attachment_state_changes.AttachmentStateChanges"
        ] = None,
        managed_agents: Optional[
            "capo_ecs.types.managed_agent_state_changes.ManagedAgentStateChanges"
        ] = None,
        pull_started_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
        pull_stopped_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
        execution_stopped_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
    ) -> (
        "capo_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse"
    ):
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that a task changed states.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.</p>
            task: <p>The task ID or full ARN of the task in the state change request.</p>
            status: <p>The status of the state change request.</p>
            reason: <p>The reason for the state change request.</p>
            containers: <p>Any containers that's associated with the state change request.</p>
            attachments: <p>Any attachments associated with the state change request.</p>
            managed_agents: <p>The details for the managed agent that's associated with the task.</p>
            pull_started_at: <p>The Unix timestamp for the time when the container image pull started.</p>
            pull_stopped_at: <p>The Unix timestamp for the time when the container image pull completed.</p>
            execution_stopped_at: <p>The Unix timestamp for the time when the task execution stopped.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_task_state_change

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_task_state_change.submit_task_state_change(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if task is not None:
            input_["task"] = task
        if status is not None:
            input_["status"] = status
        if reason is not None:
            input_["reason"] = reason
        if containers is not None:
            input_["containers"] = containers
        if attachments is not None:
            input_["attachments"] = attachments
        if managed_agents is not None:
            input_["managed_agents"] = managed_agents
        if pull_started_at is not None:
            input_["pull_started_at"] = pull_started_at
        if pull_stopped_at is not None:
            input_["pull_stopped_at"] = pull_stopped_at
        if execution_stopped_at is not None:
            input_["execution_stopped_at"] = execution_stopped_at

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncClusterResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def update(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        settings: Optional["capo_ecs.types.cluster_settings.ClusterSettings"] = None,
        configuration: Optional[
            "capo_ecs.types.cluster_configuration.ClusterConfiguration"
        ] = None,
        service_connect_defaults: Optional[
            "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
        ] = None,
    ) -> "capo_ecs.types.update_cluster_response.UpdateClusterResponse":
        """<p>Updates the cluster.</p>

        Args:
            cluster: <p>The name of the cluster to modify the settings for.</p>
            settings: <p>The cluster settings for your cluster.</p>
            configuration: <p>The execute command configuration for the cluster.</p>
            service_connect_defaults: <p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster's observability settings.
            This example turns on enhanced containerInsights in an existing cluster.

            >>> await client.update(cluster='ECS-project-update-cluster', settings=[{'name': 'containerInsights', 'value': 'enhanced'}])
            To update a cluster's Service Connect defaults.
            This example sets a default Service Connect namespace.

            >>> await client.update(cluster='ECS-project-update-cluster', service_connect_defaults={'namespace': 'test'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_cluster_request.UpdateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster.async_update_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_cluster_request.UpdateClusterRequest = {
            "cluster": cluster
        }
        if settings is not None:
            input_["settings"] = settings
        if configuration is not None:
            input_["configuration"] = configuration
        if service_connect_defaults is not None:
            input_["service_connect_defaults"] = service_connect_defaults

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_cluster_response.DeleteClusterResponse":
        """<p>Deletes the specified cluster. The cluster transitions to the <code>INACTIVE</code> state. Clusters with an <code>INACTIVE</code> status might remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don't recommend that you rely on <code>INACTIVE</code> clusters persisting.</p> <p>You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListContainerInstances.html">ListContainerInstances</a> and deregister them with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html">DeregisterContainerInstance</a>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_contains_capacity_provider_exception.ClusterContainsCapacityProviderException: <p>The cluster contains one or more capacity providers that prevent the requested operation. This exception occurs when you try to delete a cluster that still has active capacity providers, including Amazon ECS Managed Instances capacity providers. You must first delete all capacity providers from the cluster before you can delete the cluster itself.</p>
            capo_ecs.errors.cluster_contains_container_instances_exception.ClusterContainsContainerInstancesException: <p>You can't delete a cluster that has registered container instances. First, deregister the container instances before you can delete the cluster. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html">DeregisterContainerInstance</a>.</p>
            capo_ecs.errors.cluster_contains_services_exception.ClusterContainsServicesException: <p>You can't delete a cluster that contains services. First, update the service to reduce its desired task count to 0, and then delete the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html">DeleteService</a>.</p>
            capo_ecs.errors.cluster_contains_tasks_exception.ClusterContainsTasksException: <p>You can't delete a cluster that has active tasks.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an empty cluster
            This example deletes an empty cluster in your default region.

            >>> await client.delete(cluster='my_cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_cluster.async_delete_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster": cluster
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_cluster_capacity_providers(
        self,
        cluster: "capo_ecs.types.string.String",
        capacity_providers: "capo_ecs.types.string_list.StringList",
        default_capacity_provider_strategy: "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse":
        """<p>Modifies the available capacity providers and the default capacity provider strategy for a cluster.</p> <p>You must specify both the available capacity providers and a default capacity provider strategy for the cluster. If the specified cluster has existing capacity providers associated with it, you must specify all existing capacity providers in addition to any new ones you want to add. Any existing capacity providers that are associated with a cluster that are omitted from a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API call will be disassociated with the cluster. You can only disassociate an existing capacity provider from a cluster if it's not being used by any existing tasks.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified, then the cluster's default capacity provider strategy is used. We recommend that you define a default capacity provider strategy for your cluster. However, you must specify an empty array (<code>[]</code>) to bypass defining a default strategy.</p> <p>Amazon ECS Managed Instances doesn't support this, because when you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to modify the capacity provider settings for. If you don't specify a cluster, the default cluster is assumed.</p>
            capacity_providers: <p>The name of one or more capacity providers to associate with the cluster.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>
            default_capacity_provider_strategy: <p>The capacity provider strategy to use by default for the cluster.</p> <p>When creating a service or running a task on a cluster, if no capacity provider or launch type is specified then the default capacity provider strategy for the cluster is used.</p> <p>A capacity provider strategy consists of one or more capacity providers along with the <code>base</code> and <code>weight</code> to assign to them. A capacity provider must be associated with the cluster to be used in a capacity provider strategy. The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API is used to associate a capacity provider with a cluster. Only capacity providers with an <code>ACTIVE</code> or <code>UPDATING</code> status can be used.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is in-use and can't be removed.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add an existing capacity provider to a cluuster
            This example adds an existing capacity provider "MyCapacityProvider2" to a cluster that already has the capacity provider "MyCapacityProvider1" associated with it. Both "MyCapacityProvider2" and "MyCapacityProvider1" need to be specified.

            >>> await client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=['MyCapacityProvider1', 'MyCapacityProvider2'], default_capacity_provider_strategy=[{'capacityProvider': 'MyCapacityProvider1', 'weight': 1}, {'capacityProvider': 'MyCapacityProvider2', 'weight': 1}])
            To remove a capacity provider from a cluster
            This example removes a capacity provider "MyCapacityProvider2" from a cluster that has both "MyCapacityProvider2" and "MyCapacityProvider1" associated with it. Only "MyCapacityProvider1" needs to be specified in this scenario.

            >>> await client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=['MyCapacityProvider1'], default_capacity_provider_strategy=[{'capacityProvider': 'MyCapacityProvider1', 'weight': 1, 'base': 0}])
            To remove all capacity providers from a cluster
            This example removes all capacity providers associated with a cluster.

            >>> await client.put_cluster_capacity_providers(cluster='MyCluster', capacity_providers=[], default_capacity_provider_strategy=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.put_cluster_capacity_providers_response.PutClusterCapacityProvidersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.put_cluster_capacity_providers

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.put_cluster_capacity_providers.async_put_cluster_capacity_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.put_cluster_capacity_providers_request.PutClusterCapacityProvidersRequest = {
            "cluster": cluster,
            "capacity_providers": capacity_providers,
            "default_capacity_provider_strategy": default_capacity_provider_strategy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cluster_settings(
        self,
        cluster: "capo_ecs.types.string.String",
        settings: "capo_ecs.types.cluster_settings.ClusterSettings",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> (
        "capo_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse"
    ):
        """<p>Modifies the settings to use for a cluster.</p>

        Args:
            cluster: <p>The name of the cluster to modify the settings for.</p>
            settings: <p>The setting to use by default for a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p> <important> <p>Currently, if you delete an existing cluster that does not have Container Insights turned on, and then create a new cluster with the same name with Container Insights tuned on, Container Insights will not actually be turned on. If you want to preserve the same name for your existing cluster and turn on Container Insights, you must wait 7 days before you can re-create it.</p> </important>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.update_in_progress_exception.UpdateInProgressException: <p>There's already a current Amazon ECS container agent update in progress on the container instance that's specified. If the container agent becomes disconnected while it's in a transitional stage, such as <code>PENDING</code> or <code>STAGING</code>, the update process can get stuck in that state. However, when the agent reconnects, it resumes where it stopped previously.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster's settings
            This example enables CloudWatch Container Insights for the default cluster.

            >>> await client.update_cluster_settings(cluster='default', settings=[{'name': 'containerInsights', 'value': 'enabled'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster_settings

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_cluster_settings.async_update_cluster_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest = {
            "cluster": cluster,
            "settings": settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cluster(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster_name: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        settings: Optional["capo_ecs.types.cluster_settings.ClusterSettings"] = None,
        configuration: Optional[
            "capo_ecs.types.cluster_configuration.ClusterConfiguration"
        ] = None,
        capacity_providers: Optional["capo_ecs.types.string_list.StringList"] = None,
        default_capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        service_connect_defaults: Optional[
            "capo_ecs.types.cluster_service_connect_defaults_request.ClusterServiceConnectDefaultsRequest"
        ] = None,
    ) -> "capo_ecs.types.create_cluster_response.CreateClusterResponse":
        """<p>Creates a new Amazon ECS cluster. By default, your account receives a <code>default</code> cluster when you launch your first container instance. However, you can create your own cluster with a unique name.</p> <note> <p>When you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html">CreateCluster</a> API operation, Amazon ECS attempts to create the Amazon ECS service-linked role for your account. This is so that it can manage required resources in other Amazon Web Services services on your behalf. However, if the user that makes the call doesn't have permissions to create the service-linked role, it isn't created. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>

        Args:
            cluster_name: <p>The name of your cluster. If you don't specify a name for your cluster, you create a cluster that's named <code>default</code>. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. </p>
            tags: <p>The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            settings: <p>The setting to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights for a cluster. If this value is specified, it overrides the <code>containerInsights</code> value set with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html">PutAccountSetting</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html">PutAccountSettingDefault</a>.</p>
            configuration: <p>The <code>execute</code> command configuration for the cluster.</p>
            capacity_providers: <p>The short name of one or more capacity providers to associate with the cluster. A capacity provider must be associated with a cluster before it can be included as part of the default capacity provider strategy of the cluster or used in a capacity provider strategy when calling the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> actions.</p> <p>If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must be created but not associated with another cluster. New Auto Scaling group capacity providers can be created with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCapacityProvider.html">CreateCapacityProvider</a> API operation.</p> <p>To use a Fargate capacity provider, specify either the <code>FARGATE</code> or <code>FARGATE_SPOT</code> capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used.</p> <p>The <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutCapacityProvider.html">PutCapacityProvider</a> API operation is used to update the list of available capacity providers for a cluster after the cluster is created.</p>
            default_capacity_provider_strategy: <p>The capacity provider strategy to set as the default for the cluster. After a default capacity provider strategy is set for a cluster, when you call the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html">RunTask</a> APIs with no capacity provider strategy or launch type specified, the default capacity provider strategy for the cluster is used.</p> <p>If a default capacity provider strategy isn't defined for a cluster when it was created, it can be defined later with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html">PutClusterCapacityProviders</a> API operation.</p>
            service_connect_defaults: <p>Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the <code>enabled</code> parameter to <code>true</code> in the <code>ServiceConnectConfiguration</code>. You can set the namespace of each service individually in the <code>ServiceConnectConfiguration</code> to override this default parameter.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new cluster
            This example creates a cluster in your default region.

            >>> await client.create_cluster(cluster_name='my_cluster')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_cluster_request.CreateClusterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_cluster

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_cluster.async_create_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_cluster_request.CreateClusterRequest = {}
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if tags is not None:
            input_["tags"] = tags
        if settings is not None:
            input_["settings"] = settings
        if configuration is not None:
            input_["configuration"] = configuration
        if capacity_providers is not None:
            input_["capacity_providers"] = capacity_providers
        if default_capacity_provider_strategy is not None:
            input_["default_capacity_provider_strategy"] = (
                default_capacity_provider_strategy
            )
        if service_connect_defaults is not None:
            input_["service_connect_defaults"] = service_connect_defaults

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_container_instance(
        self,
        container_instance: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.deregister_container_instance_response.DeregisterContainerInstanceResponse":
        """<p>Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.</p> <p>If you intend to use the container instance for some other purpose after deregistration, we recommend that you stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.</p> <p>Deregistering a container instance removes the instance from a cluster, but it doesn't terminate the EC2 instance. If you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.</p> <note> <p>If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents aren't automatically deregistered when terminated).</p> </note>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instance: <p>The container instance ID or full ARN of the container instance to deregister. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>
            force: <p>Forces the container instance to be deregistered. If you have tasks running on the container instance when you deregister it with the <code>force</code> option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they're orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible. </p> <p>Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To deregister a container instance from a cluster
            This example deregisters a container instance from the specified cluster in your default region. If there are still tasks running on the container instance, you must either stop those tasks before deregistering, or use the force option.

            >>> await client.deregister_container_instance(cluster='default', force=True, container_instance='container_instance_UUID')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.deregister_container_instance_request.DeregisterContainerInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.deregister_container_instance_response.DeregisterContainerInstanceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_container_instance

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.deregister_container_instance.async_deregister_container_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.deregister_container_instance_request.DeregisterContainerInstanceRequest = {
            "container_instance": container_instance
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_clusters(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        clusters: Optional["capo_ecs.types.string_list.StringList"] = None,
        include: Optional["capo_ecs.types.cluster_field_list.ClusterFieldList"] = None,
    ) -> "capo_ecs.types.describe_clusters_response.DescribeClustersResponse":
        """<p>Describes one or more of your clusters.</p> <p> For CLI examples, see <a href="https://github.com/aws/aws-cli/blob/develop/awscli/examples/ecs/describe-clusters.rst">describe-clusters.rst</a> on GitHub.</p>

        Args:
            clusters: <p>A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.</p>
            include: <p>Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isn't included.</p> <p>If <code>ATTACHMENTS</code> is specified, the attachments for the container instances or tasks within the cluster are included, for example the capacity providers.</p> <p>If <code>SETTINGS</code> is specified, the settings for the cluster are included.</p> <p>If <code>CONFIGURATIONS</code> is specified, the configuration for the cluster is included.</p> <p>If <code>STATISTICS</code> is specified, the task and service count is included, separated by launch type.</p> <p>If <code>TAGS</code> is specified, the metadata tags associated with the cluster are included.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a cluster
            This example provides a description of the specified cluster in your default region.

            >>> await client.describe_clusters(clusters=['default'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_clusters_request.DescribeClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_clusters_response.DescribeClustersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_clusters

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_clusters.async_describe_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_clusters_request.DescribeClustersRequest = {}
        if clusters is not None:
            input_["clusters"] = clusters
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_command(
        self,
        command: "capo_ecs.types.string.String",
        interactive: "capo_ecs.types.boolean.Boolean",
        task: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        container: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.execute_command_response.ExecuteCommandResponse":
        """<p>Runs a command remotely on a container within a task.</p> <p>If you use a condition key in your IAM policy to refine the conditions for the policy statement, for example limit the actions to a specific cluster, you receive an <code>AccessDeniedException</code> when there is a mismatch between the condition key value and the corresponding parameter value.</p> <p>For information about required permissions and considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html">Using Amazon ECS Exec for debugging</a> in the <i>Amazon ECS Developer Guide</i>. </p>

        Args:
            cluster: <p>The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.</p>
            container: <p>The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.</p>
            command: <p>The command to run on the container.</p>
            interactive: <p>Use this flag to run your command in interactive mode.</p>
            task: <p>The Amazon Resource Name (ARN) or ID of the task the container is part of.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.target_not_connected_exception.TargetNotConnectedException: <p>The execute command cannot run. This error can be caused by any of the following configuration issues:</p> <ul> <li> <p>Incorrect IAM permissions</p> </li> <li> <p>The SSM agent is not installed or is not running</p> </li> <li> <p> There is an interface Amazon VPC endpoint for Amazon ECS, but there is not one for Systems Manager Session Manager</p> </li> </ul> <p>For information about how to troubleshoot the issues, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html">Troubleshooting issues with ECS Exec</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To run a command remotely on a container in a task
            This example runs an interactive /bin/sh command on a container MyContainer.

            >>> await client.execute_command(cluster='MyCluster', container='MyContainer', command='/bin/sh', interactive=True, task='arn:aws:ecs:us-east-1:123456789012:task/MyCluster/d789e94343414c25b9f6bd59eEXAMPLE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.execute_command_request.ExecuteCommandRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.execute_command_response.ExecuteCommandResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.execute_command

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.execute_command.async_execute_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.execute_command_request.ExecuteCommandRequest = {
            "command": command,
            "interactive": interactive,
            "task": task,
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if container is not None:
            input_["container"] = container

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_attributes(
        self,
        target_type: "capo_ecs.types.target_type.TargetType",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        attribute_name: Optional["capo_ecs.types.string.String"] = None,
        attribute_value: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_attributes_response.ListAttributesResponse":
        """<p>Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, <code>ListAttributes</code> returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value. You can do this, for example, to see which container instances in a cluster are running a Linux AMI (<code>ecs.os-type=linux</code>). </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.</p>
            target_type: <p>The type of the target to list attributes with.</p>
            attribute_name: <p>The name of the attribute to filter the results with. </p>
            attribute_value: <p>The value of the attribute to filter results with. You must also specify an attribute name to use this parameter.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListAttributes</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of cluster results that <code>ListAttributes</code> returned in paginated output. When this parameter is used, <code>ListAttributes</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAttributes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListAttributes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list container instances that have a specific attribute
            This example lists attributes for a container instance with the attribute "stack" equal to the value "production".

            >>> await client.list_attributes(cluster='MyCluster', target_type='container-instance', attribute_name='stack', attribute_value='production')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_attributes_request.ListAttributesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_attributes_response.ListAttributesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_attributes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_attributes.async_list_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_attributes_request.ListAttributesRequest = {
            "target_type": target_type
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if attribute_name is not None:
            input_["attribute_name"] = attribute_name
        if attribute_value is not None:
            input_["attribute_value"] = attribute_value
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

    async def list_clusters(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_clusters_response.ListClustersResponse":
        """<p>Returns a list of existing clusters.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListClusters</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of cluster results that <code>ListClusters</code> returned in paginated output. When this parameter is used, <code>ListClusters</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListClusters</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListClusters</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available clusters
            This example lists all of your available clusters in your default region.

            >>> await client.list_clusters()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_clusters_request.ListClustersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_clusters

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_clusters.async_list_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_clusters_request.ListClustersRequest = {}
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

    async def list_container_instances(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        filter: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        status: Optional[
            "capo_ecs.types.container_instance_status.ContainerInstanceStatus"
        ] = None,
    ) -> "capo_ecs.types.list_container_instances_response.ListContainerInstancesResponse":
        """<p>Returns a list of container instances in a specified cluster. You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements inside the <code>filter</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.</p>
            filter: <p>You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListContainerInstances</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of container instance results that <code>ListContainerInstances</code> returned in paginated output. When this parameter is used, <code>ListContainerInstances</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListContainerInstances</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListContainerInstances</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            status: <p>Filters the container instances by status. For example, if you specify the <code>DRAINING</code> status, the results include only container instances that have been set to <code>DRAINING</code> using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html">UpdateContainerInstancesState</a>. If you don't specify this parameter, the The default is to include container instances set to all states other than <code>INACTIVE</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your available container instances in a cluster
            This example lists all of your available container instances in the specified cluster in your default region.

            >>> await client.list_container_instances(cluster='default')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_container_instances_request.ListContainerInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_container_instances_response.ListContainerInstancesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_container_instances

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_container_instances.async_list_container_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_container_instances_request.ListContainerInstancesRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_attachment_state_changes(
        self,
        attachments: "capo_ecs.types.attachment_state_changes.AttachmentStateChanges",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that an attachment changed states.</p>

        Args:
            cluster: <p>The short name or full ARN of the cluster that hosts the container instance the attachment belongs to.</p>
            attachments: <p>Any attachments associated with the state change request.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_attachment_state_changes

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_attachment_state_changes.async_submit_attachment_state_changes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest = {
            "attachments": attachments
        }
        if cluster is not None:
            input_["cluster"] = cluster

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_container_state_change(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task: Optional["capo_ecs.types.string.String"] = None,
        container_name: Optional["capo_ecs.types.string.String"] = None,
        runtime_id: Optional["capo_ecs.types.string.String"] = None,
        status: Optional["capo_ecs.types.string.String"] = None,
        exit_code: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
        network_bindings: Optional[
            "capo_ecs.types.network_bindings.NetworkBindings"
        ] = None,
    ) -> "capo_ecs.types.submit_container_state_change_response.SubmitContainerStateChangeResponse":
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that a container changed states.</p>

        Args:
            cluster: <p>The short name or full ARN of the cluster that hosts the container.</p>
            task: <p>The task ID or full Amazon Resource Name (ARN) of the task that hosts the container.</p>
            container_name: <p>The name of the container.</p>
            runtime_id: <p>The ID of the Docker container.</p>
            status: <p>The status of the state change request.</p>
            exit_code: <p>The exit code that's returned for the state change request.</p>
            reason: <p>The reason for the state change request.</p>
            network_bindings: <p>The network bindings of the container.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.submit_container_state_change_request.SubmitContainerStateChangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.submit_container_state_change_response.SubmitContainerStateChangeResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_container_state_change

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_container_state_change.async_submit_container_state_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.submit_container_state_change_request.SubmitContainerStateChangeRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if task is not None:
            input_["task"] = task
        if container_name is not None:
            input_["container_name"] = container_name
        if runtime_id is not None:
            input_["runtime_id"] = runtime_id
        if status is not None:
            input_["status"] = status
        if exit_code is not None:
            input_["exit_code"] = exit_code
        if reason is not None:
            input_["reason"] = reason
        if network_bindings is not None:
            input_["network_bindings"] = network_bindings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_task_state_change(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task: Optional["capo_ecs.types.string.String"] = None,
        status: Optional["capo_ecs.types.string.String"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
        containers: Optional[
            "capo_ecs.types.container_state_changes.ContainerStateChanges"
        ] = None,
        attachments: Optional[
            "capo_ecs.types.attachment_state_changes.AttachmentStateChanges"
        ] = None,
        managed_agents: Optional[
            "capo_ecs.types.managed_agent_state_changes.ManagedAgentStateChanges"
        ] = None,
        pull_started_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
        pull_stopped_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
        execution_stopped_at: Optional["capo_ecs.types.timestamp.Timestamp"] = None,
    ) -> (
        "capo_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse"
    ):
        """<note> <p>This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.</p> </note> <p>Sent to acknowledge that a task changed states.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.</p>
            task: <p>The task ID or full ARN of the task in the state change request.</p>
            status: <p>The status of the state change request.</p>
            reason: <p>The reason for the state change request.</p>
            containers: <p>Any containers that's associated with the state change request.</p>
            attachments: <p>Any attachments associated with the state change request.</p>
            managed_agents: <p>The details for the managed agent that's associated with the task.</p>
            pull_started_at: <p>The Unix timestamp for the time when the container image pull started.</p>
            pull_stopped_at: <p>The Unix timestamp for the time when the container image pull completed.</p>
            execution_stopped_at: <p>The Unix timestamp for the time when the task execution stopped.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_task_state_change

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.submit_task_state_change.async_submit_task_state_change(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if task is not None:
            input_["task"] = task
        if status is not None:
            input_["status"] = status
        if reason is not None:
            input_["reason"] = reason
        if containers is not None:
            input_["containers"] = containers
        if attachments is not None:
            input_["attachments"] = attachments
        if managed_agents is not None:
            input_["managed_agents"] = managed_agents
        if pull_started_at is not None:
            input_["pull_started_at"] = pull_started_at
        if pull_stopped_at is not None:
            input_["pull_stopped_at"] = pull_stopped_at
        if execution_stopped_at is not None:
            input_["execution_stopped_at"] = execution_stopped_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
