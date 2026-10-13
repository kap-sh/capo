from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_data_automation._auth._signers
import capo_bedrock_data_automation._auth._sigv4
from capo_bedrock_data_automation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary
    import capo_bedrock_data_automation.types.entity_type
    import capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request
    import capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response
    import capo_bedrock_data_automation.types.input_configuration
    import capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request
    import capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type
    import capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request
    import capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response
    import capo_bedrock_data_automation.types.max_results
    import capo_bedrock_data_automation.types.next_token
    import capo_bedrock_data_automation.types.notification_configuration
    import capo_bedrock_data_automation.types.output_configuration
    import capo_bedrock_data_automation.types.tag_list
    from capo_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from capo_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class DataAutomationLibraryIngestionJobResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        input_configuration: "capo_bedrock_data_automation.types.input_configuration.InputConfiguration",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        operation_type: "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType",
        output_configuration: "capo_bedrock_data_automation.types.output_configuration.OutputConfiguration",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        notification_configuration: Optional[
            "capo_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse":
        """Async API: Invoke data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            client_token: Idempotency token
            input_configuration: Input configuration of DataAutomationLibraryIngestionJob request
            entity_type: The entity type for which DataAutomationLibraryIngestionJob is being run
            operation_type: The operation to be performed by DataAutomationLibraryIngestionJob
            output_configuration: Output configuration of DataAutomationLibraryIngestionJob
            notification_configuration: Notification configuration.
            tags: List of tags

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job.invoke_data_automation_library_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request

            return capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "InvokeDataAutomationLibraryIngestionJob", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest = {
            "library_arn": library_arn,
            "input_configuration": input_configuration,
            "entity_type": entity_type,
            "operation_type": operation_type,
            "output_configuration": output_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        job_arn: "capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse":
        """API used to get status of data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            job_arn: ARN of the DataAutomationLibraryIngestionJob

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job.get_data_automation_library_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDataAutomationLibraryIngestionJob")
        )
        input_: capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest = {
            "library_arn": library_arn,
            "job_arn": job_arn,
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
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse":
        """Lists all data automation library ingestion jobs

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            next_token: Pagination token for retrieving the next set of results

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs

            output, http_response = (
                capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs.list_data_automation_library_ingestion_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDataAutomationLibraryIngestionJobs")
        )
        input_: capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest = {
            "library_arn": library_arn
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


class AsyncDataAutomationLibraryIngestionJobResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        input_configuration: "capo_bedrock_data_automation.types.input_configuration.InputConfiguration",
        entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType",
        operation_type: "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType",
        output_configuration: "capo_bedrock_data_automation.types.output_configuration.OutputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_data_automation.types.client_token.ClientToken"
        ] = None,
        notification_configuration: Optional[
            "capo_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse":
        """Async API: Invoke data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            client_token: Idempotency token
            input_configuration: Input configuration of DataAutomationLibraryIngestionJob request
            entity_type: The entity type for which DataAutomationLibraryIngestionJob is being run
            operation_type: The operation to be performed by DataAutomationLibraryIngestionJob
            output_configuration: Output configuration of DataAutomationLibraryIngestionJob
            notification_configuration: Notification configuration.
            tags: List of tags

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.conflict_exception.ConflictException: This exception is thrown when there is a conflict performing an operation
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception is thrown when a request is made beyond the service quota
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_response.InvokeDataAutomationLibraryIngestionJobResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_data_automation_library_ingestion_job.async_invoke_data_automation_library_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request

            return capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "InvokeDataAutomationLibraryIngestionJob", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_data_automation.types.invoke_data_automation_library_ingestion_job_request.InvokeDataAutomationLibraryIngestionJobRequest = {
            "library_arn": library_arn,
            "input_configuration": input_configuration,
            "entity_type": entity_type,
            "operation_type": operation_type,
            "output_configuration": output_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        job_arn: "capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse":
        """API used to get status of data automation library ingestion job

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            job_arn: ARN of the DataAutomationLibraryIngestionJob

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_response.GetDataAutomationLibraryIngestionJobResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_data_automation_library_ingestion_job.async_get_data_automation_library_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDataAutomationLibraryIngestionJob")
        )
        input_: capo_bedrock_data_automation.types.get_data_automation_library_ingestion_job_request.GetDataAutomationLibraryIngestionJobRequest = {
            "library_arn": library_arn,
            "job_arn": job_arn,
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
        library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_data_automation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_data_automation.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse":
        """Lists all data automation library ingestion jobs

        Args:
            library_arn: ARN generated at the server side when a DataAutomationLibrary is created
            next_token: Pagination token for retrieving the next set of results

        Raises:
            capo_bedrock_data_automation.errors.access_denied_exception.AccessDeniedException: This exception is thrown when a request is denied per access permissions
            capo_bedrock_data_automation.errors.internal_server_exception.InternalServerException: This exception is thrown if there was an unexpected error during processing of request
            capo_bedrock_data_automation.errors.resource_not_found_exception.ResourceNotFoundException: This exception is thrown when a resource referenced by the operation does not exist
            capo_bedrock_data_automation.errors.throttling_exception.ThrottlingException: This exception is thrown when the number of requests exceeds the limit
            capo_bedrock_data_automation.errors.validation_exception.ValidationException: This exception is thrown when the request's input validation fails
            capo_bedrock_data_automation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_response.ListDataAutomationLibraryIngestionJobsResponse"
        ]:
            import capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.list_data_automation_library_ingestion_jobs.async_list_data_automation_library_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDataAutomationLibraryIngestionJobs")
        )
        input_: capo_bedrock_data_automation.types.list_data_automation_library_ingestion_jobs_request.ListDataAutomationLibraryIngestionJobsRequest = {
            "library_arn": library_arn
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
