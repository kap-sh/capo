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
    import capo_network_security_manager.types.create_scope_input
    import capo_network_security_manager.types.create_scope_output
    import capo_network_security_manager.types.create_scope_snapshot_input
    import capo_network_security_manager.types.create_scope_snapshot_output
    import capo_network_security_manager.types.delete_scope_input
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.get_scope_input
    import capo_network_security_manager.types.get_scope_output
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.list_scope_snapshots_input
    import capo_network_security_manager.types.list_scope_snapshots_output
    import capo_network_security_manager.types.list_scopes_input
    import capo_network_security_manager.types.list_scopes_output
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.scope_configuration
    import capo_network_security_manager.types.scope_identifier
    import capo_network_security_manager.types.scope_name
    import capo_network_security_manager.types.scope_summary
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.update_scope_input
    import capo_network_security_manager.types.update_scope_output
    import capo_network_security_manager.types.update_token
    from capo_network_security_manager._services.async_network_security_manager import (
        AsyncNetworkSecurityManagerClient,
        AsyncNetworkSecurityManagerClientConfig,
    )
    from capo_network_security_manager._services.network_security_manager import (
        NetworkSecurityManagerClient,
        NetworkSecurityManagerClientConfig,
    )


class Scope:
    def __init__(self, service: NetworkSecurityManagerClient) -> None:
        self._service = service

    def create(
        self,
        scope_name: "capo_network_security_manager.types.scope_name.ScopeName",
        scope_configuration: "capo_network_security_manager.types.scope_configuration.ScopeConfiguration",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        scope_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_scope_output.CreateScopeOutput":
        """<p>Creates a scope. A scope selects the accounts and resources that a deployment applies to. Use <code>isPublished</code> to create the scope in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            scope_name: <p>The name of the scope.</p>
            scope_description: <p>A description of the scope.</p>
            scope_configuration: <p>The configuration that defines which accounts and resources are in scope.</p>
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
            Create a scope
            Creates a new scope in published (ACTIVE) state.

            >>> client.create(client_token='550e8400-e29b-41d4-a716-446655440001', scope_name='production-web-apps', scope_description='Scope covering all production web application resources', scope_configuration={'accountFilter': {'includeAll': {}}, 'resourceScopes': {}}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_scope_input.CreateScopeInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_scope_output.CreateScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_scope.create_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_scope_input.CreateScopeInput = {
            "scope_name": scope_name,
            "scope_configuration": scope_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scope_description is not None:
            input_["scope_description"] = scope_description
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
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_scope_output.GetScopeOutput":
        """<p>Retrieves the details of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a scope
            Retrieves the current published version of a scope by its base ARN.

            >>> client.read(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_scope_input.GetScopeInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_scope_output.GetScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_scope.get_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_scope_input.GetScopeInput = {
            "scope_identifier": scope_identifier
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
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        scope_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        scope_configuration: Optional[
            "capo_network_security_manager.types.scope_configuration.ScopeConfiguration"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_scope_output.UpdateScopeOutput":
        """<p>Updates the specified scope. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the scope as a draft.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            scope_description: <p>A description of the scope.</p>
            scope_configuration: <p>The configuration that defines which accounts and resources are in scope. If you don't include this member, the scope keeps its existing configuration.</p> <p>A new configuration can change which accounts and resources are selected, but it can't add or remove the account filter itself: a scope created for multi-account use stays multi-account, and a scope created for single-account use stays single-account.</p>
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
            Update a scope and publish it
            Updates the scope's description and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', update_token='b0c4d1e2-3f4a-4b5c-8d6e-7f8a9b0c1d2e', scope_description='Scope covering all production web application resources in US East 1', scope_configuration={'accountFilter': {'includeAll': {}}, 'resourceScopes': {}}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_scope_input.UpdateScopeInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_scope_output.UpdateScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_scope.update_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_scope_input.UpdateScopeInput = {
            "scope_identifier": scope_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if scope_description is not None:
            input_["scope_description"] = scope_description
        if scope_configuration is not None:
            input_["scope_configuration"] = scope_configuration
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
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a scope
            Deletes a scope by its ARN. The scope must not be associated with any deployment.

            >>> client.delete(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_scope_input.DeleteScopeInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_scope.delete_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_scope_input.DeleteScopeInput = {
            "scope_identifier": scope_identifier
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
    ) -> "capo_network_security_manager.types.list_scopes_output.ListScopesOutput":
        """<p>Lists the scopes in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status: <code>ACTIVE</code>, <code>DRAFT</code>, or <code>DISABLED</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List scopes
            Lists the published scopes in the account, one page at a time.

            >>> client.list(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_scopes_input.ListScopesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_scopes_output.ListScopesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_scopes

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_scopes.list_scopes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_scopes_input.ListScopesInput = {}
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

    def create_scope_snapshot(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_scope_snapshot_output.CreateScopeSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
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
            Create a scope snapshot
            Creates an immutable snapshot of the current published version of a scope. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_scope_snapshot(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', client_token='550e8400-e29b-41d4-a716-446655440010')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_scope_snapshot_input.CreateScopeSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_scope_snapshot_output.CreateScopeSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_scope_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_scope_snapshot.create_scope_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_scope_snapshot_input.CreateScopeSnapshotInput = {
            "scope_identifier": scope_identifier
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

    def list_scope_snapshots(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_scope_snapshots_output.ListScopeSnapshotsOutput":
        """<p>Lists the snapshots of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a scope
            Lists the immutable snapshots that have been created for a scope.

            >>> client.list_scope_snapshots(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_scope_snapshots_input.ListScopeSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_scope_snapshots_output.ListScopeSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_scope_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_scope_snapshots.list_scope_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_scope_snapshots_input.ListScopeSnapshotsInput = {
            "scope_identifier": scope_identifier
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


class AsyncScope:
    def __init__(self, service: AsyncNetworkSecurityManagerClient) -> None:
        self._service = service

    async def create(
        self,
        scope_name: "capo_network_security_manager.types.scope_name.ScopeName",
        scope_configuration: "capo_network_security_manager.types.scope_configuration.ScopeConfiguration",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        scope_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_scope_output.CreateScopeOutput":
        """<p>Creates a scope. A scope selects the accounts and resources that a deployment applies to. Use <code>isPublished</code> to create the scope in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            scope_name: <p>The name of the scope.</p>
            scope_description: <p>A description of the scope.</p>
            scope_configuration: <p>The configuration that defines which accounts and resources are in scope.</p>
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
            Create a scope
            Creates a new scope in published (ACTIVE) state.

            >>> await client.create(client_token='550e8400-e29b-41d4-a716-446655440001', scope_name='production-web-apps', scope_description='Scope covering all production web application resources', scope_configuration={'accountFilter': {'includeAll': {}}, 'resourceScopes': {}}, is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_scope_input.CreateScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_scope_output.CreateScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_scope

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_scope.async_create_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_scope_input.CreateScopeInput = {
            "scope_name": scope_name,
            "scope_configuration": scope_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scope_description is not None:
            input_["scope_description"] = scope_description
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
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_scope_output.GetScopeOutput":
        """<p>Retrieves the details of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a scope
            Retrieves the current published version of a scope by its base ARN.

            >>> await client.read(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.get_scope_input.GetScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.get_scope_output.GetScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_scope

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.get_scope.async_get_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_scope_input.GetScopeInput = {
            "scope_identifier": scope_identifier
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
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        scope_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        scope_configuration: Optional[
            "capo_network_security_manager.types.scope_configuration.ScopeConfiguration"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_scope_output.UpdateScopeOutput":
        """<p>Updates the specified scope. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the scope as a draft.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            scope_description: <p>A description of the scope.</p>
            scope_configuration: <p>The configuration that defines which accounts and resources are in scope. If you don't include this member, the scope keeps its existing configuration.</p> <p>A new configuration can change which accounts and resources are selected, but it can't add or remove the account filter itself: a scope created for multi-account use stays multi-account, and a scope created for single-account use stays single-account.</p>
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
            Update a scope and publish it
            Updates the scope's description and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> await client.update(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', update_token='b0c4d1e2-3f4a-4b5c-8d6e-7f8a9b0c1d2e', scope_description='Scope covering all production web application resources in US East 1', scope_configuration={'accountFilter': {'includeAll': {}}, 'resourceScopes': {}}, is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.update_scope_input.UpdateScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.update_scope_output.UpdateScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_scope

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.update_scope.async_update_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_scope_input.UpdateScopeInput = {
            "scope_identifier": scope_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if scope_description is not None:
            input_["scope_description"] = scope_description
        if scope_configuration is not None:
            input_["scope_configuration"] = scope_configuration
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
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a scope
            Deletes a scope by its ARN. The scope must not be associated with any deployment.

            >>> await client.delete(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.delete_scope_input.DeleteScopeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_scope

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.delete_scope.async_delete_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_scope_input.DeleteScopeInput = {
            "scope_identifier": scope_identifier
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
    ) -> "capo_network_security_manager.types.list_scopes_output.ListScopesOutput":
        """<p>Lists the scopes in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status: <code>ACTIVE</code>, <code>DRAFT</code>, or <code>DISABLED</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List scopes
            Lists the published scopes in the account, one page at a time.

            >>> await client.list(max_results=10, status='ACTIVE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_scopes_input.ListScopesInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_scopes_output.ListScopesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_scopes

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_scopes.async_list_scopes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_scopes_input.ListScopesInput = {}
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

    async def create_scope_snapshot(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_scope_snapshot_output.CreateScopeSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
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
            Create a scope snapshot
            Creates an immutable snapshot of the current published version of a scope. The snapshot is addressable by a version-qualified ARN.

            >>> await client.create_scope_snapshot(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', client_token='550e8400-e29b-41d4-a716-446655440010')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_scope_snapshot_input.CreateScopeSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_scope_snapshot_output.CreateScopeSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_scope_snapshot

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_scope_snapshot.async_create_scope_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_scope_snapshot_input.CreateScopeSnapshotInput = {
            "scope_identifier": scope_identifier
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

    async def list_scope_snapshots(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_scope_snapshots_output.ListScopeSnapshotsOutput":
        """<p>Lists the snapshots of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a scope
            Lists the immutable snapshots that have been created for a scope.

            >>> await client.list_scope_snapshots(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_scope_snapshots_input.ListScopeSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_scope_snapshots_output.ListScopeSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_scope_snapshots

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_scope_snapshots.async_list_scope_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_scope_snapshots_input.ListScopeSnapshotsInput = {
            "scope_identifier": scope_identifier
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
