from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_harness_request
    import capo_bedrock_agentcore_control.types.create_harness_response
    import capo_bedrock_agentcore_control.types.delete_harness_request
    import capo_bedrock_agentcore_control.types.delete_harness_response
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.get_harness_request
    import capo_bedrock_agentcore_control.types.get_harness_response
    import capo_bedrock_agentcore_control.types.harness_allowed_tools
    import capo_bedrock_agentcore_control.types.harness_environment_artifact
    import capo_bedrock_agentcore_control.types.harness_environment_provider_request
    import capo_bedrock_agentcore_control.types.harness_hooks
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_model_configuration
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_skills
    import capo_bedrock_agentcore_control.types.harness_summary
    import capo_bedrock_agentcore_control.types.harness_system_prompt
    import capo_bedrock_agentcore_control.types.harness_tools
    import capo_bedrock_agentcore_control.types.harness_truncation_configuration
    import capo_bedrock_agentcore_control.types.harness_version
    import capo_bedrock_agentcore_control.types.harness_version_summary
    import capo_bedrock_agentcore_control.types.list_harness_versions_request
    import capo_bedrock_agentcore_control.types.list_harness_versions_response
    import capo_bedrock_agentcore_control.types.list_harnesses_request
    import capo_bedrock_agentcore_control.types.list_harnesses_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_harness_request
    import capo_bedrock_agentcore_control.types.update_harness_response
    import capo_bedrock_agentcore_control.types.updated_authorizer_configuration
    import capo_bedrock_agentcore_control.types.updated_harness_environment_artifact
    import capo_bedrock_agentcore_control.types.updated_harness_memory_configuration
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class HarnessResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create_harness(
        self,
        harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName",
        execution_role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        environment: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
        ] = None,
        environment_artifact: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        model: Optional[
            "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        memory: Optional[
            "capo_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
        ] = None,
        truncation: Optional[
            "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
        ] = None,
        hooks: Optional[
            "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse":
        """<p>Operation to create a harness.</p>

        Args:
            harness_name: <p>The name of the harness. Must start with a letter and contain only alphanumeric characters and underscores.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            execution_role_arn: <p>The ARN of the IAM role that the harness assumes when running. This role must have permissions for the services the agent needs to access, such as Amazon Bedrock for model invocation.</p>
            environment: <p>The compute environment configuration for the harness, including network and lifecycle settings.</p>
            environment_artifact: <p>The environment artifact for the harness, such as a custom container image containing additional dependencies.</p>
            environment_variables: <p>Environment variables to set in the harness runtime environment.</p>
            model: <p>The model configuration for the harness. Supports Amazon Bedrock, OpenAI, and Google Gemini model providers.</p>
            system_prompt: <p>The system prompt that defines the agent's behavior and instructions.</p>
            tools: <p>The tools available to the agent, such as remote MCP servers, AgentCore Gateway, AgentCore Browser, Code Interpreter, or inline functions.</p>
            skills: <p>The skills available to the agent. Skills are bundles of files that the agent can pull into its context on demand.</p>
            allowed_tools: <p>The tools that the agent is allowed to use. Supports glob patterns such as * for all tools, @builtin for all built-in tools, or @serverName/toolName for specific MCP server tools.</p>
            memory: <p>The AgentCore Memory configuration for persisting conversation context across sessions.</p>
            truncation: <p>The truncation configuration for managing conversation context when it exceeds model limits.</p>
            hooks: <p>The lifecycle hooks to run at defined points in the agent loop.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute per invocation.</p>
            max_tokens: <p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution per invocation.</p>
            tags: <p>Tags to apply to the harness resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness.create_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_harness_request

            return capo_bedrock_agentcore_control.types.create_harness_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_harness_response

            return capo_bedrock_agentcore_control.types.create_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateHarness",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest = {
            "harness_name": harness_name,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if environment is not None:
            input_["environment"] = environment
        if environment_artifact is not None:
            input_["environment_artifact"] = environment_artifact
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if model is not None:
            input_["model"] = model
        if system_prompt is not None:
            input_["system_prompt"] = system_prompt
        if tools is not None:
            input_["tools"] = tools
        if skills is not None:
            input_["skills"] = skills
        if allowed_tools is not None:
            input_["allowed_tools"] = allowed_tools
        if memory is not None:
            input_["memory"] = memory
        if truncation is not None:
            input_["truncation"] = truncation
        if hooks is not None:
            input_["hooks"] = hooks
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        delete_managed_memory: Optional[bool] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse":
        """<p>Operation to delete a Harness.</p>

        Args:
            harness_id: <p>The ID of the harness to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            delete_managed_memory: <p>Whether to delete the managed memory on harness deletion. Default: true. If false, the memory is disassociated and becomes a regular customer-owned resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_harness_request.DeleteHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness.delete_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.delete_harness_response

            return capo_bedrock_agentcore_control.types.delete_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteHarness", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.delete_harness_request.DeleteHarnessRequest = {
            "harness_id": harness_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if delete_managed_memory is not None:
            input_["delete_managed_memory"] = delete_managed_memory

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        harness_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse":
        """<p>Operation to get a single harness.</p>

        Args:
            harness_id: <p>The ID of the harness to retrieve.</p>
            harness_version: <p>Specific version of the harness to retrieve. If omitted, returns the current Harness configuration, including its status.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_harness_request.GetHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness.get_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_harness_response

            return capo_bedrock_agentcore_control.types.get_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetHarness", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_harness_request.GetHarnessRequest = {
            "harness_id": harness_id
        }
        if harness_version is not None:
            input_["harness_version"] = harness_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_harnesses(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harnesses_response.ListHarnessesResponse":
        """<p>Operation to list harnesses.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_harnesses_request.ListHarnessesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_harnesses_response.ListHarnessesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harnesses

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harnesses.list_harnesses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHarnesses")
        )
        input_: capo_bedrock_agentcore_control.types.list_harnesses_request.ListHarnessesRequest = {}
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

    def list_harness_versions(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harness_versions_response.ListHarnessVersionsResponse":
        """<p>Operation to list the versions of a Harness.</p>

        Args:
            harness_id: <p>The ID of the harness whose versions are listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_harness_versions_request.ListHarnessVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_harness_versions_response.ListHarnessVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_versions

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_versions.list_harness_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHarnessVersions")
        )
        input_: capo_bedrock_agentcore_control.types.list_harness_versions_request.ListHarnessVersionsRequest = {
            "harness_id": harness_id
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

    def update_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        environment: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
        ] = None,
        environment_artifact: Optional[
            "capo_bedrock_agentcore_control.types.updated_harness_environment_artifact.UpdatedHarnessEnvironmentArtifact"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
        ] = None,
        model: Optional[
            "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        memory: Optional[
            "capo_bedrock_agentcore_control.types.updated_harness_memory_configuration.UpdatedHarnessMemoryConfiguration"
        ] = None,
        truncation: Optional[
            "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
        ] = None,
        hooks: Optional[
            "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse":
        """<p>Operation to update a harness.</p>

        Args:
            harness_id: <p>The ID of the harness to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            execution_role_arn: <p>The ARN of the IAM role that the harness assumes when running. If not specified, the existing value is retained.</p>
            environment: <p>The compute environment configuration for the harness. If not specified, the existing value is retained.</p>
            environment_artifact: <p>The environment artifact for the harness. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>
            environment_variables: <p>Environment variables to set in the harness runtime environment. If specified, this replaces all existing environment variables. If not specified, the existing value is retained.</p>
            model: <p>The model configuration for the harness. If not specified, the existing value is retained.</p>
            system_prompt: <p>The system prompt that defines the agent's behavior. If not specified, the existing value is retained.</p>
            tools: <p>The tools available to the agent. If specified, this replaces all existing tools. If not specified, the existing value is retained.</p>
            skills: <p>The skills available to the agent. If specified, this replaces all existing skills. If not specified, the existing value is retained.</p>
            allowed_tools: <p>The tools that the agent is allowed to use. If specified, this replaces all existing allowed tools. If not specified, the existing value is retained.</p>
            memory: <p>The AgentCore Memory configuration. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>
            truncation: <p>The truncation configuration for managing conversation context. If not specified, the existing value is retained.</p>
            hooks: <p>The lifecycle hooks to run at defined points in the agent loop. If specified, this replaces all existing hooks. If not specified, the existing hooks are retained.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute per invocation. If not specified, the existing value is retained.</p>
            max_tokens: <p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation. If not specified, the existing value is retained.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution per invocation. If not specified, the existing value is retained.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness.update_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_harness_request

            return capo_bedrock_agentcore_control.types.update_harness_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_harness_response

            return capo_bedrock_agentcore_control.types.update_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateHarness",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest = {
            "harness_id": harness_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if environment is not None:
            input_["environment"] = environment
        if environment_artifact is not None:
            input_["environment_artifact"] = environment_artifact
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if model is not None:
            input_["model"] = model
        if system_prompt is not None:
            input_["system_prompt"] = system_prompt
        if tools is not None:
            input_["tools"] = tools
        if skills is not None:
            input_["skills"] = skills
        if allowed_tools is not None:
            input_["allowed_tools"] = allowed_tools
        if memory is not None:
            input_["memory"] = memory
        if truncation is not None:
            input_["truncation"] = truncation
        if hooks is not None:
            input_["hooks"] = hooks
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncHarnessResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create_harness(
        self,
        harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName",
        execution_role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        environment: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
        ] = None,
        environment_artifact: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        model: Optional[
            "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        memory: Optional[
            "capo_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
        ] = None,
        truncation: Optional[
            "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
        ] = None,
        hooks: Optional[
            "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse":
        """<p>Operation to create a harness.</p>

        Args:
            harness_name: <p>The name of the harness. Must start with a letter and contain only alphanumeric characters and underscores.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            execution_role_arn: <p>The ARN of the IAM role that the harness assumes when running. This role must have permissions for the services the agent needs to access, such as Amazon Bedrock for model invocation.</p>
            environment: <p>The compute environment configuration for the harness, including network and lifecycle settings.</p>
            environment_artifact: <p>The environment artifact for the harness, such as a custom container image containing additional dependencies.</p>
            environment_variables: <p>Environment variables to set in the harness runtime environment.</p>
            model: <p>The model configuration for the harness. Supports Amazon Bedrock, OpenAI, and Google Gemini model providers.</p>
            system_prompt: <p>The system prompt that defines the agent's behavior and instructions.</p>
            tools: <p>The tools available to the agent, such as remote MCP servers, AgentCore Gateway, AgentCore Browser, Code Interpreter, or inline functions.</p>
            skills: <p>The skills available to the agent. Skills are bundles of files that the agent can pull into its context on demand.</p>
            allowed_tools: <p>The tools that the agent is allowed to use. Supports glob patterns such as * for all tools, @builtin for all built-in tools, or @serverName/toolName for specific MCP server tools.</p>
            memory: <p>The AgentCore Memory configuration for persisting conversation context across sessions.</p>
            truncation: <p>The truncation configuration for managing conversation context when it exceeds model limits.</p>
            hooks: <p>The lifecycle hooks to run at defined points in the agent loop.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute per invocation.</p>
            max_tokens: <p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution per invocation.</p>
            tags: <p>Tags to apply to the harness resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness.async_create_harness(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_harness_request

            return capo_bedrock_agentcore_control.types.create_harness_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_harness_response

            return capo_bedrock_agentcore_control.types.create_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateHarness",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest = {
            "harness_name": harness_name,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if environment is not None:
            input_["environment"] = environment
        if environment_artifact is not None:
            input_["environment_artifact"] = environment_artifact
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if model is not None:
            input_["model"] = model
        if system_prompt is not None:
            input_["system_prompt"] = system_prompt
        if tools is not None:
            input_["tools"] = tools
        if skills is not None:
            input_["skills"] = skills
        if allowed_tools is not None:
            input_["allowed_tools"] = allowed_tools
        if memory is not None:
            input_["memory"] = memory
        if truncation is not None:
            input_["truncation"] = truncation
        if hooks is not None:
            input_["hooks"] = hooks
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        delete_managed_memory: Optional[bool] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse":
        """<p>Operation to delete a Harness.</p>

        Args:
            harness_id: <p>The ID of the harness to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            delete_managed_memory: <p>Whether to delete the managed memory on harness deletion. Default: true. If false, the memory is disassociated and becomes a regular customer-owned resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_harness_request.DeleteHarnessRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness.async_delete_harness(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.delete_harness_response

            return capo_bedrock_agentcore_control.types.delete_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteHarness", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.delete_harness_request.DeleteHarnessRequest = {
            "harness_id": harness_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if delete_managed_memory is not None:
            input_["delete_managed_memory"] = delete_managed_memory

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        harness_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse":
        """<p>Operation to get a single harness.</p>

        Args:
            harness_id: <p>The ID of the harness to retrieve.</p>
            harness_version: <p>Specific version of the harness to retrieve. If omitted, returns the current Harness configuration, including its status.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_harness_request.GetHarnessRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness.async_get_harness(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_harness_response

            return capo_bedrock_agentcore_control.types.get_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetHarness", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_harness_request.GetHarnessRequest = {
            "harness_id": harness_id
        }
        if harness_version is not None:
            input_["harness_version"] = harness_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_harnesses(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harnesses_response.ListHarnessesResponse":
        """<p>Operation to list harnesses.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_harnesses_request.ListHarnessesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_harnesses_response.ListHarnessesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harnesses

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harnesses.async_list_harnesses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHarnesses")
        )
        input_: capo_bedrock_agentcore_control.types.list_harnesses_request.ListHarnessesRequest = {}
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

    async def list_harness_versions(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harness_versions_response.ListHarnessVersionsResponse":
        """<p>Operation to list the versions of a Harness.</p>

        Args:
            harness_id: <p>The ID of the harness whose versions are listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_harness_versions_request.ListHarnessVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_harness_versions_response.ListHarnessVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_versions

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_versions.async_list_harness_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHarnessVersions")
        )
        input_: capo_bedrock_agentcore_control.types.list_harness_versions_request.ListHarnessVersionsRequest = {
            "harness_id": harness_id
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

    async def update_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        environment: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
        ] = None,
        environment_artifact: Optional[
            "capo_bedrock_agentcore_control.types.updated_harness_environment_artifact.UpdatedHarnessEnvironmentArtifact"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
        ] = None,
        model: Optional[
            "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        memory: Optional[
            "capo_bedrock_agentcore_control.types.updated_harness_memory_configuration.UpdatedHarnessMemoryConfiguration"
        ] = None,
        truncation: Optional[
            "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
        ] = None,
        hooks: Optional[
            "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse":
        """<p>Operation to update a harness.</p>

        Args:
            harness_id: <p>The ID of the harness to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            execution_role_arn: <p>The ARN of the IAM role that the harness assumes when running. If not specified, the existing value is retained.</p>
            environment: <p>The compute environment configuration for the harness. If not specified, the existing value is retained.</p>
            environment_artifact: <p>The environment artifact for the harness. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>
            environment_variables: <p>Environment variables to set in the harness runtime environment. If specified, this replaces all existing environment variables. If not specified, the existing value is retained.</p>
            model: <p>The model configuration for the harness. If not specified, the existing value is retained.</p>
            system_prompt: <p>The system prompt that defines the agent's behavior. If not specified, the existing value is retained.</p>
            tools: <p>The tools available to the agent. If specified, this replaces all existing tools. If not specified, the existing value is retained.</p>
            skills: <p>The skills available to the agent. If specified, this replaces all existing skills. If not specified, the existing value is retained.</p>
            allowed_tools: <p>The tools that the agent is allowed to use. If specified, this replaces all existing allowed tools. If not specified, the existing value is retained.</p>
            memory: <p>The AgentCore Memory configuration. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>
            truncation: <p>The truncation configuration for managing conversation context. If not specified, the existing value is retained.</p>
            hooks: <p>The lifecycle hooks to run at defined points in the agent loop. If specified, this replaces all existing hooks. If not specified, the existing hooks are retained.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute per invocation. If not specified, the existing value is retained.</p>
            max_tokens: <p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation. If not specified, the existing value is retained.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution per invocation. If not specified, the existing value is retained.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness.async_update_harness(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_harness_request

            return capo_bedrock_agentcore_control.types.update_harness_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_harness_response

            return capo_bedrock_agentcore_control.types.update_harness_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateHarness",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest = {
            "harness_id": harness_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if environment is not None:
            input_["environment"] = environment
        if environment_artifact is not None:
            input_["environment_artifact"] = environment_artifact
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if model is not None:
            input_["model"] = model
        if system_prompt is not None:
            input_["system_prompt"] = system_prompt
        if tools is not None:
            input_["tools"] = tools
        if skills is not None:
            input_["skills"] = skills
        if allowed_tools is not None:
            input_["allowed_tools"] = allowed_tools
        if memory is not None:
            input_["memory"] = memory
        if truncation is not None:
            input_["truncation"] = truncation
        if hooks is not None:
            input_["hooks"] = hooks
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
