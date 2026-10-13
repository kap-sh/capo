from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    import capo_mwaa_serverless.types.list_workflow_versions_request
    import capo_mwaa_serverless.types.list_workflow_versions_response
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_version_summary
    from capo_mwaa_serverless._services.async_mwaa_serverless import (
        AsyncMWAAServerlessClient,
        AsyncMWAAServerlessClientConfig,
    )
    from capo_mwaa_serverless._services.mwaa_serverless import (
        MWAAServerlessClient,
        MWAAServerlessClientConfig,
    )


class WorkflowVersionResource:
    def __init__(self, service: MWAAServerlessClient) -> None:
        self._service = service

    def list(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse":
        """<p>Lists all versions of a specified workflow, with optional pagination support.</p>

        Args:
            max_results: <p>The maximum number of workflow versions to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowVersions</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want to list versions.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions.list_workflow_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowVersions")
        )
        input_: capo_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest = {
            "workflow_arn": workflow_arn
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


class AsyncWorkflowVersionResource:
    def __init__(self, service: AsyncMWAAServerlessClient) -> None:
        self._service = service

    async def list(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse":
        """<p>Lists all versions of a specified workflow, with optional pagination support.</p>

        Args:
            max_results: <p>The maximum number of workflow versions to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflowVersions</code>.</p>
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow for which you want to list versions.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.list_workflow_versions_response.ListWorkflowVersionsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflow_versions.async_list_workflow_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowVersions")
        )
        input_: capo_mwaa_serverless.types.list_workflow_versions_request.ListWorkflowVersionsRequest = {
            "workflow_arn": workflow_arn
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
