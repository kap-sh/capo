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
    import capo_network_security_manager.types.create_deployment_input
    import capo_network_security_manager.types.create_deployment_output
    import capo_network_security_manager.types.create_deployment_snapshot_input
    import capo_network_security_manager.types.create_deployment_snapshot_output
    import capo_network_security_manager.types.delete_deployment_input
    import capo_network_security_manager.types.deployment_configuration
    import capo_network_security_manager.types.deployment_identifier
    import capo_network_security_manager.types.deployment_name
    import capo_network_security_manager.types.deployment_summary
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.get_deployment_input
    import capo_network_security_manager.types.get_deployment_output
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.list_deployment_snapshots_input
    import capo_network_security_manager.types.list_deployment_snapshots_output
    import capo_network_security_manager.types.list_deployments_input
    import capo_network_security_manager.types.list_deployments_output
    import capo_network_security_manager.types.list_resource_synchronization_statuses_input
    import capo_network_security_manager.types.list_resource_synchronization_statuses_output
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.policy_reference_list
    import capo_network_security_manager.types.resource_synchronization_status_summary
    import capo_network_security_manager.types.scope_reference_list
    import capo_network_security_manager.types.synchronization_status
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.update_deployment_input
    import capo_network_security_manager.types.update_deployment_output
    import capo_network_security_manager.types.update_token
    from capo_network_security_manager._services.async_network_security_manager import (
        AsyncNetworkSecurityManagerClient,
        AsyncNetworkSecurityManagerClientConfig,
    )
    from capo_network_security_manager._services.network_security_manager import (
        NetworkSecurityManagerClient,
        NetworkSecurityManagerClientConfig,
    )


class Deployment:
    def __init__(self, service: NetworkSecurityManagerClient) -> None:
        self._service = service

    def create(
        self,
        deployment_name: "capo_network_security_manager.types.deployment_name.DeploymentName",
        deployment_configuration: "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration",
        associated_policy_list: "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList",
        associated_scope_list: "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        deployment_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_deployment_output.CreateDeploymentOutput":
        """<p>Creates a deployment. A deployment applies one or more policies to the accounts and resources selected by a scope. Use <code>isPublished</code> to create the deployment in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state. The response includes coverage information and any warnings about the deployment.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            deployment_name: <p>The name of the deployment.</p>
            deployment_description: <p>A description of the deployment.</p>
            deployment_configuration: <p>The configuration settings for the deployment.</p>
            associated_policy_list: <p>The policies associated with the deployment.</p>
            associated_scope_list: <p>The scope associated with the deployment. A deployment has exactly one scope.</p>
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
            Create a deployment
            Creates a new deployment in draft state.

            >>> client.create(client_token='550e8400-e29b-41d4-a716-446655440003', deployment_name='prod-us-east-1-deployment', deployment_description='Production deployment for US East 1 region', associated_policy_list=[{'policyIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789'}], associated_scope_list=[{'scopeIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123'}], deployment_configuration={'enableCrossAccountVisibility': False}, is_published=False)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_deployment_input.CreateDeploymentInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_deployment_input.CreateDeploymentInput = {
            "deployment_name": deployment_name,
            "deployment_configuration": deployment_configuration,
            "associated_policy_list": associated_policy_list,
            "associated_scope_list": associated_scope_list,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deployment_description is not None:
            input_["deployment_description"] = deployment_description
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
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> (
        "capo_network_security_manager.types.get_deployment_output.GetDeploymentOutput"
    ):
        """<p>Retrieves the details of the specified deployment, including coverage information and any warnings.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a deployment
            Retrieves the current published version of a deployment by its base ARN, including per-firewall-type coverage showing which in-scope resource types each policy protects.

            >>> client.read(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_deployment_input.GetDeploymentInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_deployment_input.GetDeploymentInput = {
            "deployment_identifier": deployment_identifier
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
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        deployment_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        deployment_configuration: Optional[
            "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        associated_policy_list: Optional[
            "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList"
        ] = None,
        associated_scope_list: Optional[
            "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_deployment_output.UpdateDeploymentOutput":
        """<p>Updates the specified deployment. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the deployment as a draft.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            deployment_description: <p>A description of the deployment.</p>
            deployment_configuration: <p>The configuration settings for the deployment.</p>
            associated_policy_list: <p>The policies associated with the deployment.</p>
            associated_scope_list: <p>The scope associated with the deployment. A deployment has exactly one scope.</p>
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
            Update a deployment and publish it
            Updates the deployment's associations and publishes the change. The response includes deploymentCoverage showing which resource types the associated policies can protect. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', update_token='f4a5b6c7-7d8e-4f9a-8b1c-1d2e3f4a5b6c', deployment_description='Production deployment for US East 1 region - updated', associated_policy_list=[{'policyIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789'}], associated_scope_list=[{'scopeIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123'}], deployment_configuration={'enableCrossAccountVisibility': True}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_deployment_input.UpdateDeploymentInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_deployment_output.UpdateDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_deployment.update_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_deployment_input.UpdateDeploymentInput = {
            "deployment_identifier": deployment_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if deployment_description is not None:
            input_["deployment_description"] = deployment_description
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if associated_policy_list is not None:
            input_["associated_policy_list"] = associated_policy_list
        if associated_scope_list is not None:
            input_["associated_scope_list"] = associated_scope_list
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
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a deployment
            Deletes a deployment by its ARN. Deleting an active deployment stops enforcement and triggers cleanup of managed firewall resources.

            >>> client.delete(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_deployment.delete_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput = {
            "deployment_identifier": deployment_identifier
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
    ) -> "capo_network_security_manager.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

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
            List deployments
            Lists the published deployments in the account, one page at a time.

            >>> client.list(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_deployments_input.ListDeploymentsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_deployments

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_deployments_input.ListDeploymentsInput = {}
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

    def create_deployment_snapshot(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_deployment_snapshot_output.CreateDeploymentSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
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
            Create a deployment snapshot
            Creates an immutable snapshot of the current published version of a deployment. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_deployment_snapshot(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', client_token='550e8400-e29b-41d4-a716-446655440014')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_deployment_snapshot_input.CreateDeploymentSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_deployment_snapshot_output.CreateDeploymentSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment_snapshot.create_deployment_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_deployment_snapshot_input.CreateDeploymentSnapshotInput = {
            "deployment_identifier": deployment_identifier
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

    def list_deployment_snapshots(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_deployment_snapshots_output.ListDeploymentSnapshotsOutput":
        """<p>Lists the snapshots of the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a deployment
            Lists the immutable snapshots that have been created for a deployment.

            >>> client.list_deployment_snapshots(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_deployment_snapshots_input.ListDeploymentSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_deployment_snapshots_output.ListDeploymentSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_deployment_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_deployment_snapshots.list_deployment_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_deployment_snapshots_input.ListDeploymentSnapshotsInput = {
            "deployment_identifier": deployment_identifier
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

    def list_resource_synchronization_statuses(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        synchronization_status: Optional[
            "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
        ] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_resource_synchronization_statuses_output.ListResourceSynchronizationStatusesOutput":
        """<p>Lists the synchronization statuses of the resources covered by the specified deployment. You can filter the results by synchronization status and page through them.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment to list synchronization statuses for. This is the deployment's Amazon Resource Name (ARN).</p>
            synchronization_status: <p>Filters the results by synchronization status, such as <code>IN_SYNC</code> or <code>OUT_OF_SYNC</code>.</p>
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
            List out-of-sync resources for a deployment
            Lists the resources tracked by a deployment that are out of sync, including the structured reason. Here a CloudFront distribution has no web ACL where the policy requires one.

            >>> client.list_resource_synchronization_statuses(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', synchronization_status='OUT_OF_SYNC', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_resource_synchronization_statuses_input.ListResourceSynchronizationStatusesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_resource_synchronization_statuses_output.ListResourceSynchronizationStatusesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_synchronization_statuses

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_synchronization_statuses.list_resource_synchronization_statuses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_resource_synchronization_statuses_input.ListResourceSynchronizationStatusesInput = {
            "deployment_identifier": deployment_identifier
        }
        if synchronization_status is not None:
            input_["synchronization_status"] = synchronization_status
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


class AsyncDeployment:
    def __init__(self, service: AsyncNetworkSecurityManagerClient) -> None:
        self._service = service

    async def create(
        self,
        deployment_name: "capo_network_security_manager.types.deployment_name.DeploymentName",
        deployment_configuration: "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration",
        associated_policy_list: "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList",
        associated_scope_list: "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        deployment_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_deployment_output.CreateDeploymentOutput":
        """<p>Creates a deployment. A deployment applies one or more policies to the accounts and resources selected by a scope. Use <code>isPublished</code> to create the deployment in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state. The response includes coverage information and any warnings about the deployment.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            deployment_name: <p>The name of the deployment.</p>
            deployment_description: <p>A description of the deployment.</p>
            deployment_configuration: <p>The configuration settings for the deployment.</p>
            associated_policy_list: <p>The policies associated with the deployment.</p>
            associated_scope_list: <p>The scope associated with the deployment. A deployment has exactly one scope.</p>
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
            Create a deployment
            Creates a new deployment in draft state.

            >>> await client.create(client_token='550e8400-e29b-41d4-a716-446655440003', deployment_name='prod-us-east-1-deployment', deployment_description='Production deployment for US East 1 region', associated_policy_list=[{'policyIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789'}], associated_scope_list=[{'scopeIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123'}], deployment_configuration={'enableCrossAccountVisibility': False}, is_published=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_deployment_input.CreateDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment.async_create_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_deployment_input.CreateDeploymentInput = {
            "deployment_name": deployment_name,
            "deployment_configuration": deployment_configuration,
            "associated_policy_list": associated_policy_list,
            "associated_scope_list": associated_scope_list,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deployment_description is not None:
            input_["deployment_description"] = deployment_description
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
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> (
        "capo_network_security_manager.types.get_deployment_output.GetDeploymentOutput"
    ):
        """<p>Retrieves the details of the specified deployment, including coverage information and any warnings.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a deployment
            Retrieves the current published version of a deployment by its base ARN, including per-firewall-type coverage showing which in-scope resource types each policy protects.

            >>> await client.read(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.get_deployment_input.GetDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_deployment

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_deployment_input.GetDeploymentInput = {
            "deployment_identifier": deployment_identifier
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
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        deployment_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        deployment_configuration: Optional[
            "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        associated_policy_list: Optional[
            "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList"
        ] = None,
        associated_scope_list: Optional[
            "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_deployment_output.UpdateDeploymentOutput":
        """<p>Updates the specified deployment. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the deployment as a draft.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            deployment_description: <p>A description of the deployment.</p>
            deployment_configuration: <p>The configuration settings for the deployment.</p>
            associated_policy_list: <p>The policies associated with the deployment.</p>
            associated_scope_list: <p>The scope associated with the deployment. A deployment has exactly one scope.</p>
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
            Update a deployment and publish it
            Updates the deployment's associations and publishes the change. The response includes deploymentCoverage showing which resource types the associated policies can protect. The updateToken from the most recent read is required for optimistic locking.

            >>> await client.update(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', update_token='f4a5b6c7-7d8e-4f9a-8b1c-1d2e3f4a5b6c', deployment_description='Production deployment for US East 1 region - updated', associated_policy_list=[{'policyIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789'}], associated_scope_list=[{'scopeIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123'}], deployment_configuration={'enableCrossAccountVisibility': True}, is_published=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.update_deployment_input.UpdateDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.update_deployment_output.UpdateDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_deployment

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.update_deployment.async_update_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_deployment_input.UpdateDeploymentInput = {
            "deployment_identifier": deployment_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if deployment_description is not None:
            input_["deployment_description"] = deployment_description
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if associated_policy_list is not None:
            input_["associated_policy_list"] = associated_policy_list
        if associated_scope_list is not None:
            input_["associated_scope_list"] = associated_scope_list
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
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a deployment
            Deletes a deployment by its ARN. Deleting an active deployment stops enforcement and triggers cleanup of managed firewall resources.

            >>> await client.delete(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_deployment

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput = {
            "deployment_identifier": deployment_identifier
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
    ) -> "capo_network_security_manager.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

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
            List deployments
            Lists the published deployments in the account, one page at a time.

            >>> await client.list(max_results=10, status='ACTIVE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_deployments_input.ListDeploymentsInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_deployments

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_deployments_input.ListDeploymentsInput = {}
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

    async def create_deployment_snapshot(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_deployment_snapshot_output.CreateDeploymentSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
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
            Create a deployment snapshot
            Creates an immutable snapshot of the current published version of a deployment. The snapshot is addressable by a version-qualified ARN.

            >>> await client.create_deployment_snapshot(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', client_token='550e8400-e29b-41d4-a716-446655440014')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.create_deployment_snapshot_input.CreateDeploymentSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.create_deployment_snapshot_output.CreateDeploymentSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment_snapshot

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment_snapshot.async_create_deployment_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_deployment_snapshot_input.CreateDeploymentSnapshotInput = {
            "deployment_identifier": deployment_identifier
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

    async def list_deployment_snapshots(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_deployment_snapshots_output.ListDeploymentSnapshotsOutput":
        """<p>Lists the snapshots of the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
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
            List the snapshots of a deployment
            Lists the immutable snapshots that have been created for a deployment.

            >>> await client.list_deployment_snapshots(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_deployment_snapshots_input.ListDeploymentSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_deployment_snapshots_output.ListDeploymentSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_deployment_snapshots

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_deployment_snapshots.async_list_deployment_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_deployment_snapshots_input.ListDeploymentSnapshotsInput = {
            "deployment_identifier": deployment_identifier
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

    async def list_resource_synchronization_statuses(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncNetworkSecurityManagerClientConfig] = None,
        synchronization_status: Optional[
            "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
        ] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_resource_synchronization_statuses_output.ListResourceSynchronizationStatusesOutput":
        """<p>Lists the synchronization statuses of the resources covered by the specified deployment. You can filter the results by synchronization status and page through them.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment to list synchronization statuses for. This is the deployment's Amazon Resource Name (ARN).</p>
            synchronization_status: <p>Filters the results by synchronization status, such as <code>IN_SYNC</code> or <code>OUT_OF_SYNC</code>.</p>
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
            List out-of-sync resources for a deployment
            Lists the resources tracked by a deployment that are out of sync, including the structured reason. Here a CloudFront distribution has no web ACL where the policy requires one.

            >>> await client.list_resource_synchronization_statuses(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', synchronization_status='OUT_OF_SYNC', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_network_security_manager.types.list_resource_synchronization_statuses_input.ListResourceSynchronizationStatusesInput]",
        ) -> AsyncOperationResponse[
            "capo_network_security_manager.types.list_resource_synchronization_statuses_output.ListResourceSynchronizationStatusesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_synchronization_statuses

            (
                output,
                http_response,
            ) = await capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_synchronization_statuses.async_list_resource_synchronization_statuses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_resource_synchronization_statuses_input.ListResourceSynchronizationStatusesInput = {
            "deployment_identifier": deployment_identifier
        }
        if synchronization_status is not None:
            input_["synchronization_status"] = synchronization_status
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
