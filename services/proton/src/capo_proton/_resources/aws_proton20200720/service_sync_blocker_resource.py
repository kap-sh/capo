from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_proton.types.get_service_sync_blocker_summary_input
    import capo_proton.types.get_service_sync_blocker_summary_output
    import capo_proton.types.resource_name
    import capo_proton.types.update_service_sync_blocker_input
    import capo_proton.types.update_service_sync_blocker_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceSyncBlockerResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def read(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput":
        """<p>Get detailed data for the service sync blocker summary.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync blocker summary for. If given only the service name, all instances are blocked.</p>
            service_instance_name: <p>The name of the service instance that you want to get the service sync blocker summary for. If given bothe the instance name and the service name, only the instance is blocked.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_sync_blocker_summary

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_service_sync_blocker_summary.get_service_sync_blocker_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetServiceSyncBlockerSummary")
        )
        input_: capo_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput = {
            "service_name": service_name
        }
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: str,
        resolved_reason: str,
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput":
        """<p>Update the service sync blocker by resolving it.</p>

        Args:
            id: <p>The ID of the service sync blocker.</p>
            resolved_reason: <p>The reason the service sync blocker was resolved.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_sync_blocker

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_service_sync_blocker.update_service_sync_blocker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateServiceSyncBlocker")
        )
        input_: capo_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput = {
            "id": id,
            "resolved_reason": resolved_reason,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceSyncBlockerResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def read(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput":
        """<p>Get detailed data for the service sync blocker summary.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync blocker summary for. If given only the service name, all instances are blocked.</p>
            service_instance_name: <p>The name of the service instance that you want to get the service sync blocker summary for. If given bothe the instance name and the service name, only the instance is blocked.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_sync_blocker_summary_output.GetServiceSyncBlockerSummaryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_sync_blocker_summary

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_sync_blocker_summary.async_get_service_sync_blocker_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetServiceSyncBlockerSummary")
        )
        input_: capo_proton.types.get_service_sync_blocker_summary_input.GetServiceSyncBlockerSummaryInput = {
            "service_name": service_name
        }
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        id: str,
        resolved_reason: str,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput":
        """<p>Update the service sync blocker by resolving it.</p>

        Args:
            id: <p>The ID of the service sync blocker.</p>
            resolved_reason: <p>The reason the service sync blocker was resolved.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_sync_blocker_output.UpdateServiceSyncBlockerOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_sync_blocker

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_sync_blocker.async_update_service_sync_blocker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateServiceSyncBlocker")
        )
        input_: capo_proton.types.update_service_sync_blocker_input.UpdateServiceSyncBlockerInput = {
            "id": id,
            "resolved_reason": resolved_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
