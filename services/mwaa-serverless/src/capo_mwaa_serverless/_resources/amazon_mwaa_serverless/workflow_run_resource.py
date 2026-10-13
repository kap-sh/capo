from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

from capo_mwaa_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.get_workflow_run_request
    import capo_mwaa_serverless.types.get_workflow_run_response
    import capo_mwaa_serverless.types.id_string
    import capo_mwaa_serverless.types.idempotency_token_string
    import capo_mwaa_serverless.types.list_workflow_runs_request
    import capo_mwaa_serverless.types.list_workflow_runs_response
    import capo_mwaa_serverless.types.object_map
    import capo_mwaa_serverless.types.start_workflow_run_request
    import capo_mwaa_serverless.types.start_workflow_run_response
    import capo_mwaa_serverless.types.stop_workflow_run_request
    import capo_mwaa_serverless.types.stop_workflow_run_response
    import capo_mwaa_serverless.types.version_id
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_run_summary
    from capo_mwaa_serverless._services.async_mwaa_serverless import (
        AsyncMWAAServerlessClient,
        AsyncMWAAServerlessClientConfig,
    )
    from capo_mwaa_serverless._services.mwaa_serverless import (
        MWAAServerlessClient,
        MWAAServerlessClientConfig,
    )


class WorkflowRunResource:
    def __init__(self, service: MWAAServerlessClient) -> None:
        self._service = service

    def create(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        client_token: Optional[
            "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        override_parameters: Optional[
            "capo_mwaa_serverless.types.object_map.ObjectMap"
        ] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "capo_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Starts a new execution of a workflow. This operation creates a workflow run that executes the tasks that are defined in the workflow. Amazon Managed Workflows for Apache Airflow Serverless schedules the workflow execution across its managed Airflow environment, automatically scaling ECS worker tasks based on the workload. The service handles task isolation, dependency resolution, and provides comprehensive monitoring and logging throughout the execution lifecycle.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to run.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.</p>
            override_parameters: <p>Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.</p>
            workflow_version: <p>Optional. The specific version of the workflow to execute. If not specified, the latest version is used.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run.start_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest",
        ) -> dict[str, Any]:
            import capo_mwaa_serverless.types.start_workflow_run_request

            return (
                capo_mwaa_serverless.types.start_workflow_run_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartWorkflowRun", redact_input=_redact_input),
        )
        input_: capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest = {
            "workflow_arn": workflow_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if override_parameters is not None:
            input_["override_parameters"] = override_parameters
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves detailed information about a specific workflow run, including its status, execution details, and task instances.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run to retrieve.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse",
        ) -> dict[str, Any]:
            import capo_mwaa_serverless.types.get_workflow_run_response

            return (
                capo_mwaa_serverless.types.get_workflow_run_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetWorkflowRun", redact_output=_redact_output),
        )
        input_: capo_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
    ) -> (
        "capo_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
    ):
        """<p>Stops a running workflow execution. This operation terminates all running tasks and prevents new tasks from starting. Amazon Managed Workflows for Apache Airflow Serverless gracefully shuts down the workflow execution by stopping task scheduling and terminating active ECS worker containers. The operation transitions the workflow run to a <code>STOPPING</code> state and then to <code>STOPPED</code> once all cleanup is complete. In-flight tasks may complete or be terminated depending on their current execution state.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run you want to stop.</p>
            run_id: <p>The unique identifier of the workflow run to stop.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run.stop_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopWorkflowRun")
        )
        input_: capo_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
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
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "capo_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all runs for a specified workflow, with optional pagination and filtering support.</p>

        Args:
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowRuns</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.</p>
            workflow_version: <p>Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowRuns")
        )
        input_: capo_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "workflow_arn": workflow_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkflowRunResource:
    def __init__(self, service: AsyncMWAAServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        client_token: Optional[
            "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        override_parameters: Optional[
            "capo_mwaa_serverless.types.object_map.ObjectMap"
        ] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "capo_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Starts a new execution of a workflow. This operation creates a workflow run that executes the tasks that are defined in the workflow. Amazon Managed Workflows for Apache Airflow Serverless schedules the workflow execution across its managed Airflow environment, automatically scaling ECS worker tasks based on the workload. The service handles task isolation, dependency resolution, and provides comprehensive monitoring and logging throughout the execution lifecycle.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to run.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow run requests.</p>
            override_parameters: <p>Optional parameters to override default workflow parameters for this specific run. These parameters are passed to the workflow during execution and can be used to customize behavior without modifying the workflow definition. Parameters are made available as environment variables to tasks and you can reference them within the YAML workflow definition using standard parameter substitution syntax.</p>
            workflow_version: <p>Optional. The specific version of the workflow to execute. If not specified, the latest version is used.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.start_workflow_run.async_start_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest",
        ) -> dict[str, Any]:
            import capo_mwaa_serverless.types.start_workflow_run_request

            return (
                capo_mwaa_serverless.types.start_workflow_run_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartWorkflowRun", redact_input=_redact_input),
        )
        input_: capo_mwaa_serverless.types.start_workflow_run_request.StartWorkflowRunRequest = {
            "workflow_arn": workflow_arn
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if override_parameters is not None:
            input_["override_parameters"] = override_parameters
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves detailed information about a specific workflow run, including its status, execution details, and task instances.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run.</p>
            run_id: <p>The unique identifier of the workflow run to retrieve.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow_run.async_get_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mwaa_serverless.types.get_workflow_run_response.GetWorkflowRunResponse",
        ) -> dict[str, Any]:
            import capo_mwaa_serverless.types.get_workflow_run_response

            return (
                capo_mwaa_serverless.types.get_workflow_run_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetWorkflowRun", redact_output=_redact_output),
        )
        input_: capo_mwaa_serverless.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        run_id: "capo_mwaa_serverless.types.id_string.IdString",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
    ) -> (
        "capo_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
    ):
        """<p>Stops a running workflow execution. This operation terminates all running tasks and prevents new tasks from starting. Amazon Managed Workflows for Apache Airflow Serverless gracefully shuts down the workflow execution by stopping task scheduling and terminating active ECS worker containers. The operation transitions the workflow run to a <code>STOPPING</code> state and then to <code>STOPPED</code> once all cleanup is complete. In-flight tasks may complete or be terminated depending on their current execution state.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow that contains the run you want to stop.</p>
            run_id: <p>The unique identifier of the workflow run to stop.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.stop_workflow_run_response.StopWorkflowRunResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.stop_workflow_run.async_stop_workflow_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopWorkflowRun")
        )
        input_: capo_mwaa_serverless.types.stop_workflow_run_request.StopWorkflowRunRequest = {
            "workflow_arn": workflow_arn,
            "run_id": run_id,
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
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.version_id.VersionId"
        ] = None,
    ) -> "capo_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all runs for a specified workflow, with optional pagination and filtering support.</p>

        Args:
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowRuns</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want a list of runs.</p>
            workflow_version: <p>Optional. The specific version of the workflow for which you want a list of runs. If not specified, runs for all versions are returned.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_runs.async_list_workflow_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowRuns")
        )
        input_: capo_mwaa_serverless.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "workflow_arn": workflow_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
