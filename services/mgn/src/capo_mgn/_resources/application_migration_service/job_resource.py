from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.delete_job_request
    import capo_mgn.types.delete_job_response
    import capo_mgn.types.describe_job_log_items_request
    import capo_mgn.types.describe_job_log_items_response
    import capo_mgn.types.describe_jobs_request
    import capo_mgn.types.describe_jobs_request_filters
    import capo_mgn.types.describe_jobs_response
    import capo_mgn.types.job
    import capo_mgn.types.job_id
    import capo_mgn.types.job_log
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class JobResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def delete(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>Request to delete Job from service by Job ID.</p>
            account_id: <p>Request to delete Job from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_job_request.DeleteJobRequest]",
        ) -> OperationResponse["capo_mgn.types.delete_job_response.DeleteJobResponse"]:
            import capo_mgn._operations.application_migration_service.delete_job

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_job.delete_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteJob")
        )
        input_: capo_mgn.types.delete_job_request.DeleteJobRequest = {"job_id": job_id}
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the jobIDs and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDateTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>Request to describe Job log filters.</p>
            max_results: <p>Request to describe job log items by max results.</p>
            next_token: <p>Request to describe job log items by next token.</p>
            account_id: <p>Request to describe job log items by Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_jobs

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_jobs.describe_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_jobs_response.DescribeJobsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_jobs_response

            return capo_mgn.types.describe_jobs_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeJobs", redact_output=_redact_output),
        )
        input_: capo_mgn.types.describe_jobs_request.DescribeJobsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_job_log_items(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse":
        """<p>Retrieves detailed job log items with paging.</p>

        Args:
            job_id: <p>Request to describe Job log job ID.</p>
            max_results: <p>Request to describe Job log item maximum results.</p>
            next_token: <p>Request to describe Job log next token.</p>
            account_id: <p>Request to describe Job log Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_job_log_items

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_job_log_items.describe_job_log_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeJobLogItems")
        )
        input_: capo_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncJobResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def delete(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>Request to delete Job from service by Job ID.</p>
            account_id: <p>Request to delete Job from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_job_response.DeleteJobResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_job

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteJob")
        )
        input_: capo_mgn.types.delete_job_request.DeleteJobRequest = {"job_id": job_id}
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the jobIDs and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDateTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>Request to describe Job log filters.</p>
            max_results: <p>Request to describe job log items by max results.</p>
            next_token: <p>Request to describe job log items by next token.</p>
            account_id: <p>Request to describe job log items by Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_jobs

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.describe_jobs.async_describe_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.describe_jobs_response.DescribeJobsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.describe_jobs_response

            return capo_mgn.types.describe_jobs_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DescribeJobs", redact_output=_redact_output),
        )
        input_: capo_mgn.types.describe_jobs_request.DescribeJobsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_job_log_items(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse":
        """<p>Retrieves detailed job log items with paging.</p>

        Args:
            job_id: <p>Request to describe Job log job ID.</p>
            max_results: <p>Request to describe Job log item maximum results.</p>
            next_token: <p>Request to describe Job log next token.</p>
            account_id: <p>Request to describe Job log Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_job_log_items

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.describe_job_log_items.async_describe_job_log_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeJobLogItems")
        )
        input_: capo_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
