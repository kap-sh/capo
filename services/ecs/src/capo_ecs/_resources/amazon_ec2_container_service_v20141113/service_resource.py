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
    import capo_ecs.types.availability_zone_rebalancing
    import capo_ecs.types.boolean
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.create_express_gateway_service_request
    import capo_ecs.types.create_express_gateway_service_response
    import capo_ecs.types.create_service_request
    import capo_ecs.types.create_service_response
    import capo_ecs.types.created_at
    import capo_ecs.types.delete_express_gateway_service_request
    import capo_ecs.types.delete_express_gateway_service_response
    import capo_ecs.types.delete_service_request
    import capo_ecs.types.delete_service_response
    import capo_ecs.types.deployment_configuration
    import capo_ecs.types.deployment_controller
    import capo_ecs.types.describe_express_gateway_service_request
    import capo_ecs.types.describe_express_gateway_service_response
    import capo_ecs.types.describe_services_request
    import capo_ecs.types.describe_services_response
    import capo_ecs.types.express_cpu_architecture
    import capo_ecs.types.express_gateway_container
    import capo_ecs.types.express_gateway_scaling_target
    import capo_ecs.types.express_gateway_service_include_list
    import capo_ecs.types.express_gateway_service_network_configuration
    import capo_ecs.types.launch_type
    import capo_ecs.types.list_service_deployments_request
    import capo_ecs.types.list_service_deployments_response
    import capo_ecs.types.list_services_request
    import capo_ecs.types.list_services_response
    import capo_ecs.types.load_balancers
    import capo_ecs.types.monitoring_configuration
    import capo_ecs.types.network_configuration
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.resource_management_type
    import capo_ecs.types.scheduling_strategy
    import capo_ecs.types.service_connect_configuration
    import capo_ecs.types.service_deployment_status_list
    import capo_ecs.types.service_field_list
    import capo_ecs.types.service_registries
    import capo_ecs.types.service_volume_configurations
    import capo_ecs.types.stop_service_deployment_request
    import capo_ecs.types.stop_service_deployment_response
    import capo_ecs.types.stop_service_deployment_stop_type
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags
    import capo_ecs.types.update_express_gateway_service_request
    import capo_ecs.types.update_express_gateway_service_response
    import capo_ecs.types.update_service_primary_task_set_request
    import capo_ecs.types.update_service_primary_task_set_response
    import capo_ecs.types.update_service_request
    import capo_ecs.types.update_service_response
    import capo_ecs.types.vpc_lattice_configurations
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class ServiceResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def update_service_primary_task_set(
        self,
        cluster: "capo_ecs.types.string.String",
        service: "capo_ecs.types.string.String",
        primary_task_set: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.update_service_primary_task_set_response.UpdateServicePrimaryTaskSetResponse":
        """<p>Modifies which task set in a service is the primary task set. Any parameters that are updated on the primary task set in a service will transition to the service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.</p>
            primary_task_set: <p>The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.task_set_not_found_exception.TaskSetNotFoundException: <p>The specified task set wasn't found. You can view your available task sets with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html">DescribeTaskSets</a>. Task sets are specific to each cluster, service and Region.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the primary task set for a service
            This example updates the primary task set for a service MyService that uses the EXTERNAL deployment controller type.

            >>> client.update_service_primary_task_set(cluster='MyCluster', service='MyService', primary_task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_service_primary_task_set_request.UpdateServicePrimaryTaskSetRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_service_primary_task_set_response.UpdateServicePrimaryTaskSetResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service_primary_task_set

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service_primary_task_set.update_service_primary_task_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_service_primary_task_set_request.UpdateServicePrimaryTaskSetRequest = {
            "cluster": cluster,
            "service": service,
            "primary_task_set": primary_task_set,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_express_gateway_service(
        self,
        infrastructure_role_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        service_name: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        health_check_path: Optional["capo_ecs.types.string.String"] = None,
        primary_container: Optional[
            "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
        ] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        cpu_architecture: Optional[
            "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
        ] = None,
        scaling_target: Optional[
            "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        task_definition_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.create_express_gateway_service_response.CreateExpressGatewayServiceResponse":
        """<p>Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed Amazon Web Services infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.</p> <p>Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary Amazon Web Services resources for traffic distribution, health monitoring, network access control, and capacity management.</p> <p>Provide an execution role for task operations and an infrastructure role for managing Amazon Web Services resources on your behalf.</p>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. This role is required for Amazon ECS to pull container images from Amazon ECR, send container logs to Amazon CloudWatch Logs, and retrieve sensitive data from Amazon Web Services Systems Manager Parameter Store or Amazon Web Services Secrets Manager.</p> <p>The execution role must include the <code>AmazonECSTaskExecutionRolePolicy</code> managed policy or equivalent permissions. For Express services, this role is used during task startup and runtime for container management operations.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the infrastructure role that grants Amazon ECS permission to create and manage Amazon Web Services resources on your behalf for the Express service. This role is used to provision and manage Application Load Balancers, target groups, security groups, auto-scaling policies, and other Amazon Web Services infrastructure components.</p> <p>The infrastructure role must include permissions for Elastic Load Balancing, Application Auto Scaling, Amazon EC2 (for security groups), and other services required for managed infrastructure. This role is only used during Express service creation, updates, and deletion operations.</p>
            service_name: <p>The name of the Express service. This name must be unique within the specified cluster and can contain up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens. The name is used to identify the service in the Amazon ECS console and API operations.</p> <p>If you don't specify a service name, Amazon ECS generates a unique name for the service. The service name becomes part of the service ARN and cannot be changed after the service is created.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster on which to create the Express service. If you do not specify a cluster, the <code>default</code> cluster is assumed.</p>
            health_check_path: <p>The path on the container that the Application Load Balancer uses for health checks. This should be a valid HTTP endpoint that returns a successful response (HTTP 200) when the application is healthy.</p> <p>If not specified, the default health check path is <code>/ping</code>. The health check path must start with a forward slash and can include query parameters. Examples: <code>/health</code>, <code>/api/status</code>, <code>/ping?format=json</code>.</p>
            primary_container: <p>The primary container configuration for the Express service. This defines the main application container that will receive traffic from the Application Load Balancer.</p> <p>The primary container must specify at minimum a container image. You can also configure the container port (defaults to 80), logging configuration, environment variables, secrets, and startup commands. The container image can be from Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.</p>
            task_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. This role allows your application code to access other Amazon Web Services services securely.</p> <p>The task role is different from the execution role. While the execution role is used by the Amazon ECS agent to set up the task, the task role is used by your application code running inside the container to make Amazon Web Services API calls. If your application doesn't need to access Amazon Web Services services, you can omit this parameter.</p>
            network_configuration: <p>The network configuration for the Express service tasks. This specifies the VPC subnets and security groups for the tasks.</p> <p>For Express services, you can specify custom security groups and subnets. If not provided, Amazon ECS will use the default VPC configuration and create appropriate security groups automatically. The network configuration determines how your service integrates with your VPC and what network access it has.</p>
            cpu: <p>The number of CPU units used by the task. This parameter determines the CPU allocation for each task in the Express service. The default value for an Express service is 256 (.25 vCPU).</p>
            memory: <p>The amount of memory (in MiB) used by the task. This parameter determines the memory allocation for each task in the Express service. The default value for an express service is 512 MiB.</p>
            cpu_architecture: <p>The CPU architecture that the tasks in the Express service run on. Amazon ECS applies this value to the task definition revision that it registers for the service. If you don't specify a value, the default is <code>X86_64</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Make sure that the container image that you specify supports the architecture that you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> when you also specify <code>taskDefinitionArn</code>, because this value applies only to a task definition that Amazon ECS registers on your behalf.</p>
            scaling_target: <p>The auto-scaling configuration for the Express service. This defines how the service automatically adjusts the number of running tasks based on demand.</p> <p>You can specify the minimum and maximum number of tasks, the scaling metric (CPU utilization, memory utilization, or request count per target), and the target value for the metric. If not specified, the default target value for an Express service is 60.</p>
            tags: <p>The metadata that you apply to the Express service to help categorize and organize it. Each tag consists of a key and an optional value. You can apply up to 50 tags to a service.</p>
            task_definition_arn: <p>The Amazon Resource Name (ARN) of a task definition to use to create the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.create_express_gateway_service_request.CreateExpressGatewayServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.create_express_gateway_service_response.CreateExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_express_gateway_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.create_express_gateway_service.create_express_gateway_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_express_gateway_service_request.CreateExpressGatewayServiceRequest = {
            "infrastructure_role_arn": infrastructure_role_arn
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if service_name is not None:
            input_["service_name"] = service_name
        if cluster is not None:
            input_["cluster"] = cluster
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if primary_container is not None:
            input_["primary_container"] = primary_container
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if cpu_architecture is not None:
            input_["cpu_architecture"] = cpu_architecture
        if scaling_target is not None:
            input_["scaling_target"] = scaling_target
        if tags is not None:
            input_["tags"] = tags
        if task_definition_arn is not None:
            input_["task_definition_arn"] = task_definition_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_service(
        self,
        service_name: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task_definition: Optional["capo_ecs.types.string.String"] = None,
        availability_zone_rebalancing: Optional[
            "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        desired_count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        role: Optional["capo_ecs.types.string.String"] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        health_check_grace_period_seconds: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        deployment_controller: Optional[
            "capo_ecs.types.deployment_controller.DeploymentController"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        service_connect_configuration: Optional[
            "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
        ] = None,
        volume_configurations: Optional[
            "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
        ] = None,
        vpc_lattice_configurations: Optional[
            "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
        ] = None,
        monitoring: Optional[
            "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
    ) -> "capo_ecs.types.create_service_response.CreateServiceResponse":
        """<p>Runs and maintains your desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the <code>desiredCount</code>, Amazon ECS runs another copy of the task in the specified cluster. To update an existing service, use <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind one or more load balancers. The load balancers distribute traffic across the tasks that are associated with the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. <code>volumeConfigurations</code> is only supported for REPLICA service and not DAEMON service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Tasks for services that don't use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code> - The replica scheduling strategy places and maintains your desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Service scheduler concepts</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>DAEMON</code> - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It also stops tasks that don't meet the placement constraints. When using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Amazon ECS services</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> </ul> <p>The deployment controller is the mechanism that determines how tasks are deployed for your service. The valid options are:</p> <ul> <li> <p>ECS</p> <p> When you create a service which uses the <code>ECS</code> deployment controller, you can choose between the following deployment strategies (which you can set in the “<code>strategy</code>” field in “<code>deploymentConfiguration</code>”): :</p> <ul> <li> <p> <code>ROLLING</code>: When you create a service which uses the <i>rolling update</i> (<code>ROLLING</code>) deployment strategy, the Amazon ECS service scheduler replaces the currently running tasks with new tasks. The number of tasks that Amazon ECS adds or removes from the service during a rolling update is controlled by the service deployment configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html">Deploy Amazon ECS services by replacing tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Rolling update deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual service updates: You need to update your service incrementally without taking the entire service offline at once.</p> </li> <li> <p>Limited resource requirements: You want to avoid the additional resource costs of running two complete environments simultaneously (as required by blue/green deployments).</p> </li> <li> <p>Acceptable deployment time: Your application can tolerate a longer deployment process, as rolling updates replace tasks one by one.</p> </li> <li> <p>No need for instant roll back: Your service can tolerate a rollback process that takes minutes rather than seconds.</p> </li> <li> <p>Simple deployment process: You prefer a straightforward deployment approach without the complexity of managing multiple environments, target groups, and listeners.</p> </li> <li> <p>No load balancer requirement: Your service doesn't use or require a load balancer, Application Load Balancer, Network Load Balancer, or Service Connect (which are required for blue/green deployments).</p> </li> <li> <p>Stateful applications: Your application maintains state that makes it difficult to run two parallel environments.</p> </li> <li> <p>Cost sensitivity: You want to minimize deployment costs by not running duplicate environments during deployment.</p> </li> </ul> <p>Rolling updates are the default deployment strategy for services and provide a balance between deployment safety and resource efficiency for many common application scenarios.</p> </li> <li> <p> <code>BLUE_GREEN</code>: A <i>blue/green</i> deployment strategy (<code>BLUE_GREEN</code>) is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html">Amazon ECS blue/green deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Amazon ECS blue/green deployments are best suited for the following scenarios:</p> <ul> <li> <p>Service validation: When you need to validate new service revisions before directing production traffic to them</p> </li> <li> <p>Zero downtime: When your service requires zero-downtime deployments</p> </li> <li> <p>Instant roll back: When you need the ability to quickly roll back if issues are detected</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect</p> </li> </ul> </li> <li> <p> <code>LINEAR</code>: A <i>linear</i> deployment strategy (<code>LINEAR</code>) gradually shifts traffic from the current production environment to a new environment in equal percentage increments. With Amazon ECS linear deployments, you can control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic.</p> <p>Linear deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual validation: When you want to gradually validate your new service version with increasing traffic</p> </li> <li> <p>Performance monitoring: When you need time to monitor metrics and performance during the deployment</p> </li> <li> <p>Risk minimization: When you want to minimize risk by exposing the new version to production traffic incrementally</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer or Service Connect</p> </li> </ul> </li> <li> <p> <code>CANARY</code>: A <i>canary</i> deployment strategy (<code>CANARY</code>) shifts a small percentage of traffic to the new service revision first, then shifts the remaining traffic all at once after a specified time period. This allows you to test the new version with a subset of users before full deployment.</p> <p>Canary deployments are best suited for the following scenarios:</p> <ul> <li> <p>Feature testing: When you want to test new features with a small subset of users before full rollout</p> </li> <li> <p>Production validation: When you need to validate performance and functionality with real production traffic</p> </li> <li> <p>Blast radius control: When you want to minimize blast radius if issues are discovered in the new version</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer or Service Connect</p> </li> </ul> </li> </ul> </li> <li> <p>External</p> <p>Use a third-party deployment controller.</p> </li> <li> <p>Blue/green deployment (powered by CodeDeploy)</p> <p>CodeDeploy installs an updated version of the application as a new replacement task set and reroutes production traffic from the original application task set to the replacement task set. The original task set is terminated after a successful deployment. Use this deployment controller to verify a new deployment of a service before sending production traffic to it.</p> </li> </ul> <p>When creating a service that uses the <code>EXTERNAL</code> deployment controller, you can specify only parameters that aren't controlled at the task set level. The only required parameter is the service name. You control your services using the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When the service scheduler launches new tasks, it determines task placement. For information about task placement and task placement strategies, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html">Amazon ECS task placement</a> in the <i>Amazon Elastic Container Service Developer Guide</i> </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</p>
            service_name: <p>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.</p>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>A task definition must be specified if the service uses either the <code>ECS</code> or <code>CODE_DEPLOY</code> deployment controllers.</p> <p>For more information about deployment types, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a>.</p>
            availability_zone_rebalancing: <p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul>
            load_balancers: <p>A load balancer object representing the load balancers to use with your service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>ECS</code> deployment controller and using either an Application Load Balancer or Network Load Balancer, you must specify one or more target group ARNs to attach to the service. The service-linked role is required for services that use multiple target groups. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>CODE_DEPLOY</code> deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an CodeDeploy deployment group, you specify two target groups (referred to as a <code>targetGroupPair</code>). During a deployment, CodeDeploy determines which task set in your service has the status <code>PRIMARY</code>, and it associates one target group with it. Then, it also associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that you can use to perform validation tests with Lambda functions before routing production traffic to it.</p> <p>If you use the <code>CODE_DEPLOY</code> deployment controller, these values can be changed when updating the service.</p> <p>For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name, and the container port to access from the load balancer. The container name must be as it appears in a container definition. The load balancer name parameter must be omitted. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group that's specified here.</p> <p>For Classic Load Balancers, this object must contain the load balancer name, the container name , and the container port to access from the load balancer. The container name must be as it appears in a container definition. The target group ARN parameter must be omitted. When a task from this service is placed on a container instance, the container instance is registered with the load balancer that's specified here.</p> <p>Services with tasks that use the <code>awsvpc</code> network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers aren't supported. Also, when you create any target groups for these services, you must choose <code>ip</code> as the target type, not <code>instance</code>. This is because tasks that use the <code>awsvpc</code> network mode are associated with an elastic network interface, not an Amazon EC2 instance.</p>
            service_registries: <p>The details of the service discovery registry to associate with this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service discovery</a>.</p> <note> <p>Each service may be associated with one service registry. Multiple service registries for each service isn't supported.</p> </note>
            desired_count: <p>The number of instantiations of the specified task definition to place and keep running in your service.</p> <p>This is required if <code>schedulingStrategy</code> is <code>REPLICA</code> or isn't specified. If <code>schedulingStrategy</code> is <code>DAEMON</code> then this isn't required.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            launch_type: <p>The infrastructure that you run your service on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A service can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>
            capacity_provider_strategy: <p>The capacity provider strategy to use for the service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>
            platform_version: <p>The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            role: <p>The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the <code>awsvpc</code> network mode. If you specify the <code>role</code> parameter, you must also specify a load balancer object with the <code>loadBalancers</code> parameter.</p> <important> <p>If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the <code>awsvpc</code> network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code> then you would specify <code>/foo/bar</code> as the role name. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p>
            deployment_configuration: <p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p>
            placement_constraints: <p>An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>
            placement_strategy: <p>The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.</p>
            network_configuration: <p>The network configuration for the service. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            health_check_grace_period_seconds: <p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. If you do not use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p>
            scheduling_strategy: <p>The scheduling strategy to use for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Services</a>.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types.</p> </li> <li> <p> <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.</p> <note> <p>Tasks using the Fargate launch type or the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types don't support the <code>DAEMON</code> scheduling strategy.</p> </note> </li> </ul>
            deployment_controller: <p>The deployment controller to use for the service. If no deployment controller is specified, the default value of <code>ECS</code> is used.</p>
            tags: <p>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When you use Amazon ECS managed tags, you must set the <code>propagateTags</code> request parameter.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <p>You must set this to a value other than <code>NONE</code> when you use Cost Explorer. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html">Amazon ECS usage reports</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The default is <code>NONE</code>.</p>
            enable_execute_command: <p>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, this enables execute command functionality on all containers in the service tasks.</p>
            service_connect_configuration: <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            volume_configurations: <p>The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.</p>
            vpc_lattice_configurations: <p>The VPC Lattice configuration for the service being created.</p>
            monitoring: <p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new service
            This example creates a service in your default region called ``ecs-simple-service``. The service uses the ``hello_world`` task definition and it maintains 10 copies of that task.

            >>> client.create_service(service_name='ecs-simple-service', task_definition='hello_world', desired_count=10)
            To create a new service behind a load balancer
            This example creates a service in your default region called ``ecs-simple-service-elb``. The service uses the ``ecs-demo`` task definition and it maintains 10 copies of that task. You must reference an existing load balancer in the same region by its name.

            >>> client.create_service(load_balancers=[{'containerName': 'simple-app', 'containerPort': 80, 'loadBalancerName': 'EC2Contai-EcsElast-15DCDAURT3ZO2'}], service_name='ecs-simple-service-elb', role='ecsServiceRole', task_definition='console-sample-app-static', desired_count=10)
            To create a service with a pause lifecycle hook
            This example creates a service with a blue/green deployment strategy that includes a pause lifecycle hook at the POST_PRODUCTION_TRAFFIC_SHIFT stage. The deployment will pause at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 60-minute timeout expires and triggers a rollback.

            >>> client.create_service(service_name='ecs-service-with-pause-hook', task_definition='ecs-demo', desired_count=2, deployment_configuration={'strategy': 'BLUE_GREEN', 'lifecycleHooks': [{'targetType': 'PAUSE', 'lifecycleStages': ['POST_PRODUCTION_TRAFFIC_SHIFT'], 'timeoutConfiguration': {'timeoutInMinutes': 60, 'action': 'ROLLBACK'}}]})
            To create a service with a monitoring configuration
            This example creates a service with a monitoring configuration that sets 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics. The monitoring configuration is not returned in the CreateService response. Use DescribeServiceRevisions to view the monitoring configuration.

            >>> client.create_service(service_name='ecs-monitored-service', task_definition='my-app:1', desired_count=2, monitoring={'metricConfigurations': [{'metricNames': ['CPUUtilization', 'MemoryUtilization'], 'resolutionSeconds': 20}]})
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_service_request.CreateServiceRequest = {
            "service_name": service_name
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if task_definition is not None:
            input_["task_definition"] = task_definition
        if availability_zone_rebalancing is not None:
            input_["availability_zone_rebalancing"] = availability_zone_rebalancing
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if desired_count is not None:
            input_["desired_count"] = desired_count
        if client_token is not None:
            input_["client_token"] = client_token
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if role is not None:
            input_["role"] = role
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if health_check_grace_period_seconds is not None:
            input_["health_check_grace_period_seconds"] = (
                health_check_grace_period_seconds
            )
        if scheduling_strategy is not None:
            input_["scheduling_strategy"] = scheduling_strategy
        if deployment_controller is not None:
            input_["deployment_controller"] = deployment_controller
        if tags is not None:
            input_["tags"] = tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if service_connect_configuration is not None:
            input_["service_connect_configuration"] = service_connect_configuration
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations
        if vpc_lattice_configurations is not None:
            input_["vpc_lattice_configurations"] = vpc_lattice_configurations
        if monitoring is not None:
            input_["monitoring"] = monitoring

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse":
        """<p>Deletes an Express service and removes all associated Amazon Web Services resources. This operation stops service tasks, removes the Application Load Balancer, target groups, security groups, auto-scaling policies, and other managed infrastructure components.</p> <p>The service enters a <code>DRAINING</code> state where existing tasks complete current requests without starting new tasks. After all tasks stop, the service and infrastructure are permanently removed.</p> <p>This operation cannot be reversed. Back up important data and verify the service is no longer needed before deletion.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to delete. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_express_gateway_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_express_gateway_service.delete_express_gateway_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you can't delete it, and you must update the service to a desired task count of zero. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <note> <p>When you delete a service, if there are still running tasks that require cleanup, the service status moves from <code>ACTIVE</code> to <code>DRAINING</code>, and the service is no longer visible in the console or in the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a> API operation. After all tasks have transitioned to either <code>STOPPING</code> or <code>STOPPED</code> status, the service status moves from <code>DRAINING</code> to <code>INACTIVE</code>. Services in the <code>DRAINING</code> or <code>INACTIVE</code> status can still be viewed with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html">DescribeServices</a> API operation. However, in the future, <code>INACTIVE</code> services may be cleaned up and purged from Amazon ECS record keeping, and <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html">DescribeServices</a> calls on those services return a <code>ServiceNotFoundException</code> error.</p> </note> <important> <p>If you attempt to create a new service with the same name as an existing service in either <code>ACTIVE</code> or <code>DRAINING</code> status, you receive an error.</p> </important>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.</p>
            service: <p>The name of the service to delete.</p>
            force: <p>If <code>true</code>, allows you to delete a service even if it wasn't scaled down to zero tasks. It's only necessary to use this if the service uses the <code>REPLICA</code> scheduling strategy.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a service
            This example deletes the my-http-service service. The service must have a desired count and running count of 0 before you can delete it.

            >>> client.delete_service(service='my-http-service')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_service_request.DeleteServiceRequest = {
            "service": service
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

    def describe_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        include: Optional[
            "capo_ecs.types.express_gateway_service_include_list.ExpressGatewayServiceIncludeList"
        ] = None,
    ) -> "capo_ecs.types.describe_express_gateway_service_response.DescribeExpressGatewayServiceResponse":
        """<p>Retrieves detailed information about an Express service, including current status, configuration, managed infrastructure, and service revisions.</p> <p>Returns comprehensive service details, active service revisions, ingress paths with endpoints, and managed Amazon Web Services resource status including load balancers and auto-scaling policies.</p> <p>Use the <code>include</code> parameter to retrieve additional information such as resource tags.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>
            include: <p>Specifies additional information to include in the response. Valid values are <code>TAGS</code> to include resource tags associated with the Express service.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_express_gateway_service_request.DescribeExpressGatewayServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_express_gateway_service_response.DescribeExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_express_gateway_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_express_gateway_service.describe_express_gateway_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_express_gateway_service_request.DescribeExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_services(
        self,
        services: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional["capo_ecs.types.service_field_list.ServiceFieldList"] = None,
    ) -> "capo_ecs.types.describe_services_response.DescribeServicesResponse":
        """<p>Describes the specified services running in your cluster.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.</p>
            services: <p>A list of services to describe. You may specify up to 10 services to describe in a single operation.</p>
            include: <p>Determines whether you want to see the resource tags for the service. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service
            This example provides descriptive information about the service named ``ecs-simple-service``.

            >>> client.describe_services(services=['ecs-simple-service'])
            To describe a service with a pause lifecycle hook
            This example provides descriptive information about the service ``ecs-service-with-pause-hook``, which is configured with a pause lifecycle hook in its deployment configuration.

            >>> client.describe_services(services=['ecs-service-with-pause-hook'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_services_request.DescribeServicesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_services_response.DescribeServicesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_services

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_services.describe_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_services_request.DescribeServicesRequest = {
            "services": services
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_deployments(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.service_deployment_status_list.ServiceDeploymentStatusList"
        ] = None,
        created_at: Optional["capo_ecs.types.created_at.CreatedAt"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_service_deployments_response.ListServiceDeploymentsResponse":
        """<p>This operation lists all the service deployments that meet the specified filter criteria.</p> <p>A service deployment happens when you release a software update for the service. You route traffic from the running service revisions to the new service revison and control the number of running tasks. </p> <p>This API returns the values that you use for the request parameters in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html">DescribeServiceRevisions</a>.</p>

        Args:
            service: <p>The ARN or name of the service</p>
            cluster: <p>The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you don't specify a cluster, <code>default</code> is used.</p>
            status: <p>An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.</p>
            created_at: <p>An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListServiceDeployments</code> request indicating that more results are available to fulfill the request and further calls are needed. If you provided <code>maxResults</code>, it's possible the number of results is fewer than <code>maxResults</code>.</p>
            max_results: <p>The maximum number of service deployment results that <code>ListServiceDeployments</code> returned in paginated output. When this parameter is used, <code>ListServiceDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>

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
            To list service deployments that meet the specified criteria
            This example lists all successful service deployments for the service "sd-example" in the cluster "example".

            >>> client.list_service_deployments(service='sd-example', cluster='example', status=['SUCCESSFUL'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_service_deployments_request.ListServiceDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_service_deployments_response.ListServiceDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_service_deployments

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_service_deployments.list_service_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_service_deployments_request.ListServiceDeploymentsRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if status is not None:
            input_["status"] = status
        if created_at is not None:
            input_["created_at"] = created_at
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

    def list_services(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        resource_management_type: Optional[
            "capo_ecs.types.resource_management_type.ResourceManagementType"
        ] = None,
    ) -> "capo_ecs.types.list_services_response.ListServicesResponse":
        """<p>Returns a list of services. You can filter the results by cluster, launch type, and scheduling strategy.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListServices</code> results. If you do not specify a cluster, the default cluster is assumed.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListServices</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of service results that <code>ListServices</code> returned in paginated output. When this parameter is used, <code>ListServices</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServices</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>
            launch_type: <p>The launch type to use when filtering the <code>ListServices</code> results.</p>
            scheduling_strategy: <p>The scheduling strategy to use when filtering the <code>ListServices</code> results.</p>
            resource_management_type: <p>The resourceManagementType type to use when filtering the <code>ListServices</code> results.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the services in a cluster
            This example lists the services running in the default cluster for an account.

            >>> client.list_services()
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_services_response.ListServicesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_services_request.ListServicesRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if scheduling_strategy is not None:
            input_["scheduling_strategy"] = scheduling_strategy
        if resource_management_type is not None:
            input_["resource_management_type"] = resource_management_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_service_deployment(
        self,
        service_deployment_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        stop_type: Optional[
            "capo_ecs.types.stop_service_deployment_stop_type.StopServiceDeploymentStopType"
        ] = None,
    ) -> (
        "capo_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse"
    ):
        """<p>Stops an ongoing service deployment.</p> <p>The following stop types are avaiable:</p> <ul> <li> <p>ROLLBACK - This option rolls back the service deployment to the previous service revision. </p> <p>You can use this option even if you didn't configure the service deployment for the rollback option. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stop-service-deployment.html">Stopping Amazon ECS service deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service_deployment_arn: <p>The ARN of the service deployment that you want to stop.</p>
            stop_type: <p>How you want Amazon ECS to stop the service. </p> <p>The valid values are <code>ROLLBACK</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. </p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_deployment_not_found_exception.ServiceDeploymentNotFoundException: <p>The service deploy ARN that you specified in the <code>ContinueServiceDeployment</code> doesn't exist. You can use <code>ListServiceDeployments</code> to retrieve the service deployment ARNs.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop a service deployment
            This example stops the service deployment using the ROLLBACK option.

            >>> client.stop_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', stop_type='ROLLBACK')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_service_deployment

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_service_deployment.stop_service_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest = {
            "service_deployment_arn": service_deployment_arn
        }
        if stop_type is not None:
            input_["stop_type"] = stop_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        health_check_path: Optional["capo_ecs.types.string.String"] = None,
        primary_container: Optional[
            "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
        ] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        cpu_architecture: Optional[
            "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
        ] = None,
        scaling_target: Optional[
            "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
        ] = None,
        task_definition_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse":
        """<p>Updates an existing Express service configuration. Modifies container settings, resource allocation, auto-scaling configuration, and other service parameters without recreating the service.</p> <p>Amazon ECS creates a new service revision with updated configuration and performs a rolling deployment to replace existing tasks. The service remains available during updates, ensuring zero-downtime deployments.</p> <p>Some parameters like the infrastructure role cannot be modified after service creation and require creating a new service.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to update.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role for the Express service.</p>
            health_check_path: <p>The path on the container for Application Load Balancer health checks.</p>
            primary_container: <p>The primary container configuration for the Express service.</p>
            task_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role for containers in this task.</p>
            network_configuration: <p>The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.</p>
            cpu: <p>The number of CPU units used by the task.</p>
            memory: <p>The amount of memory (in MiB) used by the task.</p>
            cpu_architecture: <p>The CPU architecture that the tasks in the Express service run on. Amazon ECS applies this value to the task definition revision that it registers for the service. If you don't specify a value, the service keeps the architecture that it currently runs on.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Changing the architecture starts a new deployment that replaces the running tasks. Make sure that the container image that the service uses supports the architecture that you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> when you also specify <code>taskDefinitionArn</code>, because this value applies only to a task definition that Amazon ECS registers on your behalf.</p>
            scaling_target: <p>The auto-scaling configuration for the Express service.</p>
            task_definition_arn: <p>The Amazon Resource Name (ARN) of a task definition to use to update the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_express_gateway_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_express_gateway_service.update_express_gateway_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if primary_container is not None:
            input_["primary_container"] = primary_container
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if cpu_architecture is not None:
            input_["cpu_architecture"] = cpu_architecture
        if scaling_target is not None:
            input_["scaling_target"] = scaling_target
        if task_definition_arn is not None:
            input_["task_definition_arn"] = task_definition_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        desired_count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        task_definition: Optional["capo_ecs.types.string.String"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        availability_zone_rebalancing: Optional[
            "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
        ] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        force_new_deployment: Optional["capo_ecs.types.boolean.Boolean"] = None,
        health_check_grace_period_seconds: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
        deployment_controller: Optional[
            "capo_ecs.types.deployment_controller.DeploymentController"
        ] = None,
        enable_execute_command: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        enable_ecs_managed_tags: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        service_connect_configuration: Optional[
            "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
        ] = None,
        volume_configurations: Optional[
            "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
        ] = None,
        vpc_lattice_configurations: Optional[
            "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
        ] = None,
        monitoring: Optional[
            "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
    ) -> "capo_ecs.types.update_service_response.UpdateServiceResponse":
        """<p>Modifies the parameters of a service.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <p>For services using the rolling update (<code>ECS</code>) you can update the desired count, deployment configuration, network configuration, load balancers, service registries, enable ECS managed tags option, propagate tags option, task placement constraints and strategies, and task definition. When you update any of these parameters, Amazon ECS starts new tasks with the new configuration. </p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. You can update your volume configurations and trigger a new deployment. <code>volumeConfigurations</code> is only supported for REPLICA service and not DAEMON service. If you leave <code>volumeConfigurations</code> <code>null</code>, it doesn't trigger a new deployment. For more information on volumes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For services using the blue/green (<code>CODE_DEPLOY</code>) deployment controller, only the desired count, deployment configuration, health check grace period, task placement constraints and strategies, enable ECS managed tags option, and propagate tags can be updated using this API. If the network configuration, platform version, task definition, or load balancer need to be updated, create a new CodeDeploy deployment. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> in the <i>CodeDeploy API Reference</i>.</p> <p>For services using an external deployment controller, you can update only the desired count, task placement constraints and strategies, health check grace period, enable ECS managed tags option, and propagate tags option, using this API. If the launch type, load balancer, network configuration, platform version, or task definition need to be updated, create a new task set For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>.</p> <p>You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new <code>desiredCount</code> parameter.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If you have updated the container image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.</p> <note> <p>If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, <code>my_image:latest</code>), you don't need to create a new revision of your task definition. You can update the service using the <code>forceNewDeployment</code> option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.</p> </note> <p>You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, <code>minimumHealthyPercent</code> and <code>maximumPercent</code>, to determine the deployment strategy.</p> <ul> <li> <p>If <code>minimumHealthyPercent</code> is below 100%, the scheduler can ignore <code>desiredCount</code> temporarily during a deployment. For example, if <code>desiredCount</code> is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that don't use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> </li> <li> <p>The <code>maximumPercent</code> parameter represents an upper limit on the number of running tasks during a deployment. You can use it to define the deployment batch size. For example, if <code>desiredCount</code> is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).</p> </li> </ul> <p>When <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> stops a task during a deployment, the equivalent of <code>docker stop</code> is issued to the containers running in the task. This results in a <code>SIGTERM</code> and a 30-second timeout. After this, <code>SIGKILL</code> is sent and the containers are forcibly stopped. If the container handles the <code>SIGTERM</code> gracefully and exits within 30 seconds from receiving it, no <code>SIGKILL</code> is sent.</p> <p>When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic.</p> <ul> <li> <p>Determine which of the container instances in your cluster can support your service's task definition. For example, they have the required CPU, memory, ports, and container instance attributes.</p> </li> <li> <p>By default, the service scheduler attempts to balance tasks across Availability Zones in this manner even though you can choose a different placement strategy.</p> <ul> <li> <p>Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.</p> </li> <li> <p>Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.</p> </li> </ul> </li> </ul> <p>When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic: </p> <ul> <li> <p>Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.</p> </li> <li> <p>Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service.</p> </li> </ul>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that your service runs on. If you do not specify a cluster, the default cluster is assumed.</p> <p>You can't change the cluster name.</p>
            service: <p>The name of the service to update.</p>
            desired_count: <p>The number of instantiations of the task to place and keep running in your service.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> is not specified, the latest <code>ACTIVE</code> revision is used. If you modify the task definition with <code>UpdateService</code>, Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.</p> <p>This parameter triggers a new service deployment.</p>
            capacity_provider_strategy: <p>The details of a capacity provider strategy. You can set a capacity provider when you create a cluster, run a task, or update a service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter.</p> </note> <p>When you use Fargate, the capacity providers are <code>FARGATE</code> or <code>FARGATE_SPOT</code>.</p> <p>When you use Amazon EC2, the capacity providers are Auto Scaling groups.</p> <p>You can change capacity providers for rolling deployments and blue/green deployments.</p> <p>The following list provides the valid transitions:</p> <ul> <li> <p>Update the Fargate launch type to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 launch type to a Fargate capacity provider.</p> </li> <li> <p>Update the Fargate capacity provider to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 capacity provider to a Fargate capacity provider. </p> </li> <li> <p>Update the Auto Scaling group or Fargate capacity provider back to the launch type.</p> <p>Pass an empty list in the <code>capacityProviderStrategy</code> parameter.</p> </li> </ul> <p>For information about Amazon Web Services CDK considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html">Amazon Web Services CDK considerations</a>.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            deployment_configuration: <p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            availability_zone_rebalancing: <p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul> <p>This parameter doesn't trigger a new service deployment.</p>
            network_configuration: <p>An object representing the network configuration for the service.</p> <p>This parameter triggers a new service deployment.</p>
            placement_constraints: <p>An array of task placement constraint objects to update the service to use. If no value is specified, the existing placement constraints for the service will remain unchanged. If this value is specified, it will override any existing placement constraints defined for the service. To remove all existing placement constraints, specify an empty array.</p> <p>You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            placement_strategy: <p>The task placement strategy objects to update the service to use. If no value is specified, the existing placement strategy for the service will remain unchanged. If this value is specified, it will override the existing placement strategy defined for the service. To remove an existing placement strategy, specify an empty object.</p> <p>You can specify a maximum of five strategy rules for each service.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            platform_version: <p>The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If a platform version is not specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>
            force_new_deployment: <p>Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (<code>my_image:latest</code>) or to roll Fargate tasks onto a newer platform version.</p>
            health_check_grace_period_seconds: <p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you don't specify a health check grace period value, the default value of <code>0</code> is used. If you don't use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service's tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            enable_execute_command: <p>If <code>true</code>, this enables execute command functionality on all task containers.</p> <p>If you do not want to override the value that was set when the service was created, you can set this to <code>null</code> when performing this action.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            enable_ecs_managed_tags: <p>Determines whether to turn on Amazon ECS managed tags for the tasks in the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            load_balancers: <note> <p>You must have a service-linked role when you update this property</p> </note> <p>A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.</p> <p>When you add, update, or remove a load balancer configuration, Amazon ECS starts new tasks with the updated Elastic Load Balancing configuration, and then stops the old tasks when the new tasks are running.</p> <p>For services that use rolling updates, you can add, update, or remove Elastic Load Balancing target groups. You can update from a single target group to multiple target groups and from multiple target groups to a single target group.</p> <p>For services that use blue/green deployments, you can update Elastic Load Balancing target groups by using <code> <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> </code> through CodeDeploy. Note that multiple target groups are not supported for blue/green deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>For services that use the external deployment controller, you can add, update, or remove load balancers by using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. Note that multiple target groups are not supported for external deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>You can remove existing <code>loadBalancers</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>
            propagate_tags: <p>Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            service_registries: <note> <p>You must have a service-linked role when you update this property.</p> <p>For more information about the role see the <code>CreateService</code> request parameter <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html#ECS-CreateService-request-role"> <code>role</code> </a>. </p> </note> <p>The details for the service discovery registries to assign to this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service Discovery</a>.</p> <p>When you add, update, or remove the service registries configuration, Amazon ECS starts new tasks with the updated service registries configuration, and then stops the old tasks when the new tasks are running.</p> <p>You can remove existing <code>serviceRegistries</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>
            service_connect_configuration: <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html">ServiceManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition. If set to null, no new deployment is triggered. Otherwise, if this configuration differs from the existing one, it triggers a new deployment.</p> <p>This parameter triggers a new service deployment.</p>
            vpc_lattice_configurations: <p>An object representing the VPC Lattice configuration for the service being updated.</p> <p>This parameter triggers a new service deployment.</p>
            monitoring: <p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To change the task definition used in a service
            This example updates the my-http-service service to use the amazon-ecs-sample task definition.

            >>> client.update_service(service='my-http-service', task_definition='amazon-ecs-sample')
            To change the number of tasks in a service
            This example updates the desired count of the my-http-service service to 10.

            >>> client.update_service(service='my-http-service', desired_count=10)
            To update a service to add a pause lifecycle hook
            This example updates the my-blue-green-service service to add a pause lifecycle hook at the POST_PRODUCTION_TRAFFIC_SHIFT stage. The deployment will pause at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 30-minute timeout expires and triggers a continue.

            >>> client.update_service(service='my-blue-green-service', deployment_configuration={'strategy': 'BLUE_GREEN', 'lifecycleHooks': [{'targetType': 'PAUSE', 'lifecycleStages': ['POST_PRODUCTION_TRAFFIC_SHIFT'], 'timeoutConfiguration': {'timeoutInMinutes': 30, 'action': 'CONTINUE'}}]})
            To update a service with a monitoring configuration
            This example updates a service to add a monitoring configuration that sets 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics. The monitoring configuration is not returned in the UpdateService response. Use DescribeServiceRevisions to view the monitoring configuration.

            >>> client.update_service(service='ecs-monitored-service', monitoring={'metricConfigurations': [{'metricNames': ['CPUUtilization', 'MemoryUtilization'], 'resolutionSeconds': 20}]})
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_service_request.UpdateServiceRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if desired_count is not None:
            input_["desired_count"] = desired_count
        if task_definition is not None:
            input_["task_definition"] = task_definition
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if availability_zone_rebalancing is not None:
            input_["availability_zone_rebalancing"] = availability_zone_rebalancing
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if force_new_deployment is not None:
            input_["force_new_deployment"] = force_new_deployment
        if health_check_grace_period_seconds is not None:
            input_["health_check_grace_period_seconds"] = (
                health_check_grace_period_seconds
            )
        if deployment_controller is not None:
            input_["deployment_controller"] = deployment_controller
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if service_connect_configuration is not None:
            input_["service_connect_configuration"] = service_connect_configuration
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations
        if vpc_lattice_configurations is not None:
            input_["vpc_lattice_configurations"] = vpc_lattice_configurations
        if monitoring is not None:
            input_["monitoring"] = monitoring

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def update_service_primary_task_set(
        self,
        cluster: "capo_ecs.types.string.String",
        service: "capo_ecs.types.string.String",
        primary_task_set: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.update_service_primary_task_set_response.UpdateServicePrimaryTaskSetResponse":
        """<p>Modifies which task set in a service is the primary task set. Any parameters that are updated on the primary task set in a service will transition to the service. This is used when a service uses the <code>EXTERNAL</code> deployment controller type. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS Deployment Types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.</p>
            service: <p>The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.</p>
            primary_task_set: <p>The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.task_set_not_found_exception.TaskSetNotFoundException: <p>The specified task set wasn't found. You can view your available task sets with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTaskSets.html">DescribeTaskSets</a>. Task sets are specific to each cluster, service and Region.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update the primary task set for a service
            This example updates the primary task set for a service MyService that uses the EXTERNAL deployment controller type.

            >>> await client.update_service_primary_task_set(cluster='MyCluster', service='MyService', primary_task_set='arn:aws:ecs:us-west-2:123456789012:task-set/MyCluster/MyService/ecs-svc/1234567890123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_service_primary_task_set_request.UpdateServicePrimaryTaskSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_service_primary_task_set_response.UpdateServicePrimaryTaskSetResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service_primary_task_set

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service_primary_task_set.async_update_service_primary_task_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_service_primary_task_set_request.UpdateServicePrimaryTaskSetRequest = {
            "cluster": cluster,
            "service": service,
            "primary_task_set": primary_task_set,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_express_gateway_service(
        self,
        infrastructure_role_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        service_name: Optional["capo_ecs.types.string.String"] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        health_check_path: Optional["capo_ecs.types.string.String"] = None,
        primary_container: Optional[
            "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
        ] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        cpu_architecture: Optional[
            "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
        ] = None,
        scaling_target: Optional[
            "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        task_definition_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.create_express_gateway_service_response.CreateExpressGatewayServiceResponse":
        """<p>Creates an Express service that simplifies deploying containerized web applications on Amazon ECS with managed Amazon Web Services infrastructure. This operation provisions and configures Application Load Balancers, target groups, security groups, and auto-scaling policies automatically.</p> <p>Specify a primary container configuration with your application image and basic settings. Amazon ECS creates the necessary Amazon Web Services resources for traffic distribution, health monitoring, network access control, and capacity management.</p> <p>Provide an execution role for task operations and an infrastructure role for managing Amazon Web Services resources on your behalf.</p>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. This role is required for Amazon ECS to pull container images from Amazon ECR, send container logs to Amazon CloudWatch Logs, and retrieve sensitive data from Amazon Web Services Systems Manager Parameter Store or Amazon Web Services Secrets Manager.</p> <p>The execution role must include the <code>AmazonECSTaskExecutionRolePolicy</code> managed policy or equivalent permissions. For Express services, this role is used during task startup and runtime for container management operations.</p>
            infrastructure_role_arn: <p>The Amazon Resource Name (ARN) of the infrastructure role that grants Amazon ECS permission to create and manage Amazon Web Services resources on your behalf for the Express service. This role is used to provision and manage Application Load Balancers, target groups, security groups, auto-scaling policies, and other Amazon Web Services infrastructure components.</p> <p>The infrastructure role must include permissions for Elastic Load Balancing, Application Auto Scaling, Amazon EC2 (for security groups), and other services required for managed infrastructure. This role is only used during Express service creation, updates, and deletion operations.</p>
            service_name: <p>The name of the Express service. This name must be unique within the specified cluster and can contain up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens. The name is used to identify the service in the Amazon ECS console and API operations.</p> <p>If you don't specify a service name, Amazon ECS generates a unique name for the service. The service name becomes part of the service ARN and cannot be changed after the service is created.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster on which to create the Express service. If you do not specify a cluster, the <code>default</code> cluster is assumed.</p>
            health_check_path: <p>The path on the container that the Application Load Balancer uses for health checks. This should be a valid HTTP endpoint that returns a successful response (HTTP 200) when the application is healthy.</p> <p>If not specified, the default health check path is <code>/ping</code>. The health check path must start with a forward slash and can include query parameters. Examples: <code>/health</code>, <code>/api/status</code>, <code>/ping?format=json</code>.</p>
            primary_container: <p>The primary container configuration for the Express service. This defines the main application container that will receive traffic from the Application Load Balancer.</p> <p>The primary container must specify at minimum a container image. You can also configure the container port (defaults to 80), logging configuration, environment variables, secrets, and startup commands. The container image can be from Amazon ECR, Docker Hub, or any other container registry accessible to your execution role.</p>
            task_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. This role allows your application code to access other Amazon Web Services services securely.</p> <p>The task role is different from the execution role. While the execution role is used by the Amazon ECS agent to set up the task, the task role is used by your application code running inside the container to make Amazon Web Services API calls. If your application doesn't need to access Amazon Web Services services, you can omit this parameter.</p>
            network_configuration: <p>The network configuration for the Express service tasks. This specifies the VPC subnets and security groups for the tasks.</p> <p>For Express services, you can specify custom security groups and subnets. If not provided, Amazon ECS will use the default VPC configuration and create appropriate security groups automatically. The network configuration determines how your service integrates with your VPC and what network access it has.</p>
            cpu: <p>The number of CPU units used by the task. This parameter determines the CPU allocation for each task in the Express service. The default value for an Express service is 256 (.25 vCPU).</p>
            memory: <p>The amount of memory (in MiB) used by the task. This parameter determines the memory allocation for each task in the Express service. The default value for an express service is 512 MiB.</p>
            cpu_architecture: <p>The CPU architecture that the tasks in the Express service run on. Amazon ECS applies this value to the task definition revision that it registers for the service. If you don't specify a value, the default is <code>X86_64</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Make sure that the container image that you specify supports the architecture that you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> when you also specify <code>taskDefinitionArn</code>, because this value applies only to a task definition that Amazon ECS registers on your behalf.</p>
            scaling_target: <p>The auto-scaling configuration for the Express service. This defines how the service automatically adjusts the number of running tasks based on demand.</p> <p>You can specify the minimum and maximum number of tasks, the scaling metric (CPU utilization, memory utilization, or request count per target), and the target value for the metric. If not specified, the default target value for an Express service is 60.</p>
            tags: <p>The metadata that you apply to the Express service to help categorize and organize it. Each tag consists of a key and an optional value. You can apply up to 50 tags to a service.</p>
            task_definition_arn: <p>The Amazon Resource Name (ARN) of a task definition to use to create the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_express_gateway_service_request.CreateExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_express_gateway_service_response.CreateExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_express_gateway_service.async_create_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_express_gateway_service_request.CreateExpressGatewayServiceRequest = {
            "infrastructure_role_arn": infrastructure_role_arn
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if service_name is not None:
            input_["service_name"] = service_name
        if cluster is not None:
            input_["cluster"] = cluster
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if primary_container is not None:
            input_["primary_container"] = primary_container
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if cpu_architecture is not None:
            input_["cpu_architecture"] = cpu_architecture
        if scaling_target is not None:
            input_["scaling_target"] = scaling_target
        if tags is not None:
            input_["tags"] = tags
        if task_definition_arn is not None:
            input_["task_definition_arn"] = task_definition_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service(
        self,
        service_name: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        task_definition: Optional["capo_ecs.types.string.String"] = None,
        availability_zone_rebalancing: Optional[
            "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        desired_count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        role: Optional["capo_ecs.types.string.String"] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        health_check_grace_period_seconds: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        deployment_controller: Optional[
            "capo_ecs.types.deployment_controller.DeploymentController"
        ] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        service_connect_configuration: Optional[
            "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
        ] = None,
        volume_configurations: Optional[
            "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
        ] = None,
        vpc_lattice_configurations: Optional[
            "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
        ] = None,
        monitoring: Optional[
            "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
    ) -> "capo_ecs.types.create_service_response.CreateServiceResponse":
        """<p>Runs and maintains your desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the <code>desiredCount</code>, Amazon ECS runs another copy of the task in the specified cluster. To update an existing service, use <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind one or more load balancers. The load balancers distribute traffic across the tasks that are associated with the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. <code>volumeConfigurations</code> is only supported for REPLICA service and not DAEMON service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Tasks for services that don't use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code> - The replica scheduling strategy places and maintains your desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Service scheduler concepts</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> <li> <p> <code>DAEMON</code> - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It also stops tasks that don't meet the placement constraints. When using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Amazon ECS services</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </li> </ul> <p>The deployment controller is the mechanism that determines how tasks are deployed for your service. The valid options are:</p> <ul> <li> <p>ECS</p> <p> When you create a service which uses the <code>ECS</code> deployment controller, you can choose between the following deployment strategies (which you can set in the “<code>strategy</code>” field in “<code>deploymentConfiguration</code>”): :</p> <ul> <li> <p> <code>ROLLING</code>: When you create a service which uses the <i>rolling update</i> (<code>ROLLING</code>) deployment strategy, the Amazon ECS service scheduler replaces the currently running tasks with new tasks. The number of tasks that Amazon ECS adds or removes from the service during a rolling update is controlled by the service deployment configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html">Deploy Amazon ECS services by replacing tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Rolling update deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual service updates: You need to update your service incrementally without taking the entire service offline at once.</p> </li> <li> <p>Limited resource requirements: You want to avoid the additional resource costs of running two complete environments simultaneously (as required by blue/green deployments).</p> </li> <li> <p>Acceptable deployment time: Your application can tolerate a longer deployment process, as rolling updates replace tasks one by one.</p> </li> <li> <p>No need for instant roll back: Your service can tolerate a rollback process that takes minutes rather than seconds.</p> </li> <li> <p>Simple deployment process: You prefer a straightforward deployment approach without the complexity of managing multiple environments, target groups, and listeners.</p> </li> <li> <p>No load balancer requirement: Your service doesn't use or require a load balancer, Application Load Balancer, Network Load Balancer, or Service Connect (which are required for blue/green deployments).</p> </li> <li> <p>Stateful applications: Your application maintains state that makes it difficult to run two parallel environments.</p> </li> <li> <p>Cost sensitivity: You want to minimize deployment costs by not running duplicate environments during deployment.</p> </li> </ul> <p>Rolling updates are the default deployment strategy for services and provide a balance between deployment safety and resource efficiency for many common application scenarios.</p> </li> <li> <p> <code>BLUE_GREEN</code>: A <i>blue/green</i> deployment strategy (<code>BLUE_GREEN</code>) is a release methodology that reduces downtime and risk by running two identical production environments called blue and green. With Amazon ECS blue/green deployments, you can validate new service revisions before directing production traffic to them. This approach provides a safer way to deploy changes with the ability to quickly roll back if needed. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html">Amazon ECS blue/green deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Amazon ECS blue/green deployments are best suited for the following scenarios:</p> <ul> <li> <p>Service validation: When you need to validate new service revisions before directing production traffic to them</p> </li> <li> <p>Zero downtime: When your service requires zero-downtime deployments</p> </li> <li> <p>Instant roll back: When you need the ability to quickly roll back if issues are detected</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer, Network Load Balancer, or Service Connect</p> </li> </ul> </li> <li> <p> <code>LINEAR</code>: A <i>linear</i> deployment strategy (<code>LINEAR</code>) gradually shifts traffic from the current production environment to a new environment in equal percentage increments. With Amazon ECS linear deployments, you can control the pace of traffic shifting and validate new service revisions with increasing amounts of production traffic.</p> <p>Linear deployments are best suited for the following scenarios:</p> <ul> <li> <p>Gradual validation: When you want to gradually validate your new service version with increasing traffic</p> </li> <li> <p>Performance monitoring: When you need time to monitor metrics and performance during the deployment</p> </li> <li> <p>Risk minimization: When you want to minimize risk by exposing the new version to production traffic incrementally</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer or Service Connect</p> </li> </ul> </li> <li> <p> <code>CANARY</code>: A <i>canary</i> deployment strategy (<code>CANARY</code>) shifts a small percentage of traffic to the new service revision first, then shifts the remaining traffic all at once after a specified time period. This allows you to test the new version with a subset of users before full deployment.</p> <p>Canary deployments are best suited for the following scenarios:</p> <ul> <li> <p>Feature testing: When you want to test new features with a small subset of users before full rollout</p> </li> <li> <p>Production validation: When you need to validate performance and functionality with real production traffic</p> </li> <li> <p>Blast radius control: When you want to minimize blast radius if issues are discovered in the new version</p> </li> <li> <p>Load balancer requirement: When your service uses Application Load Balancer or Service Connect</p> </li> </ul> </li> </ul> </li> <li> <p>External</p> <p>Use a third-party deployment controller.</p> </li> <li> <p>Blue/green deployment (powered by CodeDeploy)</p> <p>CodeDeploy installs an updated version of the application as a new replacement task set and reroutes production traffic from the original application task set to the replacement task set. The original task set is terminated after a successful deployment. Use this deployment controller to verify a new deployment of a service before sending production traffic to it.</p> </li> </ul> <p>When creating a service that uses the <code>EXTERNAL</code> deployment controller, you can specify only parameters that aren't controlled at the task set level. The only required parameter is the service name. You control your services using the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When the service scheduler launches new tasks, it determines task placement. For information about task placement and task placement strategies, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html">Amazon ECS task placement</a> in the <i>Amazon Elastic Container Service Developer Guide</i> </p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</p>
            service_name: <p>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.</p>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>A task definition must be specified if the service uses either the <code>ECS</code> or <code>CODE_DEPLOY</code> deployment controllers.</p> <p>For more information about deployment types, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">Amazon ECS deployment types</a>.</p>
            availability_zone_rebalancing: <p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul>
            load_balancers: <p>A load balancer object representing the load balancers to use with your service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html">Service load balancing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>ECS</code> deployment controller and using either an Application Load Balancer or Network Load Balancer, you must specify one or more target group ARNs to attach to the service. The service-linked role is required for services that use multiple target groups. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the service uses the <code>CODE_DEPLOY</code> deployment controller, the service is required to use either an Application Load Balancer or Network Load Balancer. When creating an CodeDeploy deployment group, you specify two target groups (referred to as a <code>targetGroupPair</code>). During a deployment, CodeDeploy determines which task set in your service has the status <code>PRIMARY</code>, and it associates one target group with it. Then, it also associates the other target group with the replacement task set. The load balancer can also have up to two listeners: a required listener for production traffic and an optional listener that you can use to perform validation tests with Lambda functions before routing production traffic to it.</p> <p>If you use the <code>CODE_DEPLOY</code> deployment controller, these values can be changed when updating the service.</p> <p>For Application Load Balancers and Network Load Balancers, this object must contain the load balancer target group ARN, the container name, and the container port to access from the load balancer. The container name must be as it appears in a container definition. The load balancer name parameter must be omitted. When a task from this service is placed on a container instance, the container instance and port combination is registered as a target in the target group that's specified here.</p> <p>For Classic Load Balancers, this object must contain the load balancer name, the container name , and the container port to access from the load balancer. The container name must be as it appears in a container definition. The target group ARN parameter must be omitted. When a task from this service is placed on a container instance, the container instance is registered with the load balancer that's specified here.</p> <p>Services with tasks that use the <code>awsvpc</code> network mode (for example, those with the Fargate launch type) only support Application Load Balancers and Network Load Balancers. Classic Load Balancers aren't supported. Also, when you create any target groups for these services, you must choose <code>ip</code> as the target type, not <code>instance</code>. This is because tasks that use the <code>awsvpc</code> network mode are associated with an elastic network interface, not an Amazon EC2 instance.</p>
            service_registries: <p>The details of the service discovery registry to associate with this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service discovery</a>.</p> <note> <p>Each service may be associated with one service registry. Multiple service registries for each service isn't supported.</p> </note>
            desired_count: <p>The number of instantiations of the specified task definition to place and keep running in your service.</p> <p>This is required if <code>schedulingStrategy</code> is <code>REPLICA</code> or isn't specified. If <code>schedulingStrategy</code> is <code>DAEMON</code> then this isn't required.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 36 ASCII characters in the range of 33-126 (inclusive) are allowed.</p>
            launch_type: <p>The infrastructure that you run your service on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A service can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p>
            capacity_provider_strategy: <p>The capacity provider strategy to use for the service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>
            platform_version: <p>The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            role: <p>The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the <code>awsvpc</code> network mode. If you specify the <code>role</code> parameter, you must also specify a load balancer object with the <code>loadBalancers</code> parameter.</p> <important> <p>If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the <code>awsvpc</code> network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html">Using service-linked roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </important> <p>If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code> then you would specify <code>/foo/bar</code> as the role name. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names">Friendly names and paths</a> in the <i>IAM User Guide</i>.</p>
            deployment_configuration: <p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p>
            placement_constraints: <p>An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>
            placement_strategy: <p>The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.</p>
            network_configuration: <p>The network configuration for the service. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            health_check_grace_period_seconds: <p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used. If you do not use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p>
            scheduling_strategy: <p>The scheduling strategy to use for the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">Services</a>.</p> <p>There are two service scheduler strategies available:</p> <ul> <li> <p> <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types.</p> </li> <li> <p> <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.</p> <note> <p>Tasks using the Fargate launch type or the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types don't support the <code>DAEMON</code> scheduling strategy.</p> </note> </li> </ul>
            deployment_controller: <p>The deployment controller to use for the service. If no deployment controller is specified, the default value of <code>ECS</code> is used.</p>
            tags: <p>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            enable_ecs_managed_tags: <p>Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging your Amazon ECS resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>When you use Amazon ECS managed tags, you must set the <code>propagateTags</code> request parameter.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <p>You must set this to a value other than <code>NONE</code> when you use Cost Explorer. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html">Amazon ECS usage reports</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The default is <code>NONE</code>.</p>
            enable_execute_command: <p>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, this enables execute command functionality on all containers in the service tasks.</p>
            service_connect_configuration: <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            volume_configurations: <p>The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.</p>
            vpc_lattice_configurations: <p>The VPC Lattice configuration for the service being created.</p>
            monitoring: <p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new service
            This example creates a service in your default region called ``ecs-simple-service``. The service uses the ``hello_world`` task definition and it maintains 10 copies of that task.

            >>> await client.create_service(service_name='ecs-simple-service', task_definition='hello_world', desired_count=10)
            To create a new service behind a load balancer
            This example creates a service in your default region called ``ecs-simple-service-elb``. The service uses the ``ecs-demo`` task definition and it maintains 10 copies of that task. You must reference an existing load balancer in the same region by its name.

            >>> await client.create_service(load_balancers=[{'containerName': 'simple-app', 'containerPort': 80, 'loadBalancerName': 'EC2Contai-EcsElast-15DCDAURT3ZO2'}], service_name='ecs-simple-service-elb', role='ecsServiceRole', task_definition='console-sample-app-static', desired_count=10)
            To create a service with a pause lifecycle hook
            This example creates a service with a blue/green deployment strategy that includes a pause lifecycle hook at the POST_PRODUCTION_TRAFFIC_SHIFT stage. The deployment will pause at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 60-minute timeout expires and triggers a rollback.

            >>> await client.create_service(service_name='ecs-service-with-pause-hook', task_definition='ecs-demo', desired_count=2, deployment_configuration={'strategy': 'BLUE_GREEN', 'lifecycleHooks': [{'targetType': 'PAUSE', 'lifecycleStages': ['POST_PRODUCTION_TRAFFIC_SHIFT'], 'timeoutConfiguration': {'timeoutInMinutes': 60, 'action': 'ROLLBACK'}}]})
            To create a service with a monitoring configuration
            This example creates a service with a monitoring configuration that sets 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics. The monitoring configuration is not returned in the CreateService response. Use DescribeServiceRevisions to view the monitoring configuration.

            >>> await client.create_service(service_name='ecs-monitored-service', task_definition='my-app:1', desired_count=2, monitoring={'metricConfigurations': [{'metricNames': ['CPUUtilization', 'MemoryUtilization'], 'resolutionSeconds': 20}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.create_service_request.CreateServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.create_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.create_service.async_create_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.create_service_request.CreateServiceRequest = {
            "service_name": service_name
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if task_definition is not None:
            input_["task_definition"] = task_definition
        if availability_zone_rebalancing is not None:
            input_["availability_zone_rebalancing"] = availability_zone_rebalancing
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if desired_count is not None:
            input_["desired_count"] = desired_count
        if client_token is not None:
            input_["client_token"] = client_token
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if role is not None:
            input_["role"] = role
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if health_check_grace_period_seconds is not None:
            input_["health_check_grace_period_seconds"] = (
                health_check_grace_period_seconds
            )
        if scheduling_strategy is not None:
            input_["scheduling_strategy"] = scheduling_strategy
        if deployment_controller is not None:
            input_["deployment_controller"] = deployment_controller
        if tags is not None:
            input_["tags"] = tags
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if service_connect_configuration is not None:
            input_["service_connect_configuration"] = service_connect_configuration
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations
        if vpc_lattice_configurations is not None:
            input_["vpc_lattice_configurations"] = vpc_lattice_configurations
        if monitoring is not None:
            input_["monitoring"] = monitoring

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse":
        """<p>Deletes an Express service and removes all associated Amazon Web Services resources. This operation stops service tasks, removes the Application Load Balancer, target groups, security groups, auto-scaling policies, and other managed infrastructure components.</p> <p>The service enters a <code>DRAINING</code> state where existing tasks complete current requests without starting new tasks. After all tasks stop, the service and infrastructure are permanently removed.</p> <p>This operation cannot be reversed. Back up important data and verify the service is no longer needed before deletion.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to delete. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_express_gateway_service_response.DeleteExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_express_gateway_service.async_delete_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_express_gateway_service_request.DeleteExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        force: Optional["capo_ecs.types.boxed_boolean.BoxedBoolean"] = None,
    ) -> "capo_ecs.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you can't delete it, and you must update the service to a desired task count of zero. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a>.</p> <note> <p>When you delete a service, if there are still running tasks that require cleanup, the service status moves from <code>ACTIVE</code> to <code>DRAINING</code>, and the service is no longer visible in the console or in the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a> API operation. After all tasks have transitioned to either <code>STOPPING</code> or <code>STOPPED</code> status, the service status moves from <code>DRAINING</code> to <code>INACTIVE</code>. Services in the <code>DRAINING</code> or <code>INACTIVE</code> status can still be viewed with the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html">DescribeServices</a> API operation. However, in the future, <code>INACTIVE</code> services may be cleaned up and purged from Amazon ECS record keeping, and <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServices.html">DescribeServices</a> calls on those services return a <code>ServiceNotFoundException</code> error.</p> </note> <important> <p>If you attempt to create a new service with the same name as an existing service in either <code>ACTIVE</code> or <code>DRAINING</code> status, you receive an error.</p> </important>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to delete. If you do not specify a cluster, the default cluster is assumed.</p>
            service: <p>The name of the service to delete.</p>
            force: <p>If <code>true</code>, allows you to delete a service even if it wasn't scaled down to zero tasks. It's only necessary to use this if the service uses the <code>REPLICA</code> scheduling strategy.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a service
            This example deletes the my-http-service service. The service must have a desired count and running count of 0 before you can delete it.

            >>> await client.delete_service(service='my-http-service')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_service_request.DeleteServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_service.async_delete_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_service_request.DeleteServiceRequest = {
            "service": service
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

    async def describe_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        include: Optional[
            "capo_ecs.types.express_gateway_service_include_list.ExpressGatewayServiceIncludeList"
        ] = None,
    ) -> "capo_ecs.types.describe_express_gateway_service_response.DescribeExpressGatewayServiceResponse":
        """<p>Retrieves detailed information about an Express service, including current status, configuration, managed infrastructure, and service revisions.</p> <p>Returns comprehensive service details, active service revisions, ingress paths with endpoints, and managed Amazon Web Services resource status including load balancers and auto-scaling policies.</p> <p>Use the <code>include</code> parameter to retrieve additional information such as resource tags.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to describe. The ARN uniquely identifies the service within your Amazon Web Services account and region.</p>
            include: <p>Specifies additional information to include in the response. Valid values are <code>TAGS</code> to include resource tags associated with the Express service.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_express_gateway_service_request.DescribeExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_express_gateway_service_response.DescribeExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_express_gateway_service.async_describe_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_express_gateway_service_request.DescribeExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_services(
        self,
        services: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional["capo_ecs.types.service_field_list.ServiceFieldList"] = None,
    ) -> "capo_ecs.types.describe_services_response.DescribeServicesResponse":
        """<p>Describes the specified services running in your cluster.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN)the cluster that hosts the service to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the service or services you are describing were launched in any cluster other than the default cluster.</p>
            services: <p>A list of services to describe. You may specify up to 10 services to describe in a single operation.</p>
            include: <p>Determines whether you want to see the resource tags for the service. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a service
            This example provides descriptive information about the service named ``ecs-simple-service``.

            >>> await client.describe_services(services=['ecs-simple-service'])
            To describe a service with a pause lifecycle hook
            This example provides descriptive information about the service ``ecs-service-with-pause-hook``, which is configured with a pause lifecycle hook in its deployment configuration.

            >>> await client.describe_services(services=['ecs-service-with-pause-hook'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_services_request.DescribeServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_services_response.DescribeServicesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_services

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_services.async_describe_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_services_request.DescribeServicesRequest = {
            "services": services
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if include is not None:
            input_["include"] = include

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_service_deployments(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.service_deployment_status_list.ServiceDeploymentStatusList"
        ] = None,
        created_at: Optional["capo_ecs.types.created_at.CreatedAt"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_service_deployments_response.ListServiceDeploymentsResponse":
        """<p>This operation lists all the service deployments that meet the specified filter criteria.</p> <p>A service deployment happens when you release a software update for the service. You route traffic from the running service revisions to the new service revison and control the number of running tasks. </p> <p>This API returns the values that you use for the request parameters in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceRevisions.html">DescribeServiceRevisions</a>.</p>

        Args:
            service: <p>The ARN or name of the service</p>
            cluster: <p>The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you don't specify a cluster, <code>default</code> is used.</p>
            status: <p>An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.</p>
            created_at: <p>An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListServiceDeployments</code> request indicating that more results are available to fulfill the request and further calls are needed. If you provided <code>maxResults</code>, it's possible the number of results is fewer than <code>maxResults</code>.</p>
            max_results: <p>The maximum number of service deployment results that <code>ListServiceDeployments</code> returned in paginated output. When this parameter is used, <code>ListServiceDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>

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
            To list service deployments that meet the specified criteria
            This example lists all successful service deployments for the service "sd-example" in the cluster "example".

            >>> await client.list_service_deployments(service='sd-example', cluster='example', status=['SUCCESSFUL'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_service_deployments_request.ListServiceDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_service_deployments_response.ListServiceDeploymentsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_service_deployments

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_service_deployments.async_list_service_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_service_deployments_request.ListServiceDeploymentsRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if status is not None:
            input_["status"] = status
        if created_at is not None:
            input_["created_at"] = created_at
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

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        scheduling_strategy: Optional[
            "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
        ] = None,
        resource_management_type: Optional[
            "capo_ecs.types.resource_management_type.ResourceManagementType"
        ] = None,
    ) -> "capo_ecs.types.list_services_response.ListServicesResponse":
        """<p>Returns a list of services. You can filter the results by cluster, launch type, and scheduling strategy.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListServices</code> results. If you do not specify a cluster, the default cluster is assumed.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListServices</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of service results that <code>ListServices</code> returned in paginated output. When this parameter is used, <code>ListServices</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServices</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>
            launch_type: <p>The launch type to use when filtering the <code>ListServices</code> results.</p>
            scheduling_strategy: <p>The scheduling strategy to use when filtering the <code>ListServices</code> results.</p>
            resource_management_type: <p>The resourceManagementType type to use when filtering the <code>ListServices</code> results.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the services in a cluster
            This example lists the services running in the default cluster for an account.

            >>> await client.list_services()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_services_request.ListServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_services_response.ListServicesResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_services_request.ListServicesRequest = {}
        if cluster is not None:
            input_["cluster"] = cluster
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if scheduling_strategy is not None:
            input_["scheduling_strategy"] = scheduling_strategy
        if resource_management_type is not None:
            input_["resource_management_type"] = resource_management_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_service_deployment(
        self,
        service_deployment_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        stop_type: Optional[
            "capo_ecs.types.stop_service_deployment_stop_type.StopServiceDeploymentStopType"
        ] = None,
    ) -> (
        "capo_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse"
    ):
        """<p>Stops an ongoing service deployment.</p> <p>The following stop types are avaiable:</p> <ul> <li> <p>ROLLBACK - This option rolls back the service deployment to the previous service revision. </p> <p>You can use this option even if you didn't configure the service deployment for the rollback option. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stop-service-deployment.html">Stopping Amazon ECS service deployments</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            service_deployment_arn: <p>The ARN of the service deployment that you want to stop.</p>
            stop_type: <p>How you want Amazon ECS to stop the service. </p> <p>The valid values are <code>ROLLBACK</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. </p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_deployment_not_found_exception.ServiceDeploymentNotFoundException: <p>The service deploy ARN that you specified in the <code>ContinueServiceDeployment</code> doesn't exist. You can use <code>ListServiceDeployments</code> to retrieve the service deployment ARNs.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop a service deployment
            This example stops the service deployment using the ROLLBACK option.

            >>> await client.stop_service_deployment(service_deployment_arn='arn:aws:ecs:us-east-1:123456789012:service-deployment/MyCluster/MyService/r9i43YFjvgF_xlg7m2eJ1r', stop_type='ROLLBACK')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.stop_service_deployment_response.StopServiceDeploymentResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_service_deployment

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_service_deployment.async_stop_service_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.stop_service_deployment_request.StopServiceDeploymentRequest = {
            "service_deployment_arn": service_deployment_arn
        }
        if stop_type is not None:
            input_["stop_type"] = stop_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_express_gateway_service(
        self,
        service_arn: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        health_check_path: Optional["capo_ecs.types.string.String"] = None,
        primary_container: Optional[
            "capo_ecs.types.express_gateway_container.ExpressGatewayContainer"
        ] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.express_gateway_service_network_configuration.ExpressGatewayServiceNetworkConfiguration"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        cpu_architecture: Optional[
            "capo_ecs.types.express_cpu_architecture.ExpressCpuArchitecture"
        ] = None,
        scaling_target: Optional[
            "capo_ecs.types.express_gateway_scaling_target.ExpressGatewayScalingTarget"
        ] = None,
        task_definition_arn: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse":
        """<p>Updates an existing Express service configuration. Modifies container settings, resource allocation, auto-scaling configuration, and other service parameters without recreating the service.</p> <p>Amazon ECS creates a new service revision with updated configuration and performs a rolling deployment to replace existing tasks. The service remains available during updates, ensuring zero-downtime deployments.</p> <p>Some parameters like the infrastructure role cannot be modified after service creation and require creating a new service.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the Express service to update.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role for the Express service.</p>
            health_check_path: <p>The path on the container for Application Load Balancer health checks.</p>
            primary_container: <p>The primary container configuration for the Express service.</p>
            task_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role for containers in this task.</p>
            network_configuration: <p>The network configuration for the Express service tasks. By default, the network configuration for an Express service uses the default VPC.</p>
            cpu: <p>The number of CPU units used by the task.</p>
            memory: <p>The amount of memory (in MiB) used by the task.</p>
            cpu_architecture: <p>The CPU architecture that the tasks in the Express service run on. Amazon ECS applies this value to the task definition revision that it registers for the service. If you don't specify a value, the service keeps the architecture that it currently runs on.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul> <p>Changing the architecture starts a new deployment that replaces the running tasks. Make sure that the container image that the service uses supports the architecture that you choose. The operating system family for an Express service is always <code>LINUX</code>.</p> <p>You can't specify <code>cpuArchitecture</code> when you also specify <code>taskDefinitionArn</code>, because this value applies only to a task definition that Amazon ECS registers on your behalf.</p>
            scaling_target: <p>The auto-scaling configuration for the Express service.</p>
            task_definition_arn: <p>The Amazon Resource Name (ARN) of a task definition to use to update the Express Gateway service. This allows you to manage your own task definition, giving you more control over the service configuration such as adding sidecar containers.</p> <p>The task definition must have a container named <code>Main</code> with a single TCP port mapping that includes a container port and port name. The task definition must also have <code>FARGATE</code> compatibility.</p> <p>If you provide a task definition ARN, you cannot also specify <code>primaryContainer</code>, <code>executionRoleArn</code>, <code>taskRoleArn</code>, <code>cpu</code>, <code>memory</code>, or <code>cpuArchitecture</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_express_gateway_service_response.UpdateExpressGatewayServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_express_gateway_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_express_gateway_service.async_update_express_gateway_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_express_gateway_service_request.UpdateExpressGatewayServiceRequest = {
            "service_arn": service_arn
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if primary_container is not None:
            input_["primary_container"] = primary_container
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if cpu_architecture is not None:
            input_["cpu_architecture"] = cpu_architecture
        if scaling_target is not None:
            input_["scaling_target"] = scaling_target
        if task_definition_arn is not None:
            input_["task_definition_arn"] = task_definition_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service(
        self,
        service: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        desired_count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        task_definition: Optional["capo_ecs.types.string.String"] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        deployment_configuration: Optional[
            "capo_ecs.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        availability_zone_rebalancing: Optional[
            "capo_ecs.types.availability_zone_rebalancing.AvailabilityZoneRebalancing"
        ] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        force_new_deployment: Optional["capo_ecs.types.boolean.Boolean"] = None,
        health_check_grace_period_seconds: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
        deployment_controller: Optional[
            "capo_ecs.types.deployment_controller.DeploymentController"
        ] = None,
        enable_execute_command: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        enable_ecs_managed_tags: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
        load_balancers: Optional["capo_ecs.types.load_balancers.LoadBalancers"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        service_registries: Optional[
            "capo_ecs.types.service_registries.ServiceRegistries"
        ] = None,
        service_connect_configuration: Optional[
            "capo_ecs.types.service_connect_configuration.ServiceConnectConfiguration"
        ] = None,
        volume_configurations: Optional[
            "capo_ecs.types.service_volume_configurations.ServiceVolumeConfigurations"
        ] = None,
        vpc_lattice_configurations: Optional[
            "capo_ecs.types.vpc_lattice_configurations.VpcLatticeConfigurations"
        ] = None,
        monitoring: Optional[
            "capo_ecs.types.monitoring_configuration.MonitoringConfiguration"
        ] = None,
    ) -> "capo_ecs.types.update_service_response.UpdateServiceResponse":
        """<p>Modifies the parameters of a service.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <p>For services using the rolling update (<code>ECS</code>) you can update the desired count, deployment configuration, network configuration, load balancers, service registries, enable ECS managed tags option, propagate tags option, task placement constraints and strategies, and task definition. When you update any of these parameters, Amazon ECS starts new tasks with the new configuration. </p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. You can update your volume configurations and trigger a new deployment. <code>volumeConfigurations</code> is only supported for REPLICA service and not DAEMON service. If you leave <code>volumeConfigurations</code> <code>null</code>, it doesn't trigger a new deployment. For more information on volumes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For services using the blue/green (<code>CODE_DEPLOY</code>) deployment controller, only the desired count, deployment configuration, health check grace period, task placement constraints and strategies, enable ECS managed tags option, and propagate tags can be updated using this API. If the network configuration, platform version, task definition, or load balancer need to be updated, create a new CodeDeploy deployment. For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> in the <i>CodeDeploy API Reference</i>.</p> <p>For services using an external deployment controller, you can update only the desired count, task placement constraints and strategies, health check grace period, enable ECS managed tags option, and propagate tags option, using this API. If the launch type, load balancer, network configuration, platform version, or task definition need to be updated, create a new task set For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>.</p> <p>You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new <code>desiredCount</code> parameter.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when starting or running a task, or when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If you have updated the container image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service's deployment configuration) to determine the deployment strategy.</p> <note> <p>If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, <code>my_image:latest</code>), you don't need to create a new revision of your task definition. You can update the service using the <code>forceNewDeployment</code> option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.</p> </note> <p>You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, <code>minimumHealthyPercent</code> and <code>maximumPercent</code>, to determine the deployment strategy.</p> <ul> <li> <p>If <code>minimumHealthyPercent</code> is below 100%, the scheduler can ignore <code>desiredCount</code> temporarily during a deployment. For example, if <code>desiredCount</code> is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that don't use a load balancer are considered healthy if they're in the <code>RUNNING</code> state. Tasks for services that use a load balancer are considered healthy if they're in the <code>RUNNING</code> state and are reported as healthy by the load balancer.</p> </li> <li> <p>The <code>maximumPercent</code> parameter represents an upper limit on the number of running tasks during a deployment. You can use it to define the deployment batch size. For example, if <code>desiredCount</code> is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).</p> </li> </ul> <p>When <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html">UpdateService</a> stops a task during a deployment, the equivalent of <code>docker stop</code> is issued to the containers running in the task. This results in a <code>SIGTERM</code> and a 30-second timeout. After this, <code>SIGKILL</code> is sent and the containers are forcibly stopped. If the container handles the <code>SIGTERM</code> gracefully and exits within 30 seconds from receiving it, no <code>SIGKILL</code> is sent.</p> <p>When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic.</p> <ul> <li> <p>Determine which of the container instances in your cluster can support your service's task definition. For example, they have the required CPU, memory, ports, and container instance attributes.</p> </li> <li> <p>By default, the service scheduler attempts to balance tasks across Availability Zones in this manner even though you can choose a different placement strategy.</p> <ul> <li> <p>Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.</p> </li> <li> <p>Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.</p> </li> </ul> </li> </ul> <p>When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic: </p> <ul> <li> <p>Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.</p> </li> <li> <p>Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service.</p> </li> </ul>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that your service runs on. If you do not specify a cluster, the default cluster is assumed.</p> <p>You can't change the cluster name.</p>
            service: <p>The name of the service to update.</p>
            desired_count: <p>The number of instantiations of the task to place and keep running in your service.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> is not specified, the latest <code>ACTIVE</code> revision is used. If you modify the task definition with <code>UpdateService</code>, Amazon ECS spawns a task with the new version of the task definition and then stops an old task after the new version is running.</p> <p>This parameter triggers a new service deployment.</p>
            capacity_provider_strategy: <p>The details of a capacity provider strategy. You can set a capacity provider when you create a cluster, run a task, or update a service.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter.</p> </note> <p>When you use Fargate, the capacity providers are <code>FARGATE</code> or <code>FARGATE_SPOT</code>.</p> <p>When you use Amazon EC2, the capacity providers are Auto Scaling groups.</p> <p>You can change capacity providers for rolling deployments and blue/green deployments.</p> <p>The following list provides the valid transitions:</p> <ul> <li> <p>Update the Fargate launch type to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 launch type to a Fargate capacity provider.</p> </li> <li> <p>Update the Fargate capacity provider to an Auto Scaling group capacity provider.</p> </li> <li> <p>Update the Amazon EC2 capacity provider to a Fargate capacity provider. </p> </li> <li> <p>Update the Auto Scaling group or Fargate capacity provider back to the launch type.</p> <p>Pass an empty list in the <code>capacityProviderStrategy</code> parameter.</p> </li> </ul> <p>For information about Amazon Web Services CDK considerations, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html">Amazon Web Services CDK considerations</a>.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            deployment_configuration: <p>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            availability_zone_rebalancing: <p>Indicates whether to use Availability Zone rebalancing for the service.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html">Balancing an Amazon ECS service across Availability Zones</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <p>The default behavior of <code>AvailabilityZoneRebalancing</code> differs between create and update requests:</p> <ul> <li> <p>For create service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults the value to <code>ENABLED</code>.</p> </li> <li> <p>For update service requests, when no value is specified for <code>AvailabilityZoneRebalancing</code>, Amazon ECS defaults to the existing service’s <code>AvailabilityZoneRebalancing</code> value. If the service never had an <code>AvailabilityZoneRebalancing</code> value set, Amazon ECS treats this as <code>DISABLED</code>.</p> </li> </ul> <p>This parameter doesn't trigger a new service deployment.</p>
            network_configuration: <p>An object representing the network configuration for the service.</p> <p>This parameter triggers a new service deployment.</p>
            placement_constraints: <p>An array of task placement constraint objects to update the service to use. If no value is specified, the existing placement constraints for the service will remain unchanged. If this value is specified, it will override any existing placement constraints defined for the service. To remove all existing placement constraints, specify an empty array.</p> <p>You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            placement_strategy: <p>The task placement strategy objects to update the service to use. If no value is specified, the existing placement strategy for the service will remain unchanged. If this value is specified, it will override the existing placement strategy defined for the service. To remove an existing placement strategy, specify an empty object.</p> <p>You can specify a maximum of five strategy rules for each service.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            platform_version: <p>The platform version that your tasks in the service run on. A platform version is only specified for tasks using the Fargate launch type. If a platform version is not specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate Platform Versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>
            force_new_deployment: <p>Determines whether to force a new deployment of the service. By default, deployments aren't forced. You can use this option to start a new deployment with no service definition changes. For example, you can update a service's tasks to use a newer Docker image with the same image/tag combination (<code>my_image:latest</code>) or to roll Fargate tasks onto a newer platform version.</p>
            health_check_grace_period_seconds: <p>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you don't specify a health check grace period value, the default value of <code>0</code> is used. If you don't use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.</p> <p>If your service's tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.</p> <p>If your service has more running tasks than desired, unhealthy tasks in the grace period might be stopped to reach the desired count.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            enable_execute_command: <p>If <code>true</code>, this enables execute command functionality on all task containers.</p> <p>If you do not want to override the value that was set when the service was created, you can set this to <code>null</code> when performing this action.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            enable_ecs_managed_tags: <p>Determines whether to turn on Amazon ECS managed tags for the tasks in the service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            load_balancers: <note> <p>You must have a service-linked role when you update this property</p> </note> <p>A list of Elastic Load Balancing load balancer objects. It contains the load balancer name, the container name, and the container port to access from the load balancer. The container name is as it appears in a container definition.</p> <p>When you add, update, or remove a load balancer configuration, Amazon ECS starts new tasks with the updated Elastic Load Balancing configuration, and then stops the old tasks when the new tasks are running.</p> <p>For services that use rolling updates, you can add, update, or remove Elastic Load Balancing target groups. You can update from a single target group to multiple target groups and from multiple target groups to a single target group.</p> <p>For services that use blue/green deployments, you can update Elastic Load Balancing target groups by using <code> <a href="https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html">CreateDeployment</a> </code> through CodeDeploy. Note that multiple target groups are not supported for blue/green deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>For services that use the external deployment controller, you can add, update, or remove load balancers by using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateTaskSet.html">CreateTaskSet</a>. Note that multiple target groups are not supported for external deployments. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html">Register multiple target groups with a service</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. </p> <p>You can remove existing <code>loadBalancers</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>
            propagate_tags: <p>Determines whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p> <p>Only tasks launched after the update will reflect the update. To update the tags on all tasks, set <code>forceNewDeployment</code> to <code>true</code>, so that Amazon ECS starts new tasks with the updated tags.</p> <p>This parameter doesn't trigger a new service deployment.</p>
            service_registries: <note> <p>You must have a service-linked role when you update this property.</p> <p>For more information about the role see the <code>CreateService</code> request parameter <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html#ECS-CreateService-request-role"> <code>role</code> </a>. </p> </note> <p>The details for the service discovery registries to assign to this service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html">Service Discovery</a>.</p> <p>When you add, update, or remove the service registries configuration, Amazon ECS starts new tasks with the updated service registries configuration, and then stops the old tasks when the new tasks are running.</p> <p>You can remove existing <code>serviceRegistries</code> by passing an empty list.</p> <p>This parameter triggers a new service deployment.</p>
            service_connect_configuration: <p>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter triggers a new service deployment.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceManagedEBSVolumeConfiguration.html">ServiceManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition. If set to null, no new deployment is triggered. Otherwise, if this configuration differs from the existing one, it triggers a new deployment.</p> <p>This parameter triggers a new service deployment.</p>
            vpc_lattice_configurations: <p>An object representing the VPC Lattice configuration for the service being updated.</p> <p>This parameter triggers a new service deployment.</p>
            monitoring: <p>The optional monitoring configuration for the service, which defines the resolution for the service-level <code>CPUUtilization</code> and <code>MemoryUtilization</code> Amazon CloudWatch metrics. When not specified, Amazon ECS uses the default resolution of <code>60</code> seconds.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.service_not_active_exception.ServiceNotActiveException: <p>The specified service isn't active. You can't update a service that's inactive. If you have previously deleted a service, you can re-create it with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html">CreateService</a>.</p>
            capo_ecs.errors.service_not_found_exception.ServiceNotFoundException: <p>The specified service wasn't found. You can view your available services with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html">ListServices</a>. Amazon ECS services are cluster specific and Region specific.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To change the task definition used in a service
            This example updates the my-http-service service to use the amazon-ecs-sample task definition.

            >>> await client.update_service(service='my-http-service', task_definition='amazon-ecs-sample')
            To change the number of tasks in a service
            This example updates the desired count of the my-http-service service to 10.

            >>> await client.update_service(service='my-http-service', desired_count=10)
            To update a service to add a pause lifecycle hook
            This example updates the my-blue-green-service service to add a pause lifecycle hook at the POST_PRODUCTION_TRAFFIC_SHIFT stage. The deployment will pause at that stage until you explicitly continue or roll back using the ContinueServiceDeployment API, or until the 30-minute timeout expires and triggers a continue.

            >>> await client.update_service(service='my-blue-green-service', deployment_configuration={'strategy': 'BLUE_GREEN', 'lifecycleHooks': [{'targetType': 'PAUSE', 'lifecycleStages': ['POST_PRODUCTION_TRAFFIC_SHIFT'], 'timeoutConfiguration': {'timeoutInMinutes': 30, 'action': 'CONTINUE'}}]})
            To update a service with a monitoring configuration
            This example updates a service to add a monitoring configuration that sets 20-second resolution for CPUUtilization and MemoryUtilization CloudWatch metrics. The monitoring configuration is not returned in the UpdateService response. Use DescribeServiceRevisions to view the monitoring configuration.

            >>> await client.update_service(service='ecs-monitored-service', monitoring={'metricConfigurations': [{'metricNames': ['CPUUtilization', 'MemoryUtilization'], 'resolutionSeconds': 20}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_service_request.UpdateServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_service.async_update_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_service_request.UpdateServiceRequest = {
            "service": service
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if desired_count is not None:
            input_["desired_count"] = desired_count
        if task_definition is not None:
            input_["task_definition"] = task_definition
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if availability_zone_rebalancing is not None:
            input_["availability_zone_rebalancing"] = availability_zone_rebalancing
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if force_new_deployment is not None:
            input_["force_new_deployment"] = force_new_deployment
        if health_check_grace_period_seconds is not None:
            input_["health_check_grace_period_seconds"] = (
                health_check_grace_period_seconds
            )
        if deployment_controller is not None:
            input_["deployment_controller"] = deployment_controller
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if load_balancers is not None:
            input_["load_balancers"] = load_balancers
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if service_registries is not None:
            input_["service_registries"] = service_registries
        if service_connect_configuration is not None:
            input_["service_connect_configuration"] = service_connect_configuration
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations
        if vpc_lattice_configurations is not None:
            input_["vpc_lattice_configurations"] = vpc_lattice_configurations
        if monitoring is not None:
            input_["monitoring"] = monitoring

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
