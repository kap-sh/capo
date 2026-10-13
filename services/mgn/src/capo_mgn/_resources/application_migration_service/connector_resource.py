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
    import capo_mgn.types.connector
    import capo_mgn.types.connector_id
    import capo_mgn.types.connector_name
    import capo_mgn.types.connector_ssm_command_config
    import capo_mgn.types.create_connector_request
    import capo_mgn.types.delete_connector_request
    import capo_mgn.types.list_connectors_request
    import capo_mgn.types.list_connectors_request_filters
    import capo_mgn.types.list_connectors_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.ssm_instance_id
    import capo_mgn.types.tags_map
    import capo_mgn.types.update_connector_request
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class ConnectorResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_mgn.types.connector_name.ConnectorName",
        ssm_instance_id: "capo_mgn.types.ssm_instance_id.SsmInstanceID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        ssm_command_config: Optional[
            "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
        ] = None,
    ) -> "capo_mgn.types.connector.Connector":
        """<p>Create Connector.</p>

        Args:
            name: <p>Create Connector request name.</p>
            ssm_instance_id: <p>Create Connector request SSM instance ID.</p>
            tags: <p>Create Connector request tags.</p>
            ssm_command_config: <p>Create Connector request SSM command config.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_connector_request.CreateConnectorRequest]",
        ) -> OperationResponse["capo_mgn.types.connector.Connector"]:
            import capo_mgn._operations.application_migration_service.create_connector

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_connector.create_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_connector_request.CreateConnectorRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_connector_request

            return capo_mgn.types.create_connector_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.connector.Connector",
        ) -> dict[str, Any]:
            import capo_mgn.types.connector

            return capo_mgn.types.connector.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateConnector",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_connector_request.CreateConnectorRequest = {
            "name": name,
            "ssm_instance_id": ssm_instance_id,
        }
        if tags is not None:
            input_["tags"] = tags
        if ssm_command_config is not None:
            input_["ssm_command_config"] = ssm_command_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        connector_id: "capo_mgn.types.connector_id.ConnectorID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.connector_name.ConnectorName"] = None,
        ssm_command_config: Optional[
            "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
        ] = None,
    ) -> "capo_mgn.types.connector.Connector":
        """<p>Update Connector.</p>

        Args:
            connector_id: <p>Update Connector request connector ID.</p>
            name: <p>Update Connector request name.</p>
            ssm_command_config: <p>Update Connector request SSM command config.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_connector_request.UpdateConnectorRequest]",
        ) -> OperationResponse["capo_mgn.types.connector.Connector"]:
            import capo_mgn._operations.application_migration_service.update_connector

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_connector.update_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.connector.Connector",
        ) -> dict[str, Any]:
            import capo_mgn.types.connector

            return capo_mgn.types.connector.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateConnector", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if name is not None:
            input_["name"] = name
        if ssm_command_config is not None:
            input_["ssm_command_config"] = ssm_command_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        connector_id: "capo_mgn.types.connector_id.ConnectorID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Delete Connector.</p>

        Args:
            connector_id: <p>Delete Connector request connector ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_mgn._operations.application_migration_service.delete_connector

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_connector.delete_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConnector")
        )
        input_: capo_mgn.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_connectors_response.ListConnectorsResponse":
        """<p>List Connectors.</p>

        Args:
            filters: <p>List Connectors Request filters.</p>
            max_results: <p>List Connectors Request max results.</p>
            next_token: <p>List Connectors Request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_connectors_request.ListConnectorsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_connectors

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_connectors.list_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_connectors_response.ListConnectorsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_connectors_response

            return capo_mgn.types.list_connectors_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListConnectors", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_connectors_request.ListConnectorsRequest = {}
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


class AsyncConnectorResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_mgn.types.connector_name.ConnectorName",
        ssm_instance_id: "capo_mgn.types.ssm_instance_id.SsmInstanceID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        ssm_command_config: Optional[
            "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
        ] = None,
    ) -> "capo_mgn.types.connector.Connector":
        """<p>Create Connector.</p>

        Args:
            name: <p>Create Connector request name.</p>
            ssm_instance_id: <p>Create Connector request SSM instance ID.</p>
            tags: <p>Create Connector request tags.</p>
            ssm_command_config: <p>Create Connector request SSM command config.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.create_connector_request.CreateConnectorRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.connector.Connector"]:
            import capo_mgn._operations.application_migration_service.create_connector

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.create_connector.async_create_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_connector_request.CreateConnectorRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_connector_request

            return capo_mgn.types.create_connector_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.connector.Connector",
        ) -> dict[str, Any]:
            import capo_mgn.types.connector

            return capo_mgn.types.connector.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateConnector",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_connector_request.CreateConnectorRequest = {
            "name": name,
            "ssm_instance_id": ssm_instance_id,
        }
        if tags is not None:
            input_["tags"] = tags
        if ssm_command_config is not None:
            input_["ssm_command_config"] = ssm_command_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        connector_id: "capo_mgn.types.connector_id.ConnectorID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional["capo_mgn.types.connector_name.ConnectorName"] = None,
        ssm_command_config: Optional[
            "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
        ] = None,
    ) -> "capo_mgn.types.connector.Connector":
        """<p>Update Connector.</p>

        Args:
            connector_id: <p>Update Connector request connector ID.</p>
            name: <p>Update Connector request name.</p>
            ssm_command_config: <p>Update Connector request SSM command config.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_connector_request.UpdateConnectorRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.connector.Connector"]:
            import capo_mgn._operations.application_migration_service.update_connector

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_connector.async_update_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.connector.Connector",
        ) -> dict[str, Any]:
            import capo_mgn.types.connector

            return capo_mgn.types.connector.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateConnector", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if name is not None:
            input_["name"] = name
        if ssm_command_config is not None:
            input_["ssm_command_config"] = ssm_command_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        connector_id: "capo_mgn.types.connector_id.ConnectorID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
    ) -> None:
        """<p>Delete Connector.</p>

        Args:
            connector_id: <p>Delete Connector request connector ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_mgn._operations.application_migration_service.delete_connector

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_connector.async_delete_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConnector")
        )
        input_: capo_mgn.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_connectors_response.ListConnectorsResponse":
        """<p>List Connectors.</p>

        Args:
            filters: <p>List Connectors Request filters.</p>
            max_results: <p>List Connectors Request max results.</p>
            next_token: <p>List Connectors Request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_connectors_request.ListConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_connectors

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_connectors.async_list_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_connectors_response.ListConnectorsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_connectors_response

            return capo_mgn.types.list_connectors_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListConnectors", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_connectors_request.ListConnectorsRequest = {}
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
