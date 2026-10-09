"""Generated from Smithy shape ``com.amazonaws.signin#Signin``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

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
from capo_signin._services._aws_config import aws_config
from capo_signin._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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
    import capo_signin.types.revocation_token
    import capo_signin.types.revoke_o_auth2_token_with_iam_request
    import capo_signin.types.revoke_o_auth2_token_with_iam_response
    import capo_signin.types.source_ip
    import capo_signin.types.source_vpc
    import capo_signin.types.source_vpce
    import capo_signin.types.statement_id
    import capo_signin.types.target_id
    import capo_signin.types.token_type_hint
    import capo_signin.types.vpc_source_ip


class SigninClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SigninClient:
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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
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
                Client(http_handler)
            )
        self._config = SigninClientConfig(
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
        self, config_overrides: Optional[SigninClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SigninClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
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

    def create_o_auth2_token(
        self,
        token_input: "capo_signin.types.create_o_auth2_token_request_body.CreateOAuth2TokenRequestBody",
        *,
        config_overrides: Optional[SigninClientConfig] = None,
    ) -> "capo_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse":
        """CreateOAuth2Token API Path: /v1/token Request Method: POST Content-Type: application/json or application/x-www-form-urlencoded This API implements OAuth 2.0 flows for AWS Sign-In CLI clients, supporting both: 1. Authorization code redemption (grant_type=authorization_code) - NOT idempotent 2. Token refresh (grant_type=refresh_token) - Idempotent within token validity window The operation behavior is determined by the grant_type parameter in the request body: **Authorization Code Flow (NOT Idempotent):** - JSON or form-encoded body with client_id, grant_type=authorization_code, code, redirect_uri, code_verifier - Returns access_token, token_type, expires_in, refresh_token, and id_token - Each authorization code can only be used ONCE for security (prevents replay attacks) **Token Refresh Flow (Idempotent):** - JSON or form-encoded body with client_id, grant_type=refresh_token, refresh_token - Returns access_token, token_type, expires_in, and refresh_token (no id_token) - Multiple calls with same refresh_token return consistent results within validity window Authentication and authorization: - Confidential clients: sigv4 signing required with signin:ExchangeToken permissions - CLI clients (public): authn/authz skipped based on client_id & grant_type Note: This operation cannot be marked as @idempotent because it handles both idempotent (token refresh) and non-idempotent (auth code redemption) flows in a single endpoint.

        Args:
            token_input: Flattened token operation inputs The specific operation is determined by grant_type in the request body

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest]",
        ) -> OperationResponse[
            "capo_signin.types.create_o_auth2_token_response.CreateOAuth2TokenResponse"
        ]:
            import capo_signin._operations.signin.create_o_auth2_token

            output, http_response = (
                capo_signin._operations.signin.create_o_auth2_token.create_o_auth2_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.create_o_auth2_token_request.CreateOAuth2TokenRequest = {
            "token_input": token_input
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_o_auth2_token_with_iam(
        self,
        grant_type: "capo_signin.types.client_credentials_grant_type.ClientCredentialsGrantType",
        resource: str,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
    ) -> "capo_signin.types.create_o_auth2_token_with_iam_response.CreateOAuth2TokenWithIAMResponse":
        """Grants permission to exchange client credentials for an OAuth 2.0 access token scoped to a resource that can be used to access AWS services from applications

        Args:
            grant_type: OAuth 2.0 grant type. Must be "client_credentials".
            resource: The OAuth resource for which the access token is requested. Example: "aws-mcp.amazonaws.com".

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.create_o_auth2_token_with_iam_request.CreateOAuth2TokenWithIAMRequest]",
        ) -> OperationResponse[
            "capo_signin.types.create_o_auth2_token_with_iam_response.CreateOAuth2TokenWithIAMResponse"
        ]:
            import capo_signin._operations.signin.create_o_auth2_token_with_iam

            output, http_response = (
                capo_signin._operations.signin.create_o_auth2_token_with_iam.create_o_auth2_token_with_iam(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.create_o_auth2_token_with_iam_request.CreateOAuth2TokenWithIAMRequest = {
            "grant_type": grant_type,
            "resource": resource,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
        target_id: Optional["capo_signin.types.target_id.TargetId"] = None,
    ) -> "capo_signin.types.delete_console_authorization_configuration_output.DeleteConsoleAuthorizationConfigurationOutput":
        """Delete console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.delete_console_authorization_configuration_input.DeleteConsoleAuthorizationConfigurationInput]",
        ) -> OperationResponse[
            "capo_signin.types.delete_console_authorization_configuration_output.DeleteConsoleAuthorizationConfigurationOutput"
        ]:
            import capo_signin._operations.signin.delete_console_authorization_configuration

            output, http_response = (
                capo_signin._operations.signin.delete_console_authorization_configuration.delete_console_authorization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.delete_console_authorization_configuration_input.DeleteConsoleAuthorizationConfigurationInput = {}
        if target_id is not None:
            input_["target_id"] = target_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_permission_statement(
        self,
        statement_id: "capo_signin.types.statement_id.StatementId",
        *,
        config_overrides: Optional[SigninClientConfig] = None,
        client_token: Optional["capo_signin.types.client_token.ClientToken"] = None,
    ) -> "capo_signin.types.delete_resource_permission_statement_output.DeleteResourcePermissionStatementOutput":
        """Remove a permission statement from the account's SignIn resource-based policy

        Args:
            statement_id: Unique identifier of the permission statement to delete
            client_token: Idempotency token for the request

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.delete_resource_permission_statement_input.DeleteResourcePermissionStatementInput]",
        ) -> OperationResponse[
            "capo_signin.types.delete_resource_permission_statement_output.DeleteResourcePermissionStatementOutput"
        ]:
            import capo_signin._operations.signin.delete_resource_permission_statement

            output, http_response = (
                capo_signin._operations.signin.delete_resource_permission_statement.delete_resource_permission_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.delete_resource_permission_statement_input.DeleteResourcePermissionStatementInput = {
            "statement_id": statement_id
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

    def get_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
        target_id: Optional["capo_signin.types.target_id.TargetId"] = None,
    ) -> "capo_signin.types.get_console_authorization_configuration_output.GetConsoleAuthorizationConfigurationOutput":
        """Get console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.get_console_authorization_configuration_input.GetConsoleAuthorizationConfigurationInput]",
        ) -> OperationResponse[
            "capo_signin.types.get_console_authorization_configuration_output.GetConsoleAuthorizationConfigurationOutput"
        ]:
            import capo_signin._operations.signin.get_console_authorization_configuration

            output, http_response = (
                capo_signin._operations.signin.get_console_authorization_configuration.get_console_authorization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.get_console_authorization_configuration_input.GetConsoleAuthorizationConfigurationInput = {}
        if target_id is not None:
            input_["target_id"] = target_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self, *, config_overrides: Optional[SigninClientConfig] = None
    ) -> "capo_signin.types.get_resource_policy_output.GetResourcePolicyOutput":
        """Retrieve the account's consolidated SignIn resource-based policy

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_signin.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_signin._operations.signin.get_resource_policy

            output, http_response = (
                capo_signin._operations.signin.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.get_resource_policy_input.GetResourcePolicyInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def introspect_o_auth2_token_with_iam(
        self,
        token: "capo_signin.types.introspection_token.IntrospectionToken",
        *,
        config_overrides: Optional[SigninClientConfig] = None,
        token_type_hint: Optional[
            "capo_signin.types.token_type_hint.TokenTypeHint"
        ] = None,
    ) -> "capo_signin.types.introspect_o_auth2_token_with_iam_response.IntrospectOAuth2TokenWithIAMResponse":
        """Grants permission to inspect the metadata and state of an OAuth 2.0 access token or refresh token Implements RFC 7662 OAuth 2.0 Token Introspection over a SigV4-authenticated endpoint. Inspects the metadata of an access_token or refresh_token issued by AWS Sign-In and returns the claims associated with it. Inactive token semantics (RFC 7662 §2.2): when the supplied token is unknown, expired, revoked, malformed, or owned by a different account, the response body is exactly { "active": false } with all other claims omitted.

        Args:
            token: The string value of the token to introspect. May be either an access_token or a refresh_token issued by AWS Sign-In.
            token_type_hint: Optional hint about the type of the token submitted for introspection. The server uses this hint to optimize lookup, but still falls back to the other token type on miss. Allowed values: access_token, refresh_token.

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.introspect_o_auth2_token_with_iam_request.IntrospectOAuth2TokenWithIAMRequest]",
        ) -> OperationResponse[
            "capo_signin.types.introspect_o_auth2_token_with_iam_response.IntrospectOAuth2TokenWithIAMResponse"
        ]:
            import capo_signin._operations.signin.introspect_o_auth2_token_with_iam

            output, http_response = (
                capo_signin._operations.signin.introspect_o_auth2_token_with_iam.introspect_o_auth2_token_with_iam(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.introspect_o_auth2_token_with_iam_request.IntrospectOAuth2TokenWithIAMRequest = {
            "token": token
        }
        if token_type_hint is not None:
            input_["token_type_hint"] = token_type_hint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_resource_permission_statements(
        self,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
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
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.list_resource_permission_statements_input.ListResourcePermissionStatementsInput]",
        ) -> OperationResponse[
            "capo_signin.types.list_resource_permission_statements_output.ListResourcePermissionStatementsOutput"
        ]:
            import capo_signin._operations.signin.list_resource_permission_statements

            output, http_response = (
                capo_signin._operations.signin.list_resource_permission_statements.list_resource_permission_statements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.list_resource_permission_statements_input.ListResourcePermissionStatementsInput = {}
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

    def iter_list_resource_permission_statements(
        self,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
        max_results: Optional[
            "capo_signin.types.console_permission_max_results.ConsolePermissionMaxResults"
        ] = None,
        next_token: Optional["capo_signin.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_signin.types.permission_statement_summary.PermissionStatementSummary]":
        _token = next_token
        while True:
            _response = self.list_resource_permission_statements(
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

    def put_console_authorization_configuration(
        self,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
        target_id: Optional["capo_signin.types.target_id.TargetId"] = None,
    ) -> "capo_signin.types.put_console_authorization_configuration_output.PutConsoleAuthorizationConfigurationOutput":
        """Enable console authorization configuration with automatic scope detection

        Args:
            target_id: Target account identifier

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.conflict_exception.ConflictException: Error thrown when request conflicts with current state HTTP Status Code: 409 Conflict Used when the request conflicts with the current state of the resource
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.resource_not_found_exception.ResourceNotFoundException: Error thrown when requested resource is not found HTTP Status Code: 404 Not Found Used when the specified resource does not exist
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.put_console_authorization_configuration_input.PutConsoleAuthorizationConfigurationInput]",
        ) -> OperationResponse[
            "capo_signin.types.put_console_authorization_configuration_output.PutConsoleAuthorizationConfigurationOutput"
        ]:
            import capo_signin._operations.signin.put_console_authorization_configuration

            output, http_response = (
                capo_signin._operations.signin.put_console_authorization_configuration.put_console_authorization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.put_console_authorization_configuration_input.PutConsoleAuthorizationConfigurationInput = {}
        if target_id is not None:
            input_["target_id"] = target_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_permission_statement(
        self,
        *,
        config_overrides: Optional[SigninClientConfig] = None,
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
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.conflict_exception.ConflictException: Error thrown when request conflicts with current state HTTP Status Code: 409 Conflict Used when the request conflicts with the current state of the resource
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: Error thrown when service quota is exceeded HTTP Status Code: 402 Payment Required (used as quota exceeded indicator) Used when the request would cause a service quota to be exceeded
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.put_resource_permission_statement_input.PutResourcePermissionStatementInput]",
        ) -> OperationResponse[
            "capo_signin.types.put_resource_permission_statement_output.PutResourcePermissionStatementOutput"
        ]:
            import capo_signin._operations.signin.put_resource_permission_statement

            output, http_response = (
                capo_signin._operations.signin.put_resource_permission_statement.put_resource_permission_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def revoke_o_auth2_token_with_iam(
        self,
        token: "capo_signin.types.revocation_token.RevocationToken",
        *,
        config_overrides: Optional[SigninClientConfig] = None,
    ) -> "capo_signin.types.revoke_o_auth2_token_with_iam_response.RevokeOAuth2TokenWithIAMResponse":
        """Grants permission to revoke an OAuth 2.0 refresh token and its associated refresh tokens Revokes a refresh_token issued by AWS Sign-In, invalidating the entire token chain so that the refresh_token can no longer be used to mint new access_tokens. Idempotency: revoking an already-revoked, expired, or otherwise invalid token still returns 200 OK with an empty body. Only the refresh_token type is accepted.

        Args:
            token: The refresh_token to revoke. Must be a refresh_token issued by AWS Sign-In (prefix "ASOR"); access_tokens are not accepted for revocation.

        Raises:
            capo_signin.errors.access_denied_exception.AccessDeniedException: Error thrown for access denied scenarios with flexible HTTP status mapping Runtime HTTP Status Code Mapping: - HTTP 401 (Unauthorized): TOKEN_EXPIRED, AUTHCODE_EXPIRED - HTTP 403 (Forbidden): USER_CREDENTIALS_CHANGED, INSUFFICIENT_PERMISSIONS The specific HTTP status code is determined at runtime based on the error enum value. Consumers should use the error field to determine the specific access denial reason.
            capo_signin.errors.internal_server_exception.InternalServerException: Error thrown when an internal server error occurs HTTP Status Code: 500 Internal Server Error Used for unexpected server-side errors that prevent request processing.
            capo_signin.errors.too_many_requests_error.TooManyRequestsError: Error thrown when rate limit is exceeded HTTP Status Code: 429 Too Many Requests Possible OAuth2ErrorCode values: - INVALID_REQUEST: Rate limiting, too many requests, abuse prevention Possible causes: - Too many token requests from the same client - Rate limiting based on client_id or IP address - Abuse prevention mechanisms triggered - Service protection against excessive token generation
            capo_signin.errors.validation_exception.ValidationException: Error thrown when request validation fails HTTP Status Code: 400 Bad Request Used for request validation errors such as malformed parameters, missing required fields, or invalid parameter values.
            capo_signin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_signin.types.revoke_o_auth2_token_with_iam_request.RevokeOAuth2TokenWithIAMRequest]",
        ) -> OperationResponse[
            "capo_signin.types.revoke_o_auth2_token_with_iam_response.RevokeOAuth2TokenWithIAMResponse"
        ]:
            import capo_signin._operations.signin.revoke_o_auth2_token_with_iam

            output, http_response = (
                capo_signin._operations.signin.revoke_o_auth2_token_with_iam.revoke_o_auth2_token_with_iam(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_signin.types.revoke_o_auth2_token_with_iam_request.RevokeOAuth2TokenWithIAMRequest = {
            "token": token
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
