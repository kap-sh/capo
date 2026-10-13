from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_controltower._auth._signers
import capo_controltower._auth._sigv4
from capo_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_controltower.types.get_landing_zone_operation_input
    import capo_controltower.types.get_landing_zone_operation_output
    import capo_controltower.types.landing_zone_operation_filter
    import capo_controltower.types.landing_zone_operation_summary
    import capo_controltower.types.list_landing_zone_operations_input
    import capo_controltower.types.list_landing_zone_operations_max_results
    import capo_controltower.types.list_landing_zone_operations_output
    import capo_controltower.types.operation_identifier
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class LandingZoneOperationResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput":
        """<p>Returns the status of the specified landing zone operation. Details for an operation are available for 90 days.</p>

        Args:
            operation_identifier: <p>A unique identifier assigned to a landing zone operation.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_landing_zone_operation

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_landing_zone_operation.get_landing_zone_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLandingZoneOperation")
        )
        input_: capo_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput = {
            "operation_identifier": operation_identifier
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
        config_overrides: Optional[ControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput":
        """<p>Lists all landing zone operations from the past 90 days. Results are sorted by time, with the most recent operation first.</p>

        Args:
            filter: <p>An input filter for the <code>ListLandingZoneOperations</code> API that lets you select the types of landing zone operations to view.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_landing_zone_operations

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_landing_zone_operations.list_landing_zone_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListLandingZoneOperations")
        )
        input_: capo_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput = {}
        if filter is not None:
            input_["filter"] = filter
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


class AsyncLandingZoneOperationResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput":
        """<p>Returns the status of the specified landing zone operation. Details for an operation are available for 90 days.</p>

        Args:
            operation_identifier: <p>A unique identifier assigned to a landing zone operation.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_landing_zone_operation

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_landing_zone_operation.async_get_landing_zone_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetLandingZoneOperation")
        )
        input_: capo_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput = {
            "operation_identifier": operation_identifier
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
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput":
        """<p>Lists all landing zone operations from the past 90 days. Results are sorted by time, with the most recent operation first.</p>

        Args:
            filter: <p>An input filter for the <code>ListLandingZoneOperations</code> API that lets you select the types of landing zone operations to view.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_landing_zone_operations

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_landing_zone_operations.async_list_landing_zone_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListLandingZoneOperations")
        )
        input_: capo_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput = {}
        if filter is not None:
            input_["filter"] = filter
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
