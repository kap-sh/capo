from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_sso_admin._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.delete_application_access_scope_request
    import capo_sso_admin.types.get_application_access_scope_request
    import capo_sso_admin.types.get_application_access_scope_response
    import capo_sso_admin.types.list_application_access_scopes_request
    import capo_sso_admin.types.list_application_access_scopes_response
    import capo_sso_admin.types.max_results
    import capo_sso_admin.types.put_application_access_scope_request
    import capo_sso_admin.types.scope
    import capo_sso_admin.types.scope_details
    import capo_sso_admin.types.scope_targets
    import capo_sso_admin.types.token
    from capo_sso_admin._services.async_sso_admin import (
        AsyncSSOAdminClient,
        AsyncSSOAdminClientConfig,
    )
    from capo_sso_admin._services.sso_admin import SSOAdminClient, SSOAdminClientConfig


class ApplicationAccessScopeResource:
    def __init__(self, service: SSOAdminClient) -> None:
        self._service = service

    def put(
        self,
        scope: "capo_sso_admin.types.scope.Scope",
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        authorized_targets: Optional[
            "capo_sso_admin.types.scope_targets.ScopeTargets"
        ] = None,
    ) -> None:
        """<p>Adds or updates the list of authorized targets for an IAM Identity Center access scope for an application.</p>

        Args:
            scope: <p>Specifies the name of the access scope to be associated with the specified targets.</p>
            authorized_targets: <p>Specifies an array list of ARNs that represent the authorized targets for this access scope.</p>
            application_arn: <p>Specifies the ARN of the application with the access scope with the targets to add or update.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso_admin.types.put_application_access_scope_request.PutApplicationAccessScopeRequest]",
        ) -> OperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.put_application_access_scope

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.put_application_access_scope.put_application_access_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutApplicationAccessScope")
        )
        input_: capo_sso_admin.types.put_application_access_scope_request.PutApplicationAccessScopeRequest = {
            "scope": scope,
            "application_arn": application_arn,
        }
        if authorized_targets is not None:
            input_["authorized_targets"] = authorized_targets

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        scope: "capo_sso_admin.types.scope.Scope",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "capo_sso_admin.types.get_application_access_scope_response.GetApplicationAccessScopeResponse":
        """<p>Retrieves the authorized targets for an IAM Identity Center access scope for an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the access scope that you want to retrieve.</p>
            scope: <p>Specifies the name of the access scope for which you want the authorized targets.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso_admin.types.get_application_access_scope_request.GetApplicationAccessScopeRequest]",
        ) -> OperationResponse[
            "capo_sso_admin.types.get_application_access_scope_response.GetApplicationAccessScopeResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.get_application_access_scope

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.get_application_access_scope.get_application_access_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApplicationAccessScope")
        )
        input_: capo_sso_admin.types.get_application_access_scope_request.GetApplicationAccessScopeRequest = {
            "application_arn": application_arn,
            "scope": scope,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        scope: "capo_sso_admin.types.scope.Scope",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an IAM Identity Center access scope from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the access scope to delete.</p>
            scope: <p>Specifies the name of the access scope to remove from the application.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso_admin.types.delete_application_access_scope_request.DeleteApplicationAccessScopeRequest]",
        ) -> OperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.delete_application_access_scope

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.delete_application_access_scope.delete_application_access_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplicationAccessScope")
        )
        input_: capo_sso_admin.types.delete_application_access_scope_request.DeleteApplicationAccessScopeRequest = {
            "application_arn": application_arn,
            "scope": scope,
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
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
        max_results: Optional["capo_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_sso_admin.types.token.Token"] = None,
    ) -> "capo_sso_admin.types.list_application_access_scopes_response.ListApplicationAccessScopesResponse":
        """<p>Lists the access scopes and authorized targets associated with an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso_admin.types.list_application_access_scopes_request.ListApplicationAccessScopesRequest]",
        ) -> OperationResponse[
            "capo_sso_admin.types.list_application_access_scopes_response.ListApplicationAccessScopesResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.list_application_access_scopes

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.list_application_access_scopes.list_application_access_scopes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApplicationAccessScopes")
        )
        input_: capo_sso_admin.types.list_application_access_scopes_request.ListApplicationAccessScopesRequest = {
            "application_arn": application_arn
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


class AsyncApplicationAccessScopeResource:
    def __init__(self, service: AsyncSSOAdminClient) -> None:
        self._service = service

    async def put(
        self,
        scope: "capo_sso_admin.types.scope.Scope",
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
        authorized_targets: Optional[
            "capo_sso_admin.types.scope_targets.ScopeTargets"
        ] = None,
    ) -> None:
        """<p>Adds or updates the list of authorized targets for an IAM Identity Center access scope for an application.</p>

        Args:
            scope: <p>Specifies the name of the access scope to be associated with the specified targets.</p>
            authorized_targets: <p>Specifies an array list of ARNs that represent the authorized targets for this access scope.</p>
            application_arn: <p>Specifies the ARN of the application with the access scope with the targets to add or update.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_admin.types.put_application_access_scope_request.PutApplicationAccessScopeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.put_application_access_scope

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.put_application_access_scope.async_put_application_access_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutApplicationAccessScope")
        )
        input_: capo_sso_admin.types.put_application_access_scope_request.PutApplicationAccessScopeRequest = {
            "scope": scope,
            "application_arn": application_arn,
        }
        if authorized_targets is not None:
            input_["authorized_targets"] = authorized_targets

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        scope: "capo_sso_admin.types.scope.Scope",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> "capo_sso_admin.types.get_application_access_scope_response.GetApplicationAccessScopeResponse":
        """<p>Retrieves the authorized targets for an IAM Identity Center access scope for an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the access scope that you want to retrieve.</p>
            scope: <p>Specifies the name of the access scope for which you want the authorized targets.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_admin.types.get_application_access_scope_request.GetApplicationAccessScopeRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_admin.types.get_application_access_scope_response.GetApplicationAccessScopeResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.get_application_access_scope

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.get_application_access_scope.async_get_application_access_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApplicationAccessScope")
        )
        input_: capo_sso_admin.types.get_application_access_scope_request.GetApplicationAccessScopeRequest = {
            "application_arn": application_arn,
            "scope": scope,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        scope: "capo_sso_admin.types.scope.Scope",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an IAM Identity Center access scope from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the access scope to delete.</p>
            scope: <p>Specifies the name of the access scope to remove from the application.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_admin.types.delete_application_access_scope_request.DeleteApplicationAccessScopeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.delete_application_access_scope

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.delete_application_access_scope.async_delete_application_access_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplicationAccessScope")
        )
        input_: capo_sso_admin.types.delete_application_access_scope_request.DeleteApplicationAccessScopeRequest = {
            "application_arn": application_arn,
            "scope": scope,
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
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
        max_results: Optional["capo_sso_admin.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_sso_admin.types.token.Token"] = None,
    ) -> "capo_sso_admin.types.list_application_access_scopes_response.ListApplicationAccessScopesResponse":
        """<p>Lists the access scopes and authorized targets associated with an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            max_results: <p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_admin.types.list_application_access_scopes_request.ListApplicationAccessScopesRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_admin.types.list_application_access_scopes_response.ListApplicationAccessScopesResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.list_application_access_scopes

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.list_application_access_scopes.async_list_application_access_scopes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApplicationAccessScopes")
        )
        input_: capo_sso_admin.types.list_application_access_scopes_request.ListApplicationAccessScopesRequest = {
            "application_arn": application_arn
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
