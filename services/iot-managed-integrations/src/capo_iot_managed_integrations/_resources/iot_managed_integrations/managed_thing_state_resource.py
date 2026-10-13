from __future__ import annotations

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
    import capo_iot_managed_integrations.types.get_managed_thing_state_request
    import capo_iot_managed_integrations.types.get_managed_thing_state_response
    import capo_iot_managed_integrations.types.managed_thing_id
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ManagedThingStateResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def get_managed_thing_state(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse":
        """<p> Returns the managed thing state for the given device Id.</p>

        Args:
            managed_thing_id: <p>The id of the device.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state.get_managed_thing_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_managed_thing_state_response

            return capo_iot_managed_integrations.types.get_managed_thing_state_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetManagedThingState", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedThingStateResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def get_managed_thing_state(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse":
        """<p> Returns the managed thing state for the given device Id.</p>

        Args:
            managed_thing_id: <p>The id of the device.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state.async_get_managed_thing_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_managed_thing_state_response

            return capo_iot_managed_integrations.types.get_managed_thing_state_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetManagedThingState", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
