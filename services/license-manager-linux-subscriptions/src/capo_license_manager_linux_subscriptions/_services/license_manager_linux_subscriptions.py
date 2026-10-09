"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#LicenseManagerLinuxSubscriptions``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_license_manager_linux_subscriptions._auth._signers
import capo_license_manager_linux_subscriptions._auth._sigv4
from capo_license_manager_linux_subscriptions._auth._identity import Credentials
from capo_license_manager_linux_subscriptions._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_license_manager_linux_subscriptions._auth._zapros_handler import (
    AuthMiddleware,
)
from capo_license_manager_linux_subscriptions._pagination import (
    resolve_path as _resolve_path,
)
from capo_license_manager_linux_subscriptions._services._aws_config import aws_config
from capo_license_manager_linux_subscriptions._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.box_integer
    import capo_license_manager_linux_subscriptions.types.deregister_subscription_provider_request
    import capo_license_manager_linux_subscriptions.types.deregister_subscription_provider_response
    import capo_license_manager_linux_subscriptions.types.filter_list
    import capo_license_manager_linux_subscriptions.types.get_registered_subscription_provider_request
    import capo_license_manager_linux_subscriptions.types.get_registered_subscription_provider_response
    import capo_license_manager_linux_subscriptions.types.get_service_settings_request
    import capo_license_manager_linux_subscriptions.types.get_service_settings_response
    import capo_license_manager_linux_subscriptions.types.instance
    import capo_license_manager_linux_subscriptions.types.linux_subscriptions_discovery
    import capo_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings
    import capo_license_manager_linux_subscriptions.types.list_linux_subscription_instances_request
    import capo_license_manager_linux_subscriptions.types.list_linux_subscription_instances_response
    import capo_license_manager_linux_subscriptions.types.list_linux_subscriptions_request
    import capo_license_manager_linux_subscriptions.types.list_linux_subscriptions_response
    import capo_license_manager_linux_subscriptions.types.list_registered_subscription_providers_request
    import capo_license_manager_linux_subscriptions.types.list_registered_subscription_providers_response
    import capo_license_manager_linux_subscriptions.types.list_tags_for_resource_request
    import capo_license_manager_linux_subscriptions.types.list_tags_for_resource_response
    import capo_license_manager_linux_subscriptions.types.register_subscription_provider_request
    import capo_license_manager_linux_subscriptions.types.register_subscription_provider_response
    import capo_license_manager_linux_subscriptions.types.registered_subscription_provider
    import capo_license_manager_linux_subscriptions.types.secret_arn
    import capo_license_manager_linux_subscriptions.types.subscription
    import capo_license_manager_linux_subscriptions.types.subscription_provider_arn
    import capo_license_manager_linux_subscriptions.types.subscription_provider_source
    import capo_license_manager_linux_subscriptions.types.subscription_provider_source_list
    import capo_license_manager_linux_subscriptions.types.tag_key_list
    import capo_license_manager_linux_subscriptions.types.tag_resource_request
    import capo_license_manager_linux_subscriptions.types.tag_resource_response
    import capo_license_manager_linux_subscriptions.types.tags
    import capo_license_manager_linux_subscriptions.types.untag_resource_request
    import capo_license_manager_linux_subscriptions.types.untag_resource_response
    import capo_license_manager_linux_subscriptions.types.update_service_settings_request
    import capo_license_manager_linux_subscriptions.types.update_service_settings_response


class LicenseManagerLinuxSubscriptionsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class LicenseManagerLinuxSubscriptionsClient:
    """A client for the ``LicenseManagerLinuxSubscriptions`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = LicenseManagerLinuxSubscriptionsClientConfig(
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
        self,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LicenseManagerLinuxSubscriptionsClientConfig = config_overrides or {}
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

    def deregister_subscription_provider(
        self,
        subscription_provider_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.deregister_subscription_provider_response.DeregisterSubscriptionProviderResponse":
        """<p>Remove a third-party subscription provider from the Bring Your Own License (BYOL) subscriptions registered to your account.</p>

        Args:
            subscription_provider_arn: <p>The Amazon Resource Name (ARN) of the subscription provider resource to deregister.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to find the requested Amazon Web Services resource.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.deregister_subscription_provider_request.DeregisterSubscriptionProviderRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.deregister_subscription_provider_response.DeregisterSubscriptionProviderResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.deregister_subscription_provider

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.deregister_subscription_provider.deregister_subscription_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.deregister_subscription_provider_request.DeregisterSubscriptionProviderRequest = {
            "subscription_provider_arn": subscription_provider_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_registered_subscription_provider(
        self,
        subscription_provider_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.get_registered_subscription_provider_response.GetRegisteredSubscriptionProviderResponse":
        """<p>Get details for a Bring Your Own License (BYOL) subscription that's registered to your account.</p>

        Args:
            subscription_provider_arn: <p>The Amazon Resource Name (ARN) of the BYOL registration resource to get details for.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to find the requested Amazon Web Services resource.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.get_registered_subscription_provider_request.GetRegisteredSubscriptionProviderRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.get_registered_subscription_provider_response.GetRegisteredSubscriptionProviderResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.get_registered_subscription_provider

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.get_registered_subscription_provider.get_registered_subscription_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.get_registered_subscription_provider_request.GetRegisteredSubscriptionProviderRequest = {
            "subscription_provider_arn": subscription_provider_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_settings(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.get_service_settings_response.GetServiceSettingsResponse":
        """<p>Lists the Linux subscriptions service settings for your account.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.get_service_settings_request.GetServiceSettingsRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.get_service_settings_response.GetServiceSettingsResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.get_service_settings

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.get_service_settings.get_service_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.get_service_settings_request.GetServiceSettingsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_linux_subscription_instances(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        filters: Optional[
            "capo_license_manager_linux_subscriptions.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.list_linux_subscription_instances_response.ListLinuxSubscriptionInstancesResponse":
        """<p>Lists the running Amazon EC2 instances that were discovered with commercial Linux subscriptions.</p>

        Args:
            filters: <p>An array of structures that you can use to filter the results by your specified criteria. For example, you can specify <code>Region</code> in the <code>Name</code>, with the <code>contains</code> operator to list all subscriptions that match a partial string in the <code>Value</code>, such as <code>us-west</code>.</p> <p>For each filter, you can specify one of the following values for the <code>Name</code> key to streamline results:</p> <ul> <li> <p> <code>AccountID</code> </p> </li> <li> <p> <code>AmiID</code> </p> </li> <li> <p> <code>DualSubscription</code> </p> </li> <li> <p> <code>InstanceID</code> </p> </li> <li> <p> <code>InstanceType</code> </p> </li> <li> <p> <code>ProductCode</code> </p> </li> <li> <p> <code>Region</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>UsageOperation</code> </p> </li> </ul> <p>For each filter, you can use one of the following <code>Operator</code> values to define the behavior of the filter:</p> <ul> <li> <p> <code>contains</code> </p> </li> <li> <p> <code>equals</code> </p> </li> <li> <p> <code>Notequal</code> </p> </li> </ul>
            max_results: <p>The maximum items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.list_linux_subscription_instances_request.ListLinuxSubscriptionInstancesRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.list_linux_subscription_instances_response.ListLinuxSubscriptionInstancesResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_linux_subscription_instances

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_linux_subscription_instances.list_linux_subscription_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.list_linux_subscription_instances_request.ListLinuxSubscriptionInstancesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_linux_subscription_instances(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        filters: Optional[
            "capo_license_manager_linux_subscriptions.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_license_manager_linux_subscriptions.types.instance.Instance]":
        _token = next_token
        while True:
            _response = self.list_linux_subscription_instances(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_linux_subscriptions(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        filters: Optional[
            "capo_license_manager_linux_subscriptions.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.list_linux_subscriptions_response.ListLinuxSubscriptionsResponse":
        """<p>Lists the Linux subscriptions that have been discovered. If you have linked your organization, the returned results will include data aggregated across your accounts in Organizations.</p>

        Args:
            filters: <p>An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify. For example, you can filter by the name of <code>Subscription</code> with an optional operator to see subscriptions that match, partially match, or don't match a certain subscription's name.</p> <p>The valid names for this filter are:</p> <ul> <li> <p> <code>Subscription</code> </p> </li> </ul> <p>The valid Operators for this filter are:</p> <ul> <li> <p> <code>contains</code> </p> </li> <li> <p> <code>equals</code> </p> </li> <li> <p> <code>Notequal</code> </p> </li> </ul>
            max_results: <p>The maximum items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.list_linux_subscriptions_request.ListLinuxSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.list_linux_subscriptions_response.ListLinuxSubscriptionsResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_linux_subscriptions

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_linux_subscriptions.list_linux_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.list_linux_subscriptions_request.ListLinuxSubscriptionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_linux_subscriptions(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        filters: Optional[
            "capo_license_manager_linux_subscriptions.types.filter_list.FilterList"
        ] = None,
        max_results: Optional[
            "capo_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_license_manager_linux_subscriptions.types.subscription.Subscription]":
        _token = next_token
        while True:
            _response = self.list_linux_subscriptions(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_registered_subscription_providers(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        subscription_provider_sources: Optional[
            "capo_license_manager_linux_subscriptions.types.subscription_provider_source_list.SubscriptionProviderSourceList"
        ] = None,
        max_results: Optional[
            "capo_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.list_registered_subscription_providers_response.ListRegisteredSubscriptionProvidersResponse":
        """<p>List Bring Your Own License (BYOL) subscription registration resources for your account.</p>

        Args:
            subscription_provider_sources: <p>To filter your results, specify which subscription providers to return in the list.</p>
            max_results: <p>The maximum items to return in a request.</p>
            next_token: <p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.list_registered_subscription_providers_request.ListRegisteredSubscriptionProvidersRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.list_registered_subscription_providers_response.ListRegisteredSubscriptionProvidersResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_registered_subscription_providers

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_registered_subscription_providers.list_registered_subscription_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.list_registered_subscription_providers_request.ListRegisteredSubscriptionProvidersRequest = {}
        if subscription_provider_sources is not None:
            input_["subscription_provider_sources"] = subscription_provider_sources
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

    def iter_list_registered_subscription_providers(
        self,
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        subscription_provider_sources: Optional[
            "capo_license_manager_linux_subscriptions.types.subscription_provider_source_list.SubscriptionProviderSourceList"
        ] = None,
        max_results: Optional[
            "capo_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_license_manager_linux_subscriptions.types.registered_subscription_provider.RegisteredSubscriptionProvider]":
        _token = next_token
        while True:
            _response = self.list_registered_subscription_providers(
                config_overrides=config_overrides,
                subscription_provider_sources=subscription_provider_sources,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("registered_subscription_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List the metadata tags that are assigned to the specified Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list metadata tags.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to find the requested Amazon Web Services resource.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_tags_for_resource

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_subscription_provider(
        self,
        subscription_provider_source: "capo_license_manager_linux_subscriptions.types.subscription_provider_source.SubscriptionProviderSource",
        secret_arn: "capo_license_manager_linux_subscriptions.types.secret_arn.SecretArn",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        tags: Optional[
            "capo_license_manager_linux_subscriptions.types.tags.Tags"
        ] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.register_subscription_provider_response.RegisterSubscriptionProviderResponse":
        """<p>Register the supported third-party subscription provider for your Bring Your Own License (BYOL) subscription.</p>

        Args:
            subscription_provider_source: <p>The supported Linux subscription provider to register.</p>
            secret_arn: <p>The Amazon Resource Name (ARN) of the secret where you've stored your subscription provider's access token. For RHEL subscriptions managed through the Red Hat Subscription Manager (RHSM), the secret contains your Red Hat Offline token.</p>
            tags: <p>The metadata tags to assign to your registered Linux subscription provider resource.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.register_subscription_provider_request.RegisterSubscriptionProviderRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.register_subscription_provider_response.RegisterSubscriptionProviderResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.register_subscription_provider

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.register_subscription_provider.register_subscription_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.register_subscription_provider_request.RegisterSubscriptionProviderRequest = {
            "subscription_provider_source": subscription_provider_source,
            "secret_arn": secret_arn,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn",
        tags: "capo_license_manager_linux_subscriptions.types.tags.Tags",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.tag_resource_response.TagResourceResponse":
        """<p>Add metadata tags to the specified Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to which to add the specified metadata tags.</p>
            tags: <p>The metadata tags to assign to the Amazon Web Services resource. Tags are formatted as key value pairs.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to find the requested Amazon Web Services resource.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.tag_resource

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_license_manager_linux_subscriptions.types.subscription_provider_arn.SubscriptionProviderArn",
        tag_keys: "capo_license_manager_linux_subscriptions.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove one or more metadata tag from the specified Amazon Web Services resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource to remove the metadata tags from.</p>
            tag_keys: <p>A list of metadata tag keys to remove from the requested resource.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.resource_not_found_exception.ResourceNotFoundException: <p>Unable to find the requested Amazon Web Services resource.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.untag_resource

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_settings(
        self,
        linux_subscriptions_discovery: "capo_license_manager_linux_subscriptions.types.linux_subscriptions_discovery.LinuxSubscriptionsDiscovery",
        linux_subscriptions_discovery_settings: "capo_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.LinuxSubscriptionsDiscoverySettings",
        *,
        config_overrides: Optional[LicenseManagerLinuxSubscriptionsClientConfig] = None,
        allow_update: Optional[bool] = None,
    ) -> "capo_license_manager_linux_subscriptions.types.update_service_settings_response.UpdateServiceSettingsResponse":
        """<p>Updates the service settings for Linux subscriptions.</p>

        Args:
            linux_subscriptions_discovery: <p>Describes if the discovery of Linux subscriptions is enabled.</p>
            linux_subscriptions_discovery_settings: <p>The settings defined for Linux subscriptions discovery. The settings include if Organizations integration has been enabled, and which Regions data will be aggregated from.</p>
            allow_update: <p>Describes if updates are allowed to the service settings for Linux subscriptions. If you allow updates, you can aggregate Linux subscription data in more than one home Region.</p>

        Raises:
            capo_license_manager_linux_subscriptions.errors.internal_server_exception.InternalServerException: <p>An exception occurred with the service.</p>
            capo_license_manager_linux_subscriptions.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_license_manager_linux_subscriptions.errors.validation_exception.ValidationException: <p>The provided input is not valid. Try your request again.</p>
            capo_license_manager_linux_subscriptions.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_license_manager_linux_subscriptions.types.update_service_settings_request.UpdateServiceSettingsRequest]",
        ) -> OperationResponse[
            "capo_license_manager_linux_subscriptions.types.update_service_settings_response.UpdateServiceSettingsResponse"
        ]:
            import capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.update_service_settings

            output, http_response = (
                capo_license_manager_linux_subscriptions._operations.license_manager_linux_subscriptions.update_service_settings.update_service_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_license_manager_linux_subscriptions.types.update_service_settings_request.UpdateServiceSettingsRequest = {
            "linux_subscriptions_discovery": linux_subscriptions_discovery,
            "linux_subscriptions_discovery_settings": linux_subscriptions_discovery_settings,
        }
        if allow_update is not None:
            input_["allow_update"] = allow_update

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
