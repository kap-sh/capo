from __future__ import annotations

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
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_input
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_request
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_response
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.user_context
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class RetrieveAndGenerateResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def retrieve_and_generate(
        self,
        input: "capo_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
        retrieve_and_generate_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
        ] = None,
        session_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results and using the specified foundation model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>. The response only cites sources that are relevant to the query.</p> <note> <p>This API cannot be used with managed knowledge bases. Use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html">AgenticRetrieveStream</a> or <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html">Retrieve</a> with managed knowledge bases.</p> </note>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate.retrieve_and_generate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest = {
            "input": input
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if retrieve_and_generate_configuration is not None:
            input_["retrieve_and_generate_configuration"] = (
                retrieve_and_generate_configuration
            )
        if session_configuration is not None:
            input_["session_configuration"] = session_configuration
        if user_context is not None:
            input_["user_context"] = user_context

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRetrieveAndGenerateResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def retrieve_and_generate(
        self,
        input: "capo_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
        retrieve_and_generate_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
        ] = None,
        session_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results and using the specified foundation model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>. The response only cites sources that are relevant to the query.</p> <note> <p>This API cannot be used with managed knowledge bases. Use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html">AgenticRetrieveStream</a> or <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html">Retrieve</a> with managed knowledge bases.</p> </note>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate.async_retrieve_and_generate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest = {
            "input": input
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if retrieve_and_generate_configuration is not None:
            input_["retrieve_and_generate_configuration"] = (
                retrieve_and_generate_configuration
            )
        if session_configuration is not None:
            input_["session_configuration"] = session_configuration
        if user_context is not None:
            input_["user_context"] = user_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
