from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_controltower._auth._signers
import capo_controltower._auth._sigv4
from capo_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_controltower.types.get_baseline_operation_input
    import capo_controltower.types.get_baseline_operation_output
    import capo_controltower.types.operation_identifier
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class BaselineOperationResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput":
        """<p>Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: <code>EnableBaseline</code>, <code>DisableBaseline</code>, <code>UpdateEnabledBaseline</code>, <code>ResetEnabledBaseline</code>. A status message is displayed in case of operation failure. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_baseline_operation_input.GetBaselineOperationInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_baseline_operation

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_baseline_operation.get_baseline_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_baseline_operation_input.GetBaselineOperationInput = {
            "operation_identifier": operation_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncBaselineOperationResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput":
        """<p>Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: <code>EnableBaseline</code>, <code>DisableBaseline</code>, <code>UpdateEnabledBaseline</code>, <code>ResetEnabledBaseline</code>. A status message is displayed in case of operation failure. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_baseline_operation_input.GetBaselineOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_baseline_operation

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_baseline_operation.async_get_baseline_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_baseline_operation_input.GetBaselineOperationInput = {
            "operation_identifier": operation_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
