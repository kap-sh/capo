from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.metadata_filter_expression
    import capo_bedrock_agentcore.types.registry_id_list
    import capo_bedrock_agentcore.types.search_registry_records_request
    import capo_bedrock_agentcore.types.search_registry_records_response
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class RegistryRecordResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def search_registry_records(
        self,
        search_query: str,
        registry_ids: "capo_bedrock_agentcore.types.registry_id_list.RegistryIdList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_bedrock_agentcore.types.metadata_filter_expression.MetadataFilterExpression"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse":
        """<p> Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.</p>

        Args:
            search_query: <p> The search query to find matching registry records.</p>
            registry_ids: <p> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.</p>
            max_results: <p> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.</p>
            filters: <p> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>). For example, to filter by descriptor type: <code>{"descriptorType": {"$eq": "MCP"}}</code>. To combine filters: <code>{"$and": [{"descriptorType": {"$eq": "MCP"}}, {"name": {"$eq": "my-tool"}}]}</code>.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records.search_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest = {
            "search_query": search_query,
            "registry_ids": registry_ids,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRegistryRecordResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def search_registry_records(
        self,
        search_query: str,
        registry_ids: "capo_bedrock_agentcore.types.registry_id_list.RegistryIdList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_bedrock_agentcore.types.metadata_filter_expression.MetadataFilterExpression"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse":
        """<p> Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.</p>

        Args:
            search_query: <p> The search query to find matching registry records.</p>
            registry_ids: <p> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.</p>
            max_results: <p> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.</p>
            filters: <p> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>). For example, to filter by descriptor type: <code>{"descriptorType": {"$eq": "MCP"}}</code>. To combine filters: <code>{"$and": [{"descriptorType": {"$eq": "MCP"}}, {"name": {"$eq": "my-tool"}}]}</code>.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records.async_search_registry_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest = {
            "search_query": search_query,
            "registry_ids": registry_ids,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
