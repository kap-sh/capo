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
    import capo_network_security_manager.types.create_template_input
    import capo_network_security_manager.types.create_template_output
    import capo_network_security_manager.types.create_template_snapshot_input
    import capo_network_security_manager.types.create_template_snapshot_output
    import capo_network_security_manager.types.delete_template_input
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.get_template_input
    import capo_network_security_manager.types.get_template_output
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.list_template_snapshots_input
    import capo_network_security_manager.types.list_template_snapshots_output
    import capo_network_security_manager.types.list_templates_input
    import capo_network_security_manager.types.list_templates_output
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.rule_reference_list
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.template_firewall_type
    import capo_network_security_manager.types.template_identifier
    import capo_network_security_manager.types.template_name
    import capo_network_security_manager.types.template_summary
    import capo_network_security_manager.types.update_template_input
    import capo_network_security_manager.types.update_template_output
    import capo_network_security_manager.types.update_token
    from capo_network_security_manager._services.async_network_security_manager import (
        AsyncNetworkSecurityManagerClient,
        AsyncNetworkSecurityManagerClientConfig,
    )
    from capo_network_security_manager._services.network_security_manager import (
        NetworkSecurityManagerClient,
        NetworkSecurityManagerClientConfig,
    )


class Template:
    def __init__(self, service: NetworkSecurityManagerClient) -> None:
        self._service = service

    def create(
        self,
        template_name: "capo_network_security_manager.types.template_name.TemplateName",
        associated_rule_list: "capo_network_security_manager.types.rule_reference_list.RuleReferenceList",
        firewall_type: "capo_network_security_manager.types.template_firewall_type.TemplateFirewallType",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        template_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_template_output.CreateTemplateOutput":
        """<p>Creates a template. A template groups one or more rules to simplify reuse across policies. You can also associate rules with a policy directly, without a template. Use <code>isPublished</code> to create the template in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            template_name: <p>The name of the template.</p>
            template_description: <p>A description of the template.</p>
            associated_rule_list: <p>The rules associated with the template.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
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
            Create a WAF template
            Creates a new WAF template in published (ACTIVE) state with an associated rule.

            >>> client.create(client_token='550e8400-e29b-41d4-a716-446655440004', template_name='standard-waf-template', template_description='Standard WAF template with baseline rule groups', firewall_type='WAF', associated_rule_list=[{'ruleIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123'}], is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_template_input.CreateTemplateInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_template_output.CreateTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_template.create_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_template_input.CreateTemplateInput = {
            "template_name": template_name,
            "associated_rule_list": associated_rule_list,
            "firewall_type": firewall_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if template_description is not None:
            input_["template_description"] = template_description
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
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_template_output.GetTemplateOutput":
        """<p>Retrieves the details of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a template
            Retrieves the current published version of a template by its base ARN, including its associated rules.

            >>> client.read(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_template_input.GetTemplateInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_template_output.GetTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_template.get_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_template_input.GetTemplateInput = {
            "template_identifier": template_identifier
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
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        template_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        associated_rule_list: Optional[
            "capo_network_security_manager.types.rule_reference_list.RuleReferenceList"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_template_output.UpdateTemplateOutput":
        """<p>Updates the specified template. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the template as a draft.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            template_description: <p>A description of the template.</p>
            associated_rule_list: <p>The rules associated with the template.</p>
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
            Update a template and publish it
            Updates the template's description and rule associations and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', update_token='d2e3f4a5-5b6c-4d7e-8f9a-9b0c1d2e3f4a', template_description='Standard WAF template with baseline rule groups - updated', associated_rule_list=[{'ruleIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123'}], is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_template_input.UpdateTemplateInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_template_output.UpdateTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_template.update_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_template_input.UpdateTemplateInput = {
            "template_identifier": template_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if template_description is not None:
            input_["template_description"] = template_description
        if associated_rule_list is not None:
            input_["associated_rule_list"] = associated_rule_list
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
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a template
            Deletes a template by its ARN. The template must not be associated with any policy.

            >>> client.delete(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_template_input.DeleteTemplateInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_template.delete_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_template_input.DeleteTemplateInput = {
            "template_identifier": template_identifier
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
    ) -> (
        "capo_network_security_manager.types.list_templates_output.ListTemplatesOutput"
    ):
        """<p>Lists the templates in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

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
            List templates
            Lists the published templates in the account, one page at a time.

            >>> client.list(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_templates_input.ListTemplatesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_templates_output.ListTemplatesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_templates

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_templates.list_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_templates_input.ListTemplatesInput = {}
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

    def create_template_snapshot(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_template_snapshot_output.CreateTemplateSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
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
            Create a template snapshot
            Creates an immutable snapshot of the current published version of a template. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_template_snapshot(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', client_token='550e8400-e29b-41d4-a716-446655440012')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_template_snapshot_input.CreateTemplateSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_template_snapshot_output.CreateTemplateSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_template_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_template_snapshot.create_template_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_template_snapshot_input.CreateTemplateSnapshotInput = {
            "template_identifier": template_identifier
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

    def list_template_snapshots(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_template_snapshots_output.ListTemplateSnapshotsOutput":
        """<p>Lists the snapshots of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a template
            Lists the immutable snapshots that have been created for a template.

            >>> client.list_template_snapshots(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_template_snapshots_input.ListTemplateSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_template_snapshots_output.ListTemplateSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_template_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_template_snapshots.list_template_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_template_snapshots_input.ListTemplateSnapshotsInput = {
            "template_identifier": template_identifier
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


class AsyncTemplate:
    def __init__(self, service: AsyncNetworkSecurityManagerClient) -> None:
        self._service = service

    async def create(
        self,
        template_name: "capo_network_security_manager.types.template_name.TemplateName",
        associated_rule_list: "capo_network_security_manager.types.rule_reference_list.RuleReferenceList",
        firewall_type: "capo_network_security_manager.types.template_firewall_type.TemplateFirewallType",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        template_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_template_output.CreateTemplateOutput":
        """<p>Creates a template. A template groups one or more rules to simplify reuse across policies. You can also associate rules with a policy directly, without a template. Use <code>isPublished</code> to create the template in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            template_name: <p>The name of the template.</p>
            template_description: <p>A description of the template.</p>
            associated_rule_list: <p>The rules associated with the template.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
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
            Create a WAF template
            Creates a new WAF template in published (ACTIVE) state with an associated rule.

            >>> await client.create(client_token='550e8400-e29b-41d4-a716-446655440004', template_name='standard-waf-template', template_description='Standard WAF template with baseline rule groups', firewall_type='WAF', associated_rule_list=[{'ruleIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123'}], is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_template_input.CreateTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_template_output.CreateTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_template

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_template_input.CreateTemplateInput = {
            "template_name": template_name,
            "associated_rule_list": associated_rule_list,
            "firewall_type": firewall_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if template_description is not None:
            input_["template_description"] = template_description
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
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_template_output.GetTemplateOutput":
        """<p>Retrieves the details of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a template
            Retrieves the current published version of a template by its base ARN, including its associated rules.

            >>> await client.read(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.get_template_input.GetTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.get_template_output.GetTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_template

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_template_input.GetTemplateInput = {
            "template_identifier": template_identifier
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
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        template_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        associated_rule_list: Optional[
            "capo_network_security_manager.types.rule_reference_list.RuleReferenceList"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_template_output.UpdateTemplateOutput":
        """<p>Updates the specified template. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the template as a draft.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            template_description: <p>A description of the template.</p>
            associated_rule_list: <p>The rules associated with the template.</p>
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
            Update a template and publish it
            Updates the template's description and rule associations and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> await client.update(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', update_token='d2e3f4a5-5b6c-4d7e-8f9a-9b0c1d2e3f4a', template_description='Standard WAF template with baseline rule groups - updated', associated_rule_list=[{'ruleIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123'}], is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.update_template_input.UpdateTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.update_template_output.UpdateTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_template

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_template_input.UpdateTemplateInput = {
            "template_identifier": template_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if template_description is not None:
            input_["template_description"] = template_description
        if associated_rule_list is not None:
            input_["associated_rule_list"] = associated_rule_list
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
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a template
            Deletes a template by its ARN. The template must not be associated with any policy.

            >>> await client.delete(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.delete_template_input.DeleteTemplateInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_template

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_template_input.DeleteTemplateInput = {
            "template_identifier": template_identifier
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
    ) -> (
        "capo_network_security_manager.types.list_templates_output.ListTemplatesOutput"
    ):
        """<p>Lists the templates in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

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
            List templates
            Lists the published templates in the account, one page at a time.

            >>> await client.list(max_results=10, status='ACTIVE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_templates_input.ListTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_templates_output.ListTemplatesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_templates

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_templates_input.ListTemplatesInput = {}
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

    async def create_template_snapshot(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_template_snapshot_output.CreateTemplateSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
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
            Create a template snapshot
            Creates an immutable snapshot of the current published version of a template. The snapshot is addressable by a version-qualified ARN.

            >>> await client.create_template_snapshot(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', client_token='550e8400-e29b-41d4-a716-446655440012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_template_snapshot_input.CreateTemplateSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_template_snapshot_output.CreateTemplateSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_template_snapshot

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_template_snapshot.async_create_template_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_template_snapshot_input.CreateTemplateSnapshotInput = {
            "template_identifier": template_identifier
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

    async def list_template_snapshots(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_template_snapshots_output.ListTemplateSnapshotsOutput":
        """<p>Lists the snapshots of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a template
            Lists the immutable snapshots that have been created for a template.

            >>> await client.list_template_snapshots(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_template_snapshots_input.ListTemplateSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_template_snapshots_output.ListTemplateSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_template_snapshots

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_template_snapshots.async_list_template_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_template_snapshots_input.ListTemplateSnapshotsInput = {
            "template_identifier": template_identifier
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
