from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_rule_request
    import capo_vpc_lattice.types.create_rule_response
    import capo_vpc_lattice.types.delete_rule_request
    import capo_vpc_lattice.types.delete_rule_response
    import capo_vpc_lattice.types.get_rule_request
    import capo_vpc_lattice.types.get_rule_response
    import capo_vpc_lattice.types.list_rules_request
    import capo_vpc_lattice.types.list_rules_response
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.rule_identifier
    import capo_vpc_lattice.types.rule_match
    import capo_vpc_lattice.types.rule_name
    import capo_vpc_lattice.types.rule_priority
    import capo_vpc_lattice.types.rule_summary
    import capo_vpc_lattice.types.service_identifier
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.update_rule_request
    import capo_vpc_lattice.types.update_rule_response
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class Rule:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        name: "capo_vpc_lattice.types.rule_name.RuleName",
        match: "capo_vpc_lattice.types.rule_match.RuleMatch",
        priority: "capo_vpc_lattice.types.rule_priority.RulePriority",
        action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_rule_response.CreateRuleResponse":
        """<p>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            name: <p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            match: <p>The rule match.</p>
            priority: <p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>
            action: <p>The action for the default rule.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_rule_request.CreateRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_rule_response.CreateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_rule_request.CreateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "name": name,
            "match": match,
            "priority": priority,
            "action": action,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_rule_response.GetRuleResponse":
        """<p>Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the listener rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_rule_request.GetRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_rule_response.GetRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_rule.get_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_rule_request.GetRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        match: Optional["capo_vpc_lattice.types.rule_match.RuleMatch"] = None,
        priority: Optional["capo_vpc_lattice.types.rule_priority.RulePriority"] = None,
        action: Optional["capo_vpc_lattice.types.rule_action.RuleAction"] = None,
    ) -> "capo_vpc_lattice.types.update_rule_response.UpdateRuleResponse":
        """<p>Updates a specified rule for the listener. You can't modify a default listener rule. To modify a default listener rule, use <code>UpdateListener</code>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
            match: <p>The rule match.</p>
            priority: <p>The rule priority. A listener can't have multiple rules with the same priority.</p>
            action: <p>Information about the action for the specified listener rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_rule_request.UpdateRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_rule_response.UpdateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_rule.update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_rule_request.UpdateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }
        if match is not None:
            input_["match"] = match
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_rule_response.DeleteRuleResponse":
        """<p>Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_rule_request.DeleteRuleRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_rule

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_rule_request.DeleteRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_rules_response.ListRulesResponse":
        """<p>Lists the rules for the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_rules_request.ListRulesRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_rules_response.ListRulesResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_rules

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_rules_request.ListRulesRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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


class AsyncRule:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        name: "capo_vpc_lattice.types.rule_name.RuleName",
        match: "capo_vpc_lattice.types.rule_match.RuleMatch",
        priority: "capo_vpc_lattice.types.rule_priority.RulePriority",
        action: "capo_vpc_lattice.types.rule_action.RuleAction",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_rule_response.CreateRuleResponse":
        """<p>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            name: <p>The name of the rule. The name must be unique within the listener. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            match: <p>The rule match.</p>
            priority: <p>The priority assigned to the rule. Each rule for a specific listener must have a unique priority. The lower the priority number the higher the priority.</p>
            action: <p>The action for the default rule.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_rule_request.CreateRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_rule_response.CreateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_rule

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_rule_request.CreateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "name": name,
            "match": match,
            "priority": priority,
            "action": action,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_rule_response.GetRuleResponse":
        """<p>Retrieves information about the specified listener rules. You can also retrieve information about the default listener rule. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the listener rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_rule_request.GetRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_rule_response.GetRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_rule

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_rule_request.GetRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        match: Optional["capo_vpc_lattice.types.rule_match.RuleMatch"] = None,
        priority: Optional["capo_vpc_lattice.types.rule_priority.RulePriority"] = None,
        action: Optional["capo_vpc_lattice.types.rule_action.RuleAction"] = None,
    ) -> "capo_vpc_lattice.types.update_rule_response.UpdateRuleResponse":
        """<p>Updates a specified rule for the listener. You can't modify a default listener rule. To modify a default listener rule, use <code>UpdateListener</code>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>
            match: <p>The rule match.</p>
            priority: <p>The rule priority. A listener can't have multiple rules with the same priority.</p>
            action: <p>Information about the action for the specified listener rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.update_rule_request.UpdateRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.update_rule_response.UpdateRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_rule

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_rule_request.UpdateRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }
        if match is not None:
            input_["match"] = match
        if priority is not None:
            input_["priority"] = priority
        if action is not None:
            input_["action"] = action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_rule_response.DeleteRuleResponse":
        """<p>Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules">Listener rules</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            rule_identifier: <p>The ID or ARN of the rule.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_rule_request.DeleteRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_rule

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_rule_request.DeleteRuleRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
            "rule_identifier": rule_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier",
        listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_rules_response.ListRulesResponse":
        """<p>Lists the rules for the specified listener.</p>

        Args:
            service_identifier: <p>The ID or ARN of the service.</p>
            listener_identifier: <p>The ID or ARN of the listener.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_rules_request.ListRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_rules_response.ListRulesResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_rules

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_rules_request.ListRulesRequest = {
            "service_identifier": service_identifier,
            "listener_identifier": listener_identifier,
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
