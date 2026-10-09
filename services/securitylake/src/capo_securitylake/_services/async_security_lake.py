"""Generated from Smithy shape ``com.amazonaws.securitylake#SecurityLake``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_securitylake._auth._signers
import capo_securitylake._auth._sigv4
from capo_securitylake._auth._identity import Credentials
from capo_securitylake._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_securitylake._auth._zapros_handler import AuthMiddleware
from capo_securitylake._pagination import resolve_path as _resolve_path
from capo_securitylake._resources.security_lake.data_lake import AsyncDataLake
from capo_securitylake._resources.security_lake.subscriber import AsyncSubscriber
from capo_securitylake._services._aws_config import aaws_config
from capo_securitylake._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_securitylake.types.access_type_list
    import capo_securitylake.types.account_list
    import capo_securitylake.types.amazon_resource_name
    import capo_securitylake.types.aws_identity
    import capo_securitylake.types.aws_log_source_configuration_list
    import capo_securitylake.types.create_aws_log_source_request
    import capo_securitylake.types.create_aws_log_source_response
    import capo_securitylake.types.create_custom_log_source_request
    import capo_securitylake.types.create_custom_log_source_response
    import capo_securitylake.types.create_data_lake_exception_subscription_request
    import capo_securitylake.types.create_data_lake_exception_subscription_response
    import capo_securitylake.types.create_data_lake_organization_configuration_request
    import capo_securitylake.types.create_data_lake_organization_configuration_response
    import capo_securitylake.types.create_data_lake_request
    import capo_securitylake.types.create_data_lake_response
    import capo_securitylake.types.create_subscriber_notification_request
    import capo_securitylake.types.create_subscriber_notification_response
    import capo_securitylake.types.create_subscriber_request
    import capo_securitylake.types.create_subscriber_response
    import capo_securitylake.types.custom_log_source_configuration
    import capo_securitylake.types.custom_log_source_name
    import capo_securitylake.types.custom_log_source_version
    import capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list
    import capo_securitylake.types.data_lake_configuration_list
    import capo_securitylake.types.data_lake_exception
    import capo_securitylake.types.data_lake_source
    import capo_securitylake.types.delete_aws_log_source_request
    import capo_securitylake.types.delete_aws_log_source_response
    import capo_securitylake.types.delete_custom_log_source_request
    import capo_securitylake.types.delete_custom_log_source_response
    import capo_securitylake.types.delete_data_lake_exception_subscription_request
    import capo_securitylake.types.delete_data_lake_exception_subscription_response
    import capo_securitylake.types.delete_data_lake_organization_configuration_request
    import capo_securitylake.types.delete_data_lake_organization_configuration_response
    import capo_securitylake.types.delete_data_lake_request
    import capo_securitylake.types.delete_data_lake_response
    import capo_securitylake.types.delete_subscriber_notification_request
    import capo_securitylake.types.delete_subscriber_notification_response
    import capo_securitylake.types.delete_subscriber_request
    import capo_securitylake.types.delete_subscriber_response
    import capo_securitylake.types.deregister_data_lake_delegated_administrator_request
    import capo_securitylake.types.deregister_data_lake_delegated_administrator_response
    import capo_securitylake.types.description_string
    import capo_securitylake.types.get_data_lake_exception_subscription_request
    import capo_securitylake.types.get_data_lake_exception_subscription_response
    import capo_securitylake.types.get_data_lake_organization_configuration_request
    import capo_securitylake.types.get_data_lake_organization_configuration_response
    import capo_securitylake.types.get_data_lake_sources_request
    import capo_securitylake.types.get_data_lake_sources_response
    import capo_securitylake.types.get_subscriber_request
    import capo_securitylake.types.get_subscriber_response
    import capo_securitylake.types.list_data_lake_exceptions_request
    import capo_securitylake.types.list_data_lake_exceptions_response
    import capo_securitylake.types.list_data_lakes_request
    import capo_securitylake.types.list_data_lakes_response
    import capo_securitylake.types.list_log_sources_request
    import capo_securitylake.types.list_log_sources_response
    import capo_securitylake.types.list_subscribers_request
    import capo_securitylake.types.list_subscribers_response
    import capo_securitylake.types.list_tags_for_resource_request
    import capo_securitylake.types.list_tags_for_resource_response
    import capo_securitylake.types.log_source
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token
    import capo_securitylake.types.notification_configuration
    import capo_securitylake.types.ocsf_event_class_list
    import capo_securitylake.types.region_list
    import capo_securitylake.types.register_data_lake_delegated_administrator_request
    import capo_securitylake.types.register_data_lake_delegated_administrator_response
    import capo_securitylake.types.role_arn
    import capo_securitylake.types.safe_string
    import capo_securitylake.types.subscriber_resource
    import capo_securitylake.types.subscription_protocol
    import capo_securitylake.types.tag_key_list
    import capo_securitylake.types.tag_list
    import capo_securitylake.types.tag_resource_request
    import capo_securitylake.types.tag_resource_response
    import capo_securitylake.types.untag_resource_request
    import capo_securitylake.types.untag_resource_response
    import capo_securitylake.types.update_data_lake_exception_subscription_request
    import capo_securitylake.types.update_data_lake_exception_subscription_response
    import capo_securitylake.types.update_data_lake_request
    import capo_securitylake.types.update_data_lake_response
    import capo_securitylake.types.update_subscriber_notification_request
    import capo_securitylake.types.update_subscriber_notification_response
    import capo_securitylake.types.update_subscriber_request
    import capo_securitylake.types.update_subscriber_response
    import capo_securitylake.types.uuid


class AsyncSecurityLakeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSecurityLakeClient:
    """A client for the ``SecurityLake`` service.

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
        self._config = AsyncSecurityLakeClientConfig(
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

        # resources
        self.data_lake = AsyncDataLake(self)
        self.subscriber = AsyncSubscriber(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSecurityLakeClientConfig = config_overrides or {}
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

    async def create_data_lake_exception_subscription(
        self,
        subscription_protocol: "capo_securitylake.types.subscription_protocol.SubscriptionProtocol",
        notification_endpoint: "capo_securitylake.types.safe_string.SafeString",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        exception_time_to_live: Optional[int] = None,
    ) -> "capo_securitylake.types.create_data_lake_exception_subscription_response.CreateDataLakeExceptionSubscriptionResponse":
        """<p>Creates the specified notification subscription in Amazon Security Lake for the organization you specify. The notification subscription is created for exceptions that cannot be resolved by Security Lake automatically.</p>

        Args:
            subscription_protocol: <p>The subscription protocol to which exception notifications are posted.</p>
            notification_endpoint: <p>The Amazon Web Services account where you want to receive exception notifications.</p>
            exception_time_to_live: <p>The expiration period and time-to-live (TTL). It is the duration of time until which the exception message remains.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_data_lake_exception_subscription_request.CreateDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_data_lake_exception_subscription_response.CreateDataLakeExceptionSubscriptionResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_data_lake_exception_subscription.async_create_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_exception_subscription_request.CreateDataLakeExceptionSubscriptionRequest = {
            "subscription_protocol": subscription_protocol,
            "notification_endpoint": notification_endpoint,
        }
        if exception_time_to_live is not None:
            input_["exception_time_to_live"] = exception_time_to_live

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_lake_exception_subscription(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "capo_securitylake.types.delete_data_lake_exception_subscription_response.DeleteDataLakeExceptionSubscriptionResponse":
        """<p>Deletes the specified notification subscription in Amazon Security Lake for the organization you specify.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_data_lake_exception_subscription_request.DeleteDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_data_lake_exception_subscription_response.DeleteDataLakeExceptionSubscriptionResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_data_lake_exception_subscription.async_delete_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_exception_subscription_request.DeleteDataLakeExceptionSubscriptionRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_data_lake_delegated_administrator(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "capo_securitylake.types.deregister_data_lake_delegated_administrator_response.DeregisterDataLakeDelegatedAdministratorResponse":
        """<p>Deletes the Amazon Security Lake delegated administrator account for the organization. This API can only be called by the organization management account. The organization management account cannot be the delegated administrator account.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.deregister_data_lake_delegated_administrator_request.DeregisterDataLakeDelegatedAdministratorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.deregister_data_lake_delegated_administrator_response.DeregisterDataLakeDelegatedAdministratorResponse"
        ]:
            import capo_securitylake._operations.security_lake.deregister_data_lake_delegated_administrator

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.deregister_data_lake_delegated_administrator.async_deregister_data_lake_delegated_administrator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.deregister_data_lake_delegated_administrator_request.DeregisterDataLakeDelegatedAdministratorRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_exception_subscription(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "capo_securitylake.types.get_data_lake_exception_subscription_response.GetDataLakeExceptionSubscriptionResponse":
        """<p>Retrieves the protocol and endpoint that were provided when subscribing to Amazon SNS topics for exception notifications.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_data_lake_exception_subscription_request.GetDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_data_lake_exception_subscription_response.GetDataLakeExceptionSubscriptionResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_data_lake_exception_subscription.async_get_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_exception_subscription_request.GetDataLakeExceptionSubscriptionRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_lake_exceptions(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.list_data_lake_exceptions_response.ListDataLakeExceptionsResponse":
        """<p>Lists the Amazon Security Lake exceptions that you can use to find the source of problems and fix them.</p>

        Args:
            regions: <p>The Amazon Web Services Regions from which exceptions are retrieved.</p>
            max_results: <p>Lists the maximum number of failures in Security Lake.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_data_lake_exceptions_request.ListDataLakeExceptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_data_lake_exceptions_response.ListDataLakeExceptionsResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_data_lake_exceptions

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_data_lake_exceptions.async_list_data_lake_exceptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.list_data_lake_exceptions_request.ListDataLakeExceptionsRequest = {}
        if regions is not None:
            input_["regions"] = regions
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

    async def iter_list_data_lake_exceptions(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securitylake.types.data_lake_exception.DataLakeException]":
        _token = next_token
        while True:
            _response = await self.list_data_lake_exceptions(
                config_overrides=config_overrides,
                regions=regions,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exceptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_securitylake.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the tags (keys and values) that are associated with an Amazon Security Lake resource: a subscriber, or the data lake configuration for your Amazon Web Services account in a particular Amazon Web Services Region.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource for which you want to retrieve the tags.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_data_lake_delegated_administrator(
        self,
        account_id: "capo_securitylake.types.safe_string.SafeString",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.register_data_lake_delegated_administrator_response.RegisterDataLakeDelegatedAdministratorResponse":
        """<p>Designates the Amazon Security Lake delegated administrator account for the organization. This API can only be called by the organization management account. The organization management account cannot be the delegated administrator account.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Security Lake delegated administrator.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.register_data_lake_delegated_administrator_request.RegisterDataLakeDelegatedAdministratorRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.register_data_lake_delegated_administrator_response.RegisterDataLakeDelegatedAdministratorResponse"
        ]:
            import capo_securitylake._operations.security_lake.register_data_lake_delegated_administrator

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.register_data_lake_delegated_administrator.async_register_data_lake_delegated_administrator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.register_data_lake_delegated_administrator_request.RegisterDataLakeDelegatedAdministratorRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_securitylake.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_securitylake.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates one or more tags that are associated with an Amazon Security Lake resource: a subscriber, or the data lake configuration for your Amazon Web Services account in a particular Amazon Web Services Region. A <i>tag</i> is a label that you can define and associate with Amazon Web Services resources. Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>. A <i>tag key</i> is a general label that acts as a category for a more specific tag value. A <i>tag value</i> acts as a descriptor for a tag key. Tags can help you identify, categorize, and manage resources in different ways, such as by owner, environment, or other criteria. For more information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html">Tagging Amazon Security Lake resources</a> in the <i>Amazon Security Lake User Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to add or update the tags for.</p>
            tags: <p>An array of objects, one for each tag (key and value) to associate with the Amazon Security Lake resource. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.tag_resource

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_securitylake.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_securitylake.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags (keys and values) from an Amazon Security Lake resource: a subscriber, or the data lake configuration for your Amazon Web Services account in a particular Amazon Web Services Region.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Security Lake resource to remove one or more tags from.</p>
            tag_keys: <p>A list of one or more tag keys. For each value in the list, specify the tag key for a tag to remove from the Amazon Security Lake resource.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.untag_resource

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_data_lake_exception_subscription(
        self,
        subscription_protocol: "capo_securitylake.types.subscription_protocol.SubscriptionProtocol",
        notification_endpoint: "capo_securitylake.types.safe_string.SafeString",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        exception_time_to_live: Optional[int] = None,
    ) -> "capo_securitylake.types.update_data_lake_exception_subscription_response.UpdateDataLakeExceptionSubscriptionResponse":
        """<p>Updates the specified notification subscription in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscription_protocol: <p>The subscription protocol to which exception messages are posted.</p>
            notification_endpoint: <p>The account that is subscribed to receive exception notifications.</p>
            exception_time_to_live: <p>The time-to-live (TTL) for the exception message to remain. It is the duration of time until which the exception message remains. </p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_data_lake_exception_subscription_request.UpdateDataLakeExceptionSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_data_lake_exception_subscription_response.UpdateDataLakeExceptionSubscriptionResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_data_lake_exception_subscription

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_data_lake_exception_subscription.async_update_data_lake_exception_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.update_data_lake_exception_subscription_request.UpdateDataLakeExceptionSubscriptionRequest = {
            "subscription_protocol": subscription_protocol,
            "notification_endpoint": notification_endpoint,
        }
        if exception_time_to_live is not None:
            input_["exception_time_to_live"] = exception_time_to_live

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_aws_log_source(
        self,
        sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.create_aws_log_source_response.CreateAwsLogSourceResponse":
        """<p>Adds a natively supported Amazon Web Services service as an Amazon Security Lake source. Enables source types for member accounts in required Amazon Web Services Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an Amazon Web Services service as a source, Security Lake starts collecting logs and events from it.</p> <p>You can use this API only to enable natively supported Amazon Web Services services as a source. Use <code>CreateCustomLogSource</code> to enable data collection from a custom source.</p>

        Args:
            sources: <p>Specify the natively-supported Amazon Web Services service to add as a source in Security Lake.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_aws_log_source_request.CreateAwsLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_aws_log_source_response.CreateAwsLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_aws_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_aws_log_source.async_create_aws_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_aws_log_source_request.CreateAwsLogSourceRequest = {
            "sources": sources
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_log_source(
        self,
        source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName",
        configuration: "capo_securitylake.types.custom_log_source_configuration.CustomLogSourceConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        source_version: Optional[
            "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
        ] = None,
        event_classes: Optional[
            "capo_securitylake.types.ocsf_event_class_list.OcsfEventClassList"
        ] = None,
    ) -> "capo_securitylake.types.create_custom_log_source_response.CreateCustomLogSourceResponse":
        """<p>Adds a third-party custom source in Amazon Security Lake, from the Amazon Web Services Region where you want to create a custom source. Security Lake can collect logs and events from third-party custom sources. After creating the appropriate IAM role to invoke Glue crawler, use this API to add a custom source name in Security Lake. This operation creates a partition in the Amazon S3 bucket for Security Lake as the target location for log files from the custom source. In addition, this operation also creates an associated Glue table and an Glue crawler.</p>

        Args:
            source_name: <p>Specify the name for a third-party custom source. This must be a Regionally unique value. The <code>sourceName</code> you enter here, is used in the <code>LogProviderRole</code> name which follows the convention <code>AmazonSecurityLake-Provider-{name of the custom source}-{region}</code>. You must use a <code>CustomLogSource</code> name that is shorter than or equal to 20 characters. This ensures that the <code>LogProviderRole</code> name is below the 64 character limit.</p>
            source_version: <p>Specify the source version for the third-party custom source, to limit log collection to a specific version of custom data source.</p>
            event_classes: <p>The Open Cybersecurity Schema Framework (OCSF) event classes which describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass">Amazon Security Lake User Guide</a>.</p>
            configuration: <p>The configuration used for the third-party custom source.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_custom_log_source_request.CreateCustomLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_custom_log_source_response.CreateCustomLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_custom_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_custom_log_source.async_create_custom_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_custom_log_source_request.CreateCustomLogSourceRequest = {
            "source_name": source_name,
            "configuration": configuration,
        }
        if source_version is not None:
            input_["source_version"] = source_version
        if event_classes is not None:
            input_["event_classes"] = event_classes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_lake(
        self,
        configurations: "capo_securitylake.types.data_lake_configuration_list.DataLakeConfigurationList",
        meta_store_manager_role_arn: "capo_securitylake.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        tags: Optional["capo_securitylake.types.tag_list.TagList"] = None,
    ) -> "capo_securitylake.types.create_data_lake_response.CreateDataLakeResponse":
        """<p>Initializes an Amazon Security Lake instance with the provided (or default) configuration. You can enable Security Lake in Amazon Web Services Regions with customized settings before enabling log collection in Regions. To specify particular Regions, configure these Regions using the <code>configurations</code> parameter. If you have already enabled Security Lake in a Region when you call this command, the command will update the Region if you provide new configuration parameters. If you have not already enabled Security Lake in the Region when you call this API, it will set up the data lake in the Region with the specified configurations.</p> <p>When you enable Security Lake, it starts ingesting security data after the <code>CreateAwsLogSource</code> call and after you create subscribers using the <code>CreateSubscriber</code> API. This includes ingesting security data from sources, storing data, and making data accessible to subscribers. Security Lake also enables all the existing settings and resources that it stores or maintains for your Amazon Web Services account in the current Region, including security log and event data. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html">Amazon Security Lake User Guide</a>.</p>

        Args:
            configurations: <p>Specify the Region or Regions that will contribute data to the rollup region.</p>
            meta_store_manager_role_arn: <p>The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.</p>
            tags: <p>An array of objects, one for each tag to associate with the data lake configuration. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_data_lake_request.CreateDataLakeRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_data_lake_response.CreateDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_data_lake.async_create_data_lake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_request.CreateDataLakeRequest = {
            "configurations": configurations,
            "meta_store_manager_role_arn": meta_store_manager_role_arn,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_lake_organization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        auto_enable_new_account: Optional[
            "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
        ] = None,
    ) -> "capo_securitylake.types.create_data_lake_organization_configuration_response.CreateDataLakeOrganizationConfigurationResponse":
        """<p>Automatically enables Amazon Security Lake for new member accounts in your organization. Security Lake is not automatically enabled for any existing member accounts in your organization.</p> <p>This operation merges the new data lake organization configuration with the existing configuration for Security Lake in your organization. If you want to create a new data lake organization configuration, you must delete the existing one using <a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeOrganizationConfiguration.html">DeleteDataLakeOrganizationConfiguration</a>.</p>

        Args:
            auto_enable_new_account: <p>Enable Security Lake with the specified configuration settings, to begin collecting security data for new accounts in your organization.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_data_lake_organization_configuration_request.CreateDataLakeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_data_lake_organization_configuration_response.CreateDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_data_lake_organization_configuration.async_create_data_lake_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_organization_configuration_request.CreateDataLakeOrganizationConfigurationRequest = {}
        if auto_enable_new_account is not None:
            input_["auto_enable_new_account"] = auto_enable_new_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_aws_log_source(
        self,
        sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_aws_log_source_response.DeleteAwsLogSourceResponse":
        """<p>Removes a natively supported Amazon Web Services service as an Amazon Security Lake source. You can remove a source for one or more Regions. When you remove the source, Security Lake stops collecting data from that source in the specified Regions and accounts, and subscribers can no longer consume new data from the source. However, subscribers can still consume data that Security Lake collected from the source before removal.</p> <p>You can choose any source type in any Amazon Web Services Region for either accounts that are part of a trusted organization or standalone accounts. </p>

        Args:
            sources: <p>Specify the natively-supported Amazon Web Services service to remove as a source in Security Lake.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_aws_log_source_request.DeleteAwsLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_aws_log_source_response.DeleteAwsLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_aws_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_aws_log_source.async_delete_aws_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_aws_log_source_request.DeleteAwsLogSourceRequest = {
            "sources": sources
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_log_source(
        self,
        source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        source_version: Optional[
            "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
        ] = None,
    ) -> "capo_securitylake.types.delete_custom_log_source_response.DeleteCustomLogSourceResponse":
        """<p>Removes a custom log source from Amazon Security Lake, to stop sending data from the custom source to Security Lake.</p>

        Args:
            source_name: <p>The source name of custom log source that you want to delete.</p>
            source_version: <p>The source version for the third-party custom source. You can limit the custom source removal to the specified source version.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_custom_log_source_request.DeleteCustomLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_custom_log_source_response.DeleteCustomLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_custom_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_custom_log_source.async_delete_custom_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_custom_log_source_request.DeleteCustomLogSourceRequest = {
            "source_name": source_name
        }
        if source_version is not None:
            input_["source_version"] = source_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_lake(
        self,
        regions: "capo_securitylake.types.region_list.RegionList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_data_lake_response.DeleteDataLakeResponse":
        """<p>When you disable Amazon Security Lake from your account, Security Lake is disabled in all Amazon Web Services Regions and it stops collecting data from your sources. Also, this API automatically takes steps to remove the account from Security Lake. However, Security Lake retains all of your existing settings and the resources that it created in your Amazon Web Services account in the current Amazon Web Services Region.</p> <p>The <code>DeleteDataLake</code> operation does not delete the data that is stored in your Amazon S3 bucket, which is owned by your Amazon Web Services account. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/disable-security-lake.html">Amazon Security Lake User Guide</a>.</p>

        Args:
            regions: <p>The list of Regions where Security Lake is enabled.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_data_lake_request.DeleteDataLakeRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_data_lake_response.DeleteDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_data_lake.async_delete_data_lake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_request.DeleteDataLakeRequest = {
            "regions": regions
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_lake_organization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        auto_enable_new_account: Optional[
            "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
        ] = None,
    ) -> "capo_securitylake.types.delete_data_lake_organization_configuration_response.DeleteDataLakeOrganizationConfigurationResponse":
        """<p>Turns off automatic enablement of Amazon Security Lake for member accounts that are added to an organization in Organizations. Only the delegated Security Lake administrator for an organization can perform this operation. If the delegated Security Lake administrator performs this operation, new member accounts won't automatically contribute data to the data lake.</p>

        Args:
            auto_enable_new_account: <p>Turns off automatic enablement of Security Lake for member accounts that are added to an organization.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_data_lake_organization_configuration_request.DeleteDataLakeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_data_lake_organization_configuration_response.DeleteDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_data_lake_organization_configuration.async_delete_data_lake_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_organization_configuration_request.DeleteDataLakeOrganizationConfigurationRequest = {}
        if auto_enable_new_account is not None:
            input_["auto_enable_new_account"] = auto_enable_new_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_organization_configuration(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "capo_securitylake.types.get_data_lake_organization_configuration_response.GetDataLakeOrganizationConfigurationResponse":
        """<p>Retrieves the configuration that will be automatically set up for accounts added to the organization after the organization has onboarded to Amazon Security Lake. This API does not take input parameters.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_data_lake_organization_configuration_request.GetDataLakeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_data_lake_organization_configuration_response.GetDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_data_lake_organization_configuration.async_get_data_lake_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_organization_configuration_request.GetDataLakeOrganizationConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_sources(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.get_data_lake_sources_response.GetDataLakeSourcesResponse":
        """<p>Retrieves a snapshot of the current Region, including whether Amazon Security Lake is enabled for those accounts and which sources Security Lake is collecting data from.</p>

        Args:
            accounts: <p>The Amazon Web Services account ID for which a static snapshot of the current Amazon Web Services Region, including enabled accounts and log sources, is retrieved.</p>
            max_results: <p>The maximum limit of accounts for which the static snapshot of the current Region, including enabled accounts and log sources, is retrieved.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_data_lake_sources_request.GetDataLakeSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_data_lake_sources_response.GetDataLakeSourcesResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_sources

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_data_lake_sources.async_get_data_lake_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_sources_request.GetDataLakeSourcesRequest = {}
        if accounts is not None:
            input_["accounts"] = accounts
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

    async def iter_get_data_lake_sources(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securitylake.types.data_lake_source.DataLakeSource]":
        _token = next_token
        while True:
            _response = await self.get_data_lake_sources(
                config_overrides=config_overrides,
                accounts=accounts,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("data_lake_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_lakes(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
    ) -> "capo_securitylake.types.list_data_lakes_response.ListDataLakesResponse":
        """<p>Retrieves the Amazon Security Lake configuration object for the specified Amazon Web Services Regions. You can use this operation to determine whether Security Lake is enabled for a Region.</p>

        Args:
            regions: <p>The list of Regions where Security Lake is enabled.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_data_lakes_request.ListDataLakesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_data_lakes_response.ListDataLakesResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_data_lakes

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_data_lakes.async_list_data_lakes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.list_data_lakes_request.ListDataLakesRequest = {}
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_log_sources(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.list_log_sources_response.ListLogSourcesResponse":
        """<p>Retrieves the log sources.</p>

        Args:
            accounts: <p>The list of Amazon Web Services accounts for which log sources are displayed.</p>
            regions: <p>The list of Regions for which log sources are displayed.</p>
            sources: <p>The list of sources for which log sources are displayed.</p>
            max_results: <p>The maximum number of accounts for which the log sources are displayed.</p>
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_log_sources_request.ListLogSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_log_sources_response.ListLogSourcesResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_log_sources

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_log_sources.async_list_log_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.list_log_sources_request.ListLogSourcesRequest = {}
        if accounts is not None:
            input_["accounts"] = accounts
        if regions is not None:
            input_["regions"] = regions
        if sources is not None:
            input_["sources"] = sources
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

    async def iter_list_log_sources(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_securitylake.types.log_source.LogSource]":
        _token = next_token
        while True:
            _response = await self.list_log_sources(
                config_overrides=config_overrides,
                accounts=accounts,
                regions=regions,
                sources=sources,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_data_lake(
        self,
        configurations: "capo_securitylake.types.data_lake_configuration_list.DataLakeConfigurationList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        meta_store_manager_role_arn: Optional[
            "capo_securitylake.types.role_arn.RoleArn"
        ] = None,
    ) -> "capo_securitylake.types.update_data_lake_response.UpdateDataLakeResponse":
        """<p>You can use <code>UpdateDataLake</code> to specify where to store your security data, how it should be encrypted at rest and for how long. You can add a <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/manage-regions.html#add-rollup-region">Rollup Region</a> to consolidate data from multiple Amazon Web Services Regions, replace default encryption (SSE-S3) with <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">Customer Manged Key</a>, or specify transition and expiration actions through storage <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html">Lifecycle management</a>. The <code>UpdateDataLake</code> API works as an "upsert" operation that performs an insert if the specified item or record does not exist, or an update if it already exists. Security Lake securely stores your data at rest using Amazon Web Services encryption solutions. For more details, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/data-protection.html">Data protection in Amazon Security Lake</a>.</p> <p>For example, omitting the key <code>encryptionConfiguration</code> from a Region that is included in an update call that currently uses KMS will leave that Region's KMS key in place, but specifying <code>encryptionConfiguration: {kmsKeyId: 'S3_MANAGED_KEY'}</code> for that same Region will reset the key to <code>S3-managed</code>.</p> <p>For more details about lifecycle management and how to update retention settings for one or more Regions after enabling Security Lake, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html">Amazon Security Lake User Guide</a>. </p>

        Args:
            configurations: <p>Specifies the Region or Regions that will contribute data to the rollup region.</p>
            meta_store_manager_role_arn: <p>The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_data_lake_request.UpdateDataLakeRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_data_lake_response.UpdateDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_data_lake

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_data_lake.async_update_data_lake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.update_data_lake_request.UpdateDataLakeRequest = {
            "configurations": configurations
        }
        if meta_store_manager_role_arn is not None:
            input_["meta_store_manager_role_arn"] = meta_store_manager_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_subscriber(
        self,
        subscriber_identity: "capo_securitylake.types.aws_identity.AwsIdentity",
        subscriber_name: str,
        sources: "capo_securitylake.types.log_source_resource_list.LogSourceResourceList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        subscriber_description: Optional[
            "capo_securitylake.types.description_string.DescriptionString"
        ] = None,
        access_types: Optional[
            "capo_securitylake.types.access_type_list.AccessTypeList"
        ] = None,
        tags: Optional["capo_securitylake.types.tag_list.TagList"] = None,
    ) -> "capo_securitylake.types.create_subscriber_response.CreateSubscriberResponse":
        """<p>Creates a subscriber for accounts that are already enabled in Amazon Security Lake. You can create a subscriber with access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of your Security Lake subscriber account.</p>
            subscriber_description: <p>The description for your subscriber account in Security Lake.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services services.</p>
            access_types: <p>The Amazon S3 or Lake Formation access type.</p>
            tags: <p>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_subscriber.async_create_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_subscriber_request.CreateSubscriberRequest = {
            "subscriber_identity": subscriber_identity,
            "subscriber_name": subscriber_name,
            "sources": sources,
        }
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if access_types is not None:
            input_["access_types"] = access_types
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscriber(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.get_subscriber_response.GetSubscriberResponse":
        """<p>Retrieves the subscription information for the specified subscription ID. You can get information about a specific subscriber.</p>

        Args:
            subscriber_id: <p>A value created by Amazon Security Lake that uniquely identifies your <code>GetSubscriber</code> API request.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_subscriber_request.GetSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_subscriber_response.GetSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_subscriber.async_get_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.get_subscriber_request.GetSubscriberRequest = {
            "subscriber_id": subscriber_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscriber(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        subscriber_identity: Optional[
            "capo_securitylake.types.aws_identity.AwsIdentity"
        ] = None,
        subscriber_name: Optional[
            "capo_securitylake.types.safe_string.SafeString"
        ] = None,
        subscriber_description: Optional[
            "capo_securitylake.types.description_string.DescriptionString"
        ] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
    ) -> "capo_securitylake.types.update_subscriber_response.UpdateSubscriberResponse":
        """<p>Updates an existing subscription for the given Amazon Security Lake account ID. You can update a subscriber by changing the sources that the subscriber consumes data from.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your subscription.</p>
            subscriber_identity: <p>The Amazon Web Services identity used to access your data.</p>
            subscriber_name: <p>The name of the Security Lake account subscriber.</p>
            subscriber_description: <p>The description of the Security Lake account subscriber.</p>
            sources: <p>The supported Amazon Web Services services from which logs and events are collected. For the list of supported Amazon Web Services services, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Amazon Security Lake User Guide</a>.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_subscriber.async_update_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.update_subscriber_request.UpdateSubscriberRequest = {
            "subscriber_id": subscriber_id
        }
        if subscriber_identity is not None:
            input_["subscriber_identity"] = subscriber_identity
        if subscriber_name is not None:
            input_["subscriber_name"] = subscriber_name
        if subscriber_description is not None:
            input_["subscriber_description"] = subscriber_description
        if sources is not None:
            input_["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscriber(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse":
        """<p>Deletes the subscription permission and all notification settings for accounts that are already enabled in Amazon Security Lake. When you run <code>DeleteSubscriber</code>, the subscriber will no longer consume data from Security Lake and the subscriber is removed. This operation deletes the subscriber and removes access to data in the current Amazon Web Services Region.</p>

        Args:
            subscriber_id: <p>A value created by Security Lake that uniquely identifies your <code>DeleteSubscriber</code> API request.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_subscriber

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_subscriber.async_delete_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_subscriber_request.DeleteSubscriberRequest = {
            "subscriber_id": subscriber_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_subscribers(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
    ) -> "capo_securitylake.types.list_subscribers_response.ListSubscribersResponse":
        """<p>Lists all subscribers for the specific Amazon Security Lake account ID. You can retrieve a list of subscriptions associated with a specific organization or Amazon Web Services account.</p>

        Args:
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>
            max_results: <p>The maximum number of accounts for which the configuration is displayed.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_subscribers_request.ListSubscribersRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_subscribers_response.ListSubscribersResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_subscribers

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_subscribers.async_list_subscribers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.list_subscribers_request.ListSubscribersRequest = {}
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

    async def iter_list_subscribers(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_securitylake.types.subscriber_resource.SubscriberResource]"
    ):
        _token = next_token
        while True:
            _response = await self.list_subscribers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("subscribers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        configuration: "capo_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse":
        """<p>Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake. You can create only one subscriber notification per subscriber.</p>

        Args:
            subscriber_id: <p>The subscriber ID for the notification subscription.</p>
            configuration: <p>Specify the configuration using which you want to create the subscriber notification.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_subscriber_notification_response.CreateSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_subscriber_notification

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_subscriber_notification.async_create_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.create_subscriber_notification_request.CreateSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse":
        """<p>Deletes the specified subscription notification in Amazon Security Lake for the organization you specify.</p>

        Args:
            subscriber_id: <p>The ID of the Security Lake subscriber account.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_subscriber_notification_response.DeleteSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_subscriber_notification

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_subscriber_notification.async_delete_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_subscriber_notification_request.DeleteSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscriber_notification(
        self,
        subscriber_id: "capo_securitylake.types.uuid.UUID",
        configuration: "capo_securitylake.types.notification_configuration.NotificationConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse":
        """<p>Updates an existing notification method for the subscription (SQS or HTTPs endpoint) or switches the notification subscription endpoint for a subscriber.</p>

        Args:
            subscriber_id: <p>The subscription ID for which the subscription notification is specified.</p>
            configuration: <p>The configuration for subscriber notification.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_subscriber_notification_response.UpdateSubscriberNotificationResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_subscriber_notification

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_subscriber_notification.async_update_subscriber_notification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_securitylake.types.update_subscriber_notification_request.UpdateSubscriberNotificationRequest = {
            "subscriber_id": subscriber_id,
            "configuration": configuration,
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
