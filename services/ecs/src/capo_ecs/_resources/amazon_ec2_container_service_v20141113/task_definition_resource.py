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
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.compatibility_list
    import capo_ecs.types.container_definitions
    import capo_ecs.types.delete_task_definitions_request
    import capo_ecs.types.delete_task_definitions_response
    import capo_ecs.types.ephemeral_storage
    import capo_ecs.types.inference_accelerators
    import capo_ecs.types.ipc_mode
    import capo_ecs.types.list_task_definitions_request
    import capo_ecs.types.list_task_definitions_response
    import capo_ecs.types.network_mode
    import capo_ecs.types.pid_mode
    import capo_ecs.types.proxy_configuration
    import capo_ecs.types.register_task_definition_request
    import capo_ecs.types.register_task_definition_response
    import capo_ecs.types.runtime_platform
    import capo_ecs.types.sort_order
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.tags
    import capo_ecs.types.task_definition_placement_constraints
    import capo_ecs.types.task_definition_status
    import capo_ecs.types.volume_list
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class TaskDefinitionResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def delete_task_definitions(
        self,
        task_definitions: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> (
        "capo_ecs.types.delete_task_definitions_response.DeleteTaskDefinitionsResponse"
    ):
        """<p>Deletes one or more task definitions.</p> <p>You must deregister a task definition revision before you delete it. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html">DeregisterTaskDefinition</a>.</p> <p>When you delete a task definition revision, it is immediately transitions from the <code>INACTIVE</code> to <code>DELETE_IN_PROGRESS</code>. Existing tasks and services that reference a <code>DELETE_IN_PROGRESS</code> task definition revision continue to run without disruption. Existing services that reference a <code>DELETE_IN_PROGRESS</code> task definition revision can still scale up or down by modifying the service's desired count.</p> <p>You can't use a <code>DELETE_IN_PROGRESS</code> task definition revision to run new tasks or create new services. You also can't update an existing service to reference a <code>DELETE_IN_PROGRESS</code> task definition revision.</p> <p> A task definition revision will stay in <code>DELETE_IN_PROGRESS</code> status until all the associated tasks and services have been terminated.</p> <p>When you delete all <code>INACTIVE</code> task definition revisions, the task definition name is not displayed in the console and not returned in the API. If a task definition revisions are in the <code>DELETE_IN_PROGRESS</code> state, the task definition name is displayed in the console and returned in the API. The task definition name is retained by Amazon ECS and the revision is incremented the next time you create a task definition with that name.</p>

        Args:
            task_definitions: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to delete. You must specify a <code>revision</code>.</p> <p>You can specify up to 10 task definitions as a comma separated list.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a task definition that has been deregistered
            This example deletes a specified deregistered task definition.

            >>> client.delete_task_definitions(task_definitions=['Example-task-definition:1'])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_task_definitions_request.DeleteTaskDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_task_definitions_response.DeleteTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_definitions

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_definitions.delete_task_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_task_definitions_request.DeleteTaskDefinitionsRequest = {
            "task_definitions": task_definitions
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_task_definitions(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_status.TaskDefinitionStatus"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_task_definitions_response.ListTaskDefinitionsResponse":
        """<p>Returns a list of task definitions that are registered to your account. You can filter the results by family name with the <code>familyPrefix</code> parameter or by status with the <code>status</code> parameter.</p>

        Args:
            family_prefix: <p>The full family name to filter the <code>ListTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed task definitions to task definition revisions that belong to that family.</p>
            status: <p>The task definition status to filter the <code>ListTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> task definitions are listed. By setting this parameter to <code>INACTIVE</code>, you can view task definitions that are <code>INACTIVE</code> as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the <code>status</code> value constant in each subsequent request.</p>
            sort: <p>The order to sort the results in. Valid values are <code>ASC</code> and <code>DESC</code>. By default, (<code>ASC</code>) task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to <code>DESC</code> reverses the sort order on family name and revision. This is so that the newest task definitions in a family are listed first.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task definition results that <code>ListTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your registered task definitions
            This example lists all of your registered task definitions.

            >>> client.list_task_definitions()
            To list the registered task definitions in a family
            This example lists the task definition revisions of a specified family.

            >>> client.list_task_definitions(family_prefix='wordpress')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_task_definitions_request.ListTaskDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_task_definitions_response.ListTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definitions

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definitions.list_task_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_task_definitions_request.ListTaskDefinitionsRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort
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

    def register_task_definition(
        self,
        family: "capo_ecs.types.string.String",
        container_definitions: "capo_ecs.types.container_definitions.ContainerDefinitions",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_mode: Optional["capo_ecs.types.network_mode.NetworkMode"] = None,
        volumes: Optional["capo_ecs.types.volume_list.VolumeList"] = None,
        placement_constraints: Optional[
            "capo_ecs.types.task_definition_placement_constraints.TaskDefinitionPlacementConstraints"
        ] = None,
        requires_compatibilities: Optional[
            "capo_ecs.types.compatibility_list.CompatibilityList"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        pid_mode: Optional["capo_ecs.types.pid_mode.PidMode"] = None,
        ipc_mode: Optional["capo_ecs.types.ipc_mode.IpcMode"] = None,
        proxy_configuration: Optional[
            "capo_ecs.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        inference_accelerators: Optional[
            "capo_ecs.types.inference_accelerators.InferenceAccelerators"
        ] = None,
        ephemeral_storage: Optional[
            "capo_ecs.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        runtime_platform: Optional[
            "capo_ecs.types.runtime_platform.RuntimePlatform"
        ] = None,
        enable_fault_injection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
    ) -> "capo_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse":
        """<p>Registers a new task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information about task definition parameters and defaults, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html">Amazon ECS Task Definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can specify a role for your task with the <code>taskRoleArn</code> parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the Amazon Web Services services that are specified in the policy that's associated with the role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can specify a Docker networking mode for the containers in your task definition with the <code>networkMode</code> parameter. If you specify the <code>awsvpc</code> network mode, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            family: <p>You must specify a <code>family</code> for a task definition. You can use it track multiple versions of the same task definition. The <code>family</code> is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            task_role_arn: <p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html">IAM roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            network_mode: <p>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>.</p> <p>For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>&lt;default&gt;</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode.</p> <p>With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. </p> <important> <p>When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.</p> </important> <p>If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> value when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.</p>
            container_definitions: <p>A list of container definitions in JSON format that describe the different containers that make up your task.</p>
            volumes: <p>A list of volume definitions in JSON format that containers in your task might use.</p>
            placement_constraints: <p>An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>
            requires_compatibilities: <p>The task launch type that Amazon ECS validates the task definition against. A client exception is returned if the task definition doesn't validate against the compatibilities specified. If no value is specified, the parameter is omitted from the response.</p>
            cpu: <p>The number of CPU units used by the task. It can be expressed as an integer using CPU units (for example, <code>1024</code>) or as a string using vCPUs (for example, <code>1 vCPU</code> or <code>1 vcpu</code>) in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If you're using the EC2 launch type or external launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>196608</code> CPU units (<code>192</code> vCPUs). If you do not specify a value, the parameter is ignored.</p> <p>This field is required for Fargate. For information about the valid values, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size">Task size</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            memory: <p>The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB (for example ,<code>1024</code>) or as a string using GB (for example, <code>1GB</code> or <code>1 GB</code>) in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If using the EC2 launch type, this field is optional.</p> <p>If using the Fargate launch type, this field is required and you must use one of the following values. This determines your range of supported values for the <code>cpu</code> parameter.</p> <p>The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.</p> <ul> <li> <p>512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)</p> </li> <li> <p>1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)</p> </li> <li> <p>2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)</p> </li> <li> <p>Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)</p> </li> <li> <p>Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)</p> </li> <li> <p>Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> <li> <p>Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> </ul>
            tags: <p>The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            pid_mode: <p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the The default is a private namespace for each container.</p> <p>If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note> <note> <p>This parameter is only supported for tasks that are hosted on Fargate if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</p> </note>
            ipc_mode: <p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.</p> <p>If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.</p> <p>If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">System Controls</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <ul> <li> <p>For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported.</p> </li> <li> <p>For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task.</p> </li> </ul> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>
            proxy_configuration: <p>The configuration details for the App Mesh proxy.</p> <p>For tasks hosted on Amazon EC2 instances, the container instances require at least version <code>1.26.0</code> of the container agent and at least version <code>1.26.0-1</code> of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-versions.html">Amazon ECS-optimized AMI versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            inference_accelerators: <p>The Elastic Inference accelerators to use for the containers in the task.</p>
            ephemeral_storage: <p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html">Using data volumes in tasks</a> in the <i>Amazon ECS Developer Guide</i>.</p> <note> <p>For tasks using the Fargate launch type, the task requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>
            runtime_platform: <p>The operating system that your tasks definitions run on.</p>
            enable_fault_injection: <p>Enables fault injection when you register your task definition and allows for fault injection requests to be accepted from the task's containers. The default value is <code>false</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register a task definition
            This example registers a task definition to the specified family.

            >>> client.register_task_definition(family='sleep360', task_role_arn='', container_definitions=[{'name': 'sleep', 'image': 'public.ecr.aws/docker/library/busybox:latest', 'cpu': 10, 'command': ['sleep', '360'], 'memory': 10, 'essential': True}], volumes=[])
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_task_definition

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.register_task_definition.register_task_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest = {
            "family": family,
            "container_definitions": container_definitions,
        }
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if network_mode is not None:
            input_["network_mode"] = network_mode
        if volumes is not None:
            input_["volumes"] = volumes
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if requires_compatibilities is not None:
            input_["requires_compatibilities"] = requires_compatibilities
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if tags is not None:
            input_["tags"] = tags
        if pid_mode is not None:
            input_["pid_mode"] = pid_mode
        if ipc_mode is not None:
            input_["ipc_mode"] = ipc_mode
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if inference_accelerators is not None:
            input_["inference_accelerators"] = inference_accelerators
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if runtime_platform is not None:
            input_["runtime_platform"] = runtime_platform
        if enable_fault_injection is not None:
            input_["enable_fault_injection"] = enable_fault_injection

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTaskDefinitionResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def delete_task_definitions(
        self,
        task_definitions: "capo_ecs.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> (
        "capo_ecs.types.delete_task_definitions_response.DeleteTaskDefinitionsResponse"
    ):
        """<p>Deletes one or more task definitions.</p> <p>You must deregister a task definition revision before you delete it. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html">DeregisterTaskDefinition</a>.</p> <p>When you delete a task definition revision, it is immediately transitions from the <code>INACTIVE</code> to <code>DELETE_IN_PROGRESS</code>. Existing tasks and services that reference a <code>DELETE_IN_PROGRESS</code> task definition revision continue to run without disruption. Existing services that reference a <code>DELETE_IN_PROGRESS</code> task definition revision can still scale up or down by modifying the service's desired count.</p> <p>You can't use a <code>DELETE_IN_PROGRESS</code> task definition revision to run new tasks or create new services. You also can't update an existing service to reference a <code>DELETE_IN_PROGRESS</code> task definition revision.</p> <p> A task definition revision will stay in <code>DELETE_IN_PROGRESS</code> status until all the associated tasks and services have been terminated.</p> <p>When you delete all <code>INACTIVE</code> task definition revisions, the task definition name is not displayed in the console and not returned in the API. If a task definition revisions are in the <code>DELETE_IN_PROGRESS</code> state, the task definition name is displayed in the console and returned in the API. The task definition name is retained by Amazon ECS and the revision is incremented the next time you create a task definition with that name.</p>

        Args:
            task_definitions: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to delete. You must specify a <code>revision</code>.</p> <p>You can specify up to 10 task definitions as a comma separated list.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a task definition that has been deregistered
            This example deletes a specified deregistered task definition.

            >>> await client.delete_task_definitions(task_definitions=['Example-task-definition:1'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_task_definitions_request.DeleteTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_task_definitions_response.DeleteTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_definitions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_task_definitions.async_delete_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_task_definitions_request.DeleteTaskDefinitionsRequest = {
            "task_definitions": task_definitions
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        status: Optional[
            "capo_ecs.types.task_definition_status.TaskDefinitionStatus"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_task_definitions_response.ListTaskDefinitionsResponse":
        """<p>Returns a list of task definitions that are registered to your account. You can filter the results by family name with the <code>familyPrefix</code> parameter or by status with the <code>status</code> parameter.</p>

        Args:
            family_prefix: <p>The full family name to filter the <code>ListTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed task definitions to task definition revisions that belong to that family.</p>
            status: <p>The task definition status to filter the <code>ListTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> task definitions are listed. By setting this parameter to <code>INACTIVE</code>, you can view task definitions that are <code>INACTIVE</code> as long as an active task or service still references them. If you paginate the resulting output, be sure to keep the <code>status</code> value constant in each subsequent request.</p>
            sort: <p>The order to sort the results in. Valid values are <code>ASC</code> and <code>DESC</code>. By default, (<code>ASC</code>) task definitions are listed lexicographically by family name and in ascending numerical order by revision so that the newest task definitions in a family are listed last. Setting this parameter to <code>DESC</code> reverses the sort order on family name and revision. This is so that the newest task definitions in a family are listed first.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of task definition results that <code>ListTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list your registered task definitions
            This example lists all of your registered task definitions.

            >>> await client.list_task_definitions()
            To list the registered task definitions in a family
            This example lists the task definition revisions of a specified family.

            >>> await client.list_task_definitions(family_prefix='wordpress')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_task_definitions_request.ListTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_task_definitions_response.ListTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definitions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_task_definitions.async_list_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_task_definitions_request.ListTaskDefinitionsRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if status is not None:
            input_["status"] = status
        if sort is not None:
            input_["sort"] = sort
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

    async def register_task_definition(
        self,
        family: "capo_ecs.types.string.String",
        container_definitions: "capo_ecs.types.container_definitions.ContainerDefinitions",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        network_mode: Optional["capo_ecs.types.network_mode.NetworkMode"] = None,
        volumes: Optional["capo_ecs.types.volume_list.VolumeList"] = None,
        placement_constraints: Optional[
            "capo_ecs.types.task_definition_placement_constraints.TaskDefinitionPlacementConstraints"
        ] = None,
        requires_compatibilities: Optional[
            "capo_ecs.types.compatibility_list.CompatibilityList"
        ] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        pid_mode: Optional["capo_ecs.types.pid_mode.PidMode"] = None,
        ipc_mode: Optional["capo_ecs.types.ipc_mode.IpcMode"] = None,
        proxy_configuration: Optional[
            "capo_ecs.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        inference_accelerators: Optional[
            "capo_ecs.types.inference_accelerators.InferenceAccelerators"
        ] = None,
        ephemeral_storage: Optional[
            "capo_ecs.types.ephemeral_storage.EphemeralStorage"
        ] = None,
        runtime_platform: Optional[
            "capo_ecs.types.runtime_platform.RuntimePlatform"
        ] = None,
        enable_fault_injection: Optional[
            "capo_ecs.types.boxed_boolean.BoxedBoolean"
        ] = None,
    ) -> "capo_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse":
        """<p>Registers a new task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information about task definition parameters and defaults, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html">Amazon ECS Task Definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can specify a role for your task with the <code>taskRoleArn</code> parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the Amazon Web Services services that are specified in the policy that's associated with the role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>You can specify a Docker networking mode for the containers in your task definition with the <code>networkMode</code> parameter. If you specify the <code>awsvpc</code> network mode, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

        Args:
            family: <p>You must specify a <code>family</code> for a task definition. You can use it track multiple versions of the same task definition. The <code>family</code> is used as a name for your task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            task_role_arn: <p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html">IAM Roles for Tasks</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html">IAM roles for Amazon ECS</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            network_mode: <p>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>.</p> <p>For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>&lt;default&gt;</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode.</p> <p>With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. </p> <important> <p>When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.</p> </important> <p>If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html">NetworkConfiguration</a> value when you create a service or run a task with the task definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.</p>
            container_definitions: <p>A list of container definitions in JSON format that describe the different containers that make up your task.</p>
            volumes: <p>A list of volume definitions in JSON format that containers in your task might use.</p>
            placement_constraints: <p>An array of placement constraint objects to use for the task. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</p>
            requires_compatibilities: <p>The task launch type that Amazon ECS validates the task definition against. A client exception is returned if the task definition doesn't validate against the compatibilities specified. If no value is specified, the parameter is omitted from the response.</p>
            cpu: <p>The number of CPU units used by the task. It can be expressed as an integer using CPU units (for example, <code>1024</code>) or as a string using vCPUs (for example, <code>1 vCPU</code> or <code>1 vcpu</code>) in a task definition. String values are converted to an integer indicating the CPU units when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If you're using the EC2 launch type or external launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>196608</code> CPU units (<code>192</code> vCPUs). If you do not specify a value, the parameter is ignored.</p> <p>This field is required for Fargate. For information about the valid values, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_size">Task size</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            memory: <p>The amount of memory (in MiB) used by the task. It can be expressed as an integer using MiB (for example ,<code>1024</code>) or as a string using GB (for example, <code>1GB</code> or <code>1 GB</code>) in a task definition. String values are converted to an integer indicating the MiB when the task definition is registered.</p> <note> <p>Task-level CPU and memory parameters are ignored for Windows containers. We recommend specifying container-level resources for Windows containers.</p> </note> <p>If using the EC2 launch type, this field is optional.</p> <p>If using the Fargate launch type, this field is required and you must use one of the following values. This determines your range of supported values for the <code>cpu</code> parameter.</p> <p>The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.</p> <ul> <li> <p>512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)</p> </li> <li> <p>1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)</p> </li> <li> <p>2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)</p> </li> <li> <p>Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)</p> </li> <li> <p>Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)</p> </li> <li> <p>Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> <li> <p>Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)</p> <p>This option requires Linux platform <code>1.4.0</code> or later.</p> </li> </ul>
            tags: <p>The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            pid_mode: <p>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.</p> <p>If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.</p> <p>If <code>task</code> is specified, all containers within the specified task share the same process namespace.</p> <p>If no value is specified, the The default is a private namespace for each container.</p> <p>If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note> <note> <p>This parameter is only supported for tasks that are hosted on Fargate if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</p> </note>
            ipc_mode: <p>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.</p> <p>If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.</p> <p>If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">System Controls</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <ul> <li> <p>For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported.</p> </li> <li> <p>For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task.</p> </li> </ul> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>
            proxy_configuration: <p>The configuration details for the App Mesh proxy.</p> <p>For tasks hosted on Amazon EC2 instances, the container instances require at least version <code>1.26.0</code> of the container agent and at least version <code>1.26.0-1</code> of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS-optimized AMI version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-versions.html">Amazon ECS-optimized AMI versions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>
            inference_accelerators: <p>The Elastic Inference accelerators to use for the containers in the task.</p>
            ephemeral_storage: <p>The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on Fargate. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html">Using data volumes in tasks</a> in the <i>Amazon ECS Developer Guide</i>.</p> <note> <p>For tasks using the Fargate launch type, the task requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.4.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> </note>
            runtime_platform: <p>The operating system that your tasks definitions run on.</p>
            enable_fault_injection: <p>Enables fault injection when you register your task definition and allows for fault injection requests to be accepted from the task's containers. The default value is <code>false</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register a task definition
            This example registers a task definition to the specified family.

            >>> await client.register_task_definition(family='sleep360', task_role_arn='', container_definitions=[{'name': 'sleep', 'image': 'public.ecr.aws/docker/library/busybox:latest', 'cpu': 10, 'command': ['sleep', '360'], 'memory': 10, 'essential': True}], volumes=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.register_task_definition.async_register_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest = {
            "family": family,
            "container_definitions": container_definitions,
        }
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if network_mode is not None:
            input_["network_mode"] = network_mode
        if volumes is not None:
            input_["volumes"] = volumes
        if placement_constraints is not None:
            input_["placement_constraints"] = placement_constraints
        if requires_compatibilities is not None:
            input_["requires_compatibilities"] = requires_compatibilities
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if tags is not None:
            input_["tags"] = tags
        if pid_mode is not None:
            input_["pid_mode"] = pid_mode
        if ipc_mode is not None:
            input_["ipc_mode"] = ipc_mode
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if inference_accelerators is not None:
            input_["inference_accelerators"] = inference_accelerators
        if ephemeral_storage is not None:
            input_["ephemeral_storage"] = ephemeral_storage
        if runtime_platform is not None:
            input_["runtime_platform"] = runtime_platform
        if enable_fault_injection is not None:
            input_["enable_fault_injection"] = enable_fault_injection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
