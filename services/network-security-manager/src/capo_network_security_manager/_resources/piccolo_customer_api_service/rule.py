from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_network_security_manager._auth._signers
import capo_network_security_manager._auth._sigv4
from capo_network_security_manager._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.create_rule_input
    import capo_network_security_manager.types.create_rule_output
    import capo_network_security_manager.types.create_rule_snapshot_input
    import capo_network_security_manager.types.create_rule_snapshot_output
    import capo_network_security_manager.types.delete_rule_input
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.get_rule_input
    import capo_network_security_manager.types.get_rule_output
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.json_document
    import capo_network_security_manager.types.list_rule_snapshots_input
    import capo_network_security_manager.types.list_rule_snapshots_output
    import capo_network_security_manager.types.list_rules_input
    import capo_network_security_manager.types.list_rules_output
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.rule_firewall_type
    import capo_network_security_manager.types.rule_identifier
    import capo_network_security_manager.types.rule_name
    import capo_network_security_manager.types.rule_summary
    import capo_network_security_manager.types.rule_type
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.update_rule_input
    import capo_network_security_manager.types.update_rule_output
    import capo_network_security_manager.types.update_token
    from capo_network_security_manager._services.async_network_security_manager import (
        AsyncNetworkSecurityManagerClient,
        AsyncNetworkSecurityManagerClientConfig,
    )
    from capo_network_security_manager._services.network_security_manager import (
        NetworkSecurityManagerClient,
        NetworkSecurityManagerClientConfig,
    )


class Rule:
    def __init__(self, service: NetworkSecurityManagerClient) -> None:
        self._service = service

    def create(
        self,
        rule_name: "capo_network_security_manager.types.rule_name.RuleName",
        firewall_type: "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType",
        rule_type: "capo_network_security_manager.types.rule_type.RuleType",
        configuration: "capo_network_security_manager.types.json_document.JsonDocument",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        rule_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_rule_output.CreateRuleOutput":
        r"""<p>Creates a rule. A rule defines a network security configuration to enforce, such as an AWS WAF rule group or configuration data. Use <code>isPublished</code> to create the rule in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            rule_name: <p>The name of the rule.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            rule_description: <p>A description of the rule.</p>
            configuration: <p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a WAF rule
            Creates a new WAF inspection rule in draft state.

            >>> client.create(client_token='550e8400-e29b-41d4-a716-446655440000', rule_name='block-known-bad-ips', firewall_type='WAF', rule_type='INSPECTION', rule_description='Blocks requests from known malicious IP addresses', configuration={}, is_published=False)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_rule_input.CreateRuleInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_rule_input.CreateRuleInput = {
            "rule_name": rule_name,
            "firewall_type": firewall_type,
            "rule_type": rule_type,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rule_description is not None:
            input_["rule_description"] = rule_description
        if is_published is not None:
            input_["is_published"] = is_published
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
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_rule_output.GetRuleOutput":
        """<p>Retrieves the details of the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a rule
            Retrieves the current published version of a rule by its base ARN.

            >>> client.read(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123')
            Get a specific version of a rule
            Retrieves a specific immutable version (snapshot) of a rule using a version-qualified ARN. The response has isSnapshot set to true. Omitting the version qualifier returns the current published rule instead.

            >>> client.read(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123:3')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_rule_input.GetRuleInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_rule_output.GetRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_rule.get_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_rule_input.GetRuleInput = {
            "rule_identifier": rule_identifier
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
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        rule_type: Optional[
            "capo_network_security_manager.types.rule_type.RuleType"
        ] = None,
        rule_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        configuration: Optional[
            "capo_network_security_manager.types.json_document.JsonDocument"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_rule_output.UpdateRuleOutput":
        r"""<p>Updates the specified rule. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the rule as a draft.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            rule_description: <p>A description of the rule.</p>
            configuration: <p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a rule and publish it
            Updates the rule's description and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', update_token='c1d2e3f4-4a5b-4c6d-9e7f-8a9b0c1d2e3f', rule_type='INSPECTION', rule_description='Blocks requests from known malicious IP addresses - updated list', configuration={}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_rule_input.UpdateRuleInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_rule_output.UpdateRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_rule.update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_rule_input.UpdateRuleInput = {
            "rule_identifier": rule_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if rule_type is not None:
            input_["rule_type"] = rule_type
        if rule_description is not None:
            input_["rule_description"] = rule_description
        if configuration is not None:
            input_["configuration"] = configuration
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
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a rule
            Deletes a rule by its ARN. The rule must not be associated with any template or policy.

            >>> client.delete(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_rule_input.DeleteRuleInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_rule_input.DeleteRuleInput = {
            "rule_identifier": rule_identifier
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
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "capo_network_security_manager.types.list_rules_output.ListRulesOutput":
        """<p>Lists the rules in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status, either <code>ACTIVE</code> or <code>DRAFT</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List rules
            Lists the published rules in the account, one page at a time.

            >>> client.list(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_rules_input.ListRulesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_rules_output.ListRulesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_rules

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_rules_input.ListRulesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_rule_snapshot(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_rule_snapshot_output.CreateRuleSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified rule. A snapshot is an immutable, versioned copy that other resources can reference.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a rule snapshot
            Creates an immutable snapshot of the current published version of a rule. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_rule_snapshot(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', client_token='550e8400-e29b-41d4-a716-446655440011')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_rule_snapshot_input.CreateRuleSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_rule_snapshot_output.CreateRuleSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_rule_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_rule_snapshot.create_rule_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_rule_snapshot_input.CreateRuleSnapshotInput = {
            "rule_identifier": rule_identifier
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

    def list_rule_snapshots(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_rule_snapshots_output.ListRuleSnapshotsOutput":
        """<p>Lists the snapshots of the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a rule
            Lists the immutable snapshots that have been created for a rule.

            >>> client.list_rule_snapshots(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_rule_snapshots_input.ListRuleSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_rule_snapshots_output.ListRuleSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_rule_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_rule_snapshots.list_rule_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_rule_snapshots_input.ListRuleSnapshotsInput = {
            "rule_identifier": rule_identifier
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
    def __init__(self, service: AsyncNetworkSecurityManagerClient) -> None:
        self._service = service

    async def create(
        self,
        rule_name: "capo_network_security_manager.types.rule_name.RuleName",
        firewall_type: "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType",
        rule_type: "capo_network_security_manager.types.rule_type.RuleType",
        configuration: "capo_network_security_manager.types.json_document.JsonDocument",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        rule_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_rule_output.CreateRuleOutput":
        r"""<p>Creates a rule. A rule defines a network security configuration to enforce, such as an AWS WAF rule group or configuration data. Use <code>isPublished</code> to create the rule in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            rule_name: <p>The name of the rule.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            rule_description: <p>A description of the rule.</p>
            configuration: <p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a WAF rule
            Creates a new WAF inspection rule in draft state.

            >>> await client.create(client_token='550e8400-e29b-41d4-a716-446655440000', rule_name='block-known-bad-ips', firewall_type='WAF', rule_type='INSPECTION', rule_description='Blocks requests from known malicious IP addresses', configuration={}, is_published=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_rule_input.CreateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_rule

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_rule_input.CreateRuleInput = {
            "rule_name": rule_name,
            "firewall_type": firewall_type,
            "rule_type": rule_type,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rule_description is not None:
            input_["rule_description"] = rule_description
        if is_published is not None:
            input_["is_published"] = is_published
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
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_rule_output.GetRuleOutput":
        """<p>Retrieves the details of the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a rule
            Retrieves the current published version of a rule by its base ARN.

            >>> await client.read(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123')
            Get a specific version of a rule
            Retrieves a specific immutable version (snapshot) of a rule using a version-qualified ARN. The response has isSnapshot set to true. Omitting the version qualifier returns the current published rule instead.

            >>> await client.read(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123:3')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.get_rule_input.GetRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.get_rule_output.GetRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_rule

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_rule_input.GetRuleInput = {
            "rule_identifier": rule_identifier
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
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        rule_type: Optional[
            "capo_network_security_manager.types.rule_type.RuleType"
        ] = None,
        rule_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        configuration: Optional[
            "capo_network_security_manager.types.json_document.JsonDocument"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_rule_output.UpdateRuleOutput":
        r"""<p>Updates the specified rule. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the rule as a draft.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            rule_description: <p>A description of the rule.</p>
            configuration: <p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a rule and publish it
            Updates the rule's description and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> await client.update(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', update_token='c1d2e3f4-4a5b-4c6d-9e7f-8a9b0c1d2e3f', rule_type='INSPECTION', rule_description='Blocks requests from known malicious IP addresses - updated list', configuration={}, is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.update_rule_input.UpdateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.update_rule_output.UpdateRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_rule

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_rule_input.UpdateRuleInput = {
            "rule_identifier": rule_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if rule_type is not None:
            input_["rule_type"] = rule_type
        if rule_description is not None:
            input_["rule_description"] = rule_description
        if configuration is not None:
            input_["configuration"] = configuration
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
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a rule
            Deletes a rule by its ARN. The rule must not be associated with any template or policy.

            >>> await client.delete(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.delete_rule_input.DeleteRuleInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_rule

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_rule_input.DeleteRuleInput = {
            "rule_identifier": rule_identifier
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
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "capo_network_security_manager.types.list_rules_output.ListRulesOutput":
        """<p>Lists the rules in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status, either <code>ACTIVE</code> or <code>DRAFT</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List rules
            Lists the published rules in the account, one page at a time.

            >>> await client.list(max_results=10, status='ACTIVE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_rules_input.ListRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_rules_output.ListRulesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_rules

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_rules_input.ListRulesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_rule_snapshot(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_rule_snapshot_output.CreateRuleSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified rule. A snapshot is an immutable, versioned copy that other resources can reference.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a rule snapshot
            Creates an immutable snapshot of the current published version of a rule. The snapshot is addressable by a version-qualified ARN.

            >>> await client.create_rule_snapshot(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', client_token='550e8400-e29b-41d4-a716-446655440011')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_rule_snapshot_input.CreateRuleSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_rule_snapshot_output.CreateRuleSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_rule_snapshot

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_rule_snapshot.async_create_rule_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_rule_snapshot_input.CreateRuleSnapshotInput = {
            "rule_identifier": rule_identifier
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

    async def list_rule_snapshots(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_rule_snapshots_output.ListRuleSnapshotsOutput":
        """<p>Lists the snapshots of the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a rule
            Lists the immutable snapshots that have been created for a rule.

            >>> await client.list_rule_snapshots(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_rule_snapshots_input.ListRuleSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_rule_snapshots_output.ListRuleSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_rule_snapshots

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_rule_snapshots.async_list_rule_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_rule_snapshots_input.ListRuleSnapshotsInput = {
            "rule_identifier": rule_identifier
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
