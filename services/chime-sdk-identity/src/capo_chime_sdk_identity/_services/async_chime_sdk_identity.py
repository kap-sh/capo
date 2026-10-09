"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ChimeIdentityService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_chime_sdk_identity._auth._signers
import capo_chime_sdk_identity._auth._sigv4
from capo_chime_sdk_identity._auth._identity import Credentials
from capo_chime_sdk_identity._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_chime_sdk_identity._auth._zapros_handler import AuthMiddleware
from capo_chime_sdk_identity._pagination import resolve_path as _resolve_path
from capo_chime_sdk_identity._services._aws_config import aaws_config
from capo_chime_sdk_identity._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.allow_messages
    import capo_chime_sdk_identity.types.app_instance_retention_settings
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_type
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.client_request_token
    import capo_chime_sdk_identity.types.configuration
    import capo_chime_sdk_identity.types.create_app_instance_admin_request
    import capo_chime_sdk_identity.types.create_app_instance_admin_response
    import capo_chime_sdk_identity.types.create_app_instance_bot_request
    import capo_chime_sdk_identity.types.create_app_instance_bot_response
    import capo_chime_sdk_identity.types.create_app_instance_request
    import capo_chime_sdk_identity.types.create_app_instance_response
    import capo_chime_sdk_identity.types.create_app_instance_user_request
    import capo_chime_sdk_identity.types.create_app_instance_user_response
    import capo_chime_sdk_identity.types.delete_app_instance_admin_request
    import capo_chime_sdk_identity.types.delete_app_instance_bot_request
    import capo_chime_sdk_identity.types.delete_app_instance_request
    import capo_chime_sdk_identity.types.delete_app_instance_user_request
    import capo_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request
    import capo_chime_sdk_identity.types.describe_app_instance_admin_request
    import capo_chime_sdk_identity.types.describe_app_instance_admin_response
    import capo_chime_sdk_identity.types.describe_app_instance_bot_request
    import capo_chime_sdk_identity.types.describe_app_instance_bot_response
    import capo_chime_sdk_identity.types.describe_app_instance_request
    import capo_chime_sdk_identity.types.describe_app_instance_response
    import capo_chime_sdk_identity.types.describe_app_instance_user_endpoint_request
    import capo_chime_sdk_identity.types.describe_app_instance_user_endpoint_response
    import capo_chime_sdk_identity.types.describe_app_instance_user_request
    import capo_chime_sdk_identity.types.describe_app_instance_user_response
    import capo_chime_sdk_identity.types.endpoint_attributes
    import capo_chime_sdk_identity.types.expiration_settings
    import capo_chime_sdk_identity.types.get_app_instance_retention_settings_request
    import capo_chime_sdk_identity.types.get_app_instance_retention_settings_response
    import capo_chime_sdk_identity.types.list_app_instance_admins_request
    import capo_chime_sdk_identity.types.list_app_instance_admins_response
    import capo_chime_sdk_identity.types.list_app_instance_bots_request
    import capo_chime_sdk_identity.types.list_app_instance_bots_response
    import capo_chime_sdk_identity.types.list_app_instance_user_endpoints_request
    import capo_chime_sdk_identity.types.list_app_instance_user_endpoints_response
    import capo_chime_sdk_identity.types.list_app_instance_users_request
    import capo_chime_sdk_identity.types.list_app_instance_users_response
    import capo_chime_sdk_identity.types.list_app_instances_request
    import capo_chime_sdk_identity.types.list_app_instances_response
    import capo_chime_sdk_identity.types.list_tags_for_resource_request
    import capo_chime_sdk_identity.types.list_tags_for_resource_response
    import capo_chime_sdk_identity.types.max_results
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.next_token
    import capo_chime_sdk_identity.types.non_empty_resource_name
    import capo_chime_sdk_identity.types.put_app_instance_retention_settings_request
    import capo_chime_sdk_identity.types.put_app_instance_retention_settings_response
    import capo_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request
    import capo_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response
    import capo_chime_sdk_identity.types.register_app_instance_user_endpoint_request
    import capo_chime_sdk_identity.types.register_app_instance_user_endpoint_response
    import capo_chime_sdk_identity.types.resource_name
    import capo_chime_sdk_identity.types.sensitive_chime_arn
    import capo_chime_sdk_identity.types.sensitive_string1600
    import capo_chime_sdk_identity.types.string64
    import capo_chime_sdk_identity.types.string1600
    import capo_chime_sdk_identity.types.tag_key_list
    import capo_chime_sdk_identity.types.tag_list
    import capo_chime_sdk_identity.types.tag_resource_request
    import capo_chime_sdk_identity.types.untag_resource_request
    import capo_chime_sdk_identity.types.update_app_instance_bot_request
    import capo_chime_sdk_identity.types.update_app_instance_bot_response
    import capo_chime_sdk_identity.types.update_app_instance_request
    import capo_chime_sdk_identity.types.update_app_instance_response
    import capo_chime_sdk_identity.types.update_app_instance_user_endpoint_request
    import capo_chime_sdk_identity.types.update_app_instance_user_endpoint_response
    import capo_chime_sdk_identity.types.update_app_instance_user_request
    import capo_chime_sdk_identity.types.update_app_instance_user_response
    import capo_chime_sdk_identity.types.user_id
    import capo_chime_sdk_identity.types.user_name


class AsyncChimeSDKIdentityClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncChimeSDKIdentityClient:
    """A client for the ``ChimeSDKIdentity`` service.

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
        self._config = AsyncChimeSDKIdentityClientConfig(
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
        self, config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncChimeSDKIdentityClientConfig = config_overrides or {}
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

    async def create_app_instance(
        self,
        name: "capo_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        metadata: Optional["capo_chime_sdk_identity.types.metadata.Metadata"] = None,
        tags: Optional["capo_chime_sdk_identity.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_identity.types.create_app_instance_response.CreateAppInstanceResponse":
        """<p>Creates an Amazon Chime SDK messaging <code>AppInstance</code> under an AWS account. Only SDK messaging customers use this API. <code>CreateAppInstance</code> supports idempotency behavior as described in the AWS API Standard.</p> <p>identity</p>

        Args:
            name: <p>The name of the <code>AppInstance</code>.</p>
            metadata: <p>The metadata of the <code>AppInstance</code>. Limited to a 1KB string in UTF-8.</p>
            client_request_token: <p>The unique ID of the request. Use different tokens to create different <code>AppInstances</code>.</p>
            tags: <p>Tags assigned to the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.create_app_instance_request.CreateAppInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.create_app_instance_response.CreateAppInstanceResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance.async_create_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.create_app_instance_request.CreateAppInstanceRequest = {
            "name": name,
            "client_request_token": client_request_token,
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_app_instance_admin(
        self,
        app_instance_admin_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.create_app_instance_admin_response.CreateAppInstanceAdminResponse":
        """<p>Promotes an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> to an <code>AppInstanceAdmin</code>. The promoted entity can perform the following actions. </p> <ul> <li> <p> <code>ChannelModerator</code> actions across all channels in the <code>AppInstance</code>.</p> </li> <li> <p> <code>DeleteChannelMessage</code> actions.</p> </li> </ul> <p>Only an <code>AppInstanceUser</code> and <code>AppInstanceBot</code> can be promoted to an <code>AppInstanceAdmin</code> role.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the administrator of the current <code>AppInstance</code>.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.create_app_instance_admin_request.CreateAppInstanceAdminRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.create_app_instance_admin_response.CreateAppInstanceAdminResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance_admin

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance_admin.async_create_app_instance_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.create_app_instance_admin_request.CreateAppInstanceAdminRequest = {
            "app_instance_admin_arn": app_instance_admin_arn,
            "app_instance_arn": app_instance_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_app_instance_bot(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        client_request_token: "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        configuration: "capo_chime_sdk_identity.types.configuration.Configuration",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_identity.types.resource_name.ResourceName"
        ] = None,
        metadata: Optional["capo_chime_sdk_identity.types.metadata.Metadata"] = None,
        tags: Optional["capo_chime_sdk_identity.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_identity.types.create_app_instance_bot_response.CreateAppInstanceBotResponse":
        """<p>Creates a bot under an Amazon Chime <code>AppInstance</code>. The request consists of a unique <code>Configuration</code> and <code>Name</code> for that bot.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code> request.</p>
            name: <p>The user's name.</p>
            metadata: <p>The request metadata. Limited to a 1KB string in UTF-8.</p>
            client_request_token: <p>The unique ID for the client making the request. Use different tokens for different <code>AppInstanceBots</code>.</p>
            tags: <p>The tags assigned to the <code>AppInstanceBot</code>.</p>
            configuration: <p>Configuration information about the Amazon Lex V2 V2 bot.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.create_app_instance_bot_request.CreateAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.create_app_instance_bot_response.CreateAppInstanceBotResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance_bot

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance_bot.async_create_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.create_app_instance_bot_request.CreateAppInstanceBotRequest = {
            "app_instance_arn": app_instance_arn,
            "client_request_token": client_request_token,
            "configuration": configuration,
        }
        if name is not None:
            input_["name"] = name
        if metadata is not None:
            input_["metadata"] = metadata
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_app_instance_user(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_user_id: "capo_chime_sdk_identity.types.user_id.UserId",
        name: "capo_chime_sdk_identity.types.user_name.UserName",
        client_request_token: "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        metadata: Optional["capo_chime_sdk_identity.types.metadata.Metadata"] = None,
        tags: Optional["capo_chime_sdk_identity.types.tag_list.TagList"] = None,
        expiration_settings: Optional[
            "capo_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.create_app_instance_user_response.CreateAppInstanceUserResponse":
        """<p>Creates a user under an Amazon Chime <code>AppInstance</code>. The request consists of a unique <code>appInstanceUserId</code> and <code>Name</code> for that user.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code> request.</p>
            app_instance_user_id: <p>The user ID of the <code>AppInstance</code>.</p>
            name: <p>The user's name.</p>
            metadata: <p>The request's metadata. Limited to a 1KB string in UTF-8.</p>
            client_request_token: <p>The unique ID of the request. Use different tokens to request additional <code>AppInstances</code>.</p>
            tags: <p>Tags assigned to the <code>AppInstanceUser</code>.</p>
            expiration_settings: <p>Settings that control the interval after which the <code>AppInstanceUser</code> is automatically deleted.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.create_app_instance_user_request.CreateAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.create_app_instance_user_response.CreateAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance_user

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.create_app_instance_user.async_create_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.create_app_instance_user_request.CreateAppInstanceUserRequest = {
            "app_instance_arn": app_instance_arn,
            "app_instance_user_id": app_instance_user_id,
            "name": name,
            "client_request_token": client_request_token,
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if tags is not None:
            input_["tags"] = tags
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_app_instance(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstance</code> and all associated data asynchronously.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.delete_app_instance_request.DeleteAppInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance.async_delete_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.delete_app_instance_request.DeleteAppInstanceRequest = {
            "app_instance_arn": app_instance_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_app_instance_admin(
        self,
        app_instance_admin_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Demotes an <code>AppInstanceAdmin</code> to an <code>AppInstanceUser</code> or <code>AppInstanceBot</code>. This action does not delete the user.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the <code>AppInstance</code>'s administrator.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.delete_app_instance_admin_request.DeleteAppInstanceAdminRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_admin

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_admin.async_delete_app_instance_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.delete_app_instance_admin_request.DeleteAppInstanceAdminRequest = {
            "app_instance_admin_arn": app_instance_admin_arn,
            "app_instance_arn": app_instance_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_app_instance_bot(
        self,
        app_instance_bot_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstanceBot</code>.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code> being deleted.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.delete_app_instance_bot_request.DeleteAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_bot

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_bot.async_delete_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.delete_app_instance_bot_request.DeleteAppInstanceBotRequest = {
            "app_instance_bot_arn": app_instance_bot_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_app_instance_user(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the user request being deleted.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.delete_app_instance_user_request.DeleteAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_user

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_user.async_delete_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.delete_app_instance_user_request.DeleteAppInstanceUserRequest = {
            "app_instance_user_arn": app_instance_user_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_id: "capo_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deregisters an <code>AppInstanceUserEndpoint</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request.DeregisterAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.deregister_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.deregister_app_instance_user_endpoint.async_deregister_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request.DeregisterAppInstanceUserEndpointRequest = {
            "app_instance_user_arn": app_instance_user_arn,
            "endpoint_id": endpoint_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_app_instance(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.describe_app_instance_response.DescribeAppInstanceResponse":
        """<p>Returns the full details of an <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.describe_app_instance_request.DescribeAppInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.describe_app_instance_response.DescribeAppInstanceResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance.async_describe_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.describe_app_instance_request.DescribeAppInstanceRequest = {
            "app_instance_arn": app_instance_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_app_instance_admin(
        self,
        app_instance_admin_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.describe_app_instance_admin_response.DescribeAppInstanceAdminResponse":
        """<p>Returns the full details of an <code>AppInstanceAdmin</code>.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the <code>AppInstanceAdmin</code>.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.describe_app_instance_admin_request.DescribeAppInstanceAdminRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.describe_app_instance_admin_response.DescribeAppInstanceAdminResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_admin

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_admin.async_describe_app_instance_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.describe_app_instance_admin_request.DescribeAppInstanceAdminRequest = {
            "app_instance_admin_arn": app_instance_admin_arn,
            "app_instance_arn": app_instance_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_app_instance_bot(
        self,
        app_instance_bot_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.describe_app_instance_bot_response.DescribeAppInstanceBotResponse":
        """<p>The <code>AppInstanceBot's</code> information.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.describe_app_instance_bot_request.DescribeAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.describe_app_instance_bot_response.DescribeAppInstanceBotResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_bot

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_bot.async_describe_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.describe_app_instance_bot_request.DescribeAppInstanceBotRequest = {
            "app_instance_bot_arn": app_instance_bot_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_app_instance_user(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.describe_app_instance_user_response.DescribeAppInstanceUserResponse":
        """<p>Returns the full details of an <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.describe_app_instance_user_request.DescribeAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.describe_app_instance_user_response.DescribeAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user.async_describe_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.describe_app_instance_user_request.DescribeAppInstanceUserRequest = {
            "app_instance_user_arn": app_instance_user_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.string1600.String1600",
        endpoint_id: "capo_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.describe_app_instance_user_endpoint_response.DescribeAppInstanceUserEndpointResponse":
        """<p>Returns the full details of an <code>AppInstanceUserEndpoint</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.describe_app_instance_user_endpoint_request.DescribeAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.describe_app_instance_user_endpoint_response.DescribeAppInstanceUserEndpointResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user_endpoint.async_describe_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.describe_app_instance_user_endpoint_request.DescribeAppInstanceUserEndpointRequest = {
            "app_instance_user_arn": app_instance_user_arn,
            "endpoint_id": endpoint_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_app_instance_retention_settings(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.get_app_instance_retention_settings_response.GetAppInstanceRetentionSettingsResponse":
        """<p>Gets the retention settings for an <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.get_app_instance_retention_settings_request.GetAppInstanceRetentionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.get_app_instance_retention_settings_response.GetAppInstanceRetentionSettingsResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.get_app_instance_retention_settings

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.get_app_instance_retention_settings.async_get_app_instance_retention_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.get_app_instance_retention_settings_request.GetAppInstanceRetentionSettingsRequest = {
            "app_instance_arn": app_instance_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_app_instance_admins(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.list_app_instance_admins_response.ListAppInstanceAdminsResponse":
        """<p>Returns a list of the administrators in the <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            max_results: <p>The maximum number of administrators that you want to return.</p>
            next_token: <p>The token returned from previous API requests until the number of administrators is reached.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.list_app_instance_admins_request.ListAppInstanceAdminsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.list_app_instance_admins_response.ListAppInstanceAdminsResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_admins

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_admins.async_list_app_instance_admins(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.list_app_instance_admins_request.ListAppInstanceAdminsRequest = {
            "app_instance_arn": app_instance_arn
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

    async def iter_list_app_instance_admins(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_identity.types.list_app_instance_admins_response.ListAppInstanceAdminsResponse]":
        _token = next_token
        while True:
            _response = await self.list_app_instance_admins(
                app_instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_app_instance_bots(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.list_app_instance_bots_response.ListAppInstanceBotsResponse":
        """<p>Lists all <code>AppInstanceBots</code> created under a single <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            max_results: <p>The maximum number of requests to return.</p>
            next_token: <p>The token passed by previous API calls until all requested bots are returned.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.list_app_instance_bots_request.ListAppInstanceBotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.list_app_instance_bots_response.ListAppInstanceBotsResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_bots

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_bots.async_list_app_instance_bots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.list_app_instance_bots_request.ListAppInstanceBotsRequest = {
            "app_instance_arn": app_instance_arn
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

    async def iter_list_app_instance_bots(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_identity.types.list_app_instance_bots_response.ListAppInstanceBotsResponse]":
        _token = next_token
        while True:
            _response = await self.list_app_instance_bots(
                app_instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_app_instances(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.list_app_instances_response.ListAppInstancesResponse":
        """<p>Lists all Amazon Chime <code>AppInstance</code>s created under a single AWS account.</p>

        Args:
            max_results: <p>The maximum number of <code>AppInstance</code>s that you want to return.</p>
            next_token: <p>The token passed by previous API requests until you reach the maximum number of <code>AppInstances</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.list_app_instances_request.ListAppInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.list_app_instances_response.ListAppInstancesResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.list_app_instances

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.list_app_instances.async_list_app_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.list_app_instances_request.ListAppInstancesRequest = {}
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

    async def iter_list_app_instances(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_identity.types.list_app_instances_response.ListAppInstancesResponse]":
        _token = next_token
        while True:
            _response = await self.list_app_instances(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_app_instance_user_endpoints(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.list_app_instance_user_endpoints_response.ListAppInstanceUserEndpointsResponse":
        """<p>Lists all the <code>AppInstanceUserEndpoints</code> created under a single <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            max_results: <p>The maximum number of endpoints that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested endpoints are returned.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.list_app_instance_user_endpoints_request.ListAppInstanceUserEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.list_app_instance_user_endpoints_response.ListAppInstanceUserEndpointsResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_user_endpoints

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_user_endpoints.async_list_app_instance_user_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.list_app_instance_user_endpoints_request.ListAppInstanceUserEndpointsRequest = {
            "app_instance_user_arn": app_instance_user_arn
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

    async def iter_list_app_instance_user_endpoints(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_identity.types.list_app_instance_user_endpoints_response.ListAppInstanceUserEndpointsResponse]":
        _token = next_token
        while True:
            _response = await self.list_app_instance_user_endpoints(
                app_instance_user_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_app_instance_users(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.list_app_instance_users_response.ListAppInstanceUsersResponse":
        """<p>List all <code>AppInstanceUsers</code> created under a single <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            max_results: <p>The maximum number of requests that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested users are returned.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.list_app_instance_users_request.ListAppInstanceUsersRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.list_app_instance_users_response.ListAppInstanceUsersResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_users

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.list_app_instance_users.async_list_app_instance_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.list_app_instance_users_request.ListAppInstanceUsersRequest = {
            "app_instance_arn": app_instance_arn
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

    async def iter_list_app_instance_users(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_chime_sdk_identity.types.list_app_instance_users_response.ListAppInstanceUsersResponse]":
        _token = next_token
        while True:
            _response = await self.list_app_instance_users(
                app_instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags applied to an Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_app_instance_retention_settings(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_retention_settings: "capo_chime_sdk_identity.types.app_instance_retention_settings.AppInstanceRetentionSettings",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.put_app_instance_retention_settings_response.PutAppInstanceRetentionSettingsResponse":
        """<p>Sets the amount of time in days that a given <code>AppInstance</code> retains data.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            app_instance_retention_settings: <p>The time in days to retain data. Data type: number.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.put_app_instance_retention_settings_request.PutAppInstanceRetentionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.put_app_instance_retention_settings_response.PutAppInstanceRetentionSettingsResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.put_app_instance_retention_settings

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.put_app_instance_retention_settings.async_put_app_instance_retention_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.put_app_instance_retention_settings_request.PutAppInstanceRetentionSettingsRequest = {
            "app_instance_arn": app_instance_arn,
            "app_instance_retention_settings": app_instance_retention_settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_app_instance_user_expiration_settings(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        expiration_settings: Optional[
            "capo_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response.PutAppInstanceUserExpirationSettingsResponse":
        """<p>Sets the number of days before the <code>AppInstanceUser</code> is automatically deleted.</p> <note> <p>A background process deletes expired <code>AppInstanceUsers</code> within 6 hours of expiration. Actual deletion times may vary.</p> <p>Expired <code>AppInstanceUsers</code> that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            expiration_settings: <p>Settings that control the interval after which an <code>AppInstanceUser</code> is automatically deleted.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request.PutAppInstanceUserExpirationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response.PutAppInstanceUserExpirationSettingsResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.put_app_instance_user_expiration_settings

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.put_app_instance_user_expiration_settings.async_put_app_instance_user_expiration_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request.PutAppInstanceUserExpirationSettingsRequest = {
            "app_instance_user_arn": app_instance_user_arn
        }
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        type: "capo_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType",
        resource_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_attributes: "capo_chime_sdk_identity.types.endpoint_attributes.EndpointAttributes",
        client_request_token: "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
        ] = None,
        allow_messages: Optional[
            "capo_chime_sdk_identity.types.allow_messages.AllowMessages"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.register_app_instance_user_endpoint_response.RegisterAppInstanceUserEndpointResponse":
        """<p>Registers an endpoint under an Amazon Chime <code>AppInstanceUser</code>. The endpoint receives messages for a user. For push notifications, the endpoint is a mobile device used to receive mobile push notifications for a user.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            name: <p>The name of the <code>AppInstanceUserEndpoint</code>.</p>
            type: <p>The type of the <code>AppInstanceUserEndpoint</code>. Supported types:</p> <ul> <li> <p> <code>APNS</code>: The mobile notification service for an Apple device.</p> </li> <li> <p> <code>APNS_SANDBOX</code>: The sandbox environment of the mobile notification service for an Apple device.</p> </li> <li> <p> <code>GCM</code>: The mobile notification service for an Android device.</p> </li> </ul> <p>Populate the <code>ResourceArn</code> value of each type as <code>PinpointAppArn</code>.</p>
            resource_arn: <p>The ARN of the resource to which the endpoint belongs.</p>
            endpoint_attributes: <p>The attributes of an <code>Endpoint</code>.</p>
            client_request_token: <p>The unique ID assigned to the request. Use different tokens to register other endpoints.</p>
            allow_messages: <p>Boolean that controls whether the AppInstanceUserEndpoint is opted in to receive messages. <code>ALL</code> indicates the endpoint receives all messages. <code>NONE</code> indicates the endpoint receives no messages.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.register_app_instance_user_endpoint_request.RegisterAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.register_app_instance_user_endpoint_response.RegisterAppInstanceUserEndpointResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.register_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.register_app_instance_user_endpoint.async_register_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.register_app_instance_user_endpoint_request.RegisterAppInstanceUserEndpointRequest = {
            "app_instance_user_arn": app_instance_user_arn,
            "type": type,
            "resource_arn": resource_arn,
            "endpoint_attributes": endpoint_attributes,
            "client_request_token": client_request_token,
        }
        if name is not None:
            input_["name"] = name
        if allow_messages is not None:
            input_["allow_messages"] = allow_messages

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        tags: "capo_chime_sdk_identity.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Applies the specified tags to the specified Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tag key-value pairs.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.tag_resource_request.TagResourceRequest = {
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

    async def untag_resource(
        self,
        resource_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        tag_keys: "capo_chime_sdk_identity.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_chime_sdk_identity._operations.chime_identity_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_app_instance(
        self,
        app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "capo_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName",
        metadata: "capo_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.update_app_instance_response.UpdateAppInstanceResponse":
        """<p>Updates <code>AppInstance</code> metadata.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            name: <p>The name that you want to change.</p>
            metadata: <p>The metadata that you want to change.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.update_app_instance_request.UpdateAppInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.update_app_instance_response.UpdateAppInstanceResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance.async_update_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.update_app_instance_request.UpdateAppInstanceRequest = {
            "app_instance_arn": app_instance_arn,
            "name": name,
            "metadata": metadata,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_app_instance_bot(
        self,
        app_instance_bot_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "capo_chime_sdk_identity.types.resource_name.ResourceName",
        metadata: "capo_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        configuration: Optional[
            "capo_chime_sdk_identity.types.configuration.Configuration"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.update_app_instance_bot_response.UpdateAppInstanceBotResponse":
        """<p>Updates the name and metadata of an <code>AppInstanceBot</code>.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code>.</p>
            name: <p>The name of the <code>AppInstanceBot</code>.</p>
            metadata: <p>The metadata of the <code>AppInstanceBot</code>.</p>
            configuration: <p>The configuration for the bot update.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.update_app_instance_bot_request.UpdateAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.update_app_instance_bot_response.UpdateAppInstanceBotResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance_bot

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance_bot.async_update_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.update_app_instance_bot_request.UpdateAppInstanceBotRequest = {
            "app_instance_bot_arn": app_instance_bot_arn,
            "name": name,
            "metadata": metadata,
        }
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_app_instance_user(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "capo_chime_sdk_identity.types.user_name.UserName",
        metadata: "capo_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "capo_chime_sdk_identity.types.update_app_instance_user_response.UpdateAppInstanceUserResponse":
        """<p>Updates the details of an <code>AppInstanceUser</code>. You can update names and metadata.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            name: <p>The name of the <code>AppInstanceUser</code>.</p>
            metadata: <p>The metadata of the <code>AppInstanceUser</code>.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.update_app_instance_user_request.UpdateAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.update_app_instance_user_response.UpdateAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user.async_update_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.update_app_instance_user_request.UpdateAppInstanceUserRequest = {
            "app_instance_user_arn": app_instance_user_arn,
            "name": name,
            "metadata": metadata,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_id: "capo_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
        ] = None,
        allow_messages: Optional[
            "capo_chime_sdk_identity.types.allow_messages.AllowMessages"
        ] = None,
    ) -> "capo_chime_sdk_identity.types.update_app_instance_user_endpoint_response.UpdateAppInstanceUserEndpointResponse":
        """<p>Updates the details of an <code>AppInstanceUserEndpoint</code>. You can update the name and <code>AllowMessage</code> values.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>
            name: <p>The name of the <code>AppInstanceUserEndpoint</code>.</p>
            allow_messages: <p>Boolean that controls whether the <code>AppInstanceUserEndpoint</code> is opted in to receive messages. <code>ALL</code> indicates the endpoint will receive all messages. <code>NONE</code> indicates the endpoint will receive no messages.</p>

        Raises:
            capo_chime_sdk_identity.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_identity.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_identity.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_identity.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_identity.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_identity.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_identity.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_identity.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_chime_sdk_identity.types.update_app_instance_user_endpoint_request.UpdateAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_chime_sdk_identity.types.update_app_instance_user_endpoint_response.UpdateAppInstanceUserEndpointResponse"
        ]:
            import capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await capo_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user_endpoint.async_update_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_identity.types.update_app_instance_user_endpoint_request.UpdateAppInstanceUserEndpointRequest = {
            "app_instance_user_arn": app_instance_user_arn,
            "endpoint_id": endpoint_id,
        }
        if name is not None:
            input_["name"] = name
        if allow_messages is not None:
            input_["allow_messages"] = allow_messages

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
