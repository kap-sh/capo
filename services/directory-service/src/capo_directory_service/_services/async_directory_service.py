"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryService_20150416``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_directory_service._auth._signers
import capo_directory_service._auth._sigv4
from capo_directory_service._auth._identity import Credentials
from capo_directory_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_directory_service._auth._zapros_handler import AuthMiddleware
from capo_directory_service._pagination import resolve_path as _resolve_path
from capo_directory_service._services._aws_config import aaws_config
from capo_directory_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_directory_service.types.accept_shared_directory_request
    import capo_directory_service.types.accept_shared_directory_result
    import capo_directory_service.types.add_ip_routes_request
    import capo_directory_service.types.add_ip_routes_result
    import capo_directory_service.types.add_region_request
    import capo_directory_service.types.add_region_result
    import capo_directory_service.types.add_tags_to_resource_request
    import capo_directory_service.types.add_tags_to_resource_result
    import capo_directory_service.types.alias_name
    import capo_directory_service.types.assessment_configuration
    import capo_directory_service.types.assessment_id
    import capo_directory_service.types.assessment_limit
    import capo_directory_service.types.assessment_summary
    import capo_directory_service.types.attributes
    import capo_directory_service.types.cancel_schema_extension_request
    import capo_directory_service.types.cancel_schema_extension_result
    import capo_directory_service.types.certificate_data
    import capo_directory_service.types.certificate_id
    import capo_directory_service.types.certificate_info
    import capo_directory_service.types.certificate_type
    import capo_directory_service.types.cidr_ips
    import capo_directory_service.types.cidr_ipv6s
    import capo_directory_service.types.client_authentication_setting_info
    import capo_directory_service.types.client_authentication_type
    import capo_directory_service.types.client_cert_auth_settings
    import capo_directory_service.types.computer_name
    import capo_directory_service.types.computer_password
    import capo_directory_service.types.connect_directory_request
    import capo_directory_service.types.connect_directory_result
    import capo_directory_service.types.connect_password
    import capo_directory_service.types.create_alias_request
    import capo_directory_service.types.create_alias_result
    import capo_directory_service.types.create_computer_request
    import capo_directory_service.types.create_computer_result
    import capo_directory_service.types.create_conditional_forwarder_request
    import capo_directory_service.types.create_conditional_forwarder_result
    import capo_directory_service.types.create_directory_request
    import capo_directory_service.types.create_directory_result
    import capo_directory_service.types.create_hybrid_ad_request
    import capo_directory_service.types.create_hybrid_ad_result
    import capo_directory_service.types.create_log_subscription_request
    import capo_directory_service.types.create_log_subscription_result
    import capo_directory_service.types.create_microsoft_ad_request
    import capo_directory_service.types.create_microsoft_ad_result
    import capo_directory_service.types.create_snapshot_before_schema_extension
    import capo_directory_service.types.create_snapshot_before_update
    import capo_directory_service.types.create_snapshot_request
    import capo_directory_service.types.create_snapshot_result
    import capo_directory_service.types.create_trust_request
    import capo_directory_service.types.create_trust_result
    import capo_directory_service.types.customer_user_name
    import capo_directory_service.types.delete_ad_assessment_request
    import capo_directory_service.types.delete_ad_assessment_result
    import capo_directory_service.types.delete_associated_conditional_forwarder
    import capo_directory_service.types.delete_conditional_forwarder_request
    import capo_directory_service.types.delete_conditional_forwarder_result
    import capo_directory_service.types.delete_directory_request
    import capo_directory_service.types.delete_directory_result
    import capo_directory_service.types.delete_log_subscription_request
    import capo_directory_service.types.delete_log_subscription_result
    import capo_directory_service.types.delete_snapshot_request
    import capo_directory_service.types.delete_snapshot_result
    import capo_directory_service.types.delete_trust_request
    import capo_directory_service.types.delete_trust_result
    import capo_directory_service.types.deregister_certificate_request
    import capo_directory_service.types.deregister_certificate_result
    import capo_directory_service.types.deregister_event_topic_request
    import capo_directory_service.types.deregister_event_topic_result
    import capo_directory_service.types.describe_ad_assessment_request
    import capo_directory_service.types.describe_ad_assessment_result
    import capo_directory_service.types.describe_ca_enrollment_policy_request
    import capo_directory_service.types.describe_ca_enrollment_policy_result
    import capo_directory_service.types.describe_certificate_request
    import capo_directory_service.types.describe_certificate_result
    import capo_directory_service.types.describe_client_authentication_settings_request
    import capo_directory_service.types.describe_client_authentication_settings_result
    import capo_directory_service.types.describe_conditional_forwarders_request
    import capo_directory_service.types.describe_conditional_forwarders_result
    import capo_directory_service.types.describe_directories_request
    import capo_directory_service.types.describe_directories_result
    import capo_directory_service.types.describe_directory_data_access_request
    import capo_directory_service.types.describe_directory_data_access_result
    import capo_directory_service.types.describe_domain_controllers_request
    import capo_directory_service.types.describe_domain_controllers_result
    import capo_directory_service.types.describe_event_topics_request
    import capo_directory_service.types.describe_event_topics_result
    import capo_directory_service.types.describe_hybrid_ad_update_request
    import capo_directory_service.types.describe_hybrid_ad_update_result
    import capo_directory_service.types.describe_ldaps_settings_request
    import capo_directory_service.types.describe_ldaps_settings_result
    import capo_directory_service.types.describe_regions_request
    import capo_directory_service.types.describe_regions_result
    import capo_directory_service.types.describe_settings_request
    import capo_directory_service.types.describe_settings_result
    import capo_directory_service.types.describe_shared_directories_request
    import capo_directory_service.types.describe_shared_directories_result
    import capo_directory_service.types.describe_snapshots_request
    import capo_directory_service.types.describe_snapshots_result
    import capo_directory_service.types.describe_trusts_request
    import capo_directory_service.types.describe_trusts_result
    import capo_directory_service.types.describe_update_directory_request
    import capo_directory_service.types.describe_update_directory_result
    import capo_directory_service.types.description
    import capo_directory_service.types.desired_number_of_domain_controllers
    import capo_directory_service.types.directory_configuration_status
    import capo_directory_service.types.directory_connect_settings
    import capo_directory_service.types.directory_description
    import capo_directory_service.types.directory_edition
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.directory_ids
    import capo_directory_service.types.directory_name
    import capo_directory_service.types.directory_short_name
    import capo_directory_service.types.directory_size
    import capo_directory_service.types.directory_size_update_settings
    import capo_directory_service.types.directory_vpc_settings
    import capo_directory_service.types.disable_ca_enrollment_policy_request
    import capo_directory_service.types.disable_ca_enrollment_policy_result
    import capo_directory_service.types.disable_client_authentication_request
    import capo_directory_service.types.disable_client_authentication_result
    import capo_directory_service.types.disable_directory_data_access_request
    import capo_directory_service.types.disable_directory_data_access_result
    import capo_directory_service.types.disable_ldaps_request
    import capo_directory_service.types.disable_ldaps_result
    import capo_directory_service.types.disable_radius_request
    import capo_directory_service.types.disable_radius_result
    import capo_directory_service.types.disable_sso_request
    import capo_directory_service.types.disable_sso_result
    import capo_directory_service.types.dns_ip_addrs
    import capo_directory_service.types.dns_ipv6_addrs
    import capo_directory_service.types.domain_controller_ids
    import capo_directory_service.types.enable_ca_enrollment_policy_request
    import capo_directory_service.types.enable_ca_enrollment_policy_result
    import capo_directory_service.types.enable_client_authentication_request
    import capo_directory_service.types.enable_client_authentication_result
    import capo_directory_service.types.enable_directory_data_access_request
    import capo_directory_service.types.enable_directory_data_access_result
    import capo_directory_service.types.enable_ldaps_request
    import capo_directory_service.types.enable_ldaps_result
    import capo_directory_service.types.enable_radius_request
    import capo_directory_service.types.enable_radius_result
    import capo_directory_service.types.enable_sso_request
    import capo_directory_service.types.enable_sso_result
    import capo_directory_service.types.get_directory_limits_request
    import capo_directory_service.types.get_directory_limits_result
    import capo_directory_service.types.get_snapshot_limits_request
    import capo_directory_service.types.get_snapshot_limits_result
    import capo_directory_service.types.hybrid_administrator_account_update
    import capo_directory_service.types.hybrid_customer_instances_settings
    import capo_directory_service.types.hybrid_update_type
    import capo_directory_service.types.ip_route_info
    import capo_directory_service.types.ip_routes
    import capo_directory_service.types.ldaps_setting_info
    import capo_directory_service.types.ldaps_type
    import capo_directory_service.types.ldif_content
    import capo_directory_service.types.limit
    import capo_directory_service.types.list_ad_assessments_request
    import capo_directory_service.types.list_ad_assessments_result
    import capo_directory_service.types.list_certificates_request
    import capo_directory_service.types.list_certificates_result
    import capo_directory_service.types.list_ip_routes_request
    import capo_directory_service.types.list_ip_routes_result
    import capo_directory_service.types.list_log_subscriptions_request
    import capo_directory_service.types.list_log_subscriptions_result
    import capo_directory_service.types.list_schema_extensions_request
    import capo_directory_service.types.list_schema_extensions_result
    import capo_directory_service.types.list_tags_for_resource_request
    import capo_directory_service.types.list_tags_for_resource_result
    import capo_directory_service.types.log_group_name
    import capo_directory_service.types.log_subscription
    import capo_directory_service.types.network_type
    import capo_directory_service.types.network_update_settings
    import capo_directory_service.types.next_token
    import capo_directory_service.types.notes
    import capo_directory_service.types.organizational_unit_dn
    import capo_directory_service.types.os_update_settings
    import capo_directory_service.types.page_limit
    import capo_directory_service.types.password
    import capo_directory_service.types.pca_connector_arn
    import capo_directory_service.types.radius_settings
    import capo_directory_service.types.region_description
    import capo_directory_service.types.region_name
    import capo_directory_service.types.register_certificate_request
    import capo_directory_service.types.register_certificate_result
    import capo_directory_service.types.register_event_topic_request
    import capo_directory_service.types.register_event_topic_result
    import capo_directory_service.types.reject_shared_directory_request
    import capo_directory_service.types.reject_shared_directory_result
    import capo_directory_service.types.remote_domain_name
    import capo_directory_service.types.remote_domain_names
    import capo_directory_service.types.remove_ip_routes_request
    import capo_directory_service.types.remove_ip_routes_result
    import capo_directory_service.types.remove_region_request
    import capo_directory_service.types.remove_region_result
    import capo_directory_service.types.remove_tags_from_resource_request
    import capo_directory_service.types.remove_tags_from_resource_result
    import capo_directory_service.types.reset_user_password_request
    import capo_directory_service.types.reset_user_password_result
    import capo_directory_service.types.resource_id
    import capo_directory_service.types.restore_from_snapshot_request
    import capo_directory_service.types.restore_from_snapshot_result
    import capo_directory_service.types.schema_extension_id
    import capo_directory_service.types.schema_extension_info
    import capo_directory_service.types.secret_arn
    import capo_directory_service.types.selective_auth
    import capo_directory_service.types.settings
    import capo_directory_service.types.share_directory_request
    import capo_directory_service.types.share_directory_result
    import capo_directory_service.types.share_method
    import capo_directory_service.types.share_target
    import capo_directory_service.types.shared_directory
    import capo_directory_service.types.snapshot
    import capo_directory_service.types.snapshot_id
    import capo_directory_service.types.snapshot_ids
    import capo_directory_service.types.snapshot_name
    import capo_directory_service.types.start_ad_assessment_request
    import capo_directory_service.types.start_ad_assessment_result
    import capo_directory_service.types.start_schema_extension_request
    import capo_directory_service.types.start_schema_extension_result
    import capo_directory_service.types.tag
    import capo_directory_service.types.tag_keys
    import capo_directory_service.types.tags
    import capo_directory_service.types.topic_name
    import capo_directory_service.types.topic_names
    import capo_directory_service.types.trust
    import capo_directory_service.types.trust_direction
    import capo_directory_service.types.trust_id
    import capo_directory_service.types.trust_ids
    import capo_directory_service.types.trust_password
    import capo_directory_service.types.trust_type
    import capo_directory_service.types.unshare_directory_request
    import capo_directory_service.types.unshare_directory_result
    import capo_directory_service.types.unshare_target
    import capo_directory_service.types.update_conditional_forwarder_request
    import capo_directory_service.types.update_conditional_forwarder_result
    import capo_directory_service.types.update_directory_setup_request
    import capo_directory_service.types.update_directory_setup_result
    import capo_directory_service.types.update_hybrid_ad_request
    import capo_directory_service.types.update_hybrid_ad_result
    import capo_directory_service.types.update_info_entry
    import capo_directory_service.types.update_number_of_domain_controllers_request
    import capo_directory_service.types.update_number_of_domain_controllers_result
    import capo_directory_service.types.update_radius_request
    import capo_directory_service.types.update_radius_result
    import capo_directory_service.types.update_security_group_for_directory_controllers
    import capo_directory_service.types.update_settings_request
    import capo_directory_service.types.update_settings_result
    import capo_directory_service.types.update_trust_request
    import capo_directory_service.types.update_trust_result
    import capo_directory_service.types.update_type
    import capo_directory_service.types.user_name
    import capo_directory_service.types.user_password
    import capo_directory_service.types.verify_trust_request
    import capo_directory_service.types.verify_trust_result


class AsyncDirectoryServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDirectoryServiceClient:
    """A client for the ``DirectoryService`` service.

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
        self._config = AsyncDirectoryServiceClientConfig(
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
        self, config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDirectoryServiceClientConfig = config_overrides or {}
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

    async def accept_shared_directory(
        self,
        shared_directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.accept_shared_directory_result.AcceptSharedDirectoryResult":
        """<p>Accepts a directory sharing request that was sent from the directory owner account.</p>

        Args:
            shared_directory_id: <p>Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account. </p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_already_shared_exception.DirectoryAlreadySharedException: <p>The specified directory has already been shared with this Amazon Web Services account.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.accept_shared_directory_request.AcceptSharedDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.accept_shared_directory_result.AcceptSharedDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.accept_shared_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.accept_shared_directory.async_accept_shared_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.accept_shared_directory_request.AcceptSharedDirectoryRequest = {
            "shared_directory_id": shared_directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_ip_routes(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        ip_routes: "capo_directory_service.types.ip_routes.IpRoutes",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        update_security_group_for_directory_controllers: Optional[
            "capo_directory_service.types.update_security_group_for_directory_controllers.UpdateSecurityGroupForDirectoryControllers"
        ] = None,
    ) -> "capo_directory_service.types.add_ip_routes_result.AddIpRoutesResult":
        """<p>If the DNS server for your self-managed domain uses a publicly addressable IP address, you must add a CIDR address block to correctly route traffic to and from your Microsoft AD on Amazon Web Services. <i>AddIpRoutes</i> adds this address block. You can also use <i>AddIpRoutes</i> to facilitate routing traffic that uses public IP ranges from your Microsoft AD on Amazon Web Services to a peer VPC. </p> <p>Before you call <i>AddIpRoutes</i>, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the <i>AddIpRoutes</i> operation, see <a href="http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html">Directory Service API Permissions: Actions, Resources, and Conditions Reference</a>.</p>

        Args:
            directory_id: <p>Identifier (ID) of the directory to which to add the address block.</p>
            ip_routes: <p>IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your self-managed domain.</p>
            update_security_group_for_directory_controllers: <p>If set to true, updates the inbound and outbound rules of the security group that has the description: "Amazon Web Services created security group for <i>directory ID</i> directory controllers." Following are the new rules: </p> <p>Inbound:</p> <ul> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: DNS (UDP), Protocol: UDP, Range: 53, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: DNS (TCP), Protocol: TCP, Range: 53, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: LDAP, Protocol: TCP, Range: 389, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> <li> <p>Type: All ICMP, Protocol: All, Range: N/A, Source: Managed Microsoft AD VPC IPv4 CIDR</p> </li> </ul> <p></p> <p>Outbound:</p> <ul> <li> <p>Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0</p> </li> </ul> <p>These security rules impact an internal network interface that is not exposed publicly.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.ip_route_limit_exceeded_exception.IpRouteLimitExceededException: <p>The maximum allowed number of IP addresses was exceeded. The default limit is 100 IP address blocks.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add a CIDR address block that routes traffic for Microsoft AD
            The following example adds a CIDR address block to correctly route traffic to and from your Microsoft AD on AWS.

            >>> await client.add_ip_routes(directory_id='d-92654abfed', ip_routes=[{'Description': 'my IpRoute', 'CidrIp': '12.12.12.12/32'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.add_ip_routes_request.AddIpRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.add_ip_routes_result.AddIpRoutesResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.add_ip_routes

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.add_ip_routes.async_add_ip_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.add_ip_routes_request.AddIpRoutesRequest = {
            "directory_id": directory_id,
            "ip_routes": ip_routes,
        }
        if update_security_group_for_directory_controllers is not None:
            input_["update_security_group_for_directory_controllers"] = (
                update_security_group_for_directory_controllers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_region(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        region_name: "capo_directory_service.types.region_name.RegionName",
        vpc_settings: "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.add_region_result.AddRegionResult":
        """<p>Adds two domain controllers in the specified Region for the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory to which you want to add Region replication.</p>
            region_name: <p>The name of the Region where you want to add domain controllers for replication. For example, <code>us-east-1</code>.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_already_in_region_exception.DirectoryAlreadyInRegionException: <p>The Region you specified is the same Region where the Managed Microsoft AD directory was created. Specify a different Region and try again.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.region_limit_exceeded_exception.RegionLimitExceededException: <p>You have reached the limit for maximum number of simultaneous Region replications per directory.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.add_region_request.AddRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.add_region_result.AddRegionResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.add_region

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.add_region.async_add_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.add_region_request.AddRegionRequest = {
            "directory_id": directory_id,
            "region_name": region_name,
            "vpc_settings": vpc_settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_tags_to_resource(
        self,
        resource_id: "capo_directory_service.types.resource_id.ResourceId",
        tags: "capo_directory_service.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.add_tags_to_resource_result.AddTagsToResourceResult":
        """<p>Adds or overwrites one or more tags for the specified directory. Each directory can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique to each resource.</p>

        Args:
            resource_id: <p>Identifier (ID) for the directory to which to add the tag.</p>
            tags: <p>The tags to be assigned to the directory.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.tag_limit_exceeded_exception.TagLimitExceededException: <p>The maximum allowed number of tags was exceeded.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to a directory
            The following example adds or overwrites one or more tags for the specified directory.

            >>> await client.add_tags_to_resource(resource_id='d-92654abfed', tags=[{'Key': 'environment', 'Value': 'production'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.add_tags_to_resource_request.AddTagsToResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.add_tags_to_resource_result.AddTagsToResourceResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.add_tags_to_resource

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.add_tags_to_resource.async_add_tags_to_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.add_tags_to_resource_request.AddTagsToResourceRequest = {
            "resource_id": resource_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_schema_extension(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        schema_extension_id: "capo_directory_service.types.schema_extension_id.SchemaExtensionId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.cancel_schema_extension_result.CancelSchemaExtensionResult":
        """<p>Cancels an in-progress schema extension to a Microsoft AD directory. Once a schema extension has started replicating to all domain controllers, the task can no longer be canceled. A schema extension can be canceled during any of the following states; <code>Initializing</code>, <code>CreatingSnapshot</code>, and <code>UpdatingSchema</code>.</p>

        Args:
            directory_id: <p>The identifier of the directory whose schema extension will be canceled.</p>
            schema_extension_id: <p>The identifier of the schema extension that will be canceled.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel a Microsoft AD schema extension that is in progress
            The following example cancels an in-progress schema extension to a Microsoft AD directory.

            >>> await client.cancel_schema_extension(directory_id='d-92654abfed', schema_extension_id='e-926731d2a0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.cancel_schema_extension_request.CancelSchemaExtensionRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.cancel_schema_extension_result.CancelSchemaExtensionResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.cancel_schema_extension

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.cancel_schema_extension.async_cancel_schema_extension(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.cancel_schema_extension_request.CancelSchemaExtensionRequest = {
            "directory_id": directory_id,
            "schema_extension_id": schema_extension_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def connect_directory(
        self,
        name: "capo_directory_service.types.directory_name.DirectoryName",
        password: "capo_directory_service.types.connect_password.ConnectPassword",
        size: "capo_directory_service.types.directory_size.DirectorySize",
        connect_settings: "capo_directory_service.types.directory_connect_settings.DirectoryConnectSettings",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        short_name: Optional[
            "capo_directory_service.types.directory_short_name.DirectoryShortName"
        ] = None,
        description: Optional[
            "capo_directory_service.types.description.Description"
        ] = None,
        tags: Optional["capo_directory_service.types.tags.Tags"] = None,
        network_type: Optional[
            "capo_directory_service.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_directory_service.types.connect_directory_result.ConnectDirectoryResult":
        """<p>Creates an AD Connector to connect to a self-managed directory.</p> <p>Before you call <code>ConnectDirectory</code>, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the <code>ConnectDirectory</code> operation, see <a href="http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html">Directory Service API Permissions: Actions, Resources, and Conditions Reference</a>.</p>

        Args:
            name: <p>The fully qualified name of your self-managed directory, such as <code>corp.example.com</code>.</p>
            short_name: <p>The NetBIOS name of your self-managed directory, such as <code>CORP</code>.</p>
            password: <p>The password for your self-managed user account.</p>
            description: <p>A description for the directory.</p>
            size: <p>The size of the directory.</p>
            connect_settings: <p>A <a>DirectoryConnectSettings</a> object that contains additional information for the operation.</p>
            tags: <p>The tags to be assigned to AD Connector.</p>
            network_type: <p>The network type for your directory. The default value is <code>IPv4</code> or <code>IPv6</code> based on the provided subnet capabilities.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_limit_exceeded_exception.DirectoryLimitExceededException: <p>The maximum number of directories in the region has been reached. You can use the <a>GetDirectoryLimits</a> operation to determine your directory limits in the region.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To connect to an on-premises directory
            The following example creates an AD Connector to connect to an on-premises directory.

            >>> await client.connect_directory(name='corp.example.com', short_name='corp', password='Str0ngP@ssw0rd', description='Connector to corp', size='Small', connect_settings={'CustomerUserName': 'Administrator', 'VpcId': 'vpc-45025421', 'SubnetIds': ['subnet-ba0146de', 'subnet-bef46bc8'], 'CustomerDnsIps': ['172.30.21.228']})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.connect_directory_request.ConnectDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.connect_directory_result.ConnectDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.connect_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.connect_directory.async_connect_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.connect_directory_request.ConnectDirectoryRequest = {
            "name": name,
            "password": password,
            "size": size,
            "connect_settings": connect_settings,
        }
        if short_name is not None:
            input_["short_name"] = short_name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_alias(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        alias: "capo_directory_service.types.alias_name.AliasName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.create_alias_result.CreateAliasResult":
        """<p>Creates an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as <code>http://<alias>.awsapps.com</code>.</p> <important> <p>After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.</p> </important>

        Args:
            directory_id: <p>The identifier of the directory for which to create the alias.</p>
            alias: <p>The requested alias.</p> <p>The alias must be unique amongst all aliases in Amazon Web Services. This operation throws an <code>EntityAlreadyExistsException</code> error if the alias already exists.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an alias for a directory
            The following example creates an alias for a directory.

            >>> await client.create_alias(directory_id='d-92654abfed', alias='salesorg')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_alias_request.CreateAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_alias_result.CreateAliasResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_alias

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_alias.async_create_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_alias_request.CreateAliasRequest = {
            "directory_id": directory_id,
            "alias": alias,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_computer(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        computer_name: "capo_directory_service.types.computer_name.ComputerName",
        password: "capo_directory_service.types.computer_password.ComputerPassword",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        organizational_unit_distinguished_name: Optional[
            "capo_directory_service.types.organizational_unit_dn.OrganizationalUnitDN"
        ] = None,
        computer_attributes: Optional[
            "capo_directory_service.types.attributes.Attributes"
        ] = None,
    ) -> "capo_directory_service.types.create_computer_result.CreateComputerResult":
        """<p>Creates an Active Directory computer object in the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory in which to create the computer account.</p>
            computer_name: <p>The name of the computer account.</p>
            password: <p>A one-time password that is used to join the computer to the directory. You should generate a random, strong password to use for this parameter.</p>
            organizational_unit_distinguished_name: <p>The fully-qualified distinguished name of the organizational unit to place the computer account in.</p>
            computer_attributes: <p>An array of <a>Attribute</a> objects that contain any LDAP attributes to apply to the computer account.</p>

        Raises:
            capo_directory_service.errors.authentication_failed_exception.AuthenticationFailedException: <p>An authentication error occurred.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a computer account
            The following example creates a computer account in the specified directory, and joins the computer to the directory.

            >>> await client.create_computer(directory_id='d-92654abfed', computer_name='labcomputer', password='Str0ngP@ssw0rd', organizational_unit_distinguished_name='OU=Computers,OU=example,DC=corp,DC=example,DC=com', computer_attributes=[{'Name': 'ip', 'Value': '192.168.101.100'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_computer_request.CreateComputerRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_computer_result.CreateComputerResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_computer

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_computer.async_create_computer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_computer_request.CreateComputerRequest = {
            "directory_id": directory_id,
            "computer_name": computer_name,
            "password": password,
        }
        if organizational_unit_distinguished_name is not None:
            input_["organizational_unit_distinguished_name"] = (
                organizational_unit_distinguished_name
            )
        if computer_attributes is not None:
            input_["computer_attributes"] = computer_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_conditional_forwarder(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        remote_domain_name: "capo_directory_service.types.remote_domain_name.RemoteDomainName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        dns_ip_addrs: Optional[
            "capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"
        ] = None,
        dns_ipv6_addrs: Optional[
            "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
        ] = None,
    ) -> "capo_directory_service.types.create_conditional_forwarder_result.CreateConditionalForwarderResult":
        """<p>Creates a conditional forwarder associated with your Amazon Web Services directory. Conditional forwarders are required in order to set up a trust relationship with another domain. The conditional forwarder points to the trusted domain.</p>

        Args:
            directory_id: <p>The directory ID of the Amazon Web Services directory for which you are creating the conditional forwarder.</p>
            remote_domain_name: <p>The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.</p>
            dns_ip_addrs: <p>The IP addresses of the remote DNS server associated with RemoteDomainName.</p>
            dns_ipv6_addrs: <p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a conditional forwarder
            The following example creates a conditional forwarder associated with your AWS directory.

            >>> await client.create_conditional_forwarder(directory_id='d-92654abfed', remote_domain_name='sales.example.com', dns_ip_addrs=['172.30.21.228'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_conditional_forwarder_request.CreateConditionalForwarderRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_conditional_forwarder_result.CreateConditionalForwarderResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_conditional_forwarder

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_conditional_forwarder.async_create_conditional_forwarder(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_conditional_forwarder_request.CreateConditionalForwarderRequest = {
            "directory_id": directory_id,
            "remote_domain_name": remote_domain_name,
        }
        if dns_ip_addrs is not None:
            input_["dns_ip_addrs"] = dns_ip_addrs
        if dns_ipv6_addrs is not None:
            input_["dns_ipv6_addrs"] = dns_ipv6_addrs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_directory(
        self,
        name: "capo_directory_service.types.directory_name.DirectoryName",
        password: "capo_directory_service.types.password.Password",
        size: "capo_directory_service.types.directory_size.DirectorySize",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        short_name: Optional[
            "capo_directory_service.types.directory_short_name.DirectoryShortName"
        ] = None,
        description: Optional[
            "capo_directory_service.types.description.Description"
        ] = None,
        vpc_settings: Optional[
            "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings"
        ] = None,
        tags: Optional["capo_directory_service.types.tags.Tags"] = None,
        network_type: Optional[
            "capo_directory_service.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_directory_service.types.create_directory_result.CreateDirectoryResult":
        r"""<p>Creates a Simple AD directory. For more information, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html">Simple Active Directory</a> in the <i>Directory Service Admin Guide</i>.</p> <p>Before you call <code>CreateDirectory</code>, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the <code>CreateDirectory</code> operation, see <a href="http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html">Directory Service API Permissions: Actions, Resources, and Conditions Reference</a>.</p>

        Args:
            name: <p>The fully qualified name for the directory, such as <code>corp.example.com</code>.</p>
            short_name: <p>The NetBIOS name of the directory, such as <code>CORP</code>.</p>
            password: <p>The password for the directory administrator. The directory creation process creates a directory administrator account with the user name <code>Administrator</code> and this password.</p> <p>If you need to change the password for the administrator account, you can use the <a>ResetUserPassword</a> API call.</p> <p>The regex pattern for this string is made up of the following conditions:</p> <ul> <li> <p>Length (?=^.{8,64}$) – Must be between 8 and 64 characters</p> </li> </ul> <p>AND any 3 of the following password complexity rules required by Active Directory:</p> <ul> <li> <p>Numbers and upper case and lowercase (?=.*\d)(?=.*[A-Z])(?=.*[a-z])</p> </li> <li> <p>Numbers and special characters and lower case (?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])</p> </li> <li> <p>Special characters and upper case and lower case (?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])</p> </li> <li> <p>Numbers and upper case and special characters (?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s])</p> </li> </ul> <p>For additional information about how Active Directory passwords are enforced, see <a href="https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements">Password must meet complexity requirements</a> on the Microsoft website.</p>
            description: <p>A description for the directory.</p>
            size: <p>The size of the directory.</p>
            vpc_settings: <p>A <a>DirectoryVpcSettings</a> object that contains additional information for the operation.</p>
            tags: <p>The tags to be assigned to the Simple AD directory.</p>
            network_type: <p>The network type for your directory. Simple AD supports IPv4 and Dual-stack only.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_limit_exceeded_exception.DirectoryLimitExceededException: <p>The maximum number of directories in the region has been reached. You can use the <a>GetDirectoryLimits</a> operation to determine your directory limits in the region.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a Simple AD directory
            The following example creates a Simple AD directory.

            >>> await client.create_directory(name='seattle.example.com', short_name='seattle', password='Str0ngP@ssw0rd', description='Regional directory for example.com', size='Small', vpc_settings={'SubnetIds': ['subnet-ba0146de', 'subnet-bef46bc8'], 'VpcId': 'vpc-45025421'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_directory_request.CreateDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_directory_result.CreateDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_directory.async_create_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_directory_request.CreateDirectoryRequest = {
            "name": name,
            "password": password,
            "size": size,
        }
        if short_name is not None:
            input_["short_name"] = short_name
        if description is not None:
            input_["description"] = description
        if vpc_settings is not None:
            input_["vpc_settings"] = vpc_settings
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_hybrid_ad(
        self,
        secret_arn: "capo_directory_service.types.secret_arn.SecretArn",
        assessment_id: "capo_directory_service.types.assessment_id.AssessmentId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        tags: Optional["capo_directory_service.types.tags.Tags"] = None,
    ) -> "capo_directory_service.types.create_hybrid_ad_result.CreateHybridADResult":
        """<p>Creates a hybrid directory that connects your self-managed Active Directory (AD) infrastructure and Amazon Web Services.</p> <p>You must have a successful directory assessment using <a>StartADAssessment</a> to validate your environment compatibility before you use this operation.</p> <p>Updates are applied asynchronously. Use <a>DescribeDirectories</a> to monitor the progress of directory creation.</p>

        Args:
            secret_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials for the service account used to join hybrid domain controllers to your self-managed AD domain. This secret is used once and not stored.</p> <p>The secret must contain key-value pairs with keys matching <code>customerAdAdminDomainUsername</code> and <code>customerAdAdminDomainPassword</code>. For example: <code>{"customerAdAdminDomainUsername":"carlos_salazar","customerAdAdminDomainPassword":"ExamplePassword123!"}</code>.</p>
            assessment_id: <p>The unique identifier of the successful directory assessment that validates your self-managed AD environment. You must have a successful directory assessment before you create a hybrid directory.</p>
            tags: <p>The tags to be assigned to the directory. Each tag consists of a key and value pair. You can specify multiple tags as a list.</p>

        Raises:
            capo_directory_service.errors.ad_assessment_limit_exceeded_exception.ADAssessmentLimitExceededException: <p>A directory assessment is automatically created when you create a hybrid directory. There are two types of assessments: <code>CUSTOMER</code> and <code>SYSTEM</code>. Your Amazon Web Services account has a limit of 100 <code>CUSTOMER</code> directory assessments.</p> <p>If you attempt to create a hybrid directory; and you already have 100 <code>CUSTOMER</code> directory assessments;, you will encounter an error. Delete assessments to free up capacity before trying again.</p> <p>You can request an increase to your <code>CUSTOMER</code> directory assessment quota by contacting customer support or delete existing CUSTOMER directory assessments; to free up capacity.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_limit_exceeded_exception.DirectoryLimitExceededException: <p>The maximum number of directories in the region has been reached. You can use the <a>GetDirectoryLimits</a> operation to determine your directory limits in the region.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_hybrid_ad_request.CreateHybridADRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_hybrid_ad_result.CreateHybridADResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_hybrid_ad

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_hybrid_ad.async_create_hybrid_ad(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_hybrid_ad_request.CreateHybridADRequest = {
            "secret_arn": secret_arn,
            "assessment_id": assessment_id,
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

    async def create_log_subscription(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        log_group_name: "capo_directory_service.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.create_log_subscription_result.CreateLogSubscriptionResult":
        """<p>Creates a subscription to forward real-time Directory Service domain controller security logs to the specified Amazon CloudWatch log group in your Amazon Web Services account.</p>

        Args:
            directory_id: <p>Identifier of the directory to which you want to subscribe and receive real-time logs to your specified CloudWatch log group.</p>
            log_group_name: <p>The name of the CloudWatch log group where the real-time domain controller logs are forwarded.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>The account does not have sufficient permission to perform the operation.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_log_subscription_request.CreateLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_log_subscription_result.CreateLogSubscriptionResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_log_subscription

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_log_subscription.async_create_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_log_subscription_request.CreateLogSubscriptionRequest = {
            "directory_id": directory_id,
            "log_group_name": log_group_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_microsoft_ad(
        self,
        name: "capo_directory_service.types.directory_name.DirectoryName",
        password: "capo_directory_service.types.password.Password",
        vpc_settings: "capo_directory_service.types.directory_vpc_settings.DirectoryVpcSettings",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        short_name: Optional[
            "capo_directory_service.types.directory_short_name.DirectoryShortName"
        ] = None,
        description: Optional[
            "capo_directory_service.types.description.Description"
        ] = None,
        edition: Optional[
            "capo_directory_service.types.directory_edition.DirectoryEdition"
        ] = None,
        tags: Optional["capo_directory_service.types.tags.Tags"] = None,
        network_type: Optional[
            "capo_directory_service.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_directory_service.types.create_microsoft_ad_result.CreateMicrosoftADResult":
        """<p>Creates a Microsoft AD directory in the Amazon Web Services Cloud. For more information, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html">Managed Microsoft AD</a> in the <i>Directory Service Admin Guide</i>.</p> <p>Before you call <i>CreateMicrosoftAD</i>, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the <i>CreateMicrosoftAD</i> operation, see <a href="http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html">Directory Service API Permissions: Actions, Resources, and Conditions Reference</a>.</p>

        Args:
            name: <p>The fully qualified domain name for the Managed Microsoft AD directory, such as <code>corp.example.com</code>. This name will resolve inside your VPC only. It does not need to be publicly resolvable.</p>
            short_name: <p>The NetBIOS name for your domain, such as <code>CORP</code>. If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, <code>CORP</code> for the directory DNS <code>corp.example.com</code>. </p>
            password: <p>The password for the default administrative user named <code>Admin</code>.</p> <p>If you need to change the password for the administrator account, you can use the <a>ResetUserPassword</a> API call.</p>
            description: <p>A description for the directory. This label will appear on the Amazon Web Services console <code>Directory Details</code> page after the directory is created.</p>
            vpc_settings: <p>Contains VPC information for the <a>CreateDirectory</a> or <a>CreateMicrosoftAD</a> operation.</p>
            edition: <p>Managed Microsoft AD is available in two editions: <code>Standard</code> and <code>Enterprise</code>. <code>Enterprise</code> is the default.</p>
            tags: <p>The tags to be assigned to the Managed Microsoft AD directory.</p>
            network_type: <p> The network type for your domain. The default value is <code>IPv4</code> or <code>IPv6</code> based on the provided subnet capabilities.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_limit_exceeded_exception.DirectoryLimitExceededException: <p>The maximum number of directories in the region has been reached. You can use the <a>GetDirectoryLimits</a> operation to determine your directory limits in the region.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a Microsoft AD directory
            The following example creates a Microsoft AD directory in the AWS cloud.

            >>> await client.create_microsoft_ad(name='ad.example.com', short_name='ad', password='Str0ngP@ssw0rd', description='Corporate AD directory', vpc_settings={'SubnetIds': ['subnet-ba0146de', 'subnet-bef46bc8'], 'VpcId': 'vpc-45025421'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_microsoft_ad_request.CreateMicrosoftADRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_microsoft_ad_result.CreateMicrosoftADResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_microsoft_ad

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_microsoft_ad.async_create_microsoft_ad(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_microsoft_ad_request.CreateMicrosoftADRequest = {
            "name": name,
            "password": password,
            "vpc_settings": vpc_settings,
        }
        if short_name is not None:
            input_["short_name"] = short_name
        if description is not None:
            input_["description"] = description
        if edition is not None:
            input_["edition"] = edition
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_snapshot(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        name: Optional[
            "capo_directory_service.types.snapshot_name.SnapshotName"
        ] = None,
    ) -> "capo_directory_service.types.create_snapshot_result.CreateSnapshotResult":
        """<p>Creates a snapshot of a Simple AD or Microsoft AD directory in the Amazon Web Services cloud.</p> <note> <p>You cannot take snapshots of AD Connector directories.</p> </note>

        Args:
            directory_id: <p>The identifier of the directory of which to take a snapshot.</p>
            name: <p>The descriptive name to apply to the snapshot.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.snapshot_limit_exceeded_exception.SnapshotLimitExceededException: <p>The maximum number of manual snapshots for the directory has been reached. You can use the <a>GetSnapshotLimits</a> operation to determine the snapshot limits for a directory.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a snapshot of a directory
            The following example creates a snapshot of a Simple AD or Microsoft AD directory in the AWS cloud.

            >>> await client.create_snapshot(directory_id='d-92654abfed', name='ad.example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_snapshot_result.CreateSnapshotResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_snapshot

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_snapshot_request.CreateSnapshotRequest = {
            "directory_id": directory_id
        }
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_trust(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        remote_domain_name: "capo_directory_service.types.remote_domain_name.RemoteDomainName",
        trust_password: "capo_directory_service.types.trust_password.TrustPassword",
        trust_direction: "capo_directory_service.types.trust_direction.TrustDirection",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        trust_type: Optional[
            "capo_directory_service.types.trust_type.TrustType"
        ] = None,
        conditional_forwarder_ip_addrs: Optional[
            "capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"
        ] = None,
        conditional_forwarder_ipv6_addrs: Optional[
            "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
        ] = None,
        selective_auth: Optional[
            "capo_directory_service.types.selective_auth.SelectiveAuth"
        ] = None,
    ) -> "capo_directory_service.types.create_trust_result.CreateTrustResult":
        """<p>Directory Service for Microsoft Active Directory allows you to configure trust relationships. For example, you can establish a trust between your Managed Microsoft AD directory, and your existing self-managed Microsoft Active Directory. This would allow you to provide users and groups access to resources in either domain, with a single set of credentials.</p> <p>This action initiates the creation of the Amazon Web Services side of a trust relationship between an Managed Microsoft AD directory and an external domain. You can create either a forest trust or an external trust.</p>

        Args:
            directory_id: <p>The Directory ID of the Managed Microsoft AD directory for which to establish the trust relationship.</p>
            remote_domain_name: <p>The Fully Qualified Domain Name (FQDN) of the external domain for which to create the trust relationship.</p>
            trust_password: <p>The trust password. The trust password must be the same password that was used when creating the trust relationship on the external domain.</p>
            trust_direction: <p>The direction of the trust relationship.</p>
            trust_type: <p>The trust relationship type. <code>Forest</code> is the default.</p>
            conditional_forwarder_ip_addrs: <p>The IP addresses of the remote DNS server associated with RemoteDomainName.</p>
            conditional_forwarder_ipv6_addrs: <p>The IPv6 addresses of the remote DNS server associated with RemoteDomainName.</p>
            selective_auth: <p>Optional parameter to enable selective authentication for the trust.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a trust
            The following example creates a trust between Microsoft AD in the AWS cloud and an external domain.

            >>> await client.create_trust(directory_id='d-92654abfed', remote_domain_name='europe.example.com', trust_password='Str0ngP@ssw0rd', trust_direction='One-Way: Outgoing', trust_type='Forest', conditional_forwarder_ip_addrs=['172.30.21.228'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.create_trust_request.CreateTrustRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.create_trust_result.CreateTrustResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.create_trust

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.create_trust.async_create_trust(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.create_trust_request.CreateTrustRequest = {
            "directory_id": directory_id,
            "remote_domain_name": remote_domain_name,
            "trust_password": trust_password,
            "trust_direction": trust_direction,
        }
        if trust_type is not None:
            input_["trust_type"] = trust_type
        if conditional_forwarder_ip_addrs is not None:
            input_["conditional_forwarder_ip_addrs"] = conditional_forwarder_ip_addrs
        if conditional_forwarder_ipv6_addrs is not None:
            input_["conditional_forwarder_ipv6_addrs"] = (
                conditional_forwarder_ipv6_addrs
            )
        if selective_auth is not None:
            input_["selective_auth"] = selective_auth

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ad_assessment(
        self,
        assessment_id: "capo_directory_service.types.assessment_id.AssessmentId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.delete_ad_assessment_result.DeleteADAssessmentResult":
        """<p>Deletes a directory assessment and all associated data. This operation permanently removes the assessment results, validation reports, and configuration information.</p> <p>You cannot delete system-initiated assessments. You can delete customer-created assessments even if they are in progress.</p>

        Args:
            assessment_id: <p>The unique identifier of the directory assessment to delete.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.delete_ad_assessment_request.DeleteADAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.delete_ad_assessment_result.DeleteADAssessmentResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.delete_ad_assessment

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.delete_ad_assessment.async_delete_ad_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.delete_ad_assessment_request.DeleteADAssessmentRequest = {
            "assessment_id": assessment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_conditional_forwarder(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        remote_domain_name: "capo_directory_service.types.remote_domain_name.RemoteDomainName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.delete_conditional_forwarder_result.DeleteConditionalForwarderResult":
        """<p>Deletes a conditional forwarder that has been set up for your Amazon Web Services directory.</p>

        Args:
            directory_id: <p>The directory ID for which you are deleting the conditional forwarder.</p>
            remote_domain_name: <p>The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a conditional forwarder
            The following example deletes a conditional forwarder.

            >>> await client.delete_conditional_forwarder(directory_id='d-92654abfed', remote_domain_name='sales.example.com')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.delete_conditional_forwarder_request.DeleteConditionalForwarderRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.delete_conditional_forwarder_result.DeleteConditionalForwarderResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.delete_conditional_forwarder

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.delete_conditional_forwarder.async_delete_conditional_forwarder(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.delete_conditional_forwarder_request.DeleteConditionalForwarderRequest = {
            "directory_id": directory_id,
            "remote_domain_name": remote_domain_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_directory(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.delete_directory_result.DeleteDirectoryResult":
        """<p>Deletes an Directory Service directory.</p> <p>Before you call <code>DeleteDirectory</code>, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the <code>DeleteDirectory</code> operation, see <a href="http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html">Directory Service API Permissions: Actions, Resources, and Conditions Reference</a>.</p>

        Args:
            directory_id: <p>The identifier of the directory to delete.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a directory
            The following example deletes a directory from your AWS account.

            >>> await client.delete_directory(directory_id='d-92654abfed')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.delete_directory_request.DeleteDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.delete_directory_result.DeleteDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.delete_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.delete_directory.async_delete_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.delete_directory_request.DeleteDirectoryRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_log_subscription(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.delete_log_subscription_result.DeleteLogSubscriptionResult":
        """<p>Deletes the specified log subscription.</p>

        Args:
            directory_id: <p>Identifier of the directory whose log subscription you want to delete.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.delete_log_subscription_request.DeleteLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.delete_log_subscription_result.DeleteLogSubscriptionResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.delete_log_subscription

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.delete_log_subscription.async_delete_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.delete_log_subscription_request.DeleteLogSubscriptionRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot(
        self,
        snapshot_id: "capo_directory_service.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.delete_snapshot_result.DeleteSnapshotResult":
        """<p>Deletes a directory snapshot.</p>

        Args:
            snapshot_id: <p>The identifier of the directory snapshot to be deleted.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a snapshot
            The following example deletes a directory snapshot.

            >>> await client.delete_snapshot(snapshot_id='s-9267f8d3f0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.delete_snapshot_result.DeleteSnapshotResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.delete_snapshot

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.delete_snapshot.async_delete_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.delete_snapshot_request.DeleteSnapshotRequest = {
            "snapshot_id": snapshot_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_trust(
        self,
        trust_id: "capo_directory_service.types.trust_id.TrustId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        delete_associated_conditional_forwarder: Optional[
            "capo_directory_service.types.delete_associated_conditional_forwarder.DeleteAssociatedConditionalForwarder"
        ] = None,
    ) -> "capo_directory_service.types.delete_trust_result.DeleteTrustResult":
        """<p>Deletes an existing trust relationship between your Managed Microsoft AD directory and an external domain.</p>

        Args:
            trust_id: <p>The Trust ID of the trust relationship to be deleted.</p>
            delete_associated_conditional_forwarder: <p>Delete a conditional forwarder as part of a DeleteTrustRequest.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a trust
            The following example deletes an existing trust between your Microsoft AD in the AWS cloud and an external domain.

            >>> await client.delete_trust(trust_id='t-9267353743', delete_associated_conditional_forwarder=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.delete_trust_request.DeleteTrustRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.delete_trust_result.DeleteTrustResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.delete_trust

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.delete_trust.async_delete_trust(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.delete_trust_request.DeleteTrustRequest = {
            "trust_id": trust_id
        }
        if delete_associated_conditional_forwarder is not None:
            input_["delete_associated_conditional_forwarder"] = (
                delete_associated_conditional_forwarder
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_certificate(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        certificate_id: "capo_directory_service.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.deregister_certificate_result.DeregisterCertificateResult":
        """<p>Deletes from the system the certificate that was registered for secure LDAP or client certificate authentication.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            certificate_id: <p>The identifier of the certificate.</p>

        Raises:
            capo_directory_service.errors.certificate_does_not_exist_exception.CertificateDoesNotExistException: <p>The certificate is not present in the system for describe or deregister activities.</p>
            capo_directory_service.errors.certificate_in_use_exception.CertificateInUseException: <p>The certificate is being used for the LDAP security connection and cannot be removed without disabling LDAP security.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.deregister_certificate_request.DeregisterCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.deregister_certificate_result.DeregisterCertificateResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.deregister_certificate

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.deregister_certificate.async_deregister_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.deregister_certificate_request.DeregisterCertificateRequest = {
            "directory_id": directory_id,
            "certificate_id": certificate_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_event_topic(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        topic_name: "capo_directory_service.types.topic_name.TopicName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.deregister_event_topic_result.DeregisterEventTopicResult":
        """<p>Removes the specified directory as a publisher to the specified Amazon SNS topic.</p>

        Args:
            directory_id: <p>The Directory ID to remove as a publisher. This directory will no longer send messages to the specified Amazon SNS topic.</p>
            topic_name: <p>The name of the Amazon SNS topic from which to remove the directory as a publisher.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove an event topic
            The following example removes the specified directory as a publisher to the specified SNS topic.

            >>> await client.deregister_event_topic(directory_id='d-92654abfed', topic_name='snstopicexample')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.deregister_event_topic_request.DeregisterEventTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.deregister_event_topic_result.DeregisterEventTopicResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.deregister_event_topic

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.deregister_event_topic.async_deregister_event_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.deregister_event_topic_request.DeregisterEventTopicRequest = {
            "directory_id": directory_id,
            "topic_name": topic_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_ad_assessment(
        self,
        assessment_id: "capo_directory_service.types.assessment_id.AssessmentId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.describe_ad_assessment_result.DescribeADAssessmentResult":
        """<p>Retrieves detailed information about a directory assessment, including its current status, validation results, and configuration details. Use this operation to monitor assessment progress and review results.</p>

        Args:
            assessment_id: <p>The identifier of the directory assessment to describe.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_ad_assessment_request.DescribeADAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_ad_assessment_result.DescribeADAssessmentResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_ad_assessment

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_ad_assessment.async_describe_ad_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_ad_assessment_request.DescribeADAssessmentRequest = {
            "assessment_id": assessment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_ca_enrollment_policy(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.describe_ca_enrollment_policy_result.DescribeCAEnrollmentPolicyResult":
        """<p>Retrieves detailed information about the certificate authority (CA) enrollment policy for the specified directory. This policy determines how client certificates are automatically enrolled and managed through Amazon Web Services Private Certificate Authority. </p>

        Args:
            directory_id: <p>The identifier of the directory for which to retrieve the CA enrollment policy information.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_ca_enrollment_policy_request.DescribeCAEnrollmentPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_ca_enrollment_policy_result.DescribeCAEnrollmentPolicyResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_ca_enrollment_policy

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_ca_enrollment_policy.async_describe_ca_enrollment_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_ca_enrollment_policy_request.DescribeCAEnrollmentPolicyRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_certificate(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        certificate_id: "capo_directory_service.types.certificate_id.CertificateId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.describe_certificate_result.DescribeCertificateResult":
        """<p>Displays information about the certificate registered for secure LDAP or client certificate authentication.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            certificate_id: <p>The identifier of the certificate.</p>

        Raises:
            capo_directory_service.errors.certificate_does_not_exist_exception.CertificateDoesNotExistException: <p>The certificate is not present in the system for describe or deregister activities.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_certificate_request.DescribeCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_certificate_result.DescribeCertificateResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_certificate

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_certificate.async_describe_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_certificate_request.DescribeCertificateRequest = {
            "directory_id": directory_id,
            "certificate_id": certificate_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_client_authentication_settings(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        type: Optional[
            "capo_directory_service.types.client_authentication_type.ClientAuthenticationType"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.page_limit.PageLimit"] = None,
    ) -> "capo_directory_service.types.describe_client_authentication_settings_result.DescribeClientAuthenticationSettingsResult":
        """<p>Retrieves information about the type of client authentication for the specified directory, if the type is specified. If no type is specified, information about all client authentication types that are supported for the specified directory is retrieved. Currently, only <code>SmartCard</code> is supported. </p>

        Args:
            directory_id: <p>The identifier of the directory for which to retrieve information.</p>
            type: <p>The type of client authentication for which to retrieve information. If no type is specified, a list of all client authentication types that are supported for the specified directory is retrieved.</p>
            next_token: <p>The <i>DescribeClientAuthenticationSettingsResult.NextToken</i> value from a previous call to <a>DescribeClientAuthenticationSettings</a>. Pass null if this is the first call.</p>
            limit: <p>The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation. </p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_client_authentication_settings_request.DescribeClientAuthenticationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_client_authentication_settings_result.DescribeClientAuthenticationSettingsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_client_authentication_settings

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_client_authentication_settings.async_describe_client_authentication_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_client_authentication_settings_request.DescribeClientAuthenticationSettingsRequest = {
            "directory_id": directory_id
        }
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_client_authentication_settings(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        type: Optional[
            "capo_directory_service.types.client_authentication_type.ClientAuthenticationType"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.client_authentication_setting_info.ClientAuthenticationSettingInfo]":
        _token = next_token
        while True:
            _response = await self.describe_client_authentication_settings(
                directory_id,
                config_overrides=config_overrides,
                type=type,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("client_authentication_settings_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_conditional_forwarders(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        remote_domain_names: Optional[
            "capo_directory_service.types.remote_domain_names.RemoteDomainNames"
        ] = None,
    ) -> "capo_directory_service.types.describe_conditional_forwarders_result.DescribeConditionalForwardersResult":
        """<p>Obtains information about the conditional forwarders for this account.</p> <p>If no input parameters are provided for RemoteDomainNames, this request describes all conditional forwarders for the specified directory ID.</p>

        Args:
            directory_id: <p>The directory ID for which to get the list of associated conditional forwarders.</p>
            remote_domain_names: <p>The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe conditional forwarders
            The following example obtains information about the conditional forwarders for a specified directory.

            >>> await client.describe_conditional_forwarders(directory_id='d-92654abfed', remote_domain_names=['sales.example.com'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_conditional_forwarders_request.DescribeConditionalForwardersRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_conditional_forwarders_result.DescribeConditionalForwardersResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_conditional_forwarders

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_conditional_forwarders.async_describe_conditional_forwarders(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_conditional_forwarders_request.DescribeConditionalForwardersRequest = {
            "directory_id": directory_id
        }
        if remote_domain_names is not None:
            input_["remote_domain_names"] = remote_domain_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_directories(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_ids: Optional[
            "capo_directory_service.types.directory_ids.DirectoryIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.describe_directories_result.DescribeDirectoriesResult":
        """<p>Obtains information about the directories that belong to this account.</p> <p>You can retrieve information about specific directories by passing the directory identifiers in the <code>DirectoryIds</code> parameter. Otherwise, all directories that belong to the current account are returned.</p> <p>This operation supports pagination with the use of the <code>NextToken</code> request and response parameters. If more results are available, the <code>DescribeDirectoriesResult.NextToken</code> member contains a token that you pass in the next call to <a>DescribeDirectories</a> to retrieve the next set of items.</p> <p>You can also specify a maximum number of return results with the <code>Limit</code> parameter.</p>

        Args:
            directory_ids: <p>A list of identifiers of the directories for which to obtain the information. If this member is null, all directories that belong to the current account are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>
            next_token: <p>The <code>DescribeDirectoriesResult.NextToken</code> value from a previous call to <a>DescribeDirectories</a>. Pass null if this is the first call.</p>
            limit: <p>The maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe one or more directories
            The following example obtains information about a specified directory.

            >>> await client.describe_directories(directory_ids=['d-92654abfed'], limit=0)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_directories_request.DescribeDirectoriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_directories_result.DescribeDirectoriesResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_directories

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_directories.async_describe_directories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_directories_request.DescribeDirectoriesRequest = {}
        if directory_ids is not None:
            input_["directory_ids"] = directory_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_directories(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_ids: Optional[
            "capo_directory_service.types.directory_ids.DirectoryIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.directory_description.DirectoryDescription]":
        _token = next_token
        while True:
            _response = await self.describe_directories(
                config_overrides=config_overrides,
                directory_ids=directory_ids,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("directory_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_directory_data_access(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.describe_directory_data_access_result.DescribeDirectoryDataAccessResult":
        """<p>Obtains status of directory data access enablement through the Directory Service Data API for the specified directory.</p>

        Args:
            directory_id: <p>The directory identifier.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_directory_data_access_request.DescribeDirectoryDataAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_directory_data_access_result.DescribeDirectoryDataAccessResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_directory_data_access

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_directory_data_access.async_describe_directory_data_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_directory_data_access_request.DescribeDirectoryDataAccessRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain_controllers(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        domain_controller_ids: Optional[
            "capo_directory_service.types.domain_controller_ids.DomainControllerIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.describe_domain_controllers_result.DescribeDomainControllersResult":
        """<p>Provides information about any domain controllers in your directory.</p>

        Args:
            directory_id: <p>Identifier of the directory for which to retrieve the domain controller information.</p>
            domain_controller_ids: <p>A list of identifiers for the domain controllers whose information will be provided.</p>
            next_token: <p>The <i>DescribeDomainControllers.NextToken</i> value from a previous call to <a>DescribeDomainControllers</a>. Pass null if this is the first call. </p>
            limit: <p>The maximum number of items to return.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_domain_controllers_request.DescribeDomainControllersRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_domain_controllers_result.DescribeDomainControllersResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_domain_controllers

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_domain_controllers.async_describe_domain_controllers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_domain_controllers_request.DescribeDomainControllersRequest = {
            "directory_id": directory_id
        }
        if domain_controller_ids is not None:
            input_["domain_controller_ids"] = domain_controller_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_domain_controllers(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        domain_controller_ids: Optional[
            "capo_directory_service.types.domain_controller_ids.DomainControllerIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.describe_domain_controllers_result.DescribeDomainControllersResult]":
        _token = next_token
        while True:
            _response = await self.describe_domain_controllers(
                directory_id,
                config_overrides=config_overrides,
                domain_controller_ids=domain_controller_ids,
                next_token=_token,
                limit=limit,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_event_topics(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        topic_names: Optional[
            "capo_directory_service.types.topic_names.TopicNames"
        ] = None,
    ) -> "capo_directory_service.types.describe_event_topics_result.DescribeEventTopicsResult":
        """<p>Obtains information about which Amazon SNS topics receive status messages from the specified directory.</p> <p>If no input parameters are provided, such as DirectoryId or TopicName, this request describes all of the associations in the account.</p>

        Args:
            directory_id: <p>The Directory ID for which to get the list of associated Amazon SNS topics. If this member is null, associations for all Directory IDs are returned.</p>
            topic_names: <p>A list of Amazon SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe event topics
            The following example obtains information about which SNS topics receive status messages from the specified directory.

            >>> await client.describe_event_topics(directory_id='d-92654abfed', topic_names=['snstopicexample'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_event_topics_request.DescribeEventTopicsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_event_topics_result.DescribeEventTopicsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_event_topics

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_event_topics.async_describe_event_topics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_event_topics_request.DescribeEventTopicsRequest = {}
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if topic_names is not None:
            input_["topic_names"] = topic_names

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_hybrid_ad_update(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        update_type: Optional[
            "capo_directory_service.types.hybrid_update_type.HybridUpdateType"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_directory_service.types.describe_hybrid_ad_update_result.DescribeHybridADUpdateResult":
        """<p>Retrieves information about update activities for a hybrid directory. This operation provides details about configuration changes, administrator account updates, and self-managed instance settings (IDs and DNS IPs).</p>

        Args:
            directory_id: <p>The identifier of the hybrid directory for which to retrieve update information.</p>
            update_type: <p>The type of update activities to retrieve. Valid values include <code>SelfManagedInstances</code> and <code>HybridAdministratorAccount</code>.</p>
            next_token: <p>The pagination token from a previous request to <a>DescribeHybridADUpdate</a>. Pass null if this is the first request.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_hybrid_ad_update_request.DescribeHybridADUpdateRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_hybrid_ad_update_result.DescribeHybridADUpdateResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_hybrid_ad_update

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_hybrid_ad_update.async_describe_hybrid_ad_update(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_hybrid_ad_update_request.DescribeHybridADUpdateRequest = {
            "directory_id": directory_id
        }
        if update_type is not None:
            input_["update_type"] = update_type
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_ldaps_settings(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        type: Optional["capo_directory_service.types.ldaps_type.LDAPSType"] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.page_limit.PageLimit"] = None,
    ) -> "capo_directory_service.types.describe_ldaps_settings_result.DescribeLDAPSSettingsResult":
        """<p>Describes the status of LDAP security for the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            type: <p>The type of LDAP security to enable. Currently only the value <code>Client</code> is supported.</p>
            next_token: <p>The type of next token used for pagination.</p>
            limit: <p>Specifies the number of items that should be displayed on one page.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_ldaps_settings_request.DescribeLDAPSSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_ldaps_settings_result.DescribeLDAPSSettingsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_ldaps_settings

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_ldaps_settings.async_describe_ldaps_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_ldaps_settings_request.DescribeLDAPSSettingsRequest = {
            "directory_id": directory_id
        }
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_ldaps_settings(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        type: Optional["capo_directory_service.types.ldaps_type.LDAPSType"] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.ldaps_setting_info.LDAPSSettingInfo]":
        _token = next_token
        while True:
            _response = await self.describe_ldaps_settings(
                directory_id,
                config_overrides=config_overrides,
                type=type,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("ldaps_settings_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_regions(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        region_name: Optional[
            "capo_directory_service.types.region_name.RegionName"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_directory_service.types.describe_regions_result.DescribeRegionsResult":
        """<p>Provides information about the Regions that are configured for multi-Region replication.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            region_name: <p>The name of the Region. For example, <code>us-east-1</code>.</p>
            next_token: <p>The <code>DescribeRegionsResult.NextToken</code> value from a previous call to <a>DescribeRegions</a>. Pass null if this is the first call.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_regions_request.DescribeRegionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_regions_result.DescribeRegionsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_regions

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_regions.async_describe_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_regions_request.DescribeRegionsRequest = {
            "directory_id": directory_id
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_regions(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        region_name: Optional[
            "capo_directory_service.types.region_name.RegionName"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_directory_service.types.region_description.RegionDescription]":
        _token = next_token
        while True:
            _response = await self.describe_regions(
                directory_id,
                config_overrides=config_overrides,
                region_name=region_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("regions_description",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_settings(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        status: Optional[
            "capo_directory_service.types.directory_configuration_status.DirectoryConfigurationStatus"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_directory_service.types.describe_settings_result.DescribeSettingsResult":
        """<p>Retrieves information about the configurable settings for the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to retrieve information.</p>
            status: <p>The status of the directory settings for which to retrieve information.</p>
            next_token: <p>The <code>DescribeSettingsResult.NextToken</code> value from a previous call to <a>DescribeSettings</a>. Pass null if this is the first call.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_settings_request.DescribeSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_settings_result.DescribeSettingsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_settings

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_settings.async_describe_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_settings_request.DescribeSettingsRequest = {
            "directory_id": directory_id
        }
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_shared_directories(
        self,
        owner_directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        shared_directory_ids: Optional[
            "capo_directory_service.types.directory_ids.DirectoryIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.describe_shared_directories_result.DescribeSharedDirectoriesResult":
        """<p>Returns the shared directories in your account. </p>

        Args:
            owner_directory_id: <p>Returns the identifier of the directory in the directory owner account. </p>
            shared_directory_ids: <p>A list of identifiers of all shared directories in your account. </p>
            next_token: <p>The <code>DescribeSharedDirectoriesResult.NextToken</code> value from a previous call to <a>DescribeSharedDirectories</a>. Pass null if this is the first call. </p>
            limit: <p>The number of shared directories to return in the response object.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_shared_directories_request.DescribeSharedDirectoriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_shared_directories_result.DescribeSharedDirectoriesResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_shared_directories

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_shared_directories.async_describe_shared_directories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_shared_directories_request.DescribeSharedDirectoriesRequest = {
            "owner_directory_id": owner_directory_id
        }
        if shared_directory_ids is not None:
            input_["shared_directory_ids"] = shared_directory_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_shared_directories(
        self,
        owner_directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        shared_directory_ids: Optional[
            "capo_directory_service.types.directory_ids.DirectoryIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.shared_directory.SharedDirectory]":
        _token = next_token
        while True:
            _response = await self.describe_shared_directories(
                owner_directory_id,
                config_overrides=config_overrides,
                shared_directory_ids=shared_directory_ids,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("shared_directories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        snapshot_ids: Optional[
            "capo_directory_service.types.snapshot_ids.SnapshotIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> (
        "capo_directory_service.types.describe_snapshots_result.DescribeSnapshotsResult"
    ):
        """<p>Obtains information about the directory snapshots that belong to this account.</p> <p>This operation supports pagination with the use of the <i>NextToken</i> request and response parameters. If more results are available, the <i>DescribeSnapshots.NextToken</i> member contains a token that you pass in the next call to <a>DescribeSnapshots</a> to retrieve the next set of items.</p> <p>You can also specify a maximum number of return results with the <i>Limit</i> parameter.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to retrieve snapshot information.</p>
            snapshot_ids: <p>A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the <i>Limit</i> and <i>NextToken</i> members.</p>
            next_token: <p>The <i>DescribeSnapshotsResult.NextToken</i> value from a previous call to <a>DescribeSnapshots</a>. Pass null if this is the first call.</p>
            limit: <p>The maximum number of objects to return.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe snapshots
            The following example obtains information about a specified directory snapshot.

            >>> await client.describe_snapshots(directory_id='d-92654abfed', snapshot_ids=['s-9267f6da4e'], limit=0)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_snapshots_request.DescribeSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_snapshots_result.DescribeSnapshotsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_snapshots

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_snapshots.async_describe_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_snapshots_request.DescribeSnapshotsRequest = {}
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if snapshot_ids is not None:
            input_["snapshot_ids"] = snapshot_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        snapshot_ids: Optional[
            "capo_directory_service.types.snapshot_ids.SnapshotIds"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.snapshot.Snapshot]":
        _token = next_token
        while True:
            _response = await self.describe_snapshots(
                config_overrides=config_overrides,
                directory_id=directory_id,
                snapshot_ids=snapshot_ids,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_trusts(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        trust_ids: Optional["capo_directory_service.types.trust_ids.TrustIds"] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.describe_trusts_result.DescribeTrustsResult":
        """<p>Obtains information about the trust relationships for this account.</p> <p>If no input parameters are provided, such as DirectoryId or TrustIds, this request describes all the trust relationships belonging to the account.</p>

        Args:
            directory_id: <p>The Directory ID of the Amazon Web Services directory that is a part of the requested trust relationship.</p>
            trust_ids: <p>A list of identifiers of the trust relationships for which to obtain the information. If this member is null, all trust relationships that belong to the current account are returned.</p> <p>An empty list results in an <code>InvalidParameterException</code> being thrown.</p>
            next_token: <p>The <i>DescribeTrustsResult.NextToken</i> value from a previous call to <a>DescribeTrusts</a>. Pass null if this is the first call.</p>
            limit: <p>The maximum number of objects to return.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe a trust
            The following example obtains information about the trust relationship for a specified directory.

            >>> await client.describe_trusts(directory_id='d-92654abfed', trust_ids=['t-9267353df0'], limit=0)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_trusts_request.DescribeTrustsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_trusts_result.DescribeTrustsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_trusts

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_trusts.async_describe_trusts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_trusts_request.DescribeTrustsRequest = {}
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if trust_ids is not None:
            input_["trust_ids"] = trust_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_trusts(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        trust_ids: Optional["capo_directory_service.types.trust_ids.TrustIds"] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.trust.Trust]":
        _token = next_token
        while True:
            _response = await self.describe_trusts(
                config_overrides=config_overrides,
                directory_id=directory_id,
                trust_ids=trust_ids,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("trusts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_update_directory(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        update_type: "capo_directory_service.types.update_type.UpdateType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        region_name: Optional[
            "capo_directory_service.types.region_name.RegionName"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
    ) -> "capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult":
        """<p> Describes the updates of a directory for a particular update type. </p>

        Args:
            directory_id: <p> The unique identifier of the directory. </p>
            update_type: <p> The type of updates you want to describe for the directory. </p>
            region_name: <p> The name of the Region. </p>
            next_token: <p> The <code>DescribeUpdateDirectoryResult</code>. NextToken value from a previous call to <a>DescribeUpdateDirectory</a>. Pass null if this is the first call. </p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.describe_update_directory_request.DescribeUpdateDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.describe_update_directory_result.DescribeUpdateDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.describe_update_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.describe_update_directory.async_describe_update_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.describe_update_directory_request.DescribeUpdateDirectoryRequest = {
            "directory_id": directory_id,
            "update_type": update_type,
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_update_directory(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        update_type: "capo_directory_service.types.update_type.UpdateType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        region_name: Optional[
            "capo_directory_service.types.region_name.RegionName"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_directory_service.types.update_info_entry.UpdateInfoEntry]"
    ):
        _token = next_token
        while True:
            _response = await self.describe_update_directory(
                directory_id,
                update_type,
                config_overrides=config_overrides,
                region_name=region_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("update_activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disable_ca_enrollment_policy(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.disable_ca_enrollment_policy_result.DisableCAEnrollmentPolicyResult":
        """<p>Disables the certificate authority (CA) enrollment policy for the specified directory. This stops automatic certificate enrollment and management for domain-joined clients, but does not affect existing certificates.</p> <important> <p>Disabling the CA enrollment policy prevents new certificates from being automatically enrolled, but existing certificates remain valid and functional until they expire.</p> </important>

        Args:
            directory_id: <p>The identifier of the directory for which to disable the CA enrollment policy.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.disable_already_in_progress_exception.DisableAlreadyInProgressException: <p>A disable operation for CA enrollment policy is already in progress for this directory.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.disable_ca_enrollment_policy_request.DisableCAEnrollmentPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.disable_ca_enrollment_policy_result.DisableCAEnrollmentPolicyResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.disable_ca_enrollment_policy

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.disable_ca_enrollment_policy.async_disable_ca_enrollment_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.disable_ca_enrollment_policy_request.DisableCAEnrollmentPolicyRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_client_authentication(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        type: "capo_directory_service.types.client_authentication_type.ClientAuthenticationType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.disable_client_authentication_result.DisableClientAuthenticationResult":
        """<p>Disables alternative client authentication methods for the specified directory. </p>

        Args:
            directory_id: <p>The identifier of the directory </p>
            type: <p>The type of client authentication to disable. Currently the only parameter <code>"SmartCard"</code> is supported.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_client_auth_status_exception.InvalidClientAuthStatusException: <p>Client authentication is already enabled.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.disable_client_authentication_request.DisableClientAuthenticationRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.disable_client_authentication_result.DisableClientAuthenticationResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.disable_client_authentication

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.disable_client_authentication.async_disable_client_authentication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.disable_client_authentication_request.DisableClientAuthenticationRequest = {
            "directory_id": directory_id,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_directory_data_access(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.disable_directory_data_access_result.DisableDirectoryDataAccessResult":
        """<p>Deactivates access to directory data via the Directory Service Data API for the specified directory. For more information, see <a href="https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html">Directory Service Data API Reference</a>.</p>

        Args:
            directory_id: <p>The directory identifier.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_in_desired_state_exception.DirectoryInDesiredStateException: <p> The directory is already updated to desired update type settings. </p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.disable_directory_data_access_request.DisableDirectoryDataAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.disable_directory_data_access_result.DisableDirectoryDataAccessResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.disable_directory_data_access

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.disable_directory_data_access.async_disable_directory_data_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.disable_directory_data_access_request.DisableDirectoryDataAccessRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_ldaps(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        type: "capo_directory_service.types.ldaps_type.LDAPSType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.disable_ldaps_result.DisableLDAPSResult":
        """<p>Deactivates LDAP secure calls for the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            type: <p>The type of LDAP security to enable. Currently only the value <code>Client</code> is supported.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.invalid_ldaps_status_exception.InvalidLDAPSStatusException: <p>The LDAP activities could not be performed because they are limited by the LDAPS status.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.disable_ldaps_request.DisableLDAPSRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.disable_ldaps_result.DisableLDAPSResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.disable_ldaps

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.disable_ldaps.async_disable_ldaps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.disable_ldaps_request.DisableLDAPSRequest = {
            "directory_id": directory_id,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_radius(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.disable_radius_result.DisableRadiusResult":
        """<p>Disables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to disable MFA.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable radius
            The following example disables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector directory.

            >>> await client.disable_radius(directory_id='d-92654abfed')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.disable_radius_request.DisableRadiusRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.disable_radius_result.DisableRadiusResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.disable_radius

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.disable_radius.async_disable_radius(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.disable_radius_request.DisableRadiusRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_sso(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        user_name: Optional["capo_directory_service.types.user_name.UserName"] = None,
        password: Optional[
            "capo_directory_service.types.connect_password.ConnectPassword"
        ] = None,
    ) -> "capo_directory_service.types.disable_sso_result.DisableSsoResult":
        """<p>Disables single-sign on for a directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to disable single-sign on.</p>
            user_name: <p>The username of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. This account must have privileges to remove a service principal name.</p> <p>If the AD Connector service account does not have privileges to remove a service principal name, you can specify an alternate account with the <i>UserName</i> and <i>Password</i> parameters. These credentials are only used to disable single sign-on and are not stored by the service. The AD Connector service account is not changed.</p>
            password: <p>The password of an alternate account to use to disable single-sign on. This is only used for AD Connector directories. For more information, see the <i>UserName</i> parameter.</p>

        Raises:
            capo_directory_service.errors.authentication_failed_exception.AuthenticationFailedException: <p>An authentication error occurred.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>The account does not have sufficient permission to perform the operation.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To disable SSO
            The following example disables single sign-on for a specified directory.

            >>> await client.disable_sso(directory_id='d-92654abfed', user_name='Admin', password='Str0ngP@ssw0rd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.disable_sso_request.DisableSsoRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.disable_sso_result.DisableSsoResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.disable_sso

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.disable_sso.async_disable_sso(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.disable_sso_request.DisableSsoRequest = {
            "directory_id": directory_id
        }
        if user_name is not None:
            input_["user_name"] = user_name
        if password is not None:
            input_["password"] = password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_ca_enrollment_policy(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        pca_connector_arn: "capo_directory_service.types.pca_connector_arn.PcaConnectorArn",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.enable_ca_enrollment_policy_result.EnableCAEnrollmentPolicyResult":
        """<p>Enables certificate authority (CA) enrollment policy for the specified directory. This allows domain-joined clients to automatically request and receive certificates from the specified Amazon Web Services Private Certificate Authority.</p> <note> <p>Before enabling CA enrollment, ensure that the PCA connector is properly configured and accessible from the directory. The connector must be in an active state and have the necessary permissions.</p> </note>

        Args:
            directory_id: <p>The identifier of the directory for which to enable the CA enrollment policy.</p>
            pca_connector_arn: <p>The Amazon Resource Name (ARN) of the Private Certificate Authority (PCA) connector to use for automatic certificate enrollment. This connector must be properly configured and accessible from the directory.</p> <p>The ARN format is: <code>arn:aws:pca-connector-ad:<i>region</i>:<i>account-id</i>:connector/<i>connector-id</i> </code> </p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.enable_already_in_progress_exception.EnableAlreadyInProgressException: <p>An enable operation for CA enrollment policy is already in progress for this directory.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.enable_ca_enrollment_policy_request.EnableCAEnrollmentPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.enable_ca_enrollment_policy_result.EnableCAEnrollmentPolicyResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.enable_ca_enrollment_policy

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.enable_ca_enrollment_policy.async_enable_ca_enrollment_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.enable_ca_enrollment_policy_request.EnableCAEnrollmentPolicyRequest = {
            "directory_id": directory_id,
            "pca_connector_arn": pca_connector_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_client_authentication(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        type: "capo_directory_service.types.client_authentication_type.ClientAuthenticationType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.enable_client_authentication_result.EnableClientAuthenticationResult":
        """<p>Enables alternative client authentication methods for the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the specified directory. </p>
            type: <p>The type of client authentication to enable. Currently only the value <code>SmartCard</code> is supported. Smart card authentication in AD Connector requires that you enable Kerberos Constrained Delegation for the Service User to the LDAP service in your self-managed AD. </p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_client_auth_status_exception.InvalidClientAuthStatusException: <p>Client authentication is already enabled.</p>
            capo_directory_service.errors.no_available_certificate_exception.NoAvailableCertificateException: <p>Client authentication setup could not be completed because at least one valid certificate must be registered in the system.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.enable_client_authentication_request.EnableClientAuthenticationRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.enable_client_authentication_result.EnableClientAuthenticationResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.enable_client_authentication

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.enable_client_authentication.async_enable_client_authentication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.enable_client_authentication_request.EnableClientAuthenticationRequest = {
            "directory_id": directory_id,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_directory_data_access(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.enable_directory_data_access_result.EnableDirectoryDataAccessResult":
        """<p>Enables access to directory data via the Directory Service Data API for the specified directory. For more information, see <a href="https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html">Directory Service Data API Reference</a>.</p>

        Args:
            directory_id: <p>The directory identifier.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_in_desired_state_exception.DirectoryInDesiredStateException: <p> The directory is already updated to desired update type settings. </p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.enable_directory_data_access_request.EnableDirectoryDataAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.enable_directory_data_access_result.EnableDirectoryDataAccessResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.enable_directory_data_access

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.enable_directory_data_access.async_enable_directory_data_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.enable_directory_data_access_request.EnableDirectoryDataAccessRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_ldaps(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        type: "capo_directory_service.types.ldaps_type.LDAPSType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.enable_ldaps_result.EnableLDAPSResult":
        """<p>Activates the switch for the specific directory to always use LDAP secure calls.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            type: <p>The type of LDAP security to enable. Currently only the value <code>Client</code> is supported.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.invalid_ldaps_status_exception.InvalidLDAPSStatusException: <p>The LDAP activities could not be performed because they are limited by the LDAPS status.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.no_available_certificate_exception.NoAvailableCertificateException: <p>Client authentication setup could not be completed because at least one valid certificate must be registered in the system.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.enable_ldaps_request.EnableLDAPSRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.enable_ldaps_result.EnableLDAPSResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.enable_ldaps

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.enable_ldaps.async_enable_ldaps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.enable_ldaps_request.EnableLDAPSRequest = {
            "directory_id": directory_id,
            "type": type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_radius(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        radius_settings: "capo_directory_service.types.radius_settings.RadiusSettings",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.enable_radius_result.EnableRadiusResult":
        """<p>Enables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector or Microsoft AD directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to enable MFA.</p>
            radius_settings: <p>A <a>RadiusSettings</a> object that contains information about the RADIUS server.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The specified entity already exists.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable radius
            The following example enables multi-factor authentication (MFA) with the Remote Authentication Dial In User Service (RADIUS) server for an AD Connector directory.

            >>> await client.enable_radius(directory_id='d-92654abfed', radius_settings={'DisplayLabel': 'MyRadius', 'UseSameUsername': True, 'RadiusTimeout': 1, 'AuthenticationProtocol': 'PAP', 'RadiusPort': 1200, 'RadiusRetries': 2, 'SharedSecret': '123456789', 'RadiusServers': ['172.168.111.12']})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.enable_radius_request.EnableRadiusRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.enable_radius_result.EnableRadiusResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.enable_radius

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.enable_radius.async_enable_radius(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.enable_radius_request.EnableRadiusRequest = {
            "directory_id": directory_id,
            "radius_settings": radius_settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_sso(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        user_name: Optional["capo_directory_service.types.user_name.UserName"] = None,
        password: Optional[
            "capo_directory_service.types.connect_password.ConnectPassword"
        ] = None,
    ) -> "capo_directory_service.types.enable_sso_result.EnableSsoResult":
        """<p>Enables single sign-on for a directory. Single sign-on allows users in your directory to access certain Amazon Web Services services from a computer joined to the directory without having to enter their credentials separately.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to enable single-sign on.</p>
            user_name: <p>The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.</p> <p>If the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the <i>UserName</i> and <i>Password</i> parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.</p>
            password: <p>The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the <i>UserName</i> parameter.</p>

        Raises:
            capo_directory_service.errors.authentication_failed_exception.AuthenticationFailedException: <p>An authentication error occurred.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.insufficient_permissions_exception.InsufficientPermissionsException: <p>The account does not have sufficient permission to perform the operation.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To enable SSO
            To enable single sign-on for a specified directory.

            >>> await client.enable_sso(directory_id='d-92654abfed', user_name='Admin', password='Str0ngP@ssw0rd')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.enable_sso_request.EnableSsoRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.enable_sso_result.EnableSsoResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.enable_sso

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.enable_sso.async_enable_sso(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.enable_sso_request.EnableSsoRequest = {
            "directory_id": directory_id
        }
        if user_name is not None:
            input_["user_name"] = user_name
        if password is not None:
            input_["password"] = password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_directory_limits(
        self, *, config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None
    ) -> "capo_directory_service.types.get_directory_limits_result.GetDirectoryLimitsResult":
        """<p>Obtains directory limit information for the current Region.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get directory limits
            The following example obtains directory limit information for the current region.

            >>> await client.get_directory_limits()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.get_directory_limits_request.GetDirectoryLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.get_directory_limits_result.GetDirectoryLimitsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.get_directory_limits

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.get_directory_limits.async_get_directory_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.get_directory_limits_request.GetDirectoryLimitsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_snapshot_limits(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.get_snapshot_limits_result.GetSnapshotLimitsResult":
        """<p>Obtains the manual snapshot limits for a directory.</p>

        Args:
            directory_id: <p>Contains the identifier of the directory to obtain the limits for.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get snapshot limits
            The following example obtains the manual snapshot limits for a specified directory.

            >>> await client.get_snapshot_limits(directory_id='d-92654abfed')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.get_snapshot_limits_request.GetSnapshotLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.get_snapshot_limits_result.GetSnapshotLimitsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.get_snapshot_limits

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.get_snapshot_limits.async_get_snapshot_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.get_snapshot_limits_request.GetSnapshotLimitsRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ad_assessments(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "capo_directory_service.types.assessment_limit.AssessmentLimit"
        ] = None,
    ) -> "capo_directory_service.types.list_ad_assessments_result.ListADAssessmentsResult":
        """<p>Retrieves a list of directory assessments for the specified directory or all assessments in your account. Use this operation to monitor assessment status and manage multiple assessments.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to list assessments. If not specified, all assessments in your account are returned.</p>
            next_token: <p>The pagination token from a previous request to <a>ListADAssessments</a>. Pass null if this is the first request.</p>
            limit: <p>The maximum number of assessment summaries to return.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.list_ad_assessments_request.ListADAssessmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.list_ad_assessments_result.ListADAssessmentsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.list_ad_assessments

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.list_ad_assessments.async_list_ad_assessments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.list_ad_assessments_request.ListADAssessmentsRequest = {}
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ad_assessments(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional[
            "capo_directory_service.types.assessment_limit.AssessmentLimit"
        ] = None,
    ) -> "AsyncIterator[capo_directory_service.types.assessment_summary.AssessmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_ad_assessments(
                config_overrides=config_overrides,
                directory_id=directory_id,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("assessments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_certificates(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.page_limit.PageLimit"] = None,
    ) -> "capo_directory_service.types.list_certificates_result.ListCertificatesResult":
        """<p>For the specified directory, lists all the certificates registered for a secure LDAP or client certificate authentication.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            next_token: <p>A token for requesting another page of certificates if the <code>NextToken</code> response element indicates that more certificates are available. Use the value of the returned <code>NextToken</code> element in your request until the token comes back as <code>null</code>. Pass <code>null</code> if this is the first call.</p>
            limit: <p>The number of items that should show up on one page</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.list_certificates_request.ListCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.list_certificates_result.ListCertificatesResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.list_certificates

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.list_certificates.async_list_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.list_certificates_request.ListCertificatesRequest = {
            "directory_id": directory_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_certificates(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.page_limit.PageLimit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.certificate_info.CertificateInfo]":
        _token = next_token
        while True:
            _response = await self.list_certificates(
                directory_id,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("certificates_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ip_routes(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.list_ip_routes_result.ListIpRoutesResult":
        """<p>Lists the address blocks that you have added to a directory.</p>

        Args:
            directory_id: <p>Identifier (ID) of the directory for which you want to retrieve the IP addresses.</p>
            next_token: <p>The <i>ListIpRoutes.NextToken</i> value from a previous call to <a>ListIpRoutes</a>. Pass null if this is the first call.</p>
            limit: <p>Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list IP routes
            The following example lists the address blocks that have been added to a specified directory.

            >>> await client.list_ip_routes(directory_id='d-92654abfed', limit=0)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.list_ip_routes_request.ListIpRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.list_ip_routes_result.ListIpRoutesResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.list_ip_routes

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.list_ip_routes.async_list_ip_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.list_ip_routes_request.ListIpRoutesRequest = {
            "directory_id": directory_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ip_routes(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.ip_route_info.IpRouteInfo]":
        _token = next_token
        while True:
            _response = await self.list_ip_routes(
                directory_id,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("ip_routes_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_log_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.list_log_subscriptions_result.ListLogSubscriptionsResult":
        """<p>Lists the active log subscriptions for the Amazon Web Services account.</p>

        Args:
            directory_id: <p>If a <i>DirectoryID</i> is provided, lists only the log subscription associated with that directory. If no <i>DirectoryId</i> is provided, lists all log subscriptions associated with your Amazon Web Services account. If there are no log subscriptions for the Amazon Web Services account or the directory, an empty list will be returned.</p>
            next_token: <p>The token for the next set of items to return.</p>
            limit: <p>The maximum number of items returned.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.list_log_subscriptions_request.ListLogSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.list_log_subscriptions_result.ListLogSubscriptionsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.list_log_subscriptions

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.list_log_subscriptions.async_list_log_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.list_log_subscriptions_request.ListLogSubscriptionsRequest = {}
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_log_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.log_subscription.LogSubscription]":
        _token = next_token
        while True:
            _response = await self.list_log_subscriptions(
                config_overrides=config_overrides,
                directory_id=directory_id,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("log_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schema_extensions(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.list_schema_extensions_result.ListSchemaExtensionsResult":
        """<p>Lists all schema extensions applied to a Microsoft AD Directory.</p>

        Args:
            directory_id: <p>The identifier of the directory from which to retrieve the schema extension information.</p>
            next_token: <p>The <code>ListSchemaExtensions.NextToken</code> value from a previous call to <code>ListSchemaExtensions</code>. Pass null if this is the first call.</p>
            limit: <p>The maximum number of items to return.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list schema extensions
            The following example lists all schema extensions applied to a specified Microsoft AD Directory.

            >>> await client.list_schema_extensions(directory_id='d-92654abfed', limit=0)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.list_schema_extensions_request.ListSchemaExtensionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.list_schema_extensions_result.ListSchemaExtensionsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.list_schema_extensions

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.list_schema_extensions.async_list_schema_extensions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.list_schema_extensions_request.ListSchemaExtensionsRequest = {
            "directory_id": directory_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_schema_extensions(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.schema_extension_info.SchemaExtensionInfo]":
        _token = next_token
        while True:
            _response = await self.list_schema_extensions(
                directory_id,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("schema_extensions_info",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_id: "capo_directory_service.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "capo_directory_service.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>Lists all tags on a directory.</p>

        Args:
            resource_id: <p>Identifier (ID) of the directory for which you want to retrieve tags.</p>
            next_token: <p>Reserved for future use.</p>
            limit: <p>Reserved for future use.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> value is not valid.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list tags for a directory
            The following example lists all tags associated with a specified directory.

            >>> await client.list_tags_for_resource(resource_id='d-92654abfed', limit=0)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_id": resource_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_tags_for_resource(
        self,
        resource_id: "capo_directory_service.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        next_token: Optional[
            "capo_directory_service.types.next_token.NextToken"
        ] = None,
        limit: Optional["capo_directory_service.types.limit.Limit"] = None,
    ) -> "AsyncIterator[capo_directory_service.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_id,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def register_certificate(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        certificate_data: "capo_directory_service.types.certificate_data.CertificateData",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        type: Optional[
            "capo_directory_service.types.certificate_type.CertificateType"
        ] = None,
        client_cert_auth_settings: Optional[
            "capo_directory_service.types.client_cert_auth_settings.ClientCertAuthSettings"
        ] = None,
    ) -> "capo_directory_service.types.register_certificate_result.RegisterCertificateResult":
        """<p>Registers a certificate for a secure LDAP or client certificate authentication.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            certificate_data: <p>The certificate PEM string that needs to be registered.</p>
            type: <p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>
            client_cert_auth_settings: <p>A <code>ClientCertAuthSettings</code> object that contains client certificate authentication settings.</p>

        Raises:
            capo_directory_service.errors.certificate_already_exists_exception.CertificateAlreadyExistsException: <p>The certificate has already been registered into the system.</p>
            capo_directory_service.errors.certificate_limit_exceeded_exception.CertificateLimitExceededException: <p>The certificate could not be added because the certificate limit has been reached.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.invalid_certificate_exception.InvalidCertificateException: <p>The certificate PEM that was provided has incorrect encoding.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.register_certificate_request.RegisterCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.register_certificate_result.RegisterCertificateResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.register_certificate

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.register_certificate.async_register_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.register_certificate_request.RegisterCertificateRequest = {
            "directory_id": directory_id,
            "certificate_data": certificate_data,
        }
        if type is not None:
            input_["type"] = type
        if client_cert_auth_settings is not None:
            input_["client_cert_auth_settings"] = client_cert_auth_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_event_topic(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        topic_name: "capo_directory_service.types.topic_name.TopicName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.register_event_topic_result.RegisterEventTopicResult":
        """<p>Associates a directory with an Amazon SNS topic. This establishes the directory as a publisher to the specified Amazon SNS topic. You can then receive email or text (SMS) messages when the status of your directory changes. You get notified if your directory goes from an Active status to an Impaired or Inoperable status. You also receive a notification when the directory returns to an Active status.</p>

        Args:
            directory_id: <p>The Directory ID that will publish status messages to the Amazon SNS topic.</p>
            topic_name: <p>The Amazon SNS topic name to which the directory will publish status messages. This Amazon SNS topic must be in the same region as the specified Directory ID.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To register an event topic
            The following example associates a directory with an SNS topic.

            >>> await client.register_event_topic(directory_id='d-92654abfed', topic_name='snstopicexample')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.register_event_topic_request.RegisterEventTopicRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.register_event_topic_result.RegisterEventTopicResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.register_event_topic

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.register_event_topic.async_register_event_topic(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.register_event_topic_request.RegisterEventTopicRequest = {
            "directory_id": directory_id,
            "topic_name": topic_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_shared_directory(
        self,
        shared_directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.reject_shared_directory_result.RejectSharedDirectoryResult":
        """<p>Rejects a directory sharing request that was sent from the directory owner account.</p>

        Args:
            shared_directory_id: <p>Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_already_shared_exception.DirectoryAlreadySharedException: <p>The specified directory has already been shared with this Amazon Web Services account.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.reject_shared_directory_request.RejectSharedDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.reject_shared_directory_result.RejectSharedDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.reject_shared_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.reject_shared_directory.async_reject_shared_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.reject_shared_directory_request.RejectSharedDirectoryRequest = {
            "shared_directory_id": shared_directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_ip_routes(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        cidr_ips: Optional["capo_directory_service.types.cidr_ips.CidrIps"] = None,
        cidr_ipv6s: Optional[
            "capo_directory_service.types.cidr_ipv6s.CidrIpv6s"
        ] = None,
    ) -> "capo_directory_service.types.remove_ip_routes_result.RemoveIpRoutesResult":
        """<p>Removes IP address blocks from a directory.</p>

        Args:
            directory_id: <p>Identifier (ID) of the directory from which you want to remove the IP addresses.</p>
            cidr_ips: <p>IP address blocks that you want to remove.</p>
            cidr_ipv6s: <p>IPv6 address blocks that you want to remove.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove IP routes
            The following example removes IP address blocks from a specified directory.

            >>> await client.remove_ip_routes(directory_id='d-92654abfed', cidr_ips=['12.12.12.12/32'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.remove_ip_routes_request.RemoveIpRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.remove_ip_routes_result.RemoveIpRoutesResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.remove_ip_routes

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.remove_ip_routes.async_remove_ip_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.remove_ip_routes_request.RemoveIpRoutesRequest = {
            "directory_id": directory_id
        }
        if cidr_ips is not None:
            input_["cidr_ips"] = cidr_ips
        if cidr_ipv6s is not None:
            input_["cidr_ipv6s"] = cidr_ipv6s

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_region(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.remove_region_result.RemoveRegionResult":
        """<p>Stops all replication and removes the domain controllers from the specified Region. You cannot remove the primary Region with this operation. Instead, use the <code>DeleteDirectory</code> API.</p>

        Args:
            directory_id: <p>The identifier of the directory for which you want to remove Region replication.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.remove_region_request.RemoveRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.remove_region_result.RemoveRegionResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.remove_region

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.remove_region.async_remove_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.remove_region_request.RemoveRegionRequest = {
            "directory_id": directory_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags_from_resource(
        self,
        resource_id: "capo_directory_service.types.resource_id.ResourceId",
        tag_keys: "capo_directory_service.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.remove_tags_from_resource_result.RemoveTagsFromResourceResult":
        """<p>Removes tags from a directory.</p>

        Args:
            resource_id: <p>Identifier (ID) of the directory from which to remove the tag.</p>
            tag_keys: <p>The tag key (name) of the tag to be removed.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a directory
            The following example removes a tag from a specified directory.

            >>> await client.remove_tags_from_resource(resource_id='d-92654abfed', tag_keys=['environment'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.remove_tags_from_resource_request.RemoveTagsFromResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.remove_tags_from_resource_result.RemoveTagsFromResourceResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.remove_tags_from_resource

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.remove_tags_from_resource.async_remove_tags_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.remove_tags_from_resource_request.RemoveTagsFromResourceRequest = {
            "resource_id": resource_id,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_user_password(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        user_name: "capo_directory_service.types.customer_user_name.CustomerUserName",
        new_password: "capo_directory_service.types.user_password.UserPassword",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.reset_user_password_result.ResetUserPasswordResult":
        """<p>Resets the password for any user in your Managed Microsoft AD or Simple AD directory. Disabled users will become enabled and can be authenticated following the API call.</p> <p>You can reset the password for any user in your directory with the following exceptions:</p> <ul> <li> <p>For Simple AD, you cannot reset the password for any user that is a member of either the <b>Domain Admins</b> or <b>Enterprise Admins</b> group except for the administrator user.</p> </li> <li> <p>For Managed Microsoft AD, you can only reset the password for a user that is in an OU based off of the NetBIOS name that you typed when you created your directory. For example, you cannot reset the password for a user in the <b>Amazon Web Services Reserved</b> OU. For more information about the OU structure for an Managed Microsoft AD directory, see <a href="https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html">What Gets Created</a> in the <i>Directory Service Administration Guide</i>.</p> </li> </ul>

        Args:
            directory_id: <p>Identifier of the Managed Microsoft AD or Simple AD directory in which the user resides.</p>
            user_name: <p>The user name of the user whose password will be reset.</p>
            new_password: <p>The new password that will be reset.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_password_exception.InvalidPasswordException: <p>The new password provided by the user does not meet the password complexity requirements defined in your directory.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.user_does_not_exist_exception.UserDoesNotExistException: <p>The user provided a username that does not exist in your directory.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.reset_user_password_request.ResetUserPasswordRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.reset_user_password_result.ResetUserPasswordResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.reset_user_password

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.reset_user_password.async_reset_user_password(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.reset_user_password_request.ResetUserPasswordRequest = {
            "directory_id": directory_id,
            "user_name": user_name,
            "new_password": new_password,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_from_snapshot(
        self,
        snapshot_id: "capo_directory_service.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.restore_from_snapshot_result.RestoreFromSnapshotResult":
        """<p>Restores a directory using an existing directory snapshot.</p> <p>When you restore a directory from a snapshot, any changes made to the directory after the snapshot date are overwritten.</p> <p>This action returns as soon as the restore operation is initiated. You can monitor the progress of the restore operation by calling the <a>DescribeDirectories</a> operation with the directory identifier. When the <b>DirectoryDescription.Stage</b> value changes to <code>Active</code>, the restore operation is complete.</p>

        Args:
            snapshot_id: <p>The identifier of the snapshot to restore from.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To restore a snapshot
            The following example restores a directory using an existing directory snapshot.

            >>> await client.restore_from_snapshot(snapshot_id='s-9267f6da4e')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.restore_from_snapshot_request.RestoreFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.restore_from_snapshot_result.RestoreFromSnapshotResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.restore_from_snapshot

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.restore_from_snapshot.async_restore_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.restore_from_snapshot_request.RestoreFromSnapshotRequest = {
            "snapshot_id": snapshot_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def share_directory(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        share_target: "capo_directory_service.types.share_target.ShareTarget",
        share_method: "capo_directory_service.types.share_method.ShareMethod",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        share_notes: Optional["capo_directory_service.types.notes.Notes"] = None,
    ) -> "capo_directory_service.types.share_directory_result.ShareDirectoryResult":
        """<p>Shares a specified directory (<code>DirectoryId</code>) in your Amazon Web Services account (directory owner) with another Amazon Web Services account (directory consumer). With this operation you can use your directory from any Amazon Web Services account and from any Amazon VPC within an Amazon Web Services Region.</p> <p>When you share your Managed Microsoft AD directory, Directory Service creates a shared directory in the directory consumer account. This shared directory contains the metadata to provide access to the directory within the directory owner account. The shared directory is visible in all VPCs in the directory consumer account.</p> <p>The <code>ShareMethod</code> parameter determines whether the specified directory can be shared between Amazon Web Services accounts inside the same Amazon Web Services organization (<code>ORGANIZATIONS</code>). It also determines whether you can share the directory with any other Amazon Web Services account either inside or outside of the organization (<code>HANDSHAKE</code>).</p> <p>The <code>ShareNotes</code> parameter is only used when <code>HANDSHAKE</code> is called, which sends a directory sharing request to the directory consumer. </p>

        Args:
            directory_id: <p>Identifier of the Managed Microsoft AD directory that you want to share with other Amazon Web Services accounts.</p>
            share_notes: <p>A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.</p>
            share_target: <p>Identifier for the directory consumer account with whom the directory is to be shared.</p>
            share_method: <p>The method used when sharing a directory to determine whether the directory should be shared within your Amazon Web Services organization (<code>ORGANIZATIONS</code>) or with any Amazon Web Services account by sending a directory sharing request (<code>HANDSHAKE</code>).</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_already_shared_exception.DirectoryAlreadySharedException: <p>The specified directory has already been shared with this Amazon Web Services account.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.invalid_target_exception.InvalidTargetException: <p>The specified shared target is not valid.</p>
            capo_directory_service.errors.organizations_exception.OrganizationsException: <p>Exception encountered while trying to access your Amazon Web Services organization.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.share_limit_exceeded_exception.ShareLimitExceededException: <p>The maximum number of Amazon Web Services accounts that you can share with this directory has been reached.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.share_directory_request.ShareDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.share_directory_result.ShareDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.share_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.share_directory.async_share_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.share_directory_request.ShareDirectoryRequest = {
            "directory_id": directory_id,
            "share_target": share_target,
            "share_method": share_method,
        }
        if share_notes is not None:
            input_["share_notes"] = share_notes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_ad_assessment(
        self,
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        assessment_configuration: Optional[
            "capo_directory_service.types.assessment_configuration.AssessmentConfiguration"
        ] = None,
        directory_id: Optional[
            "capo_directory_service.types.directory_id.DirectoryId"
        ] = None,
    ) -> "capo_directory_service.types.start_ad_assessment_result.StartADAssessmentResult":
        """<p>Initiates a directory assessment to validate your self-managed AD environment for hybrid domain join. The assessment checks compatibility and connectivity of the self-managed AD environment.</p> <p>A directory assessment is automatically created when you create a hybrid directory. There are two types of assessments: <code>CUSTOMER</code> and <code>SYSTEM</code>. Your Amazon Web Services account has a limit of 100 <code>CUSTOMER</code> directory assessments.</p> <p>The assessment process typically takes 30 minutes or more to complete. The assessment process is asynchronous and you can monitor it with <code>DescribeADAssessment</code>.</p> <p>The <code>InstanceIds</code> must have a one-to-one correspondence with <code>CustomerDnsIps</code>, meaning that if the IP address for instance i-10243410 is 10.24.34.100 and the IP address for instance i-10243420 is 10.24.34.200, then the input arrays must maintain the same order relationship, either [10.24.34.100, 10.24.34.200] paired with [i-10243410, i-10243420] or [10.24.34.200, 10.24.34.100] paired with [i-10243420, i-10243410].</p> <p>Note: You must provide exactly one <code>DirectoryId</code> or <code>AssessmentConfiguration</code>.</p>

        Args:
            assessment_configuration: <p>Configuration parameters for the directory assessment, including DNS server information, domain name, Amazon VPC subnet, and Amazon Web Services System Manager managed node details.</p>
            directory_id: <p>The identifier of the directory for which to perform the assessment. This should be an existing directory. If the assessment is not for an existing directory, this parameter should be omitted.</p>

        Raises:
            capo_directory_service.errors.ad_assessment_limit_exceeded_exception.ADAssessmentLimitExceededException: <p>A directory assessment is automatically created when you create a hybrid directory. There are two types of assessments: <code>CUSTOMER</code> and <code>SYSTEM</code>. Your Amazon Web Services account has a limit of 100 <code>CUSTOMER</code> directory assessments.</p> <p>If you attempt to create a hybrid directory; and you already have 100 <code>CUSTOMER</code> directory assessments;, you will encounter an error. Delete assessments to free up capacity before trying again.</p> <p>You can request an increase to your <code>CUSTOMER</code> directory assessment quota by contacting customer support or delete existing CUSTOMER directory assessments; to free up capacity.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.start_ad_assessment_request.StartADAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.start_ad_assessment_result.StartADAssessmentResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.start_ad_assessment

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.start_ad_assessment.async_start_ad_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.start_ad_assessment_request.StartADAssessmentRequest = {}
        if assessment_configuration is not None:
            input_["assessment_configuration"] = assessment_configuration
        if directory_id is not None:
            input_["directory_id"] = directory_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_schema_extension(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        create_snapshot_before_schema_extension: "capo_directory_service.types.create_snapshot_before_schema_extension.CreateSnapshotBeforeSchemaExtension",
        ldif_content: "capo_directory_service.types.ldif_content.LdifContent",
        description: "capo_directory_service.types.description.Description",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.start_schema_extension_result.StartSchemaExtensionResult":
        r"""<p>Applies a schema extension to a Microsoft AD directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which the schema extension will be applied to.</p>
            create_snapshot_before_schema_extension: <p>If true, creates a snapshot of the directory before applying the schema extension.</p>
            ldif_content: <p>The LDIF file represented as a string. To construct the LdifContent string, precede each line as it would be formatted in an ldif file with \n. See the example request below for more details. The file size can be no larger than 1MB.</p>
            description: <p>A description of the schema extension.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.snapshot_limit_exceeded_exception.SnapshotLimitExceededException: <p>The maximum number of manual snapshots for the directory has been reached. You can use the <a>GetSnapshotLimits</a> operation to determine the snapshot limits for a directory.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start a schema extension
            The following example applies a schema extension to a specified Microsoft AD directory.

            >>> await client.start_schema_extension(create_snapshot_before_schema_extension=True, directory_id='d-92654abfed', ldif_content='dn: CN=User,CN=Schema,CN=Configuration,DC=sales,DC=example,DC=com\nchangetype: modify\nadd: mayContain\nmayContain: drink\n-\n\nDN:\nchangetype: modify\nreplace: schemaupdatenow\nschemaupdatenow: 1\n-', description='Adds maycontain attribute to user class. Precede each line as it would be formatted in an ldif file.')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.start_schema_extension_request.StartSchemaExtensionRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.start_schema_extension_result.StartSchemaExtensionResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.start_schema_extension

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.start_schema_extension.async_start_schema_extension(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.start_schema_extension_request.StartSchemaExtensionRequest = {
            "directory_id": directory_id,
            "create_snapshot_before_schema_extension": create_snapshot_before_schema_extension,
            "ldif_content": ldif_content,
            "description": description,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unshare_directory(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        unshare_target: "capo_directory_service.types.unshare_target.UnshareTarget",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.unshare_directory_result.UnshareDirectoryResult":
        """<p>Stops the directory sharing between the directory owner and consumer accounts. </p>

        Args:
            directory_id: <p>The identifier of the Managed Microsoft AD directory that you want to stop sharing.</p>
            unshare_target: <p>Identifier for the directory consumer account with whom the directory has to be unshared.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_not_shared_exception.DirectoryNotSharedException: <p>The specified directory has not been shared with this Amazon Web Services account.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_target_exception.InvalidTargetException: <p>The specified shared target is not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.unshare_directory_request.UnshareDirectoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.unshare_directory_result.UnshareDirectoryResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.unshare_directory

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.unshare_directory.async_unshare_directory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.unshare_directory_request.UnshareDirectoryRequest = {
            "directory_id": directory_id,
            "unshare_target": unshare_target,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_conditional_forwarder(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        remote_domain_name: "capo_directory_service.types.remote_domain_name.RemoteDomainName",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        dns_ip_addrs: Optional[
            "capo_directory_service.types.dns_ip_addrs.DnsIpAddrs"
        ] = None,
        dns_ipv6_addrs: Optional[
            "capo_directory_service.types.dns_ipv6_addrs.DnsIpv6Addrs"
        ] = None,
    ) -> "capo_directory_service.types.update_conditional_forwarder_result.UpdateConditionalForwarderResult":
        """<p>Updates a conditional forwarder that has been set up for your Amazon Web Services directory.</p>

        Args:
            directory_id: <p>The directory ID of the Amazon Web Services directory for which to update the conditional forwarder.</p>
            remote_domain_name: <p>The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.</p>
            dns_ip_addrs: <p>The updated IP addresses of the remote DNS server associated with the conditional forwarder.</p>
            dns_ipv6_addrs: <p>The updated IPv6 addresses of the remote DNS server associated with the conditional forwarder.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a conditional forwarder
            The following example updates a conditional forwarder for a specified directory.

            >>> await client.update_conditional_forwarder(directory_id='d-92654abfed', remote_domain_name='sales.example.com', dns_ip_addrs=['172.168.101.11'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_conditional_forwarder_request.UpdateConditionalForwarderRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_conditional_forwarder_result.UpdateConditionalForwarderResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_conditional_forwarder

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_conditional_forwarder.async_update_conditional_forwarder(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_conditional_forwarder_request.UpdateConditionalForwarderRequest = {
            "directory_id": directory_id,
            "remote_domain_name": remote_domain_name,
        }
        if dns_ip_addrs is not None:
            input_["dns_ip_addrs"] = dns_ip_addrs
        if dns_ipv6_addrs is not None:
            input_["dns_ipv6_addrs"] = dns_ipv6_addrs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_directory_setup(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        update_type: "capo_directory_service.types.update_type.UpdateType",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        os_update_settings: Optional[
            "capo_directory_service.types.os_update_settings.OSUpdateSettings"
        ] = None,
        directory_size_update_settings: Optional[
            "capo_directory_service.types.directory_size_update_settings.DirectorySizeUpdateSettings"
        ] = None,
        network_update_settings: Optional[
            "capo_directory_service.types.network_update_settings.NetworkUpdateSettings"
        ] = None,
        create_snapshot_before_update: Optional[
            "capo_directory_service.types.create_snapshot_before_update.CreateSnapshotBeforeUpdate"
        ] = None,
    ) -> "capo_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult":
        """<p>Updates directory configuration for the specified update type.</p>

        Args:
            directory_id: <p>The identifier of the directory to update.</p>
            update_type: <p>The type of update to perform on the directory.</p>
            os_update_settings: <p>Operating system configuration to apply during the directory update operation.</p>
            directory_size_update_settings: <p>Directory size configuration to apply during the update operation.</p>
            network_update_settings: <p>Network configuration to apply during the directory update operation.</p>
            create_snapshot_before_update: <p>Specifies whether to create a directory snapshot before performing the update.</p>

        Raises:
            capo_directory_service.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_in_desired_state_exception.DirectoryInDesiredStateException: <p> The directory is already updated to desired update type settings. </p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.snapshot_limit_exceeded_exception.SnapshotLimitExceededException: <p>The maximum number of manual snapshots for the directory has been reached. You can use the <a>GetSnapshotLimits</a> operation to determine the snapshot limits for a directory.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_directory_setup_request.UpdateDirectorySetupRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_directory_setup_result.UpdateDirectorySetupResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_directory_setup

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_directory_setup.async_update_directory_setup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_directory_setup_request.UpdateDirectorySetupRequest = {
            "directory_id": directory_id,
            "update_type": update_type,
        }
        if os_update_settings is not None:
            input_["os_update_settings"] = os_update_settings
        if directory_size_update_settings is not None:
            input_["directory_size_update_settings"] = directory_size_update_settings
        if network_update_settings is not None:
            input_["network_update_settings"] = network_update_settings
        if create_snapshot_before_update is not None:
            input_["create_snapshot_before_update"] = create_snapshot_before_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_hybrid_ad(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        hybrid_administrator_account_update: Optional[
            "capo_directory_service.types.hybrid_administrator_account_update.HybridAdministratorAccountUpdate"
        ] = None,
        self_managed_instances_settings: Optional[
            "capo_directory_service.types.hybrid_customer_instances_settings.HybridCustomerInstancesSettings"
        ] = None,
    ) -> "capo_directory_service.types.update_hybrid_ad_result.UpdateHybridADResult":
        """<p>Updates the configuration of an existing hybrid directory. You can recover hybrid directory administrator account or modify self-managed instance settings.</p> <p>Updates are applied asynchronously. Use <a>DescribeHybridADUpdate</a> to monitor the progress of configuration changes.</p> <p>The <code>InstanceIds</code> must have a one-to-one correspondence with <code>CustomerDnsIps</code>, meaning that if the IP address for instance i-10243410 is 10.24.34.100 and the IP address for instance i-10243420 is 10.24.34.200, then the input arrays must maintain the same order relationship, either [10.24.34.100, 10.24.34.200] paired with [i-10243410, i-10243420] or [10.24.34.200, 10.24.34.100] paired with [i-10243420, i-10243410].</p> <note> <p>You must provide at least one update to <a>UpdateHybridADRequest$HybridAdministratorAccountUpdate</a> or <a>UpdateHybridADRequest$SelfManagedInstancesSettings</a>.</p> </note>

        Args:
            directory_id: <p>The identifier of the hybrid directory to update.</p>
            hybrid_administrator_account_update: <p>We create a hybrid directory administrator account when we create a hybrid directory. Use <code>HybridAdministratorAccountUpdate</code> to recover the hybrid directory administrator account if you have deleted it.</p> <p>To recover your hybrid directory administrator account, we need temporary access to a user in your self-managed AD with administrator permissions in the form of a secret from Amazon Web Services Secrets Manager. We use these credentials once during recovery and don't store them.</p> <p>If your hybrid directory administrator account exists, then you don’t need to use <code>HybridAdministratorAccountUpdate</code>, even if you have updated your self-managed AD administrator user.</p>
            self_managed_instances_settings: <p>Updates to the self-managed AD configuration, including DNS server IP addresses and Amazon Web Services System Manager managed node identifiers.</p>

        Raises:
            capo_directory_service.errors.ad_assessment_limit_exceeded_exception.ADAssessmentLimitExceededException: <p>A directory assessment is automatically created when you create a hybrid directory. There are two types of assessments: <code>CUSTOMER</code> and <code>SYSTEM</code>. Your Amazon Web Services account has a limit of 100 <code>CUSTOMER</code> directory assessments.</p> <p>If you attempt to create a hybrid directory; and you already have 100 <code>CUSTOMER</code> directory assessments;, you will encounter an error. Delete assessments to free up capacity before trying again.</p> <p>You can request an increase to your <code>CUSTOMER</code> directory assessment quota by contacting customer support or delete existing CUSTOMER directory assessments; to free up capacity.</p>
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_hybrid_ad_request.UpdateHybridADRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_hybrid_ad_result.UpdateHybridADResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_hybrid_ad

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_hybrid_ad.async_update_hybrid_ad(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_hybrid_ad_request.UpdateHybridADRequest = {
            "directory_id": directory_id
        }
        if hybrid_administrator_account_update is not None:
            input_["hybrid_administrator_account_update"] = (
                hybrid_administrator_account_update
            )
        if self_managed_instances_settings is not None:
            input_["self_managed_instances_settings"] = self_managed_instances_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_number_of_domain_controllers(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        desired_number: "capo_directory_service.types.desired_number_of_domain_controllers.DesiredNumberOfDomainControllers",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.update_number_of_domain_controllers_result.UpdateNumberOfDomainControllersResult":
        """<p>Adds or removes domain controllers to or from the directory. Based on the difference between current value and new value (provided through this API call), domain controllers will be added or removed. It may take up to 45 minutes for any new domain controllers to become fully active once the requested number of domain controllers is updated. During this time, you cannot make another update request.</p>

        Args:
            directory_id: <p>Identifier of the directory to which the domain controllers will be added or removed.</p>
            desired_number: <p>The number of domain controllers desired in the directory.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.domain_controller_limit_exceeded_exception.DomainControllerLimitExceededException: <p>The maximum allowed number of domain controllers per directory was exceeded. The default limit per directory is 20 domain controllers.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_number_of_domain_controllers_request.UpdateNumberOfDomainControllersRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_number_of_domain_controllers_result.UpdateNumberOfDomainControllersResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_number_of_domain_controllers

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_number_of_domain_controllers.async_update_number_of_domain_controllers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_number_of_domain_controllers_request.UpdateNumberOfDomainControllersRequest = {
            "directory_id": directory_id,
            "desired_number": desired_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_radius(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        radius_settings: "capo_directory_service.types.radius_settings.RadiusSettings",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.update_radius_result.UpdateRadiusResult":
        """<p>Updates the Remote Authentication Dial In User Service (RADIUS) server information for an AD Connector or Microsoft AD directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to update the RADIUS server information.</p>
            radius_settings: <p>A <a>RadiusSettings</a> object that contains information about the RADIUS server.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update Radius
            The following example updates the Remote Authentication Dial In User Service (RADIUS) server settings for an AD Connector directory.

            >>> await client.update_radius(directory_id='d-92654abfed', radius_settings={'DisplayLabel': 'MyRadius', 'UseSameUsername': True, 'RadiusTimeout': 1, 'AuthenticationProtocol': 'PAP', 'RadiusPort': 1027, 'RadiusRetries': 1, 'SharedSecret': '12345678', 'RadiusServers': ['172.168.101.113']})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_radius_request.UpdateRadiusRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_radius_result.UpdateRadiusResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_radius

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_radius.async_update_radius(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_radius_request.UpdateRadiusRequest = {
            "directory_id": directory_id,
            "radius_settings": radius_settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_settings(
        self,
        directory_id: "capo_directory_service.types.directory_id.DirectoryId",
        settings: "capo_directory_service.types.settings.Settings",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.update_settings_result.UpdateSettingsResult":
        """<p>Updates the configurable settings for the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory for which to update settings.</p>
            settings: <p>The list of <a>Setting</a> objects.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.directory_does_not_exist_exception.DirectoryDoesNotExistException: <p>The specified directory does not exist in the system.</p>
            capo_directory_service.errors.directory_unavailable_exception.DirectoryUnavailableException: <p>The specified directory is unavailable.</p>
            capo_directory_service.errors.incompatible_settings_exception.IncompatibleSettingsException: <p>The specified directory setting is not compatible with other settings.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.unsupported_settings_exception.UnsupportedSettingsException: <p>The specified directory setting is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_settings_request.UpdateSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_settings_result.UpdateSettingsResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_settings

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_settings.async_update_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_settings_request.UpdateSettingsRequest = {
            "directory_id": directory_id,
            "settings": settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_trust(
        self,
        trust_id: "capo_directory_service.types.trust_id.TrustId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
        selective_auth: Optional[
            "capo_directory_service.types.selective_auth.SelectiveAuth"
        ] = None,
    ) -> "capo_directory_service.types.update_trust_result.UpdateTrustResult":
        """<p>Updates the trust that has been set up between your Managed Microsoft AD directory and an self-managed Active Directory.</p>

        Args:
            trust_id: <p>Identifier of the trust relationship.</p>
            selective_auth: <p>Updates selective authentication for the trust.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.update_trust_request.UpdateTrustRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.update_trust_result.UpdateTrustResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.update_trust

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.update_trust.async_update_trust(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.update_trust_request.UpdateTrustRequest = {
            "trust_id": trust_id
        }
        if selective_auth is not None:
            input_["selective_auth"] = selective_auth

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def verify_trust(
        self,
        trust_id: "capo_directory_service.types.trust_id.TrustId",
        *,
        config_overrides: Optional[AsyncDirectoryServiceClientConfig] = None,
    ) -> "capo_directory_service.types.verify_trust_result.VerifyTrustResult":
        """<p>Directory Service for Microsoft Active Directory allows you to configure and verify trust relationships.</p> <p>This action verifies a trust relationship between your Managed Microsoft AD directory and an external domain.</p>

        Args:
            trust_id: <p>The unique Trust ID of the trust relationship to verify.</p>

        Raises:
            capo_directory_service.errors.client_exception.ClientException: <p>A client exception has occurred.</p>
            capo_directory_service.errors.entity_does_not_exist_exception.EntityDoesNotExistException: <p>The specified entity could not be found.</p>
            capo_directory_service.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_directory_service.errors.service_exception.ServiceException: <p>An exception has occurred in Directory Service.</p>
            capo_directory_service.errors.unsupported_operation_exception.UnsupportedOperationException: <p>The operation is not supported.</p>
            capo_directory_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To verify a trust
            The following example verifies a trust relationship between your Microsoft AD in the AWS cloud and an external domain.

            >>> await client.verify_trust(trust_id='t-9267353df0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_directory_service.types.verify_trust_request.VerifyTrustRequest]",
        ) -> AsyncOperationResponse[
            "capo_directory_service.types.verify_trust_result.VerifyTrustResult"
        ]:
            import capo_directory_service._operations.directory_service_20150416.verify_trust

            (
                output,
                http_response,
            ) = await capo_directory_service._operations.directory_service_20150416.verify_trust.async_verify_trust(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_directory_service.types.verify_trust_request.VerifyTrustRequest = {
            "trust_id": trust_id
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
