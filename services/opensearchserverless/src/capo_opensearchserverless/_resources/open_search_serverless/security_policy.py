from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.delete_security_policy_request
    import capo_opensearchserverless.types.delete_security_policy_response
    import capo_opensearchserverless.types.get_security_policy_request
    import capo_opensearchserverless.types.get_security_policy_response
    import capo_opensearchserverless.types.list_security_policies_request
    import capo_opensearchserverless.types.list_security_policies_response
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_document
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.policy_version
    import capo_opensearchserverless.types.resource_filter
    import capo_opensearchserverless.types.security_policy_type
    import capo_opensearchserverless.types.update_security_policy_request
    import capo_opensearchserverless.types.update_security_policy_response
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class SecurityPolicy:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def read(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse":
        """<p>Returns information about a configured OpenSearch Serverless security policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the security policy.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_security_policy.get_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest = {
            "type": type,
            "name": name,
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
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "capo_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse":
        """<p>Updates an OpenSearch Serverless security policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of access policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_security_policy.update_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest = {
            "type": type,
            "name": name,
            "policy_version": policy_version,
        }
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
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
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse":
        """<p>Deletes an OpenSearch Serverless security policy.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_security_policy

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_security_policy.delete_security_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest = {
            "type": type,
            "name": name,
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
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "capo_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Returns information about configured OpenSearch Serverless security policies.</p>

        Args:
            type: <p>The type of policy.</p>
            resource: <p>Resource filters (can be collection or indexes) that policies can apply to. </p>
            next_token: <p>If your initial <code>ListSecurityPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_security_policies

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_security_policies.list_security_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest = {
            "type": type
        }
        if resource is not None:
            input_["resource"] = resource
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSecurityPolicy:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def read(
        self,
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse":
        """<p>Returns information about a configured OpenSearch Serverless security policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of security policy.</p>
            name: <p>The name of the security policy.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_security_policy_response.GetSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_security_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_security_policy.async_get_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_security_policy_request.GetSecurityPolicyRequest = {
            "type": type,
            "name": name,
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
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        policy_version: "capo_opensearchserverless.types.policy_version.PolicyVersion",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[
            "capo_opensearchserverless.types.policy_description.PolicyDescription"
        ] = None,
        policy: Optional[
            "capo_opensearchserverless.types.policy_document.PolicyDocument"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse":
        """<p>Updates an OpenSearch Serverless security policy. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html">Network access for Amazon OpenSearch Serverless</a> and <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html">Encryption at rest for Amazon OpenSearch Serverless</a>.</p>

        Args:
            type: <p>The type of access policy.</p>
            name: <p>The name of the policy.</p>
            policy_version: <p>The version of the policy being updated.</p>
            description: <p>A description of the policy. Typically used to store information about the permissions defined in the policy.</p>
            policy: <p>The JSON policy document to use as the content for the new policy.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_security_policy_response.UpdateSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_security_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_security_policy.async_update_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_security_policy_request.UpdateSecurityPolicyRequest = {
            "type": type,
            "name": name,
            "policy_version": policy_version,
        }
        if description is not None:
            input_["description"] = description
        if policy is not None:
            input_["policy"] = policy
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
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        name: "capo_opensearchserverless.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse":
        """<p>Deletes an OpenSearch Serverless security policy.</p>

        Args:
            type: <p>The type of policy.</p>
            name: <p>The name of the policy to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_security_policy_response.DeleteSecurityPolicyResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_security_policy

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_security_policy.async_delete_security_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_security_policy_request.DeleteSecurityPolicyRequest = {
            "type": type,
            "name": name,
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
        type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        resource: Optional[
            "capo_opensearchserverless.types.resource_filter.ResourceFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse":
        """<p>Returns information about configured OpenSearch Serverless security policies.</p>

        Args:
            type: <p>The type of policy.</p>
            resource: <p>Resource filters (can be collection or indexes) that policies can apply to. </p>
            next_token: <p>If your initial <code>ListSecurityPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityPolicies</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_security_policies_response.ListSecurityPoliciesResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_security_policies

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_security_policies.async_list_security_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_security_policies_request.ListSecurityPoliciesRequest = {
            "type": type
        }
        if resource is not None:
            input_["resource"] = resource
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
