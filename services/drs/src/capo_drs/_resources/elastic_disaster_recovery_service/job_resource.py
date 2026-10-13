from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_drs._auth._signers
import capo_drs._auth._sigv4
from capo_drs._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_drs.types.delete_job_request
    import capo_drs.types.delete_job_response
    import capo_drs.types.describe_job_log_items_request
    import capo_drs.types.describe_job_log_items_response
    import capo_drs.types.describe_jobs_request
    import capo_drs.types.describe_jobs_request_filters
    import capo_drs.types.describe_jobs_response
    import capo_drs.types.job
    import capo_drs.types.job_id
    import capo_drs.types.job_log
    import capo_drs.types.pagination_token
    import capo_drs.types.strictly_positive_integer
    from capo_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig
    from capo_drs._services.drs import drsClient, drsClientConfig


class JobResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

    def delete(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
    ) -> "capo_drs.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>The ID of the Job to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.delete_job_request.DeleteJobRequest]",
        ) -> OperationResponse["capo_drs.types.delete_job_response.DeleteJobResponse"]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_job

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.delete_job.delete_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteJob")
        )
        input_: capo_drs.types.delete_job_request.DeleteJobRequest = {"job_id": job_id}

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
        config_overrides: Optional[drsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are created by the StartRecovery, TerminateRecoveryInstances and StartFailbackLaunch APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>A set of filters by which to return Jobs.</p>
            max_results: <p>Maximum number of Jobs to retrieve.</p>
            next_token: <p>The token of the next Job to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_jobs

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_jobs.describe_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_jobs_response.DescribeJobsResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_jobs_response

            return capo_drs.types.describe_jobs_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeJobs", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_jobs_request.DescribeJobsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def describe_job_log_items(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[drsClientConfig] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse":
        """<p>Retrieves a detailed Job log with pagination.</p>

        Args:
            job_id: <p>The ID of the Job for which Job log items will be retrieved.</p>
            max_results: <p>Maximum number of Job log items to retrieve.</p>
            next_token: <p>The token of the next Job log items to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> OperationResponse[
            "capo_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_job_log_items

            output, http_response = (
                capo_drs._operations.elastic_disaster_recovery_service.describe_job_log_items.describe_job_log_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeJobLogItems")
        )
        input_: capo_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {
            "job_id": job_id
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


class AsyncJobResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service

    async def delete(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
    ) -> "capo_drs.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>The ID of the Job to be deleted.</p>

        Raises:
            capo_drs.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource for this operation was not found.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.delete_job_response.DeleteJobResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.delete_job

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteJob")
        )
        input_: capo_drs.types.delete_job_request.DeleteJobRequest = {"job_id": job_id}

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
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        filters: Optional[
            "capo_drs.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the JobsID and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are created by the StartRecovery, TerminateRecoveryInstances and StartFailbackLaunch APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>A set of filters by which to return Jobs.</p>
            max_results: <p>Maximum number of Jobs to retrieve.</p>
            next_token: <p>The token of the next Job to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_jobs

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_jobs.async_describe_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_drs.types.describe_jobs_response.DescribeJobsResponse",
        ) -> dict[str, Any]:
            import capo_drs.types.describe_jobs_response

            return capo_drs.types.describe_jobs_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeJobs", redact_output=_redact_output),
        )
        input_: capo_drs.types.describe_jobs_request.DescribeJobsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def describe_job_log_items(
        self,
        job_id: "capo_drs.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncdrsClientConfig] = None,
        max_results: Optional[
            "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        next_token: Optional["capo_drs.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse":
        """<p>Retrieves a detailed Job log with pagination.</p>

        Args:
            job_id: <p>The ID of the Job for which Job log items will be retrieved.</p>
            max_results: <p>Maximum number of Job log items to retrieve.</p>
            next_token: <p>The token of the next Job log items to retrieve.</p>

        Raises:
            capo_drs.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_drs.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_drs.errors.uninitialized_account_exception.UninitializedAccountException: <p>The account performing the request has not been initialized.</p>
            capo_drs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the AWS service.</p>
            capo_drs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_drs.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import capo_drs._operations.elastic_disaster_recovery_service.describe_job_log_items

            (
                output,
                http_response,
            ) = await capo_drs._operations.elastic_disaster_recovery_service.describe_job_log_items.async_describe_job_log_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeJobLogItems")
        )
        input_: capo_drs.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {
            "job_id": job_id
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
