from __future__ import annotations

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
    import capo_iot_managed_integrations.types.get_runtime_log_configuration_request
    import capo_iot_managed_integrations.types.get_runtime_log_configuration_response
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.put_runtime_log_configuration_request
    import capo_iot_managed_integrations.types.reset_runtime_log_configuration_request
    import capo_iot_managed_integrations.types.runtime_log_configurations
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class RuntimeLogConfigurationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def get_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse":
        """<p>Get the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration.get_runtime_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRuntimeLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        runtime_log_configurations: "capo_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Set the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
            runtime_log_configurations: <p>The runtime log configuration for a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration.put_runtime_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutRuntimeLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id,
            "runtime_log_configurations": runtime_log_configurations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reset_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Reset a runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id of a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration.reset_runtime_log_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ResetRuntimeLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRuntimeLogConfigurationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def get_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse":
        """<p>Get the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration.async_get_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRuntimeLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        runtime_log_configurations: "capo_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Set the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
            runtime_log_configurations: <p>The runtime log configuration for a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration.async_put_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutRuntimeLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id,
            "runtime_log_configurations": runtime_log_configurations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Reset a runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id of a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration.async_reset_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ResetRuntimeLogConfiguration")
        )
        input_: capo_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
