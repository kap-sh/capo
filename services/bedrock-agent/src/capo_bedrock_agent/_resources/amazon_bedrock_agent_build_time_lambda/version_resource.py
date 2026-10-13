from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_version_summary
    import capo_bedrock_agent.types.delete_agent_version_request
    import capo_bedrock_agent.types.delete_agent_version_response
    import capo_bedrock_agent.types.get_agent_version_request
    import capo_bedrock_agent.types.get_agent_version_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.list_agent_versions_request
    import capo_bedrock_agent.types.list_agent_versions_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.numerical_version
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class VersionResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def delete_agent_version(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse":
        """<p>Deletes a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the version belongs to.</p>
            agent_version: <p>The version of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version.delete_agent_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentVersion")
        )
        input_: capo_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_version(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse":
        """<p>Gets details about a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version.get_agent_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.get_agent_version_response

            return capo_bedrock_agent.types.get_agent_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentVersion", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_versions(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse":
        """<p>Lists the versions of an agent and information about each version.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions.list_agent_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAgentVersions")
        )
        input_: capo_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest = {
            "agent_id": agent_id
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


class AsyncVersionResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def delete_agent_version(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        skip_resource_in_use_check: Optional[bool] = None,
    ) -> "capo_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse":
        """<p>Deletes a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent that the version belongs to.</p>
            agent_version: <p>The version of the agent to delete.</p>
            skip_resource_in_use_check: <p>By default, this value is <code>false</code> and deletion is stopped if the resource is in use. If you set it to <code>true</code>, the resource will be deleted even if the resource is in use.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_agent_version_response.DeleteAgentVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_agent_version.async_delete_agent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentVersion")
        )
        input_: capo_bedrock_agent.types.delete_agent_version_request.DeleteAgentVersionRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_version(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.numerical_version.NumericalVersion",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse":
        """<p>Gets details about a version of an agent.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            agent_version: <p>The version of the agent.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_version.async_get_agent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.get_agent_version_response.GetAgentVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.get_agent_version_response

            return capo_bedrock_agent.types.get_agent_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentVersion", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.get_agent_version_request.GetAgentVersionRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_versions(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse":
        """<p>Lists the versions of an agent and information about each version.</p>

        Args:
            agent_id: <p>The unique identifier of the agent.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_agent_versions_response.ListAgentVersionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_versions.async_list_agent_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAgentVersions")
        )
        input_: capo_bedrock_agent.types.list_agent_versions_request.ListAgentVersionsRequest = {
            "agent_id": agent_id
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
