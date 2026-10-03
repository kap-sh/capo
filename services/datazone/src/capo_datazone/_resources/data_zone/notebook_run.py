from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.compute_config
    import capo_datazone.types.domain_id
    import capo_datazone.types.get_notebook_run_input
    import capo_datazone.types.get_notebook_run_output
    import capo_datazone.types.list_notebook_runs_input
    import capo_datazone.types.list_notebook_runs_output
    import capo_datazone.types.max_results
    import capo_datazone.types.metadata
    import capo_datazone.types.network_config
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_run_id
    import capo_datazone.types.notebook_run_status
    import capo_datazone.types.notebook_run_summary
    import capo_datazone.types.pagination_token
    import capo_datazone.types.parameters
    import capo_datazone.types.project_id
    import capo_datazone.types.schedule_id
    import capo_datazone.types.sort_order
    import capo_datazone.types.start_notebook_run_input
    import capo_datazone.types.start_notebook_run_output
    import capo_datazone.types.stop_notebook_run_input
    import capo_datazone.types.stop_notebook_run_output
    import capo_datazone.types.timeout_config
    import capo_datazone.types.trigger_source
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class NotebookRun:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        notebook_identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        compute_configuration: Optional[
            "capo_datazone.types.compute_config.ComputeConfig"
        ] = None,
        network_configuration: Optional[
            "capo_datazone.types.network_config.NetworkConfig"
        ] = None,
        timeout_configuration: Optional[
            "capo_datazone.types.timeout_config.TimeoutConfig"
        ] = None,
        trigger_source: Optional[
            "capo_datazone.types.trigger_source.TriggerSource"
        ] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_run_output.StartNotebookRunOutput":
        """<p>Starts a notebook run in Amazon SageMaker Unified Studio. A notebook run represents the execution of an <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">Amazon SageMaker notebook</a> within a project. You can configure compute, network, timeout, and environment settings for the run.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook run.</p>
            notebook_identifier: <p>The identifier of the notebook to run.</p>
            schedule_identifier: <p>The identifier of the schedule associated with the notebook run.</p>
            compute_configuration: <p>The compute configuration for the notebook run, including instance type and environment version.</p>
            network_configuration: <p>The network configuration for the notebook run, including network access type and optional VPC settings.</p>
            timeout_configuration: <p>The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).</p>
            trigger_source: <p>The source that triggered the notebook run.</p>
            metadata: <p>The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

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
            req: "OperationRequest[capo_datazone.types.start_notebook_run_input.StartNotebookRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.start_notebook_run_output.StartNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_run

            output, http_response = (
                capo_datazone._operations.data_zone.start_notebook_run.start_notebook_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.start_notebook_run_input.StartNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "notebook_identifier": notebook_identifier,
        }
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if timeout_configuration is not None:
            input_["timeout_configuration"] = timeout_configuration
        if trigger_source is not None:
            input_["trigger_source"] = trigger_source
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
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
        identifier: "capo_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_run_output.GetNotebookRunOutput":
        """<p>Gets the details of a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>
            identifier: <p>The identifier of the notebook run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_notebook_run_input.GetNotebookRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_notebook_run_output.GetNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook_run

            output, http_response = (
                capo_datazone._operations.data_zone.get_notebook_run.get_notebook_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_run_input.GetNotebookRunInput = {
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
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        notebook_identifier: Optional[
            "capo_datazone.types.notebook_id.NotebookId"
        ] = None,
        status: Optional[
            "capo_datazone.types.notebook_run_status.NotebookRunStatus"
        ] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook runs</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook runs.</p>
            notebook_identifier: <p>The identifier of the notebook to filter runs by.</p>
            status: <p>The status to filter notebook runs by.</p>
            schedule_identifier: <p>The identifier of the schedule to filter notebook runs by.</p>
            max_results: <p>The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            next_token: <p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_notebook_runs_input.ListNotebookRunsInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notebook_runs

            output, http_response = (
                capo_datazone._operations.data_zone.list_notebook_runs.list_notebook_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.list_notebook_runs_input.ListNotebookRunsInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if notebook_identifier is not None:
            input_["notebook_identifier"] = notebook_identifier
        if status is not None:
            input_["status"] = status
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_notebook_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.stop_notebook_run_output.StopNotebookRunOutput":
        """<p>Stops a running <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.</p>
            identifier: <p>The identifier of the notebook run to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.stop_notebook_run_input.StopNotebookRunInput]",
        ) -> OperationResponse[
            "capo_datazone.types.stop_notebook_run_output.StopNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.stop_notebook_run

            output, http_response = (
                capo_datazone._operations.data_zone.stop_notebook_run.stop_notebook_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.stop_notebook_run_input.StopNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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


class AsyncNotebookRun:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        notebook_identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        compute_configuration: Optional[
            "capo_datazone.types.compute_config.ComputeConfig"
        ] = None,
        network_configuration: Optional[
            "capo_datazone.types.network_config.NetworkConfig"
        ] = None,
        timeout_configuration: Optional[
            "capo_datazone.types.timeout_config.TimeoutConfig"
        ] = None,
        trigger_source: Optional[
            "capo_datazone.types.trigger_source.TriggerSource"
        ] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_run_output.StartNotebookRunOutput":
        """<p>Starts a notebook run in Amazon SageMaker Unified Studio. A notebook run represents the execution of an <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">Amazon SageMaker notebook</a> within a project. You can configure compute, network, timeout, and environment settings for the run.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook run.</p>
            notebook_identifier: <p>The identifier of the notebook to run.</p>
            schedule_identifier: <p>The identifier of the schedule associated with the notebook run.</p>
            compute_configuration: <p>The compute configuration for the notebook run, including instance type and environment version.</p>
            network_configuration: <p>The network configuration for the notebook run, including network access type and optional VPC settings.</p>
            timeout_configuration: <p>The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).</p>
            trigger_source: <p>The source that triggered the notebook run.</p>
            metadata: <p>The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.start_notebook_run_input.StartNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_notebook_run_output.StartNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_notebook_run.async_start_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.start_notebook_run_input.StartNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "notebook_identifier": notebook_identifier,
        }
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if timeout_configuration is not None:
            input_["timeout_configuration"] = timeout_configuration
        if trigger_source is not None:
            input_["trigger_source"] = trigger_source
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
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
        identifier: "capo_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_run_output.GetNotebookRunOutput":
        """<p>Gets the details of a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>
            identifier: <p>The identifier of the notebook run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_notebook_run_input.GetNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_notebook_run_output.GetNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_notebook_run.async_get_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_run_input.GetNotebookRunInput = {
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
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        notebook_identifier: Optional[
            "capo_datazone.types.notebook_id.NotebookId"
        ] = None,
        status: Optional[
            "capo_datazone.types.notebook_run_status.NotebookRunStatus"
        ] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook runs</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook runs.</p>
            notebook_identifier: <p>The identifier of the notebook to filter runs by.</p>
            status: <p>The status to filter notebook runs by.</p>
            schedule_identifier: <p>The identifier of the schedule to filter notebook runs by.</p>
            max_results: <p>The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            next_token: <p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_notebook_runs_input.ListNotebookRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notebook_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_notebook_runs.async_list_notebook_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.list_notebook_runs_input.ListNotebookRunsInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if notebook_identifier is not None:
            input_["notebook_identifier"] = notebook_identifier
        if status is not None:
            input_["status"] = status
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_notebook_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.stop_notebook_run_output.StopNotebookRunOutput":
        """<p>Stops a running <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.</p>
            identifier: <p>The identifier of the notebook run to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.stop_notebook_run_input.StopNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.stop_notebook_run_output.StopNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.stop_notebook_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.stop_notebook_run.async_stop_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.stop_notebook_run_input.StopNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
