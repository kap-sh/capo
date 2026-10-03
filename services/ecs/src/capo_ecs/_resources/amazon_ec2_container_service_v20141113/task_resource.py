from __future__ import annotations

import uuid
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
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.capacity_provider_strategy
    import capo_ecs.types.describe_tasks_request
    import capo_ecs.types.describe_tasks_response
    import capo_ecs.types.get_task_protection_request
    import capo_ecs.types.get_task_protection_response
    import capo_ecs.types.launch_type
    import capo_ecs.types.network_configuration
    import capo_ecs.types.placement_constraints
    import capo_ecs.types.placement_strategies
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.run_task_request
    import capo_ecs.types.run_task_response
    import capo_ecs.types.start_task_request
    import capo_ecs.types.start_task_response
    import capo_ecs.types.stop_task_request
    import capo_ecs.types.stop_task_response
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags
    import capo_ecs.types.task_field_list
    import capo_ecs.types.task_override
    import capo_ecs.types.task_volume_configurations
    import capo_ecs.types.update_task_protection_request
    import capo_ecs.types.update_task_protection_response
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class TaskResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def describe_tasks(
        self,
        tasks: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional["capo_ecs.types.task_field_list.TaskFieldList"] = None,
    ) -> "capo_ecs.types.describe_tasks_response.DescribeTasksResponse":
        """<p>Describes a specified task or tasks.</p> <p>Currently, stopped tasks appear in the returned results for at least one hour.</p> <p>If you have tasks with tags, and then delete the cluster, the tagged tasks are returned in the response. If you create a new cluster with the same name as the deleted cluster, the tagged tasks are not included in the response.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed.</p>
            tasks: <p>A list of up to 100 task IDs or full ARN entries.</p>
            include: <p>Specifies whether you want to see the resource tags for the task. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a task
            This example provides a description of the specified task, using the task UUID as an identifier.

            >>> client.describe_tasks(tasks=['c5cba4eb-5dad-405e-96db-71ef8eefe6a8'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_tasks_request.DescribeTasksRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_tasks_response.DescribeTasksResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_tasks

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_tasks.describe_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_tasks_request.DescribeTasksRequest = {
            "tasks": tasks
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

    def get_task_protection(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        tasks: Optional["capo_ecs.types.string_list.StringList"] = None,
    ) -> "capo_ecs.types.get_task_protection_response.GetTaskProtectionResponse":
        """<p>Retrieves the protection status of tasks in an Amazon ECS service.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            tasks: <p>A list of up to 100 task IDs or full ARN entries.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the protection status of a task
            In this example, we get the protection status for a single task.

            >>> client.get_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.get_task_protection_request.GetTaskProtectionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.get_task_protection_response.GetTaskProtectionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.get_task_protection

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.get_task_protection.get_task_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.get_task_protection_request.GetTaskProtectionRequest = {
            "cluster": cluster
        }
        if tasks is not None:
            input_["tasks"] = tasks

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def run_task(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        group: Optional["capo_ecs.types.string.String"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        overrides: Optional["capo_ecs.types.task_override.TaskOverride"] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        reference_id: Optional["capo_ecs.types.string.String"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        volume_configurations: Optional[
            "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
        ] = None,
    ) -> "capo_ecs.types.run_task_response.RunTaskResponse":
        """<p>Starts a new task using the specified task definition.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">Scheduling Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Alternatively, you can use <code>StartTask</code> to use your own scheduler or place tasks manually on specific container instances.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.</p> <p>To manage eventual consistency, you can do the following:</p> <ul> <li> <p>Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.</p> </li> <li> <p>Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.</p> </li> </ul> <p>If you get a <code>ConflictException</code> error, the <code>RunTask</code> request could not be processed due to conflicts. The provided <code>clientToken</code> is already in use with a different <code>RunTask</code> request. The <code>resourceIds</code> are the existing task ARNs which are already associated with the <code>clientToken</code>. </p> <p>To fix this issue:</p> <ul> <li> <p>Run <code>RunTask</code> with a unique <code>clientToken</code>.</p> </li> <li> <p>Run <code>RunTask</code> with the <code>clientToken</code> and the original set of parameters</p> </li> </ul> <p>If you get a <code>ClientException</code>error, the <code>RunTask</code> could not be processed because you use managed scaling and there is a capacity error because the quota of tasks in the <code>PROVISIONING</code> per cluster has been reached. For information about the service quotas, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html">Amazon ECS service quotas</a>.</p>

        Args:
            capacity_provider_strategy: <p>The capacity provider strategy to use for the task.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.</p> <p>Each account receives a default cluster the first time you use the service, but you may also create other clusters.</p>
            count: <p>The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.</p>
            enable_ecs_managed_tags: <p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Determines whether to use the execute command functionality for the containers in this task. If <code>true</code>, this enables execute command functionality on all containers in the task.</p> <p>If <code>true</code>, then the task definition must have a task role, or you must provide one as an override.</p>
            group: <p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, <code>family:my-family-name</code>).</p>
            launch_type: <p>The infrastructure to run your standalone task on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A task can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p>
            network_configuration: <p>The network configuration for the task. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            overrides: <p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p>
            placement_constraints: <p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).</p>
            placement_strategy: <p>The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.</p>
            platform_version: <p>The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the<a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <note> <p>An error will be received if you specify the <code>SERVICE</code> option when running a task.</p> </note>
            reference_id: <p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>
            started_by: <p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, then the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>
            tags: <p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>The full ARN value must match the value that you specified as the <code>Resource</code> of the principal's permissions policy.</p> <p>When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.</p> <p>To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2</code>.</p> <p>To specify all revisions, use the wildcard (*) in the ARN. For example, to specify all revisions, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">Policy Resources for Amazon ECS</a> in the Amazon Elastic Container Service Developer Guide.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html">Ensuring idempotency</a>.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.blocked_exception.BlockedException: <p>Your Amazon Web Services account was blocked. For more information, contact <a href="http://aws.amazon.com/contact-us/"> Amazon Web Services Support</a>.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. </p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To run a task on your default cluster
            This example runs the specified task definition on your default cluster.

            >>> client.run_task(cluster='default', task_definition='sleep360:1')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.run_task_request.RunTaskRequest]",
        ) -> OperationResponse["capo_ecs.types.run_task_response.RunTaskResponse"]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.run_task

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.run_task.run_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.run_task_request.RunTaskRequest = {
            "task_definition": task_definition
        }
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if cluster is not None:
            input_["cluster"] = cluster
        if count is not None:
            input_["count"] = count
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if group is not None:
            input_["group"] = group
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if overrides is not None:
            input_["overrides"] = overrides
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if reference_id is not None:
            input_["reference_id"] = reference_id
        if started_by is not None:
            input_["started_by"] = started_by
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_task(
        self,
        container_instances: "capo_ecs.types.string_list.StringList",
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        group: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        overrides: Optional["capo_ecs.types.task_override.TaskOverride"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        reference_id: Optional["capo_ecs.types.string.String"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        volume_configurations: Optional[
            "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
        ] = None,
    ) -> "capo_ecs.types.start_task_response.StartTaskResponse":
        """<p>Starts a new task from the specified task definition on the specified container instance or instances.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>Alternatively, you can use<code>RunTask</code> to place tasks for you. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">Scheduling Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster where to start your task. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instances: <p>The container instance IDs or full ARN entries for the container instances where you would like to place your task. You can specify up to 10 container instances.</p>
            enable_ecs_managed_tags: <p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Whether or not the execute command functionality is turned on for the task. If <code>true</code>, this turns on the execute command functionality on all containers in the task.</p>
            group: <p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).</p>
            network_configuration: <p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>
            overrides: <p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it receives. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <note> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p> </note>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p>
            reference_id: <p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>
            started_by: <p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 36 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>
            tags: <p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to start. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start a new task
            This example starts a new task in the cluster "MyCluster" on the specified container instance using the latest revision of the "hello-world" task definition.

            >>> client.start_task(cluster='MyCluster', container_instances=['4c543eed-f83f-47da-b1d8-3d23f1da4c64'], task_definition='hello-world')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.start_task_request.StartTaskRequest]",
        ) -> OperationResponse["capo_ecs.types.start_task_response.StartTaskResponse"]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.start_task

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.start_task.start_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.start_task_request.StartTaskRequest = {
            "container_instances": container_instances,
            "task_definition": task_definition,
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if group is not None:
            input_["group"] = group
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if overrides is not None:
            input_["overrides"] = overrides
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if reference_id is not None:
            input_["reference_id"] = reference_id
        if started_by is not None:
            input_["started_by"] = started_by
        if tags is not None:
            input_["tags"] = tags
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_task(
        self,
        task: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.stop_task_response.StopTaskResponse":
        """<p>Stops a running task. Any tags associated with the task will be deleted.</p> <p>When you call <code>StopTask</code> on a task, the equivalent of <code>docker stop</code> is issued to the containers running in the task. This results in a stop signal value and a default 30-second timeout, after which the <code>SIGKILL</code> value is sent and the containers are forcibly stopped. This signal can be defined in your container image with the <code>STOPSIGNAL</code> instruction and will default to <code>SIGTERM</code>. If the container handles the <code>SIGTERM</code> value gracefully and exits within 30 seconds from receiving it, no <code>SIGKILL</code> value is sent.</p> <p>For Windows containers, POSIX signals do not work and runtime stops the container by sending a <code>CTRL_SHUTDOWN_EVENT</code>. For more information, see <a href="https://github.com/moby/moby/issues/25982">Unable to react to graceful shutdown of (Windows) container #25982</a> on GitHub.</p> <note> <p>The default 30-second timeout can be configured on the Amazon ECS container agent with the <code>ECS_CONTAINER_STOP_TIMEOUT</code> variable. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html">Amazon ECS Container Agent Configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.</p>
            task: <p>Thefull Amazon Resource Name (ARN) of the task.</p>
            reason: <p>An optional message specified when a task is stopped. For example, if you're using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html">DescribeTasks</a>&gt; API operations on this task.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop a task
            This example stops a task with ID "1dc5c17a-422b-4dc4-b493-371970c6c4d6" in cluster "MyCluster".

            >>> client.stop_task(cluster='MyCluster', task='1dc5c17a-422b-4dc4-b493-371970c6c4d6', reason='testing stop task.')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.stop_task_request.StopTaskRequest]",
        ) -> OperationResponse["capo_ecs.types.stop_task_response.StopTaskResponse"]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_task

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_task.stop_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.stop_task_request.StopTaskRequest = {"task": task}
        if cluster is not None:
            input_["cluster"] = cluster
        if reason is not None:
            input_["reason"] = reason

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_task_protection(
        self,
        cluster: "capo_ecs.types.string.String",
        tasks: "capo_ecs.types.string_list.StringList",
        protection_enabled: "capo_ecs.types.boolean.Boolean",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        expires_in_minutes: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
    ) -> "capo_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse":
        """<p>Updates the protection status of a task. You can set <code>protectionEnabled</code> to <code>true</code> to protect your task from termination during scale-in events from <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html">Service Autoscaling</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">deployments</a>.</p> <p>Task-protection, by default, expires after 2 hours at which point Amazon ECS clears the <code>protectionEnabled</code> property making the task eligible for termination by a subsequent scale-in event.</p> <p>You can specify a custom expiration period for task protection from 1 minute to up to 2,880 minutes (48 hours). To specify the custom expiration period, set the <code>expiresInMinutes</code> property. The <code>expiresInMinutes</code> property is always reset when you invoke this operation for a task that already has <code>protectionEnabled</code> set to <code>true</code>. You can keep extending the protection expiration period of a task by invoking this operation repeatedly.</p> <p>To learn more about Amazon ECS task protection, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection.html">Task scale-in protection</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <note> <p>This operation is only supported for tasks belonging to an Amazon ECS service. Invoking this operation for a standalone task will result in an <code>TASK_NOT_VALID</code> failure. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html">API failure reasons</a>.</p> </note> <important> <p>If you prefer to set task protection from within the container, we recommend using the <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection-endpoint.html">Task scale-in protection endpoint</a>.</p> </important>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            tasks: <p>A list of up to 10 task IDs or full ARN entries.</p>
            protection_enabled: <p>Specify <code>true</code> to mark a task for protection and <code>false</code> to unset protection, making it eligible for termination.</p>
            expires_in_minutes: <p>If you set <code>protectionEnabled</code> to <code>true</code>, you can specify the duration for task protection in minutes. You can specify a value from 1 minute to up to 2,880 minutes (48 hours). During this time, your task will not be terminated by scale-in events from Service Auto Scaling or deployments. After this time period lapses, <code>protectionEnabled</code> will be reset to <code>false</code>.</p> <p>If you don’t specify the time, then the task is automatically protected for 120 minutes (2 hours).</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set task scale-in protection for a task for 60 minutes
            This example enables scale-in protection for a task for 60 minutes.

            >>> client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=True, expires_in_minutes=60)
            To set task scale-in protection for the default time period in minutes
            This example enables task scale-in protection for a task, without specifying the expiresInMinutes parameter, for the default protection period of 120 minutes.

            >>> client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=True)
            To remove task scale-in protection
            This example removes scale-in protection for a task.

            >>> client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=False)
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_protection

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_protection.update_task_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest = {
            "cluster": cluster,
            "tasks": tasks,
            "protection_enabled": protection_enabled,
        }
        if expires_in_minutes is not None:
            input_["expires_in_minutes"] = expires_in_minutes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTaskResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def describe_tasks(
        self,
        tasks: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        include: Optional["capo_ecs.types.task_field_list.TaskFieldList"] = None,
    ) -> "capo_ecs.types.describe_tasks_response.DescribeTasksResponse":
        """<p>Describes a specified task or tasks.</p> <p>Currently, stopped tasks appear in the returned results for at least one hour.</p> <p>If you have tasks with tags, and then delete the cluster, the tagged tasks are returned in the response. If you create a new cluster with the same name as the deleted cluster, the tagged tasks are not included in the response.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed.</p>
            tasks: <p>A list of up to 100 task IDs or full ARN entries.</p>
            include: <p>Specifies whether you want to see the resource tags for the task. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a task
            This example provides a description of the specified task, using the task UUID as an identifier.

            >>> await client.describe_tasks(tasks=['c5cba4eb-5dad-405e-96db-71ef8eefe6a8'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_tasks_request.DescribeTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_tasks_response.DescribeTasksResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_tasks

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_tasks.async_describe_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_tasks_request.DescribeTasksRequest = {
            "tasks": tasks
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

    async def get_task_protection(
        self,
        cluster: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        tasks: Optional["capo_ecs.types.string_list.StringList"] = None,
    ) -> "capo_ecs.types.get_task_protection_response.GetTaskProtectionResponse":
        """<p>Retrieves the protection status of tasks in an Amazon ECS service.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            tasks: <p>A list of up to 100 task IDs or full ARN entries.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the protection status of a task
            In this example, we get the protection status for a single task.

            >>> await client.get_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.get_task_protection_request.GetTaskProtectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.get_task_protection_response.GetTaskProtectionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.get_task_protection

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.get_task_protection.async_get_task_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.get_task_protection_request.GetTaskProtectionRequest = {
            "cluster": cluster
        }
        if tasks is not None:
            input_["tasks"] = tasks

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def run_task(
        self,
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        capacity_provider_strategy: Optional[
            "capo_ecs.types.capacity_provider_strategy.CapacityProviderStrategy"
        ] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        count: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        group: Optional["capo_ecs.types.string.String"] = None,
        launch_type: Optional["capo_ecs.types.launch_type.LaunchType"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        overrides: Optional["capo_ecs.types.task_override.TaskOverride"] = None,
        placement_constraints: Optional[
            "capo_ecs.types.placement_constraints.PlacementConstraints"
        ] = None,
        placement_strategy: Optional[
            "capo_ecs.types.placement_strategies.PlacementStrategies"
        ] = None,
        platform_version: Optional["capo_ecs.types.string.String"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        reference_id: Optional["capo_ecs.types.string.String"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        client_token: Optional["capo_ecs.types.string.String"] = None,
        volume_configurations: Optional[
            "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
        ] = None,
    ) -> "capo_ecs.types.run_task_response.RunTaskResponse":
        """<p>Starts a new task using the specified task definition.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">Scheduling Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>Alternatively, you can use <code>StartTask</code> to use your own scheduler or place tasks manually on specific container instances.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.</p> <p>To manage eventual consistency, you can do the following:</p> <ul> <li> <p>Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.</p> </li> <li> <p>Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.</p> </li> </ul> <p>If you get a <code>ConflictException</code> error, the <code>RunTask</code> request could not be processed due to conflicts. The provided <code>clientToken</code> is already in use with a different <code>RunTask</code> request. The <code>resourceIds</code> are the existing task ARNs which are already associated with the <code>clientToken</code>. </p> <p>To fix this issue:</p> <ul> <li> <p>Run <code>RunTask</code> with a unique <code>clientToken</code>.</p> </li> <li> <p>Run <code>RunTask</code> with the <code>clientToken</code> and the original set of parameters</p> </li> </ul> <p>If you get a <code>ClientException</code>error, the <code>RunTask</code> could not be processed because you use managed scaling and there is a capacity error because the quota of tasks in the <code>PROVISIONING</code> per cluster has been reached. For information about the service quotas, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html">Amazon ECS service quotas</a>.</p>

        Args:
            capacity_provider_strategy: <p>The capacity provider strategy to use for the task.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p> <p>A capacity provider strategy can contain a maximum of 20 capacity providers.</p>
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster to run your task on. If you do not specify a cluster, the default cluster is assumed.</p> <p>Each account receives a default cluster the first time you use the service, but you may also create other clusters.</p>
            count: <p>The number of instantiations of the specified task to place on your cluster. You can specify up to 10 tasks for each call.</p>
            enable_ecs_managed_tags: <p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Determines whether to use the execute command functionality for the containers in this task. If <code>true</code>, this enables execute command functionality on all containers in the task.</p> <p>If <code>true</code>, then the task definition must have a task role, or you must provide one as an override.</p>
            group: <p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, <code>family:my-family-name</code>).</p>
            launch_type: <p>The infrastructure to run your standalone task on. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html">Amazon ECS launch types</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>If you want to use Amazon ECS Managed Instances, you must use the <code>capacityProviderStrategy</code> request parameter and omit the <code>launchType</code> request parameter.</p> </note> <p>The <code>FARGATE</code> launch type runs your tasks on Fargate On-Demand infrastructure.</p> <note> <p>Fargate Spot infrastructure is available for use but a capacity provider strategy must be used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html">Fargate capacity providers</a> in the <i>Amazon ECS Developer Guide</i>.</p> </note> <p>The <code>EC2</code> launch type runs your tasks on Amazon EC2 instances registered to your cluster.</p> <p>The <code>EXTERNAL</code> launch type runs your tasks on your on-premises server or virtual machine (VM) capacity registered to your cluster.</p> <p>A task can use either a launch type or a capacity provider strategy. If a <code>launchType</code> is specified, the <code>capacityProviderStrategy</code> parameter must be omitted.</p> <p>When you use cluster auto scaling, you must specify <code>capacityProviderStrategy</code> and not <code>launchType</code>. </p>
            network_configuration: <p>The network configuration for the task. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it isn't supported for other network modes. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            overrides: <p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it should receive. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p>
            placement_constraints: <p>An array of placement constraint objects to use for the task. You can specify up to 10 constraints for each task (including constraints in the task definition and those specified at runtime).</p>
            placement_strategy: <p>The placement strategy objects to use for the task. You can specify a maximum of 5 strategy rules for each task.</p>
            platform_version: <p>The platform version the task uses. A platform version is only specified for tasks hosted on Fargate. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">Fargate platform versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the<a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html">TagResource</a> API action.</p> <note> <p>An error will be received if you specify the <code>SERVICE</code> option when running a task.</p> </note>
            reference_id: <p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>
            started_by: <p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 128 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, then the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>
            tags: <p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p> <p>The full ARN value must match the value that you specified as the <code>Resource</code> of the principal's permissions policy.</p> <p>When you specify a task definition, you must either specify a specific revision, or all revisions in the ARN.</p> <p>To specify a specific revision, include the revision number in the ARN. For example, to specify revision 2, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:2</code>.</p> <p>To specify all revisions, use the wildcard (*) in the ARN. For example, to specify all revisions, use <code>arn:aws:ecs:us-east-1:111122223333:task-definition/TaskFamilyName:*</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources">Policy Resources for Amazon ECS</a> in the Amazon Elastic Container Service Developer Guide.</p>
            client_token: <p>An identifier that you provide to ensure the idempotency of the request. It must be unique and is case sensitive. Up to 64 characters are allowed. The valid characters are characters in the range of 33-126, inclusive. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/ECS_Idempotency.html">Ensuring idempotency</a>.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.blocked_exception.BlockedException: <p>Your Amazon Web Services account was blocked. For more information, contact <a href="http://aws.amazon.com/contact-us/"> Amazon Web Services Support</a>.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. </p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.platform_task_definition_incompatibility_exception.PlatformTaskDefinitionIncompatibilityException: <p>The specified platform version doesn't satisfy the required capabilities of the task definition.</p>
            capo_ecs.errors.platform_unknown_exception.PlatformUnknownException: <p>The specified platform version doesn't exist.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To run a task on your default cluster
            This example runs the specified task definition on your default cluster.

            >>> await client.run_task(cluster='default', task_definition='sleep360:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.run_task_request.RunTaskRequest]",
        ) -> AsyncOperationResponse["capo_ecs.types.run_task_response.RunTaskResponse"]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.run_task

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.run_task.async_run_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.run_task_request.RunTaskRequest = {
            "task_definition": task_definition
        }
        if capacity_provider_strategy is not None:
            input_["capacity_provider_strategy"] = capacity_provider_strategy
        if cluster is not None:
            input_["cluster"] = cluster
        if count is not None:
            input_["count"] = count
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if group is not None:
            input_["group"] = group
        if launch_type is not None:
            input_["launch_type"] = launch_type
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if overrides is not None:
            input_["overrides"] = overrides
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if placement_strategy is not None:
            input_["placement_strategy"] = placement_strategy
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if reference_id is not None:
            input_["reference_id"] = reference_id
        if started_by is not None:
            input_["started_by"] = started_by
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_task(
        self,
        container_instances: "capo_ecs.types.string_list.StringList",
        task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        enable_ecs_managed_tags: Optional["capo_ecs.types.boolean.Boolean"] = None,
        enable_execute_command: Optional["capo_ecs.types.boolean.Boolean"] = None,
        group: Optional["capo_ecs.types.string.String"] = None,
        network_configuration: Optional[
            "capo_ecs.types.network_configuration.NetworkConfiguration"
        ] = None,
        overrides: Optional["capo_ecs.types.task_override.TaskOverride"] = None,
        propagate_tags: Optional["capo_ecs.types.propagate_tags.PropagateTags"] = None,
        reference_id: Optional["capo_ecs.types.string.String"] = None,
        started_by: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        volume_configurations: Optional[
            "capo_ecs.types.task_volume_configurations.TaskVolumeConfigurations"
        ] = None,
    ) -> "capo_ecs.types.start_task_response.StartTaskResponse":
        """<p>Starts a new task from the specified task definition on the specified container instance or instances.</p> <note> <p>On March 21, 2024, a change was made to resolve the task definition revision before authorization. When a task definition revision is not specified, authorization will occur using the latest revision of a task definition.</p> </note> <note> <p>Amazon Elastic Inference (EI) is no longer available to customers.</p> </note> <p>Alternatively, you can use<code>RunTask</code> to place tasks for you. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">Scheduling Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can attach Amazon EBS volumes to Amazon ECS tasks by configuring the volume when creating or updating a service. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html#ebs-volume-types">Amazon EBS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster where to start your task. If you do not specify a cluster, the default cluster is assumed.</p>
            container_instances: <p>The container instance IDs or full ARN entries for the container instances where you would like to place your task. You can specify up to 10 container instances.</p>
            enable_ecs_managed_tags: <p>Specifies whether to use Amazon ECS managed tags for the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html">Tagging Your Amazon ECS Resources</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            enable_execute_command: <p>Whether or not the execute command functionality is turned on for the task. If <code>true</code>, this turns on the execute command functionality on all containers in the task.</p>
            group: <p>The name of the task group to associate with the task. The default value is the family name of the task definition (for example, family:my-family-name).</p>
            network_configuration: <p>The VPC subnet and security group configuration for tasks that receive their own elastic network interface by using the <code>awsvpc</code> networking mode.</p>
            overrides: <p>A list of container overrides in JSON format that specify the name of a container in the specified task definition and the overrides it receives. You can override the default command for a container (that's specified in the task definition or Docker image) with a <code>command</code> override. You can also override existing environment variables (that are specified in the task definition or Docker image) on a container or add new environment variables to it with an <code>environment</code> override.</p> <note> <p>A total of 8192 characters are allowed for overrides. This limit includes the JSON formatting characters of the override structure.</p> </note>
            propagate_tags: <p>Specifies whether to propagate the tags from the task definition or the service to the task. If no value is specified, the tags aren't propagated.</p>
            reference_id: <p>This parameter is only used by Amazon ECS. It is not intended for use by customers.</p>
            started_by: <p>An optional tag specified when a task is started. For example, if you automatically trigger a task to run a batch process job, you could apply a unique identifier for that job to your task with the <code>startedBy</code> parameter. You can then identify which tasks belong to that job by filtering the results of a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListTasks.html">ListTasks</a> call with the <code>startedBy</code> value. Up to 36 letters (uppercase and lowercase), numbers, hyphens (-), forward slash (/), and underscores (_) are allowed.</p> <p>If a task is started by an Amazon ECS service, the <code>startedBy</code> parameter contains the deployment ID of the service that starts it.</p>
            tags: <p>The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to start. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.</p>
            volume_configurations: <p>The details of the volume that was <code>configuredAtLaunch</code>. You can configure the size, volumeType, IOPS, throughput, snapshot and encryption in <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TaskManagedEBSVolumeConfiguration.html">TaskManagedEBSVolumeConfiguration</a>. The <code>name</code> of the volume must match the <code>name</code> from the task definition.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.namespace_not_found_exception.NamespaceNotFoundException: <p>The specified namespace wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start a new task
            This example starts a new task in the cluster "MyCluster" on the specified container instance using the latest revision of the "hello-world" task definition.

            >>> await client.start_task(cluster='MyCluster', container_instances=['4c543eed-f83f-47da-b1d8-3d23f1da4c64'], task_definition='hello-world')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.start_task_request.StartTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.start_task_response.StartTaskResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.start_task

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.start_task.async_start_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.start_task_request.StartTaskRequest = {
            "container_instances": container_instances,
            "task_definition": task_definition,
        }
        if cluster is not None:
            input_["cluster"] = cluster
        if enable_ecs_managed_tags is not None:
            input_["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            input_["enable_execute_command"] = enable_execute_command
        if group is not None:
            input_["group"] = group
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if overrides is not None:
            input_["overrides"] = overrides
        if propagate_tags is not None:
            input_["propagate_tags"] = propagate_tags
        if reference_id is not None:
            input_["reference_id"] = reference_id
        if started_by is not None:
            input_["started_by"] = started_by
        if tags is not None:
            input_["tags"] = tags
        if volume_configurations is not None:
            input_["volume_configurations"] = volume_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_task(
        self,
        task: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        cluster: Optional["capo_ecs.types.string.String"] = None,
        reason: Optional["capo_ecs.types.string.String"] = None,
    ) -> "capo_ecs.types.stop_task_response.StopTaskResponse":
        """<p>Stops a running task. Any tags associated with the task will be deleted.</p> <p>When you call <code>StopTask</code> on a task, the equivalent of <code>docker stop</code> is issued to the containers running in the task. This results in a stop signal value and a default 30-second timeout, after which the <code>SIGKILL</code> value is sent and the containers are forcibly stopped. This signal can be defined in your container image with the <code>STOPSIGNAL</code> instruction and will default to <code>SIGTERM</code>. If the container handles the <code>SIGTERM</code> value gracefully and exits within 30 seconds from receiving it, no <code>SIGKILL</code> value is sent.</p> <p>For Windows containers, POSIX signals do not work and runtime stops the container by sending a <code>CTRL_SHUTDOWN_EVENT</code>. For more information, see <a href="https://github.com/moby/moby/issues/25982">Unable to react to graceful shutdown of (Windows) container #25982</a> on GitHub.</p> <note> <p>The default 30-second timeout can be configured on the Amazon ECS container agent with the <code>ECS_CONTAINER_STOP_TIMEOUT</code> variable. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html">Amazon ECS Container Agent Configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.</p>
            task: <p>Thefull Amazon Resource Name (ARN) of the task.</p>
            reason: <p>An optional message specified when a task is stopped. For example, if you're using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html">DescribeTasks</a>&gt; API operations on this task.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To stop a task
            This example stops a task with ID "1dc5c17a-422b-4dc4-b493-371970c6c4d6" in cluster "MyCluster".

            >>> await client.stop_task(cluster='MyCluster', task='1dc5c17a-422b-4dc4-b493-371970c6c4d6', reason='testing stop task.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.stop_task_request.StopTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.stop_task_response.StopTaskResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_task

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.stop_task.async_stop_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.stop_task_request.StopTaskRequest = {"task": task}
        if cluster is not None:
            input_["cluster"] = cluster
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_task_protection(
        self,
        cluster: "capo_ecs.types.string.String",
        tasks: "capo_ecs.types.string_list.StringList",
        protection_enabled: "capo_ecs.types.boolean.Boolean",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        expires_in_minutes: Optional[
            "capo_ecs.types.boxed_integer.BoxedInteger"
        ] = None,
    ) -> "capo_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse":
        """<p>Updates the protection status of a task. You can set <code>protectionEnabled</code> to <code>true</code> to protect your task from termination during scale-in events from <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html">Service Autoscaling</a> or <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html">deployments</a>.</p> <p>Task-protection, by default, expires after 2 hours at which point Amazon ECS clears the <code>protectionEnabled</code> property making the task eligible for termination by a subsequent scale-in event.</p> <p>You can specify a custom expiration period for task protection from 1 minute to up to 2,880 minutes (48 hours). To specify the custom expiration period, set the <code>expiresInMinutes</code> property. The <code>expiresInMinutes</code> property is always reset when you invoke this operation for a task that already has <code>protectionEnabled</code> set to <code>true</code>. You can keep extending the protection expiration period of a task by invoking this operation repeatedly.</p> <p>To learn more about Amazon ECS task protection, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection.html">Task scale-in protection</a> in the <i> <i>Amazon Elastic Container Service Developer Guide</i> </i>.</p> <note> <p>This operation is only supported for tasks belonging to an Amazon ECS service. Invoking this operation for a standalone task will result in an <code>TASK_NOT_VALID</code> failure. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html">API failure reasons</a>.</p> </note> <important> <p>If you prefer to set task protection from within the container, we recommend using the <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection-endpoint.html">Task scale-in protection endpoint</a>.</p> </important>

        Args:
            cluster: <p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>
            tasks: <p>A list of up to 10 task IDs or full ARN entries.</p>
            protection_enabled: <p>Specify <code>true</code> to mark a task for protection and <code>false</code> to unset protection, making it eligible for termination.</p>
            expires_in_minutes: <p>If you set <code>protectionEnabled</code> to <code>true</code>, you can specify the duration for task protection in minutes. You can specify a value from 1 minute to up to 2,880 minutes (48 hours). During this time, your task will not be terminated by scale-in events from Service Auto Scaling or deployments. After this time period lapses, <code>protectionEnabled</code> will be reset to <code>false</code>.</p> <p>If you don’t specify the time, then the task is automatically protected for 120 minutes (2 hours).</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.cluster_not_found_exception.ClusterNotFoundException: <p>The specified cluster wasn't found. You can view your available clusters with <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListClusters.html">ListClusters</a>. Amazon ECS clusters are Region specific.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.unsupported_feature_exception.UnsupportedFeatureException: <p>The specified task isn't supported in this Region.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set task scale-in protection for a task for 60 minutes
            This example enables scale-in protection for a task for 60 minutes.

            >>> await client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=True, expires_in_minutes=60)
            To set task scale-in protection for the default time period in minutes
            This example enables task scale-in protection for a task, without specifying the expiresInMinutes parameter, for the default protection period of 120 minutes.

            >>> await client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=True)
            To remove task scale-in protection
            This example removes scale-in protection for a task.

            >>> await client.update_task_protection(cluster='test-task-protection', tasks=['b8b1cf532d0e46ba8d44a40d1de16772'], protection_enabled=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_protection

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.update_task_protection.async_update_task_protection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest = {
            "cluster": cluster,
            "tasks": tasks,
            "protection_enabled": protection_enabled,
        }
        if expires_in_minutes is not None:
            input_["expires_in_minutes"] = expires_in_minutes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
