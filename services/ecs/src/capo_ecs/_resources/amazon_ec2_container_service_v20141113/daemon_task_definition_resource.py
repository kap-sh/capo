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
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.daemon_container_definition_list
    import capo_ecs.types.daemon_ipc_mode
    import capo_ecs.types.daemon_pid_mode
    import capo_ecs.types.daemon_task_definition_revision_filter
    import capo_ecs.types.daemon_task_definition_status_filter
    import capo_ecs.types.daemon_volume_list
    import capo_ecs.types.delete_daemon_task_definition_request
    import capo_ecs.types.delete_daemon_task_definition_response
    import capo_ecs.types.describe_daemon_task_definition_request
    import capo_ecs.types.describe_daemon_task_definition_response
    import capo_ecs.types.list_daemon_task_definitions_request
    import capo_ecs.types.list_daemon_task_definitions_response
    import capo_ecs.types.register_daemon_task_definition_request
    import capo_ecs.types.register_daemon_task_definition_response
    import capo_ecs.types.sort_order
    import capo_ecs.types.string
    import capo_ecs.types.tags
    from capo_ecs._services.async_ecs import AsyncECSClient, AsyncECSClientConfig
    from capo_ecs._services.ecs import ECSClient, ECSClientConfig


class DaemonTaskDefinitionResource:
    def __init__(self, service: ECSClient) -> None:
        self._service = service

    def delete_daemon_task_definition(
        self,
        daemon_task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse":
        """<p>Deletes the specified daemon task definition. After a daemon task definition is deleted, no new daemons can be created using this definition. Existing daemons that reference the deleted daemon task definition continue to run.</p> <p>A daemon task definition must be in an <code>ACTIVE</code> state to be deleted.</p>

        Args:
            daemon_task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the daemon task definition to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a daemon task definition
            This example deletes the first revision of the monitoring-agent daemon task definition.

            >>> client.delete_daemon_task_definition(daemon_task_definition='monitoring-agent:1')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon_task_definition

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon_task_definition.delete_daemon_task_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest = {
            "daemon_task_definition": daemon_task_definition
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_daemon_task_definition(
        self,
        daemon_task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_task_definition_response.DescribeDaemonTaskDefinitionResponse":
        """<p>Describes a daemon task definition. You can specify a <code>family</code> and <code>revision</code> to find information about a specific daemon task definition, or you can simply specify the family to find the latest <code>ACTIVE</code> revision in that family.</p>

        Args:
            daemon_task_definition: <p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the daemon task definition to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a daemon task definition
            This example describes the first revision of the monitoring-agent daemon task definition.

            >>> client.describe_daemon_task_definition(daemon_task_definition='monitoring-agent:1')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.describe_daemon_task_definition_request.DescribeDaemonTaskDefinitionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.describe_daemon_task_definition_response.DescribeDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_task_definition

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_task_definition.describe_daemon_task_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_task_definition_request.DescribeDaemonTaskDefinitionRequest = {
            "daemon_task_definition": daemon_task_definition
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_daemon_task_definitions(
        self,
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        family: Optional["capo_ecs.types.string.String"] = None,
        revision: Optional[
            "capo_ecs.types.daemon_task_definition_revision_filter.DaemonTaskDefinitionRevisionFilter"
        ] = None,
        status: Optional[
            "capo_ecs.types.daemon_task_definition_status_filter.DaemonTaskDefinitionStatusFilter"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse":
        """<p>Returns a list of daemon task definitions that are registered to your account. You can filter the results by family name, status, or both to find daemon task definitions that match your criteria.</p>

        Args:
            family_prefix: <p>The full family name to filter the <code>ListDaemonTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed daemon task definitions to daemon task definition families that start with the <code>familyPrefix</code> string.</p>
            family: <p>The exact name of the daemon task definition family to filter results with.</p>
            revision: <p>The revision filter to apply. Specify <code>LAST_REGISTERED</code> to return only the last registered revision for each daemon task definition family.</p>
            status: <p>The daemon task definition status to filter the <code>ListDaemonTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> daemon task definitions are listed. If you set this parameter to <code>DELETE_IN_PROGRESS</code>, only daemon task definitions that are in the process of being deleted are listed. If you set this parameter to <code>ALL</code>, all daemon task definitions are listed regardless of status.</p>
            sort: <p>The order to sort the results. Valid values are <code>ASC</code> and <code>DESC</code>. By default (<code>ASC</code>), daemon task definitions are listed in ascending order by family name and revision number.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemonTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of daemon task definition results that <code>ListDaemonTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListDaemonTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemon task definitions
            This example lists all daemon task definitions in your account that start with the monitoring prefix.

            >>> client.list_daemon_task_definitions(family_prefix='monitoring')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_task_definitions

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_task_definitions.list_daemon_task_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if family is not None:
            input_["family"] = family
        if revision is not None:
            input_["revision"] = revision
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

    def register_daemon_task_definition(
        self,
        family: "capo_ecs.types.string.String",
        container_definitions: "capo_ecs.types.daemon_container_definition_list.DaemonContainerDefinitionList",
        *,
        config_overrides: Optional[ECSClientConfig] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        volumes: Optional["capo_ecs.types.daemon_volume_list.DaemonVolumeList"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        pid_mode: Optional["capo_ecs.types.daemon_pid_mode.DaemonPidMode"] = None,
        ipc_mode: Optional["capo_ecs.types.daemon_ipc_mode.DaemonIpcMode"] = None,
    ) -> "capo_ecs.types.register_daemon_task_definition_response.RegisterDaemonTaskDefinitionResponse":
        """<p>Registers a new daemon task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-task-definitions.html">Daemon task definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents such as security monitoring, telemetry, and logging across your Amazon ECS infrastructure.</p> <p>Each time you call <code>RegisterDaemonTaskDefinition</code>, a new revision of the daemon task definition is created. You can't modify a revision after you register it.</p>

        Args:
            family: <p>You must specify a <code>family</code> for a daemon task definition. This family is used as a name for your daemon task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            task_role_arn: <p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this daemon task can assume. All containers in this daemon task are granted the permissions that are specified in this role.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. The task execution role is required for daemon tasks that pull container images from Amazon ECR or send container logs to CloudWatch.</p>
            container_definitions: <p>A list of container definitions in JSON format that describe the containers that make up your daemon task.</p>
            cpu: <p>The number of CPU units used by the daemon task. It can be expressed as an integer using CPU units (for example, <code>1024</code>).</p>
            memory: <p>The amount of memory (in MiB) used by the daemon task. It can be expressed as an integer using MiB (for example, <code>1024</code>).</p>
            volumes: <p>A list of volume definitions in JSON format that containers in your daemon task can use.</p>
            tags: <p>The metadata that you apply to the daemon task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            pid_mode: <p>The PID namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use <code>pidMode: "host"</code> or other daemons that use <code>pidMode: "shared"</code>.</p>
            ipc_mode: <p>The IPC namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use <code>ipcMode: "host"</code> or other daemons that use <code>ipcMode: "shared"</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register a daemon task definition
            This example registers a daemon task definition in the monitoring-agent family with a single container that runs a CloudWatch agent.

            >>> client.register_daemon_task_definition(family='monitoring-agent', container_definitions=[{'name': 'cloudwatch-agent', 'image': 'public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest', 'memory': 256, 'cpu': 128, 'essential': True, 'logConfiguration': {'logDriver': 'awslogs', 'options': {'awslogs-group': '/ecs/daemon/monitoring-agent', 'awslogs-region': 'us-east-1', 'awslogs-stream-prefix': 'ecs'}}, 'environment': [{'name': 'USE_DEFAULT_CONFIG', 'value': 'true'}]}], cpu='128', memory='256', execution_role_arn='arn:aws:iam::123456789012:role/ecsTaskExecutionRole', task_role_arn='arn:aws:iam::123456789012:role/ecsDaemonTaskRole')
        """

        def _handler(
            req: "OperationRequest[capo_ecs.types.register_daemon_task_definition_request.RegisterDaemonTaskDefinitionRequest]",
        ) -> OperationResponse[
            "capo_ecs.types.register_daemon_task_definition_response.RegisterDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_daemon_task_definition

            output, http_response = (
                capo_ecs._operations.amazon_ec2_container_service_v20141113.register_daemon_task_definition.register_daemon_task_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.register_daemon_task_definition_request.RegisterDaemonTaskDefinitionRequest = {
            "family": family,
            "container_definitions": container_definitions,
        }
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if volumes is not None:
            input_["volumes"] = volumes
        if tags is not None:
            input_["tags"] = tags
        if pid_mode is not None:
            input_["pid_mode"] = pid_mode
        if ipc_mode is not None:
            input_["ipc_mode"] = ipc_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDaemonTaskDefinitionResource:
    def __init__(self, service: AsyncECSClient) -> None:
        self._service = service

    async def delete_daemon_task_definition(
        self,
        daemon_task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse":
        """<p>Deletes the specified daemon task definition. After a daemon task definition is deleted, no new daemons can be created using this definition. Existing daemons that reference the deleted daemon task definition continue to run.</p> <p>A daemon task definition must be in an <code>ACTIVE</code> state to be deleted.</p>

        Args:
            daemon_task_definition: <p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the daemon task definition to delete.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a daemon task definition
            This example deletes the first revision of the monitoring-agent daemon task definition.

            >>> await client.delete_daemon_task_definition(daemon_task_definition='monitoring-agent:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.delete_daemon_task_definition.async_delete_daemon_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest = {
            "daemon_task_definition": daemon_task_definition
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_daemon_task_definition(
        self,
        daemon_task_definition: "capo_ecs.types.string.String",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
    ) -> "capo_ecs.types.describe_daemon_task_definition_response.DescribeDaemonTaskDefinitionResponse":
        """<p>Describes a daemon task definition. You can specify a <code>family</code> and <code>revision</code> to find information about a specific daemon task definition, or you can simply specify the family to find the latest <code>ACTIVE</code> revision in that family.</p>

        Args:
            daemon_task_definition: <p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the daemon task definition to describe.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a daemon task definition
            This example describes the first revision of the monitoring-agent daemon task definition.

            >>> await client.describe_daemon_task_definition(daemon_task_definition='monitoring-agent:1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.describe_daemon_task_definition_request.DescribeDaemonTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.describe_daemon_task_definition_response.DescribeDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.describe_daemon_task_definition.async_describe_daemon_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.describe_daemon_task_definition_request.DescribeDaemonTaskDefinitionRequest = {
            "daemon_task_definition": daemon_task_definition
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_daemon_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        family_prefix: Optional["capo_ecs.types.string.String"] = None,
        family: Optional["capo_ecs.types.string.String"] = None,
        revision: Optional[
            "capo_ecs.types.daemon_task_definition_revision_filter.DaemonTaskDefinitionRevisionFilter"
        ] = None,
        status: Optional[
            "capo_ecs.types.daemon_task_definition_status_filter.DaemonTaskDefinitionStatusFilter"
        ] = None,
        sort: Optional["capo_ecs.types.sort_order.SortOrder"] = None,
        next_token: Optional["capo_ecs.types.string.String"] = None,
        max_results: Optional["capo_ecs.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse":
        """<p>Returns a list of daemon task definitions that are registered to your account. You can filter the results by family name, status, or both to find daemon task definitions that match your criteria.</p>

        Args:
            family_prefix: <p>The full family name to filter the <code>ListDaemonTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed daemon task definitions to daemon task definition families that start with the <code>familyPrefix</code> string.</p>
            family: <p>The exact name of the daemon task definition family to filter results with.</p>
            revision: <p>The revision filter to apply. Specify <code>LAST_REGISTERED</code> to return only the last registered revision for each daemon task definition family.</p>
            status: <p>The daemon task definition status to filter the <code>ListDaemonTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> daemon task definitions are listed. If you set this parameter to <code>DELETE_IN_PROGRESS</code>, only daemon task definitions that are in the process of being deleted are listed. If you set this parameter to <code>ALL</code>, all daemon task definitions are listed regardless of status.</p>
            sort: <p>The order to sort the results. Valid values are <code>ASC</code> and <code>DESC</code>. By default (<code>ASC</code>), daemon task definitions are listed in ascending order by family name and revision number.</p>
            next_token: <p>The <code>nextToken</code> value returned from a <code>ListDaemonTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of daemon task definition results that <code>ListDaemonTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListDaemonTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list daemon task definitions
            This example lists all daemon task definitions in your account that start with the monitoring prefix.

            >>> await client.list_daemon_task_definitions(family_prefix='monitoring')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_task_definitions

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.list_daemon_task_definitions.async_list_daemon_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest = {}
        if family_prefix is not None:
            input_["family_prefix"] = family_prefix
        if family is not None:
            input_["family"] = family
        if revision is not None:
            input_["revision"] = revision
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

    async def register_daemon_task_definition(
        self,
        family: "capo_ecs.types.string.String",
        container_definitions: "capo_ecs.types.daemon_container_definition_list.DaemonContainerDefinitionList",
        *,
        config_overrides: Optional[AsyncECSClientConfig] = None,
        task_role_arn: Optional["capo_ecs.types.string.String"] = None,
        execution_role_arn: Optional["capo_ecs.types.string.String"] = None,
        cpu: Optional["capo_ecs.types.string.String"] = None,
        memory: Optional["capo_ecs.types.string.String"] = None,
        volumes: Optional["capo_ecs.types.daemon_volume_list.DaemonVolumeList"] = None,
        tags: Optional["capo_ecs.types.tags.Tags"] = None,
        pid_mode: Optional["capo_ecs.types.daemon_pid_mode.DaemonPidMode"] = None,
        ipc_mode: Optional["capo_ecs.types.daemon_ipc_mode.DaemonIpcMode"] = None,
    ) -> "capo_ecs.types.register_daemon_task_definition_response.RegisterDaemonTaskDefinitionResponse":
        """<p>Registers a new daemon task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/daemon-task-definitions.html">Daemon task definitions</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>A daemon task definition is a template that describes the containers that form a daemon. Daemons deploy cross-cutting software agents such as security monitoring, telemetry, and logging across your Amazon ECS infrastructure.</p> <p>Each time you call <code>RegisterDaemonTaskDefinition</code>, a new revision of the daemon task definition is created. You can't modify a revision after you register it.</p>

        Args:
            family: <p>You must specify a <code>family</code> for a daemon task definition. This family is used as a name for your daemon task definition. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.</p>
            task_role_arn: <p>The short name or full Amazon Resource Name (ARN) of the IAM role that containers in this daemon task can assume. All containers in this daemon task are granted the permissions that are specified in this role.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make Amazon Web Services API calls on your behalf. The task execution role is required for daemon tasks that pull container images from Amazon ECR or send container logs to CloudWatch.</p>
            container_definitions: <p>A list of container definitions in JSON format that describe the containers that make up your daemon task.</p>
            cpu: <p>The number of CPU units used by the daemon task. It can be expressed as an integer using CPU units (for example, <code>1024</code>).</p>
            memory: <p>The amount of memory (in MiB) used by the daemon task. It can be expressed as an integer using MiB (for example, <code>1024</code>).</p>
            volumes: <p>A list of volume definitions in JSON format that containers in your daemon task can use.</p>
            tags: <p>The metadata that you apply to the daemon task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>
            pid_mode: <p>The PID namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own PID namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host PID namespace, making it accessible to non-daemon tasks that use <code>pidMode: "host"</code> or other daemons that use <code>pidMode: "shared"</code>.</p>
            ipc_mode: <p>The IPC namespace mode for the daemon. The valid values are <code>none</code> and <code>shared</code>. The default is <code>none</code>.</p> <p>If <code>none</code> is specified or no value is provided, the daemon runs with its own IPC namespace, isolated from other tasks. If <code>shared</code> is specified, the daemon joins the host IPC namespace, making it accessible to non-daemon tasks that use <code>ipcMode: "host"</code> or other daemons that use <code>ipcMode: "shared"</code>.</p>

        Raises:
            capo_ecs.errors.access_denied_exception.AccessDeniedException: <p>You don't have authorization to perform the requested action.</p>
            capo_ecs.errors.client_exception.ClientException: <p>These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.</p>
            capo_ecs.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter isn't valid. Review the available parameters for the API request.</p> <p>For more information about service event errors, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html">Amazon ECS service event messages</a>. </p>
            capo_ecs.errors.limit_exceeded_exception.LimitExceededException: <p>The limit for the resource was exceeded.</p>
            capo_ecs.errors.server_exception.ServerException: <p>These errors are usually caused by a server issue.</p>
            capo_ecs.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register a daemon task definition
            This example registers a daemon task definition in the monitoring-agent family with a single container that runs a CloudWatch agent.

            >>> await client.register_daemon_task_definition(family='monitoring-agent', container_definitions=[{'name': 'cloudwatch-agent', 'image': 'public.ecr.aws/cloudwatch-agent/cloudwatch-agent:latest', 'memory': 256, 'cpu': 128, 'essential': True, 'logConfiguration': {'logDriver': 'awslogs', 'options': {'awslogs-group': '/ecs/daemon/monitoring-agent', 'awslogs-region': 'us-east-1', 'awslogs-stream-prefix': 'ecs'}}, 'environment': [{'name': 'USE_DEFAULT_CONFIG', 'value': 'true'}]}], cpu='128', memory='256', execution_role_arn='arn:aws:iam::123456789012:role/ecsTaskExecutionRole', task_role_arn='arn:aws:iam::123456789012:role/ecsDaemonTaskRole')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ecs.types.register_daemon_task_definition_request.RegisterDaemonTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ecs.types.register_daemon_task_definition_response.RegisterDaemonTaskDefinitionResponse"
        ]:
            import capo_ecs._operations.amazon_ec2_container_service_v20141113.register_daemon_task_definition

            (
                output,
                http_response,
            ) = await capo_ecs._operations.amazon_ec2_container_service_v20141113.register_daemon_task_definition.async_register_daemon_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_ecs.types.register_daemon_task_definition_request.RegisterDaemonTaskDefinitionRequest = {
            "family": family,
            "container_definitions": container_definitions,
        }
        if task_role_arn is not None:
            input_["task_role_arn"] = task_role_arn
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if cpu is not None:
            input_["cpu"] = cpu
        if memory is not None:
            input_["memory"] = memory
        if volumes is not None:
            input_["volumes"] = volumes
        if tags is not None:
            input_["tags"] = tags
        if pid_mode is not None:
            input_["pid_mode"] = pid_mode
        if ipc_mode is not None:
            input_["ipc_mode"] = ipc_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
