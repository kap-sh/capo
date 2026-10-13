from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_snow_device_management._auth._signers
import capo_snow_device_management._auth._sigv4
from capo_snow_device_management._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_snow_device_management.types.cancel_task_input
    import capo_snow_device_management.types.cancel_task_output
    import capo_snow_device_management.types.command
    import capo_snow_device_management.types.create_task_input
    import capo_snow_device_management.types.create_task_output
    import capo_snow_device_management.types.describe_task_input
    import capo_snow_device_management.types.describe_task_output
    import capo_snow_device_management.types.idempotency_token
    import capo_snow_device_management.types.list_tasks_input
    import capo_snow_device_management.types.list_tasks_output
    import capo_snow_device_management.types.max_results
    import capo_snow_device_management.types.next_token
    import capo_snow_device_management.types.tag_map
    import capo_snow_device_management.types.target_list
    import capo_snow_device_management.types.task_description_string
    import capo_snow_device_management.types.task_id
    import capo_snow_device_management.types.task_state
    import capo_snow_device_management.types.task_summary
    from capo_snow_device_management._services.async_snow_device_management import (
        AsyncSnowDeviceManagementClient,
        AsyncSnowDeviceManagementClientConfig,
    )
    from capo_snow_device_management._services.snow_device_management import (
        SnowDeviceManagementClient,
        SnowDeviceManagementClientConfig,
    )


class Task:
    def __init__(self, service: SnowDeviceManagementClient) -> None:
        self._service = service

    def create(
        self,
        targets: "capo_snow_device_management.types.target_list.TargetList",
        command: "capo_snow_device_management.types.command.Command",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        description: Optional[
            "capo_snow_device_management.types.task_description_string.TaskDescriptionString"
        ] = None,
        tags: Optional["capo_snow_device_management.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_snow_device_management.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_snow_device_management.types.create_task_output.CreateTaskOutput":
        """<p>Instructs one or more devices to start a task, such as unlocking or rebooting.</p>

        Args:
            targets: <p>A list of managed device IDs.</p>
            command: <p>The task to be performed. Only one task is executed on a device at a time.</p>
            description: <p>A description of the task and its targets.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>
            client_token: <p>A token ensuring that the action is called only once with the specified details.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.create_task_input.CreateTaskInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.create_task_output.CreateTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.create_task

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.create_task.create_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateTask")
        )
        input_: capo_snow_device_management.types.create_task_input.CreateTaskInput = {
            "targets": targets,
            "command": command,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_task_output.DescribeTaskOutput":
        """<p>Checks the metadata for a given task on a device. </p>

        Args:
            task_id: <p>The ID of the task to be described.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_task_input.DescribeTaskInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_task_output.DescribeTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_task

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_task.describe_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeTask")
        )
        input_: capo_snow_device_management.types.describe_task_input.DescribeTaskInput = {
            "task_id": task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        state: Optional[
            "capo_snow_device_management.types.task_state.TaskState"
        ] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_tasks_output.ListTasksOutput":
        """<p>Returns a list of tasks that can be filtered by state.</p>

        Args:
            state: <p>A structure used to filter the list of tasks.</p>
            max_results: <p>The maximum number of tasks per page.</p>
            next_token: <p>A pagination token to continue to the next page of tasks.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_tasks_input.ListTasksInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_tasks_output.ListTasksOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_tasks

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_tasks.list_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTasks")
        )
        input_: capo_snow_device_management.types.list_tasks_input.ListTasksInput = {}
        if state is not None:
            input_["state"] = state
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

    def cancel_task(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.cancel_task_output.CancelTaskOutput":
        """<p>Sends a cancel request for a specified task. You can cancel a task only if it's still in a <code>QUEUED</code> state. Tasks that are already running can't be cancelled.</p> <note> <p>A task might still run if it's processed from the queue before the <code>CancelTask</code> operation changes the task's state.</p> </note>

        Args:
            task_id: <p>The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the <code>ListTasks</code> operation.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.cancel_task_input.CancelTaskInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.cancel_task_output.CancelTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.cancel_task

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.cancel_task.cancel_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelTask")
        )
        input_: capo_snow_device_management.types.cancel_task_input.CancelTaskInput = {
            "task_id": task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTask:
    def __init__(self, service: AsyncSnowDeviceManagementClient) -> None:
        self._service = service

    async def create(
        self,
        targets: "capo_snow_device_management.types.target_list.TargetList",
        command: "capo_snow_device_management.types.command.Command",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        description: Optional[
            "capo_snow_device_management.types.task_description_string.TaskDescriptionString"
        ] = None,
        tags: Optional["capo_snow_device_management.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_snow_device_management.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_snow_device_management.types.create_task_output.CreateTaskOutput":
        """<p>Instructs one or more devices to start a task, such as unlocking or rebooting.</p>

        Args:
            targets: <p>A list of managed device IDs.</p>
            command: <p>The task to be performed. Only one task is executed on a device at a time.</p>
            description: <p>A description of the task and its targets.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>
            client_token: <p>A token ensuring that the action is called only once with the specified details.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.create_task_input.CreateTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.create_task_output.CreateTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.create_task

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.create_task.async_create_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateTask")
        )
        input_: capo_snow_device_management.types.create_task_input.CreateTaskInput = {
            "targets": targets,
            "command": command,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_task_output.DescribeTaskOutput":
        """<p>Checks the metadata for a given task on a device. </p>

        Args:
            task_id: <p>The ID of the task to be described.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.describe_task_input.DescribeTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.describe_task_output.DescribeTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_task

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.describe_task.async_describe_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeTask")
        )
        input_: capo_snow_device_management.types.describe_task_input.DescribeTaskInput = {
            "task_id": task_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        state: Optional[
            "capo_snow_device_management.types.task_state.TaskState"
        ] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_tasks_output.ListTasksOutput":
        """<p>Returns a list of tasks that can be filtered by state.</p>

        Args:
            state: <p>A structure used to filter the list of tasks.</p>
            max_results: <p>The maximum number of tasks per page.</p>
            next_token: <p>A pagination token to continue to the next page of tasks.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.list_tasks_input.ListTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.list_tasks_output.ListTasksOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_tasks

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.list_tasks.async_list_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTasks")
        )
        input_: capo_snow_device_management.types.list_tasks_input.ListTasksInput = {}
        if state is not None:
            input_["state"] = state
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

    async def cancel_task(
        self,
        task_id: "capo_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.cancel_task_output.CancelTaskOutput":
        """<p>Sends a cancel request for a specified task. You can cancel a task only if it's still in a <code>QUEUED</code> state. Tasks that are already running can't be cancelled.</p> <note> <p>A task might still run if it's processed from the queue before the <code>CancelTask</code> operation changes the task's state.</p> </note>

        Args:
            task_id: <p>The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the <code>ListTasks</code> operation.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.cancel_task_input.CancelTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.cancel_task_output.CancelTaskOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.cancel_task

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.cancel_task.async_cancel_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelTask")
        )
        input_: capo_snow_device_management.types.cancel_task_input.CancelTaskInput = {
            "task_id": task_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
