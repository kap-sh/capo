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
    import capo_sso_admin.types.authentication_method
    import capo_sso_admin.types.authentication_method_item
    import capo_sso_admin.types.authentication_method_type
    import capo_sso_admin.types.delete_application_authentication_method_request
    import capo_sso_admin.types.get_application_authentication_method_request
    import capo_sso_admin.types.get_application_authentication_method_response
    import capo_sso_admin.types.list_application_authentication_methods_request
    import capo_sso_admin.types.list_application_authentication_methods_response
    import capo_sso_admin.types.put_application_authentication_method_request
    import capo_sso_admin.types.token
    from capo_sso_admin._services.async_sso_admin import (
        AsyncSSOAdminClient,
        AsyncSSOAdminClientConfig,
    )
    from capo_sso_admin._services.sso_admin import SSOAdminClient, SSOAdminClientConfig


class ApplicationAuthenticationMethodResource:
    def __init__(self, service: SSOAdminClient) -> None:
        self._service = service

    def put(
        self,
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        authentication_method: "capo_sso_admin.types.authentication_method.AuthenticationMethod",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Adds or updates an authentication method for an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to add or update.</p>
            authentication_method_type: <p>Specifies the type of the authentication method that you want to add or update.</p>
            authentication_method: <p>Specifies a structure that describes the authentication method to add or update. The structure type you provide is determined by the <code>AuthenticationMethodType</code> parameter.</p>

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
            req: "OperationRequest[capo_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest]",
        ) -> OperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.put_application_authentication_method

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.put_application_authentication_method.put_application_authentication_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutApplicationAuthenticationMethod")
        )
        input_: capo_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest = {
            "application_arn": application_arn,
            "authentication_method_type": authentication_method_type,
            "authentication_method": authentication_method,
        }

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
        authentication_method_type: "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> "capo_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse":
        """<p>Retrieves details about an authentication method used by an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            authentication_method_type: <p>Specifies the type of authentication method for which you want details.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest]",
        ) -> OperationResponse[
            "capo_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.get_application_authentication_method

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.get_application_authentication_method.get_application_authentication_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApplicationAuthenticationMethod")
        )
        input_: capo_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest = {
            "application_arn": application_arn,
            "authentication_method_type": authentication_method_type,
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
        authentication_method_type: "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[SSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an authentication method from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to delete.</p>
            authentication_method_type: <p>Specifies the authentication method type to delete from the application.</p>

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
            req: "OperationRequest[capo_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest]",
        ) -> OperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.delete_application_authentication_method

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.delete_application_authentication_method.delete_application_authentication_method(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplicationAuthenticationMethod")
        )
        input_: capo_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest = {
            "application_arn": application_arn,
            "authentication_method_type": authentication_method_type,
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
        next_token: Optional["capo_sso_admin.types.token.Token"] = None,
    ) -> "capo_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse":
        """<p>Lists all of the authentication methods supported by the specified application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication methods you want to list.</p>
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
            req: "OperationRequest[capo_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest]",
        ) -> OperationResponse[
            "capo_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.list_application_authentication_methods

            output, http_response = (
                capo_sso_admin._operations.swb_external_service.list_application_authentication_methods.list_application_authentication_methods(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApplicationAuthenticationMethods")
        )
        input_: capo_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest = {
            "application_arn": application_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApplicationAuthenticationMethodResource:
    def __init__(self, service: AsyncSSOAdminClient) -> None:
        self._service = service

    async def put(
        self,
        application_arn: "capo_sso_admin.types.application_arn.ApplicationArn",
        authentication_method_type: "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        authentication_method: "capo_sso_admin.types.authentication_method.AuthenticationMethod",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Adds or updates an authentication method for an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to add or update.</p>
            authentication_method_type: <p>Specifies the type of the authentication method that you want to add or update.</p>
            authentication_method: <p>Specifies a structure that describes the authentication method to add or update. The structure type you provide is determined by the <code>AuthenticationMethodType</code> parameter.</p>

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
            req: "AsyncOperationRequest[capo_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.put_application_authentication_method

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.put_application_authentication_method.async_put_application_authentication_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutApplicationAuthenticationMethod")
        )
        input_: capo_sso_admin.types.put_application_authentication_method_request.PutApplicationAuthenticationMethodRequest = {
            "application_arn": application_arn,
            "authentication_method_type": authentication_method_type,
            "authentication_method": authentication_method,
        }

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
        authentication_method_type: "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> "capo_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse":
        """<p>Retrieves details about an authentication method used by an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application.</p>
            authentication_method_type: <p>Specifies the type of authentication method for which you want details.</p>

        Raises:
            capo_sso_admin.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_admin.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure with an internal server.</p>
            capo_sso_admin.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_sso_admin.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_sso_admin.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_sso_admin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_admin.types.get_application_authentication_method_response.GetApplicationAuthenticationMethodResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.get_application_authentication_method

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.get_application_authentication_method.async_get_application_authentication_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApplicationAuthenticationMethod")
        )
        input_: capo_sso_admin.types.get_application_authentication_method_request.GetApplicationAuthenticationMethodRequest = {
            "application_arn": application_arn,
            "authentication_method_type": authentication_method_type,
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
        authentication_method_type: "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
        *,
        config_overrides: Optional[AsyncSSOAdminClientConfig] = None,
    ) -> None:
        """<p>Deletes an authentication method from an application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication method to delete.</p>
            authentication_method_type: <p>Specifies the authentication method type to delete from the application.</p>

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
            req: "AsyncOperationRequest[capo_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_sso_admin._operations.swb_external_service.delete_application_authentication_method

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.delete_application_authentication_method.async_delete_application_authentication_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplicationAuthenticationMethod")
        )
        input_: capo_sso_admin.types.delete_application_authentication_method_request.DeleteApplicationAuthenticationMethodRequest = {
            "application_arn": application_arn,
            "authentication_method_type": authentication_method_type,
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
        next_token: Optional["capo_sso_admin.types.token.Token"] = None,
    ) -> "capo_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse":
        """<p>Lists all of the authentication methods supported by the specified application.</p>

        Args:
            application_arn: <p>Specifies the ARN of the application with the authentication methods you want to list.</p>
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
            req: "AsyncOperationRequest[capo_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_admin.types.list_application_authentication_methods_response.ListApplicationAuthenticationMethodsResponse"
        ]:
            import capo_sso_admin._operations.swb_external_service.list_application_authentication_methods

            (
                output,
                http_response,
            ) = await capo_sso_admin._operations.swb_external_service.list_application_authentication_methods.async_list_application_authentication_methods(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApplicationAuthenticationMethods")
        )
        input_: capo_sso_admin.types.list_application_authentication_methods_request.ListApplicationAuthenticationMethodsRequest = {
            "application_arn": application_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
