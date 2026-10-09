"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#AWSCognitoIdentityService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cognito_identity._auth._signers
import capo_cognito_identity._auth._sigv4
from capo_cognito_identity._auth._identity import Credentials
from capo_cognito_identity._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cognito_identity._auth._zapros_handler import AuthMiddleware
from capo_cognito_identity._pagination import resolve_path as _resolve_path
from capo_cognito_identity._services._aws_config import aaws_config
from capo_cognito_identity._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cognito_identity.types.account_id
    import capo_cognito_identity.types.arn_string
    import capo_cognito_identity.types.classic_flow
    import capo_cognito_identity.types.cognito_identity_provider_list
    import capo_cognito_identity.types.create_identity_pool_input
    import capo_cognito_identity.types.delete_identities_input
    import capo_cognito_identity.types.delete_identities_response
    import capo_cognito_identity.types.delete_identity_pool_input
    import capo_cognito_identity.types.describe_identity_input
    import capo_cognito_identity.types.describe_identity_pool_input
    import capo_cognito_identity.types.developer_provider_name
    import capo_cognito_identity.types.developer_user_identifier
    import capo_cognito_identity.types.get_credentials_for_identity_input
    import capo_cognito_identity.types.get_credentials_for_identity_response
    import capo_cognito_identity.types.get_id_input
    import capo_cognito_identity.types.get_id_response
    import capo_cognito_identity.types.get_identity_pool_roles_input
    import capo_cognito_identity.types.get_identity_pool_roles_response
    import capo_cognito_identity.types.get_open_id_token_for_developer_identity_input
    import capo_cognito_identity.types.get_open_id_token_for_developer_identity_response
    import capo_cognito_identity.types.get_open_id_token_input
    import capo_cognito_identity.types.get_open_id_token_response
    import capo_cognito_identity.types.get_principal_tag_attribute_map_input
    import capo_cognito_identity.types.get_principal_tag_attribute_map_response
    import capo_cognito_identity.types.hide_disabled
    import capo_cognito_identity.types.identity_description
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.identity_id_list
    import capo_cognito_identity.types.identity_pool
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.identity_pool_name
    import capo_cognito_identity.types.identity_pool_short_description
    import capo_cognito_identity.types.identity_pool_tags_list_type
    import capo_cognito_identity.types.identity_pool_tags_type
    import capo_cognito_identity.types.identity_pool_unauthenticated
    import capo_cognito_identity.types.identity_provider_name
    import capo_cognito_identity.types.identity_providers
    import capo_cognito_identity.types.list_identities_input
    import capo_cognito_identity.types.list_identities_response
    import capo_cognito_identity.types.list_identity_pools_input
    import capo_cognito_identity.types.list_identity_pools_response
    import capo_cognito_identity.types.list_tags_for_resource_input
    import capo_cognito_identity.types.list_tags_for_resource_response
    import capo_cognito_identity.types.logins_list
    import capo_cognito_identity.types.logins_map
    import capo_cognito_identity.types.lookup_developer_identity_input
    import capo_cognito_identity.types.lookup_developer_identity_response
    import capo_cognito_identity.types.merge_developer_identities_input
    import capo_cognito_identity.types.merge_developer_identities_response
    import capo_cognito_identity.types.oidc_provider_list
    import capo_cognito_identity.types.pagination_key
    import capo_cognito_identity.types.principal_tags
    import capo_cognito_identity.types.query_limit
    import capo_cognito_identity.types.role_mapping_map
    import capo_cognito_identity.types.roles_map
    import capo_cognito_identity.types.saml_provider_list
    import capo_cognito_identity.types.set_identity_pool_roles_input
    import capo_cognito_identity.types.set_principal_tag_attribute_map_input
    import capo_cognito_identity.types.set_principal_tag_attribute_map_response
    import capo_cognito_identity.types.tag_resource_input
    import capo_cognito_identity.types.tag_resource_response
    import capo_cognito_identity.types.token_duration
    import capo_cognito_identity.types.unlink_developer_identity_input
    import capo_cognito_identity.types.unlink_identity_input
    import capo_cognito_identity.types.untag_resource_input
    import capo_cognito_identity.types.untag_resource_response
    import capo_cognito_identity.types.use_defaults


class AsyncCognitoIdentityClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCognitoIdentityClient:
    """A client for the ``CognitoIdentity`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
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
        anonymous: bool | None = None,
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
        self._config = AsyncCognitoIdentityClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCognitoIdentityClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def create_identity_pool(
        self,
        identity_pool_name: "capo_cognito_identity.types.identity_pool_name.IdentityPoolName",
        allow_unauthenticated_identities: "capo_cognito_identity.types.identity_pool_unauthenticated.IdentityPoolUnauthenticated",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        allow_classic_flow: Optional[
            "capo_cognito_identity.types.classic_flow.ClassicFlow"
        ] = None,
        supported_login_providers: Optional[
            "capo_cognito_identity.types.identity_providers.IdentityProviders"
        ] = None,
        developer_provider_name: Optional[
            "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName"
        ] = None,
        open_id_connect_provider_ar_ns: Optional[
            "capo_cognito_identity.types.oidc_provider_list.OIDCProviderList"
        ] = None,
        cognito_identity_providers: Optional[
            "capo_cognito_identity.types.cognito_identity_provider_list.CognitoIdentityProviderList"
        ] = None,
        saml_provider_ar_ns: Optional[
            "capo_cognito_identity.types.saml_provider_list.SAMLProviderList"
        ] = None,
        identity_pool_tags: Optional[
            "capo_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType"
        ] = None,
    ) -> "capo_cognito_identity.types.identity_pool.IdentityPool":
        """<p>Creates a new identity pool. The identity pool is a store of user identity information that is specific to your Amazon Web Services account. The keys for <code>SupportedLoginProviders</code> are as follows:</p> <ul> <li> <p>Facebook: <code>graph.facebook.com</code> </p> </li> <li> <p>Google: <code>accounts.google.com</code> </p> </li> <li> <p>Sign in With Apple: <code>appleid.apple.com</code> </p> </li> <li> <p>Amazon: <code>www.amazon.com</code> </p> </li> <li> <p>Twitter: <code>api.twitter.com</code> </p> </li> <li> <p>Digits: <code>www.digits.com</code> </p> </li> </ul> <important> <p>If you don't provide a value for a parameter, Amazon Cognito sets it to its default value. </p> </important> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_name: <p>A string that you provide.</p>
            allow_unauthenticated_identities: <p>TRUE if the identity pool supports unauthenticated logins.</p>
            allow_classic_flow: <p>Enables or disables the Basic (Classic) authentication flow. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html">Identity Pools (Federated Identities) Authentication Flow</a> in the <i>Amazon Cognito Developer Guide</i>.</p>
            supported_login_providers: <p>Optional key:value pairs mapping provider names to provider app IDs.</p>
            developer_provider_name: <p>The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the <code>DeveloperProviderName</code>, you can use letters as well as period (<code>.</code>), underscore (<code>_</code>), and dash (<code>-</code>).</p> <p>Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.</p>
            open_id_connect_provider_ar_ns: <p>The Amazon Resource Names (ARN) of the OpenID Connect providers.</p>
            cognito_identity_providers: <p>An array of Amazon Cognito user pools and their client IDs.</p>
            saml_provider_ar_ns: <p>An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.</p>
            identity_pool_tags: <p>Tags to assign to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.limit_exceeded_exception.LimitExceededException: <p>Thrown when the total number of user pools has exceeded a preset limit.</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.create_identity_pool_input.CreateIdentityPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.identity_pool.IdentityPool"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.create_identity_pool

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.create_identity_pool.async_create_identity_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.create_identity_pool_input.CreateIdentityPoolInput = {
            "identity_pool_name": identity_pool_name,
            "allow_unauthenticated_identities": allow_unauthenticated_identities,
        }
        if allow_classic_flow is not None:
            input_["allow_classic_flow"] = allow_classic_flow
        if supported_login_providers is not None:
            input_["supported_login_providers"] = supported_login_providers
        if developer_provider_name is not None:
            input_["developer_provider_name"] = developer_provider_name
        if open_id_connect_provider_ar_ns is not None:
            input_["open_id_connect_provider_ar_ns"] = open_id_connect_provider_ar_ns
        if cognito_identity_providers is not None:
            input_["cognito_identity_providers"] = cognito_identity_providers
        if saml_provider_ar_ns is not None:
            input_["saml_provider_ar_ns"] = saml_provider_ar_ns
        if identity_pool_tags is not None:
            input_["identity_pool_tags"] = identity_pool_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_identities(
        self,
        identity_ids_to_delete: "capo_cognito_identity.types.identity_id_list.IdentityIdList",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.delete_identities_response.DeleteIdentitiesResponse":
        """<p>Deletes identities from an identity pool. You can specify a list of 1-60 identities that you want to delete.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_ids_to_delete: <p>A list of 1-60 identities that you want to delete.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.delete_identities_input.DeleteIdentitiesInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.delete_identities_response.DeleteIdentitiesResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.delete_identities

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.delete_identities.async_delete_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.delete_identities_input.DeleteIdentitiesInput = {
            "identity_ids_to_delete": identity_ids_to_delete
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_identity_pool(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an identity pool. Once a pool is deleted, users will not be able to authenticate with the pool.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.delete_identity_pool_input.DeleteIdentityPoolInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.delete_identity_pool

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.delete_identity_pool.async_delete_identity_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.delete_identity_pool_input.DeleteIdentityPoolInput = {
            "identity_pool_id": identity_pool_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_identity(
        self,
        identity_id: "capo_cognito_identity.types.identity_id.IdentityId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.identity_description.IdentityDescription":
        """<p>Returns metadata related to the given identity, including when the identity was created and any associated linked logins.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.describe_identity_input.DescribeIdentityInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.identity_description.IdentityDescription"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.describe_identity

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.describe_identity.async_describe_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.describe_identity_input.DescribeIdentityInput = {
            "identity_id": identity_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_identity_pool(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.identity_pool.IdentityPool":
        """<p>Gets details about a particular identity pool, including the pool name, ID description, creation date, and current number of users.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.describe_identity_pool_input.DescribeIdentityPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.identity_pool.IdentityPool"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.describe_identity_pool

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.describe_identity_pool.async_describe_identity_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.describe_identity_pool_input.DescribeIdentityPoolInput = {
            "identity_pool_id": identity_pool_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_credentials_for_identity(
        self,
        identity_id: "capo_cognito_identity.types.identity_id.IdentityId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        logins: Optional["capo_cognito_identity.types.logins_map.LoginsMap"] = None,
        custom_role_arn: Optional[
            "capo_cognito_identity.types.arn_string.ARNString"
        ] = None,
    ) -> "capo_cognito_identity.types.get_credentials_for_identity_response.GetCredentialsForIdentityResponse":
        """<p>Returns credentials for the provided identity ID. Any provided logins will be validated against supported login providers. If the token is for <code>cognito-identity.amazonaws.com</code>, it will be passed through to Security Token Service with the appropriate role for the token.</p> <p>This is a public API. You do not need any credentials to call this API.</p>

        Args:
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>
            logins: <p>A set of optional name-value pairs that map provider names to provider tokens. The name-value pair will follow the syntax "provider_name": "provider_user_identifier".</p> <p>Logins should not be specified when trying to get credentials for an unauthenticated identity.</p> <p>The Logins parameter is required when using identities associated with external identity providers such as Facebook. For examples of <code>Logins</code> maps, see the code examples in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html">External Identity Providers</a> section of the Amazon Cognito Developer Guide.</p>
            custom_role_arn: <p>The Amazon Resource Name (ARN) of the role to be assumed when multiple roles were received in the token from the identity provider. For example, a SAML-based identity provider. This parameter is optional for identity providers that do not support role customization.</p>

        Raises:
            capo_cognito_identity.errors.external_service_exception.ExternalServiceException: <p>An exception thrown when a dependent service such as Facebook or Twitter is not responding</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_identity_pool_configuration_exception.InvalidIdentityPoolConfigurationException: <p>If you provided authentication information in the request, the identity pool has no authenticated role configured, or STS returned an error response to the request to assume the authenticated role from the identity pool. If you provided no authentication information in the request, the identity pool has no unauthenticated role configured, or STS returned an error response to the request to assume the unauthenticated role from the identity pool.</p> <p>Your role trust policy must grant <code>AssumeRoleWithWebIdentity</code> permissions to <code>cognito-identity.amazonaws.com</code>.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.get_credentials_for_identity_input.GetCredentialsForIdentityInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.get_credentials_for_identity_response.GetCredentialsForIdentityResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.get_credentials_for_identity

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.get_credentials_for_identity.async_get_credentials_for_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.get_credentials_for_identity_input.GetCredentialsForIdentityInput = {
            "identity_id": identity_id
        }
        if logins is not None:
            input_["logins"] = logins
        if custom_role_arn is not None:
            input_["custom_role_arn"] = custom_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_id(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        account_id: Optional["capo_cognito_identity.types.account_id.AccountId"] = None,
        logins: Optional["capo_cognito_identity.types.logins_map.LoginsMap"] = None,
    ) -> "capo_cognito_identity.types.get_id_response.GetIdResponse":
        """<p>Generates (or retrieves) IdentityID. Supplying multiple logins will create an implicit linked account.</p> <p>This is a public API. You do not need any credentials to call this API.</p>

        Args:
            account_id: <p>A standard Amazon Web Services account ID (9+ digits).</p>
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            logins: <p>A set of optional name-value pairs that map provider names to provider tokens. The available provider names for <code>Logins</code> are as follows:</p> <ul> <li> <p>Facebook: <code>graph.facebook.com</code> </p> </li> <li> <p>Amazon Cognito user pool: <code>cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID></code>, for example, <code>cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789</code>. </p> </li> <li> <p>Google: <code>accounts.google.com</code> </p> </li> <li> <p>Amazon: <code>www.amazon.com</code> </p> </li> <li> <p>Twitter: <code>api.twitter.com</code> </p> </li> <li> <p>Digits: <code>www.digits.com</code> </p> </li> </ul>

        Raises:
            capo_cognito_identity.errors.external_service_exception.ExternalServiceException: <p>An exception thrown when a dependent service such as Facebook or Twitter is not responding</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.limit_exceeded_exception.LimitExceededException: <p>Thrown when the total number of user pools has exceeded a preset limit.</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.get_id_input.GetIdInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.get_id_response.GetIdResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.get_id

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.get_id.async_get_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.get_id_input.GetIdInput = {
            "identity_pool_id": identity_pool_id
        }
        if account_id is not None:
            input_["account_id"] = account_id
        if logins is not None:
            input_["logins"] = logins

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_pool_roles(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.get_identity_pool_roles_response.GetIdentityPoolRolesResponse":
        """<p>Gets the roles for an identity pool.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.get_identity_pool_roles_input.GetIdentityPoolRolesInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.get_identity_pool_roles_response.GetIdentityPoolRolesResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.get_identity_pool_roles

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.get_identity_pool_roles.async_get_identity_pool_roles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.get_identity_pool_roles_input.GetIdentityPoolRolesInput = {
            "identity_pool_id": identity_pool_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_open_id_token(
        self,
        identity_id: "capo_cognito_identity.types.identity_id.IdentityId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        logins: Optional["capo_cognito_identity.types.logins_map.LoginsMap"] = None,
    ) -> (
        "capo_cognito_identity.types.get_open_id_token_response.GetOpenIdTokenResponse"
    ):
        """<p>Gets an OpenID token, using a known Cognito ID. This known Cognito ID is returned by <a>GetId</a>. You can optionally add additional logins for the identity. Supplying multiple logins creates an implicit link.</p> <p>The OpenID token is valid for 10 minutes.</p> <p>This is a public API. You do not need any credentials to call this API.</p>

        Args:
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>
            logins: <p>A set of optional name-value pairs that map provider names to provider tokens. When using graph.facebook.com and www.amazon.com, supply the access_token returned from the provider's authflow. For accounts.google.com, an Amazon Cognito user pool provider, or any other OpenID Connect provider, always include the <code>id_token</code>.</p>

        Raises:
            capo_cognito_identity.errors.external_service_exception.ExternalServiceException: <p>An exception thrown when a dependent service such as Facebook or Twitter is not responding</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.get_open_id_token_input.GetOpenIdTokenInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.get_open_id_token_response.GetOpenIdTokenResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.get_open_id_token

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.get_open_id_token.async_get_open_id_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.get_open_id_token_input.GetOpenIdTokenInput = {
            "identity_id": identity_id
        }
        if logins is not None:
            input_["logins"] = logins

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_open_id_token_for_developer_identity(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        logins: "capo_cognito_identity.types.logins_map.LoginsMap",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        identity_id: Optional[
            "capo_cognito_identity.types.identity_id.IdentityId"
        ] = None,
        principal_tags: Optional[
            "capo_cognito_identity.types.principal_tags.PrincipalTags"
        ] = None,
        token_duration: Optional[
            "capo_cognito_identity.types.token_duration.TokenDuration"
        ] = None,
    ) -> "capo_cognito_identity.types.get_open_id_token_for_developer_identity_response.GetOpenIdTokenForDeveloperIdentityResponse":
        """<p>Registers (or retrieves) a Cognito <code>IdentityId</code> and an OpenID Connect token for a user authenticated by your backend authentication process. Supplying multiple logins will create an implicit linked account. You can only specify one developer provider as part of the <code>Logins</code> map, which is linked to the identity pool. The developer provider is the "domain" by which Cognito will refer to your users.</p> <p>You can use <code>GetOpenIdTokenForDeveloperIdentity</code> to create a new identity and to link new logins (that is, user credentials issued by a public provider or developer provider) to an existing identity. When you want to create a new identity, the <code>IdentityId</code> should be null. When you want to associate a new login with an existing authenticated/unauthenticated identity, you can do so by providing the existing <code>IdentityId</code>. This API will create the identity in the specified <code>IdentityPoolId</code>.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>
            logins: <p>A set of optional name-value pairs that map provider names to provider tokens. Each name-value pair represents a user from a public provider or developer provider. If the user is from a developer provider, the name-value pair will follow the syntax <code>"developer_provider_name": "developer_user_identifier"</code>. The developer provider is the "domain" by which Cognito will refer to your users; you provided this domain while creating/updating the identity pool. The developer user identifier is an identifier from your backend that uniquely identifies a user. When you create an identity pool, you can specify the supported logins.</p>
            principal_tags: <p>Use this operation to configure attribute mappings for custom providers. </p>
            token_duration: <p>The expiration time of the token, in seconds. You can specify a custom expiration time for the token so that you can cache it. If you don't provide an expiration time, the token is valid for 15 minutes. You can exchange the token with Amazon STS for temporary Amazon Web Services credentials, which are valid for a maximum of one hour. The maximum token duration you can set is 24 hours. You should take care in setting the expiration time for a token, as there are significant security implications: an attacker could use a leaked token to access your Amazon Web Services resources for the token's duration.</p> <note> <p>Please provide for a small grace period, usually no more than 5 minutes, to account for clock skew.</p> </note>

        Raises:
            capo_cognito_identity.errors.developer_user_already_registered_exception.DeveloperUserAlreadyRegisteredException: <p>The provided developer user identifier is already registered with Cognito under a different identity ID.</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.get_open_id_token_for_developer_identity_input.GetOpenIdTokenForDeveloperIdentityInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.get_open_id_token_for_developer_identity_response.GetOpenIdTokenForDeveloperIdentityResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.get_open_id_token_for_developer_identity

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.get_open_id_token_for_developer_identity.async_get_open_id_token_for_developer_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.get_open_id_token_for_developer_identity_input.GetOpenIdTokenForDeveloperIdentityInput = {
            "identity_pool_id": identity_pool_id,
            "logins": logins,
        }
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if principal_tags is not None:
            input_["principal_tags"] = principal_tags
        if token_duration is not None:
            input_["token_duration"] = token_duration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_principal_tag_attribute_map(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        identity_provider_name: "capo_cognito_identity.types.identity_provider_name.IdentityProviderName",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.get_principal_tag_attribute_map_response.GetPrincipalTagAttributeMapResponse":
        """<p>Use <code>GetPrincipalTagAttributeMap</code> to list all mappings between <code>PrincipalTags</code> and user attributes.</p>

        Args:
            identity_pool_id: <p>You can use this operation to get the ID of the Identity Pool you setup attribute mappings for.</p>
            identity_provider_name: <p>You can use this operation to get the provider name.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.get_principal_tag_attribute_map_input.GetPrincipalTagAttributeMapInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.get_principal_tag_attribute_map_response.GetPrincipalTagAttributeMapResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.get_principal_tag_attribute_map

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.get_principal_tag_attribute_map.async_get_principal_tag_attribute_map(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.get_principal_tag_attribute_map_input.GetPrincipalTagAttributeMapInput = {
            "identity_pool_id": identity_pool_id,
            "identity_provider_name": identity_provider_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_identities(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        max_results: "capo_cognito_identity.types.query_limit.QueryLimit",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        next_token: Optional[
            "capo_cognito_identity.types.pagination_key.PaginationKey"
        ] = None,
        hide_disabled: Optional[
            "capo_cognito_identity.types.hide_disabled.HideDisabled"
        ] = None,
    ) -> "capo_cognito_identity.types.list_identities_response.ListIdentitiesResponse":
        """<p>Lists the identities in an identity pool.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            max_results: <p>The maximum number of identities to return.</p>
            next_token: <p>A pagination token.</p>
            hide_disabled: <p>An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.list_identities_input.ListIdentitiesInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.list_identities_response.ListIdentitiesResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.list_identities

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.list_identities.async_list_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.list_identities_input.ListIdentitiesInput = {
            "identity_pool_id": identity_pool_id,
            "max_results": max_results,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if hide_disabled is not None:
            input_["hide_disabled"] = hide_disabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_identity_pools(
        self,
        max_results: "capo_cognito_identity.types.query_limit.QueryLimit",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        next_token: Optional[
            "capo_cognito_identity.types.pagination_key.PaginationKey"
        ] = None,
    ) -> "capo_cognito_identity.types.list_identity_pools_response.ListIdentityPoolsResponse":
        """<p>Lists all of the Cognito identity pools registered for your account.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            max_results: <p>The maximum number of identities to return.</p>
            next_token: <p>A pagination token.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.list_identity_pools_input.ListIdentityPoolsInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.list_identity_pools_response.ListIdentityPoolsResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.list_identity_pools

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.list_identity_pools.async_list_identity_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.list_identity_pools_input.ListIdentityPoolsInput = {
            "max_results": max_results
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

    async def iter_list_identity_pools(
        self,
        max_results: "capo_cognito_identity.types.query_limit.QueryLimit",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        next_token: Optional[
            "capo_cognito_identity.types.pagination_key.PaginationKey"
        ] = None,
    ) -> "AsyncIterator[capo_cognito_identity.types.identity_pool_short_description.IdentityPoolShortDescription]":
        _token = next_token
        while True:
            _response = await self.list_identity_pools(
                max_results,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("identity_pools",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_cognito_identity.types.arn_string.ARNString",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags that are assigned to an Amazon Cognito identity pool.</p> <p>A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.</p> <p>You can use this action up to 10 times per second, per account.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the identity pool that the tags are assigned to.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def lookup_developer_identity(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        identity_id: Optional[
            "capo_cognito_identity.types.identity_id.IdentityId"
        ] = None,
        developer_user_identifier: Optional[
            "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier"
        ] = None,
        max_results: Optional[
            "capo_cognito_identity.types.query_limit.QueryLimit"
        ] = None,
        next_token: Optional[
            "capo_cognito_identity.types.pagination_key.PaginationKey"
        ] = None,
    ) -> "capo_cognito_identity.types.lookup_developer_identity_response.LookupDeveloperIdentityResponse":
        """<p>Retrieves the <code>IdentityID</code> associated with a <code>DeveloperUserIdentifier</code> or the list of <code>DeveloperUserIdentifier</code> values associated with an <code>IdentityId</code> for an existing identity. Either <code>IdentityID</code> or <code>DeveloperUserIdentifier</code> must not be null. If you supply only one of these values, the other value will be searched in the database and returned as a part of the response. If you supply both, <code>DeveloperUserIdentifier</code> will be matched against <code>IdentityID</code>. If the values are verified against the database, the response returns both values and is the same as the request. Otherwise, a <code>ResourceConflictException</code> is thrown.</p> <p> <code>LookupDeveloperIdentity</code> is intended for low-throughput control plane operations: for example, to enable customer service to locate an identity ID by username. If you are using it for higher-volume operations such as user authentication, your requests are likely to be throttled. <a>GetOpenIdTokenForDeveloperIdentity</a> is a better option for higher-volume operations for user authentication.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>
            developer_user_identifier: <p>A unique ID used by your backend authentication process to identify a user. Typically, a developer identity provider would issue many developer user identifiers, in keeping with the number of users.</p>
            max_results: <p>The maximum number of identities to return.</p>
            next_token: <p>A pagination token. The first call you make will have <code>NextToken</code> set to null. After that the service will return <code>NextToken</code> values as needed. For example, let's say you make a request with <code>MaxResults</code> set to 10, and there are 20 matches in the database. The service will return a pagination token as a part of the response. This token can be used to call the API again and get results starting from the 11th match.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.lookup_developer_identity_input.LookupDeveloperIdentityInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.lookup_developer_identity_response.LookupDeveloperIdentityResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.lookup_developer_identity

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.lookup_developer_identity.async_lookup_developer_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.lookup_developer_identity_input.LookupDeveloperIdentityInput = {
            "identity_pool_id": identity_pool_id
        }
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if developer_user_identifier is not None:
            input_["developer_user_identifier"] = developer_user_identifier
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

    async def merge_developer_identities(
        self,
        source_user_identifier: "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier",
        destination_user_identifier: "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier",
        developer_provider_name: "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName",
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.merge_developer_identities_response.MergeDeveloperIdentitiesResponse":
        """<p>Merges two users having different <code>IdentityId</code>s, existing in the same identity pool, and identified by the same developer provider. You can use this action to request that discrete users be merged and identified as a single user in the Cognito environment. Cognito associates the given source user (<code>SourceUserIdentifier</code>) with the <code>IdentityId</code> of the <code>DestinationUserIdentifier</code>. Only developer-authenticated users can be merged. If the users to be merged are associated with the same public provider, but as two different users, an exception will be thrown.</p> <p>The number of linked logins is limited to 20. So, the number of linked logins for the source user, <code>SourceUserIdentifier</code>, and the destination user, <code>DestinationUserIdentifier</code>, together should not be larger than 20. Otherwise, an exception will be thrown.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            source_user_identifier: <p>User identifier for the source user. The value should be a <code>DeveloperUserIdentifier</code>.</p>
            destination_user_identifier: <p>User identifier for the destination user. The value should be a <code>DeveloperUserIdentifier</code>.</p>
            developer_provider_name: <p>The "domain" by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the <code>DeveloperProviderName</code>, you can use letters as well as period (.), underscore (_), and dash (-).</p>
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.merge_developer_identities_input.MergeDeveloperIdentitiesInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.merge_developer_identities_response.MergeDeveloperIdentitiesResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.merge_developer_identities

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.merge_developer_identities.async_merge_developer_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.merge_developer_identities_input.MergeDeveloperIdentitiesInput = {
            "source_user_identifier": source_user_identifier,
            "destination_user_identifier": destination_user_identifier,
            "developer_provider_name": developer_provider_name,
            "identity_pool_id": identity_pool_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_identity_pool_roles(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        roles: "capo_cognito_identity.types.roles_map.RolesMap",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        role_mappings: Optional[
            "capo_cognito_identity.types.role_mapping_map.RoleMappingMap"
        ] = None,
    ) -> None:
        """<p>Sets the roles for an identity pool. These roles are used when making calls to <a>GetCredentialsForIdentity</a> action.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            roles: <p>The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.</p>
            role_mappings: <p>How users for a specific identity provider are to mapped to roles. This is a string to <a>RoleMapping</a> object map. The string identifies the identity provider, for example, <code>graph.facebook.com</code> or <code>cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id</code>.</p> <p>Up to 25 rules can be specified per identity provider.</p>

        Raises:
            capo_cognito_identity.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Thrown if there are parallel requests to modify a resource.</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.set_identity_pool_roles_input.SetIdentityPoolRolesInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.set_identity_pool_roles

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.set_identity_pool_roles.async_set_identity_pool_roles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.set_identity_pool_roles_input.SetIdentityPoolRolesInput = {
            "identity_pool_id": identity_pool_id,
            "roles": roles,
        }
        if role_mappings is not None:
            input_["role_mappings"] = role_mappings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_principal_tag_attribute_map(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        identity_provider_name: "capo_cognito_identity.types.identity_provider_name.IdentityProviderName",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        use_defaults: Optional[
            "capo_cognito_identity.types.use_defaults.UseDefaults"
        ] = None,
        principal_tags: Optional[
            "capo_cognito_identity.types.principal_tags.PrincipalTags"
        ] = None,
    ) -> "capo_cognito_identity.types.set_principal_tag_attribute_map_response.SetPrincipalTagAttributeMapResponse":
        """<p>You can use this operation to use default (username and clientID) attribute or custom attribute mappings.</p>

        Args:
            identity_pool_id: <p>The ID of the Identity Pool you want to set attribute mappings for.</p>
            identity_provider_name: <p>The provider name you want to use for attribute mappings.</p>
            use_defaults: <p>You can use this operation to use default (username and clientID) attribute mappings.</p>
            principal_tags: <p>You can use this operation to add principal tags.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.set_principal_tag_attribute_map_input.SetPrincipalTagAttributeMapInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.set_principal_tag_attribute_map_response.SetPrincipalTagAttributeMapResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.set_principal_tag_attribute_map

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.set_principal_tag_attribute_map.async_set_principal_tag_attribute_map(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.set_principal_tag_attribute_map_input.SetPrincipalTagAttributeMapInput = {
            "identity_pool_id": identity_pool_id,
            "identity_provider_name": identity_provider_name,
        }
        if use_defaults is not None:
            input_["use_defaults"] = use_defaults
        if principal_tags is not None:
            input_["principal_tags"] = principal_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_cognito_identity.types.arn_string.ARNString",
        tags: "capo_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns a set of tags to the specified Amazon Cognito identity pool. A tag is a label that you can use to categorize and manage identity pools in different ways, such as by purpose, owner, environment, or other criteria.</p> <p>Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of an identity pool, one for testing and another for production, you might assign an <code>Environment</code> tag key to both identity pools. The value of this key might be <code>Test</code> for one identity pool and <code>Production</code> for the other.</p> <p>Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your identity pools. In an IAM policy, you can constrain permissions for identity pools based on specific tags or tag values.</p> <p>You can use this action up to 5 times per second, per account. An identity pool can have as many as 50 tags.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the identity pool.</p>
            tags: <p>The tags to assign to the identity pool.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unlink_developer_identity(
        self,
        identity_id: "capo_cognito_identity.types.identity_id.IdentityId",
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        developer_provider_name: "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName",
        developer_user_identifier: "capo_cognito_identity.types.developer_user_identifier.DeveloperUserIdentifier",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> None:
        """<p>Unlinks a <code>DeveloperUserIdentifier</code> from an existing identity. Unlinked developer users will be considered new identities next time they are seen. If, for a given Cognito identity, you remove all federated identities as well as the developer user identifier, the Cognito identity becomes inaccessible.</p> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            developer_provider_name: <p>The "domain" by which Cognito will refer to your users.</p>
            developer_user_identifier: <p>A unique ID used by your backend authentication process to identify a user.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.unlink_developer_identity_input.UnlinkDeveloperIdentityInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.unlink_developer_identity

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.unlink_developer_identity.async_unlink_developer_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.unlink_developer_identity_input.UnlinkDeveloperIdentityInput = {
            "identity_id": identity_id,
            "identity_pool_id": identity_pool_id,
            "developer_provider_name": developer_provider_name,
            "developer_user_identifier": developer_user_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unlink_identity(
        self,
        identity_id: "capo_cognito_identity.types.identity_id.IdentityId",
        logins: "capo_cognito_identity.types.logins_map.LoginsMap",
        logins_to_remove: "capo_cognito_identity.types.logins_list.LoginsList",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> None:
        """<p>Unlinks a federated identity from an existing account. Unlinked logins will be considered new identities next time they are seen. Removing the last linked login will make this identity inaccessible.</p> <p>This is a public API. You do not need any credentials to call this API.</p>

        Args:
            identity_id: <p>A unique identifier in the format REGION:GUID.</p>
            logins: <p>A set of optional name-value pairs that map provider names to provider tokens.</p>
            logins_to_remove: <p>Provider names to unlink from this identity.</p>

        Raises:
            capo_cognito_identity.errors.external_service_exception.ExternalServiceException: <p>An exception thrown when a dependent service such as Facebook or Twitter is not responding</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.unlink_identity_input.UnlinkIdentityInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.unlink_identity

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.unlink_identity.async_unlink_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.unlink_identity_input.UnlinkIdentityInput = {
            "identity_id": identity_id,
            "logins": logins,
            "logins_to_remove": logins_to_remove,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_cognito_identity.types.arn_string.ARNString",
        tag_keys: "capo_cognito_identity.types.identity_pool_tags_list_type.IdentityPoolTagsListType",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
    ) -> "capo_cognito_identity.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified Amazon Cognito identity pool. You can use this action up to 5 times per second, per account</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the identity pool.</p>
            tag_keys: <p>The keys of the tags to remove from the user pool.</p>

        Raises:
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_identity_pool(
        self,
        identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId",
        identity_pool_name: "capo_cognito_identity.types.identity_pool_name.IdentityPoolName",
        allow_unauthenticated_identities: "capo_cognito_identity.types.identity_pool_unauthenticated.IdentityPoolUnauthenticated",
        *,
        config_overrides: Optional[AsyncCognitoIdentityClientConfig] = None,
        allow_classic_flow: Optional[
            "capo_cognito_identity.types.classic_flow.ClassicFlow"
        ] = None,
        supported_login_providers: Optional[
            "capo_cognito_identity.types.identity_providers.IdentityProviders"
        ] = None,
        developer_provider_name: Optional[
            "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName"
        ] = None,
        open_id_connect_provider_ar_ns: Optional[
            "capo_cognito_identity.types.oidc_provider_list.OIDCProviderList"
        ] = None,
        cognito_identity_providers: Optional[
            "capo_cognito_identity.types.cognito_identity_provider_list.CognitoIdentityProviderList"
        ] = None,
        saml_provider_ar_ns: Optional[
            "capo_cognito_identity.types.saml_provider_list.SAMLProviderList"
        ] = None,
        identity_pool_tags: Optional[
            "capo_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType"
        ] = None,
    ) -> "capo_cognito_identity.types.identity_pool.IdentityPool":
        """<p>Updates the configuration of an identity pool.</p> <important> <p>If you don't provide a value for a parameter, Amazon Cognito sets it to its default value. </p> </important> <p>You must use Amazon Web Services developer credentials to call this operation.</p>

        Args:
            identity_pool_id: <p>An identity pool ID in the format REGION:GUID.</p>
            identity_pool_name: <p>A string that you provide.</p>
            allow_unauthenticated_identities: <p>TRUE if the identity pool supports unauthenticated logins.</p>
            allow_classic_flow: <p>Enables or disables the Basic (Classic) authentication flow. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html">Identity Pools (Federated Identities) Authentication Flow</a> in the <i>Amazon Cognito Developer Guide</i>.</p>
            supported_login_providers: <p>Optional key:value pairs mapping provider names to provider app IDs.</p>
            developer_provider_name: <p>The "domain" by which Cognito will refer to your users.</p>
            open_id_connect_provider_ar_ns: <p>The ARNs of the OpenID Connect providers.</p>
            cognito_identity_providers: <p>A list representing an Amazon Cognito user pool and its client ID.</p>
            saml_provider_ar_ns: <p>An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.</p>
            identity_pool_tags: <p>The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.</p>

        Raises:
            capo_cognito_identity.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Thrown if there are parallel requests to modify a resource.</p>
            capo_cognito_identity.errors.internal_error_exception.InternalErrorException: <p>Thrown when the service encounters an error during processing the request.</p>
            capo_cognito_identity.errors.invalid_parameter_exception.InvalidParameterException: <p>Thrown for missing or bad input parameter(s).</p>
            capo_cognito_identity.errors.limit_exceeded_exception.LimitExceededException: <p>Thrown when the total number of user pools has exceeded a preset limit.</p>
            capo_cognito_identity.errors.not_authorized_exception.NotAuthorizedException: <p>Thrown when a user is not authorized to access the requested resource.</p>
            capo_cognito_identity.errors.resource_conflict_exception.ResourceConflictException: <p>Thrown when a user tries to use a login which is already linked to another account.</p>
            capo_cognito_identity.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when the requested resource (for example, a dataset or record) does not exist.</p>
            capo_cognito_identity.errors.too_many_requests_exception.TooManyRequestsException: <p>Thrown when a request is throttled.</p>
            capo_cognito_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cognito_identity.types.identity_pool.IdentityPool]",
        ) -> AsyncOperationResponse[
            "capo_cognito_identity.types.identity_pool.IdentityPool"
        ]:
            import capo_cognito_identity._operations.aws_cognito_identity_service.update_identity_pool

            (
                output,
                http_response,
            ) = await capo_cognito_identity._operations.aws_cognito_identity_service.update_identity_pool.async_update_identity_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cognito_identity.types.identity_pool.IdentityPool = {
            "identity_pool_id": identity_pool_id,
            "identity_pool_name": identity_pool_name,
            "allow_unauthenticated_identities": allow_unauthenticated_identities,
        }
        if allow_classic_flow is not None:
            input_["allow_classic_flow"] = allow_classic_flow
        if supported_login_providers is not None:
            input_["supported_login_providers"] = supported_login_providers
        if developer_provider_name is not None:
            input_["developer_provider_name"] = developer_provider_name
        if open_id_connect_provider_ar_ns is not None:
            input_["open_id_connect_provider_ar_ns"] = open_id_connect_provider_ar_ns
        if cognito_identity_providers is not None:
            input_["cognito_identity_providers"] = cognito_identity_providers
        if saml_provider_ar_ns is not None:
            input_["saml_provider_ar_ns"] = saml_provider_ar_ns
        if identity_pool_tags is not None:
            input_["identity_pool_tags"] = identity_pool_tags

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
