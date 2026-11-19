from __future__ import annotations

import uuid
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
    import capo_mgn.types.client_idempotency_token
    import capo_mgn.types.connector_arn
    import capo_mgn.types.list_remote_source_action_invocations_request
    import capo_mgn.types.list_remote_source_action_invocations_request_filters
    import capo_mgn.types.list_remote_source_action_invocations_response
    import capo_mgn.types.list_remote_source_action_jobs_request
    import capo_mgn.types.list_remote_source_action_jobs_request_filters
    import capo_mgn.types.list_remote_source_action_jobs_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.remote_source_action_arns
    import capo_mgn.types.remote_source_action_invocation
    import capo_mgn.types.remote_source_action_job
    import capo_mgn.types.remote_source_action_job_id
    import capo_mgn.types.source_server_arns
    import capo_mgn.types.start_remote_source_action_job_request
    import capo_mgn.types.start_remote_source_action_job_response
    import capo_mgn.types.tags_map
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class RemoteSourceActionJobResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        remote_source_action_arns: "capo_mgn.types.remote_source_action_arns.RemoteSourceActionArns",
        connector_arn: "capo_mgn.types.connector_arn.ConnectorArn",
        source_server_arns: "capo_mgn.types.source_server_arns.SourceServerArns",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        client_token: Optional[
            "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_remote_source_action_job_response.StartRemoteSourceActionJobResponse":
        """<p>Starts a job that runs a source action on source servers through a connector.</p>

        Args:
            remote_source_action_arns: <p>The ARNs of the source actions to run.</p>
            connector_arn: <p>The ARN of the connector that runs the source actions.</p>
            source_server_arns: <p>The ARNs of the source servers to run the source actions on.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Tags to assign to the job.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_remote_source_action_job_request.StartRemoteSourceActionJobRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_remote_source_action_job_response.StartRemoteSourceActionJobResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_remote_source_action_job

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_remote_source_action_job.start_remote_source_action_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_remote_source_action_job_request.StartRemoteSourceActionJobRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_remote_source_action_job_request

            return (
                capo_mgn.types.start_remote_source_action_job_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_mgn.types.start_remote_source_action_job_response.StartRemoteSourceActionJobResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_remote_source_action_job_response

            return (
                capo_mgn.types.start_remote_source_action_job_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRemoteSourceActionJob",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.start_remote_source_action_job_request.StartRemoteSourceActionJobRequest = {
            "remote_source_action_arns": remote_source_action_arns,
            "connector_arn": connector_arn,
            "source_server_arns": source_server_arns,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
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
            "capo_mgn.types.list_remote_source_action_jobs_request_filters.ListRemoteSourceActionJobsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_remote_source_action_jobs_response.ListRemoteSourceActionJobsResponse":
        """<p>Lists the source action jobs in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing source action jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_remote_source_action_jobs_request.ListRemoteSourceActionJobsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_remote_source_action_jobs_response.ListRemoteSourceActionJobsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_remote_source_action_jobs

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_remote_source_action_jobs.list_remote_source_action_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_remote_source_action_jobs_response.ListRemoteSourceActionJobsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_remote_source_action_jobs_response

            return (
                capo_mgn.types.list_remote_source_action_jobs_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListRemoteSourceActionJobs", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.list_remote_source_action_jobs_request.ListRemoteSourceActionJobsRequest = {}
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

    def list_remote_source_action_invocations(
        self,
        remote_source_action_job_id: "capo_mgn.types.remote_source_action_job_id.RemoteSourceActionJobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_remote_source_action_invocations_request_filters.ListRemoteSourceActionInvocationsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_remote_source_action_invocations_response.ListRemoteSourceActionInvocationsResponse":
        """<p>Lists the invocations of a source action job, one for each source server and source action, with optional filtering.</p>

        Args:
            remote_source_action_job_id: <p>The unique identifier of the job to list invocations for.</p>
            filters: <p>Filters to apply when listing invocations, such as source server or status.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_remote_source_action_invocations_request.ListRemoteSourceActionInvocationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_remote_source_action_invocations_response.ListRemoteSourceActionInvocationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_remote_source_action_invocations

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_remote_source_action_invocations.list_remote_source_action_invocations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRemoteSourceActionInvocations")
        )
        input_: capo_mgn.types.list_remote_source_action_invocations_request.ListRemoteSourceActionInvocationsRequest = {
            "remote_source_action_job_id": remote_source_action_job_id
        }
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


class AsyncRemoteSourceActionJobResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        remote_source_action_arns: "capo_mgn.types.remote_source_action_arns.RemoteSourceActionArns",
        connector_arn: "capo_mgn.types.connector_arn.ConnectorArn",
        source_server_arns: "capo_mgn.types.source_server_arns.SourceServerArns",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        client_token: Optional[
            "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_remote_source_action_job_response.StartRemoteSourceActionJobResponse":
        """<p>Starts a job that runs a source action on source servers through a connector.</p>

        Args:
            remote_source_action_arns: <p>The ARNs of the source actions to run.</p>
            connector_arn: <p>The ARN of the connector that runs the source actions.</p>
            source_server_arns: <p>The ARNs of the source servers to run the source actions on.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>Tags to assign to the job.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.start_remote_source_action_job_request.StartRemoteSourceActionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.start_remote_source_action_job_response.StartRemoteSourceActionJobResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_remote_source_action_job

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.start_remote_source_action_job.async_start_remote_source_action_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.start_remote_source_action_job_request.StartRemoteSourceActionJobRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_remote_source_action_job_request

            return (
                capo_mgn.types.start_remote_source_action_job_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_mgn.types.start_remote_source_action_job_response.StartRemoteSourceActionJobResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.start_remote_source_action_job_response

            return (
                capo_mgn.types.start_remote_source_action_job_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRemoteSourceActionJob",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.start_remote_source_action_job_request.StartRemoteSourceActionJobRequest = {
            "remote_source_action_arns": remote_source_action_arns,
            "connector_arn": connector_arn,
            "source_server_arns": source_server_arns,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
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
            "capo_mgn.types.list_remote_source_action_jobs_request_filters.ListRemoteSourceActionJobsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_remote_source_action_jobs_response.ListRemoteSourceActionJobsResponse":
        """<p>Lists the source action jobs in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing source action jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_remote_source_action_jobs_request.ListRemoteSourceActionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_remote_source_action_jobs_response.ListRemoteSourceActionJobsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_remote_source_action_jobs

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_remote_source_action_jobs.async_list_remote_source_action_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_remote_source_action_jobs_response.ListRemoteSourceActionJobsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_remote_source_action_jobs_response

            return (
                capo_mgn.types.list_remote_source_action_jobs_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListRemoteSourceActionJobs", redact_output=_redact_output
            ),
        )
        input_: capo_mgn.types.list_remote_source_action_jobs_request.ListRemoteSourceActionJobsRequest = {}
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

    async def list_remote_source_action_invocations(
        self,
        remote_source_action_job_id: "capo_mgn.types.remote_source_action_job_id.RemoteSourceActionJobID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_remote_source_action_invocations_request_filters.ListRemoteSourceActionInvocationsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_remote_source_action_invocations_response.ListRemoteSourceActionInvocationsResponse":
        """<p>Lists the invocations of a source action job, one for each source server and source action, with optional filtering.</p>

        Args:
            remote_source_action_job_id: <p>The unique identifier of the job to list invocations for.</p>
            filters: <p>Filters to apply when listing invocations, such as source server or status.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_remote_source_action_invocations_request.ListRemoteSourceActionInvocationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_remote_source_action_invocations_response.ListRemoteSourceActionInvocationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_remote_source_action_invocations

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_remote_source_action_invocations.async_list_remote_source_action_invocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRemoteSourceActionInvocations")
        )
        input_: capo_mgn.types.list_remote_source_action_invocations_request.ListRemoteSourceActionInvocationsRequest = {
            "remote_source_action_job_id": remote_source_action_job_id
        }
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
