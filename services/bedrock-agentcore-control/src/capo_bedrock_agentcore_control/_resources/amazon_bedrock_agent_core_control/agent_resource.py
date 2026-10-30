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
    import capo_bedrock_agentcore_control.types.agent_runtime
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_name
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.allowed_ports
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.capacity_provider_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_agent_runtime_request
    import capo_bedrock_agentcore_control.types.create_agent_runtime_response
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_request
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_response
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.filesystem_configurations
    import capo_bedrock_agentcore_control.types.get_agent_runtime_request
    import capo_bedrock_agentcore_control.types.get_agent_runtime_response
    import capo_bedrock_agentcore_control.types.lifecycle_configuration
    import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request
    import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response
    import capo_bedrock_agentcore_control.types.list_agent_runtimes_request
    import capo_bedrock_agentcore_control.types.list_agent_runtimes_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.network_configuration
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.platform_version
    import capo_bedrock_agentcore_control.types.protocol_configuration
    import capo_bedrock_agentcore_control.types.request_header_configuration
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.runtime_metadata_configuration
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_agent_runtime_request
    import capo_bedrock_agentcore_control.types.update_agent_runtime_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class AgentResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        agent_runtime_name: "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName",
        agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        network_configuration: Optional[
            "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        request_header_configuration: Optional[
            "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
        ] = None,
        lifecycle_configuration: Optional[
            "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
        ] = None,
        capacity_provider_configuration: Optional[
            "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
        platform_version: Optional[
            "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
        ] = None,
        allowed_ports: Optional[
            "capo_bedrock_agentcore_control.types.allowed_ports.AllowedPorts"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse":
        """<p>Creates an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_name: <p>The name of the AgentCore Runtime.</p>
            agent_runtime_artifact: <p>The artifact of the AgentCore Runtime.</p>
            role_arn: <p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The network configuration for the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            description: <p>The description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>Configuration for HTTP request headers that will be passed through to the runtime.</p>
            protocol_configuration: <p>The protocol configuration for the AgentCore Runtime, including the protocol, port, and path on which the agent server is available.</p>
            lifecycle_configuration: <p>The life cycle configuration for the AgentCore Runtime.</p>
            environment_variables: <p>Environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>
            capacity_provider_configuration: <p>The capacity provider configuration for the AgentCore Runtime. Use a capacity provider to run the AgentCore Runtime on the Instances compute type, which provisions Amazon Web Services managed compute in your account.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
            platform_version: <p>The version of the runtime platform to use for the AgentCore Runtime.</p>
            allowed_ports: <p>The additional ports on the AgentCore Runtime that are reachable through the runtime's session URL. Specify one to five non-overlapping entries, each containing either a single port or an inclusive port range. Ports must be between <code>8000</code> and <code>12000</code>, excluding the reserved port <code>8443</code>.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime.create_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_agent_runtime_request

            return capo_bedrock_agentcore_control.types.create_agent_runtime_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateAgentRuntime", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest = {
            "agent_runtime_name": agent_runtime_name,
            "agent_runtime_artifact": agent_runtime_artifact,
            "role_arn": role_arn,
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input_["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
        if capacity_provider_configuration is not None:
            input_["capacity_provider_configuration"] = capacity_provider_configuration
        if tags is not None:
            input_["tags"] = tags
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if allowed_ports is not None:
            input_["allowed_ports"] = allowed_ports

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse":
        """<p>Gets an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to retrieve.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime.get_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_runtime_response

            return capo_bedrock_agentcore_control.types.get_agent_runtime_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentRuntime", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        network_configuration: Optional[
            "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        request_header_configuration: Optional[
            "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
        ] = None,
        lifecycle_configuration: Optional[
            "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
        metadata_configuration: Optional[
            "capo_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
        ] = None,
        capacity_provider_configuration: Optional[
            "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
        ] = None,
        platform_version: Optional[
            "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
        ] = None,
        allowed_ports: Optional[
            "capo_bedrock_agentcore_control.types.allowed_ports.AllowedPorts"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse":
        """<p>Updates an existing Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to update.</p>
            agent_runtime_artifact: <p>The updated artifact of the AgentCore Runtime.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The updated network configuration for the AgentCore Runtime.</p>
            description: <p>The updated description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>The updated configuration for HTTP request headers that will be passed through to the runtime.</p>
            protocol_configuration: <p>The updated protocol configuration for the AgentCore Runtime, including the protocol, port, and path on which the agent server is available.</p>
            lifecycle_configuration: <p>The updated life cycle configuration for the AgentCore Runtime.</p>
            metadata_configuration: <p>The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>
            environment_variables: <p>Updated environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The updated filesystem configurations to mount into the AgentCore Runtime.</p>
            capacity_provider_configuration: <p>The updated capacity provider configuration for the AgentCore Runtime.</p>
            platform_version: <p>The updated version of the runtime platform to use for the AgentCore Runtime.</p>
            allowed_ports: <p>The updated additional ports on the AgentCore Runtime that are reachable through the runtime's session URL. Specify one to five non-overlapping entries, each containing either a single port or an inclusive port range. Ports must be between <code>8000</code> and <code>12000</code>, excluding the reserved port <code>8443</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime.update_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_agent_runtime_request

            return capo_bedrock_agentcore_control.types.update_agent_runtime_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAgentRuntime", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id,
            "agent_runtime_artifact": agent_runtime_artifact,
            "role_arn": role_arn,
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input_["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration
        if metadata_configuration is not None:
            input_["metadata_configuration"] = metadata_configuration
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
        if capacity_provider_configuration is not None:
            input_["capacity_provider_configuration"] = capacity_provider_configuration
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if allowed_ports is not None:
            input_["allowed_ports"] = allowed_ports
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

    def delete(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse":
        """<p>Deletes an Amazon Bedrock AgentCore Runtime, or a single version of an AgentCore Runtime when you provide the version qualifier.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to delete.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to delete. When you provide this value, only that version is deleted. When you omit it, the entire AgentCore Runtime and all of its versions are deleted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime.delete_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentRuntime")
        )
        input_: capo_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
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

    def list(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse":
        """<p>Lists all Amazon Secure Agents in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes.list_agent_runtimes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_agent_runtimes_response

            return capo_bedrock_agentcore_control.types.list_agent_runtimes_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentRuntimes", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest = {}
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

    def list_agent_runtime_versions(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse":
        """<p>Lists all versions of a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list versions for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions.list_agent_runtime_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response

            return capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentRuntimeVersions", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest = {
            "agent_runtime_id": agent_runtime_id
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


class AsyncAgentResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        agent_runtime_name: "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName",
        agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        network_configuration: Optional[
            "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        request_header_configuration: Optional[
            "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
        ] = None,
        lifecycle_configuration: Optional[
            "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
        ] = None,
        capacity_provider_configuration: Optional[
            "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
        platform_version: Optional[
            "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
        ] = None,
        allowed_ports: Optional[
            "capo_bedrock_agentcore_control.types.allowed_ports.AllowedPorts"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse":
        """<p>Creates an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_name: <p>The name of the AgentCore Runtime.</p>
            agent_runtime_artifact: <p>The artifact of the AgentCore Runtime.</p>
            role_arn: <p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The network configuration for the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            description: <p>The description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>Configuration for HTTP request headers that will be passed through to the runtime.</p>
            protocol_configuration: <p>The protocol configuration for the AgentCore Runtime, including the protocol, port, and path on which the agent server is available.</p>
            lifecycle_configuration: <p>The life cycle configuration for the AgentCore Runtime.</p>
            environment_variables: <p>Environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>
            capacity_provider_configuration: <p>The capacity provider configuration for the AgentCore Runtime. Use a capacity provider to run the AgentCore Runtime on the Instances compute type, which provisions Amazon Web Services managed compute in your account.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
            platform_version: <p>The version of the runtime platform to use for the AgentCore Runtime.</p>
            allowed_ports: <p>The additional ports on the AgentCore Runtime that are reachable through the runtime's session URL. Specify one to five non-overlapping entries, each containing either a single port or an inclusive port range. Ports must be between <code>8000</code> and <code>12000</code>, excluding the reserved port <code>8443</code>.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime.async_create_agent_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_agent_runtime_request

            return capo_bedrock_agentcore_control.types.create_agent_runtime_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateAgentRuntime", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest = {
            "agent_runtime_name": agent_runtime_name,
            "agent_runtime_artifact": agent_runtime_artifact,
            "role_arn": role_arn,
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input_["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
        if capacity_provider_configuration is not None:
            input_["capacity_provider_configuration"] = capacity_provider_configuration
        if tags is not None:
            input_["tags"] = tags
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if allowed_ports is not None:
            input_["allowed_ports"] = allowed_ports

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse":
        """<p>Gets an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to retrieve.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime.async_get_agent_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_agent_runtime_response

            return capo_bedrock_agentcore_control.types.get_agent_runtime_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentRuntime", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        network_configuration: Optional[
            "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        request_header_configuration: Optional[
            "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
        ] = None,
        lifecycle_configuration: Optional[
            "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
        metadata_configuration: Optional[
            "capo_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
        ] = None,
        capacity_provider_configuration: Optional[
            "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
        ] = None,
        platform_version: Optional[
            "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
        ] = None,
        allowed_ports: Optional[
            "capo_bedrock_agentcore_control.types.allowed_ports.AllowedPorts"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse":
        """<p>Updates an existing Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to update.</p>
            agent_runtime_artifact: <p>The updated artifact of the AgentCore Runtime.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The updated network configuration for the AgentCore Runtime.</p>
            description: <p>The updated description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>The updated configuration for HTTP request headers that will be passed through to the runtime.</p>
            protocol_configuration: <p>The updated protocol configuration for the AgentCore Runtime, including the protocol, port, and path on which the agent server is available.</p>
            lifecycle_configuration: <p>The updated life cycle configuration for the AgentCore Runtime.</p>
            metadata_configuration: <p>The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>
            environment_variables: <p>Updated environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The updated filesystem configurations to mount into the AgentCore Runtime.</p>
            capacity_provider_configuration: <p>The updated capacity provider configuration for the AgentCore Runtime.</p>
            platform_version: <p>The updated version of the runtime platform to use for the AgentCore Runtime.</p>
            allowed_ports: <p>The updated additional ports on the AgentCore Runtime that are reachable through the runtime's session URL. Specify one to five non-overlapping entries, each containing either a single port or an inclusive port range. Ports must be between <code>8000</code> and <code>12000</code>, excluding the reserved port <code>8443</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime.async_update_agent_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_agent_runtime_request

            return capo_bedrock_agentcore_control.types.update_agent_runtime_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateAgentRuntime", redact_input=_redact_input),
        )
        input_: capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id,
            "agent_runtime_artifact": agent_runtime_artifact,
            "role_arn": role_arn,
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input_["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration
        if metadata_configuration is not None:
            input_["metadata_configuration"] = metadata_configuration
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
        if capacity_provider_configuration is not None:
            input_["capacity_provider_configuration"] = capacity_provider_configuration
        if platform_version is not None:
            input_["platform_version"] = platform_version
        if allowed_ports is not None:
            input_["allowed_ports"] = allowed_ports
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

    async def delete(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse":
        """<p>Deletes an Amazon Bedrock AgentCore Runtime, or a single version of an AgentCore Runtime when you provide the version qualifier.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to delete.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to delete. When you provide this value, only that version is deleted. When you omit it, the entire AgentCore Runtime and all of its versions are deleted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime.async_delete_agent_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAgentRuntime")
        )
        input_: capo_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
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

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse":
        """<p>Lists all Amazon Secure Agents in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes.async_list_agent_runtimes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_agent_runtimes_response

            return capo_bedrock_agentcore_control.types.list_agent_runtimes_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentRuntimes", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest = {}
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

    async def list_agent_runtime_versions(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse":
        """<p>Lists all versions of a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list versions for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions.async_list_agent_runtime_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response

            return capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentRuntimeVersions", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest = {
            "agent_runtime_id": agent_runtime_id
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
