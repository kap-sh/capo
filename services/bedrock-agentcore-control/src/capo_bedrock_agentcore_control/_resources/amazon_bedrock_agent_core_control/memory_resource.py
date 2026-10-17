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
    import capo_bedrock_agentcore_control.types.arn
    import capo_bedrock_agentcore_control.types.create_memory_input
    import capo_bedrock_agentcore_control.types.create_memory_output
    import capo_bedrock_agentcore_control.types.delete_memory_input
    import capo_bedrock_agentcore_control.types.delete_memory_output
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.get_memory_input
    import capo_bedrock_agentcore_control.types.get_memory_output
    import capo_bedrock_agentcore_control.types.indexed_keys_list
    import capo_bedrock_agentcore_control.types.list_memories_input
    import capo_bedrock_agentcore_control.types.list_memories_output
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.memory_strategy_input_list
    import capo_bedrock_agentcore_control.types.memory_summary
    import capo_bedrock_agentcore_control.types.memory_view
    import capo_bedrock_agentcore_control.types.modify_memory_strategies
    import capo_bedrock_agentcore_control.types.name
    import capo_bedrock_agentcore_control.types.namespace_keys_list
    import capo_bedrock_agentcore_control.types.non_empty_string
    import capo_bedrock_agentcore_control.types.stream_delivery_resources
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_memory_input
    import capo_bedrock_agentcore_control.types.update_memory_output
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class MemoryResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agentcore_control.types.name.Name",
        event_expiry_duration: int,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "capo_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
        ] = None,
        indexed_keys: Optional[
            "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        namespace_keys: Optional[
            "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput":
        """<p>Creates a new Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            name: <p>The name of the memory. The name must be unique within your account.</p>
            description: <p>The description of the memory.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>
            memory_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>
            event_expiry_duration: <p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>
            memory_strategies: <p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>
            indexed_keys: <p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>
            namespace_keys: <p>The namespace variable key definitions with optional validation rules. Use these <code>namespaceKeys</code> in <code>namespaceTemplates</code> to control namespace hierarchy.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory.create_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_memory_input

            return capo_bedrock_agentcore_control.types.create_memory_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_memory_output

            return capo_bedrock_agentcore_control.types.create_memory_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateMemory", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput = {
            "name": name,
            "event_expiry_duration": event_expiry_duration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if indexed_keys is not None:
            input_["indexed_keys"] = indexed_keys
        if namespace_keys is not None:
            input_["namespace_keys"] = namespace_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        view: Optional[
            "capo_bedrock_agentcore_control.types.memory_view.MemoryView"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput":
        """<p>Retrieve an existing Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to retrieve.</p>
            view: <p>The level of detail to return for the memory.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory.get_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_memory_output

            return (
                capo_bedrock_agentcore_control.types.get_memory_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetMemory", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput = {
            "memory_id": memory_id
        }
        if view is not None:
            input_["view"] = view

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        event_expiry_duration: Optional[int] = None,
        memory_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "capo_bedrock_agentcore_control.types.modify_memory_strategies.ModifyMemoryStrategies"
        ] = None,
        add_indexed_keys: Optional[
            "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        namespace_keys: Optional[
            "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput":
        """<p>Update an Amazon Bedrock AgentCore Memory resource memory.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique Amazon Web Services identifier.</p>
            memory_id: <p>The unique identifier of the memory to update.</p>
            description: <p>The updated description of the AgentCore Memory resource.</p>
            event_expiry_duration: <p>The number of days after which memory events will expire, between 7 and 365 days.</p>
            memory_execution_role_arn: <p>The ARN of the IAM role that provides permissions for the AgentCore Memory resource.</p>
            memory_strategies: <p>The memory strategies to add, modify, or delete.</p>
            add_indexed_keys: <p>Additional metadata keys to index. Previously indexed keys cannot be removed.</p>
            namespace_keys: <p>The namespace variable key definitions with validation rules for this memory. This value fully replaces the existing set — any key you omit is removed. Any referenced <code>namespaceKey</code> omission will throw ValidationException.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory.update_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_memory_input

            return capo_bedrock_agentcore_control.types.update_memory_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_memory_output

            return capo_bedrock_agentcore_control.types.update_memory_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateMemory", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput = {
            "memory_id": memory_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if event_expiry_duration is not None:
            input_["event_expiry_duration"] = event_expiry_duration
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if add_indexed_keys is not None:
            input_["add_indexed_keys"] = add_indexed_keys
        if namespace_keys is not None:
            input_["namespace_keys"] = namespace_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput":
        """<p>Deletes an Amazon Bedrock AgentCore Memory resource. When you delete a memory resource, it is permanently removed.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique Amazon Web Services identifier.</p>
            memory_id: <p>The unique identifier of the memory to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory.delete_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMemory")
        )
        input_: capo_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput = {
            "memory_id": memory_id
        }
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
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput":
        """<p>Lists the available Amazon Bedrock AgentCore Memory resources in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories.list_memories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMemories")
        )
        input_: capo_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput = {}
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


class AsyncMemoryResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agentcore_control.types.name.Name",
        event_expiry_duration: int,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "capo_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
        ] = None,
        indexed_keys: Optional[
            "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        namespace_keys: Optional[
            "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput":
        """<p>Creates a new Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            name: <p>The name of the memory. The name must be unique within your account.</p>
            description: <p>The description of the memory.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>
            memory_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>
            event_expiry_duration: <p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>
            memory_strategies: <p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>
            indexed_keys: <p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>
            namespace_keys: <p>The namespace variable key definitions with optional validation rules. Use these <code>namespaceKeys</code> in <code>namespaceTemplates</code> to control namespace hierarchy.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory.async_create_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_memory_input

            return capo_bedrock_agentcore_control.types.create_memory_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_memory_output

            return capo_bedrock_agentcore_control.types.create_memory_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateMemory", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput = {
            "name": name,
            "event_expiry_duration": event_expiry_duration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if indexed_keys is not None:
            input_["indexed_keys"] = indexed_keys
        if namespace_keys is not None:
            input_["namespace_keys"] = namespace_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        view: Optional[
            "capo_bedrock_agentcore_control.types.memory_view.MemoryView"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput":
        """<p>Retrieve an existing Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to retrieve.</p>
            view: <p>The level of detail to return for the memory.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory.async_get_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_memory_output

            return (
                capo_bedrock_agentcore_control.types.get_memory_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetMemory", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput = {
            "memory_id": memory_id
        }
        if view is not None:
            input_["view"] = view

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        event_expiry_duration: Optional[int] = None,
        memory_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "capo_bedrock_agentcore_control.types.modify_memory_strategies.ModifyMemoryStrategies"
        ] = None,
        add_indexed_keys: Optional[
            "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        namespace_keys: Optional[
            "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput":
        """<p>Update an Amazon Bedrock AgentCore Memory resource memory.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique Amazon Web Services identifier.</p>
            memory_id: <p>The unique identifier of the memory to update.</p>
            description: <p>The updated description of the AgentCore Memory resource.</p>
            event_expiry_duration: <p>The number of days after which memory events will expire, between 7 and 365 days.</p>
            memory_execution_role_arn: <p>The ARN of the IAM role that provides permissions for the AgentCore Memory resource.</p>
            memory_strategies: <p>The memory strategies to add, modify, or delete.</p>
            add_indexed_keys: <p>Additional metadata keys to index. Previously indexed keys cannot be removed.</p>
            namespace_keys: <p>The namespace variable key definitions with validation rules for this memory. This value fully replaces the existing set — any key you omit is removed. Any referenced <code>namespaceKey</code> omission will throw ValidationException.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory.async_update_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_memory_input

            return capo_bedrock_agentcore_control.types.update_memory_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_memory_output

            return capo_bedrock_agentcore_control.types.update_memory_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateMemory", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput = {
            "memory_id": memory_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if event_expiry_duration is not None:
            input_["event_expiry_duration"] = event_expiry_duration
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if add_indexed_keys is not None:
            input_["add_indexed_keys"] = add_indexed_keys
        if namespace_keys is not None:
            input_["namespace_keys"] = namespace_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput":
        """<p>Deletes an Amazon Bedrock AgentCore Memory resource. When you delete a memory resource, it is permanently removed.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique Amazon Web Services identifier.</p>
            memory_id: <p>The unique identifier of the memory to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory.async_delete_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMemory")
        )
        input_: capo_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput = {
            "memory_id": memory_id
        }
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
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput":
        """<p>Lists the available Amazon Bedrock AgentCore Memory resources in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories.async_list_memories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMemories")
        )
        input_: capo_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput = {}
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
