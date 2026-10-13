from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_braket._auth._signers
import capo_braket._auth._sigv4
from capo_braket._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_braket.types.associations
    import capo_braket.types.cancel_quantum_task_request
    import capo_braket.types.cancel_quantum_task_response
    import capo_braket.types.create_quantum_task_request
    import capo_braket.types.create_quantum_task_response
    import capo_braket.types.device_arn
    import capo_braket.types.experimental_capabilities
    import capo_braket.types.get_quantum_task_request
    import capo_braket.types.get_quantum_task_response
    import capo_braket.types.job_token
    import capo_braket.types.json_value
    import capo_braket.types.quantum_task_additional_attribute_names_list
    import capo_braket.types.quantum_task_arn
    import capo_braket.types.quantum_task_summary
    import capo_braket.types.search_quantum_tasks_filter_list
    import capo_braket.types.search_quantum_tasks_request
    import capo_braket.types.search_quantum_tasks_response
    import capo_braket.types.string64
    import capo_braket.types.tags_map
    from capo_braket._services.async_braket import (
        AsyncBraketClient,
        AsyncBraketClientConfig,
    )
    from capo_braket._services.braket import BraketClient, BraketClientConfig


class QuantumTaskResource:
    def __init__(self, service: BraketClient) -> None:
        self._service = service

    def create(
        self,
        client_token: "capo_braket.types.string64.String64",
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        shots: int,
        output_s3_bucket: str,
        output_s3_key_prefix: str,
        action: "capo_braket.types.json_value.JsonValue",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        device_parameters: Optional["capo_braket.types.json_value.JsonValue"] = None,
        tags: Optional["capo_braket.types.tags_map.TagsMap"] = None,
        job_token: Optional["capo_braket.types.job_token.JobToken"] = None,
        associations: Optional["capo_braket.types.associations.Associations"] = None,
        experimental_capabilities: Optional[
            "capo_braket.types.experimental_capabilities.ExperimentalCapabilities"
        ] = None,
    ) -> "capo_braket.types.create_quantum_task_response.CreateQuantumTaskResponse":
        """<p>Creates a quantum task.</p>

        Args:
            client_token: <p>The client token associated with the request.</p>
            device_arn: <p>The ARN of the device to run the quantum task on.</p>
            device_parameters: <p>The parameters for the device to run the quantum task on.</p>
            shots: <p>The number of shots to use for the quantum task.</p>
            output_s3_bucket: <p>The S3 bucket to store quantum task result files in.</p>
            output_s3_key_prefix: <p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>
            action: <p>The action associated with the quantum task.</p>
            tags: <p>Tags to be added to the quantum task you're creating.</p>
            job_token: <p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>
            associations: <p>The list of Amazon Braket resources associated with the quantum task.</p>
            experimental_capabilities: <p>Enable experimental capabilities for the quantum task.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.device_offline_exception.DeviceOfflineException: <p>The specified device is currently offline.</p>
            capo_braket.errors.device_retired_exception.DeviceRetiredException: <p>The specified device has been retired.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_braket.types.create_quantum_task_request.CreateQuantumTaskRequest]",
        ) -> OperationResponse[
            "capo_braket.types.create_quantum_task_response.CreateQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.create_quantum_task

            output, http_response = (
                capo_braket._operations.braket.create_quantum_task.create_quantum_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateQuantumTask")
        )
        input_: capo_braket.types.create_quantum_task_request.CreateQuantumTaskRequest = {
            "client_token": client_token,
            "device_arn": device_arn,
            "shots": shots,
            "output_s3_bucket": output_s3_bucket,
            "output_s3_key_prefix": output_s3_key_prefix,
            "action": action,
        }
        if device_parameters is not None:
            input_["device_parameters"] = device_parameters
        if tags is not None:
            input_["tags"] = tags
        if job_token is not None:
            input_["job_token"] = job_token
        if associations is not None:
            input_["associations"] = associations
        if experimental_capabilities is not None:
            input_["experimental_capabilities"] = experimental_capabilities

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        additional_attribute_names: Optional[
            "capo_braket.types.quantum_task_additional_attribute_names_list.QuantumTaskAdditionalAttributeNamesList"
        ] = None,
    ) -> "capo_braket.types.get_quantum_task_response.GetQuantumTaskResponse":
        """<p>Retrieves the specified quantum task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_braket.types.get_quantum_task_request.GetQuantumTaskRequest]",
        ) -> OperationResponse[
            "capo_braket.types.get_quantum_task_response.GetQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.get_quantum_task

            output, http_response = (
                capo_braket._operations.braket.get_quantum_task.get_quantum_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQuantumTask")
        )
        input_: capo_braket.types.get_quantum_task_request.GetQuantumTaskRequest = {
            "quantum_task_arn": quantum_task_arn
        }
        if additional_attribute_names is not None:
            input_["additional_attribute_names"] = additional_attribute_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn",
        client_token: "capo_braket.types.string64.String64",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "capo_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse":
        """<p>Cancels the specified task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to cancel.</p>
            client_token: <p>The client token associated with the cancellation request.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest]",
        ) -> OperationResponse[
            "capo_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.cancel_quantum_task

            output, http_response = (
                capo_braket._operations.braket.cancel_quantum_task.cancel_quantum_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelQuantumTask")
        )
        input_: capo_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest = {
            "quantum_task_arn": quantum_task_arn,
            "client_token": client_token,
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
        filters: "capo_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse":
        """<p>Searches for tasks that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>Maximum number of results to return in the response.</p>
            filters: <p>Array of <code>SearchQuantumTasksFilter</code> objects to use when searching for quantum tasks.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest]",
        ) -> OperationResponse[
            "capo_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
        ]:
            import capo_braket._operations.braket.search_quantum_tasks

            output, http_response = (
                capo_braket._operations.braket.search_quantum_tasks.search_quantum_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SearchQuantumTasks")
        )
        input_: capo_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest = {
            "filters": filters
        }
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


class AsyncQuantumTaskResource:
    def __init__(self, service: AsyncBraketClient) -> None:
        self._service = service

    async def create(
        self,
        client_token: "capo_braket.types.string64.String64",
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        shots: int,
        output_s3_bucket: str,
        output_s3_key_prefix: str,
        action: "capo_braket.types.json_value.JsonValue",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        device_parameters: Optional["capo_braket.types.json_value.JsonValue"] = None,
        tags: Optional["capo_braket.types.tags_map.TagsMap"] = None,
        job_token: Optional["capo_braket.types.job_token.JobToken"] = None,
        associations: Optional["capo_braket.types.associations.Associations"] = None,
        experimental_capabilities: Optional[
            "capo_braket.types.experimental_capabilities.ExperimentalCapabilities"
        ] = None,
    ) -> "capo_braket.types.create_quantum_task_response.CreateQuantumTaskResponse":
        """<p>Creates a quantum task.</p>

        Args:
            client_token: <p>The client token associated with the request.</p>
            device_arn: <p>The ARN of the device to run the quantum task on.</p>
            device_parameters: <p>The parameters for the device to run the quantum task on.</p>
            shots: <p>The number of shots to use for the quantum task.</p>
            output_s3_bucket: <p>The S3 bucket to store quantum task result files in.</p>
            output_s3_key_prefix: <p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>
            action: <p>The action associated with the quantum task.</p>
            tags: <p>Tags to be added to the quantum task you're creating.</p>
            job_token: <p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>
            associations: <p>The list of Amazon Braket resources associated with the quantum task.</p>
            experimental_capabilities: <p>Enable experimental capabilities for the quantum task.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.device_offline_exception.DeviceOfflineException: <p>The specified device is currently offline.</p>
            capo_braket.errors.device_retired_exception.DeviceRetiredException: <p>The specified device has been retired.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request failed because a service quota is exceeded.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.create_quantum_task_request.CreateQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.create_quantum_task_response.CreateQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.create_quantum_task

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.create_quantum_task.async_create_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateQuantumTask")
        )
        input_: capo_braket.types.create_quantum_task_request.CreateQuantumTaskRequest = {
            "client_token": client_token,
            "device_arn": device_arn,
            "shots": shots,
            "output_s3_bucket": output_s3_bucket,
            "output_s3_key_prefix": output_s3_key_prefix,
            "action": action,
        }
        if device_parameters is not None:
            input_["device_parameters"] = device_parameters
        if tags is not None:
            input_["tags"] = tags
        if job_token is not None:
            input_["job_token"] = job_token
        if associations is not None:
            input_["associations"] = associations
        if experimental_capabilities is not None:
            input_["experimental_capabilities"] = experimental_capabilities

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        additional_attribute_names: Optional[
            "capo_braket.types.quantum_task_additional_attribute_names_list.QuantumTaskAdditionalAttributeNamesList"
        ] = None,
    ) -> "capo_braket.types.get_quantum_task_response.GetQuantumTaskResponse":
        """<p>Retrieves the specified quantum task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to retrieve.</p>
            additional_attribute_names: <p>A list of attributes to return additional information for. Only the QueueInfo additional attribute name is currently supported.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.get_quantum_task_request.GetQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.get_quantum_task_response.GetQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.get_quantum_task

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.get_quantum_task.async_get_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQuantumTask")
        )
        input_: capo_braket.types.get_quantum_task_request.GetQuantumTaskRequest = {
            "quantum_task_arn": quantum_task_arn
        }
        if additional_attribute_names is not None:
            input_["additional_attribute_names"] = additional_attribute_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn",
        client_token: "capo_braket.types.string64.String64",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse":
        """<p>Cancels the specified task.</p>

        Args:
            quantum_task_arn: <p>The ARN of the quantum task to cancel.</p>
            client_token: <p>The client token associated with the cancellation request.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.cancel_quantum_task_response.CancelQuantumTaskResponse"
        ]:
            import capo_braket._operations.braket.cancel_quantum_task

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.cancel_quantum_task.async_cancel_quantum_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelQuantumTask")
        )
        input_: capo_braket.types.cancel_quantum_task_request.CancelQuantumTaskRequest = {
            "quantum_task_arn": quantum_task_arn,
            "client_token": client_token,
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
        filters: "capo_braket.types.search_quantum_tasks_filter_list.SearchQuantumTasksFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse":
        """<p>Searches for tasks that match the specified filter values.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>Maximum number of results to return in the response.</p>
            filters: <p>Array of <code>SearchQuantumTasksFilter</code> objects to use when searching for quantum tasks.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.search_quantum_tasks_response.SearchQuantumTasksResponse"
        ]:
            import capo_braket._operations.braket.search_quantum_tasks

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.search_quantum_tasks.async_search_quantum_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SearchQuantumTasks")
        )
        input_: capo_braket.types.search_quantum_tasks_request.SearchQuantumTasksRequest = {
            "filters": filters
        }
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
