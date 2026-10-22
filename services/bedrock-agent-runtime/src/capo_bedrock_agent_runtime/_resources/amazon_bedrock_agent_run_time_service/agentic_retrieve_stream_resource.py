from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
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
    import capo_bedrock_agent_runtime.types.agentic_retrieve_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_instruction_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_messages
    import capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request
    import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response
    import capo_bedrock_agent_runtime.types.agentic_retrievers
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.user_context
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class AgenticRetrieveStreamResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    @contextmanager
    def agentic_retrieve_stream(
        self,
        messages: "capo_bedrock_agent_runtime.types.agentic_retrieve_messages.AgenticRetrieveMessages",
        retrievers: "capo_bedrock_agent_runtime.types.agentic_retrievers.AgenticRetrievers",
        agentic_retrieve_configuration: "capo_bedrock_agent_runtime.types.agentic_retrieve_configuration.AgenticRetrieveConfiguration",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        policy_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration.AgenticRetrievePolicyConfiguration"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration.AgenticRetrieveMemoryConfiguration"
        ] = None,
        retrieval_instruction_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_instruction_configuration.AgenticRetrieveInstructionConfiguration"
        ] = None,
        generate_response: Optional[bool] = None,
    ) -> "Generator[capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse]":
        """<p>Retrieves information from one or more knowledge bases using an agentic approach. Agentic retrieval uses a foundation model to intelligently decompose complex queries into sub-queries and iteratively retrieve relevant information from your knowledge bases. This approach improves retrieval accuracy for complex, multi-step questions that a single retrieval pass might not fully address.</p> <p>The operation returns results through a stream that includes retrieval results, trace events for visibility into the process, and a generated response synthesized from the results by default, which can be turned off.</p>

        Args:
            messages: <p>The list of messages for the agentic retrieval conversation.</p>
            retrievers: <p>The list of retrievers to use for agentic retrieval.</p>
            agentic_retrieve_configuration: <p>Configuration settings for the agentic retrieval operation.</p>
            policy_configuration: <p>Policy configuration for guardrails and content filtering.</p>
            next_token: <p>Opaque continuation token for paginated results.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>
            memory_configuration: <p>The configuration for using an Amazon Bedrock AgentCore Memory resource with this retrieval.</p>
            retrieval_instruction_configuration: <p>A retrieval instruction to apply to this request.</p>
            generate_response: <p>Whether to generate a response based on the retrieved results.</p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream.agentic_retrieve_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request

            return capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response

            return capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AgenticRetrieveStream",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest = {
            "messages": messages,
            "retrievers": retrievers,
            "agentic_retrieve_configuration": agentic_retrieve_configuration,
        }
        if policy_configuration is not None:
            input_["policy_configuration"] = policy_configuration
        if next_token is not None:
            input_["next_token"] = next_token
        if user_context is not None:
            input_["user_context"] = user_context
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if retrieval_instruction_configuration is not None:
            input_["retrieval_instruction_configuration"] = (
                retrieval_instruction_configuration
            )
        if generate_response is not None:
            input_["generate_response"] = generate_response

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()


class AsyncAgenticRetrieveStreamResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    @asynccontextmanager
    async def agentic_retrieve_stream(
        self,
        messages: "capo_bedrock_agent_runtime.types.agentic_retrieve_messages.AgenticRetrieveMessages",
        retrievers: "capo_bedrock_agent_runtime.types.agentic_retrievers.AgenticRetrievers",
        agentic_retrieve_configuration: "capo_bedrock_agent_runtime.types.agentic_retrieve_configuration.AgenticRetrieveConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        policy_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration.AgenticRetrievePolicyConfiguration"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration.AgenticRetrieveMemoryConfiguration"
        ] = None,
        retrieval_instruction_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_instruction_configuration.AgenticRetrieveInstructionConfiguration"
        ] = None,
        generate_response: Optional[bool] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse]":
        """<p>Retrieves information from one or more knowledge bases using an agentic approach. Agentic retrieval uses a foundation model to intelligently decompose complex queries into sub-queries and iteratively retrieve relevant information from your knowledge bases. This approach improves retrieval accuracy for complex, multi-step questions that a single retrieval pass might not fully address.</p> <p>The operation returns results through a stream that includes retrieval results, trace events for visibility into the process, and a generated response synthesized from the results by default, which can be turned off.</p>

        Args:
            messages: <p>The list of messages for the agentic retrieval conversation.</p>
            retrievers: <p>The list of retrievers to use for agentic retrieval.</p>
            agentic_retrieve_configuration: <p>Configuration settings for the agentic retrieval operation.</p>
            policy_configuration: <p>Policy configuration for guardrails and content filtering.</p>
            next_token: <p>Opaque continuation token for paginated results.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>
            memory_configuration: <p>The configuration for using an Amazon Bedrock AgentCore Memory resource with this retrieval.</p>
            retrieval_instruction_configuration: <p>A retrieval instruction to apply to this request.</p>
            generate_response: <p>Whether to generate a response based on the retrieved results.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream.async_agentic_retrieve_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request

            return capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response

            return capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AgenticRetrieveStream",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest = {
            "messages": messages,
            "retrievers": retrievers,
            "agentic_retrieve_configuration": agentic_retrieve_configuration,
        }
        if policy_configuration is not None:
            input_["policy_configuration"] = policy_configuration
        if next_token is not None:
            input_["next_token"] = next_token
        if user_context is not None:
            input_["user_context"] = user_context
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if retrieval_instruction_configuration is not None:
            input_["retrieval_instruction_configuration"] = (
                retrieval_instruction_configuration
            )
        if generate_response is not None:
            input_["generate_response"] = generate_response

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()
