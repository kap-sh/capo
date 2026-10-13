from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_iot_managed_integrations.types.create_notification_configuration_request
    import capo_iot_managed_integrations.types.create_notification_configuration_response
    import capo_iot_managed_integrations.types.delete_notification_configuration_request
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.event_type
    import capo_iot_managed_integrations.types.get_notification_configuration_request
    import capo_iot_managed_integrations.types.get_notification_configuration_response
    import capo_iot_managed_integrations.types.list_notification_configurations_request
    import capo_iot_managed_integrations.types.list_notification_configurations_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.notification_configuration_summary
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.update_notification_configuration_request
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class NotificationConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        destination_name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a notification configuration. A configuration is a connection between an event type and a destination that you have already created. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the notification configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration.create_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_notification_configuration_request

            return capo_iot_managed_integrations.types.create_notification_configuration_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateNotificationConfiguration", redact_input=_redact_input
            ),
        )
        input_: capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {
            "event_type": event_type,
            "destination_name": destination_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification configuration. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration.delete_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteNotificationConfiguration")
        )
        input_: capo_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {
            "event_type": event_type
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p> Get a notification configuration for a specified event type.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration.get_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_notification_configuration_response

            return capo_iot_managed_integrations.types.get_notification_configuration_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetNotificationConfiguration", redact_output=_redact_output
            ),
        )
        input_: capo_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {
            "event_type": event_type
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_notification_configurations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p> List all notification configurations.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations.list_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListNotificationConfigurations")
        )
        input_: capo_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}
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

    def update_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        destination_name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p> Update a notification configuration.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration.update_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateNotificationConfiguration")
        )
        input_: capo_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {
            "event_type": event_type,
            "destination_name": destination_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncNotificationConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        destination_name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a notification configuration. A configuration is a connection between an event type and a destination that you have already created. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the notification configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration.async_create_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_notification_configuration_request

            return capo_iot_managed_integrations.types.create_notification_configuration_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateNotificationConfiguration", redact_input=_redact_input
            ),
        )
        input_: capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {
            "event_type": event_type,
            "destination_name": destination_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification configuration. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration.async_delete_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteNotificationConfiguration")
        )
        input_: capo_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {
            "event_type": event_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p> Get a notification configuration for a specified event type.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration.async_get_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_notification_configuration_response

            return capo_iot_managed_integrations.types.get_notification_configuration_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetNotificationConfiguration", redact_output=_redact_output
            ),
        )
        input_: capo_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {
            "event_type": event_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_notification_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p> List all notification configurations.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations.async_list_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListNotificationConfigurations")
        )
        input_: capo_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}
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

    async def update_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        destination_name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p> Update a notification configuration.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration.async_update_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateNotificationConfiguration")
        )
        input_: capo_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {
            "event_type": event_type,
            "destination_name": destination_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
