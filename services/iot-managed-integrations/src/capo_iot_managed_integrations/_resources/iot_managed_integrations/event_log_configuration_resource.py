from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.create_event_log_configuration_request
    import capo_iot_managed_integrations.types.create_event_log_configuration_response
    import capo_iot_managed_integrations.types.delete_event_log_configuration_request
    import capo_iot_managed_integrations.types.event_log_configuration_summary
    import capo_iot_managed_integrations.types.get_event_log_configuration_request
    import capo_iot_managed_integrations.types.get_event_log_configuration_response
    import capo_iot_managed_integrations.types.list_event_log_configurations_request
    import capo_iot_managed_integrations.types.list_event_log_configurations_response
    import capo_iot_managed_integrations.types.log_configuration_id
    import capo_iot_managed_integrations.types.log_level
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.smart_home_resource_id
    import capo_iot_managed_integrations.types.smart_home_resource_type
    import capo_iot_managed_integrations.types.update_event_log_configuration_request
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class EventLogConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_event_log_configuration(
        self,
        resource_type: "capo_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType",
        event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        resource_id: Optional[
            "capo_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse":
        """<p>Set the event log configuration for the account, resource type, or specific resource.</p>

        Args:
            resource_type: <p>The type of resource for the event log configuration.</p>
            resource_id: <p>The identifier of the resource for the event log configuration.</p>
            event_log_level: <p>The logging level for the event log configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration.create_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest = {
            "resource_type": resource_type,
            "event_log_level": event_log_level,
        }
        if resource_id is not None:
            input_["resource_id"] = resource_id
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

    def delete_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration.delete_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse":
        """<p>Get an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration.get_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_event_log_configurations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse":
        """<p>List all event log configurations for an account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations.list_event_log_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEventLogConfigurations")
        )
        input_: capo_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest = {}
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

    def update_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Update an event log configuration by log configuration ID.</p>

        Args:
            id: <p>The log configuration id.</p>
            event_log_level: <p>The log level for the event in terms of severity.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration.update_event_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest = {
            "id": id,
            "event_log_level": event_log_level,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEventLogConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_event_log_configuration(
        self,
        resource_type: "capo_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType",
        event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        resource_id: Optional[
            "capo_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse":
        """<p>Set the event log configuration for the account, resource type, or specific resource.</p>

        Args:
            resource_type: <p>The type of resource for the event log configuration.</p>
            resource_id: <p>The identifier of the resource for the event log configuration.</p>
            event_log_level: <p>The logging level for the event log configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration.async_create_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest = {
            "resource_type": resource_type,
            "event_log_level": event_log_level,
        }
        if resource_id is not None:
            input_["resource_id"] = resource_id
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

    async def delete_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration.async_delete_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse":
        """<p>Get an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration.async_get_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_event_log_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse":
        """<p>List all event log configurations for an account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations.async_list_event_log_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEventLogConfigurations")
        )
        input_: capo_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest = {}
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

    async def update_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Update an event log configuration by log configuration ID.</p>

        Args:
            id: <p>The log configuration id.</p>
            event_log_level: <p>The log level for the event in terms of severity.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration.async_update_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateEventLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest = {
            "id": id,
            "event_log_level": event_log_level,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
