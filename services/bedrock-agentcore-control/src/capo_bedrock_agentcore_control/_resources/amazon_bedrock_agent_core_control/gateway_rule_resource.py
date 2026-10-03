from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.actions
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.conditions
    import capo_bedrock_agentcore_control.types.create_gateway_rule_request
    import capo_bedrock_agentcore_control.types.create_gateway_rule_response
    import capo_bedrock_agentcore_control.types.delete_gateway_rule_request
    import capo_bedrock_agentcore_control.types.delete_gateway_rule_response
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rule_description
    import capo_bedrock_agentcore_control.types.gateway_rule_detail
    import capo_bedrock_agentcore_control.types.gateway_rule_id
    import capo_bedrock_agentcore_control.types.gateway_rule_max_results
    import capo_bedrock_agentcore_control.types.gateway_rule_next_token
    import capo_bedrock_agentcore_control.types.gateway_rule_priority
    import capo_bedrock_agentcore_control.types.get_gateway_rule_request
    import capo_bedrock_agentcore_control.types.get_gateway_rule_response
    import capo_bedrock_agentcore_control.types.list_gateway_rules_request
    import capo_bedrock_agentcore_control.types.list_gateway_rules_response
    import capo_bedrock_agentcore_control.types.update_gateway_rule_request
    import capo_bedrock_agentcore_control.types.update_gateway_rule_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class GatewayRuleResource:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        priority: "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority",
        actions: "capo_bedrock_agentcore_control.types.actions.Actions",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        conditions: Optional[
            "capo_bedrock_agentcore_control.types.conditions.Conditions"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_rule_response.CreateGatewayRuleResponse":
        """<p>Creates a rule for a gateway. Rules define conditions and actions that control how requests are routed and processed through the gateway, including principal-based access control and path-based routing.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to create a rule for.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            priority: <p>The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first. Must be between 1 and 1,000,000.</p>
            conditions: <p>The conditions that must be met for the rule to apply. Conditions can match on principals (IAM ARNs) or request paths.</p>
            actions: <p>The actions to take when the rule conditions are met. Actions can route to a specific target or apply a configuration bundle override.</p>
            description: <p>The description of the gateway rule.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_gateway_rule_request.CreateGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_rule_response.CreateGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rule.create_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_rule_request.CreateGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "priority": priority,
            "actions": actions,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if conditions is not None:
            input_["conditions"] = conditions
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_rule_response.DeleteGatewayRuleResponse":
        """<p>Deletes a gateway rule.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to delete.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_rule_request.DeleteGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_rule_response.DeleteGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rule.delete_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_rule_request.DeleteGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_rule_response.GetGatewayRuleResponse":
        """<p>Retrieves detailed information about a specific gateway rule.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_gateway_rule_request.GetGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_rule_response.GetGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rule.get_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_rule_request.GetGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_rules(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_max_results.GatewayRuleMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_next_token.GatewayRuleNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_rules_response.ListGatewayRulesResponse":
        """<p>Lists all rules for a gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to list rules for.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>The pagination token from a previous request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_gateway_rules_request.ListGatewayRulesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_rules_response.ListGatewayRulesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rules

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rules.list_gateway_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_rules_request.ListGatewayRulesRequest = {
            "gateway_identifier": gateway_identifier
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

    def update_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        priority: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
        ] = None,
        conditions: Optional[
            "capo_bedrock_agentcore_control.types.conditions.Conditions"
        ] = None,
        actions: Optional[
            "capo_bedrock_agentcore_control.types.actions.Actions"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_rule_response.UpdateGatewayRuleResponse":
        """<p>Updates a gateway rule's priority, conditions, actions, or description.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to update.</p>
            priority: <p>The updated priority of the rule.</p>
            conditions: <p>The updated conditions for the rule.</p>
            actions: <p>The updated actions for the rule.</p>
            description: <p>The updated description of the rule.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_gateway_rule_request.UpdateGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_rule_response.UpdateGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rule.update_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_rule_request.UpdateGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }
        if priority is not None:
            input_["priority"] = priority
        if conditions is not None:
            input_["conditions"] = conditions
        if actions is not None:
            input_["actions"] = actions
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGatewayRuleResource:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        priority: "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority",
        actions: "capo_bedrock_agentcore_control.types.actions.Actions",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        conditions: Optional[
            "capo_bedrock_agentcore_control.types.conditions.Conditions"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_rule_response.CreateGatewayRuleResponse":
        """<p>Creates a rule for a gateway. Rules define conditions and actions that control how requests are routed and processed through the gateway, including principal-based access control and path-based routing.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to create a rule for.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            priority: <p>The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first. Must be between 1 and 1,000,000.</p>
            conditions: <p>The conditions that must be met for the rule to apply. Conditions can match on principals (IAM ARNs) or request paths.</p>
            actions: <p>The actions to take when the rule conditions are met. Actions can route to a specific target or apply a configuration bundle override.</p>
            description: <p>The description of the gateway rule.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_gateway_rule_request.CreateGatewayRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_rule_response.CreateGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rule

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rule.async_create_gateway_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_rule_request.CreateGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "priority": priority,
            "actions": actions,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if conditions is not None:
            input_["conditions"] = conditions
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_rule_response.DeleteGatewayRuleResponse":
        """<p>Deletes a gateway rule.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_rule_request.DeleteGatewayRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_rule_response.DeleteGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rule

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rule.async_delete_gateway_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_rule_request.DeleteGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_rule_response.GetGatewayRuleResponse":
        """<p>Retrieves detailed information about a specific gateway rule.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_gateway_rule_request.GetGatewayRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_rule_response.GetGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rule

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rule.async_get_gateway_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_rule_request.GetGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_gateway_rules(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_max_results.GatewayRuleMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_next_token.GatewayRuleNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_rules_response.ListGatewayRulesResponse":
        """<p>Lists all rules for a gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to list rules for.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>The pagination token from a previous request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_gateway_rules_request.ListGatewayRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_rules_response.ListGatewayRulesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rules

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rules.async_list_gateway_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_rules_request.ListGatewayRulesRequest = {
            "gateway_identifier": gateway_identifier
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

    async def update_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        priority: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
        ] = None,
        conditions: Optional[
            "capo_bedrock_agentcore_control.types.conditions.Conditions"
        ] = None,
        actions: Optional[
            "capo_bedrock_agentcore_control.types.actions.Actions"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_rule_response.UpdateGatewayRuleResponse":
        """<p>Updates a gateway rule's priority, conditions, actions, or description.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to update.</p>
            priority: <p>The updated priority of the rule.</p>
            conditions: <p>The updated conditions for the rule.</p>
            actions: <p>The updated actions for the rule.</p>
            description: <p>The updated description of the rule.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_gateway_rule_request.UpdateGatewayRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_rule_response.UpdateGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rule

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rule.async_update_gateway_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_rule_request.UpdateGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }
        if priority is not None:
            input_["priority"] = priority
        if conditions is not None:
            input_["conditions"] = conditions
        if actions is not None:
            input_["actions"] = actions
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
