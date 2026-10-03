"""Generated from Smithy shape ``com.amazonaws.ssooidc#AWSSSOOIDCService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sso_oidc._auth._signers
import capo_sso_oidc._auth._sigv4
from capo_sso_oidc._auth._identity import Credentials
from capo_sso_oidc._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sso_oidc._auth._zapros_handler import AuthMiddleware
from capo_sso_oidc._services._aws_config import aaws_config
from capo_sso_oidc._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sso_oidc.types.arn_type
    import capo_sso_oidc.types.assertion
    import capo_sso_oidc.types.auth_code
    import capo_sso_oidc.types.client_id
    import capo_sso_oidc.types.client_name
    import capo_sso_oidc.types.client_secret
    import capo_sso_oidc.types.client_type
    import capo_sso_oidc.types.code_verifier
    import capo_sso_oidc.types.create_token_request
    import capo_sso_oidc.types.create_token_response
    import capo_sso_oidc.types.create_token_with_iam_request
    import capo_sso_oidc.types.create_token_with_iam_response
    import capo_sso_oidc.types.device_code
    import capo_sso_oidc.types.grant_type
    import capo_sso_oidc.types.grant_types
    import capo_sso_oidc.types.redirect_uris
    import capo_sso_oidc.types.refresh_token
    import capo_sso_oidc.types.register_client_request
    import capo_sso_oidc.types.register_client_response
    import capo_sso_oidc.types.scopes
    import capo_sso_oidc.types.start_device_authorization_request
    import capo_sso_oidc.types.start_device_authorization_response
    import capo_sso_oidc.types.subject_token
    import capo_sso_oidc.types.token_type_uri
    import capo_sso_oidc.types.uri


class AsyncSSOOIDCClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSSOOIDCClient:
    """A client for the ``SSOOIDC`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncSSOOIDCClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSSOOIDCClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSSOOIDCClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_token(
        self,
        client_id: "capo_sso_oidc.types.client_id.ClientId",
        client_secret: "capo_sso_oidc.types.client_secret.ClientSecret",
        grant_type: "capo_sso_oidc.types.grant_type.GrantType",
        *,
        config_overrides: Optional[AsyncSSOOIDCClientConfig] = None,
        device_code: Optional["capo_sso_oidc.types.device_code.DeviceCode"] = None,
        code: Optional["capo_sso_oidc.types.auth_code.AuthCode"] = None,
        refresh_token: Optional[
            "capo_sso_oidc.types.refresh_token.RefreshToken"
        ] = None,
        scope: Optional["capo_sso_oidc.types.scopes.Scopes"] = None,
        redirect_uri: Optional["capo_sso_oidc.types.uri.URI"] = None,
        code_verifier: Optional[
            "capo_sso_oidc.types.code_verifier.CodeVerifier"
        ] = None,
    ) -> "capo_sso_oidc.types.create_token_response.CreateTokenResponse":
        """<p>Creates and returns access and refresh tokens for clients that are authenticated using client secrets. The access token can be used to fetch short-lived credentials for the assigned AWS accounts or to access application APIs using <code>bearer</code> authentication.</p>

        Args:
            client_id: <p>The unique identifier string for the client or application. This value comes from the result of the <a>RegisterClient</a> API.</p>
            client_secret: <p>A secret string generated for the client. This value should come from the persisted result of the <a>RegisterClient</a> API.</p>
            grant_type: <p>Supports the following OAuth grant types: Authorization Code, Device Code, and Refresh Token. Specify one of the following values, depending on the grant type that you want:</p> <p>* Authorization Code - <code>authorization_code</code> </p> <p>* Device Code - <code>urn:ietf:params:oauth:grant-type:device_code</code> </p> <p>* Refresh Token - <code>refresh_token</code> </p>
            device_code: <p>Used only when calling this API for the Device Code grant type. This short-lived code is used to identify this authorization request. This comes from the result of the <a>StartDeviceAuthorization</a> API.</p>
            code: <p>Used only when calling this API for the Authorization Code grant type. The short-lived code is used to identify this authorization request.</p>
            refresh_token: <p>Used only when calling this API for the Refresh Token grant type. This token is used to refresh short-lived tokens, such as the access token, that might expire.</p> <p>For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html">IAM Identity Center OIDC API Reference</a>.</p>
            scope: <p>The list of scopes for which authorization is requested. This parameter has no effect; the access token will always include all scopes configured during client registration.</p>
            redirect_uri: <p>Used only when calling this API for the Authorization Code grant type. This value specifies the location of the client or application that has registered to receive the authorization code.</p>
            code_verifier: <p>Used only when calling this API for the Authorization Code grant type. This value is generated by the client and presented to validate the original code challenge value the client passed at authorization time.</p>

        Raises:
            capo_sso_oidc.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_oidc.errors.authorization_pending_exception.AuthorizationPendingException: <p>Indicates that a request to authorize a client with an access user session token is pending.</p>
            capo_sso_oidc.errors.expired_token_exception.ExpiredTokenException: <p>Indicates that the token issued by the service is expired and is no longer valid.</p>
            capo_sso_oidc.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_sso_oidc.errors.invalid_client_exception.InvalidClientException: <p>Indicates that the <code>clientId</code> or <code>clientSecret</code> in the request is invalid. For example, this can occur when a client sends an incorrect <code>clientId</code> or an expired <code>clientSecret</code>.</p>
            capo_sso_oidc.errors.invalid_grant_exception.InvalidGrantException: <p>Indicates that a request contains an invalid grant. This can occur if a client makes a <a>CreateToken</a> request with an invalid grant type.</p>
            capo_sso_oidc.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso_oidc.errors.invalid_scope_exception.InvalidScopeException: <p>Indicates that the scope provided in the request is invalid.</p>
            capo_sso_oidc.errors.slow_down_exception.SlowDownException: <p>Indicates that the client is making the request too frequently and is more than the service can handle. </p>
            capo_sso_oidc.errors.unauthorized_client_exception.UnauthorizedClientException: <p>Indicates that the client is not currently authorized to make the request. This can happen when a <code>clientId</code> is not issued for a public client.</p>
            capo_sso_oidc.errors.unsupported_grant_type_exception.UnsupportedGrantTypeException: <p>Indicates that the grant type in the request is not supported by the service.</p>
            capo_sso_oidc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Call OAuth/OIDC /token endpoint for Device Code grant with Secret authentication

            >>> await client.create_token(client_id='_yzkThXVzLWVhc3QtMQEXAMPLECLIENTID', client_secret='VERYLONGSECRETeyJraWQiOiJrZXktMTU2NDAyODA5OSIsImFsZyI6IkhTMzg0In0', grant_type='urn:ietf:params:oauth:grant-type:device-code', device_code='yJraWQiOiJrZXktMTU2Njk2ODA4OCIsImFsZyI6IkhTMzIn0EXAMPLEDEVICECODE')
            Call OAuth/OIDC /token endpoint for Refresh Token grant with Secret authentication

            >>> await client.create_token(client_id='_yzkThXVzLWVhc3QtMQEXAMPLECLIENTID', client_secret='VERYLONGSECRETeyJraWQiOiJrZXktMTU2NDAyODA5OSIsImFsZyI6IkhTMzg0In0', grant_type='refresh_token', refresh_token='aorvJYubGpU6i91YnH7Mfo-AT2fIVa1zCfA_Rvq9yjVKIP3onFmmykuQ7E93y2I-9Nyj-A_sVvMufaLNL0bqnDRtgAkc0:MGUCMFrRsktMRVlWaOR70XGMFGLL0SlcCw4DiYveIiOVx1uK9BbD0gvAddsW3UTLozXKMgIxAJ3qxUvjpnlLIOaaKOoa/FuNgqJVvr9GMwDtnAtlh9iZzAkEXAMPLEREFRESHTOKEN', scope=['codewhisperer:completions'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_oidc.types.create_token_request.CreateTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_oidc.types.create_token_response.CreateTokenResponse"
        ]:
            import capo_sso_oidc._operations.awsssooidc_service.create_token

            (
                output,
                http_response,
            ) = await capo_sso_oidc._operations.awsssooidc_service.create_token.async_create_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso_oidc.types.create_token_request.CreateTokenRequest = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
        }
        if device_code is not None:
            input_["device_code"] = device_code
        if code is not None:
            input_["code"] = code
        if refresh_token is not None:
            input_["refresh_token"] = refresh_token
        if scope is not None:
            input_["scope"] = scope
        if redirect_uri is not None:
            input_["redirect_uri"] = redirect_uri
        if code_verifier is not None:
            input_["code_verifier"] = code_verifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_token_with_iam(
        self,
        client_id: "capo_sso_oidc.types.client_id.ClientId",
        grant_type: "capo_sso_oidc.types.grant_type.GrantType",
        *,
        config_overrides: Optional[AsyncSSOOIDCClientConfig] = None,
        code: Optional["capo_sso_oidc.types.auth_code.AuthCode"] = None,
        refresh_token: Optional[
            "capo_sso_oidc.types.refresh_token.RefreshToken"
        ] = None,
        assertion: Optional["capo_sso_oidc.types.assertion.Assertion"] = None,
        scope: Optional["capo_sso_oidc.types.scopes.Scopes"] = None,
        redirect_uri: Optional["capo_sso_oidc.types.uri.URI"] = None,
        subject_token: Optional[
            "capo_sso_oidc.types.subject_token.SubjectToken"
        ] = None,
        subject_token_type: Optional[
            "capo_sso_oidc.types.token_type_uri.TokenTypeURI"
        ] = None,
        requested_token_type: Optional[
            "capo_sso_oidc.types.token_type_uri.TokenTypeURI"
        ] = None,
        code_verifier: Optional[
            "capo_sso_oidc.types.code_verifier.CodeVerifier"
        ] = None,
    ) -> (
        "capo_sso_oidc.types.create_token_with_iam_response.CreateTokenWithIAMResponse"
    ):
        """<p>Creates and returns access and refresh tokens for authorized client applications that are authenticated using any IAM entity, such as a service role or user. These tokens might contain defined scopes that specify permissions such as <code>read:profile</code> or <code>write:data</code>. Through downscoping, you can use the scopes parameter to request tokens with reduced permissions compared to the original client application's permissions or, if applicable, the refresh token's scopes. The access token can be used to fetch short-lived credentials for the assigned Amazon Web Services accounts or to access application APIs using <code>bearer</code> authentication.</p> <note> <p>This API is used with Signature Version 4. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html">Amazon Web Services Signature Version 4 for API Requests</a>.</p> </note>

        Args:
            client_id: <p>The unique identifier string for the client or application. This value is an application ARN that has OAuth grants configured.</p>
            grant_type: <p>Supports the following OAuth grant types: Authorization Code, Refresh Token, JWT Bearer, and Token Exchange. Specify one of the following values, depending on the grant type that you want:</p> <p>* Authorization Code - <code>authorization_code</code> </p> <p>* Refresh Token - <code>refresh_token</code> </p> <p>* JWT Bearer - <code>urn:ietf:params:oauth:grant-type:jwt-bearer</code> </p> <p>* Token Exchange - <code>urn:ietf:params:oauth:grant-type:token-exchange</code> </p>
            code: <p>Used only when calling this API for the Authorization Code grant type. This short-lived code is used to identify this authorization request. The code is obtained through a redirect from IAM Identity Center to a redirect URI persisted in the Authorization Code GrantOptions for the application.</p>
            refresh_token: <p>Used only when calling this API for the Refresh Token grant type. This token is used to refresh short-lived tokens, such as the access token, that might expire.</p> <p>For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html">IAM Identity Center OIDC API Reference</a>.</p>
            assertion: <p>Used only when calling this API for the JWT Bearer grant type. This value specifies the JSON Web Token (JWT) issued by a trusted token issuer. To authorize a trusted token issuer, configure the JWT Bearer GrantOptions for the application.</p>
            scope: <p>The list of scopes for which authorization is requested. The access token that is issued is limited to the scopes that are granted. If the value is not specified, IAM Identity Center authorizes all scopes configured for the application, including the following default scopes: <code>openid</code>, <code>aws</code>, <code>sts:identity_context</code>.</p>
            redirect_uri: <p>Used only when calling this API for the Authorization Code grant type. This value specifies the location of the client or application that has registered to receive the authorization code. </p>
            subject_token: <p>Used only when calling this API for the Token Exchange grant type. This value specifies the subject of the exchange. The value of the subject token must be an access token issued by IAM Identity Center to a different client or application. The access token must have authorized scopes that indicate the requested application as a target audience.</p>
            subject_token_type: <p>Used only when calling this API for the Token Exchange grant type. This value specifies the type of token that is passed as the subject of the exchange. The following value is supported:</p> <p>* Access Token - <code>urn:ietf:params:oauth:token-type:access_token</code> </p>
            requested_token_type: <p>Used only when calling this API for the Token Exchange grant type. This value specifies the type of token that the requester can receive. The following values are supported:</p> <p>* Access Token - <code>urn:ietf:params:oauth:token-type:access_token</code> </p> <p>* Refresh Token - <code>urn:ietf:params:oauth:token-type:refresh_token</code> </p>
            code_verifier: <p>Used only when calling this API for the Authorization Code grant type. This value is generated by the client and presented to validate the original code challenge value the client passed at authorization time.</p>

        Raises:
            capo_sso_oidc.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sso_oidc.errors.authorization_pending_exception.AuthorizationPendingException: <p>Indicates that a request to authorize a client with an access user session token is pending.</p>
            capo_sso_oidc.errors.expired_token_exception.ExpiredTokenException: <p>Indicates that the token issued by the service is expired and is no longer valid.</p>
            capo_sso_oidc.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_sso_oidc.errors.invalid_client_exception.InvalidClientException: <p>Indicates that the <code>clientId</code> or <code>clientSecret</code> in the request is invalid. For example, this can occur when a client sends an incorrect <code>clientId</code> or an expired <code>clientSecret</code>.</p>
            capo_sso_oidc.errors.invalid_grant_exception.InvalidGrantException: <p>Indicates that a request contains an invalid grant. This can occur if a client makes a <a>CreateToken</a> request with an invalid grant type.</p>
            capo_sso_oidc.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso_oidc.errors.invalid_request_region_exception.InvalidRequestRegionException: <p>Indicates that a token provided as input to the request was issued by and is only usable by calling IAM Identity Center endpoints in another region.</p>
            capo_sso_oidc.errors.invalid_scope_exception.InvalidScopeException: <p>Indicates that the scope provided in the request is invalid.</p>
            capo_sso_oidc.errors.slow_down_exception.SlowDownException: <p>Indicates that the client is making the request too frequently and is more than the service can handle. </p>
            capo_sso_oidc.errors.unauthorized_client_exception.UnauthorizedClientException: <p>Indicates that the client is not currently authorized to make the request. This can happen when a <code>clientId</code> is not issued for a public client.</p>
            capo_sso_oidc.errors.unsupported_grant_type_exception.UnsupportedGrantTypeException: <p>Indicates that the grant type in the request is not supported by the service.</p>
            capo_sso_oidc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Call OAuth/OIDC /token endpoint for Authorization Code grant with IAM authentication

            >>> await client.create_token_with_iam(client_id='arn:aws:sso::123456789012:application/ssoins-111111111111/apl-222222222222', grant_type='authorization_code', code='yJraWQiOiJrZXktMTU2Njk2ODA4OCIsImFsZyI6IkhTMzg0In0EXAMPLEAUTHCODE', redirect_uri='https://mywebapp.example/redirect', scope=['openid', 'aws', 'sts:identity_context'])
            Call OAuth/OIDC /token endpoint for JWT Bearer grant with IAM authentication

            >>> await client.create_token_with_iam(client_id='arn:aws:sso::123456789012:application/ssoins-111111111111/apl-222222222222', grant_type='urn:ietf:params:oauth:grant-type:jwt-bearer', assertion='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjFMVE16YWtpaGlSbGFfOHoyQkVKVlhlV01xbyJ9.eyJ2ZXIiOiIyLjAiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOTEyMjA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkL3YyLjAiLCJzdWIiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFJa3pxRlZyU2FTYUZIeTc4MmJidGFRIiwiYXVkIjoiNmNiMDQwMTgtYTNmNS00NmE3LWI5OTUtOTQwYzc4ZjVhZWYzIiwiZXhwIjoxNTM2MzYxNDExLCJpYXQiOjE1MzYyNzQ3MTEsIm5iZiI6MTUzNjI3NDcxMSwibmFtZSI6IkFiZSBMaW5jb2xuIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiQWJlTGlAbWljcm9zb2Z0LmNvbSIsIm9pZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC02NmYzLTMzMzJlY2E3ZWE4MSIsInRpZCI6IjkxMjIwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsIm5vbmNlIjoiMTIzNTIzIiwiYWlvIjoiRGYyVVZYTDFpeCFsTUNXTVNPSkJjRmF0emNHZnZGR2hqS3Y4cTVnMHg3MzJkUjVNQjVCaXN2R1FPN1lXQnlqZDhpUURMcSFlR2JJRGFreXA1bW5PcmNkcUhlWVNubHRlcFFtUnA2QUlaOGpZIn0.1AFWW-Ck5nROwSlltm7GzZvDwUkqvhSQpm55TQsmVo9Y59cLhRXpvB8n-55HCr9Z6G_31_UbeUkoz612I2j_Sm9FFShSDDjoaLQr54CreGIJvjtmS3EkK9a7SJBbcpL1MpUtlfygow39tFjY7EVNW9plWUvRrTgVk7lYLprvfzw-CIqw3gHC-T7IK_m_xkr08INERBtaecwhTeN4chPC4W3jdmw_lIxzC48YoQ0dB1L9-ImX98Egypfrlbm0IBL5spFzL6JDZIRRJOu8vecJvj1mq-IUhGt0MacxX8jdxYLP-KUu2d9MbNKpCKJuZ7p8gwTL5B7NlUdh_dmSviPWrw')
            Call OAuth/OIDC /token endpoint for Refresh Token grant with IAM authentication

            >>> await client.create_token_with_iam(client_id='arn:aws:sso::123456789012:application/ssoins-111111111111/apl-222222222222', grant_type='refresh_token', refresh_token='aorvJYubGpU6i91YnH7Mfo-AT2fIVa1zCfA_Rvq9yjVKIP3onFmmykuQ7E93y2I-9Nyj-A_sVvMufaLNL0bqnDRtgAkc0:MGUCMFrRsktMRVlWaOR70XGMFGLL0SlcCw4DiYveIiOVx1uK9BbD0gvAddsW3UTLozXKMgIxAJ3qxUvjpnlLIOaaKOoa/FuNgqJVvr9GMwDtnAtlh9iZzAkEXAMPLEREFRESHTOKEN')
            Call OAuth/OIDC /token endpoint for Token Exchange grant with IAM authentication

            >>> await client.create_token_with_iam(client_id='arn:aws:sso::123456789012:application/ssoins-111111111111/apl-222222222222', grant_type='urn:ietf:params:oauth:grant-type:token-exchange', subject_token='aoak-Hig8TUDPNX1xZwOMXM5MxOWDL0E0jg9P6_C_jKQPxS_SKCP6f0kh1Up4g7TtvQqkMnD-GJiU_S1gvug6SrggAkc0:MGYCMQD3IatVjV7jAJU91kK3PkS/SfA2wtgWzOgZWDOR7sDGN9t0phCZz5It/aes/3C1Zj0CMQCKWOgRaiz6AIhza3DSXQNMLjRKXC8F8ceCsHlgYLMZ7hZDIFFERENTACCESSTOKEN', subject_token_type='urn:ietf:params:oauth:token-type:access_token', requested_token_type='urn:ietf:params:oauth:token-type:access_token')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_oidc.types.create_token_with_iam_request.CreateTokenWithIAMRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_oidc.types.create_token_with_iam_response.CreateTokenWithIAMResponse"
        ]:
            import capo_sso_oidc._operations.awsssooidc_service.create_token_with_iam

            (
                output,
                http_response,
            ) = await capo_sso_oidc._operations.awsssooidc_service.create_token_with_iam.async_create_token_with_iam(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso_oidc.types.create_token_with_iam_request.CreateTokenWithIAMRequest = {
            "client_id": client_id,
            "grant_type": grant_type,
        }
        if code is not None:
            input_["code"] = code
        if refresh_token is not None:
            input_["refresh_token"] = refresh_token
        if assertion is not None:
            input_["assertion"] = assertion
        if scope is not None:
            input_["scope"] = scope
        if redirect_uri is not None:
            input_["redirect_uri"] = redirect_uri
        if subject_token is not None:
            input_["subject_token"] = subject_token
        if subject_token_type is not None:
            input_["subject_token_type"] = subject_token_type
        if requested_token_type is not None:
            input_["requested_token_type"] = requested_token_type
        if code_verifier is not None:
            input_["code_verifier"] = code_verifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_client(
        self,
        client_name: "capo_sso_oidc.types.client_name.ClientName",
        client_type: "capo_sso_oidc.types.client_type.ClientType",
        *,
        config_overrides: Optional[AsyncSSOOIDCClientConfig] = None,
        scopes: Optional["capo_sso_oidc.types.scopes.Scopes"] = None,
        redirect_uris: Optional[
            "capo_sso_oidc.types.redirect_uris.RedirectUris"
        ] = None,
        grant_types: Optional["capo_sso_oidc.types.grant_types.GrantTypes"] = None,
        issuer_url: Optional["capo_sso_oidc.types.uri.URI"] = None,
        entitled_application_arn: Optional[
            "capo_sso_oidc.types.arn_type.ArnType"
        ] = None,
    ) -> "capo_sso_oidc.types.register_client_response.RegisterClientResponse":
        """<p>Registers a public client with IAM Identity Center. This allows clients to perform authorization using the authorization code grant with Proof Key for Code Exchange (PKCE) or the device code grant.</p>

        Args:
            client_name: <p>The friendly name of the client.</p>
            client_type: <p>The type of client. The service supports only <code>public</code> as a client type. Anything other than public will be rejected by the service.</p>
            scopes: <p>The list of scopes that are defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token.</p>
            redirect_uris: <p>The list of redirect URI that are defined by the client. At completion of authorization, this list is used to restrict what locations the user agent can be redirected back to.</p>
            grant_types: <p>The list of OAuth 2.0 grant types that are defined by the client. This list is used to restrict the token granting flows available to the client. Supports the following OAuth 2.0 grant types: Authorization Code, Device Code, and Refresh Token. </p> <p>* Authorization Code - <code>authorization_code</code> </p> <p>* Device Code - <code>urn:ietf:params:oauth:grant-type:device_code</code> </p> <p>* Refresh Token - <code>refresh_token</code> </p>
            issuer_url: <p>The IAM Identity Center Issuer URL associated with an instance of IAM Identity Center. This value is needed for user access to resources through the client.</p>
            entitled_application_arn: <p>This IAM Identity Center application ARN is used to define administrator-managed configuration for public client access to resources. At authorization, the scopes, grants, and redirect URI available to this client will be restricted by this application resource.</p>

        Raises:
            capo_sso_oidc.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_sso_oidc.errors.invalid_client_metadata_exception.InvalidClientMetadataException: <p>Indicates that the client information sent in the request during registration is invalid.</p>
            capo_sso_oidc.errors.invalid_redirect_uri_exception.InvalidRedirectUriException: <p>Indicates that one or more redirect URI in the request is not supported for this operation.</p>
            capo_sso_oidc.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso_oidc.errors.invalid_scope_exception.InvalidScopeException: <p>Indicates that the scope provided in the request is invalid.</p>
            capo_sso_oidc.errors.slow_down_exception.SlowDownException: <p>Indicates that the client is making the request too frequently and is more than the service can handle. </p>
            capo_sso_oidc.errors.unsupported_grant_type_exception.UnsupportedGrantTypeException: <p>Indicates that the grant type in the request is not supported by the service.</p>
            capo_sso_oidc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Call OAuth/OIDC /register-client endpoint

            >>> await client.register_client(client_name='My IDE Plugin', client_type='public', scopes=['sso:account:access', 'codewhisperer:completions'], redirect_uris=['127.0.0.1:PORT/oauth/callback'], grant_types=['authorization_code', 'refresh_token'], issuer_url='https://identitycenter.amazonaws.com/ssoins-1111111111111111', entitled_application_arn='arn:aws:sso::ACCOUNTID:application/ssoins-1111111111111111/apl-1111111111111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_oidc.types.register_client_request.RegisterClientRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_oidc.types.register_client_response.RegisterClientResponse"
        ]:
            import capo_sso_oidc._operations.awsssooidc_service.register_client

            (
                output,
                http_response,
            ) = await capo_sso_oidc._operations.awsssooidc_service.register_client.async_register_client(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso_oidc.types.register_client_request.RegisterClientRequest = {
            "client_name": client_name,
            "client_type": client_type,
        }
        if scopes is not None:
            input_["scopes"] = scopes
        if redirect_uris is not None:
            input_["redirect_uris"] = redirect_uris
        if grant_types is not None:
            input_["grant_types"] = grant_types
        if issuer_url is not None:
            input_["issuer_url"] = issuer_url
        if entitled_application_arn is not None:
            input_["entitled_application_arn"] = entitled_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_device_authorization(
        self,
        client_id: "capo_sso_oidc.types.client_id.ClientId",
        client_secret: "capo_sso_oidc.types.client_secret.ClientSecret",
        start_url: "capo_sso_oidc.types.uri.URI",
        *,
        config_overrides: Optional[AsyncSSOOIDCClientConfig] = None,
    ) -> "capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse":
        """<p>Initiates device authorization by requesting a pair of verification codes from the authorization service.</p>

        Args:
            client_id: <p>The unique identifier string for the client that is registered with IAM Identity Center. This value should come from the persisted result of the <a>RegisterClient</a> API operation.</p>
            client_secret: <p>A secret string that is generated for the client. This value should come from the persisted result of the <a>RegisterClient</a> API operation.</p>
            start_url: <p>The URL for the Amazon Web Services access portal. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html">Using the Amazon Web Services access portal</a> in the <i>IAM Identity Center User Guide</i>.</p>

        Raises:
            capo_sso_oidc.errors.internal_server_exception.InternalServerException: <p>Indicates that an error from the service occurred while trying to process a request.</p>
            capo_sso_oidc.errors.invalid_client_exception.InvalidClientException: <p>Indicates that the <code>clientId</code> or <code>clientSecret</code> in the request is invalid. For example, this can occur when a client sends an incorrect <code>clientId</code> or an expired <code>clientSecret</code>.</p>
            capo_sso_oidc.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that something is wrong with the input to the request. For example, a required parameter might be missing or out of range.</p>
            capo_sso_oidc.errors.slow_down_exception.SlowDownException: <p>Indicates that the client is making the request too frequently and is more than the service can handle. </p>
            capo_sso_oidc.errors.unauthorized_client_exception.UnauthorizedClientException: <p>Indicates that the client is not currently authorized to make the request. This can happen when a <code>clientId</code> is not issued for a public client.</p>
            capo_sso_oidc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Call OAuth/OIDC /start-device-authorization endpoint

            >>> await client.start_device_authorization(client_id='_yzkThXVzLWVhc3QtMQEXAMPLECLIENTID', client_secret='VERYLONGSECRETeyJraWQiOiJrZXktMTU2NDAyODA5OSIsImFsZyI6IkhTMzg0In0', start_url='https://identitycenter.amazonaws.com/ssoins-111111111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sso_oidc.types.start_device_authorization_request.StartDeviceAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_sso_oidc.types.start_device_authorization_response.StartDeviceAuthorizationResponse"
        ]:
            import capo_sso_oidc._operations.awsssooidc_service.start_device_authorization

            (
                output,
                http_response,
            ) = await capo_sso_oidc._operations.awsssooidc_service.start_device_authorization.async_start_device_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sso_oidc.types.start_device_authorization_request.StartDeviceAuthorizationRequest = {
            "client_id": client_id,
            "client_secret": client_secret,
            "start_url": start_url,
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
