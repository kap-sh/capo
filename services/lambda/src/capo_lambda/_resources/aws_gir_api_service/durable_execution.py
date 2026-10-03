from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.checkpoint_durable_execution_request
    import capo_lambda.types.checkpoint_durable_execution_response
    import capo_lambda.types.checkpoint_token
    import capo_lambda.types.client_token
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.error_object
    import capo_lambda.types.event
    import capo_lambda.types.get_durable_execution_history_request
    import capo_lambda.types.get_durable_execution_history_response
    import capo_lambda.types.get_durable_execution_request
    import capo_lambda.types.get_durable_execution_response
    import capo_lambda.types.get_durable_execution_state_request
    import capo_lambda.types.get_durable_execution_state_response
    import capo_lambda.types.include_execution_data
    import capo_lambda.types.item_count
    import capo_lambda.types.operation
    import capo_lambda.types.operation_updates
    import capo_lambda.types.reverse_order
    import capo_lambda.types.stop_durable_execution_request
    import capo_lambda.types.stop_durable_execution_response
    import capo_lambda.types.string
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class DurableExecution:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def read(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
    ) -> "capo_lambda.types.get_durable_execution_response.GetDurableExecutionResponse":
        """<p>Retrieves detailed information about a specific <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable execution</a>, including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as input payload, result, and error information in the response. Set to <code>false</code> for a more compact response that includes only execution metadata. The default value is set to <code>true</code>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_durable_execution_request.GetDurableExecutionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_durable_execution_response.GetDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_durable_execution.get_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_request.GetDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def checkpoint_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        updates: Optional[
            "capo_lambda.types.operation_updates.OperationUpdates"
        ] = None,
        client_token: Optional["capo_lambda.types.client_token.ClientToken"] = None,
    ) -> "capo_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse":
        """<p>Saves the progress of a <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable function</a> execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically.</p> <p>Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.</p>
            updates: <p>An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.</p>
            client_token: <p>An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.checkpoint_durable_execution

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.checkpoint_durable_execution.checkpoint_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn,
            "checkpoint_token": checkpoint_token,
        }
        if updates is not None:
            input_["updates"] = updates
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

    def get_durable_execution_history(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse":
        """<p>Retrieves the execution history for a <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable execution</a>, showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time.</p> <p>The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as step results and callback payloads in the history events. Set to <code>true</code> to include data, or <code>false</code> to exclude it for a more compact response. The default is <code>true</code>.</p>
            max_items: <p>The maximum number of history events to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.</p>
            reverse_order: <p>When set to <code>true</code>, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution_history

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_durable_execution_history.get_durable_execution_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_durable_execution_state(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "capo_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse":
        """<p>Retrieves the current execution state required for the replay process during <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable function</a> execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically.</p> <p>The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.</p>
            max_items: <p>The maximum number of operations to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution_state

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_durable_execution_state.get_durable_execution_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest = {
            "durable_execution_arn": durable_execution_arn,
            "checkpoint_token": checkpoint_token,
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        error: Optional["capo_lambda.types.error_object.ErrorObject"] = None,
    ) -> (
        "capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
    ):
        """<p>Stops a running <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable execution</a>. The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            error: <p>Optional error details explaining why the execution is being stopped.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.stop_durable_execution

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.stop_durable_execution.stop_durable_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDurableExecution:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def read(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
    ) -> "capo_lambda.types.get_durable_execution_response.GetDurableExecutionResponse":
        """<p>Retrieves detailed information about a specific <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable execution</a>, including its current status, input payload, result or error information, and execution metadata such as start time and usage statistics.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as input payload, result, and error information in the response. Set to <code>false</code> for a more compact response that includes only execution metadata. The default value is set to <code>true</code>.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_durable_execution_request.GetDurableExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_durable_execution_response.GetDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_durable_execution.async_get_durable_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_request.GetDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def checkpoint_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        updates: Optional[
            "capo_lambda.types.operation_updates.OperationUpdates"
        ] = None,
        client_token: Optional["capo_lambda.types.client_token.ClientToken"] = None,
    ) -> "capo_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse":
        """<p>Saves the progress of a <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable function</a> execution during runtime. This API is used by the Lambda durable functions SDK to checkpoint completed steps and schedule asynchronous operations. You typically don't need to call this API directly as the SDK handles checkpointing automatically.</p> <p>Each checkpoint operation consumes the current checkpoint token and returns a new one for the next checkpoint. This ensures that checkpoints are applied in the correct order and prevents duplicate or out-of-order state updates.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A unique token that identifies the current checkpoint state. This token is provided by the Lambda runtime and must be used to ensure checkpoints are applied in the correct order. Each checkpoint operation consumes this token and returns a new one.</p>
            updates: <p>An array of state updates to apply during this checkpoint. Each update represents a change to the execution state, such as completing a step, starting a callback, or scheduling a timer. Updates are applied atomically as part of the checkpoint operation.</p>
            client_token: <p>An optional idempotency token to ensure that duplicate checkpoint requests are handled correctly. If provided, Lambda uses this token to detect and handle duplicate requests within a 15-minute window.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.checkpoint_durable_execution_response.CheckpointDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.checkpoint_durable_execution

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.checkpoint_durable_execution.async_checkpoint_durable_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.checkpoint_durable_execution_request.CheckpointDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn,
            "checkpoint_token": checkpoint_token,
        }
        if updates is not None:
            input_["updates"] = updates
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

    async def get_durable_execution_history(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        include_execution_data: Optional[
            "capo_lambda.types.include_execution_data.IncludeExecutionData"
        ] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        reverse_order: Optional["capo_lambda.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse":
        """<p>Retrieves the execution history for a <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable execution</a>, showing all the steps, callbacks, and events that occurred during the execution. This provides a detailed audit trail of the execution's progress over time.</p> <p>The history is available while the execution is running and for a retention period after it completes (1-90 days, default 30 days). You can control whether to include execution data such as step results and callback payloads.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            include_execution_data: <p>Specifies whether to include execution data such as step results and callback payloads in the history events. Set to <code>true</code> to include data, or <code>false</code> to exclude it for a more compact response. The default is <code>true</code>.</p>
            max_items: <p>The maximum number of history events to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of results. Each pagination token expires after 24 hours.</p>
            reverse_order: <p>When set to <code>true</code>, returns the history events in reverse chronological order (newest first). By default, events are returned in chronological order (oldest first).</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_durable_execution_history_response.GetDurableExecutionHistoryResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution_history

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_durable_execution_history.async_get_durable_execution_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_history_request.GetDurableExecutionHistoryRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if include_execution_data is not None:
            input_["include_execution_data"] = include_execution_data
        if max_items is not None:
            input_["max_items"] = max_items
        if marker is not None:
            input_["marker"] = marker
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_durable_execution_state(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        checkpoint_token: "capo_lambda.types.checkpoint_token.CheckpointToken",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.item_count.ItemCount"] = None,
    ) -> "capo_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse":
        """<p>Retrieves the current execution state required for the replay process during <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable function</a> execution. This API is used by the Lambda durable functions SDK to get state information needed for replay. You typically don't need to call this API directly as the SDK handles state management automatically.</p> <p>The response contains operations ordered by start sequence number in ascending order. Completed operations with children don't include child operation details since they don't need to be replayed.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            checkpoint_token: <p>A checkpoint token that identifies the current state of the execution. This token is provided by the Lambda runtime and ensures that state retrieval is consistent with the current execution context.</p>
            marker: <p>If <code>NextMarker</code> was returned from a previous request, use this value to retrieve the next page of operations. Each pagination token expires after 24 hours.</p>
            max_items: <p>The maximum number of operations to return per call. You can use <code>Marker</code> to retrieve additional pages of results. The default is 100 and the maximum allowed is 1000. A value of 0 uses the default.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_durable_execution_state_response.GetDurableExecutionStateResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_durable_execution_state

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_durable_execution_state.async_get_durable_execution_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_durable_execution_state_request.GetDurableExecutionStateRequest = {
            "durable_execution_arn": durable_execution_arn,
            "checkpoint_token": checkpoint_token,
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_durable_execution(
        self,
        durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        error: Optional["capo_lambda.types.error_object.ErrorObject"] = None,
    ) -> (
        "capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
    ):
        """<p>Stops a running <a href="https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html">durable execution</a>. The execution transitions to STOPPED status and cannot be resumed. Any in-progress operations are terminated.</p>

        Args:
            durable_execution_arn: <p>The Amazon Resource Name (ARN) of the durable execution.</p>
            error: <p>Optional error details explaining why the execution is being stopped.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.kms_access_denied_exception.KMSAccessDeniedException: <p>Lambda couldn't decrypt the environment variables because KMS access was denied. Check the Lambda function's KMS permissions.</p>
            capo_lambda.errors.kms_disabled_exception.KMSDisabledException: <p>Lambda couldn't decrypt the environment variables because the KMS key used is disabled. Check the Lambda function's KMS key settings.</p>
            capo_lambda.errors.kms_invalid_state_exception.KMSInvalidStateException: <p>Lambda couldn't decrypt the environment variables because the state of the KMS key used is not valid for Decrypt. Check the function's KMS key settings.</p>
            capo_lambda.errors.kms_not_found_exception.KMSNotFoundException: <p>Lambda couldn't decrypt the environment variables because the KMS key was not found. Check the function's KMS key settings.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.stop_durable_execution_response.StopDurableExecutionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.stop_durable_execution

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.stop_durable_execution.async_stop_durable_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.stop_durable_execution_request.StopDurableExecutionRequest = {
            "durable_execution_arn": durable_execution_arn
        }
        if error is not None:
            input_["error"] = error

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
