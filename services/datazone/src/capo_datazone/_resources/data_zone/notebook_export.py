from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.export_id
    import capo_datazone.types.file_format
    import capo_datazone.types.get_notebook_export_input
    import capo_datazone.types.get_notebook_export_output
    import capo_datazone.types.notebook_id
    import capo_datazone.types.project_id
    import capo_datazone.types.start_notebook_export_input
    import capo_datazone.types.start_notebook_export_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class NotebookExport:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        notebook_identifier: "capo_datazone.types.notebook_id.NotebookId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        file_format: "capo_datazone.types.file_format.FileFormat",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_export_output.StartNotebookExportOutput":
        """<p>Starts a notebook export in Amazon SageMaker Unified Studio. This operation exports a notebook to a specified file format and stores the output in Amazon Simple Storage Service.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>
            notebook_identifier: <p>The identifier of the notebook to export.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            file_format: <p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>
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
            req: "OperationRequest[capo_datazone.types.start_notebook_export_input.StartNotebookExportInput]",
        ) -> OperationResponse[
            "capo_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_export

            output, http_response = (
                capo_datazone._operations.data_zone.start_notebook_export.start_notebook_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartNotebookExport")
        )
        input_: capo_datazone.types.start_notebook_export_input.StartNotebookExportInput = {
            "domain_identifier": domain_identifier,
            "notebook_identifier": notebook_identifier,
            "owning_project_identifier": owning_project_identifier,
            "file_format": file_format,
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
        identifier: "capo_datazone.types.export_id.ExportId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput":
        """<p>Gets the details of a notebook export in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.</p>
            identifier: <p>The identifier of the notebook export.</p>

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
            req: "OperationRequest[capo_datazone.types.get_notebook_export_input.GetNotebookExportInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook_export

            output, http_response = (
                capo_datazone._operations.data_zone.get_notebook_export.get_notebook_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_notebook_export_output

            return capo_datazone.types.get_notebook_export_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetNotebookExport", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_notebook_export_input.GetNotebookExportInput = {
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


class AsyncNotebookExport:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        notebook_identifier: "capo_datazone.types.notebook_id.NotebookId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        file_format: "capo_datazone.types.file_format.FileFormat",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_export_output.StartNotebookExportOutput":
        """<p>Starts a notebook export in Amazon SageMaker Unified Studio. This operation exports a notebook to a specified file format and stores the output in Amazon Simple Storage Service.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>
            notebook_identifier: <p>The identifier of the notebook to export.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            file_format: <p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>
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
            req: "AsyncOperationRequest[capo_datazone.types.start_notebook_export_input.StartNotebookExportInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_export

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_notebook_export.async_start_notebook_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartNotebookExport")
        )
        input_: capo_datazone.types.start_notebook_export_input.StartNotebookExportInput = {
            "domain_identifier": domain_identifier,
            "notebook_identifier": notebook_identifier,
            "owning_project_identifier": owning_project_identifier,
            "file_format": file_format,
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
        identifier: "capo_datazone.types.export_id.ExportId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput":
        """<p>Gets the details of a notebook export in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.</p>
            identifier: <p>The identifier of the notebook export.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.get_notebook_export_input.GetNotebookExportInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook_export

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_notebook_export.async_get_notebook_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_notebook_export_output

            return capo_datazone.types.get_notebook_export_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetNotebookExport", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_notebook_export_input.GetNotebookExportInput = {
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
