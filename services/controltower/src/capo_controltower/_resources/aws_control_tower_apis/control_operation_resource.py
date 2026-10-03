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
    import capo_controltower.types.control_operation_filter
    import capo_controltower.types.control_operation_summary
    import capo_controltower.types.get_control_operation_input
    import capo_controltower.types.get_control_operation_output
    import capo_controltower.types.list_control_operations_input
    import capo_controltower.types.list_control_operations_max_results
    import capo_controltower.types.list_control_operations_next_token
    import capo_controltower.types.list_control_operations_output
    import capo_controltower.types.operation_identifier
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class ControlOperationResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def read(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> (
        "capo_controltower.types.get_control_operation_output.GetControlOperationOutput"
    ):
        """<p>Returns the status of a particular <code>EnableControl</code> or <code>DisableControl</code> operation. Displays a message in case of error. Details for an operation are available for 90 days. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.get_control_operation_input.GetControlOperationInput]",
        ) -> OperationResponse[
            "capo_controltower.types.get_control_operation_output.GetControlOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_control_operation

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.get_control_operation.get_control_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_control_operation_input.GetControlOperationInput = {
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
            "capo_controltower.types.control_operation_filter.ControlOperationFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_control_operations_output.ListControlOperationsOutput":
        """<p>Provides a list of operations in progress or queued. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html#list-control-operations-api-examples">ListControlOperation examples</a>.</p>

        Args:
            filter: <p>An input filter for the <code>ListControlOperations</code> API that lets you select the types of control operations to view.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_control_operations_input.ListControlOperationsInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_control_operations_output.ListControlOperationsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_control_operations

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_control_operations.list_control_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_control_operations_input.ListControlOperationsInput = {}
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


class AsyncControlOperationResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def read(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> (
        "capo_controltower.types.get_control_operation_output.GetControlOperationOutput"
    ):
        """<p>Returns the status of a particular <code>EnableControl</code> or <code>DisableControl</code> operation. Displays a message in case of error. Details for an operation are available for 90 days. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_control_operation_input.GetControlOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_control_operation_output.GetControlOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_control_operation

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_control_operation.async_get_control_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.get_control_operation_input.GetControlOperationInput = {
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
            "capo_controltower.types.control_operation_filter.ControlOperationFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_control_operations_output.ListControlOperationsOutput":
        """<p>Provides a list of operations in progress or queued. For usage examples, see <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html#list-control-operations-api-examples">ListControlOperation examples</a>.</p>

        Args:
            filter: <p>An input filter for the <code>ListControlOperations</code> API that lets you select the types of control operations to view.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_control_operations_input.ListControlOperationsInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_control_operations_output.ListControlOperationsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_control_operations

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_control_operations.async_list_control_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_control_operations_input.ListControlOperationsInput = {}
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
