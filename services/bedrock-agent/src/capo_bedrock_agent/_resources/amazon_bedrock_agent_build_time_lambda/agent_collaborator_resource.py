from __future__ import annotations

import uuid
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
    import capo_bedrock_agent.types.agent_collaborator_summary
    import capo_bedrock_agent.types.agent_descriptor
    import capo_bedrock_agent.types.associate_agent_collaborator_request
    import capo_bedrock_agent.types.associate_agent_collaborator_response
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.collaboration_instruction
    import capo_bedrock_agent.types.disassociate_agent_collaborator_request
    import capo_bedrock_agent.types.disassociate_agent_collaborator_response
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.get_agent_collaborator_request
    import capo_bedrock_agent.types.get_agent_collaborator_response
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.list_agent_collaborators_request
    import capo_bedrock_agent.types.list_agent_collaborators_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.relay_conversation_history
    import capo_bedrock_agent.types.update_agent_collaborator_request
    import capo_bedrock_agent.types.update_agent_collaborator_response
    import capo_bedrock_agent.types.version
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class AgentCollaboratorResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def associate_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "capo_bedrock_agent.types.name.Name",
        collaboration_instruction: "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse":
        """<p>Makes an agent a collaborator for another agent.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>An agent version.</p>
            agent_descriptor: <p>The alias of the collaborator agent.</p>
            collaborator_name: <p>A name for the collaborator.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator.associate_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.associate_agent_collaborator_request

            return capo_bedrock_agent.types.associate_agent_collaborator_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.associate_agent_collaborator_response

            return capo_bedrock_agent.types.associate_agent_collaborator_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AssociateAgentCollaborator",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "agent_descriptor": agent_descriptor,
            "collaborator_name": collaborator_name,
            "collaboration_instruction": collaboration_instruction,
        }
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history
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

    def disassociate_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse":
        """<p>Disassociates an agent collaborator.</p>

        Args:
            agent_id: <p>An agent ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator.disassociate_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateAgentCollaborator")
        )
        input_: capo_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse":
        """<p>Retrieves information about an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator.get_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.get_agent_collaborator_response

            return capo_bedrock_agent.types.get_agent_collaborator_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentCollaborator", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_agent_collaborators(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse":
        """<p>Retrieve a list of an agent's collaborators.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            max_results: <p>The maximum number of agent collaborators to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators.list_agent_collaborators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.list_agent_collaborators_response

            return capo_bedrock_agent.types.list_agent_collaborators_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentCollaborators", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    def update_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "capo_bedrock_agent.types.name.Name",
        collaboration_instruction: "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse":
        """<p>Updates an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
            agent_descriptor: <p>An agent descriptor for the agent collaborator.</p>
            collaborator_name: <p>The collaborator's name.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator.update_agent_collaborator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_agent_collaborator_request

            return capo_bedrock_agent.types.update_agent_collaborator_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_agent_collaborator_response

            return capo_bedrock_agent.types.update_agent_collaborator_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAgentCollaborator",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
            "agent_descriptor": agent_descriptor,
            "collaborator_name": collaborator_name,
            "collaboration_instruction": collaboration_instruction,
        }
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAgentCollaboratorResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def associate_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "capo_bedrock_agent.types.name.Name",
        collaboration_instruction: "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse":
        """<p>Makes an agent a collaborator for another agent.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>An agent version.</p>
            agent_descriptor: <p>The alias of the collaborator agent.</p>
            collaborator_name: <p>A name for the collaborator.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>
            client_token: <p>A client token.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.associate_agent_collaborator.async_associate_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.associate_agent_collaborator_request

            return capo_bedrock_agent.types.associate_agent_collaborator_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.associate_agent_collaborator_response.AssociateAgentCollaboratorResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.associate_agent_collaborator_response

            return capo_bedrock_agent.types.associate_agent_collaborator_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "AssociateAgentCollaborator",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.associate_agent_collaborator_request.AssociateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "agent_descriptor": agent_descriptor,
            "collaborator_name": collaborator_name,
            "collaboration_instruction": collaboration_instruction,
        }
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history
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

    async def disassociate_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse":
        """<p>Disassociates an agent collaborator.</p>

        Args:
            agent_id: <p>An agent ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.disassociate_agent_collaborator_response.DisassociateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.disassociate_agent_collaborator.async_disassociate_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateAgentCollaborator")
        )
        input_: capo_bedrock_agent.types.disassociate_agent_collaborator_request.DisassociateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse":
        """<p>Retrieves information about an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_agent_collaborator.async_get_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.get_agent_collaborator_response.GetAgentCollaboratorResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.get_agent_collaborator_response

            return capo_bedrock_agent.types.get_agent_collaborator_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentCollaborator", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.get_agent_collaborator_request.GetAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_collaborators(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.version.Version",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse":
        """<p>Retrieve a list of an agent's collaborators.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            max_results: <p>The maximum number of agent collaborators to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_agent_collaborators.async_list_agent_collaborators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.list_agent_collaborators_response.ListAgentCollaboratorsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.list_agent_collaborators_response

            return capo_bedrock_agent.types.list_agent_collaborators_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentCollaborators", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.list_agent_collaborators_request.ListAgentCollaboratorsRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
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

    async def update_agent_collaborator(
        self,
        agent_id: "capo_bedrock_agent.types.id.Id",
        agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion",
        collaborator_id: "capo_bedrock_agent.types.id.Id",
        agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor",
        collaborator_name: "capo_bedrock_agent.types.name.Name",
        collaboration_instruction: "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        relay_conversation_history: Optional[
            "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse":
        """<p>Updates an agent's collaborator.</p>

        Args:
            agent_id: <p>The agent's ID.</p>
            agent_version: <p>The agent's version.</p>
            collaborator_id: <p>The collaborator's ID.</p>
            agent_descriptor: <p>An agent descriptor for the agent collaborator.</p>
            collaborator_name: <p>The collaborator's name.</p>
            collaboration_instruction: <p>Instruction for the collaborator.</p>
            relay_conversation_history: <p>A relay conversation history for the collaborator.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_agent_collaborator.async_update_agent_collaborator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_agent_collaborator_request

            return capo_bedrock_agent.types.update_agent_collaborator_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.update_agent_collaborator_response.UpdateAgentCollaboratorResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_agent_collaborator_response

            return capo_bedrock_agent.types.update_agent_collaborator_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAgentCollaborator",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.update_agent_collaborator_request.UpdateAgentCollaboratorRequest = {
            "agent_id": agent_id,
            "agent_version": agent_version,
            "collaborator_id": collaborator_id,
            "agent_descriptor": agent_descriptor,
            "collaborator_name": collaborator_name,
            "collaboration_instruction": collaboration_instruction,
        }
        if relay_conversation_history is not None:
            input_["relay_conversation_history"] = relay_conversation_history

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
