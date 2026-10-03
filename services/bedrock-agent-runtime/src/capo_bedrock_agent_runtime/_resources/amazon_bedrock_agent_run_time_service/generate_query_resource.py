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
    import capo_bedrock_agent_runtime.types.generate_query_request
    import capo_bedrock_agent_runtime.types.generate_query_response
    import capo_bedrock_agent_runtime.types.query_generation_input
    import capo_bedrock_agent_runtime.types.transformation_configuration
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class GenerateQueryResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def generate_query(
        self,
        query_generation_input: "capo_bedrock_agent_runtime.types.query_generation_input.QueryGenerationInput",
        transformation_configuration: "capo_bedrock_agent_runtime.types.transformation_configuration.TransformationConfiguration",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
    ):
        """<p>Generates an SQL query from a natural language query. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html">Generate a query for structured data</a> in the Amazon Bedrock User Guide.</p>

        Args:
            query_generation_input: <p>Specifies information about a natural language query to transform into SQL.</p>
            transformation_configuration: <p>Specifies configurations for transforming the natural language query into SQL.</p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query.generate_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest = {
            "query_generation_input": query_generation_input,
            "transformation_configuration": transformation_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGenerateQueryResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def generate_query(
        self,
        query_generation_input: "capo_bedrock_agent_runtime.types.query_generation_input.QueryGenerationInput",
        transformation_configuration: "capo_bedrock_agent_runtime.types.transformation_configuration.TransformationConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
    ):
        """<p>Generates an SQL query from a natural language query. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html">Generate a query for structured data</a> in the Amazon Bedrock User Guide.</p>

        Args:
            query_generation_input: <p>Specifies information about a natural language query to transform into SQL.</p>
            transformation_configuration: <p>Specifies configurations for transforming the natural language query into SQL.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query.async_generate_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest = {
            "query_generation_input": query_generation_input,
            "transformation_configuration": transformation_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
