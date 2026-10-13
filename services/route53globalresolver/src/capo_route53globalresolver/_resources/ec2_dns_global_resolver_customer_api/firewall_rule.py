from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_route53globalresolver._auth._signers
import capo_route53globalresolver._auth._sigv4
from capo_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_route53globalresolver.types.batch_create_firewall_rule_input
    import capo_route53globalresolver.types.batch_create_firewall_rule_input_items
    import capo_route53globalresolver.types.batch_create_firewall_rule_output
    import capo_route53globalresolver.types.batch_delete_firewall_rule_input
    import capo_route53globalresolver.types.batch_delete_firewall_rule_input_items
    import capo_route53globalresolver.types.batch_delete_firewall_rule_output
    import capo_route53globalresolver.types.batch_update_firewall_rule_input
    import capo_route53globalresolver.types.batch_update_firewall_rule_input_items
    import capo_route53globalresolver.types.batch_update_firewall_rule_output
    import capo_route53globalresolver.types.block_override_dns_query_type
    import capo_route53globalresolver.types.block_override_ttl
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.confidence_threshold
    import capo_route53globalresolver.types.create_firewall_rule_input
    import capo_route53globalresolver.types.create_firewall_rule_output
    import capo_route53globalresolver.types.delete_firewall_rule_input
    import capo_route53globalresolver.types.delete_firewall_rule_output
    import capo_route53globalresolver.types.dns_advanced_protection
    import capo_route53globalresolver.types.dns_query_type
    import capo_route53globalresolver.types.domain
    import capo_route53globalresolver.types.filters
    import capo_route53globalresolver.types.firewall_block_response
    import capo_route53globalresolver.types.firewall_rule_action
    import capo_route53globalresolver.types.firewall_rule_priority
    import capo_route53globalresolver.types.firewall_rules_item
    import capo_route53globalresolver.types.get_firewall_rule_input
    import capo_route53globalresolver.types.get_firewall_rule_output
    import capo_route53globalresolver.types.list_firewall_rules_input
    import capo_route53globalresolver.types.list_firewall_rules_output
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.update_firewall_rule_input
    import capo_route53globalresolver.types.update_firewall_rule_output
    from capo_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from capo_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class FirewallRule:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        action: "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        block_override_dns_type: Optional[
            "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "capo_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        firewall_domain_list_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
        priority: Optional[
            "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
        q_type: Optional[
            "capo_route53globalresolver.types.dns_query_type.DnsQueryType"
        ] = None,
    ) -> "capo_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput":
        """<p>Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to CloudWatch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>.</p> </li> </ul>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_response: <p>The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.</p>
            description: <p>An optional description for the firewall rule.</p>
            dns_advanced_protection: <p>Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.</p>
            firewall_domain_list_id: <p>The ID of the firewall domain list to use in this rule.</p>
            name: <p>A descriptive name for the firewall rule.</p>
            priority: <p>The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this firewall rule.</p>
            q_type: <p>The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule.create_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFirewallRule")
        )
        input_: capo_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput = {
            "action": action,
            "name": name,
            "dns_view_id": dns_view_id,
        }
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        if priority is not None:
            input_["priority"] = priority
        if q_type is not None:
            input_["q_type"] = q_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput":
        """<p>Retrieves information about a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>ID of the DNS Firewall rule.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule.get_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFirewallRule")
        )
        input_: capo_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput = {
            "firewall_rule_id": firewall_rule_id
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
        client_token: "capo_route53globalresolver.types.client_token.ClientToken",
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        action: Optional[
            "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
        ] = None,
        block_override_dns_type: Optional[
            "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "capo_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        priority: Optional[
            "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput":
        """<p>Updates the configuration of a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_response: <p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>
            description: <p>The description for the Firewall rule.</p>
            dns_advanced_protection: <p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>
            firewall_rule_id: <p>The ID of the DNS Firewall rule.</p>
            name: <p>The name of the DNS Firewall rule.</p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule.update_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFirewallRule")
        )
        input_: capo_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput = {
            "client_token": client_token,
            "firewall_rule_id": firewall_rule_id,
        }
        if action is not None:
            input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput":
        """<p>Deletes a DNS firewall rule. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>The unique identifier of the firewall rule to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule.delete_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFirewallRule")
        )
        input_: capo_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput = {
            "firewall_rule_id": firewall_rule_id
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
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput":
        """<p>Lists all DNS firewall rules for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>ID of the DNS view.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules.list_firewall_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFirewallRules")
        )
        input_: capo_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput = {
            "dns_view_id": dns_view_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_create_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_create_firewall_rule_input_items.BatchCreateFirewallRuleInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput":
        """<p>Creates multiple DNS firewall rules in a single operation. This is more efficient than creating rules individually when you need to set up multiple rules at once.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The <code>BatchCreateFirewallRuleInputItem</code> objects contain the information for each Firewall rule.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule.batch_create_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchCreateFirewallRule")
        )
        input_: capo_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput":
        """<p>Deletes multiple DNS firewall rules in a single operation. This is more efficient than deleting rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>An array of the DNS Firewall IDs to be deleted.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule.batch_delete_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchDeleteFirewallRule")
        )
        input_: capo_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_update_firewall_rule_input_items.BatchUpdateFirewallRuleInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput":
        """<p>Updates multiple DNS firewall rules in a single operation. This is more efficient than updating rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The DNS Firewall rule IDs to be updated.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput]",
        ) -> OperationResponse[
            "capo_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule

            output, http_response = (
                capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule.batch_update_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchUpdateFirewallRule")
        )
        input_: capo_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFirewallRule:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        action: "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction",
        name: "capo_route53globalresolver.types.resource_name.ResourceName",
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        block_override_dns_type: Optional[
            "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "capo_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        client_token: Optional[
            "capo_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        firewall_domain_list_id: Optional[
            "capo_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
        priority: Optional[
            "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
        q_type: Optional[
            "capo_route53globalresolver.types.dns_query_type.DnsQueryType"
        ] = None,
    ) -> "capo_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput":
        """<p>Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to CloudWatch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>.</p> </li> </ul>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_response: <p>The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.</p>
            description: <p>An optional description for the firewall rule.</p>
            dns_advanced_protection: <p>Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.</p>
            firewall_domain_list_id: <p>The ID of the firewall domain list to use in this rule.</p>
            name: <p>A descriptive name for the firewall rule.</p>
            priority: <p>The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this firewall rule.</p>
            q_type: <p>The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule.async_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateFirewallRule")
        )
        input_: capo_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput = {
            "action": action,
            "name": name,
            "dns_view_id": dns_view_id,
        }
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        if priority is not None:
            input_["priority"] = priority
        if q_type is not None:
            input_["q_type"] = q_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput":
        """<p>Retrieves information about a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>ID of the DNS Firewall rule.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule.async_get_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetFirewallRule")
        )
        input_: capo_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput = {
            "firewall_rule_id": firewall_rule_id
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
        client_token: "capo_route53globalresolver.types.client_token.ClientToken",
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        action: Optional[
            "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
        ] = None,
        block_override_dns_type: Optional[
            "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "capo_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        confidence_threshold: Optional[
            "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "capo_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        name: Optional[
            "capo_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        priority: Optional[
            "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
    ) -> "capo_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput":
        """<p>Updates the configuration of a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_response: <p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>
            description: <p>The description for the Firewall rule.</p>
            dns_advanced_protection: <p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>
            firewall_rule_id: <p>The ID of the DNS Firewall rule.</p>
            name: <p>The name of the DNS Firewall rule.</p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule.async_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateFirewallRule")
        )
        input_: capo_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput = {
            "client_token": client_token,
            "firewall_rule_id": firewall_rule_id,
        }
        if action is not None:
            input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        firewall_rule_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput":
        """<p>Deletes a DNS firewall rule. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>The unique identifier of the firewall rule to delete.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule.async_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteFirewallRule")
        )
        input_: capo_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput = {
            "firewall_rule_id": firewall_rule_id
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
        dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["capo_route53globalresolver.types.filters.Filters"] = None,
    ) -> "capo_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput":
        """<p>Lists all DNS firewall rules for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>ID of the DNS view.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules.async_list_firewall_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListFirewallRules")
        )
        input_: capo_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput = {
            "dns_view_id": dns_view_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_create_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_create_firewall_rule_input_items.BatchCreateFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput":
        """<p>Creates multiple DNS firewall rules in a single operation. This is more efficient than creating rules individually when you need to set up multiple rules at once.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The <code>BatchCreateFirewallRuleInputItem</code> objects contain the information for each Firewall rule.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule.async_batch_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchCreateFirewallRule")
        )
        input_: capo_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput":
        """<p>Deletes multiple DNS firewall rules in a single operation. This is more efficient than deleting rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>An array of the DNS Firewall IDs to be deleted.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule.async_batch_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchDeleteFirewallRule")
        )
        input_: capo_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_firewall_rule(
        self,
        firewall_rules: "capo_route53globalresolver.types.batch_update_firewall_rule_input_items.BatchUpdateFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "capo_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput":
        """<p>Updates multiple DNS firewall rules in a single operation. This is more efficient than updating rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The DNS Firewall rule IDs to be updated.</p>

        Raises:
            capo_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            capo_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            capo_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            capo_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            capo_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput"
        ]:
            import capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule

            (
                output,
                http_response,
            ) = await capo_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule.async_batch_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchUpdateFirewallRule")
        )
        input_: capo_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput = {
            "firewall_rules": firewall_rules
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
