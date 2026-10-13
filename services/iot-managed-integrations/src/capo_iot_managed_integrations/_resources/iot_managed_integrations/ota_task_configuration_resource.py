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
    import capo_iot_managed_integrations.types.create_ota_task_configuration_request
    import capo_iot_managed_integrations.types.create_ota_task_configuration_response
    import capo_iot_managed_integrations.types.delete_ota_task_configuration_request
    import capo_iot_managed_integrations.types.get_ota_task_configuration_request
    import capo_iot_managed_integrations.types.get_ota_task_configuration_response
    import capo_iot_managed_integrations.types.list_ota_task_configurations_request
    import capo_iot_managed_integrations.types.list_ota_task_configurations_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.ota_description
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_configuration_name
    import capo_iot_managed_integrations.types.ota_task_configuration_summary
    import capo_iot_managed_integrations.types.push_config
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class OtaTaskConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_ota_task_configuration(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
        ] = None,
        push_config: Optional[
            "capo_iot_managed_integrations.types.push_config.PushConfig"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse":
        """<p>Create a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            description: <p>A description of the over-the-air (OTA) task configuration.</p>
            name: <p>The name of the over-the-air (OTA) task.</p>
            push_config: <p>Describes the type of configuration used for the over-the-air (OTA) task.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration.create_ota_task_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_ota_task_configuration_request

            return capo_iot_managed_integrations.types.create_ota_task_configuration_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateOtaTaskConfiguration", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest = {}
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if push_config is not None:
            input_["push_config"] = push_config
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

    def delete_ota_task_configuration(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task configuration.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration.delete_ota_task_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteOtaTaskConfiguration")
        )
        input_: capo_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ota_task_configuration(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse":
        """<p>Get a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task configuration id.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration.get_ota_task_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_ota_task_configuration_response

            return capo_iot_managed_integrations.types.get_ota_task_configuration_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetOtaTaskConfiguration", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ota_task_configurations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse":
        """<p>List all of the over-the-air (OTA) task configurations.</p>

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
            req: "OperationRequest[capo_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations.list_ota_task_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.list_ota_task_configurations_response

            return capo_iot_managed_integrations.types.list_ota_task_configurations_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListOtaTaskConfigurations", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest = {}
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


class AsyncOtaTaskConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_ota_task_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
        ] = None,
        push_config: Optional[
            "capo_iot_managed_integrations.types.push_config.PushConfig"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse":
        """<p>Create a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            description: <p>A description of the over-the-air (OTA) task configuration.</p>
            name: <p>The name of the over-the-air (OTA) task.</p>
            push_config: <p>Describes the type of configuration used for the over-the-air (OTA) task.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration.async_create_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_ota_task_configuration_request

            return capo_iot_managed_integrations.types.create_ota_task_configuration_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateOtaTaskConfiguration", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest = {}
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if push_config is not None:
            input_["push_config"] = push_config
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

    async def delete_ota_task_configuration(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task configuration.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration.async_delete_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteOtaTaskConfiguration")
        )
        input_: capo_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ota_task_configuration(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse":
        """<p>Get a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task configuration id.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration.async_get_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_ota_task_configuration_response

            return capo_iot_managed_integrations.types.get_ota_task_configuration_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetOtaTaskConfiguration", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ota_task_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse":
        """<p>List all of the over-the-air (OTA) task configurations.</p>

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
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations.async_list_ota_task_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.list_ota_task_configurations_response

            return capo_iot_managed_integrations.types.list_ota_task_configurations_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListOtaTaskConfigurations", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest = {}
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
