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
    import capo_datazone.types.cell_order
    import capo_datazone.types.client_token
    import capo_datazone.types.create_notebook_input
    import capo_datazone.types.create_notebook_output
    import capo_datazone.types.delete_notebook_input
    import capo_datazone.types.delete_notebook_output
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_config
    import capo_datazone.types.get_notebook_input
    import capo_datazone.types.get_notebook_output
    import capo_datazone.types.list_notebooks_input
    import capo_datazone.types.list_notebooks_output
    import capo_datazone.types.max_results
    import capo_datazone.types.metadata
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_status
    import capo_datazone.types.notebook_summary
    import capo_datazone.types.notebook_type
    import capo_datazone.types.pagination_token
    import capo_datazone.types.parameters
    import capo_datazone.types.project_id
    import capo_datazone.types.sort_key
    import capo_datazone.types.sort_order
    import capo_datazone.types.update_notebook_input
    import capo_datazone.types.update_notebook_output
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class Notebook:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        name: "capo_datazone.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_notebook_output.CreateNotebookOutput":
        """<p>Creates a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio. A notebook is a collaborative document within a project that contains code cells for interactive computing.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to create the notebook.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            name: <p>The name of the notebook. The name must be between 1 and 256 characters.</p>
            description: <p>The description of the notebook.</p>
            type: <p>The type of the notebook.</p>
            metadata: <p>The metadata for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
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
            req: "OperationRequest[capo_datazone.types.create_notebook_input.CreateNotebookInput]",
        ) -> OperationResponse[
            "capo_datazone.types.create_notebook_output.CreateNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.create_notebook

            output, http_response = (
                capo_datazone._operations.data_zone.create_notebook.create_notebook(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.create_notebook_input.CreateNotebookInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
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
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_output.GetNotebookOutput":
        """<p>Gets the details of a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook.</p>

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
            req: "OperationRequest[capo_datazone.types.get_notebook_input.GetNotebookInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_notebook_output.GetNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook

            output, http_response = (
                capo_datazone._operations.data_zone.get_notebook.get_notebook(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_input.GetNotebookInput = {
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

    def update(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        name: Optional["capo_datazone.types.notebook_name.NotebookName"] = None,
        cell_order: Optional["capo_datazone.types.cell_order.CellOrder"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        environment_configuration: Optional[
            "capo_datazone.types.environment_config.EnvironmentConfig"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_notebook_output.UpdateNotebookOutput":
        """<p>Updates a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook to update.</p>
            description: <p>The updated description of the notebook.</p>
            status: <p>The updated status of the notebook.</p>
            name: <p>The updated name of the notebook.</p>
            cell_order: <p>The updated ordered list of cells in the notebook.</p>
            type: <p>The updated type of the notebook.</p>
            metadata: <p>The updated metadata for the notebook, specified as key-value pairs.</p>
            parameters: <p>The updated sensitive parameters for the notebook, specified as key-value pairs.</p>
            environment_configuration: <p>The updated environment configuration for the notebook.</p>
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
            req: "OperationRequest[capo_datazone.types.update_notebook_input.UpdateNotebookInput]",
        ) -> OperationResponse[
            "capo_datazone.types.update_notebook_output.UpdateNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.update_notebook

            output, http_response = (
                capo_datazone._operations.data_zone.update_notebook.update_notebook(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.update_notebook_input.UpdateNotebookInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if cell_order is not None:
            input_["cell_order"] = cell_order
        if type is not None:
            input_["type"] = type
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
        if environment_configuration is not None:
            input_["environment_configuration"] = environment_configuration
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

    def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_notebook_output.DeleteNotebookOutput":
        """<p>Deletes a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook to delete.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_notebook_input.DeleteNotebookInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_notebook_output.DeleteNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_notebook

            output, http_response = (
                capo_datazone._operations.data_zone.delete_notebook.delete_notebook(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.delete_notebook_input.DeleteNotebookInput = {
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
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notebooks_output.ListNotebooksOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebooks</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebooks.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebooks.</p>
            max_results: <p>The maximum number of notebooks to return in a single call. When the number of notebooks exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            sort_by: <p>The field to sort the results by.</p>
            status: <p>The status to filter notebooks by.</p>
            type: <p>The type to filter notebooks by.</p>
            next_token: <p>When the number of notebooks is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebooks, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebooks</code> to list the next set of notebooks.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_notebooks_input.ListNotebooksInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_notebooks_output.ListNotebooksOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notebooks

            output, http_response = (
                capo_datazone._operations.data_zone.list_notebooks.list_notebooks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.list_notebooks_input.ListNotebooksInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncNotebook:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def create(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        name: "capo_datazone.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_notebook_output.CreateNotebookOutput":
        """<p>Creates a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio. A notebook is a collaborative document within a project that contains code cells for interactive computing.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to create the notebook.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            name: <p>The name of the notebook. The name must be between 1 and 256 characters.</p>
            description: <p>The description of the notebook.</p>
            type: <p>The type of the notebook.</p>
            metadata: <p>The metadata for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
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
            req: "AsyncOperationRequest[capo_datazone.types.create_notebook_input.CreateNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_notebook_output.CreateNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.create_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_notebook.async_create_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.create_notebook_input.CreateNotebookInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
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
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_output.GetNotebookOutput":
        """<p>Gets the details of a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook.</p>

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
            req: "AsyncOperationRequest[capo_datazone.types.get_notebook_input.GetNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_notebook_output.GetNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_notebook.async_get_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_input.GetNotebookInput = {
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

    async def update(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        name: Optional["capo_datazone.types.notebook_name.NotebookName"] = None,
        cell_order: Optional["capo_datazone.types.cell_order.CellOrder"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        environment_configuration: Optional[
            "capo_datazone.types.environment_config.EnvironmentConfig"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_notebook_output.UpdateNotebookOutput":
        """<p>Updates a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook to update.</p>
            description: <p>The updated description of the notebook.</p>
            status: <p>The updated status of the notebook.</p>
            name: <p>The updated name of the notebook.</p>
            cell_order: <p>The updated ordered list of cells in the notebook.</p>
            type: <p>The updated type of the notebook.</p>
            metadata: <p>The updated metadata for the notebook, specified as key-value pairs.</p>
            parameters: <p>The updated sensitive parameters for the notebook, specified as key-value pairs.</p>
            environment_configuration: <p>The updated environment configuration for the notebook.</p>
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
            req: "AsyncOperationRequest[capo_datazone.types.update_notebook_input.UpdateNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_notebook_output.UpdateNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.update_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_notebook.async_update_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.update_notebook_input.UpdateNotebookInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if cell_order is not None:
            input_["cell_order"] = cell_order
        if type is not None:
            input_["type"] = type
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
        if environment_configuration is not None:
            input_["environment_configuration"] = environment_configuration
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

    async def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_notebook_output.DeleteNotebookOutput":
        """<p>Deletes a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook to delete.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_notebook_input.DeleteNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_notebook_output.DeleteNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_notebook.async_delete_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.delete_notebook_input.DeleteNotebookInput = {
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
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notebooks_output.ListNotebooksOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebooks</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebooks.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebooks.</p>
            max_results: <p>The maximum number of notebooks to return in a single call. When the number of notebooks exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            sort_by: <p>The field to sort the results by.</p>
            status: <p>The status to filter notebooks by.</p>
            type: <p>The type to filter notebooks by.</p>
            next_token: <p>When the number of notebooks is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebooks, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebooks</code> to list the next set of notebooks.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_notebooks_input.ListNotebooksInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_notebooks_output.ListNotebooksOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notebooks

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_notebooks.async_list_notebooks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_datazone.types.list_notebooks_input.ListNotebooksInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
