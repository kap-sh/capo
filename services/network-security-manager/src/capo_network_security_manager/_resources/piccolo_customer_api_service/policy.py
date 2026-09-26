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
    import capo_network_security_manager.types.create_policy_input
    import capo_network_security_manager.types.create_policy_output
    import capo_network_security_manager.types.create_policy_snapshot_input
    import capo_network_security_manager.types.create_policy_snapshot_output
    import capo_network_security_manager.types.delete_policy_input
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.get_policy_input
    import capo_network_security_manager.types.get_policy_output
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.list_policies_input
    import capo_network_security_manager.types.list_policies_output
    import capo_network_security_manager.types.list_policy_snapshots_input
    import capo_network_security_manager.types.list_policy_snapshots_output
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.policy_configuration
    import capo_network_security_manager.types.policy_firewall_type
    import capo_network_security_manager.types.policy_identifier
    import capo_network_security_manager.types.policy_name
    import capo_network_security_manager.types.policy_summary
    import capo_network_security_manager.types.priority
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.template_and_rule_reference_list
    import capo_network_security_manager.types.update_policy_input
    import capo_network_security_manager.types.update_policy_output
    import capo_network_security_manager.types.update_token
    from capo_network_security_manager._services.async_network_security_manager import (
        AsyncNetworkSecurityManagerClient,
        AsyncNetworkSecurityManagerClientConfig,
    )
    from capo_network_security_manager._services.network_security_manager import (
        NetworkSecurityManagerClient,
        NetworkSecurityManagerClientConfig,
    )


class Policy:
    def __init__(self, service: NetworkSecurityManagerClient) -> None:
        self._service = service

    def create(
        self,
        policy_name: "capo_network_security_manager.types.policy_name.PolicyName",
        priority: "capo_network_security_manager.types.priority.Priority",
        firewall_type: "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType",
        policy_configuration: "capo_network_security_manager.types.policy_configuration.PolicyConfiguration",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        policy_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        associated_template_and_rule_list: Optional[
            "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_policy_output.CreatePolicyOutput":
        """<p>Creates a policy. A policy combines templates and rules with enforcement settings for a firewall type, such as AWS WAF or AWS Shield Advanced. Use <code>isPublished</code> to create the policy in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            policy_name: <p>The name of the policy.</p>
            policy_description: <p>A description of the policy.</p>
            priority: <p>The priority of the resource. A lower number indicates a higher priority.</p>
            associated_template_and_rule_list: <p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            policy_configuration: <p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>
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
            Create a WAF policy
            Creates a new WAF policy in draft state with a template association.

            >>> client.create(client_token='550e8400-e29b-41d4-a716-446655440002', policy_name='web-app-waf-policy', policy_description='WAF policy for web application protection', firewall_type='WAF', priority=1, associated_template_and_rule_list=[{'templateIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789'}], policy_configuration={'remediationEnabled': False, 'resourcesCleanUp': False, 'wafConfig': {'existingCustomerWebACLResolution': 'NO_REMEDIATION', 'conflictResolution': 'MERGE_WHERE_APPLICABLE'}}, is_published=False)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_policy_input.CreatePolicyInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_policy_output.CreatePolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_policy.create_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_policy_input.CreatePolicyInput = {
            "policy_name": policy_name,
            "priority": priority,
            "firewall_type": firewall_type,
            "policy_configuration": policy_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if associated_template_and_rule_list is not None:
            input_["associated_template_and_rule_list"] = (
                associated_template_and_rule_list
            )
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
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_policy_output.GetPolicyOutput":
        """<p>Retrieves the details of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a policy
            Retrieves the current published version of a policy by its base ARN, including its associated templates and rules and its enforcement configuration.

            >>> client.read(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_policy_input.GetPolicyInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_policy_output.GetPolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_policy_input.GetPolicyInput = {
            "policy_identifier": policy_identifier
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
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        policy_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        priority: Optional[
            "capo_network_security_manager.types.priority.Priority"
        ] = None,
        associated_template_and_rule_list: Optional[
            "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
        ] = None,
        policy_configuration: Optional[
            "capo_network_security_manager.types.policy_configuration.PolicyConfiguration"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_policy_output.UpdatePolicyOutput":
        """<p>Updates the specified policy. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the policy as a draft.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            policy_description: <p>A description of the policy.</p>
            priority: <p>The priority of the resource. A lower number indicates a higher priority.</p>
            associated_template_and_rule_list: <p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>
            policy_configuration: <p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>
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
            Update a policy and publish it
            Updates the policy's description, priority, and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', update_token='e3f4a5b6-6c7d-4e8f-9a0b-0c1d2e3f4a5b', policy_description='WAF policy for web application protection - updated', priority=2, associated_template_and_rule_list=[{'templateIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789'}], policy_configuration={'remediationEnabled': True, 'resourcesCleanUp': False, 'wafConfig': {'existingCustomerWebACLResolution': 'NO_REMEDIATION', 'conflictResolution': 'MERGE_WHERE_APPLICABLE'}}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_policy_input.UpdatePolicyInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_policy_output.UpdatePolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_policy.update_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_policy_input.UpdatePolicyInput = {
            "policy_identifier": policy_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if priority is not None:
            input_["priority"] = priority
        if associated_template_and_rule_list is not None:
            input_["associated_template_and_rule_list"] = (
                associated_template_and_rule_list
            )
        if policy_configuration is not None:
            input_["policy_configuration"] = policy_configuration
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
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a policy
            Deletes a policy by its ARN. The policy must not be associated with any deployment.

            >>> client.delete(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_policy_input.DeletePolicyInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_policy_input.DeletePolicyInput = {
            "policy_identifier": policy_identifier
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
    ) -> "capo_network_security_manager.types.list_policies_output.ListPoliciesOutput":
        """<p>Lists the policies in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

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
            List policies
            Lists the published policies in the account, one page at a time.

            >>> client.list(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_policies_input.ListPoliciesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_policies_output.ListPoliciesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_policies

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_policies_input.ListPoliciesInput = {}
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

    def create_policy_snapshot(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_policy_snapshot_output.CreatePolicySnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
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
            Create a policy snapshot
            Creates an immutable snapshot of the current published version of a policy. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_policy_snapshot(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', client_token='550e8400-e29b-41d4-a716-446655440013')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_policy_snapshot_input.CreatePolicySnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_policy_snapshot_output.CreatePolicySnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_policy_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_policy_snapshot.create_policy_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_policy_snapshot_input.CreatePolicySnapshotInput = {
            "policy_identifier": policy_identifier
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

    def list_policy_snapshots(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_policy_snapshots_output.ListPolicySnapshotsOutput":
        """<p>Lists the snapshots of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a policy
            Lists the immutable snapshots that have been created for a policy.

            >>> client.list_policy_snapshots(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_policy_snapshots_input.ListPolicySnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_policy_snapshots_output.ListPolicySnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_policy_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_policy_snapshots.list_policy_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_policy_snapshots_input.ListPolicySnapshotsInput = {
            "policy_identifier": policy_identifier
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


class AsyncPolicy:
    def __init__(self, service: AsyncNetworkSecurityManagerClient) -> None:
        self._service = service

    async def create(
        self,
        policy_name: "capo_network_security_manager.types.policy_name.PolicyName",
        priority: "capo_network_security_manager.types.priority.Priority",
        firewall_type: "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType",
        policy_configuration: "capo_network_security_manager.types.policy_configuration.PolicyConfiguration",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        policy_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        associated_template_and_rule_list: Optional[
            "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_policy_output.CreatePolicyOutput":
        """<p>Creates a policy. A policy combines templates and rules with enforcement settings for a firewall type, such as AWS WAF or AWS Shield Advanced. Use <code>isPublished</code> to create the policy in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            policy_name: <p>The name of the policy.</p>
            policy_description: <p>A description of the policy.</p>
            priority: <p>The priority of the resource. A lower number indicates a higher priority.</p>
            associated_template_and_rule_list: <p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            policy_configuration: <p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>
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
            Create a WAF policy
            Creates a new WAF policy in draft state with a template association.

            >>> await client.create(client_token='550e8400-e29b-41d4-a716-446655440002', policy_name='web-app-waf-policy', policy_description='WAF policy for web application protection', firewall_type='WAF', priority=1, associated_template_and_rule_list=[{'templateIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789'}], policy_configuration={'remediationEnabled': False, 'resourcesCleanUp': False, 'wafConfig': {'existingCustomerWebACLResolution': 'NO_REMEDIATION', 'conflictResolution': 'MERGE_WHERE_APPLICABLE'}}, is_published=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_policy_input.CreatePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_policy_output.CreatePolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_policy

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_policy.async_create_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_policy_input.CreatePolicyInput = {
            "policy_name": policy_name,
            "priority": priority,
            "firewall_type": firewall_type,
            "policy_configuration": policy_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if associated_template_and_rule_list is not None:
            input_["associated_template_and_rule_list"] = (
                associated_template_and_rule_list
            )
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
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_policy_output.GetPolicyOutput":
        """<p>Retrieves the details of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a policy
            Retrieves the current published version of a policy by its base ARN, including its associated templates and rules and its enforcement configuration.

            >>> await client.read(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.get_policy_input.GetPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.get_policy_output.GetPolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_policy

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_policy_input.GetPolicyInput = {
            "policy_identifier": policy_identifier
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
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        policy_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        priority: Optional[
            "capo_network_security_manager.types.priority.Priority"
        ] = None,
        associated_template_and_rule_list: Optional[
            "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
        ] = None,
        policy_configuration: Optional[
            "capo_network_security_manager.types.policy_configuration.PolicyConfiguration"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_policy_output.UpdatePolicyOutput":
        """<p>Updates the specified policy. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the policy as a draft.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            policy_description: <p>A description of the policy.</p>
            priority: <p>The priority of the resource. A lower number indicates a higher priority.</p>
            associated_template_and_rule_list: <p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>
            policy_configuration: <p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>
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
            Update a policy and publish it
            Updates the policy's description, priority, and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> await client.update(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', update_token='e3f4a5b6-6c7d-4e8f-9a0b-0c1d2e3f4a5b', policy_description='WAF policy for web application protection - updated', priority=2, associated_template_and_rule_list=[{'templateIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789'}], policy_configuration={'remediationEnabled': True, 'resourcesCleanUp': False, 'wafConfig': {'existingCustomerWebACLResolution': 'NO_REMEDIATION', 'conflictResolution': 'MERGE_WHERE_APPLICABLE'}}, is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.update_policy_input.UpdatePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.update_policy_output.UpdatePolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_policy

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.update_policy.async_update_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_policy_input.UpdatePolicyInput = {
            "policy_identifier": policy_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if priority is not None:
            input_["priority"] = priority
        if associated_template_and_rule_list is not None:
            input_["associated_template_and_rule_list"] = (
                associated_template_and_rule_list
            )
        if policy_configuration is not None:
            input_["policy_configuration"] = policy_configuration
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
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a policy
            Deletes a policy by its ARN. The policy must not be associated with any deployment.

            >>> await client.delete(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.delete_policy_input.DeletePolicyInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_policy

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.delete_policy.async_delete_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_policy_input.DeletePolicyInput = {
            "policy_identifier": policy_identifier
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
    ) -> "capo_network_security_manager.types.list_policies_output.ListPoliciesOutput":
        """<p>Lists the policies in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

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
            List policies
            Lists the published policies in the account, one page at a time.

            >>> await client.list(max_results=10, status='ACTIVE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_policies_input.ListPoliciesInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_policies_output.ListPoliciesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_policies

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_policies.async_list_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_policies_input.ListPoliciesInput = {}
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

    async def create_policy_snapshot(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_policy_snapshot_output.CreatePolicySnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
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
            Create a policy snapshot
            Creates an immutable snapshot of the current published version of a policy. The snapshot is addressable by a version-qualified ARN.

            >>> await client.create_policy_snapshot(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', client_token='550e8400-e29b-41d4-a716-446655440013')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_policy_snapshot_input.CreatePolicySnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_policy_snapshot_output.CreatePolicySnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_policy_snapshot

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_policy_snapshot.async_create_policy_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_policy_snapshot_input.CreatePolicySnapshotInput = {
            "policy_identifier": policy_identifier
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

    async def list_policy_snapshots(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_policy_snapshots_output.ListPolicySnapshotsOutput":
        """<p>Lists the snapshots of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a policy
            Lists the immutable snapshots that have been created for a policy.

            >>> await client.list_policy_snapshots(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_policy_snapshots_input.ListPolicySnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_policy_snapshots_output.ListPolicySnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_policy_snapshots

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_policy_snapshots.async_list_policy_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_policy_snapshots_input.ListPolicySnapshotsInput = {
            "policy_identifier": policy_identifier
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
