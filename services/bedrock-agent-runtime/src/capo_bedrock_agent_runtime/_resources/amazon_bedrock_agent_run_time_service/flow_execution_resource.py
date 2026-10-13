from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_alias_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_event
    import capo_bedrock_agent_runtime.types.flow_execution_event_type
    import capo_bedrock_agent_runtime.types.flow_execution_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_name
    import capo_bedrock_agent_runtime.types.flow_execution_summary
    import capo_bedrock_agent_runtime.types.flow_identifier
    import capo_bedrock_agent_runtime.types.flow_inputs
    import capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request
    import capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response
    import capo_bedrock_agent_runtime.types.get_flow_execution_request
    import capo_bedrock_agent_runtime.types.get_flow_execution_response
    import capo_bedrock_agent_runtime.types.list_flow_execution_events_request
    import capo_bedrock_agent_runtime.types.list_flow_execution_events_response
    import capo_bedrock_agent_runtime.types.list_flow_executions_request
    import capo_bedrock_agent_runtime.types.list_flow_executions_response
    import capo_bedrock_agent_runtime.types.max_results
    import capo_bedrock_agent_runtime.types.model_performance_configuration
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.start_flow_execution_request
    import capo_bedrock_agent_runtime.types.start_flow_execution_response
    import capo_bedrock_agent_runtime.types.stop_flow_execution_request
    import capo_bedrock_agent_runtime.types.stop_flow_execution_response
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class FlowExecutionResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def get_execution_flow_snapshot(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response.GetExecutionFlowSnapshotResponse":
        """<p>Retrieves the flow definition snapshot used for a flow execution. The snapshot represents the flow metadata and definition as it existed at the time the execution was started. Note that even if the flow is edited after an execution starts, the snapshot connected to the execution remains unchanged.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the flow execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request.GetExecutionFlowSnapshotRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response.GetExecutionFlowSnapshotResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_execution_flow_snapshot

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_execution_flow_snapshot.get_execution_flow_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetExecutionFlowSnapshot")
        )
        input_: capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request.GetExecutionFlowSnapshotRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_flow_execution_response.GetFlowExecutionResponse":
        """<p>Retrieves details about a specific flow execution, including its status, start and end times, and any errors that occurred during execution.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution to retrieve.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.get_flow_execution_request.GetFlowExecutionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.get_flow_execution_response.GetFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_flow_execution

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_flow_execution.get_flow_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFlowExecution")
        )
        input_: capo_bedrock_agent_runtime.types.get_flow_execution_request.GetFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_flow_execution_events(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        event_type: "capo_bedrock_agent_runtime.types.flow_execution_event_type.FlowExecutionEventType",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse":
        """<p>Lists events that occurred during a flow execution. Events provide detailed information about the execution progress, including node inputs and outputs, flow inputs and outputs, condition results, and failure events.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution.</p>
            max_results: <p>The maximum number of events to return in a single response. If more events exist than the specified maxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>
            event_type: <p>The type of events to retrieve. Specify <code>Node</code> for node-level events or <code>Flow</code> for flow-level events.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.list_flow_execution_events_request.ListFlowExecutionEventsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_execution_events

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_execution_events.list_flow_execution_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.list_flow_execution_events_response

            return capo_bedrock_agent_runtime.types.list_flow_execution_events_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListFlowExecutionEvents", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent_runtime.types.list_flow_execution_events_request.ListFlowExecutionEventsRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
            "event_type": event_type,
        }
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

    def list_flow_executions(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        flow_alias_identifier: Optional[
            "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_flow_executions_response.ListFlowExecutionsResponse":
        """<p>Lists all executions of a flow. Results can be paginated and include summary information about each execution, such as status, start and end times, and the execution's Amazon Resource Name (ARN).</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow to list executions for.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias to list executions for.</p>
            max_results: <p>The maximum number of flow executions to return in a single response. If more executions exist than the specified <code>maxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.list_flow_executions_request.ListFlowExecutionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.list_flow_executions_response.ListFlowExecutionsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_executions

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_executions.list_flow_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFlowExecutions")
        )
        input_: capo_bedrock_agent_runtime.types.list_flow_executions_request.ListFlowExecutionsRequest = {
            "flow_identifier": flow_identifier
        }
        if flow_alias_identifier is not None:
            input_["flow_alias_identifier"] = flow_alias_identifier
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

    def start_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        flow_execution_name: Optional[
            "capo_bedrock_agent_runtime.types.flow_execution_name.FlowExecutionName"
        ] = None,
        model_performance_configuration: Optional[
            "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.start_flow_execution_response.StartFlowExecutionResponse":
        """<p>Starts an execution of an Amazon Bedrock flow. Unlike flows that run until completion or time out after five minutes, flow executions let you run flows asynchronously for longer durations. Flow executions also yield control so that your application can perform other tasks.</p> <p>This operation returns an Amazon Resource Name (ARN) that you can use to track and manage your flow execution.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow to execute.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias to use for the flow execution.</p>
            flow_execution_name: <p>The unique name for the flow execution. If you don't provide one, a system-generated name is used.</p>
            inputs: <p>The input data required for the flow execution. This must match the input schema defined in the flow.</p>
            model_performance_configuration: <p>The performance settings for the foundation model used in the flow execution.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.start_flow_execution_response.StartFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.start_flow_execution

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.start_flow_execution.start_flow_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.start_flow_execution_request

            return capo_bedrock_agent_runtime.types.start_flow_execution_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartFlowExecution", redact_input=_redact_input),
        )
        input_: capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "inputs": inputs,
        }
        if flow_execution_name is not None:
            input_["flow_execution_name"] = flow_execution_name
        if model_performance_configuration is not None:
            input_["model_performance_configuration"] = model_performance_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.stop_flow_execution_response.StopFlowExecutionResponse":
        """<p>Stops an Amazon Bedrock flow's execution. This operation prevents further processing of the flow and changes the execution status to <code>Aborted</code>.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution to stop.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.stop_flow_execution_request.StopFlowExecutionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.stop_flow_execution_response.StopFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.stop_flow_execution

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.stop_flow_execution.stop_flow_execution(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopFlowExecution")
        )
        input_: capo_bedrock_agent_runtime.types.stop_flow_execution_request.StopFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFlowExecutionResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def get_execution_flow_snapshot(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response.GetExecutionFlowSnapshotResponse":
        """<p>Retrieves the flow definition snapshot used for a flow execution. The snapshot represents the flow metadata and definition as it existed at the time the execution was started. Note that even if the flow is edited after an execution starts, the snapshot connected to the execution remains unchanged.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the flow execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request.GetExecutionFlowSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response.GetExecutionFlowSnapshotResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_execution_flow_snapshot

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_execution_flow_snapshot.async_get_execution_flow_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetExecutionFlowSnapshot")
        )
        input_: capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request.GetExecutionFlowSnapshotRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_flow_execution_response.GetFlowExecutionResponse":
        """<p>Retrieves details about a specific flow execution, including its status, start and end times, and any errors that occurred during execution.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution to retrieve.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_flow_execution_request.GetFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_flow_execution_response.GetFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_flow_execution

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_flow_execution.async_get_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFlowExecution")
        )
        input_: capo_bedrock_agent_runtime.types.get_flow_execution_request.GetFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_flow_execution_events(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        event_type: "capo_bedrock_agent_runtime.types.flow_execution_event_type.FlowExecutionEventType",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse":
        """<p>Lists events that occurred during a flow execution. Events provide detailed information about the execution progress, including node inputs and outputs, flow inputs and outputs, condition results, and failure events.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution.</p>
            max_results: <p>The maximum number of events to return in a single response. If more events exist than the specified maxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>
            event_type: <p>The type of events to retrieve. Specify <code>Node</code> for node-level events or <code>Flow</code> for flow-level events.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_flow_execution_events_request.ListFlowExecutionEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_execution_events

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_execution_events.async_list_flow_execution_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.list_flow_execution_events_response

            return capo_bedrock_agent_runtime.types.list_flow_execution_events_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListFlowExecutionEvents", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent_runtime.types.list_flow_execution_events_request.ListFlowExecutionEventsRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
            "event_type": event_type,
        }
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

    async def list_flow_executions(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        flow_alias_identifier: Optional[
            "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_flow_executions_response.ListFlowExecutionsResponse":
        """<p>Lists all executions of a flow. Results can be paginated and include summary information about each execution, such as status, start and end times, and the execution's Amazon Resource Name (ARN).</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow to list executions for.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias to list executions for.</p>
            max_results: <p>The maximum number of flow executions to return in a single response. If more executions exist than the specified <code>maxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_flow_executions_request.ListFlowExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_flow_executions_response.ListFlowExecutionsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_executions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_executions.async_list_flow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFlowExecutions")
        )
        input_: capo_bedrock_agent_runtime.types.list_flow_executions_request.ListFlowExecutionsRequest = {
            "flow_identifier": flow_identifier
        }
        if flow_alias_identifier is not None:
            input_["flow_alias_identifier"] = flow_alias_identifier
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

    async def start_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        flow_execution_name: Optional[
            "capo_bedrock_agent_runtime.types.flow_execution_name.FlowExecutionName"
        ] = None,
        model_performance_configuration: Optional[
            "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.start_flow_execution_response.StartFlowExecutionResponse":
        """<p>Starts an execution of an Amazon Bedrock flow. Unlike flows that run until completion or time out after five minutes, flow executions let you run flows asynchronously for longer durations. Flow executions also yield control so that your application can perform other tasks.</p> <p>This operation returns an Amazon Resource Name (ARN) that you can use to track and manage your flow execution.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow to execute.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias to use for the flow execution.</p>
            flow_execution_name: <p>The unique name for the flow execution. If you don't provide one, a system-generated name is used.</p>
            inputs: <p>The input data required for the flow execution. This must match the input schema defined in the flow.</p>
            model_performance_configuration: <p>The performance settings for the foundation model used in the flow execution.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.start_flow_execution_response.StartFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.start_flow_execution

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.start_flow_execution.async_start_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.start_flow_execution_request

            return capo_bedrock_agent_runtime.types.start_flow_execution_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartFlowExecution", redact_input=_redact_input),
        )
        input_: capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "inputs": inputs,
        }
        if flow_execution_name is not None:
            input_["flow_execution_name"] = flow_execution_name
        if model_performance_configuration is not None:
            input_["model_performance_configuration"] = model_performance_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.stop_flow_execution_response.StopFlowExecutionResponse":
        """<p>Stops an Amazon Bedrock flow's execution. This operation prevents further processing of the flow and changes the execution status to <code>Aborted</code>.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution to stop.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.stop_flow_execution_request.StopFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.stop_flow_execution_response.StopFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.stop_flow_execution

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.stop_flow_execution.async_stop_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopFlowExecution")
        )
        input_: capo_bedrock_agent_runtime.types.stop_flow_execution_request.StopFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
