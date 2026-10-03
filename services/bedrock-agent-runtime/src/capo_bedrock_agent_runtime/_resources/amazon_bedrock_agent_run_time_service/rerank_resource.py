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
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.rerank_queries_list
    import capo_bedrock_agent_runtime.types.rerank_request
    import capo_bedrock_agent_runtime.types.rerank_response
    import capo_bedrock_agent_runtime.types.rerank_result
    import capo_bedrock_agent_runtime.types.rerank_sources_list
    import capo_bedrock_agent_runtime.types.reranking_configuration
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class RerankResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def rerank(
        self,
        queries: "capo_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList",
        sources: "capo_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList",
        reranking_configuration: "capo_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.rerank_response.RerankResponse":
        """<p>Reranks the relevance of sources based on queries. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html">Improve the relevance of query responses with a reranker model</a>.</p>

        Args:
            queries: <p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>
            sources: <p>An array of objects, each of which contains information about the sources to rerank.</p>
            reranking_configuration: <p>Contains configurations for reranking.</p>
            next_token: <p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>

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
            req: "OperationRequest[capo_bedrock_agent_runtime.types.rerank_request.RerankRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.rerank_response.RerankResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank.rerank(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.rerank_request.RerankRequest = {
            "queries": queries,
            "sources": sources,
            "reranking_configuration": reranking_configuration,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRerankResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def rerank(
        self,
        queries: "capo_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList",
        sources: "capo_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList",
        reranking_configuration: "capo_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.rerank_response.RerankResponse":
        """<p>Reranks the relevance of sources based on queries. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html">Improve the relevance of query responses with a reranker model</a>.</p>

        Args:
            queries: <p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>
            sources: <p>An array of objects, each of which contains information about the sources to rerank.</p>
            reranking_configuration: <p>Contains configurations for reranking.</p>
            next_token: <p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.rerank_request.RerankRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.rerank_response.RerankResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank.async_rerank(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.rerank_request.RerankRequest = {
            "queries": queries,
            "sources": sources,
            "reranking_configuration": reranking_configuration,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
