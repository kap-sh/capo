"""Generated from Smithy shape ``com.amazonaws.signin#Signin``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_signin._auth._signers
import capo_signin._auth._sigv4
from capo_signin._auth._identity import Credentials
from capo_signin._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_signin._auth._zapros_handler import AuthMiddleware
from capo_signin._pagination import resolve_path as _resolve_path
from capo_signin._services._aws_config import aaws_config
from capo_signin._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    aretry,
)

if TYPE_CHECKING:
    import capo_signin.types.client_credentials_grant_type
    import capo_signin.types.client_token
    import capo_signin.types.console_permission_max_results
    import capo_signin.types.create_o_auth2_token_request
    import capo_signin.types.create_o_auth2_token_request_body
    import capo_signin.types.create_o_auth2_token_response
    import capo_signin.types.create_o_auth2_token_with_iam_request
    import capo_signin.types.create_o_auth2_token_with_iam_response
    import capo_signin.types.create_o_auth2_token_with_token_exchange_request
    import capo_signin.types.create_o_auth2_token_with_token_exchange_response
    import capo_signin.types.delete_console_authorization_configuration_input
    import capo_signin.types.delete_console_authorization_configuration_output
    import capo_signin.types.delete_resource_permission_statement_input
    import capo_signin.types.delete_resource_permission_statement_output
    import capo_signin.types.excluded_principal
    import capo_signin.types.get_console_authorization_configuration_input
    import capo_signin.types.get_console_authorization_configuration_output
    import capo_signin.types.get_resource_policy_input
    import capo_signin.types.get_resource_policy_output
    import capo_signin.types.introspect_o_auth2_token_with_iam_request
    import capo_signin.types.introspect_o_auth2_token_with_iam_response
    import capo_signin.types.introspection_token
    import capo_signin.types.list_resource_permission_statements_input
    import capo_signin.types.list_resource_permission_statements_output
    import capo_signin.types.next_token
    import capo_signin.types.permission_statement_summary
    import capo_signin.types.put_console_authorization_configuration_input
    import capo_signin.types.put_console_authorization_configuration_output
    import capo_signin.types.put_resource_permission_statement_input
    import capo_signin.types.put_resource_permission_statement_output
    import capo_signin.types.requested_region
    import capo_signin.types.resource
    import capo_signin.types.revocation_token
    import capo_signin.types.revoke_o_auth2_token_with_iam_request
    import capo_signin.types.revoke_o_auth2_token_with_iam_response
    import capo_signin.types.scope
    import capo_signin.types.source_ip
    import capo_signin.types.source_vpc
    import capo_signin.types.source_vpce
    import capo_signin.types.statement_id
    import capo_signin.types.subject_token
    import capo_signin.types.subject_token_type
    import capo_signin.types.target_id
    import capo_signin.types.token_exchange_grant_type
    import capo_signin.types.token_type_hint
    import capo_signin.types.vpc_source_ip


class AsyncSigninClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSigninClient:
    """A client for the ``Signin`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(raw_handler)
            )
        self._config = AsyncSigninClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSigninClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_o_auth2_token(
        self,
        token_input: "capo_signin.types.create_o_auth2_token_request_body.CreateOAuth2TokenRequestBody",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
    ) -> "capo_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse":
        """Exchanges an authorization code or refresh token for an OAuth 2.0 access token and refresh token.

        Args:
            token_input: Flattened token operation inputs. The "grant_type" in the request body determines the specific operation.

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse"
        ]:
            import capo_signin._operations.signin.create_o_auth2_token

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.create_o_auth2_token.async_create_o_auth2_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest",
        ) -> dict[str, Any]:
            import capo_signin.types.create_o_auth2_token_request

            return capo_signin.types.create_o_auth2_token_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse",
        ) -> dict[str, Any]:
            import capo_signin.types.create_o_auth2_token_response

            return capo_signin.types.create_o_auth2_token_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "CreateOAuth2Token",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest = {
            "token_input": token_input
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_o_auth2_token_with_iam(
        self,
        grant_type: "capo_signin.types.client_credentials_grant_type.ClientCredentialsGrantType",
        resource: "capo_signin.types.resource.Resource",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
    ) -> "capo_signin.types.create_o_auth2_token_with_iam_response.CreateOAuth2TokenWithIAMResponse":
        """Exchanges client credentials for an OAuth 2.0 access token scoped to a resource, which you can use to access AWS services from applications.

        Args:
            grant_type: The OAuth 2.0 grant type. Must be "client_credentials".
            resource: The OAuth resource for which the access token is requested. Example: "aws-mcp.amazonaws.com".

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.create_o_auth2_token_with_iam_request.CreateOAuth2TokenWithIAMRequest]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.create_o_auth2_token_with_iam_response.CreateOAuth2TokenWithIAMResponse"
        ]:
            import capo_signin._operations.signin.create_o_auth2_token_with_iam

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.create_o_auth2_token_with_iam.async_create_o_auth2_token_with_iam(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_signin.types.create_o_auth2_token_with_iam_response.CreateOAuth2TokenWithIAMResponse",
        ) -> dict[str, Any]:
            import capo_signin.types.create_o_auth2_token_with_iam_response

            return capo_signin.types.create_o_auth2_token_with_iam_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateOAuth2TokenWithIAM", redact_output=_redact_output),
        )
        input_: capo_signin.types.create_o_auth2_token_with_iam_request.CreateOAuth2TokenWithIAMRequest = {
            "grant_type": grant_type,
            "resource": resource,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_o_auth2_token_with_token_exchange(
        self,
        grant_type: "capo_signin.types.token_exchange_grant_type.TokenExchangeGrantType",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        subject_token: Optional["capo_signin.types.subject_token.SubjectToken"] = None,
        subject_token_type: Optional[
            "capo_signin.types.subject_token_type.SubjectTokenType"
        ] = None,
        resource: Optional["capo_signin.types.resource.Resource"] = None,
        scope: Optional["capo_signin.types.scope.Scope"] = None,
    ) -> "capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse":
        """Exchanges a supported token for an OAuth 2.0 access token scoped to a resource, which you can use to access AWS services from applications.

        Args:
            grant_type: The OAuth 2.0 grant type. Currently only supports "urn:ietf:params:oauth:grant-type:token-exchange".
            subject_token: The subject token that represents the identity of the party on whose behalf the request is made. Required when "grant_type=urn:ietf:params:oauth:grant-type:token-exchange".
            subject_token_type: The token type of the subject token. Currently only supports "urn:ietf:params:oauth:token-type:jwt". Required when "grant_type=urn:ietf:params:oauth:grant-type:token-exchange".
            resource: The OAuth resource for which the access token is requested. Required when "grant_type=urn:ietf:params:oauth:grant-type:token-exchange". Example: "glue.amazonaws.com".
            scope: IAM managed policy Amazon Resource Names (ARNs) to apply as session policies that further scope down the permissions of the issued access token, provided as a space-delimited list. Example: "arn:aws:iam::444455556666:policy/MyPolicy".

        Raises:
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.invalid_grant_exception.InvalidGrantException: The request failed because the provided grant is invalid or expired.
            capo_signin.errors.invalid_scope_exception.InvalidScopeException: The request failed because the requested scope is invalid or exceeds the scope that can be granted.
            capo_signin.errors.service_unavailable_exception.ServiceUnavailableException: The request failed because a dependency is temporarily unavailable. You can retry the request.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.create_o_auth2_token_with_token_exchange_request.CreateOAuth2TokenWithTokenExchangeRequest]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse"
        ]:
            import capo_signin._operations.signin.create_o_auth2_token_with_token_exchange

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.create_o_auth2_token_with_token_exchange.async_create_o_auth2_token_with_token_exchange(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_signin.types.create_o_auth2_token_with_token_exchange_request.CreateOAuth2TokenWithTokenExchangeRequest",
        ) -> dict[str, Any]:
            import capo_signin.types.create_o_auth2_token_with_token_exchange_request

            return capo_signin.types.create_o_auth2_token_with_token_exchange_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_signin.types.create_o_auth2_token_with_token_exchange_response.CreateOAuth2TokenWithTokenExchangeResponse",
        ) -> dict[str, Any]:
            import capo_signin.types.create_o_auth2_token_with_token_exchange_response

            return capo_signin.types.create_o_auth2_token_with_token_exchange_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "CreateOAuth2TokenWithTokenExchange",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_signin.types.create_o_auth2_token_with_token_exchange_request.CreateOAuth2TokenWithTokenExchangeRequest = {
            "grant_type": grant_type
        }
        if subject_token is not None:
            input_["subject_token"] = subject_token
        if subject_token_type is not None:
            input_["subject_token_type"] = subject_token_type
        if resource is not None:
            input_["resource"] = resource
        if scope is not None:
            input_["scope"] = scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        target_id: Optional["capo_signin.types.target_id.TargetId"] = None,
    ) -> "capo_signin.types.delete_console_authorization_configuration_output.DeleteConsoleAuthorizationConfigurationOutput":
        """Delete console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.delete_console_authorization_configuration_input.DeleteConsoleAuthorizationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.delete_console_authorization_configuration_output.DeleteConsoleAuthorizationConfigurationOutput"
        ]:
            import capo_signin._operations.signin.delete_console_authorization_configuration

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.delete_console_authorization_configuration.async_delete_console_authorization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("DeleteConsoleAuthorizationConfiguration"),
        )
        input_: capo_signin.types.delete_console_authorization_configuration_input.DeleteConsoleAuthorizationConfigurationInput = {}
        if target_id is not None:
            input_["target_id"] = target_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_permission_statement(
        self,
        statement_id: "capo_signin.types.statement_id.StatementId",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        client_token: Optional["capo_signin.types.client_token.ClientToken"] = None,
    ) -> "capo_signin.types.delete_resource_permission_statement_output.DeleteResourcePermissionStatementOutput":
        """Remove a permission statement from the account's SignIn resource-based policy

        Args:
            statement_id: Unique identifier of the permission statement to delete
            client_token: Idempotency token for the request

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.delete_resource_permission_statement_input.DeleteResourcePermissionStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.delete_resource_permission_statement_output.DeleteResourcePermissionStatementOutput"
        ]:
            import capo_signin._operations.signin.delete_resource_permission_statement

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.delete_resource_permission_statement.async_delete_resource_permission_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteResourcePermissionStatement")
        )
        input_: capo_signin.types.delete_resource_permission_statement_input.DeleteResourcePermissionStatementInput = {
            "statement_id": statement_id
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

    async def get_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        target_id: Optional["capo_signin.types.target_id.TargetId"] = None,
    ) -> "capo_signin.types.get_console_authorization_configuration_output.GetConsoleAuthorizationConfigurationOutput":
        """Get console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.get_console_authorization_configuration_input.GetConsoleAuthorizationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.get_console_authorization_configuration_output.GetConsoleAuthorizationConfigurationOutput"
        ]:
            import capo_signin._operations.signin.get_console_authorization_configuration

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.get_console_authorization_configuration.async_get_console_authorization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetConsoleAuthorizationConfiguration")
        )
        input_: capo_signin.types.get_console_authorization_configuration_input.GetConsoleAuthorizationConfigurationInput = {}
        if target_id is not None:
            input_["target_id"] = target_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self, *, config_overrides: Optional[AsyncSigninClientConfig] = None
    ) -> "capo_signin.types.get_resource_policy_output.GetResourcePolicyOutput":
        """Retrieve the account's consolidated SignIn resource-based policy

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_signin._operations.signin.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetResourcePolicy")
        )
        input_: capo_signin.types.get_resource_policy_input.GetResourcePolicyInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def introspect_o_auth2_token_with_iam(
        self,
        token: "capo_signin.types.introspection_token.IntrospectionToken",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        token_type_hint: Optional[
            "capo_signin.types.token_type_hint.TokenTypeHint"
        ] = None,
    ) -> "capo_signin.types.introspect_o_auth2_token_with_iam_response.IntrospectOAuth2TokenWithIAMResponse":
        """Inspects the metadata and active state of an OAuth 2.0 access token or refresh token. Implements RFC 7662 OAuth 2.0 Token Introspection over a SigV4-authenticated endpoint. Returns the claims associated with a token issued by AWS Sign-In.

        Args:
            token: The access token or refresh token issued by AWS Sign-In.
            token_type_hint: An optional hint about the type of the token submitted for introspection, as defined in RFC 7662 §2.1. The server checks both token types regardless of the hint. Allowed values: "access_token", "refresh_token".

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.introspect_o_auth2_token_with_iam_request.IntrospectOAuth2TokenWithIAMRequest]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.introspect_o_auth2_token_with_iam_response.IntrospectOAuth2TokenWithIAMResponse"
        ]:
            import capo_signin._operations.signin.introspect_o_auth2_token_with_iam

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.introspect_o_auth2_token_with_iam.async_introspect_o_auth2_token_with_iam(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_signin.types.introspect_o_auth2_token_with_iam_request.IntrospectOAuth2TokenWithIAMRequest",
        ) -> dict[str, Any]:
            import capo_signin.types.introspect_o_auth2_token_with_iam_request

            return capo_signin.types.introspect_o_auth2_token_with_iam_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "IntrospectOAuth2TokenWithIAM", redact_input=_redact_input
            ),
        )
        input_: capo_signin.types.introspect_o_auth2_token_with_iam_request.IntrospectOAuth2TokenWithIAMRequest = {
            "token": token
        }
        if token_type_hint is not None:
            input_["token_type_hint"] = token_type_hint

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_resource_permission_statements(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        max_results: Optional[
            "capo_signin.types.console_permission_max_results.ConsolePermissionMaxResults"
        ] = None,
        next_token: Optional["capo_signin.types.next_token.NextToken"] = None,
    ) -> "capo_signin.types.list_resource_permission_statements_output.ListResourcePermissionStatementsOutput":
        """Retrieve all permission statements in the account's SignIn resource-based policy

        Args:
            max_results: Maximum number of results to return
            next_token: Token for pagination

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.list_resource_permission_statements_input.ListResourcePermissionStatementsInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.list_resource_permission_statements_output.ListResourcePermissionStatementsOutput"
        ]:
            import capo_signin._operations.signin.list_resource_permission_statements

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.list_resource_permission_statements.async_list_resource_permission_statements(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListResourcePermissionStatements")
        )
        input_: capo_signin.types.list_resource_permission_statements_input.ListResourcePermissionStatementsInput = {}
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

    async def iter_list_resource_permission_statements(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        max_results: Optional[
            "capo_signin.types.console_permission_max_results.ConsolePermissionMaxResults"
        ] = None,
        next_token: Optional["capo_signin.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_signin.types.permission_statement_summary.PermissionStatementSummary]":
        _token = next_token
        while True:
            _response = await self.list_resource_permission_statements(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("permission_statements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        target_id: Optional["capo_signin.types.target_id.TargetId"] = None,
    ) -> "capo_signin.types.put_console_authorization_configuration_output.PutConsoleAuthorizationConfigurationOutput":
        """Enable console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.conflict_exception.ConflictException: Error thrown when request conflicts with current state HTTP Status Code: 409 Conflict Used when the request conflicts with the current state of the resource
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.put_console_authorization_configuration_input.PutConsoleAuthorizationConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.put_console_authorization_configuration_output.PutConsoleAuthorizationConfigurationOutput"
        ]:
            import capo_signin._operations.signin.put_console_authorization_configuration

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.put_console_authorization_configuration.async_put_console_authorization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("PutConsoleAuthorizationConfiguration")
        )
        input_: capo_signin.types.put_console_authorization_configuration_input.PutConsoleAuthorizationConfigurationInput = {}
        if target_id is not None:
            input_["target_id"] = target_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_permission_statement(
        self,
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
        source_vpc: Optional["capo_signin.types.source_vpc.SourceVpc"] = None,
        signin_source_vpce: Optional["capo_signin.types.source_vpce.SourceVpce"] = None,
        console_source_vpce: Optional[
            "capo_signin.types.source_vpce.SourceVpce"
        ] = None,
        vpc_source_ip: Optional["capo_signin.types.vpc_source_ip.VpcSourceIp"] = None,
        source_ip: Optional["capo_signin.types.source_ip.SourceIp"] = None,
        requested_region: Optional[
            "capo_signin.types.requested_region.RequestedRegion"
        ] = None,
        excluded_principal: Optional[
            "capo_signin.types.excluded_principal.ExcludedPrincipal"
        ] = None,
        client_token: Optional["capo_signin.types.client_token.ClientToken"] = None,
    ) -> "capo_signin.types.put_resource_permission_statement_output.PutResourcePermissionStatementOutput":
        """Create a permission statement in the account's SignIn resource-based policy

        Args:
            source_vpc: VPC identifier to restrict console access
            signin_source_vpce: SignIn VPC endpoint identifier
            console_source_vpce: Console VPC endpoint identifier
            vpc_source_ip: Source IP address within VPC
            source_ip: Source IP address
            requested_region: AWS region where the VPC and VPC endpoint reside Required when sourceVpc or signinSourceVpce/consoleSourceVpce is provided
            excluded_principal: Principal to exclude from the permission statement
            client_token: Idempotency token for the request

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.conflict_exception.ConflictException: Error thrown when request conflicts with current state HTTP Status Code: 409 Conflict Used when the request conflicts with the current state of the resource
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: Error thrown when service quota is exceeded HTTP Status Code: 402 Payment Required (used as quota exceeded indicator) Used when the request would cause a service quota to be exceeded
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.put_resource_permission_statement_input.PutResourcePermissionStatementInput]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.put_resource_permission_statement_output.PutResourcePermissionStatementOutput"
        ]:
            import capo_signin._operations.signin.put_resource_permission_statement

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.put_resource_permission_statement.async_put_resource_permission_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("PutResourcePermissionStatement")
        )
        input_: capo_signin.types.put_resource_permission_statement_input.PutResourcePermissionStatementInput = {}
        if source_vpc is not None:
            input_["source_vpc"] = source_vpc
        if signin_source_vpce is not None:
            input_["signin_source_vpce"] = signin_source_vpce
        if console_source_vpce is not None:
            input_["console_source_vpce"] = console_source_vpce
        if vpc_source_ip is not None:
            input_["vpc_source_ip"] = vpc_source_ip
        if source_ip is not None:
            input_["source_ip"] = source_ip
        if requested_region is not None:
            input_["requested_region"] = requested_region
        if excluded_principal is not None:
            input_["excluded_principal"] = excluded_principal
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

    async def revoke_o_auth2_token_with_iam(
        self,
        token: "capo_signin.types.revocation_token.RevocationToken",
        *,
        config_overrides: Optional[AsyncSigninClientConfig] = None,
    ) -> "capo_signin.types.revoke_o_auth2_token_with_iam_response.RevokeOAuth2TokenWithIAMResponse":
        """Revokes an OAuth 2.0 refresh token and its associated token chain.

        Args:
            token: The refresh token to revoke. Must be a refresh token issued by AWS Sign-In. Access tokens are not accepted for revocation.

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action.
            capo_signin.errors.internal_server_exception.InternalServerException: The request failed because of an internal server error.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: The request failed because you exceeded the request rate limit for this operation.
            capo_signin.errors.validation_exception.ValidationException: The request failed because it contains a malformed, missing, or invalid parameter.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_signin.types.revoke_o_auth2_token_with_iam_request.RevokeOAuth2TokenWithIAMRequest]",
        ) -> AsyncOperationResponse[
            "capo_signin.types.revoke_o_auth2_token_with_iam_response.RevokeOAuth2TokenWithIAMResponse"
        ]:
            import capo_signin._operations.signin.revoke_o_auth2_token_with_iam

            (
                output,
                http_response,
            ) = await capo_signin._operations.signin.revoke_o_auth2_token_with_iam.async_revoke_o_auth2_token_with_iam(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_signin.types.revoke_o_auth2_token_with_iam_request.RevokeOAuth2TokenWithIAMRequest",
        ) -> dict[str, Any]:
            import capo_signin.types.revoke_o_auth2_token_with_iam_request

            return capo_signin.types.revoke_o_auth2_token_with_iam_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("RevokeOAuth2TokenWithIAM", redact_input=_redact_input),
        )
        input_: capo_signin.types.revoke_o_auth2_token_with_iam_request.RevokeOAuth2TokenWithIAMRequest = {
            "token": token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
