from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_nova_act._auth._signers
import capo_nova_act._auth._sigv4
from capo_nova_act._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_nova_act.types.client_token
    import capo_nova_act.types.create_workflow_definition_request
    import capo_nova_act.types.create_workflow_definition_response
    import capo_nova_act.types.delete_workflow_definition_request
    import capo_nova_act.types.delete_workflow_definition_response
    import capo_nova_act.types.get_workflow_definition_request
    import capo_nova_act.types.get_workflow_definition_response
    import capo_nova_act.types.list_workflow_definitions_request
    import capo_nova_act.types.list_workflow_definitions_response
    import capo_nova_act.types.max_results
    import capo_nova_act.types.next_token
    import capo_nova_act.types.sort_order
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_definition_summary
    import capo_nova_act.types.workflow_description
    import capo_nova_act.types.workflow_export_config
    from capo_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from capo_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class WorkflowDefinitionResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        description: Optional[
            "capo_nova_act.types.workflow_description.WorkflowDescription"
        ] = None,
        export_config: Optional[
            "capo_nova_act.types.workflow_export_config.WorkflowExportConfig"
        ] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse":
        """<p>Creates a new workflow definition template that can be used to execute multiple workflow runs.</p>

        Args:
            name: <p>The name of the workflow definition. Must be unique within your account and region.</p>
            description: <p>An optional description of the workflow definition's purpose and functionality.</p>
            export_config: <p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition.create_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.create_workflow_definition_request

            return (
                capo_nova_act.types.create_workflow_definition_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateWorkflowDefinition", redact_input=_redact_input),
        )
        input_: capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if export_config is not None:
            input_["export_config"] = export_config
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
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse":
        """<p>Retrieves the details and configuration of a specific workflow definition.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to retrieve.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition.get_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse",
        ) -> dict[str, Any]:
            import capo_nova_act.types.get_workflow_definition_response

            return (
                capo_nova_act.types.get_workflow_definition_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetWorkflowDefinition", redact_output=_redact_output),
        )
        input_: capo_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest = {
            "workflow_definition_name": workflow_definition_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse":
        """<p>Deletes a workflow definition and all associated resources. This operation cannot be undone.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to delete.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition.delete_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowDefinition")
        )
        input_: capo_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest = {
            "workflow_definition_name": workflow_definition_name
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
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse":
        """<p>Lists all workflow definitions in your account with optional filtering and pagination.</p>

        Args:
            max_results: <p>The maximum number of workflow definitions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow definitions (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions.list_workflow_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowDefinitions")
        )
        input_: capo_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkflowDefinitionResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        description: Optional[
            "capo_nova_act.types.workflow_description.WorkflowDescription"
        ] = None,
        export_config: Optional[
            "capo_nova_act.types.workflow_export_config.WorkflowExportConfig"
        ] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse":
        """<p>Creates a new workflow definition template that can be used to execute multiple workflow runs.</p>

        Args:
            name: <p>The name of the workflow definition. Must be unique within your account and region.</p>
            description: <p>An optional description of the workflow definition's purpose and functionality.</p>
            export_config: <p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition.async_create_workflow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest",
        ) -> dict[str, Any]:
            import capo_nova_act.types.create_workflow_definition_request

            return (
                capo_nova_act.types.create_workflow_definition_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateWorkflowDefinition", redact_input=_redact_input),
        )
        input_: capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if export_config is not None:
            input_["export_config"] = export_config
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
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse":
        """<p>Retrieves the details and configuration of a specific workflow definition.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to retrieve.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition.async_get_workflow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse",
        ) -> dict[str, Any]:
            import capo_nova_act.types.get_workflow_definition_response

            return (
                capo_nova_act.types.get_workflow_definition_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetWorkflowDefinition", redact_output=_redact_output),
        )
        input_: capo_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest = {
            "workflow_definition_name": workflow_definition_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "capo_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse":
        """<p>Deletes a workflow definition and all associated resources. This operation cannot be undone.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to delete.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition.async_delete_workflow_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflowDefinition")
        )
        input_: capo_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest = {
            "workflow_definition_name": workflow_definition_name
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
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse":
        """<p>Lists all workflow definitions in your account with optional filtering and pagination.</p>

        Args:
            max_results: <p>The maximum number of workflow definitions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow definitions (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions

            (
                output,
                http_response,
            ) = await capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions.async_list_workflow_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflowDefinitions")
        )
        input_: capo_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
