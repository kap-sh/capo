from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_id
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.data_source_run_summary
    import capo_datazone.types.domain_id
    import capo_datazone.types.get_data_source_run_input
    import capo_datazone.types.get_data_source_run_output
    import capo_datazone.types.list_data_source_runs_input
    import capo_datazone.types.list_data_source_runs_output
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.start_data_source_run_input
    import capo_datazone.types.start_data_source_run_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class DataSourceRun:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.start_data_source_run_output.StartDataSourceRunOutput":
        """<p>Start the run of the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.start_data_source_run_input.StartDataSourceRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.start_data_source_run_output.StartDataSourceRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_data_source_run

            output, http_response = (
                capo_datazone._operations.data_zone.start_data_source_run.start_data_source_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDataSourceRun")
        )
        input_: capo_datazone.types.start_data_source_run_input.StartDataSourceRunInput = {
            "domain_identifier": domain_identifier,
            "data_source_identifier": data_source_identifier,
        }
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_source_run_output.GetDataSourceRunOutput":
        """<p>Gets an Amazon DataZone data source run.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which this data source run was performed.</p>
            identifier: <p>The ID of the data source run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_data_source_run_input.GetDataSourceRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_data_source_run_output.GetDataSourceRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_source_run

            output, http_response = (
                capo_datazone._operations.data_zone.get_data_source_run.get_data_source_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDataSourceRun")
        )
        input_: capo_datazone.types.get_data_source_run_input.GetDataSourceRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput":
        """<p>Lists data source runs in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>ListDataSourceRuns</code> action.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            status: <p>The status of the data source.</p>
            next_token: <p>When the number of runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
            max_results: <p>The maximum number of runs to return in a single call to <code>ListDataSourceRuns</code>. When the number of runs to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_source_runs

            output, http_response = (
                capo_datazone._operations.data_zone.list_data_source_runs.list_data_source_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDataSourceRuns")
        )
        input_: capo_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput = {
            "domain_identifier": domain_identifier,
            "data_source_identifier": data_source_identifier,
        }
        if status is not None:
            input_["status"] = status
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


class AsyncDataSourceRun:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.start_data_source_run_output.StartDataSourceRunOutput":
        """<p>Start the run of the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_data_source_run_input.StartDataSourceRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_data_source_run_output.StartDataSourceRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_data_source_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_data_source_run.async_start_data_source_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDataSourceRun")
        )
        input_: capo_datazone.types.start_data_source_run_input.StartDataSourceRunInput = {
            "domain_identifier": domain_identifier,
            "data_source_identifier": data_source_identifier,
        }
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_source_run_output.GetDataSourceRunOutput":
        """<p>Gets an Amazon DataZone data source run.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which this data source run was performed.</p>
            identifier: <p>The ID of the data source run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_data_source_run_input.GetDataSourceRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_data_source_run_output.GetDataSourceRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_source_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_data_source_run.async_get_data_source_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDataSourceRun")
        )
        input_: capo_datazone.types.get_data_source_run_input.GetDataSourceRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput":
        """<p>Lists data source runs in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>ListDataSourceRuns</code> action.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            status: <p>The status of the data source.</p>
            next_token: <p>When the number of runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
            max_results: <p>The maximum number of runs to return in a single call to <code>ListDataSourceRuns</code>. When the number of runs to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_source_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_data_source_runs.async_list_data_source_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDataSourceRuns")
        )
        input_: capo_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput = {
            "domain_identifier": domain_identifier,
            "data_source_identifier": data_source_identifier,
        }
        if status is not None:
            input_["status"] = status
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
