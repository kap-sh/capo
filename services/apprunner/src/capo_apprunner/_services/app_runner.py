"""Generated from Smithy shape ``com.amazonaws.apprunner#AppRunner``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_apprunner._auth._signers
import capo_apprunner._auth._sigv4
from capo_apprunner._auth._identity import Credentials
from capo_apprunner._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_apprunner._auth._zapros_handler import AuthMiddleware
from capo_apprunner._pagination import resolve_path as _resolve_path
from capo_apprunner._services._aws_config import aws_config
from capo_apprunner._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.as_config_max_concurrency
    import capo_apprunner.types.as_config_max_size
    import capo_apprunner.types.as_config_min_size
    import capo_apprunner.types.associate_custom_domain_request
    import capo_apprunner.types.associate_custom_domain_response
    import capo_apprunner.types.auto_scaling_configuration_name
    import capo_apprunner.types.boolean
    import capo_apprunner.types.connection_name
    import capo_apprunner.types.create_auto_scaling_configuration_request
    import capo_apprunner.types.create_auto_scaling_configuration_response
    import capo_apprunner.types.create_connection_request
    import capo_apprunner.types.create_connection_response
    import capo_apprunner.types.create_observability_configuration_request
    import capo_apprunner.types.create_observability_configuration_response
    import capo_apprunner.types.create_service_request
    import capo_apprunner.types.create_service_response
    import capo_apprunner.types.create_vpc_connector_request
    import capo_apprunner.types.create_vpc_connector_response
    import capo_apprunner.types.create_vpc_ingress_connection_request
    import capo_apprunner.types.create_vpc_ingress_connection_response
    import capo_apprunner.types.delete_auto_scaling_configuration_request
    import capo_apprunner.types.delete_auto_scaling_configuration_response
    import capo_apprunner.types.delete_connection_request
    import capo_apprunner.types.delete_connection_response
    import capo_apprunner.types.delete_observability_configuration_request
    import capo_apprunner.types.delete_observability_configuration_response
    import capo_apprunner.types.delete_service_request
    import capo_apprunner.types.delete_service_response
    import capo_apprunner.types.delete_vpc_connector_request
    import capo_apprunner.types.delete_vpc_connector_response
    import capo_apprunner.types.delete_vpc_ingress_connection_request
    import capo_apprunner.types.delete_vpc_ingress_connection_response
    import capo_apprunner.types.describe_auto_scaling_configuration_request
    import capo_apprunner.types.describe_auto_scaling_configuration_response
    import capo_apprunner.types.describe_custom_domains_max_results
    import capo_apprunner.types.describe_custom_domains_request
    import capo_apprunner.types.describe_custom_domains_response
    import capo_apprunner.types.describe_observability_configuration_request
    import capo_apprunner.types.describe_observability_configuration_response
    import capo_apprunner.types.describe_service_request
    import capo_apprunner.types.describe_service_response
    import capo_apprunner.types.describe_vpc_connector_request
    import capo_apprunner.types.describe_vpc_connector_response
    import capo_apprunner.types.describe_vpc_ingress_connection_request
    import capo_apprunner.types.describe_vpc_ingress_connection_response
    import capo_apprunner.types.disassociate_custom_domain_request
    import capo_apprunner.types.disassociate_custom_domain_response
    import capo_apprunner.types.domain_name
    import capo_apprunner.types.encryption_configuration
    import capo_apprunner.types.health_check_configuration
    import capo_apprunner.types.ingress_vpc_configuration
    import capo_apprunner.types.instance_configuration
    import capo_apprunner.types.list_auto_scaling_configurations_request
    import capo_apprunner.types.list_auto_scaling_configurations_response
    import capo_apprunner.types.list_connections_request
    import capo_apprunner.types.list_connections_response
    import capo_apprunner.types.list_observability_configurations_request
    import capo_apprunner.types.list_observability_configurations_response
    import capo_apprunner.types.list_operations_max_results
    import capo_apprunner.types.list_operations_request
    import capo_apprunner.types.list_operations_response
    import capo_apprunner.types.list_services_for_auto_scaling_configuration_request
    import capo_apprunner.types.list_services_for_auto_scaling_configuration_response
    import capo_apprunner.types.list_services_request
    import capo_apprunner.types.list_services_response
    import capo_apprunner.types.list_tags_for_resource_request
    import capo_apprunner.types.list_tags_for_resource_response
    import capo_apprunner.types.list_vpc_connectors_request
    import capo_apprunner.types.list_vpc_connectors_response
    import capo_apprunner.types.list_vpc_ingress_connections_filter
    import capo_apprunner.types.list_vpc_ingress_connections_request
    import capo_apprunner.types.list_vpc_ingress_connections_response
    import capo_apprunner.types.max_results
    import capo_apprunner.types.network_configuration
    import capo_apprunner.types.next_token
    import capo_apprunner.types.nullable_boolean
    import capo_apprunner.types.observability_configuration_name
    import capo_apprunner.types.pause_service_request
    import capo_apprunner.types.pause_service_response
    import capo_apprunner.types.provider_type
    import capo_apprunner.types.resume_service_request
    import capo_apprunner.types.resume_service_response
    import capo_apprunner.types.service_max_results
    import capo_apprunner.types.service_name
    import capo_apprunner.types.service_observability_configuration
    import capo_apprunner.types.source_configuration
    import capo_apprunner.types.start_deployment_request
    import capo_apprunner.types.start_deployment_response
    import capo_apprunner.types.string
    import capo_apprunner.types.string_list
    import capo_apprunner.types.tag_key_list
    import capo_apprunner.types.tag_list
    import capo_apprunner.types.tag_resource_request
    import capo_apprunner.types.tag_resource_response
    import capo_apprunner.types.trace_configuration
    import capo_apprunner.types.untag_resource_request
    import capo_apprunner.types.untag_resource_response
    import capo_apprunner.types.update_default_auto_scaling_configuration_request
    import capo_apprunner.types.update_default_auto_scaling_configuration_response
    import capo_apprunner.types.update_service_request
    import capo_apprunner.types.update_service_response
    import capo_apprunner.types.update_vpc_ingress_connection_request
    import capo_apprunner.types.update_vpc_ingress_connection_response
    import capo_apprunner.types.vpc_connector_name
    import capo_apprunner.types.vpc_ingress_connection_name


class AppRunnerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AppRunnerClient:
    """A client for the ``AppRunner`` service.

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
        self._config = AppRunnerClientConfig(
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
        self, config_overrides: Optional[AppRunnerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppRunnerClientConfig = config_overrides or {}
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

    def associate_custom_domain(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        domain_name: "capo_apprunner.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        enable_www_subdomain: Optional[
            "capo_apprunner.types.nullable_boolean.NullableBoolean"
        ] = None,
    ) -> "capo_apprunner.types.associate_custom_domain_response.AssociateCustomDomainResponse":
        """<p>Associate your own domain name with the App Runner subdomain URL of your App Runner service.</p> <p>After you call <code>AssociateCustomDomain</code> and receive a successful response, use the information in the <a>CustomDomain</a> record that's returned to add CNAME records to your Domain Name System (DNS). For each mapped domain name, add a mapping to the target App Runner subdomain and one or more certificate validation records. App Runner then performs DNS validation to verify that you own or control the domain name that you associated. App Runner tracks domain validity in a certificate stored in <a href="https://docs.aws.amazon.com/acm/latest/userguide">AWS Certificate Manager (ACM)</a>.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to associate a custom domain name with.</p>
            domain_name: <p>A custom domain endpoint to associate. Specify a root domain (for example, <code>example.com</code>), a subdomain (for example, <code>login.example.com</code> or <code>admin.login.example.com</code>), or a wildcard (for example, <code>*.example.com</code>).</p>
            enable_www_subdomain: <p>Set to <code>true</code> to associate the subdomain <code>www.<i>DomainName</i> </code> with the App Runner service in addition to the base domain.</p> <p>Default: <code>true</code> </p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.associate_custom_domain_request.AssociateCustomDomainRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.associate_custom_domain_response.AssociateCustomDomainResponse"
        ]:
            import capo_apprunner._operations.app_runner.associate_custom_domain

            output, http_response = (
                capo_apprunner._operations.app_runner.associate_custom_domain.associate_custom_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.associate_custom_domain_request.AssociateCustomDomainRequest = {
            "service_arn": service_arn,
            "domain_name": domain_name,
        }
        if enable_www_subdomain is not None:
            input_["enable_www_subdomain"] = enable_www_subdomain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_auto_scaling_configuration(
        self,
        auto_scaling_configuration_name: "capo_apprunner.types.auto_scaling_configuration_name.AutoScalingConfigurationName",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        max_concurrency: Optional[
            "capo_apprunner.types.as_config_max_concurrency.ASConfigMaxConcurrency"
        ] = None,
        min_size: Optional[
            "capo_apprunner.types.as_config_min_size.ASConfigMinSize"
        ] = None,
        max_size: Optional[
            "capo_apprunner.types.as_config_max_size.ASConfigMaxSize"
        ] = None,
        tags: Optional["capo_apprunner.types.tag_list.TagList"] = None,
    ) -> "capo_apprunner.types.create_auto_scaling_configuration_response.CreateAutoScalingConfigurationResponse":
        """<p>Create an App Runner automatic scaling configuration resource. App Runner requires this resource when you create or update App Runner services and you require non-default auto scaling settings. You can share an auto scaling configuration across multiple services.</p> <p>Create multiple revisions of a configuration by calling this action multiple times using the same <code>AutoScalingConfigurationName</code>. The call returns incremental <code>AutoScalingConfigurationRevision</code> values. When you create a service and configure an auto scaling configuration resource, the service uses the latest active revision of the auto scaling configuration by default. You can optionally configure the service to use a specific revision.</p> <p>Configure a higher <code>MinSize</code> to increase the spread of your App Runner service over more Availability Zones in the Amazon Web Services Region. The tradeoff is a higher minimal cost.</p> <p>Configure a lower <code>MaxSize</code> to control your cost. The tradeoff is lower responsiveness during peak demand.</p>

        Args:
            auto_scaling_configuration_name: <p>A name for the auto scaling configuration. When you use it for the first time in an Amazon Web Services Region, App Runner creates revision number <code>1</code> of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</p> <note> <p>Prior to the release of <a href="https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2023-09-22-auto-scale-config.html">Auto scale configuration enhancements</a>, the name <code>DefaultConfiguration</code> was reserved. </p> <p>This restriction is no longer in place. You can now manage <code>DefaultConfiguration</code> the same way you manage your custom auto scaling configurations. This means you can do the following with the <code>DefaultConfiguration</code> that App Runner provides:</p> <ul> <li> <p>Create new revisions of the <code>DefaultConfiguration</code>.</p> </li> <li> <p>Delete the revisions of the <code>DefaultConfiguration</code>.</p> </li> <li> <p>Delete the auto scaling configuration for which the App Runner <code>DefaultConfiguration</code> was created.</p> </li> <li> <p>If you delete the auto scaling configuration you can create another custom auto scaling configuration with the same <code>DefaultConfiguration</code> name. The original <code>DefaultConfiguration</code> resource provided by App Runner remains in your account unless you make changes to it.</p> </li> </ul> </note>
            max_concurrency: <p>The maximum number of concurrent requests that you want an instance to process. If the number of concurrent requests exceeds this limit, App Runner scales up your service.</p> <p>Default: <code>100</code> </p>
            min_size: <p>The minimum number of instances that App Runner provisions for your service. The service always has at least <code>MinSize</code> provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.</p> <p>App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.</p> <p>Default: <code>1</code> </p>
            max_size: <p>The maximum number of instances that your service scales up to. At most <code>MaxSize</code> instances actively serve traffic for your service.</p> <p>Default: <code>25</code> </p>
            tags: <p>A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>App Runner can't create this resource. You've reached your account quota for this resource type.</p> <p>For App Runner per-resource quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/apprunner.html">App Runner endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.create_auto_scaling_configuration_request.CreateAutoScalingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.create_auto_scaling_configuration_response.CreateAutoScalingConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.create_auto_scaling_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.create_auto_scaling_configuration.create_auto_scaling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.create_auto_scaling_configuration_request.CreateAutoScalingConfigurationRequest = {
            "auto_scaling_configuration_name": auto_scaling_configuration_name
        }
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if min_size is not None:
            input_["min_size"] = min_size
        if max_size is not None:
            input_["max_size"] = max_size
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connection(
        self,
        connection_name: "capo_apprunner.types.connection_name.ConnectionName",
        provider_type: "capo_apprunner.types.provider_type.ProviderType",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        tags: Optional["capo_apprunner.types.tag_list.TagList"] = None,
    ) -> "capo_apprunner.types.create_connection_response.CreateConnectionResponse":
        """<p>Create an App Runner connection resource. App Runner requires a connection resource when you create App Runner services that access private repositories from certain third-party providers. You can share a connection across multiple services.</p> <p>A connection resource is needed to access GitHub and Bitbucket repositories. Both require a user interface approval process through the App Runner console before you can use the connection.</p>

        Args:
            connection_name: <p>A name for the new connection. It must be unique across all App Runner connections for the Amazon Web Services account in the Amazon Web Services Region.</p>
            provider_type: <p>The source repository provider.</p>
            tags: <p>A list of metadata items that you can associate with your connection resource. A tag is a key-value pair.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>App Runner can't create this resource. You've reached your account quota for this resource type.</p> <p>For App Runner per-resource quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/apprunner.html">App Runner endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.create_connection_request.CreateConnectionRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.create_connection_response.CreateConnectionResponse"
        ]:
            import capo_apprunner._operations.app_runner.create_connection

            output, http_response = (
                capo_apprunner._operations.app_runner.create_connection.create_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.create_connection_request.CreateConnectionRequest = {
            "connection_name": connection_name,
            "provider_type": provider_type,
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

    def create_observability_configuration(
        self,
        observability_configuration_name: "capo_apprunner.types.observability_configuration_name.ObservabilityConfigurationName",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        trace_configuration: Optional[
            "capo_apprunner.types.trace_configuration.TraceConfiguration"
        ] = None,
        tags: Optional["capo_apprunner.types.tag_list.TagList"] = None,
    ) -> "capo_apprunner.types.create_observability_configuration_response.CreateObservabilityConfigurationResponse":
        """<p>Create an App Runner observability configuration resource. App Runner requires this resource when you create or update App Runner services and you want to enable non-default observability features. You can share an observability configuration across multiple services.</p> <p>Create multiple revisions of a configuration by calling this action multiple times using the same <code>ObservabilityConfigurationName</code>. The call returns incremental <code>ObservabilityConfigurationRevision</code> values. When you create a service and configure an observability configuration resource, the service uses the latest active revision of the observability configuration by default. You can optionally configure the service to use a specific revision.</p> <p>The observability configuration resource is designed to configure multiple features (currently one feature, tracing). This action takes optional parameters that describe the configuration of these features (currently one parameter, <code>TraceConfiguration</code>). If you don't specify a feature parameter, App Runner doesn't enable the feature.</p>

        Args:
            observability_configuration_name: <p>A name for the observability configuration. When you use it for the first time in an Amazon Web Services Region, App Runner creates revision number <code>1</code> of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</p> <note> <p>The name <code>DefaultConfiguration</code> is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it.</p> <p>When you want to use your own observability configuration for your App Runner service, <i>create a configuration with a different name</i>, and then provide it when you create or update your service.</p> </note>
            trace_configuration: <p>The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.</p>
            tags: <p>A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>App Runner can't create this resource. You've reached your account quota for this resource type.</p> <p>For App Runner per-resource quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/apprunner.html">App Runner endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.create_observability_configuration_request.CreateObservabilityConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.create_observability_configuration_response.CreateObservabilityConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.create_observability_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.create_observability_configuration.create_observability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.create_observability_configuration_request.CreateObservabilityConfigurationRequest = {
            "observability_configuration_name": observability_configuration_name
        }
        if trace_configuration is not None:
            input_["trace_configuration"] = trace_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_service(
        self,
        service_name: "capo_apprunner.types.service_name.ServiceName",
        source_configuration: "capo_apprunner.types.source_configuration.SourceConfiguration",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        instance_configuration: Optional[
            "capo_apprunner.types.instance_configuration.InstanceConfiguration"
        ] = None,
        tags: Optional["capo_apprunner.types.tag_list.TagList"] = None,
        encryption_configuration: Optional[
            "capo_apprunner.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        health_check_configuration: Optional[
            "capo_apprunner.types.health_check_configuration.HealthCheckConfiguration"
        ] = None,
        auto_scaling_configuration_arn: Optional[
            "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
        ] = None,
        network_configuration: Optional[
            "capo_apprunner.types.network_configuration.NetworkConfiguration"
        ] = None,
        observability_configuration: Optional[
            "capo_apprunner.types.service_observability_configuration.ServiceObservabilityConfiguration"
        ] = None,
    ) -> "capo_apprunner.types.create_service_response.CreateServiceResponse":
        """<p>Create an App Runner service. After the service is created, the action also automatically starts a deployment.</p> <p>This is an asynchronous operation. On a successful call, you can use the returned <code>OperationId</code> and the <a href="https://docs.aws.amazon.com/apprunner/latest/api/API_ListOperations.html">ListOperations</a> call to track the operation's progress.</p>

        Args:
            service_name: <p>A name for the App Runner service. It must be unique across all the running App Runner services in your Amazon Web Services account in the Amazon Web Services Region.</p>
            source_configuration: <p>The source to deploy to the App Runner service. It can be a code or an image repository.</p>
            instance_configuration: <p>The runtime configuration of instances (scaling units) of your service.</p>
            tags: <p>An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.</p>
            encryption_configuration: <p>An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an Amazon Web Services managed key.</p>
            health_check_configuration: <p>The settings for the health check that App Runner performs to monitor the health of the App Runner service.</p>
            auto_scaling_configuration_arn: <p>The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration.</p> <p>Specify an ARN with a name and a revision number to associate that revision. For example: <code>arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3</code> </p> <p>Specify just the name to associate the latest revision. For example: <code>arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability</code> </p>
            network_configuration: <p>Configuration settings related to network traffic of the web application that the App Runner service runs.</p>
            observability_configuration: <p>The observability configuration of your service.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>App Runner can't create this resource. You've reached your account quota for this resource type.</p> <p>For App Runner per-resource quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/apprunner.html">App Runner endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_apprunner._operations.app_runner.create_service

            output, http_response = (
                capo_apprunner._operations.app_runner.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.create_service_request.CreateServiceRequest = {
            "service_name": service_name,
            "source_configuration": source_configuration,
        }
        if instance_configuration is not None:
            input_["instance_configuration"] = instance_configuration
        if tags is not None:
            input_["tags"] = tags
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if health_check_configuration is not None:
            input_["health_check_configuration"] = health_check_configuration
        if auto_scaling_configuration_arn is not None:
            input_["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if observability_configuration is not None:
            input_["observability_configuration"] = observability_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_connector(
        self,
        vpc_connector_name: "capo_apprunner.types.vpc_connector_name.VpcConnectorName",
        subnets: "capo_apprunner.types.string_list.StringList",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        security_groups: Optional["capo_apprunner.types.string_list.StringList"] = None,
        tags: Optional["capo_apprunner.types.tag_list.TagList"] = None,
    ) -> (
        "capo_apprunner.types.create_vpc_connector_response.CreateVpcConnectorResponse"
    ):
        """<p>Create an App Runner VPC connector resource. App Runner requires this resource when you want to associate your App Runner service to a custom Amazon Virtual Private Cloud (Amazon VPC).</p>

        Args:
            vpc_connector_name: <p>A name for the VPC connector.</p>
            subnets: <p>A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.</p> <note> <p> App Runner only supports subnets of IP address type <i>IPv4</i> and <i>dual stack</i> (IPv4 and IPv6).</p> </note>
            security_groups: <p>A list of IDs of security groups that App Runner should use for access to Amazon Web Services resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.</p>
            tags: <p>A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>App Runner can't create this resource. You've reached your account quota for this resource type.</p> <p>For App Runner per-resource quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/apprunner.html">App Runner endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.create_vpc_connector_request.CreateVpcConnectorRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.create_vpc_connector_response.CreateVpcConnectorResponse"
        ]:
            import capo_apprunner._operations.app_runner.create_vpc_connector

            output, http_response = (
                capo_apprunner._operations.app_runner.create_vpc_connector.create_vpc_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.create_vpc_connector_request.CreateVpcConnectorRequest = {
            "vpc_connector_name": vpc_connector_name,
            "subnets": subnets,
        }
        if security_groups is not None:
            input_["security_groups"] = security_groups
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_ingress_connection(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        vpc_ingress_connection_name: "capo_apprunner.types.vpc_ingress_connection_name.VpcIngressConnectionName",
        ingress_vpc_configuration: "capo_apprunner.types.ingress_vpc_configuration.IngressVpcConfiguration",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        tags: Optional["capo_apprunner.types.tag_list.TagList"] = None,
    ) -> "capo_apprunner.types.create_vpc_ingress_connection_response.CreateVpcIngressConnectionResponse":
        """<p>Create an App Runner VPC Ingress Connection resource. App Runner requires this resource when you want to associate your App Runner service with an Amazon VPC endpoint.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.</p>
            vpc_ingress_connection_name: <p>A name for the VPC Ingress Connection resource. It must be unique across all the active VPC Ingress Connections in your Amazon Web Services account in the Amazon Web Services Region. </p>
            ingress_vpc_configuration: <p>Specifications for the customer’s Amazon VPC and the related Amazon Web Services PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.</p>
            tags: <p>An optional list of metadata items that you can associate with the VPC Ingress Connection resource. A tag is a key-value pair.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>App Runner can't create this resource. You've reached your account quota for this resource type.</p> <p>For App Runner per-resource quotas, see <a href="https://docs.aws.amazon.com/general/latest/gr/apprunner.html">App Runner endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.create_vpc_ingress_connection_request.CreateVpcIngressConnectionRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.create_vpc_ingress_connection_response.CreateVpcIngressConnectionResponse"
        ]:
            import capo_apprunner._operations.app_runner.create_vpc_ingress_connection

            output, http_response = (
                capo_apprunner._operations.app_runner.create_vpc_ingress_connection.create_vpc_ingress_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.create_vpc_ingress_connection_request.CreateVpcIngressConnectionRequest = {
            "service_arn": service_arn,
            "vpc_ingress_connection_name": vpc_ingress_connection_name,
            "ingress_vpc_configuration": ingress_vpc_configuration,
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

    def delete_auto_scaling_configuration(
        self,
        auto_scaling_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        delete_all_revisions: Optional["capo_apprunner.types.boolean.Boolean"] = None,
    ) -> "capo_apprunner.types.delete_auto_scaling_configuration_response.DeleteAutoScalingConfigurationResponse":
        """<p>Delete an App Runner automatic scaling configuration resource. You can delete a top level auto scaling configuration, a specific revision of one, or all revisions associated with the top level configuration. You can't delete the default auto scaling configuration or a configuration that's used by one or more App Runner services.</p>

        Args:
            auto_scaling_configuration_arn: <p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to delete.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is deleted.</p>
            delete_all_revisions: <p>Set to <code>true</code> to delete all of the revisions associated with the <code>AutoScalingConfigurationArn</code> parameter value.</p> <p>When <code>DeleteAllRevisions</code> is set to <code>true</code>, the only valid value for the Amazon Resource Name (ARN) is a partial ARN ending with: <code>.../name</code>.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.delete_auto_scaling_configuration_request.DeleteAutoScalingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.delete_auto_scaling_configuration_response.DeleteAutoScalingConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.delete_auto_scaling_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.delete_auto_scaling_configuration.delete_auto_scaling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.delete_auto_scaling_configuration_request.DeleteAutoScalingConfigurationRequest = {
            "auto_scaling_configuration_arn": auto_scaling_configuration_arn
        }
        if delete_all_revisions is not None:
            input_["delete_all_revisions"] = delete_all_revisions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connection(
        self,
        connection_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Delete an App Runner connection. You must first ensure that there are no running App Runner services that use this connection. If there are any, the <code>DeleteConnection</code> action fails.</p>

        Args:
            connection_arn: <p>The Amazon Resource Name (ARN) of the App Runner connection that you want to delete.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import capo_apprunner._operations.app_runner.delete_connection

            output, http_response = (
                capo_apprunner._operations.app_runner.delete_connection.delete_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.delete_connection_request.DeleteConnectionRequest = {
            "connection_arn": connection_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_observability_configuration(
        self,
        observability_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.delete_observability_configuration_response.DeleteObservabilityConfigurationResponse":
        """<p>Delete an App Runner observability configuration resource. You can delete a specific revision or the latest active revision. You can't delete a configuration that's used by one or more App Runner services.</p>

        Args:
            observability_configuration_arn: <p>The Amazon Resource Name (ARN) of the App Runner observability configuration that you want to delete.</p> <p>The ARN can be a full observability configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is deleted.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.delete_observability_configuration_request.DeleteObservabilityConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.delete_observability_configuration_response.DeleteObservabilityConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.delete_observability_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.delete_observability_configuration.delete_observability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.delete_observability_configuration_request.DeleteObservabilityConfigurationRequest = {
            "observability_configuration_arn": observability_configuration_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.delete_service_response.DeleteServiceResponse":
        """<p>Delete an App Runner service.</p> <p>This is an asynchronous operation. On a successful call, you can use the returned <code>OperationId</code> and the <a>ListOperations</a> call to track the operation's progress.</p> <note> <p>Make sure that you don't have any active VPCIngressConnections associated with the service you want to delete. </p> </note>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to delete.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_apprunner._operations.app_runner.delete_service

            output, http_response = (
                capo_apprunner._operations.app_runner.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.delete_service_request.DeleteServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_connector(
        self,
        vpc_connector_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> (
        "capo_apprunner.types.delete_vpc_connector_response.DeleteVpcConnectorResponse"
    ):
        """<p>Delete an App Runner VPC connector resource. You can't delete a connector that's used by one or more App Runner services.</p>

        Args:
            vpc_connector_arn: <p>The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to delete.</p> <p>The ARN must be a full VPC connector ARN.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.delete_vpc_connector_request.DeleteVpcConnectorRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.delete_vpc_connector_response.DeleteVpcConnectorResponse"
        ]:
            import capo_apprunner._operations.app_runner.delete_vpc_connector

            output, http_response = (
                capo_apprunner._operations.app_runner.delete_vpc_connector.delete_vpc_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.delete_vpc_connector_request.DeleteVpcConnectorRequest = {
            "vpc_connector_arn": vpc_connector_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_ingress_connection(
        self,
        vpc_ingress_connection_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.delete_vpc_ingress_connection_response.DeleteVpcIngressConnectionResponse":
        """<p>Delete an App Runner VPC Ingress Connection resource that's associated with an App Runner service. The VPC Ingress Connection must be in one of the following states to be deleted: </p> <ul> <li> <p> <code>AVAILABLE</code> </p> </li> <li> <p> <code>FAILED_CREATION</code> </p> </li> <li> <p> <code>FAILED_UPDATE</code> </p> </li> <li> <p> <code>FAILED_DELETION</code> </p> </li> </ul>

        Args:
            vpc_ingress_connection_arn: <p>The Amazon Resource Name (ARN) of the App Runner VPC Ingress Connection that you want to delete.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.delete_vpc_ingress_connection_request.DeleteVpcIngressConnectionRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.delete_vpc_ingress_connection_response.DeleteVpcIngressConnectionResponse"
        ]:
            import capo_apprunner._operations.app_runner.delete_vpc_ingress_connection

            output, http_response = (
                capo_apprunner._operations.app_runner.delete_vpc_ingress_connection.delete_vpc_ingress_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.delete_vpc_ingress_connection_request.DeleteVpcIngressConnectionRequest = {
            "vpc_ingress_connection_arn": vpc_ingress_connection_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_auto_scaling_configuration(
        self,
        auto_scaling_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.describe_auto_scaling_configuration_response.DescribeAutoScalingConfigurationResponse":
        """<p>Return a full description of an App Runner automatic scaling configuration resource.</p>

        Args:
            auto_scaling_configuration_arn: <p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want a description for.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is described.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.describe_auto_scaling_configuration_request.DescribeAutoScalingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.describe_auto_scaling_configuration_response.DescribeAutoScalingConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.describe_auto_scaling_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.describe_auto_scaling_configuration.describe_auto_scaling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.describe_auto_scaling_configuration_request.DescribeAutoScalingConfigurationRequest = {
            "auto_scaling_configuration_arn": auto_scaling_configuration_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_custom_domains(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        next_token: Optional["capo_apprunner.types.string.String"] = None,
        max_results: Optional[
            "capo_apprunner.types.describe_custom_domains_max_results.DescribeCustomDomainsMaxResults"
        ] = None,
    ) -> "capo_apprunner.types.describe_custom_domains_response.DescribeCustomDomainsResponse":
        """<p>Return a description of custom domain names that are associated with an App Runner service.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want associated custom domain names to be described for.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>
            max_results: <p>The maximum number of results that each response (result page) can include. It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.describe_custom_domains_request.DescribeCustomDomainsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.describe_custom_domains_response.DescribeCustomDomainsResponse"
        ]:
            import capo_apprunner._operations.app_runner.describe_custom_domains

            output, http_response = (
                capo_apprunner._operations.app_runner.describe_custom_domains.describe_custom_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.describe_custom_domains_request.DescribeCustomDomainsRequest = {
            "service_arn": service_arn
        }
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

    def iter_describe_custom_domains(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        next_token: Optional["capo_apprunner.types.string.String"] = None,
        max_results: Optional[
            "capo_apprunner.types.describe_custom_domains_max_results.DescribeCustomDomainsMaxResults"
        ] = None,
    ) -> "Iterator[capo_apprunner.types.describe_custom_domains_response.DescribeCustomDomainsResponse]":
        _token = next_token
        while True:
            _response = self.describe_custom_domains(
                service_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_observability_configuration(
        self,
        observability_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.describe_observability_configuration_response.DescribeObservabilityConfigurationResponse":
        """<p>Return a full description of an App Runner observability configuration resource.</p>

        Args:
            observability_configuration_arn: <p>The Amazon Resource Name (ARN) of the App Runner observability configuration that you want a description for.</p> <p>The ARN can be a full observability configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is described.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.describe_observability_configuration_request.DescribeObservabilityConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.describe_observability_configuration_response.DescribeObservabilityConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.describe_observability_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.describe_observability_configuration.describe_observability_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.describe_observability_configuration_request.DescribeObservabilityConfigurationRequest = {
            "observability_configuration_arn": observability_configuration_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_service(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.describe_service_response.DescribeServiceResponse":
        """<p>Return a full description of an App Runner service.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want a description for.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.describe_service_request.DescribeServiceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.describe_service_response.DescribeServiceResponse"
        ]:
            import capo_apprunner._operations.app_runner.describe_service

            output, http_response = (
                capo_apprunner._operations.app_runner.describe_service.describe_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.describe_service_request.DescribeServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vpc_connector(
        self,
        vpc_connector_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.describe_vpc_connector_response.DescribeVpcConnectorResponse":
        """<p>Return a description of an App Runner VPC connector resource.</p>

        Args:
            vpc_connector_arn: <p>The Amazon Resource Name (ARN) of the App Runner VPC connector that you want a description for.</p> <p>The ARN must be a full VPC connector ARN.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.describe_vpc_connector_request.DescribeVpcConnectorRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.describe_vpc_connector_response.DescribeVpcConnectorResponse"
        ]:
            import capo_apprunner._operations.app_runner.describe_vpc_connector

            output, http_response = (
                capo_apprunner._operations.app_runner.describe_vpc_connector.describe_vpc_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.describe_vpc_connector_request.DescribeVpcConnectorRequest = {
            "vpc_connector_arn": vpc_connector_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vpc_ingress_connection(
        self,
        vpc_ingress_connection_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.describe_vpc_ingress_connection_response.DescribeVpcIngressConnectionResponse":
        """<p>Return a full description of an App Runner VPC Ingress Connection resource.</p>

        Args:
            vpc_ingress_connection_arn: <p>The Amazon Resource Name (ARN) of the App Runner VPC Ingress Connection that you want a description for.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.describe_vpc_ingress_connection_request.DescribeVpcIngressConnectionRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.describe_vpc_ingress_connection_response.DescribeVpcIngressConnectionResponse"
        ]:
            import capo_apprunner._operations.app_runner.describe_vpc_ingress_connection

            output, http_response = (
                capo_apprunner._operations.app_runner.describe_vpc_ingress_connection.describe_vpc_ingress_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.describe_vpc_ingress_connection_request.DescribeVpcIngressConnectionRequest = {
            "vpc_ingress_connection_arn": vpc_ingress_connection_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_custom_domain(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        domain_name: "capo_apprunner.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.disassociate_custom_domain_response.DisassociateCustomDomainResponse":
        """<p>Disassociate a custom domain name from an App Runner service.</p> <p>Certificates tracking domain validity are associated with a custom domain and are stored in <a href="https://docs.aws.amazon.com/acm/latest/userguide">AWS Certificate Manager (ACM)</a>. These certificates aren't deleted as part of this action. App Runner delays certificate deletion for 30 days after a domain is disassociated from your service.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to disassociate a custom domain name from.</p>
            domain_name: <p>The domain name that you want to disassociate from the App Runner service.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.disassociate_custom_domain_request.DisassociateCustomDomainRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.disassociate_custom_domain_response.DisassociateCustomDomainResponse"
        ]:
            import capo_apprunner._operations.app_runner.disassociate_custom_domain

            output, http_response = (
                capo_apprunner._operations.app_runner.disassociate_custom_domain.disassociate_custom_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.disassociate_custom_domain_request.DisassociateCustomDomainRequest = {
            "service_arn": service_arn,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_auto_scaling_configurations(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        auto_scaling_configuration_name: Optional[
            "capo_apprunner.types.auto_scaling_configuration_name.AutoScalingConfigurationName"
        ] = None,
        latest_only: Optional["capo_apprunner.types.boolean.Boolean"] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "capo_apprunner.types.list_auto_scaling_configurations_response.ListAutoScalingConfigurationsResponse":
        """<p>Returns a list of active App Runner automatic scaling configurations in your Amazon Web Services account. You can query the revisions for a specific configuration name or the revisions for all active configurations in your account. You can optionally query only the latest revision of each requested name.</p> <p>To retrieve a full description of a particular configuration revision, call and provide one of the ARNs returned by <code>ListAutoScalingConfigurations</code>.</p>

        Args:
            auto_scaling_configuration_name: <p>The name of the App Runner auto scaling configuration that you want to list. If specified, App Runner lists revisions that share this name. If not specified, App Runner returns revisions of all active configurations.</p>
            latest_only: <p>Set to <code>true</code> to list only the latest revision for each requested configuration name.</p> <p>Set to <code>false</code> to list all revisions for each requested configuration name.</p> <p>Default: <code>true</code> </p>
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_auto_scaling_configurations_request.ListAutoScalingConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_auto_scaling_configurations_response.ListAutoScalingConfigurationsResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_auto_scaling_configurations

            output, http_response = (
                capo_apprunner._operations.app_runner.list_auto_scaling_configurations.list_auto_scaling_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_auto_scaling_configurations_request.ListAutoScalingConfigurationsRequest = {}
        if auto_scaling_configuration_name is not None:
            input_["auto_scaling_configuration_name"] = auto_scaling_configuration_name
        if latest_only is not None:
            input_["latest_only"] = latest_only
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

    def iter_list_auto_scaling_configurations(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        auto_scaling_configuration_name: Optional[
            "capo_apprunner.types.auto_scaling_configuration_name.AutoScalingConfigurationName"
        ] = None,
        latest_only: Optional["capo_apprunner.types.boolean.Boolean"] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_apprunner.types.list_auto_scaling_configurations_response.ListAutoScalingConfigurationsResponse]":
        _token = next_token
        while True:
            _response = self.list_auto_scaling_configurations(
                config_overrides=config_overrides,
                auto_scaling_configuration_name=auto_scaling_configuration_name,
                latest_only=latest_only,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_connections(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        connection_name: Optional[
            "capo_apprunner.types.connection_name.ConnectionName"
        ] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "capo_apprunner.types.list_connections_response.ListConnectionsResponse":
        """<p>Returns a list of App Runner connections that are associated with your Amazon Web Services account.</p>

        Args:
            connection_name: <p>If specified, only this connection is returned. If not specified, the result isn't filtered by name.</p>
            max_results: <p>The maximum number of results to include in each response (result page). Used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>
            next_token: <p>A token from a previous result page. Used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_connections_request.ListConnectionsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_connections_response.ListConnectionsResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_connections

            output, http_response = (
                capo_apprunner._operations.app_runner.list_connections.list_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_connections_request.ListConnectionsRequest = {}
        if connection_name is not None:
            input_["connection_name"] = connection_name
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

    def iter_list_connections(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        connection_name: Optional[
            "capo_apprunner.types.connection_name.ConnectionName"
        ] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_apprunner.types.list_connections_response.ListConnectionsResponse]":
        _token = next_token
        while True:
            _response = self.list_connections(
                config_overrides=config_overrides,
                connection_name=connection_name,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_observability_configurations(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        observability_configuration_name: Optional[
            "capo_apprunner.types.observability_configuration_name.ObservabilityConfigurationName"
        ] = None,
        latest_only: Optional["capo_apprunner.types.boolean.Boolean"] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "capo_apprunner.types.list_observability_configurations_response.ListObservabilityConfigurationsResponse":
        """<p>Returns a list of active App Runner observability configurations in your Amazon Web Services account. You can query the revisions for a specific configuration name or the revisions for all active configurations in your account. You can optionally query only the latest revision of each requested name.</p> <p>To retrieve a full description of a particular configuration revision, call and provide one of the ARNs returned by <code>ListObservabilityConfigurations</code>.</p>

        Args:
            observability_configuration_name: <p>The name of the App Runner observability configuration that you want to list. If specified, App Runner lists revisions that share this name. If not specified, App Runner returns revisions of all active configurations.</p>
            latest_only: <p>Set to <code>true</code> to list only the latest revision for each requested configuration name.</p> <p>Set to <code>false</code> to list all revisions for each requested configuration name.</p> <p>Default: <code>true</code> </p>
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_observability_configurations_request.ListObservabilityConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_observability_configurations_response.ListObservabilityConfigurationsResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_observability_configurations

            output, http_response = (
                capo_apprunner._operations.app_runner.list_observability_configurations.list_observability_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_observability_configurations_request.ListObservabilityConfigurationsRequest = {}
        if observability_configuration_name is not None:
            input_["observability_configuration_name"] = (
                observability_configuration_name
            )
        if latest_only is not None:
            input_["latest_only"] = latest_only
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

    def iter_list_observability_configurations(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        observability_configuration_name: Optional[
            "capo_apprunner.types.observability_configuration_name.ObservabilityConfigurationName"
        ] = None,
        latest_only: Optional["capo_apprunner.types.boolean.Boolean"] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_apprunner.types.list_observability_configurations_response.ListObservabilityConfigurationsResponse]":
        _token = next_token
        while True:
            _response = self.list_observability_configurations(
                config_overrides=config_overrides,
                observability_configuration_name=observability_configuration_name,
                latest_only=latest_only,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_operations(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        next_token: Optional["capo_apprunner.types.string.String"] = None,
        max_results: Optional[
            "capo_apprunner.types.list_operations_max_results.ListOperationsMaxResults"
        ] = None,
    ) -> "capo_apprunner.types.list_operations_response.ListOperationsResponse":
        """<p>Return a list of operations that occurred on an App Runner service.</p> <p>The resulting list of <a>OperationSummary</a> objects is sorted in reverse chronological order. The first object on the list represents the last started operation.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want a list of operations for.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_operations_request.ListOperationsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_operations_response.ListOperationsResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_operations

            output, http_response = (
                capo_apprunner._operations.app_runner.list_operations.list_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_operations_request.ListOperationsRequest = {
            "service_arn": service_arn
        }
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

    def iter_list_operations(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        next_token: Optional["capo_apprunner.types.string.String"] = None,
        max_results: Optional[
            "capo_apprunner.types.list_operations_max_results.ListOperationsMaxResults"
        ] = None,
    ) -> (
        "Iterator[capo_apprunner.types.list_operations_response.ListOperationsResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_operations(
                service_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        next_token: Optional["capo_apprunner.types.string.String"] = None,
        max_results: Optional[
            "capo_apprunner.types.service_max_results.ServiceMaxResults"
        ] = None,
    ) -> "capo_apprunner.types.list_services_response.ListServicesResponse":
        """<p>Returns a list of running App Runner services in your Amazon Web Services account.</p>

        Args:
            next_token: <p>A token from a previous result page. Used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_services_response.ListServicesResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_services

            output, http_response = (
                capo_apprunner._operations.app_runner.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_services_request.ListServicesRequest = {}
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

    def iter_list_services(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        next_token: Optional["capo_apprunner.types.string.String"] = None,
        max_results: Optional[
            "capo_apprunner.types.service_max_results.ServiceMaxResults"
        ] = None,
    ) -> "Iterator[capo_apprunner.types.list_services_response.ListServicesResponse]":
        _token = next_token
        while True:
            _response = self.list_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services_for_auto_scaling_configuration(
        self,
        auto_scaling_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "capo_apprunner.types.list_services_for_auto_scaling_configuration_response.ListServicesForAutoScalingConfigurationResponse":
        """<p>Returns a list of the associated App Runner services using an auto scaling configuration.</p>

        Args:
            auto_scaling_configuration_arn: <p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to list the services for.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is used.</p>
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_services_for_auto_scaling_configuration_request.ListServicesForAutoScalingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_services_for_auto_scaling_configuration_response.ListServicesForAutoScalingConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_services_for_auto_scaling_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.list_services_for_auto_scaling_configuration.list_services_for_auto_scaling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_services_for_auto_scaling_configuration_request.ListServicesForAutoScalingConfigurationRequest = {
            "auto_scaling_configuration_arn": auto_scaling_configuration_arn
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

    def iter_list_services_for_auto_scaling_configuration(
        self,
        auto_scaling_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_apprunner.types.list_services_for_auto_scaling_configuration_response.ListServicesForAutoScalingConfigurationResponse]":
        _token = next_token
        while True:
            _response = self.list_services_for_auto_scaling_configuration(
                auto_scaling_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List tags that are associated with for an App Runner resource. The response contains a list of tag key-value pairs.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that a tag list is requested for.</p> <p>It must be the ARN of an App Runner resource.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_tags_for_resource

            output, http_response = (
                capo_apprunner._operations.app_runner.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vpc_connectors(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "capo_apprunner.types.list_vpc_connectors_response.ListVpcConnectorsResponse":
        """<p>Returns a list of App Runner VPC connectors in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_vpc_connectors_request.ListVpcConnectorsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_vpc_connectors_response.ListVpcConnectorsResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_vpc_connectors

            output, http_response = (
                capo_apprunner._operations.app_runner.list_vpc_connectors.list_vpc_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_vpc_connectors_request.ListVpcConnectorsRequest = {}
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

    def iter_list_vpc_connectors(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_apprunner.types.list_vpc_connectors_response.ListVpcConnectorsResponse]":
        _token = next_token
        while True:
            _response = self.list_vpc_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_vpc_ingress_connections(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        filter: Optional[
            "capo_apprunner.types.list_vpc_ingress_connections_filter.ListVpcIngressConnectionsFilter"
        ] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "capo_apprunner.types.list_vpc_ingress_connections_response.ListVpcIngressConnectionsResponse":
        """<p>Return a list of App Runner VPC Ingress Connections in your Amazon Web Services account.</p>

        Args:
            filter: <p>The VPC Ingress Connections to be listed based on either the Service Arn or Vpc Endpoint Id, or both.</p>
            max_results: <p>The maximum number of results to include in each response (result page). It's used for a paginated request.</p> <p>If you don't specify <code>MaxResults</code>, the request retrieves all available results in a single response.</p>
            next_token: <p>A token from a previous result page. It's used for a paginated request. The request retrieves the next result page. All other parameter values must be identical to the ones that are specified in the initial request.</p> <p>If you don't specify <code>NextToken</code>, the request retrieves the first result page.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.list_vpc_ingress_connections_request.ListVpcIngressConnectionsRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.list_vpc_ingress_connections_response.ListVpcIngressConnectionsResponse"
        ]:
            import capo_apprunner._operations.app_runner.list_vpc_ingress_connections

            output, http_response = (
                capo_apprunner._operations.app_runner.list_vpc_ingress_connections.list_vpc_ingress_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.list_vpc_ingress_connections_request.ListVpcIngressConnectionsRequest = {}
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_vpc_ingress_connections(
        self,
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        filter: Optional[
            "capo_apprunner.types.list_vpc_ingress_connections_filter.ListVpcIngressConnectionsFilter"
        ] = None,
        max_results: Optional["capo_apprunner.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apprunner.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_apprunner.types.list_vpc_ingress_connections_response.ListVpcIngressConnectionsResponse]":
        _token = next_token
        while True:
            _response = self.list_vpc_ingress_connections(
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def pause_service(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.pause_service_response.PauseServiceResponse":
        """<p>Pause an active App Runner service. App Runner reduces compute capacity for the service to zero and loses state (for example, ephemeral storage is removed).</p> <p>This is an asynchronous operation. On a successful call, you can use the returned <code>OperationId</code> and the <a>ListOperations</a> call to track the operation's progress.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to pause.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.pause_service_request.PauseServiceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.pause_service_response.PauseServiceResponse"
        ]:
            import capo_apprunner._operations.app_runner.pause_service

            output, http_response = (
                capo_apprunner._operations.app_runner.pause_service.pause_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.pause_service_request.PauseServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resume_service(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.resume_service_response.ResumeServiceResponse":
        """<p>Resume an active App Runner service. App Runner provisions compute capacity for the service.</p> <p>This is an asynchronous operation. On a successful call, you can use the returned <code>OperationId</code> and the <a>ListOperations</a> call to track the operation's progress.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to resume.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.resume_service_request.ResumeServiceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.resume_service_response.ResumeServiceResponse"
        ]:
            import capo_apprunner._operations.app_runner.resume_service

            output, http_response = (
                capo_apprunner._operations.app_runner.resume_service.resume_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.resume_service_request.ResumeServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_deployment(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.start_deployment_response.StartDeploymentResponse":
        """<p>Initiate a manual deployment of the latest commit in a source code repository or the latest image in a source image repository to an App Runner service.</p> <p>For a source code repository, App Runner retrieves the commit and builds a Docker image. For a source image repository, App Runner retrieves the latest Docker image. In both cases, App Runner then deploys the new image to your service and starts a new container instance.</p> <p>This is an asynchronous operation. On a successful call, you can use the returned <code>OperationId</code> and the <a>ListOperations</a> call to track the operation's progress.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to manually deploy to.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.start_deployment_request.StartDeploymentRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.start_deployment_response.StartDeploymentResponse"
        ]:
            import capo_apprunner._operations.app_runner.start_deployment

            output, http_response = (
                capo_apprunner._operations.app_runner.start_deployment.start_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.start_deployment_request.StartDeploymentRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        tags: "capo_apprunner.types.tag_list.TagList",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.tag_resource_response.TagResourceResponse":
        """<p>Add tags to, or update the tag values of, an App Runner resource. A tag is a key-value pair.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to update tags for.</p> <p>It must be the ARN of an App Runner resource.</p>
            tags: <p>A list of tag key-value pairs to add or update. If a key is new to the resource, the tag is added with the provided value. If a key is already associated with the resource, the value of the tag is updated.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_apprunner._operations.app_runner.tag_resource

            output, http_response = (
                capo_apprunner._operations.app_runner.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        tag_keys: "capo_apprunner.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from an App Runner resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p> <p>It must be the ARN of an App Runner resource.</p>
            tag_keys: <p>A list of tag keys that you want to remove.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_apprunner._operations.app_runner.untag_resource

            output, http_response = (
                capo_apprunner._operations.app_runner.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.untag_resource_request.UntagResourceRequest = {
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

    def update_default_auto_scaling_configuration(
        self,
        auto_scaling_configuration_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.update_default_auto_scaling_configuration_response.UpdateDefaultAutoScalingConfigurationResponse":
        """<p>Update an auto scaling configuration to be the default. The existing default auto scaling configuration will be set to non-default automatically.</p>

        Args:
            auto_scaling_configuration_arn: <p>The Amazon Resource Name (ARN) of the App Runner auto scaling configuration that you want to set as the default.</p> <p>The ARN can be a full auto scaling configuration ARN, or a partial ARN ending with either <code>.../<i>name</i> </code> or <code>.../<i>name</i>/<i>revision</i> </code>. If a revision isn't specified, the latest active revision is set as the default.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.update_default_auto_scaling_configuration_request.UpdateDefaultAutoScalingConfigurationRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.update_default_auto_scaling_configuration_response.UpdateDefaultAutoScalingConfigurationResponse"
        ]:
            import capo_apprunner._operations.app_runner.update_default_auto_scaling_configuration

            output, http_response = (
                capo_apprunner._operations.app_runner.update_default_auto_scaling_configuration.update_default_auto_scaling_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.update_default_auto_scaling_configuration_request.UpdateDefaultAutoScalingConfigurationRequest = {
            "auto_scaling_configuration_arn": auto_scaling_configuration_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service(
        self,
        service_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
        source_configuration: Optional[
            "capo_apprunner.types.source_configuration.SourceConfiguration"
        ] = None,
        instance_configuration: Optional[
            "capo_apprunner.types.instance_configuration.InstanceConfiguration"
        ] = None,
        auto_scaling_configuration_arn: Optional[
            "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
        ] = None,
        health_check_configuration: Optional[
            "capo_apprunner.types.health_check_configuration.HealthCheckConfiguration"
        ] = None,
        network_configuration: Optional[
            "capo_apprunner.types.network_configuration.NetworkConfiguration"
        ] = None,
        observability_configuration: Optional[
            "capo_apprunner.types.service_observability_configuration.ServiceObservabilityConfiguration"
        ] = None,
    ) -> "capo_apprunner.types.update_service_response.UpdateServiceResponse":
        """<p>Update an App Runner service. You can update the source configuration and instance configuration of the service. You can also update the ARN of the auto scaling configuration resource that's associated with the service. However, you can't change the name or the encryption configuration of the service. These can be set only when you create the service.</p> <p>To update the tags applied to your service, use the separate actions <a>TagResource</a> and <a>UntagResource</a>.</p> <p>This is an asynchronous operation. On a successful call, you can use the returned <code>OperationId</code> and the <a>ListOperations</a> call to track the operation's progress.</p>

        Args:
            service_arn: <p>The Amazon Resource Name (ARN) of the App Runner service that you want to update.</p>
            source_configuration: <p>The source configuration to apply to the App Runner service.</p> <p>You can change the configuration of the code or image repository that the service uses. However, you can't switch from code to image or the other way around. This means that you must provide the same structure member of <code>SourceConfiguration</code> that you originally included when you created the service. Specifically, you can include either <code>CodeRepository</code> or <code>ImageRepository</code>. To update the source configuration, set the values to members of the structure that you include.</p>
            instance_configuration: <p>The runtime configuration to apply to instances (scaling units) of your service.</p>
            auto_scaling_configuration_arn: <p>The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with the App Runner service.</p>
            health_check_configuration: <p>The settings for the health check that App Runner performs to monitor the health of the App Runner service.</p>
            network_configuration: <p>Configuration settings related to network traffic of the web application that the App Runner service runs.</p>
            observability_configuration: <p>The observability configuration of your service.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_apprunner._operations.app_runner.update_service

            output, http_response = (
                capo_apprunner._operations.app_runner.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.update_service_request.UpdateServiceRequest = {
            "service_arn": service_arn
        }
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if instance_configuration is not None:
            input_["instance_configuration"] = instance_configuration
        if auto_scaling_configuration_arn is not None:
            input_["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if health_check_configuration is not None:
            input_["health_check_configuration"] = health_check_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if observability_configuration is not None:
            input_["observability_configuration"] = observability_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_ingress_connection(
        self,
        vpc_ingress_connection_arn: "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn",
        ingress_vpc_configuration: "capo_apprunner.types.ingress_vpc_configuration.IngressVpcConfiguration",
        *,
        config_overrides: Optional[AppRunnerClientConfig] = None,
    ) -> "capo_apprunner.types.update_vpc_ingress_connection_response.UpdateVpcIngressConnectionResponse":
        """<p>Update an existing App Runner VPC Ingress Connection resource. The VPC Ingress Connection must be in one of the following states to be updated:</p> <ul> <li> <p> AVAILABLE </p> </li> <li> <p> FAILED_CREATION </p> </li> <li> <p> FAILED_UPDATE </p> </li> </ul>

        Args:
            vpc_ingress_connection_arn: <p>The Amazon Resource Name (Arn) for the App Runner VPC Ingress Connection resource that you want to update.</p>
            ingress_vpc_configuration: <p>Specifications for the customer’s Amazon VPC and the related Amazon Web Services PrivateLink VPC endpoint that are used to update the VPC Ingress Connection resource.</p>

        Raises:
            capo_apprunner.errors.internal_service_error_exception.InternalServiceErrorException: <p>An unexpected service exception occurred.</p>
            capo_apprunner.errors.invalid_request_exception.InvalidRequestException: <p>One or more input parameters aren't valid. Refer to the API action's document page, correct the input parameters, and try the action again.</p>
            capo_apprunner.errors.invalid_state_exception.InvalidStateException: <p>You can't perform this action when the resource is in its current state.</p>
            capo_apprunner.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource doesn't exist for the specified Amazon Resource Name (ARN) in your Amazon Web Services account.</p>
            capo_apprunner.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apprunner.types.update_vpc_ingress_connection_request.UpdateVpcIngressConnectionRequest]",
        ) -> OperationResponse[
            "capo_apprunner.types.update_vpc_ingress_connection_response.UpdateVpcIngressConnectionResponse"
        ]:
            import capo_apprunner._operations.app_runner.update_vpc_ingress_connection

            output, http_response = (
                capo_apprunner._operations.app_runner.update_vpc_ingress_connection.update_vpc_ingress_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apprunner.types.update_vpc_ingress_connection_request.UpdateVpcIngressConnectionRequest = {
            "vpc_ingress_connection_arn": vpc_ingress_connection_arn,
            "ingress_vpc_configuration": ingress_vpc_configuration,
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
