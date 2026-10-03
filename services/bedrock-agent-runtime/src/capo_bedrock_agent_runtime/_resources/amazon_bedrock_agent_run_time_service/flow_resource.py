from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_alias_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_id
    import capo_bedrock_agent_runtime.types.flow_identifier
    import capo_bedrock_agent_runtime.types.flow_inputs
    import capo_bedrock_agent_runtime.types.invoke_flow_request
    import capo_bedrock_agent_runtime.types.invoke_flow_response
    import capo_bedrock_agent_runtime.types.model_performance_configuration
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class FlowResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    @contextmanager
    def invoke_flow(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        enable_trace: Optional[bool] = None,
        model_performance_configuration: Optional[
            "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
        execution_id: Optional[
            "capo_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
        ] = None,
    ) -> "Generator[capo_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse]":
        """<p>Invokes an alias of a flow to run the inputs that you specify and return the output of each node as a stream. If there's an error, the error is returned. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html">Test a flow in Amazon Bedrock</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeFlow</code>.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias.</p>
            inputs: <p>A list of objects, each containing information about an input into the flow.</p>
            enable_trace: <p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>
            model_performance_configuration: <p>Model performance settings for the request.</p>
            execution_id: <p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow.invoke_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "inputs": inputs,
        }
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if model_performance_configuration is not None:
            input_["model_performance_configuration"] = model_performance_configuration
        if execution_id is not None:
            input_["execution_id"] = execution_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()


class AsyncFlowResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    @asynccontextmanager
    async def invoke_flow(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        enable_trace: Optional[bool] = None,
        model_performance_configuration: Optional[
            "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
        execution_id: Optional[
            "capo_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse]":
        """<p>Invokes an alias of a flow to run the inputs that you specify and return the output of each node as a stream. If there's an error, the error is returned. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html">Test a flow in Amazon Bedrock</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeFlow</code>.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias.</p>
            inputs: <p>A list of objects, each containing information about an input into the flow.</p>
            enable_trace: <p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>
            model_performance_configuration: <p>Model performance settings for the request.</p>
            execution_id: <p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow.async_invoke_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "inputs": inputs,
        }
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if model_performance_configuration is not None:
            input_["model_performance_configuration"] = model_performance_configuration
        if execution_id is not None:
            input_["execution_id"] = execution_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()
